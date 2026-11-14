import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"


def read(name):
    return json.loads((OUT / name).read_text(encoding="utf-8"))


def assert_relative(test, actual, expected, tolerance, label):
    if expected == 0.0:
        test.assertLessEqual(abs(actual), tolerance, label)
    else:
        test.assertLessEqual(abs(actual / expected - 1.0), tolerance, label)


class B16HighEnergyStrictNumpyReproductionTests(unittest.TestCase):
    def test_full_channel_resolved_calculation_matches_v8(self):
        numpy = read("b16_channel_resolved_energy_10mev_2026-11-15_numpy.json")
        v8 = read("b16_channel_resolved_energy_10mev_2026-11-10_v8.json")
        n, v = numpy["result"], v8["result"]

        self.assertTrue(numpy.get("script_sha256"))
        self.assertEqual(n["execution"]["engine"], "Python/NumPy/SciPy reference implementation")
        self.assertEqual(n["execution"]["profile_sha256"], v["execution"]["profile_sha256"])

        assert_relative(
            self, n["integrated"]["calculated_luminosity_erg_s"],
            v["integrated"]["calculated_luminosity_erg_s"], 2.0e-12,
            "B.1+B.2 luminosity"
        )
        assert_relative(
            self, n["integrated"]["escape_probability"],
            v["integrated"]["escape_probability"], 2.0e-12,
            "global escape probability"
        )
        assert_relative(
            self, n["opacity_decomposition"]["mean_tau_source_weighted"]["total"],
            v["opacity_decomposition"]["mean_tau_source_weighted"]["total"],
            2.0e-12, "source-weighted mean optical depth"
        )
        for channel in ("neutrino", "compton"):
            assert_relative(
                self,
                n["integrated"]["source_channel_luminosity_fractions"][channel],
                v["integrated"]["source_channel_fractions"][channel],
                2.0e-12, f"{channel} source fraction"
            )

    def test_36_ray_chord_convergence_matches_v8(self):
        numpy = read("b16_high_energy_nu_chord_convergence_10mev_2026-11-15_numpy.json")
        v8 = read("b16_high_energy_nu_chord_convergence_10mev_2026-11-10_v8.json")
        n = numpy["result"]["maximum_absolute_relative_refinement"]
        v = v8["result"]["maximum_absolute_relative_refinement"]
        mapping = {
            "path_32_to_64_at_opacity640": "path32_to64_at_opacity640",
            "path_64_to_128_at_opacity640": "path64_to128_at_opacity640",
            "path_128_to_256_at_opacity640": "path128_to256_at_opacity640",
            "opacity_320_to_640_at_path256": "opacity320_to640_at_path256",
            "opacity_640_to_1280_at_path256": "opacity640_to1280_at_path256",
        }
        for key, v8_key in mapping.items():
            assert_relative(self, n[key], v[v8_key], 2.0e-9, key)
        self.assertEqual(len(numpy["result"]["cases"]), 108)

    def test_outer_temperature_sensitivities_match_v8(self):
        numpy = read("b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-15_numpy.json")
        v8 = read("b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-10.json")
        nrows = {row["scenario"]: row for row in numpy["result"]["results"]}
        vrows = {row["scenario"]: row for row in v8["result"]["results"]}
        self.assertEqual(set(nrows), set(vrows))
        for scenario, n in nrows.items():
            v = vrows[scenario]
            for key in (
                "source_weight_per_g2", "escaped_weight_per_g2",
                "escape_probability", "mean_tau_source_weighted",
                "mean_tau_escape_weighted", "escape_luminosity_erg_s",
            ):
                assert_relative(self, n[key], v[key], 3.0e-7, f"{scenario}: {key}")
            self.assertLessEqual(
                abs(n["escaped_high_energy_ratio_vs_baseline"]
                    - v["escaped_high_energy_ratio_vs_baseline"]),
                3.0e-7,
                f"{scenario}: relative change vs baseline"
            )

    def test_global_path_redshift_bilinear_interpolation_matches_v8(self):
        numpy = read("b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-15_numpy.json")
        v8 = read("b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-10.json")
        n, v = numpy["result"], v8["result"]
        self.assertEqual(
            n["configuration"]["path_redshift_opacity_interpolation"],
            "bilinear in radius and local energy"
        )
        for label in ("fixed_omega", "path_redshift"):
            for key in (
                "source_per_g2", "escaped_per_g2", "escape_probability",
                "mean_tau_source_weighted", "mean_tau_escape_weighted",
                "nu_source_fraction", "compton_source_fraction",
                "nu_escaped_source_fraction", "compton_escaped_source_fraction",
                "escaped_luminosity_erg_s",
            ):
                assert_relative(self, n[label][key], v[label][key], 1.0e-12, f"{label}: {key}")
        for key in ("escaped_luminosity", "escape_probability", "mean_tau_source_weighted"):
            self.assertLessEqual(
                abs(n["relative_change"][key] - v["relative_change"][key]),
                1.0e-12, f"relative change: {key}"
            )
        for nbin, vbin in zip(n["sub_bands"], v["sub_bands"]):
            self.assertLessEqual(
                abs(nbin["relative_escaped_luminosity_change"]
                    - vbin["relative_escaped_luminosity_change"]),
                1.0e-12, nbin["bin"]
            )

    def test_direct_local_rate_method_is_kept_separate(self):
        numpy = read("b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-15_numpy.json")
        result = numpy["result"]
        delta = result["interpolation_sensitivity"][
            "direct_vs_bilinear_escaped_luminosity_relative_difference"
        ]
        self.assertGreater(delta, 0.004)
        self.assertLess(delta, 0.006)
        self.assertIn("not the bilinear opacity interpolation", result[
            "direct_local_rate_recomputation"
        ]["qualification"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
