import unittest

import numpy as np

from rates import M_MU
from thermal_integrals.dimuon import dimuon_thermal_integral


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

    def test_momentum_quadrature_converges(self):
        lo = dimuon_thermal_integral(300.0, 30.0, 80.0, 0.0, 1.0, order=64)
        hi = dimuon_thermal_integral(300.0, 30.0, 80.0, 0.0, 1.0, order=128)
        np.testing.assert_allclose(lo["Q_by_mode"], hi["Q_by_mode"], rtol=3e-3, atol=0.0)


if __name__ == "__main__":
    unittest.main()
