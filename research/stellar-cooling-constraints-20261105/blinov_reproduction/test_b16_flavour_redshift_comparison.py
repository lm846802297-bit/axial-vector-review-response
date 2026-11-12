import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import (
    radial_rule, load_profile, local_rates, scalar_optical_depths,
)
from blinov_reproduction.audit_b16_global_redshift import (
    redshifted_scalar_optical_depths,
)
from blinov_reproduction.audit_b16_flavour_redshift_comparison import (
    _fixed_omega_shell_columns, redshifted_shell_columns_by_flavour,
    _single_channel_rates,
)
from blinov_reproduction.audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
from blinov_reproduction.audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel


class B16FlavourRedshiftComparisonTests(unittest.TestCase):
    def setUp(self):
        self.mass = 10.0
        self.radius = 25.0
        self.r, self.rw = radial_rule(self.radius, 8)
        self.radial_grid = np.unique(np.r_[0.0, self.r, self.radius])
        self.energies = np.array([12.0, 15.0, 20.0, 30.0, 50.0])
        self.profile = {
            "T": np.linspace(30.0, 4.0, len(self.radial_grid)),
            "mu_mu": np.linspace(70.0, 0.0, len(self.radial_grid)),
            "mu_numu": np.zeros(len(self.radial_grid)),
            "lapse": np.linspace(0.70, 0.95, len(self.radial_grid)),
        }

    def test_fixed_omega_flavour_sum_closes_to_direct_total(self):
        shells, angles, rates = _fixed_omega_shell_columns(
            self.r, self.radial_grid, self.profile, self.mass, self.energies,
            self.radius, 8, 16
        )
        direct, direct_angles = scalar_optical_depths(
            self.r, self.radial_grid, rates["reduced_absorption"],
            self.mass, self.energies, self.radius, 8, 16
        )
        summed = sum(np.sum(v, axis=0) for v in shells.values())
        np.testing.assert_allclose(angles, direct_angles, rtol=0, atol=1e-14)
        np.testing.assert_allclose(summed, direct, rtol=2e-10, atol=1e-300)

    def test_fixed_omega_mu_and_tau_flavours_equal_when_mu_numu_is_zero(self):
        shells, _, _ = _fixed_omega_shell_columns(
            self.r, self.radial_grid, self.profile, self.mass, self.energies,
            self.radius, 8, 16
        )
        np.testing.assert_allclose(
            shells["nu_mu"], shells["nu_tau"], rtol=2e-13, atol=1e-300
        )

    def test_redshift_flavour_shells_close_to_direct_total_on_escaping_bins(self):
        result = redshifted_shell_columns_by_flavour(
            self.r, self.radial_grid, self.profile, self.mass, self.energies,
            self.radius, 8, 16
        )
        summed = sum(result["channel_columns"].values())
        eligible = result["eligible_source_energy_mask"]
        direct, direct_angles, _ = redshifted_scalar_optical_depths(
            self.r, self.radial_grid, self.profile, self.mass, self.energies,
            self.radius, 8, 16
        )
        eligible_3d = np.broadcast_to(eligible[:, None, :], direct.shape)
        self.assertTrue(np.all(np.isfinite(summed[eligible_3d])))
        self.assertTrue(np.all(summed >= 0.0))
        np.testing.assert_allclose(result["angle_weights"], direct_angles, rtol=0, atol=1e-14)
        np.testing.assert_allclose(
            summed[eligible_3d], direct[eligible_3d], rtol=3e-10, atol=1e-300
        )
        np.testing.assert_allclose(
            result["channel_columns"]["nu_mu"],
            result["channel_columns"]["nu_tau"],
            rtol=2e-13, atol=1e-300
        )

    def test_non_escaping_modes_are_zero_in_removed_flavour_columns(self):
        profile = dict(self.profile)
        profile["lapse"] = np.linspace(0.60, 0.90, len(self.radial_grid))
        result = redshifted_shell_columns_by_flavour(
            self.r, self.radial_grid, profile, self.mass, self.energies,
            self.radius, 8, 16
        )
        ineligible = ~result["eligible_source_energy_mask"]
        for channel in ("nu_mu", "nu_tau", "compton", "dimuon"):
            values = result["channel_columns"][channel]
            ineligible_3d = np.broadcast_to(ineligible[:, None, :], values.shape)
            self.assertTrue(np.all(values[ineligible_3d] == 0.0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
