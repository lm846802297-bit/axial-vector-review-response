import unittest

from higgs_signal_strength_screen import (
    BENCHMARKS,
    M_H_GEV,
    gamma_scalar_to_aprime_pair,
    screen_point,
)


class HiggsSignalStrengthScreenTests(unittest.TestCase):
    def test_aprime_pair_threshold_for_benchmark_b(self):
        benchmark_b = BENCHMARKS[1]
        self.assertEqual(
            gamma_scalar_to_aprime_pair(
                M_H_GEV, benchmark_b.m_aprime_GeV, benchmark_b.vs_GeV
            ),
            0.0,
        )

    def test_open_aprime_pair_width_matches_response_scale(self):
        benchmark_a = BENCHMARKS[0]
        width = gamma_scalar_to_aprime_pair(
            M_H_GEV, benchmark_a.m_aprime_GeV, benchmark_a.vs_GeV
        )
        self.assertGreater(width, 3.7)
        self.assertLess(width, 3.8)

    def test_near_degeneracy_is_not_given_a_physical_mixing_proxy(self):
        benchmark_b = BENCHMARKS[1]
        result = screen_point(M_H_GEV, benchmark_b)
        self.assertIn("unclassified_near_degeneracy", result["status"])
        self.assertIsNone(result["mixing_proxy"])
        self.assertIsNone(result["mu_visible_proxy"])

    def test_h_to_ss_open_region_is_left_unclassified(self):
        benchmark_a = BENCHMARKS[0]
        result = screen_point(M_H_GEV / 2.0 - 0.1, benchmark_a)
        self.assertIn("h_to_ss_kinematically_open", result["status"])
        self.assertIsNone(result["mu_visible_proxy"])

    def test_off_degeneracy_screen_is_tiny_and_not_an_exclusion(self):
        benchmark_a, benchmark_b = BENCHMARKS
        result_a = screen_point(100.0, benchmark_a)
        result_b = screen_point(100.0, benchmark_b)
        self.assertLess(result_a["delta_mu_visible_proxy"], 1e-4)
        self.assertLess(result_b["delta_mu_visible_proxy"], 1e-6)
        self.assertIn("screen_only", result_a["status"])
        self.assertNotIn("excluded", result_a["status"])

    def test_benchmark_a_higgs_exotic_branching_proxy_is_small_away_from_degeneracy(self):
        benchmark_a = BENCHMARKS[0]
        low = screen_point(65.0, benchmark_a)
        high = screen_point(115.0, benchmark_a)
        self.assertGreater(low["br_h_to_aprime_pair_proxy"], 1.0e-6)
        self.assertLess(low["br_h_to_aprime_pair_proxy"], 2.0e-6)
        self.assertGreater(high["br_h_to_aprime_pair_proxy"], 2.0e-5)
        self.assertLess(high["br_h_to_aprime_pair_proxy"], 3.5e-5)
        self.assertAlmostEqual(
            high["br_h_to_4mu_proxy"],
            high["br_h_to_aprime_pair_proxy"] / 9.0,
            delta=1.0e-12,
        )

    def test_benchmark_a_accounts_for_open_higgs_to_aprime_pair(self):
        benchmark_a, benchmark_b = BENCHMARKS
        result_a = screen_point(120.0, benchmark_a)
        result_b = screen_point(120.0, benchmark_b)
        self.assertGreater(result_a["gamma_h_to_aprime_pair_GeV"], 0.0)
        self.assertEqual(result_b["gamma_h_to_aprime_pair_GeV"], 0.0)
        self.assertGreater(
            result_a["delta_mu_visible_proxy"],
            result_b["delta_mu_visible_proxy"],
        )


if __name__ == "__main__":
    unittest.main()
