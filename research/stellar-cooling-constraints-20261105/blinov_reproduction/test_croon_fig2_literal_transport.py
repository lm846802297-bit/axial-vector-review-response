import unittest
from pathlib import Path

import numpy as np

from croon_fig2_literal_transport import (
    CROON_MASSES_MEV,
    CROON_RAFFELT_ERG_PER_S,
    M_MU_MEV,
    KM_TO_MEV_INV,
    bose_factor,
    compute_benchmark,
    croon_local_rates_per_g2,
    energy_quadrature,
    load_and_sample_profile,
    luminosity_curve,
    muon_susceptibility,
    outer_vacuum_tau_per_g2,
    phase_space_weight,
    thin_channel_fractions,
)

PROFILE = Path(__file__).resolve().parents[1] / "data" / "sfho188_digitized.csv"


class CroonFig2LiteralTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile_01 = load_and_sample_profile(PROFILE, radial_step_km=0.1)
        cls.profile_005 = load_and_sample_profile(PROFILE, radial_step_km=0.05)

    def test_neutrinosphere_is_temperature_three_mev(self):
        self.assertAlmostEqual(self.profile_005["rnu_km"], 25.1511683, places=5)
        self.assertAlmostEqual(self.profile_005["temperature_mev"][-1], 3.0, places=10)

    def test_croon_phase_space_contains_energy_weight_once(self):
        omega = np.array([12.0, 20.0, 50.0])
        mass = 10.0
        expected = np.sqrt(omega**2 - mass**2) * omega**2 / (2*np.pi**2)
        np.testing.assert_allclose(phase_space_weight(omega, mass), expected, rtol=1e-14)

    def test_detailed_balance_identity(self):
        omega = np.array([12.0, 20.0, 50.0])
        temperature = np.array([3.0, 10.0, 20.0])
        bose = bose_factor(omega, temperature)
        ratio = (1.0 + bose) / bose
        np.testing.assert_allclose(ratio, np.exp(omega/temperature), rtol=2e-14)

    def test_printed_croon_local_rate_formulas(self):
        mass = 10.0
        omega = np.array([20.0, 30.0, 50.0])
        temperature = np.array([20.0, 25.0])
        chi = np.array([100.0, 200.0])
        rates = croon_local_rates_per_g2(mass, omega, temperature, chi)
        bose = 1.0 / np.expm1(omega[None, :] / temperature[:, None])
        velocity = np.sqrt(1.0 - (mass/omega)**2)
        expected_nu = mass**2/(12*np.pi*omega[None, :])*bose
        expected_sc = (2/137.035999084/(3*M_MU_MEV**2)
                       * chi[:, None]*velocity[None, :]*bose)
        np.testing.assert_allclose(rates["neutrino_production_per_g2"], expected_nu)
        np.testing.assert_allclose(rates["semi_compton_production_per_g2"], expected_sc)

    def test_outer_vacuum_decay_tail_is_nonzero_and_linear_in_path(self):
        omega = np.array([12.0, 20.0, 50.0])
        m = 10.0
        rnu = self.profile_005["rnu_km"]
        tau = outer_vacuum_tau_per_g2(m, omega, rnu, 100.0)
        expected = (100.0-rnu)*KM_TO_MEV_INV*m*m/(12*np.pi*omega)
        np.testing.assert_allclose(tau, expected, rtol=1e-14)
        self.assertTrue(np.all(tau > 0.0))
        self.assertTrue(np.all(outer_vacuum_tau_per_g2(m, omega, rnu, rnu) == 0.0))

    def test_thin_luminosity_scales_as_g_squared(self):
        couplings = np.array([1.0e-11, 2.0e-11])
        luminosity = luminosity_curve(
            10.0, couplings, self.profile_01, rfar_km=100.0, energy_order=64
        )
        self.assertAlmostEqual(
            luminosity[1]/luminosity[0], 4.0, delta=2.0e-5
        )

    def test_outer_vacuum_tail_reduces_finite_coupling_luminosity(self):
        g = np.array([1.0e-8])
        rnu = self.profile_01["rnu_km"]
        with_tail = luminosity_curve(
            10.0, g, self.profile_01, rfar_km=100.0, energy_order=64
        )[0]
        without_tail = luminosity_curve(
            10.0, g, self.profile_01, rfar_km=rnu, energy_order=64
        )[0]
        self.assertLess(with_tail, without_tail)

    def test_radial_step_convergence_at_ten_mev(self):
        g = np.array([1.0e-8])
        coarse = luminosity_curve(
            10.0, g, self.profile_01, rfar_km=100.0, energy_order=64
        )[0]
        fine = luminosity_curve(
            10.0, g, self.profile_005, rfar_km=100.0, energy_order=64
        )[0]
        self.assertLess(abs(coarse/fine - 1.0), 5.0e-3)

    def test_channel_dominance_matches_the_published_regime_description(self):
        low = thin_channel_fractions(1.0e-7, self.profile_01, energy_order=64)
        high = thin_channel_fractions(200.0, self.profile_01, energy_order=64)
        self.assertGreater(low["semi_compton_fraction"], 0.999)
        self.assertGreater(high["neutrino_fraction"], 0.99)

    def test_figure_two_mass_set_stays_below_dimuon_threshold(self):
        self.assertLess(max(CROON_MASSES_MEV.values()), 2.0*M_MU_MEV)
        self.assertEqual(CROON_RAFFELT_ERG_PER_S, 3.0e52)

    def test_muon_susceptibility_is_positive_and_finite(self):
        chi = muon_susceptibility(
            np.array([20.0, 39.0, 3.0]),
            np.array([46.0, 98.0, 0.0]),
            order=128,
        )
        self.assertTrue(np.all(np.isfinite(chi)))
        self.assertTrue(np.all(chi > 0.0))


if __name__ == "__main__":
    unittest.main()
