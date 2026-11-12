import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import (
    radial_rule, local_rates, fermi_pair_average
)
from blinov_reproduction.audit_b16_neutrino_flavour_opacity import (
    flavour_rate_arrays, fake_flavour_rates,
)
from blinov_reproduction.audit_b16_shell_luminosity_sensitivity import (
    shell_columns_by_channel,
)


class B16NeutrinoFlavourOpacityTests(unittest.TestCase):
    def test_mu_and_tau_flavours_reconstruct_total_neutrino_rate(self):
        mass = 10.0
        energies = np.array([15.0, 20.0, 30.0])
        profile = {
            "T": np.array([15.0, 10.0, 5.0]),
            "mu_numu": np.array([5.0, 1.0, 0.0]),
            "mu_mu": np.array([60.0, 30.0, 10.0]),
        }
        mu, tau = flavour_rate_arrays(mass, energies, profile)
        total = local_rates(
            mass, energies[None,:], profile["T"][:,None],
            profile["mu_numu"][:,None], profile["mu_mu"][:,None]
        )["neutrino_production"]
        np.testing.assert_allclose(mu+tau, total, rtol=2e-13, atol=1e-300)

    def test_mu_and_tau_rates_are_equal_when_muon_neutrino_chemical_potential_is_zero(self):
        mass = 10.0
        energies = np.array([15.0, 20.0, 30.0])
        profile = {
            "T": np.array([15.0, 10.0, 5.0]),
            "mu_numu": np.zeros(3),
        }
        mu, tau = flavour_rate_arrays(mass, energies, profile)
        np.testing.assert_allclose(mu, tau, rtol=0, atol=0)

    def test_tau_flavour_remains_when_muon_neutrino_chemical_potential_is_zero(self):
        mass = 10.0
        energies = np.array([15.0, 20.0, 30.0])
        profile = {
            "T": np.array([15.0, 10.0, 5.0]),
            "mu_numu": np.zeros(3),
        }
        mu, tau = flavour_rate_arrays(mass, energies, profile)
        self.assertGreater(float(np.sum(tau)), 0.0)
        np.testing.assert_allclose(mu, tau, rtol=0, atol=0)

    def test_shell_columns_of_each_flavour_are_nonnegative(self):
        mass = 10.0
        radius = 25.0
        r, _ = radial_rule(radius, 8)
        radial_grid = np.unique(np.r_[0.0, r, radius])
        temperature = np.full(len(radial_grid), 20.0)
        mu_numu = np.zeros(len(radial_grid))
        energies = np.array([15.0, 20.0, 30.0, 50.0])
        profile = {"T": temperature, "mu_numu": mu_numu}
        mu, tau = flavour_rate_arrays(mass, energies, profile)
        for production in (mu, tau):
            rates = fake_flavour_rates(production, temperature, energies)
            result = shell_columns_by_channel(
                r, radial_grid, temperature, rates, mass, energies,
                radius, angular_order=8, path_order=16
            )
            self.assertTrue(np.all(result["columns_total"] >= 0.0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
