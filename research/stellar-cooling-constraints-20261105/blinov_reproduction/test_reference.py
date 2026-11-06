import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from vector_reference import summed_decay_production, thomson_absorption_modes
from blinov_reproduction.reference import (
    M_MU, compton_production, decay_production, fermi_pair_average,
    negative_muon_density_and_degeneracy, scalar_optical_depths,
)


class BlinovReferenceTests(unittest.TestCase):
    def test_fermi_pair_rest_limit(self):
        mu, omega, temp = 35.0, 80.0, 22.0
        expected = (1.0 / (1.0 + np.exp(-(mu - omega / 2) / temp))
                    * 1.0 / (1.0 + np.exp(-(-mu - omega / 2) / temp)))
        actual = fermi_pair_average(mu, omega, temp, 0.0)
        self.assertAlmostEqual(float(actual), float(expected), places=13)

    def test_decay_rates_match_archived_independent_spin_sum(self):
        points = [
            (1.0, 1.8, 24.0, -40.0, 50.0),
            (10.0, 18.0, 24.0, -20.0, 70.0),
            (100.0, 180.0, 24.0, 0.0, 100.0),
            (220.0, 396.0, 24.0, 25.0, 120.0),
            (300.0, 540.0, 24.0, 0.0, 0.0),
        ]
        for mass, omega, temp, mu_nu, mu_mu in points:
            nu, mm = decay_production(mass, omega, temp, mu_nu, mu_mu)
            ref_nu, ref_mm = summed_decay_production(
                mass, omega, temp, mu_nu, mu_mu)
            self.assertAlmostEqual(float(nu + mm), float(ref_nu + ref_mm),
                                   delta=max(abs(float(ref_nu + ref_mm))*3e-12, 1e-30))

    def test_dimuon_threshold_is_closed(self):
        masses = np.array([2.0 * M_MU - 1e-5, 2.0 * M_MU])
        energy = masses * 1.5
        nu, mm = decay_production(masses, energy, [20.0, 20.0],
                                  [0.0, 0.0], [100.0, 100.0])
        self.assertTrue(np.all(np.isfinite(nu)))
        np.testing.assert_array_equal(mm, np.zeros(2))

    def test_compton_rate_reduces_to_thomson_sum(self):
        mass, omega, temp = 1.0, 100.0, 25.0
        n_mu_fdeg = 3.2e-4
        fdeg = 0.73
        actual = compton_production(
            mass, omega, temp, n_mu_fdeg / fdeg, fdeg)
        expected_abs = np.sum(thomson_absorption_modes(
            mass, omega, temp, np.array(n_mu_fdeg)))
        expected_prod = np.exp(-omega / temp) * expected_abs
        np.testing.assert_allclose(actual, expected_prod, rtol=2e-13)

    def test_muon_density_and_degeneracy_are_finite(self):
        n, fdeg = negative_muon_density_and_degeneracy(
            np.array([10.0, 25.0]), np.array([45.0, 60.0]))
        self.assertTrue(np.all(n > 0))
        self.assertTrue(np.all((fdeg > 0) & (fdeg <= 1)))

    def test_constant_opacity_chord_column(self):
        radius = 10.0
        source_r = np.array([1e-9, 3.0])
        grid = np.array([0.0, 3.0, radius])
        energy = np.array([2.0])
        mass = 1.0
        gamma = 2.5e-12
        columns, weights = scalar_optical_depths(
            source_r, grid, np.full((3, 1), gamma), mass, energy,
            radius, angular_order=8, path_order=24)
        centre_tau = columns[0, :, 0]
        expected = gamma * radius * (1e18 / 197.3269804) / np.sqrt(1 - (mass / 2.0)**2)
        np.testing.assert_allclose(centre_tau, expected, rtol=2e-9)
        self.assertAlmostEqual(float(np.sum(weights)), 1.0, places=14)


if __name__ == "__main__":
    unittest.main()
