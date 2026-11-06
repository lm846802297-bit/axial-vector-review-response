"""Stage-1 regression tests for Blinov polarization-resolved detailed balance.

These tests do not change the production rate or transport implementation.
They verify the collision-integrand identity in B.19 using the actual
mode-resolved inverse-Compton matrix elements, and independently audit the
two-charge susceptibility convention used by transport.effective_muon_density.
"""
import unittest

import numpy as np
from numpy.testing import assert_allclose
from scipy.integrate import quad
from scipy.special import expit

import rates
import transport


class SemiComptonDetailedBalanceTests(unittest.TestCase):
    def test_b19_collision_integrand_balance_for_each_vector_mode(self):
        """Check B.19 pointwise with exact two-body recoil and both muon charges."""
        cases = [
            # mediator mass, energy, T, positive-muon chemical potential
            (10.0, 40.0, 25.0, 46.0),
            (100.0, 150.0, 30.0, 80.0),
            (200.0, 250.0, 35.0, 60.0),
        ]
        cosines = np.array([-0.8, -0.2, 0.35, 0.8])
        for mass, omega, temperature, mu_mu in cases:
            photon_energy, matrix_elements = rates.compton_matrix_elements(
                mass, [omega], cosines, current="vector"
            )
            photon_energy = photon_energy[0]
            # The inverse process has an initial muon at rest. Energy
            # conservation fixes the final muon energy for each angle.
            e_mu_initial = rates.M_MU
            e_mu_final = e_mu_initial + omega - photon_energy
            self.assertTrue(np.all(e_mu_final >= rates.M_MU))
            self.assertTrue(np.all(matrix_elements[0] >= 0.0))
            f_gamma = 1.0 / np.expm1(photon_energy / temperature)

            # sign=+1 is mu-, sign=-1 is mu+. The chemical potential changes
            # sign under charge conjugation.
            for charge_sign in (+1.0, -1.0):
                mu = charge_sign * mu_mu
                f_initial = expit((mu - e_mu_initial) / temperature)
                f_final = expit((mu - e_mu_final) / temperature)

                # Inverse absorption: V_h + mu -> gamma + mu.
                inverse_statistical_factor = (
                    f_initial * (1.0 - f_final) * (1.0 + f_gamma)
                )
                # Forward production: mu + gamma -> mu + V_h.
                forward_statistical_factor = (
                    f_final * (1.0 - f_initial) * f_gamma
                )

                # The same |M_h|^2 multiplies both collision terms. Check
                # each h=L,+,- and each scattering angle independently.
                inverse_integrand = matrix_elements[0] * inverse_statistical_factor[:, None]
                forward_integrand = matrix_elements[0] * forward_statistical_factor[:, None]
                assert_allclose(
                    forward_integrand,
                    np.exp(-omega / temperature) * inverse_integrand,
                    rtol=8e-13,
                    atol=0.0,
                )

    def test_compton_absorption_retains_three_incident_modes(self):
        """The inverse kernel returns one opacity for each incident V mode."""
        mass = 10.0
        energies = np.array([30.0, 60.0, 120.0])
        kernels = rates.compton_kernels(mass, energies, order=48, current="vector")
        opacity = rates.compton_absorption(kernels, temperature=25.0, n_mu_eff=1.0)
        self.assertEqual(opacity.shape, (len(energies), 3))
        self.assertTrue(np.all(np.isfinite(opacity)))
        self.assertTrue(np.all(opacity > 0.0))
        # At finite mass/energy the longitudinal Thomson-limit suppression
        # is not imposed by hand; it follows from the mode-resolved kernel.
        self.assertTrue(np.all(opacity[:, 0] < opacity[:, 1]))
        self.assertTrue(np.all(opacity[:, 0] < opacity[:, 2]))


class MuonSusceptibilityTests(unittest.TestCase):
    @staticmethod
    def _one_charge_susceptibility(temperature, chemical_potential):
        """2-spin susceptibility: 2 int d^3p/(2pi)^3 f(1-f)."""
        def integrand(momentum):
            energy = np.hypot(momentum, rates.M_MU)
            occupation = expit((chemical_potential - energy) / temperature)
            return momentum**2 * occupation * (1.0 - occupation)

        return quad(
            integrand, 0.0, np.inf, epsabs=1e-12, epsrel=2e-11, limit=300
        )[0] / np.pi**2

    def test_effective_density_matches_independent_two_charge_integral(self):
        """Check the current code's mu- plus mu+ susceptibility convention."""
        temperature = 19.26522111
        mu_mu = 46.67432845
        n_minus = self._one_charge_susceptibility(temperature, +mu_mu)
        n_plus = self._one_charge_susceptibility(temperature, -mu_mu)
        expected_both_charges = n_minus + n_plus
        implemented = transport.effective_muon_density(
            np.array([temperature]), np.array([mu_mu]), order=160
        )[0]
        assert_allclose(implemented, expected_both_charges, rtol=1e-5)
        self.assertGreater(n_plus, 0.0)
        self.assertGreater(n_minus, n_plus)
        assert_allclose(n_plus / n_minus, 8.08469548e-3, rtol=2e-7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
