import unittest

from audit_croon_antimuon_opacity_sensitivity import (
    DEFAULT_PROFILE,
    run_antimuon_sensitivity,
)


class CroonAntimuonOpacitySensitivityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_antimuon_sensitivity(
            profile_path=DEFAULT_PROFILE,
            couplings=[3.0e-2],
            energy_order=48,
            tau_grid_points=151,
            susceptibility_order=64,
        )

    def test_profile_and_charge_content_are_pinned(self):
        profile = self.result["profile"]
        self.assertEqual(
            profile["sha256"],
            "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c",
        )
        self.assertEqual(profile["rows"], 1687)
        self.assertGreater(profile["chi_edge_total_over_mu_minus"], 1.4)
        self.assertLess(profile["chi_edge_total_over_mu_minus"], 1.8)
        self.assertAlmostEqual(
            profile["chi_Rnu_total_over_mu_minus"], 2.0, delta=2e-3
        )

    def test_antimuon_extension_increases_outer_opacity_suppression(self):
        row = self.result["comparison"][0]
        self.assertGreater(
            row["mu_pm_Rnu_over_Tedge_ratio"],
            row["mu_minus_only_Rnu_over_Tedge_ratio"],
        )
        self.assertLess(row["mu_pm_Rnu_over_Tedge_ratio"], 1.1)

    def test_charge_conjugate_extension_does_not_close_published_gap(self):
        row = self.result["comparison"][0]
        self.assertGreater(row["mu_pm_gap_remaining"], 3.0)
        self.assertGreater(
            row["mu_pm_gap_remaining"],
            row["mu_minus_only_gap_remaining"],
        )

    def test_literal_croon_convention_is_retained(self):
        self.assertIn("single f_mu", self.result["reference_convention"])
        self.assertIn("not the literal", self.result["sensitivity_convention"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
