import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import local_rates
from blinov_reproduction.audit_b16_inner_path_channel_directional import (
    analytic_ray_shell_columns,
    direction_binned_radial_columns,
)
from blinov_reproduction.audit_b16_outer_shell_polarization_resolved import (
    mode_neutrino_rates,
)


class B16OuterShellPolarizationResolvedTests(unittest.TestCase):
    def setUp(self):
        self.mass = 10.0
        self.energies = np.array([12.0, 20.0, 50.0])
        self.temperature = np.array([3.2, 3.5])
        self.mu_numu = np.array([0.0, 0.0])

    def test_mode_sum_and_detailed_balance_close_to_scalar_reference(self):
        production_modes, absorption_modes = mode_neutrino_rates(
            self.mass, self.energies, self.temperature, self.mu_numu, order=48
        )
        scalar = local_rates(
            self.mass,
            self.energies[None, :],
            self.temperature[:, None],
            self.mu_numu[:, None],
            np.zeros((len(self.temperature), 1)),
        )
        np.testing.assert_allclose(
            np.sum(production_modes, axis=-1),
            scalar["neutrino_production"],
            rtol=2e-12,
            atol=1e-300,
        )
        x = self.energies[None, :] / self.temperature[:, None]
        np.testing.assert_allclose(
            production_modes,
            np.exp(-x)[..., None] * absorption_modes,
            rtol=2e-12,
            atol=1e-300,
        )
        reduced_modes = -np.expm1(-x)[..., None] * absorption_modes
        reduced_scalar = np.expm1(x) * scalar["neutrino_production"]
        np.testing.assert_allclose(
            np.sum(reduced_modes, axis=-1),
            reduced_scalar,
            rtol=2e-12,
            atol=1e-300,
        )

    def test_transverse_modes_are_equal_when_mu_numu_is_zero(self):
        production_modes, absorption_modes = mode_neutrino_rates(
            self.mass, self.energies, self.temperature, self.mu_numu, order=48
        )
        np.testing.assert_allclose(
            production_modes[..., 1], production_modes[..., 2],
            rtol=2e-13, atol=1e-300,
        )
        np.testing.assert_allclose(
            absorption_modes[..., 1], absorption_modes[..., 2],
            rtol=2e-13, atol=1e-300,
        )

    def test_outer_shell_mode_columns_sum_to_scalar_column(self):
        radial_grid = np.array([0.0, 22.0, 23.0, 24.0, 25.0])
        energies = self.energies
        source_radii = np.array([8.0, 12.0, 15.0])
        modes = {
            "L": np.tile(np.array([0.0, 0.20, 0.23, 0.25, 0.27])[:, None], (1, len(energies))),
            "plus": np.tile(np.array([0.0, 0.18, 0.21, 0.23, 0.25])[:, None], (1, len(energies))),
            "minus": np.tile(np.array([0.0, 0.18, 0.21, 0.23, 0.25])[:, None], (1, len(energies))),
        }
        compton = np.tile(np.array([0.0, 1e-8, 8e-9, 6e-9, 4e-9])[:, None], (1, len(energies)))
        scalar = {
            "scalar": modes["L"] + modes["plus"] + modes["minus"] + compton
        }
        mode_columns, angles, weights, bins = direction_binned_radial_columns(
            source_radii, radial_grid, modes, self.mass, energies,
            25.0, per_bin_order=8,
        )
        compton_columns, _, _, _ = direction_binned_radial_columns(
            source_radii, radial_grid, {"compton": compton}, self.mass,
            energies, 25.0, per_bin_order=8,
        )
        scalar_columns, _, _, _ = direction_binned_radial_columns(
            source_radii, radial_grid, scalar, self.mass, energies,
            25.0, per_bin_order=8,
        )
        summed = np.sum(mode_columns[:, -1], axis=0) + compton_columns[0, -1]
        np.testing.assert_allclose(
            summed, scalar_columns[0, -1], rtol=3e-13, atol=1e-10
        )
        self.assertAlmostEqual(float(np.sum(weights)), 1.0, places=14)
        self.assertEqual(len(bins), len(angles))

    def test_outer_shell_column_is_invariant_under_direction_reversal(self):
        radial_grid = np.array([0.0, 22.0, 23.0, 24.0, 25.0])
        reduced = {
            "L": np.tile(np.array([0.0, 0.20, 0.23, 0.25, 0.27])[:, None], (1, len(self.energies))),
            "plus": np.tile(np.array([0.0, 0.18, 0.21, 0.23, 0.25])[:, None], (1, len(self.energies))),
            "minus": np.tile(np.array([0.0, 0.18, 0.21, 0.23, 0.25])[:, None], (1, len(self.energies))),
        }
        outward = analytic_ray_shell_columns(
            12.0, 0.6, radial_grid, reduced, self.mass,
            self.energies, 25.0,
        )
        inward = analytic_ray_shell_columns(
            12.0, -0.6, radial_grid, reduced, self.mass,
            self.energies, 25.0,
        )
        np.testing.assert_allclose(
            outward[:, -1, :], inward[:, -1, :],
            rtol=3e-13, atol=1e-10,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
