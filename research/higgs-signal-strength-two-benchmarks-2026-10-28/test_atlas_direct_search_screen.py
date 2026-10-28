import unittest

from atlas_direct_search_screen import (
    ATLAS_GLOBAL_MIN_OBSERVED_LIMIT_FB,
    M_H_GEV,
    gamma_scalar_to_aprime_pair,
    screen_point,
)


class ATLASDirectSearchScreenTests(unittest.TestCase):
    def test_channel_threshold(self):
        self.assertEqual(gamma_scalar_to_aprime_pair(126.0), 0.0)
        self.assertGreater(gamma_scalar_to_aprime_pair(150.0), 0.0)

    def test_screen_uses_documented_first_high_mass_mc_point(self):
        result = screen_point(150.0)
        self.assertAlmostEqual(result.mixing_proxy, 1.4154213e-5, delta=2e-12)
        self.assertAlmostEqual(
            result.sigma_production_upper_fb, 1.0017087e-5, delta=2e-9
        )
        self.assertAlmostEqual(
            result.gamma_s_to_aprime_pair_GeV, 0.12259434, delta=1e-7
        )

    def test_production_upper_bound_is_below_global_best_limit_scale(self):
        result = screen_point(150.0)
        self.assertGreater(
            ATLAS_GLOBAL_MIN_OBSERVED_LIMIT_FB / result.sigma_production_upper_fb,
            4.9e3,
        )
        self.assertLess(result.sigma_4mu_upper_fb, result.sigma_production_upper_fb)

    def test_non_degenerate_proxy_rejects_exact_degeneracy(self):
        with self.assertRaises(ValueError):
            screen_point(M_H_GEV)


if __name__ == "__main__":
    unittest.main()
