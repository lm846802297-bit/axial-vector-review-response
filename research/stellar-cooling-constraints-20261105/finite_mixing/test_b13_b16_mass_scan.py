import unittest

from finite_mixing.b13_b16_comparison import b14_b16_rate
from finite_mixing.b13_b16_mass_scan import (
    FIXED_OMEGA_POINTS_MEV,
    NEW_MASSES_MEV,
    REFERENCE_MASS_MEV,
    muon_kinematic_diagnostics,
)


class B13B16LowMassScanTests(unittest.TestCase):
    def test_mass_grid_targets_paper_low_mass_regime_and_keeps_10mev_reference(self):
        self.assertEqual(NEW_MASSES_MEV, (0.1, 0.3, 1.0, 3.0))
        self.assertEqual(REFERENCE_MASS_MEV, 10.0)
        self.assertTrue(all(0.0 < m < REFERENCE_MASS_MEV for m in NEW_MASSES_MEV))
        self.assertEqual(FIXED_OMEGA_POINTS_MEV, (15.0, 30.0, 50.0))

    def test_explicit_mass_correction_is_small_at_1mev_and_30mev(self):
        result = b14_b16_rate(
            mass=1.0, omega=30.0, temperature=20.0,
            n_mu_fdeg=1.0e4, include_mass_correction=True
        )
        self.assertAlmostEqual(result["mass_correction_factor"], 1.0005555555556, places=12)
        self.assertLess(result["mass_correction_factor"]-1.0, 6.0e-4)

    def test_massless_parenthesis_limit_has_no_longitudinal_piece(self):
        result = b14_b16_rate(
            mass=0.3, omega=30.0, temperature=20.0,
            n_mu_fdeg=1.0e4, include_mass_correction=True
        )
        self.assertGreater(result["B16_mode_rates_with_mass_correction_MeV"][0], 0.0)
        self.assertEqual(
            result["B16_mode_rates_without_parenthesis_correction_MeV"][0], 0.0
        )
        self.assertAlmostEqual(
            result["B16_total_with_mass_correction_MeV"]
            / result["B16_total_without_parenthesis_correction_MeV"],
            1.0 + 0.3**2/(2.0*30.0**2),
            places=13,
        )

    def test_b17_weighted_muon_kinematics_are_normalized(self):
        result = muon_kinematic_diagnostics(
            temperature=19.26522111, mu_mu=46.67432845, order=128
        )
        combined = result["species"]["combined"]
        self.assertGreater(combined["rms_velocity"], 0.0)
        self.assertLess(combined["rms_velocity"], 1.0)
        self.assertGreater(combined["mean_kinetic_energy_over_m"], 0.0)
        self.assertGreaterEqual(combined["fraction_p_over_m_below_0p3"], 0.0)
        self.assertLessEqual(combined["fraction_p_over_m_below_0p3"], 1.0)
        self.assertGreaterEqual(combined["fraction_p_over_m_below_0p5"], 0.0)
        self.assertLessEqual(combined["fraction_p_over_m_below_0p5"], 1.0)
        self.assertAlmostEqual(
            combined["B17_susceptibility_MeV3"],
            result["species"]["mu_minus"]["B17_susceptibility_MeV3"]
            + result["species"]["mu_plus"]["B17_susceptibility_MeV3"],
            places=10,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
