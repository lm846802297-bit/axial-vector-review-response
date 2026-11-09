import unittest

from scan_original_uv_widths import evaluate_scan_point


class OriginalUVWidthScanTests(unittest.TestCase):
    def test_on_shell_AA_region(self):
        p = evaluate_scan_point(4.0, 0.5, 0.1, 1e-2, 1e-2, 64)
        self.assertEqual(p["width_regime"], "on_shell_AA")
        self.assertTrue(p["branching_fractions_exact_under_declared_benchmark"])
        self.assertFalse(p["branching_fractions_nontrivially_bounded_under_declared_benchmark"])
        self.assertAlmostEqual(p["BR_mu_mu_min"], p["BR_mu_mu_max"])
        self.assertGreater(p["Gamma_A_A_on_shell_GeV"], 0.0)

    def test_one_on_shell_one_virtual_region_includes_three_body(self):
        p = evaluate_scan_point(4.0, 2.1, 0.1, 1e-2, 1e-2, 64)
        self.assertEqual(p["width_regime"], "one_on_shell_one_virtual_A_three_body")
        self.assertTrue(p["branching_fractions_exact_under_declared_benchmark"])
        self.assertFalse(p["branching_fractions_nontrivially_bounded_under_declared_benchmark"])
        self.assertAlmostEqual(p["BR_mu_mu_min"], p["BR_mu_mu_max"])
        self.assertGreater(p["Gamma_A_nu_nu_mu_mu_tau_tau_three_body_GeV"], 0.0)

    def test_two_virtual_region_has_diagonal_and_exchange_bound(self):
        p = evaluate_scan_point(4.0, 5.0, 0.1, 1e-2, 1e-2, 64)
        self.assertEqual(p["width_regime"], "two_virtual_A_four_body_bounded")
        self.assertFalse(p["branching_fractions_exact_under_declared_benchmark"])
        self.assertTrue(p["branching_fractions_bounded_under_declared_benchmark"])
        self.assertTrue(p["branching_fractions_nontrivially_bounded_under_declared_benchmark"])
        self.assertLess(p["BR_mu_mu_min"], p["BR_mu_mu_max"])
        self.assertGreater(p["Gamma_Astar_Astar_four_fermion_diagonal_GeV"], 0.0)
        self.assertGreaterEqual(
            p["Gamma_4f_identical_exchange_upper_GeV"],
            p["Gamma_Astar_Astar_four_fermion_diagonal_GeV"],
        )

    def test_lambda_and_width_interval_are_reported(self):
        p = evaluate_scan_point(4.0, 0.5, 0.1, 1e-2, 1e-2, 64)
        self.assertAlmostEqual(p["lambdaS"], 1.28)
        self.assertGreaterEqual(p["Gamma_s_over_ms_upper_bound"],
                                p["Gamma_s_over_ms_lower_bound"])
        self.assertGreaterEqual(p["ctau_s_upper_bound_m"],
                                p["ctau_s_lower_bound_m"])

    def test_lambdaS_criterion_is_not_mistaken_for_full_perturbativity(self):
        p = evaluate_scan_point(0.212, 0.05, 0.1, 1e-2, 1e-2, 64)
        self.assertTrue(p["passes_lambdaS_le_4pi"])
        self.assertFalse(p["passes_scalar_yukawas_le_sqrt4pi"])
        self.assertFalse(p["passes_lambdaS_and_scalar_yukawas_le_4pi"])

    def test_original_field_content_does_not_add_electron_yukawa(self):
        p = evaluate_scan_point(4.0, 5.0, 0.1, 1e-2, 1e-2, 64)
        self.assertNotIn("Gamma_ee_GeV", p)
        self.assertNotIn("BR_ee_min", p)


if __name__ == "__main__":
    unittest.main()
