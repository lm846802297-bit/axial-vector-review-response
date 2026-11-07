import unittest

import numpy as np

from rates import M_MU
from finite_mixing.thermal_integrals.dimuon import dimuon_thermal_integral


class DimuonThermalIntegralTests(unittest.TestCase):
    def test_channel_is_exactly_closed_at_and_below_threshold(self):
        for mass in (2*M_MU-1e-6, 2*M_MU):
            out = dimuon_thermal_integral(mass, 30.0, 80.0, 0.2, 0.8)
            np.testing.assert_array_equal(out["Q_by_mode"], np.zeros(3))
            np.testing.assert_array_equal(out["absorption_number_by_mode"], np.zeros(3))
            self.assertEqual(out["momentum"].size, 0)

    def test_production_absorption_detailed_balance_pointwise(self):
        out = dimuon_thermal_integral(300.0, 30.0, 80.0, 1e-4, 1.0, order=64)
        ratio = np.exp(-out["energy"] / 30.0)[:, None] * out["absorption_spectrum"]
        np.testing.assert_allclose(out["production_spectrum"], ratio, rtol=3e-11, atol=1e-300)

    def test_pure_vector_and_axial_are_nonzero_above_threshold(self):
        vector = dimuon_thermal_integral(300.0, 30.0, 80.0, 1.0, 0.0, order=64)
        axial = dimuon_thermal_integral(300.0, 30.0, 80.0, 0.0, 1.0, order=64)
        self.assertTrue(np.all(vector["Q_by_mode"] > 0))
        self.assertTrue(np.all(axial["Q_by_mode"] > 0))
        self.assertFalse(np.allclose(vector["Q_by_mode"], axial["Q_by_mode"]))

    def test_mixed_result_is_positive_and_finite(self):
        out = dimuon_thermal_integral(500.0, 35.0, 75.0, 1e-4, 1.0, order=64)
        self.assertTrue(np.all(np.isfinite(out["Q_by_mode"])))
        self.assertTrue(np.all(out["Q_by_mode"] > 0))
        self.assertTrue(np.all(out["absorption_number_by_mode"] > 0))


    def test_near_threshold_vector_axial_ratio_is_stable(self):
        # Summing all three polarizations removes the angular-distribution
        # dependence; the thermal ratio then follows the vacuum-width ratio.
        for delta in (1e-4, 1e-8, 1e-12):
            mass = 2*M_MU*(1.0 + delta)
            vector = dimuon_thermal_integral(
                mass, 30.0, 80.0, 1.0, 0.0, order=128
            )
            axial = dimuon_thermal_integral(
                mass, 30.0, 80.0, 0.0, 1.0, order=128
            )
            beta2 = 1.0 - 4.0*M_MU*M_MU/(mass*mass)
            expected = beta2/(1.0 + 2.0*M_MU*M_MU/(mass*mass))
            observed = np.sum(axial["Q_by_mode"])/np.sum(vector["Q_by_mode"])
            self.assertTrue(np.all(np.isfinite(vector["Q_by_mode"])))
            self.assertTrue(np.all(np.isfinite(axial["Q_by_mode"])))
            self.assertTrue(np.all(vector["Q_by_mode"] > 0.0))
            self.assertTrue(np.all(axial["Q_by_mode"] > 0.0))
            self.assertAlmostEqual(observed/expected, 1.0, delta=2e-8)

    def test_quadrature_convergence_64_128_and_128_192(self):
        q64 = dimuon_thermal_integral(
            300.0, 30.0, 80.0, 0.0, 1.0, order=64
        )["Q_by_mode"]
        q128 = dimuon_thermal_integral(
            300.0, 30.0, 80.0, 0.0, 1.0, order=128
        )["Q_by_mode"]
        q192 = dimuon_thermal_integral(
            300.0, 30.0, 80.0, 0.0, 1.0, order=192
        )["Q_by_mode"]
        np.testing.assert_allclose(q64, q128, rtol=3e-3, atol=0.0)
        np.testing.assert_allclose(q128, q192, rtol=3e-5, atol=0.0)

    def test_momentum_quadrature_converges(self):
        lo = dimuon_thermal_integral(300.0, 30.0, 80.0, 0.0, 1.0, order=64)
        hi = dimuon_thermal_integral(300.0, 30.0, 80.0, 0.0, 1.0, order=128)
        np.testing.assert_allclose(lo["Q_by_mode"], hi["Q_by_mode"], rtol=3e-3, atol=0.0)


if __name__ == "__main__":
    unittest.main()
