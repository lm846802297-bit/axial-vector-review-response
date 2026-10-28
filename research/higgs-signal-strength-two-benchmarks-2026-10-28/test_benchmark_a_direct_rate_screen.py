import unittest

from benchmark_a_direct_rate_screen import (
    ATLAS_LOW_MASS_GLOBAL_MIN_LIMIT_FB,
    M_H_GEV,
    screen_point,
)


class BenchmarkADirectRateScreenTests(unittest.TestCase):
    def test_rate_increases_as_scalar_mass_approaches_higgs(self):
        low = screen_point(65.0)
        high = screen_point(110.0)
        self.assertLess(low.sigma_production_upper_fb, high.sigma_production_upper_fb)

    def test_conservative_production_envelope_is_below_published_limit_scale(self):
        for mass in (65.0, 80.0, 100.0, 110.0):
            result = screen_point(mass)
            self.assertLess(result.sigma_production_upper_fb, ATLAS_LOW_MASS_GLOBAL_MIN_LIMIT_FB)
            self.assertGreater(result.ratio_min_limit_to_inclusive_rate, 90.0)

    def test_four_muon_rate_is_one_ninth_of_production_upper_envelope(self):
        for mass in (65.0, 80.0, 100.0, 110.0):
            result = screen_point(mass)
            self.assertAlmostEqual(
                result.sigma_4mu_upper_fb,
                result.sigma_production_upper_fb / 9.0,
                delta=1e-15,
            )

    def test_non_degenerate_proxy_rejects_exact_degeneracy(self):
        with self.assertRaises(ValueError):
            screen_point(M_H_GEV)


if __name__ == "__main__":
    unittest.main()
