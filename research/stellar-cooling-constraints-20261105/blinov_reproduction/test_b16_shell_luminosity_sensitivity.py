import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import (
    radial_rule, load_profile, local_rates, scalar_optical_depths
)
from blinov_reproduction.audit_b16_shell_luminosity_sensitivity import (
    shell_columns_by_channel, log_escaped_integral, removal_diagnostic,
)


class B16ShellLuminositySensitivityTests(unittest.TestCase):
    def test_shell_columns_reconstruct_direct_columns_and_channels(self):
        mass = 10.0
        radius = 25.0
        r, _ = radial_rule(radius, 8)
        radial_grid = np.unique(np.r_[0.0, r, radius])
        profile = {
            "T": np.full(len(radial_grid), 20.0),
            "mu_mu": np.full(len(radial_grid), 55.0),
            "mu_numu": np.zeros(len(radial_grid)),
            "lapse": np.full(len(radial_grid), 0.80),
        }
        energies = np.array([15.0, 20.0, 30.0, 50.0])
        rates = local_rates(
            mass, energies[None,:], profile["T"][:,None],
            profile["mu_numu"][:,None], profile["mu_mu"][:,None]
        )
        result = shell_columns_by_channel(
            r, radial_grid, profile["T"], rates, mass, energies,
            radius, angular_order=8, path_order=16
        )
        self.assertLess(result["detailed_balance_channel_sum_relative_residual"], 2e-12)
        self.assertLess(result["angular_weight_relative_residual"], 1e-14)
        self.assertLess(result["shell_sum_to_direct_column_max_relative_residual"], 2e-10)

    def test_removing_all_opacity_recovers_optically_thin_integral(self):
        source = np.array([[1.0, 2.0], [3.0, 4.0]])
        angles = np.array([0.25, 0.75])
        columns = np.ones((2, 2, 2))*100.0
        g = 0.2
        base = log_escaped_integral(source, angles, columns, g)
        removed = removal_diagnostic(source, angles, columns, columns, g)
        thin = np.log(np.sum(source))
        self.assertAlmostEqual(base, np.log(np.sum(source))-g*g*100.0, places=12)
        self.assertAlmostEqual(
            removed["log10_luminosity_enhancement"],
            (thin-base)/np.log(10.0), places=12
        )

    def test_zero_coupling_has_no_shell_removal_effect(self):
        source = np.array([[1.0, 2.0], [3.0, 4.0]])
        angles = np.array([0.5, 0.5])
        columns = np.ones((2, 2, 2))*100.0
        base = log_escaped_integral(source, angles, columns, 0.0)
        removed = log_escaped_integral(
            source, angles, np.zeros_like(columns), 0.0
        )
        self.assertAlmostEqual(base, removed, places=14)


if __name__ == "__main__":
    unittest.main(verbosity=2)
