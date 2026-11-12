"""Regression tests for the archived-curve coupling-rescaling audit."""
import unittest
from run import log_interpolate, run_audit

class RescalingAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_audit()

    def test_log_log_interpolation(self):
        self.assertAlmostEqual(
            log_interpolate(4.0, [1.0, 2.0, 4.0, 8.0], [3.0, 12.0, 48.0, 192.0]),
            48.0,
        )

    def test_10_mev_fig7_can_be_locally_aligned_but_not_globally_normalized(self):
        ten = self.report["literal_blinov_scalar"]["per_mass"]["10"]
        fit = ten["best_fit"]
        self.assertAlmostEqual(fit["kappa"], 1.06675, delta=0.001)
        self.assertLess(fit["metrics"]["mean_abs_relative_residual_pct"], 4.0)
        self.assertLess(fit["metrics"]["max_abs_relative_residual_pct"], 8.0)
        self.assertGreater(ten["baseline_all_points"]["mean_abs_relative_residual_pct"], 10.0)
        self.assertGreater(ten["baseline_all_points"]["max_abs_relative_residual_pct"], 80.0)

    def test_no_single_kappa_reconciles_all_literal_fig7_masses(self):
        global_fit = self.report["literal_blinov_scalar"]["global_fit"]
        self.assertAlmostEqual(global_fit["kappa"], 1.03, delta=0.002)
        self.assertGreater(global_fit["metrics"]["max_abs_relative_residual_pct"], 40.0)

    def test_fig4_10_mev_boundary_match_is_damaged_by_fig7_masswise_rescaling(self):
        row = next(
            item for item in self.report["fig4_boundary_cross_check"]
            if item["mass_MeV"] == 10.0
        )
        unscaled = row["unscaled_boundary_deviation_pct"]
        masswise = row["masswise_rescaled_boundary_deviation_pct"]
        self.assertLess(abs(unscaled["lower"]), 1.1)
        self.assertLess(abs(unscaled["upper"]), 1.1)
        self.assertLess(masswise["lower_pct"], -5.0)
        self.assertLess(masswise["upper_pct"], -5.0)

    def test_mode_resolved_curve_is_not_fixed_by_a_near_unity_rescaling(self):
        result = self.report["production_mode_resolved_vector_control"]
        self.assertTrue(result["global_fit"]["fit_at_search_boundary"])
        self.assertGreater(
            result["global_fit"]["metrics"]["mean_abs_relative_residual_pct"], 100.0
        )

    def test_fixed_overlap_counts_prevent_endpoint_loss_bias(self):
        counts = self.report["literal_blinov_scalar"]["fixed_fit_point_counts"]
        self.assertEqual(counts, {"1": 32, "10": 25, "200": 12})
        mode_counts = self.report["production_mode_resolved_vector_control"]["fixed_fit_point_counts"]
        self.assertEqual(mode_counts, {"1": 30, "10": 23, "200": 10})

if __name__ == "__main__":
    unittest.main(verbosity=2)
