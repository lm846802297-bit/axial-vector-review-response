import sys
import unittest
from pathlib import Path

import numpy as np
from scipy.special import expit

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import (
    M_MU, compton_production, fermi_pair_average,
    negative_muon_density_and_degeneracy,
)
from blinov_reproduction.audit_b16_local_absorption import (
    direct_neutrino_modes,
    independent_b14_b16_compton,
    independent_muon_density_susceptibility,
)


class B16LocalAbsorptionTests(unittest.TestCase):
    def test_direct_B6_flavour_integral_matches_analytic_I(self):
        mass, omega, temperature = 10.0, 20.0, 24.0
        velocity = np.sqrt(1.0 - (mass / omega) ** 2)
        for mu in (-58.0, -2.0, 0.0, 45.0):
            production, _ = direct_neutrino_modes(
                mass, omega, temperature, mu, order=256
            )
            direct = float(np.sum(production))
            analytic = (
                mass**2 / (8.0 * np.pi * omega)
                * float(fermi_pair_average(mu, omega, temperature, velocity))
            )
            np.testing.assert_allclose(direct, analytic, rtol=3e-12, atol=1e-300)

    def test_direct_B10_absorption_and_B4_reduction(self):
        mass, omega, temperature, mu = 10.0, 30.0, 18.0, -20.0
        production, absorption = direct_neutrino_modes(
            mass, omega, temperature, mu, order=256
        )
        p, a = float(np.sum(production)), float(np.sum(absorption))
        np.testing.assert_allclose(
            p, np.exp(-omega / temperature) * a, rtol=3e-12, atol=1e-300
        )
        reduced_a = (1.0 - np.exp(-omega / temperature)) * a
        reduced_p = np.expm1(omega / temperature) * p
        np.testing.assert_allclose(reduced_a, reduced_p, rtol=3e-12, atol=1e-300)

    def test_B17_susceptibility_quadrature_converges(self):
        temperature, mu = 38.7430643817, 91.8049536968
        n128, chi128, f128 = independent_muon_density_susceptibility(
            temperature, mu, 128
        )
        n256, chi256, f256 = independent_muon_density_susceptibility(
            temperature, mu, 256
        )
        n512, chi512, f512 = independent_muon_density_susceptibility(
            temperature, mu, 512
        )
        np.testing.assert_allclose(n128, n256, rtol=2e-12)
        np.testing.assert_allclose(chi128, chi256, rtol=2e-12)
        np.testing.assert_allclose(n256, n512, rtol=2e-12)
        np.testing.assert_allclose(chi256, chi512, rtol=2e-12)
        np.testing.assert_allclose(n256 * f256, chi256, rtol=2e-14)

    def test_reference_muon_integral_resolves_dilute_outer_tail(self):
        for temperature in (3.384020032, 3.216426215, 3.033770692):
            density, fdeg = negative_muon_density_and_degeneracy(
                np.array([temperature]), np.array([0.0])
            )
            n_ind, chi_ind, _ = independent_muon_density_susceptibility(
                temperature, 0.0, 256
            )
            np.testing.assert_allclose(density[0], n_ind, rtol=3e-9)
            np.testing.assert_allclose(density[0] * fdeg[0], chi_ind, rtol=3e-9)

    def test_B14_B16_direct_rate_matches_reference_compton_kernel(self):
        mass, omega, temperature, mu = 10.0, 15.0, 38.7430643817, 91.8049536968
        n, chi, fdeg = independent_muon_density_susceptibility(temperature, mu, 256)
        direct = independent_b14_b16_compton(mass, omega, temperature, chi)
        reference = float(compton_production(mass, omega, temperature, n, fdeg))
        np.testing.assert_allclose(
            direct["production_B16_MeV_per_g2"], reference, rtol=3e-12
        )
        np.testing.assert_allclose(
            direct["reduced_B4_from_absorption_MeV_per_g2"],
            direct["reduced_closed_form_MeV_per_g2"],
            rtol=3e-12,
        )

    def test_B19_pointwise_Compton_statistical_identity(self):
        temperature, mu = 25.0, 70.0
        omega, photon_energy, initial_muon_energy = 20.0, 35.0, 130.0
        final_muon_energy = initial_muon_energy + photon_energy - omega
        f_initial = expit((mu - initial_muon_energy) / temperature)
        f_final = expit((mu - final_muon_energy) / temperature)
        bose = 1.0 / np.expm1(photon_energy / temperature)
        production_stat = f_initial * (1.0 - f_final) * bose
        absorption_stat = f_final * (1.0 - f_initial) * (1.0 + bose)
        np.testing.assert_allclose(
            production_stat / absorption_stat,
            np.exp(-omega / temperature),
            rtol=3e-14,
        )

    def test_10MeV_dimuon_channel_is_kinematically_closed(self):
        self.assertLess(10.0, 2.0 * M_MU)


if __name__ == "__main__":
    unittest.main(verbosity=2)
