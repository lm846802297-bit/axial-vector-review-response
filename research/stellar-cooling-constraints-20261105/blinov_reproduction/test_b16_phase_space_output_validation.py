import math
import tempfile
import unittest
from pathlib import Path

from validate_b16_escape_phase_space_output import compare_joint_marginal, load_json, validate


class JointMarginalValidationTests(unittest.TestCase):
    def test_omitted_zero_weight_partition_bin_is_accepted(self):
        joint = [
            {"energy_bin": "11-12 MeV", "thin_source_fraction_within_region": 0.4},
            {"energy_bin": "12-13 MeV", "thin_source_fraction_within_region": 0.6},
        ]
        partition = [
            {"bin": "10-11 MeV", "thin_source_fraction_within_region": 0.0},
            {"bin": "11-12 MeV", "thin_source_fraction_within_region": 0.4},
            {"bin": "12-13 MeV", "thin_source_fraction_within_region": 0.6},
        ]
        result = compare_joint_marginal(
            joint, partition, "energy_bin", "thin_source_fraction_within_region"
        )
        self.assertEqual(result["missing_zero_bins_omitted_from_joint"], ["10-11 MeV"])
        self.assertLess(result["max_absolute_residual"], 1e-15)

    def test_missing_nonzero_partition_bin_fails(self):
        joint = [
            {"energy_bin": "12-13 MeV", "thin_source_fraction_within_region": 1.0}
        ]
        partition = [
            {"bin": "11-12 MeV", "thin_source_fraction_within_region": 0.4},
            {"bin": "12-13 MeV", "thin_source_fraction_within_region": 0.6},
        ]
        with self.assertRaises(AssertionError):
            compare_joint_marginal(
                joint, partition, "energy_bin", "thin_source_fraction_within_region"
            )

    def test_unexpected_joint_bin_fails(self):
        joint = [
            {"energy_bin": "12-13 MeV", "thin_source_fraction_within_region": 1.0},
            {"energy_bin": "13-15 MeV", "thin_source_fraction_within_region": 0.0},
        ]
        partition = [
            {"bin": "12-13 MeV", "thin_source_fraction_within_region": 1.0}
        ]
        with self.assertRaises(AssertionError):
            compare_joint_marginal(
                joint, partition, "energy_bin", "thin_source_fraction_within_region"
            )




def minimal_valid_data():
    def make_region(name, source_fraction, escaped_fraction):
        shell, energy, direction = "8-10 km", "10-20 MeV", "-1-1 cos(theta)"
        cell = {
            "emission_shell": shell, "energy_bin": energy, "direction_bin": direction,
            "thin_source_fraction_within_region": 1.0,
            "escaped_luminosity_fraction_within_region": 1.0,
            "thin_source_fraction_of_global": source_fraction,
            "escaped_luminosity_fraction_of_global": escaped_fraction,
        }
        def rows(label):
            return [{"bin": label, "thin_source_fraction_within_region": 1.0,
                     "escaped_luminosity_fraction_within_region": 1.0}]
        return {
            "region": name, "source_fraction_of_global_B1": source_fraction,
            "escaped_luminosity_fraction_of_global": escaped_fraction,
            "source_weighted_escape_probability": 0.01,
            "emission_radius_bins": rows(shell), "energy_bins": rows(energy),
            "direction_bins_4": rows(direction), "direction_bins_8": rows(direction),
            "joint_bin_count_nonempty": 1, "joint_radius_energy_direction_bins": [cell],
        }
    return {
        "mass_MeV": 10.0, "coupling": 0.1, "calculated_luminosity_erg_s": 1.0,
        "optically_thin_luminosity_erg_s": 100.0, "reference_luminosity_erg_s": 0.5,
        "relative_difference_vs_fig7": 1.0, "escape_probability": 0.01,
        "baseline_json_sha256": "a" * 64, "fig7_reference_sha256": "b" * 64,
        "profile": {"sha256": "c" * 64},
        "closure": {
            "luminosity_relative_residual_vs_high_order_baseline": 0.0,
            "thin_luminosity_relative_residual_vs_high_order_baseline": 0.0,
            "escape_probability_absolute_residual_vs_high_order_baseline": 0.0,
        },
        "configuration": {
            "direction_weight_sum": 1.0, "direction_weight_closure_residual": 0.0,
            "source_grid_sha256": "d" * 64, "opacity_grid_sha256": "e" * 64,
            "energy_grid_sha256": "f" * 64, "source_radial_node_count": 200,
            "opacity_radial_node_count": 200, "energy_node_count": 842,
        },
        "source_channel_fractions": {"compton": 0.5, "neutrino": 0.5},
        "source_measure_metadata": {"radial_node_count": 200, "energy_node_count": 842},
        "regions": [make_region("all_emission_radii", 1.0, 1.0),
                    make_region("dominant_8_15km_emission", 0.8, 0.85)],
    }




