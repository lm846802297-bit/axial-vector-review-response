import unittest

from validate_b16_escape_phase_space_output import compare_joint_marginal


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


if __name__ == "__main__":
    unittest.main()
