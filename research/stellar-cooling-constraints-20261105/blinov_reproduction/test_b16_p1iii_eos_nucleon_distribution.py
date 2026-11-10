import math
import unittest

import numpy as np
from scipy.special import expit

from audit_b16_p1iii_eos_nucleon_distribution import (
    HBARC_MEV_FM,
    NucleonEOSState,
    aggregate_profile_rows,
    candidate_state_from_hs_spp,
    degeneracy_factor,
    degeneracy_factor_from_density_derivative,
    kinetic_energy_mev,
    number_density_fm3,
    occupation,
    phase_space_integrals,
)


class TestGarchingEOSNucleonDistribution(unittest.TestCase):
    def test_kinetic_energy_matches_relativistic_definition(self):
        p = np.array([0.0, 10.0, 100.0, 500.0])
        mstar = 650.0
        expected = np.sqrt(p * p + mstar * mstar) - mstar
        np.testing.assert_allclose(
            kinetic_energy_mev(p, mstar), expected, rtol=0.0, atol=1e-13
        )

    def test_occupation_is_bounded(self):
        state = NucleonEOSState("n", 5.0, 650.0, -20.0, 70.0)
        f = occupation(np.linspace(0.0, 1500.0, 101), state)
        self.assertTrue(np.all(f >= 0.0))
        self.assertTrue(np.all(f <= 1.0))

    def test_common_shift_of_U_and_mu_star_leaves_distribution_unchanged(self):
        p = np.linspace(0.0, 1000.0, 101)
        state_a = NucleonEOSState("n", 5.0, 650.0, -20.0, 70.0)
        state_b = NucleonEOSState("n", 5.0, 650.0, 103.0, 193.0)
        np.testing.assert_allclose(
            occupation(p, state_a), occupation(p, state_b),
            rtol=0.0, atol=1e-15
        )
        self.assertAlmostEqual(
            degeneracy_factor(state_a), degeneracy_factor(state_b), places=14
        )

    def test_vacuum_mass_limit_matches_total_chemical_potential_form(self):
        mass = 939.56542052
        temperature = 3.03
        mu_total = 935.0
        state = NucleonEOSState(
            "n", temperature, mass, 0.0, mu_total - mass
        )
        p = np.linspace(0.0, 1000.0, 101)
        expected = expit(
            (mu_total - np.sqrt(p * p + mass * mass)) / temperature
        )
        np.testing.assert_allclose(
            occupation(p, state), expected, rtol=0.0, atol=1e-15
        )

    def test_direct_degeneracy_equals_density_derivative(self):
        states = (
            NucleonEOSState("n", 3.03, 650.0, -45.0, 38.0),
            NucleonEOSState("p", 3.03, 648.706667, -40.0, 25.0),
            NucleonEOSState("n", 12.0, 700.0, -25.0, 18.0),
            NucleonEOSState("p", 12.0, 698.706667, -20.0, 8.0),
        )
        for state in states:
            direct = degeneracy_factor(state, order=512)
            derivative = degeneracy_factor_from_density_derivative(
                state, order=512
            )
            self.assertLess(abs(direct - derivative), 2.0e-9)

    def test_dilute_boltzmann_limit_is_one(self):
        state = NucleonEOSState("n", 10.0, 700.0, 25.0, -975.0)
        self.assertAlmostEqual(degeneracy_factor(state), 1.0, places=12)

    def test_quadrature_convergence(self):
        state = NucleonEOSState("n", 3.03, 650.0, -45.0, 38.0)
        f256 = degeneracy_factor(state, order=256)
        f512 = degeneracy_factor(state, order=512)
        self.assertLess(abs(f256 - f512), 1.0e-10)

    def test_density_units_and_spin_factor(self):
        state = NucleonEOSState("n", 8.0, 650.0, -25.0, 30.0)
        n_mev3, blocked_mev3 = phase_space_integrals(state, order=512)
        self.assertGreater(n_mev3, 0.0)
        self.assertGreater(blocked_mev3, 0.0)
        self.assertAlmostEqual(
            number_density_fm3(state, order=512),
            n_mev3 / HBARC_MEV_FM**3,
            places=15,
        )

    def test_profile_weightings_use_cell_measure_and_correct_powers(self):
        rows = [
            {
                "T_MeV": 4.0, "rho_g_cm3": 1.0e14, "dMdt_weight": 2.0, "xi": 0.82,
                "mstar_n_MeV": 700.0, "U_n_MeV": -30.0,
                "mu_star_n_MeV": 50.0,
                "mstar_p_MeV": 698.706667, "U_p_MeV": -20.0,
                "mu_star_p_MeV": 35.0,
            },
            {
                "T_MeV": 8.0, "rho_g_cm3": 2.0e14, "dMdt_weight": 1.0, "xi": 0.73,
                "mstar_n_MeV": 650.0, "U_n_MeV": -25.0,
                "mu_star_n_MeV": 30.0,
                "mstar_p_MeV": 648.706667, "U_p_MeV": -15.0,
                "mu_star_p_MeV": 18.0,
            },
        ]
        result = aggregate_profile_rows(rows, order=128)
        local = result["local_rows"]
        for species in ("p", "n"):
            w_t3 = [
                2.0 * 4.0**3,
                1.0 * 8.0**3,
            ]
            w_rho_t52 = [
                2.0 * 1.0e14 * 4.0**2.5,
                1.0 * 2.0e14 * 8.0**2.5,
            ]
            expected_t3 = sum(
                w * row["Fdeg"][species] for w, row in zip(w_t3, local)
            ) / sum(w_t3)
            expected_rho_t52 = sum(
                w * row["Fdeg"][species]
                for w, row in zip(w_rho_t52, local)
            ) / sum(w_rho_t52)
            self.assertAlmostEqual(
                result["global_averages"]["T3"][species],
                expected_t3, places=14
            )
            self.assertAlmostEqual(
                result["global_averages"]["rhoT52"][species],
                expected_rho_t52, places=14
            )
        self.assertLess(
            result["max_effective_mass_splitting_residual_MeV"], 1e-10
        )
        for source_row, local_row in zip(rows, local):
            for species in ("p", "n"):
                self.assertAlmostEqual(
                    local_row["n_actual_fm3"][species],
                    source_row["xi"] * local_row["nprime_fm3"][species],
                    places=14,
                )

    def test_hs_spp_mapping_reproduces_rmF_single_particle_energy(self):
        for species, m_vac in (("n", 939.565346), ("p", 938.272013)):
            mstar = 690.0 if species == "n" else 688.706667
            sigma_v = 115.0 if species == "n" else 104.0
            mu_nonrel = 35.0 if species == "n" else 20.0
            state = candidate_state_from_hs_spp(
                species, 5.0, mstar, sigma_v, mu_nonrel
            )
            p = np.linspace(0.0, 800.0, 101)
            lhs = (
                state.scalar_potential_mev
                + kinetic_energy_mev(p, mstar)
                - state.chemical_potential_star_mev
            )
            rhs = (
                np.sqrt(p*p + mstar*mstar)
                + sigma_v
                - (mu_nonrel + m_vac)
            )
            np.testing.assert_allclose(lhs, rhs, rtol=0.0, atol=2e-13)

    def test_invalid_state_is_rejected(self):
        with self.assertRaises(ValueError):
            degeneracy_factor(
                NucleonEOSState("x", 3.0, 600.0, 0.0, 10.0)
            )
        with self.assertRaises(ValueError):
            degeneracy_factor(
                NucleonEOSState("n", 0.0, 600.0, 0.0, 10.0)
            )


if __name__ == "__main__":
    unittest.main()
