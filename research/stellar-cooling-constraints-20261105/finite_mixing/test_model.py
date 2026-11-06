import math
import unittest

from finite_mixing.model import muon_couplings, neutrino_couplings


class FiniteMixingCouplingTests(unittest.TestCase):
    def test_zero_angle_is_pure_axial_endpoint(self):
        gx = 0.13
        c = muon_couplings(gx, 0.0)
        self.assertEqual(c.g_vector, 0.0)
        self.assertAlmostEqual(c.g_axial, -gx, places=15)
        self.assertAlmostEqual(c.g_left, gx, places=15)
        self.assertAlmostEqual(c.g_right, -gx, places=15)
        self.assertAlmostEqual(c.code_axial_minus_gamma5_coefficient, gx, places=15)

    def test_pi_over_two_is_pure_vector_endpoint(self):
        gx = 0.13
        c = muon_couplings(gx, math.pi / 2.0)
        self.assertAlmostEqual(c.g_vector, gx, places=15)
        self.assertAlmostEqual(c.g_axial, 0.0, places=15)
        self.assertAlmostEqual(c.g_left, gx, places=15)
        self.assertAlmostEqual(c.g_right, gx, places=15)
        self.assertEqual(c.code_axial_minus_gamma5_coefficient, 0.0)

    def test_small_angle_ratio_and_uv_benchmark(self):
        theta = 1.0e-2
        c = muon_couplings(0.1, theta)
        self.assertAlmostEqual(
            c.abs_vector_to_axial_ratio, math.tan(theta) ** 2, places=15
        )
        self.assertAlmostEqual(c.abs_vector_to_axial_ratio, 1.0000666704446414e-4,
                               delta=1.0e-15)
        self.assertAlmostEqual(c.g_left, 0.1, places=15)

    def test_neutrino_couplings_are_independent_of_mixing_angle(self):
        self.assertEqual(neutrino_couplings(0.1), (0.1, -0.1))
        self.assertEqual(neutrino_couplings(0.0), (0.0, -0.0))

    def test_invalid_inputs_are_rejected(self):
        for gx, theta in [(-1.0, 0.1), (float("nan"), 0.1),
                          (0.1, -0.1), (0.1, math.pi / 2.0 + 1e-6)]:
            with self.subTest(gx=gx, theta=theta):
                with self.assertRaises(ValueError):
                    muon_couplings(gx, theta)


if __name__ == "__main__":
    unittest.main()
