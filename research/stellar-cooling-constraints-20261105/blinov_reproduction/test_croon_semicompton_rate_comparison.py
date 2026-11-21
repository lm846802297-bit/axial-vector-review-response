import math
import unittest

from croon_semicompton_rate_comparison import (
    blinov_eq_b16_nr_rate,
    corrected_to_croon_ratio,
    croon_eq47_rate,
)


class CroonSemiComptonComparisonTests(unittest.TestCase):
    def test_published_formula_ratio(self):
        for ratio in (1.0e-3, 0.1, 0.5, 0.9):
            omega = 30.0
            mv = ratio * omega
            args = (mv, omega, 8.0, 1.7e-4, 0.73, 2.0e-8)
            croon = croon_eq47_rate(*args)
            corrected = blinov_eq_b16_nr_rate(*args)
            self.assertGreater(croon, 0.0)
            self.assertGreater(corrected, 0.0)
            self.assertAlmostEqual(
                corrected / croon,
                corrected_to_croon_ratio(mv, omega),
                delta=2.0e-14 * corrected_to_croon_ratio(mv, omega),
            )

    def test_small_mass_limit_ratio_tends_to_two(self):
        ratio = corrected_to_croon_ratio(1.0e-6, 10.0)
        self.assertAlmostEqual(ratio, 2.0, places=12)

    def test_coupling_scaling_is_quadratic(self):
        args = (0.2, 10.0, 5.0, 1.0e-5, 0.8)
        rate_g = croon_eq47_rate(*args, 1.0e-8)
        rate_2g = croon_eq47_rate(*args, 2.0e-8)
        self.assertAlmostEqual(rate_2g / rate_g, 4.0, places=13)

    def test_rejects_threshold_and_unphysical_inputs(self):
        with self.assertRaises(ValueError):
            croon_eq47_rate(10.0, 10.0, 5.0, 1.0, 1.0, 1.0e-8)
        with self.assertRaises(ValueError):
            blinov_eq_b16_nr_rate(10.0, 20.0, 5.0, -1.0, 1.0, 1.0e-8)

    def test_rate_ratio_is_not_a_constant_factor(self):
        low = corrected_to_croon_ratio(0.1, 10.0)
        near_threshold = corrected_to_croon_ratio(9.0, 10.0)
        self.assertGreater(near_threshold, low)
        self.assertTrue(math.isfinite(near_threshold))


if __name__ == "__main__":
    unittest.main()
