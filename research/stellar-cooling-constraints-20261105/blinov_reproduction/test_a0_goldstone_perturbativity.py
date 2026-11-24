import math
import unittest

from audit_a0_goldstone_perturbativity import (
    goldstone_yukawa,
    perturbative_gx_max,
)


class A0GoldstonePerturbativityTests(unittest.TestCase):
    def test_boundary_saturates_yukawa_perturbativity(self):
        for mass in (1.0e-7, 1.0e-6, 1.0e-5, 0.1, 10.0, 200.0):
            gx_max = perturbative_gx_max(mass)
            y_g = goldstone_yukawa(gx_max, mass)
            self.assertAlmostEqual(y_g * y_g / (4.0 * math.pi), 1.0, places=14)

    def test_perturbative_limit_scales_linearly_with_mediator_mass(self):
        self.assertAlmostEqual(
            perturbative_gx_max(10.0) / perturbative_gx_max(0.1),
            100.0,
            places=12,
        )

    def test_ten_mev_reference_value(self):
        self.assertAlmostEqual(
            perturbative_gx_max(10.0),
            0.167770051,
            delta=1.0e-9,
        )

    def test_two_hundred_mev_mass_covers_entire_gx_scan(self):
        self.assertGreater(perturbative_gx_max(200.0), 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
