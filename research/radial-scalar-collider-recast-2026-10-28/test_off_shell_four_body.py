import unittest

from off_shell_four_body import fourbody_spectral_widths


class OffShellFourBodyTests(unittest.TestCase):
    def test_rejects_non_double_virtual_region(self):
        with self.assertRaises(ValueError):
            fourbody_spectral_widths(4.0, 3.9, 0.1)

    def test_widths_are_finite_positive_and_bounded(self):
        result = fourbody_spectral_widths(4.0, 5.0, 0.1, quadrature_order=96)
        self.assertGreater(result["total_diagonal_pairing_GeV"], 0.0)
        self.assertGreaterEqual(result["same_species_diagonal_GeV"], 0.0)
        self.assertGreaterEqual(result["distinct_species_GeV"], 0.0)
        self.assertGreaterEqual(
            result["identical_exchange_cauchy_upper_bound_GeV"],
            result["total_diagonal_pairing_GeV"],
        )
        self.assertFalse(result["identical_flavor_exchange_explicitly_integrated"])

    def test_gX_sixth_power_scaling_without_offshell_width_insertion(self):
        a = fourbody_spectral_widths(4.0, 5.0, 0.05, quadrature_order=64)
        b = fourbody_spectral_widths(4.0, 5.0, 0.1, quadrature_order=64)
        self.assertAlmostEqual(
            b["total_diagonal_pairing_GeV"] / a["total_diagonal_pairing_GeV"],
            64.0, places=9
        )

    def test_converges_for_near_threshold_grid_point(self):
        a = fourbody_spectral_widths(8.48750903116088, 8.633168407011583, 0.1,
                                     quadrature_order=96)
        b = fourbody_spectral_widths(8.48750903116088, 8.633168407011583, 0.1,
                                     quadrature_order=128)
        rel = abs(a["total_diagonal_pairing_GeV"] -
                  b["total_diagonal_pairing_GeV"]) / b["total_diagonal_pairing_GeV"]
        self.assertLess(rel, 0.002)

    def test_benchmark_fourbody_upper_bound_is_small(self):
        r = fourbody_spectral_widths(4.0, 5.0, 0.1, quadrature_order=96)
        self.assertLess(r["ratio_upper_over_diagonal"], 1.5)


if __name__ == "__main__":
    unittest.main()
