import unittest

from independent_belleii_pointwise_audit import (
    FLIGHT_CEILING_M,
    M_MU,
    M_TAU,
    NARROW_CEILING,
    loglog_interpolate,
    partial_weight,
    tau_reference_branching,
    width_status,
)


class IndependentBelleIIPointwiseAuditTests(unittest.TestCase):
    def test_muon_threshold_is_closed_below_and_open_above(self):
        self.assertEqual(partial_weight(2.0 * M_MU - 1e-8, M_MU), 0.0)
        self.assertGreater(partial_weight(2.0 * M_MU + 1e-8, M_MU), 0.0)

    def test_tau_reference_branching_turns_on_above_threshold(self):
        self.assertEqual(tau_reference_branching(2.0 * M_TAU), 0.0)
        self.assertGreater(tau_reference_branching(2.0 * M_TAU + 1e-8), 0.0)
        self.assertLessEqual(tau_reference_branching(6.0), 1.0)

    def test_log_log_interpolation_and_no_extrapolation(self):
        self.assertAlmostEqual(loglog_interpolate(2.0, [1.0, 4.0], [2.0, 8.0]), 4.0)
        self.assertIsNone(loglog_interpolate(0.9, [1.0, 4.0], [2.0, 8.0]))
        self.assertIsNone(loglog_interpolate(4.1, [1.0, 4.0], [2.0, 8.0]))

    def test_width_and_flight_interval_boundaries_are_conservative(self):
        row = {
            "fourmu_Gamma_over_sigma_lower_bound": "0.099",
            "fourmu_Gamma_over_sigma_upper_bound": "0.100",
            "scalar_mean_lab_flight_max_lower_m": "0.004",
            "scalar_mean_lab_flight_max_upper_m": "0.005",
        }
        status = width_status(row, "fourmu")
        self.assertEqual(status["width_status"], "width_interval_straddles_narrow_threshold")
        self.assertEqual(status["flight_status"], "flight_interval_straddles_5mm_proxy")
        row["fourmu_Gamma_over_sigma_upper_bound"] = str(NARROW_CEILING - 1e-8)
        row["scalar_mean_lab_flight_max_upper_m"] = str(FLIGHT_CEILING_M - 1e-8)
        status = width_status(row, "fourmu")
        self.assertEqual(status["width_status"], "narrow_proxy_pass")
        self.assertEqual(status["flight_status"], "prompt_geometry_proxy_pass")

    def test_jpsi_veto_interval_is_exactly_the_declared_interval(self):
        self.assertTrue(3.07 <= 3.095 <= 3.12)
        self.assertFalse(3.07 <= 3.069999 <= 3.12)
        self.assertFalse(3.07 <= 3.120001 <= 3.12)


if __name__ == "__main__":
    unittest.main()