def minimal_baseline(data):
    return {
        "result": {
            "mass_MeV": data["mass_MeV"],
            "configuration": dict(data["configuration"]),
            "profile": dict(data["profile"]),
            "eq_b2_fixed_omega_baseline": {
                "points": [{
                    "g": data["coupling"],
                    "calculated_luminosity_erg_s": data["calculated_luminosity_erg_s"],
                    "optically_thin_luminosity_erg_s": data["optically_thin_luminosity_erg_s"],
                    "escape_fraction": data["escape_probability"],
                    "reference_luminosity_erg_s": data["reference_luminosity_erg_s"],
                    "relative_difference": data["relative_difference_vs_fig7"],
                }]
            },
        }
    }


class StrictNumericValidationTests(unittest.TestCase):
    def test_valid_minimal_result_passes(self):
        self.assertEqual(validate(minimal_valid_data())["status"], "PASS")

    def test_nested_nan_fails(self):
        data = minimal_valid_data()
        data["regions"][0]["joint_radius_energy_direction_bins"][0]["tau"] = math.nan
        with self.assertRaisesRegex(AssertionError, "Non-finite numeric value"):
            validate(data)

    def test_positive_infinity_fails(self):
        data = minimal_valid_data()
        data["calculated_luminosity_erg_s"] = math.inf
        with self.assertRaisesRegex(AssertionError, "Non-finite numeric value"):
            validate(data)

    def test_negative_infinity_fails(self):
        data = minimal_valid_data()
        data["configuration"]["direction_weight_sum"] = -math.inf
        with self.assertRaisesRegex(AssertionError, "Non-finite numeric value"):
            validate(data)

    def test_json_loader_rejects_nan_and_infinities(self):
        for token in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(token=token), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "bad.json"
                path.write_text('{"x":' + token + '}', encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Non-standard non-finite"):
                    load_json(path)

    def test_fig7_ratio_mismatch_fails(self):
        data = minimal_valid_data()
        data["relative_difference_vs_fig7"] = 0.5
        with self.assertRaisesRegex(AssertionError, "inconsistent with calculated/reference"):
            validate(data)

    def test_escape_probability_mismatch_fails(self):
        data = minimal_valid_data()
        data["escape_probability"] = 0.02
        with self.assertRaisesRegex(AssertionError, "inconsistent with calculated/optically-thin"):
            validate(data)

    def test_negative_partition_fails(self):
        data = minimal_valid_data()
        data["regions"][0]["energy_bins"][0]["thin_source_fraction_within_region"] = -1.0
        with self.assertRaises(AssertionError):
            validate(data)

    def test_baseline_grid_mismatch_fails(self):
        data = minimal_valid_data()
        baseline = minimal_baseline(data)
        baseline["result"]["configuration"]["energy_grid_sha256"] = "0" * 64
        with self.assertRaisesRegex(AssertionError, "energy_grid_sha256 differs"):
            validate(data, baseline, baseline_sha256="a" * 64)

    def test_valid_result_matches_archived_baseline(self):
        data = minimal_valid_data()
        self.assertEqual(validate(data, minimal_baseline(data), baseline_sha256="a" * 64)["status"], "PASS")

    def test_baseline_hash_argument_required(self):
        data = minimal_valid_data()
        baseline = minimal_baseline(data)
        with self.assertRaisesRegex(AssertionError, "baseline_sha256 is required"):
            validate(data, baseline)

    def test_baseline_file_sha256_mismatch_fails(self):
        data = minimal_valid_data()
        baseline = minimal_baseline(data)
        with self.assertRaisesRegex(AssertionError, "does not match the supplied baseline file"):
            validate(data, baseline, baseline_sha256="c" * 64)

    def test_baseline_luminosity_mismatch_fails(self):
        data = minimal_valid_data()
        baseline = minimal_baseline(data)
        data["calculated_luminosity_erg_s"] = 1.1
        data["relative_difference_vs_fig7"] = 1.1 / data["reference_luminosity_erg_s"] - 1.0
        data["escape_probability"] = 1.1 / data["optically_thin_luminosity_erg_s"]
        with self.assertRaisesRegex(
            AssertionError, "luminosity_relative_residual_vs_high_order_baseline is inconsistent"
        ):
            validate(data, baseline, baseline_sha256="a" * 64)

    def test_baseline_thin_luminosity_mismatch_fails(self):
        data = minimal_valid_data()
        baseline = minimal_baseline(data)
        data["optically_thin_luminosity_erg_s"] = 110.0
        data["escape_probability"] = (
            data["calculated_luminosity_erg_s"] / data["optically_thin_luminosity_erg_s"]
        )
        with self.assertRaisesRegex(
            AssertionError, "thin_luminosity_relative_residual_vs_high_order_baseline is inconsistent"
        ):
            validate(data, baseline, baseline_sha256="a" * 64)

    def test_baseline_escape_probability_mismatch_fails(self):
        data = minimal_valid_data()
        baseline = minimal_baseline(data)
        baseline["result"]["eq_b2_fixed_omega_baseline"]["points"][0]["escape_fraction"] = 0.02
        with self.assertRaisesRegex(
            AssertionError, "escape_probability_absolute_residual_vs_high_order_baseline is inconsistent"
        ):
            validate(data, baseline, baseline_sha256="a" * 64)

    def test_missing_all_emission_region_fails(self):
        data = minimal_valid_data()
        data["regions"] = [data["regions"][1]]
        with self.assertRaisesRegex(AssertionError, "must contain exactly"):
            validate(data)

    def test_duplicate_region_name_fails(self):
        data = minimal_valid_data()
        data["regions"][1]["region"] = "all_emission_radii"
        with self.assertRaisesRegex(AssertionError, "Duplicate region names"):
            validate(data)

    def test_duplicate_partition_label_fails(self):
        rows = [{"bin":"x", "thin_source_fraction_within_region":0.5},
                {"bin":"x", "thin_source_fraction_within_region":0.5}]
        with self.assertRaisesRegex(AssertionError, "Duplicate"):
            compare_joint_marginal([], rows, "energy_bin", "thin_source_fraction_within_region")



    def test_joint_fraction_string_fails(self):
        data = minimal_valid_data()
        data["regions"][0]["joint_radius_energy_direction_bins"][0][
            "thin_source_fraction_within_region"
        ] = "1.0"
        with self.assertRaisesRegex(AssertionError, "must be a JSON number"):
            validate(data)

    def test_joint_fraction_boolean_fails(self):
        data = minimal_valid_data()
        data["regions"][0]["joint_radius_energy_direction_bins"][0][
            "thin_source_fraction_within_region"
        ] = True
        with self.assertRaisesRegex(AssertionError, "must be a JSON number"):
            validate(data)

    def test_joint_bin_count_boolean_fails(self):
        data = minimal_valid_data()
        data["regions"][0]["joint_bin_count_nonempty"] = True
        with self.assertRaisesRegex(AssertionError, "must be an integer"):
            validate(data)


if __name__ == "__main__":
    unittest.main()
