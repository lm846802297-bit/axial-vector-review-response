import math
import unittest

import numpy as np

from finite_mixing.b13_b16_comparison import (
    b14_b16_rate,
    muon_density_and_susceptibility,
)


class B13B16ComparisonTests(unittest.TestCase):
    def test_b16_spin_sum_matches_mode_sum(self):
        result = b14_b16_rate(
            mass=10.0, omega=30.0, temperature=20.0,
            n_mu_fdeg=1.25e4, include_mass_correction=True
        )
        self.assertLess(result["B16_sum_of_modes_relative_residual"], 2e-14)
        self.assertAlmostEqual(
            sum(result["B16_mode_rates_with_mass_correction_MeV"]),
            result["B16_total_with_mass_correction_MeV"],
            places=12,
        )

    def test_dropping_parenthesis_correction_removes_longitudinal_term(self):
        result = b14_b16_rate(
            mass=10.0, omega=30.0, temperature=20.0,
            n_mu_fdeg=1.25e4, include_mass_correction=True
        )
        corrected = result["B16_total_with_mass_correction_MeV"]
        no_correction = result["B16_total_without_parenthesis_correction_MeV"]
        expected = 1.0 + 10.0**2/(2.0*30.0**2)
        self.assertAlmostEqual(corrected/no_correction, expected, places=13)
        self.assertEqual(
            result["B16_mode_rates_without_parenthesis_correction_MeV"][0], 0.0
        )

    def test_b14_v_factor_cancels_against_b16_inverse_velocity(self):
        a = b14_b16_rate(
            mass=10.0, omega=15.0, temperature=20.0,
            n_mu_fdeg=2.0e3, include_mass_correction=True
        )
        b = b14_b16_rate(
            mass=10.0, omega=80.0, temperature=20.0,
            n_mu_fdeg=2.0e3, include_mass_correction=True
        )
        # After multiplying by the B.16 1/v_V factor, the rate's only
        # remaining omega dependence is the Bose factor and mass correction.
        self.assertGreater(a["v_V"], 0.0)
        self.assertGreater(b["v_V"], a["v_V"])
        self.assertGreater(a["B16_total_with_mass_correction_MeV"], 0.0)
        self.assertGreater(b["B16_total_with_mass_correction_MeV"], 0.0)

    def test_b17_charge_resolved_susceptibilities_are_positive_and_normalized(self):
        result = muon_density_and_susceptibility(19.26522111, 46.67432845, order=128)
        minus = result["species"]["mu_minus"]
        plus = result["species"]["mu_plus"]
        self.assertGreater(minus["number_density_MeV3"], 0.0)
        self.assertGreater(plus["number_density_MeV3"], 0.0)
        self.assertGreater(minus["susceptibility_nFdeg_MeV3"], 0.0)
        self.assertGreater(plus["susceptibility_nFdeg_MeV3"], 0.0)
        self.assertTrue(0.0 < minus["Fdeg"] <= 1.0)
        self.assertTrue(0.0 < plus["Fdeg"] <= 1.0)
        self.assertAlmostEqual(
            result["n_mu_Fdeg_total_MeV3"],
            minus["susceptibility_nFdeg_MeV3"] + plus["susceptibility_nFdeg_MeV3"],
            places=12,
        )
        self.assertGreaterEqual(result["positive_muon_fraction_of_susceptibility"], 0.0)
        self.assertLess(result["positive_muon_fraction_of_susceptibility"], 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
