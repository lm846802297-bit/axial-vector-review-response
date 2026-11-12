import unittest

from independent_fourbody_tensor_audit import (
    independent_width,
    pointwise_tensor_checks,
)


class IndependentFourBodyTensorAuditTests(unittest.TestCase):
    def test_direct_lorentz_tensors_match_projector_contraction(self):
        result = pointwise_tensor_checks()
        self.assertEqual(result["samples"], 48)
        self.assertLess(result["max_relative_difference_direct_tensor_vs_projector"], 2e-10)

    def test_independent_integral_agrees_with_production_quadrature(self):
        from off_shell_four_body import fourbody_spectral_widths

        cases = (
            (4.0, 5.0, 0.1),
            (8.48750903116088, 8.633168407011583, 0.1),
            (4.0, 10.0, 0.07),
            (3.8, 4.2, 0.1),
        )
        for ms, m_a, g_x in cases:
            reference = independent_width(ms, m_a, g_x, 384)
            production = fourbody_spectral_widths(ms, m_a, g_x, quadrature_order=128)
            rel = abs(
                reference["diagonal_pairing_GeV"]
                - production["total_diagonal_pairing_GeV"]
            ) / reference["diagonal_pairing_GeV"]
            self.assertLess(rel, 2e-3)

    def test_independent_quadrature_convergence(self):
        low = independent_width(8.48750903116088, 8.633168407011583, 0.1, 128)
        high = independent_width(8.48750903116088, 8.633168407011583, 0.1, 512)
        rel = abs(low["diagonal_pairing_GeV"] - high["diagonal_pairing_GeV"]) / high["diagonal_pairing_GeV"]
        self.assertLess(rel, 2e-3)

    def test_exchange_bound_and_gx_sixth_power(self):
        a = independent_width(4.0, 5.0, 0.05, 96)
        b = independent_width(4.0, 5.0, 0.10, 96)
        self.assertAlmostEqual(
            b["diagonal_pairing_GeV"] / a["diagonal_pairing_GeV"],
            64.0, places=7,
        )
        self.assertGreaterEqual(
            a["identical_exchange_cauchy_upper_bound_GeV"],
            a["diagonal_pairing_GeV"],
        )
        self.assertGreaterEqual(a["distinct_species_GeV"], 0.0)
        self.assertGreaterEqual(a["same_species_diagonal_GeV"], 0.0)


if __name__ == "__main__":
    unittest.main()
