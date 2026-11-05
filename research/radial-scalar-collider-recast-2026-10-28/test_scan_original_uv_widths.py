import unittest

from scan_original_uv_widths import evaluate_scan_point


class OriginalUVWidthScanTests(unittest.TestCase):
    def test_on_shell_AA_region_has_complete_declared_tree_level_width(self):
        p = evaluate_scan_point(4.0, 0.5, 0.1, 1e-2, 1e-2, 64, 1e-2)
        self.assertEqual(p["width_regime"], "on_shell_AA")
        self.assertTrue(p["branching_fractions_complete"])
        self.assertGreater(p["Gamma_A_A_on_shell_GeV"], 0.0)
        self.assertGreater(p["fraction_A_A_on_shell"], 0.0)

    def test_one_on_shell_one_virtual_region_includes_three_body(self):
        p = evaluate_scan_point(4.0, 2.1, 0.1, 1e-2, 1e-2, 64, 1e-2)
        self.assertEqual(p["width_regime"], "one_on_shell_one_virtual_A_three_body")
        self.assertTrue(p["branching_fractions_complete"])
        self.assertGreater(p["Gamma_A_nu_nu_mu_mu_tau_tau_three_body_GeV"], 0.0)

    def test_two_virtual_region_is_explicitly_incomplete(self):
        p = evaluate_scan_point(4.0, 5.0, 0.1, 1e-2, 1e-2, 64, 1e-2)
        self.assertEqual(p["width_regime"], "two_virtual_A_four_body_missing")
        self.assertFalse(p["branching_fractions_complete"])
        self.assertFalse(p["four_body_A_virtual_cascade_included"])

    def test_lambda_and_width_ratio_are_reported(self):
        p = evaluate_scan_point(4.0, 0.5, 0.1, 1e-2, 1e-2, 64, 1e-2)
        self.assertAlmostEqual(p["lambdaS"], 1.28)
        self.assertAlmostEqual(p["Gamma_s_over_ms"], 0.0252020078593, places=10)
        self.assertFalse(p["narrow_ratio_below_user_threshold"])

    def test_original_field_content_does_not_add_electron_yukawa(self):
        p = evaluate_scan_point(4.0, 5.0, 0.1, 1e-2, 1e-2, 64, 1e-2)
        self.assertNotIn("Gamma_ee_GeV", p)
        self.assertNotIn("fraction_ee", p)


if __name__ == "__main__":
    unittest.main()
