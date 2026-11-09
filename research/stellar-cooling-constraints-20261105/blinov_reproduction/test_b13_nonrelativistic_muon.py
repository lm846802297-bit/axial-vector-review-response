import unittest
import numpy as np

from audit_b13_nonrelativistic_muon import (
    integrate_range,
    muon_susceptibility_moments,
)


class MuonApproximationDiagnosticTests(unittest.TestCase):
    def test_integrate_range_linear_function(self):
        x = np.linspace(0.0, 10.0, 101)
        y = 2.0 * x
        self.assertAlmostEqual(integrate_range(x, y, 2.0, 8.0), 60.0, places=10)

    def test_susceptibility_velocity_moments_are_physical(self):
        moments = muon_susceptibility_moments(
            np.array([20.0, 35.0]),
            np.array([45.0, 100.0]),
            p_max=400.0,
            dp=0.5,
        )
        self.assertTrue(np.all(moments["chi_mu_MeV3"] > 0.0))
        self.assertTrue(np.all((moments["mean_v_chi"] > 0.0) & (moments["mean_v_chi"] < 1.0)))
        self.assertTrue(np.all((moments["rms_v_chi"] > 0.0) & (moments["rms_v_chi"] < 1.0)))
        self.assertTrue(np.all((moments["fraction_p_gt_m_chi"] >= 0.0) & (moments["fraction_p_gt_m_chi"] <= 1.0)))
        self.assertTrue(np.all((moments["fraction_v_gt_0p5_chi"] >= 0.0) & (moments["fraction_v_gt_0p5_chi"] <= 1.0)))


if __name__ == "__main__":
    unittest.main()
