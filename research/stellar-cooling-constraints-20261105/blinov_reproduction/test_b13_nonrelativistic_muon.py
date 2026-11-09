ifrom blinov_reproduction.reference import (
    ALPHA,
    M_MU,
    compton_production,
    negative_muon_density_and_degeneracy,
)
mport unittest
import numpy as np

from audit_b13_nonrelativistic_muon import (
    integrate_range,
    muon_susceptibility_moments,
)


class MuonApproximationDiagnosticTests(unittest.TestCase):
    def test_b16_reduced_compton_opacity_cancels_bose_factor(self):
        mass = np.array([0.1, 1.0, 10.0])
        omega = np.array([5.0, 20.0, 50.0])
        temperature = np.array([5.0, 20.0, 40.0])
        mu_mu = np.array([10.0, 60.0, 100.0])
        n_mu, f_deg = negative_muon_density_and_degeneracy(temperature, mu_mu)
        production = compton_production(mass, omega, temperature, n_mu, f_deg)
        x = omega / temperature
        reduced = (1.0 - np.exp(-x)) * np.exp(x) * production
        alpha_v = 1.0 / (4.0 * np.pi)
        expected = (
            16.0 * np.pi * ALPHA * alpha_v / (3.0 * M_MU**2)
            * n_mu * f_deg * (1.0 + mass**2 / (2.0 * omega**2))
        )
        np.testing.assert_allclose(reduced, expected, rtol=2.0e-14, atol=0.0)

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
