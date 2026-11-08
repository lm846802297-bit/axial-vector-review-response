import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import (
    KM_TO_MEV_INV, radial_rule, energy_weights, local_rates,
    scalar_optical_depths,
)
from blinov_reproduction.audit_b16_global_redshift import (
    eq_b1_source_measure, redshifted_scalar_optical_depths,
    radial_shell_opacity_decomposition,
)


class B16GlobalRedshiftAuditTests(unittest.TestCase):
    def test_eq_b1_radial_weight_integrates_flat_spherical_volume_times_lapse_squared(self):
        radius = 25.0
        lapse = 0.73
        r, rw = radial_rule(radius, 40)
        numeric = np.sum(4.0*np.pi*r**2*rw*lapse**2)
        analytic = 4.0*np.pi*radius**3*lapse**2/3.0
        self.assertAlmostEqual(numeric/analytic, 1.0, places=12)

    def test_eq_b1_energy_weights_integrate_constant_spectrum_from_local_escape_threshold(self):
        mass = 10.0
        lapse = np.array([0.70, 0.80, 0.90])
        energies = np.unique(np.r_[mass+np.geomspace(1e-5, 100.0, 80), mass/lapse])
        energies.sort()
        weights = energy_weights(energies, mass/lapse)
        expected = energies[-1]-mass/lapse
        np.testing.assert_allclose(np.sum(weights, axis=1), expected, rtol=2e-13, atol=1e-12)

    def test_eq_b1_source_measure_contains_n_squared_and_massive_vector_phase_space(self):
        mass = 10.0
        r = np.array([2.0, 7.0, 13.0])
        rw = np.array([0.5, 0.7, 0.9])
        lapse = np.array([0.72, 0.80, 0.88])
        energies = np.unique(np.r_[15.0, 20.0, 30.0, 50.0, mass/lapse])
        production = np.ones((len(r), len(energies)))
        source, pieces = eq_b1_source_measure(
            r, rw, energies, lapse, mass, production
        )
        eweights = energy_weights(energies, mass/lapse)
        momentum = np.sqrt(energies**2-mass**2)
        radial = 4*np.pi*(r*KM_TO_MEV_INV)**2*rw*KM_TO_MEV_INV*lapse**2
        spectral = momentum*energies**2/(2*np.pi**2)
        expected = radial[:,None]*eweights*spectral[None,:]*1.602176634e-6/6.582119569e-22
        np.testing.assert_allclose(source, expected, rtol=2e-14, atol=0.0)
        np.testing.assert_allclose(
            pieces["radial_measure_MeVminus3"], radial, rtol=2e-14
        )

    def test_fixed_omega_and_path_redshift_opacity_agree_for_constant_lapse_profile(self):
        mass = 10.0
        radius = 10.0
        source_r = np.array([1.0, 3.0])
        radial_grid = np.array([0.0, 1.0, 3.0, radius])
        profile = {
            "T": np.full(4, 20.0),
            "mu_mu": np.full(4, 55.0),
            "mu_numu": np.full(4, -15.0),
            "lapse": np.full(4, 0.80),
        }
        energies = np.array([15.0, 20.0, 30.0, 50.0])
        rates = local_rates(
            mass, energies[None,:], profile["T"][:,None],
            profile["mu_numu"][:,None], profile["mu_mu"][:,None]
        )
        fixed, angle_fixed = scalar_optical_depths(
            source_r, radial_grid, rates["reduced_absorption"],
            mass, energies, radius, angular_order=8, path_order=16
        )
        shifted, angle_shifted, info = redshifted_scalar_optical_depths(
            source_r, radial_grid, profile, mass, energies,
            radius, angular_order=8, path_order=16
        )
        np.testing.assert_allclose(angle_shifted, angle_fixed, rtol=0, atol=1e-14)
        np.testing.assert_allclose(shifted, fixed, rtol=3e-12, atol=1e-12)
        self.assertAlmostEqual(info["energy_ratio_local_over_source_min"], 1.0, places=14)
        self.assertAlmostEqual(info["energy_ratio_local_over_source_max"], 1.0, places=14)

    def test_radial_shell_opacities_reconstruct_direct_chord_columns(self):
        mass = 10.0
        radius = 25.0
        r, rw = radial_rule(radius, 8)
        radial_grid = np.unique(np.r_[0.0, r, radius])
        profile = {
            "T": np.full(len(radial_grid), 20.0),
            "mu_mu": np.full(len(radial_grid), 55.0),
            "mu_numu": np.full(len(radial_grid), -15.0),
            "lapse": np.full(len(radial_grid), 0.80),
        }
        energies = np.unique(np.r_[
            mass+np.geomspace(1e-5, 100.0, 24), mass/0.80
        ])
        energies.sort()
        rates = local_rates(
            mass, energies[None,:], profile["T"][:,None],
            profile["mu_numu"][:,None], profile["mu_mu"][:,None]
        )
        source_indices = np.searchsorted(radial_grid, r)
        source, _ = eq_b1_source_measure(
            r, rw, energies, profile["lapse"][source_indices],
            mass, rates["production"][source_indices]
        )
        columns, angle_weights = scalar_optical_depths(
            r, radial_grid, rates["reduced_absorption"], mass, energies,
            radius, angular_order=8, path_order=16
        )
        result = radial_shell_opacity_decomposition(
            r, radial_grid, profile["T"], rates, mass, energies,
            radius, source, columns, angle_weights,
            angular_order=8, path_order=16
        )
        self.assertLess(abs(result["shell_sum_rule_relative_residual"]), 2e-10)
        self.assertLess(
            result["B19_B4_reduced_absorption_channel_sum_relative_residual"],
            2e-12
        )
        self.assertAlmostEqual(
            sum(result["channel_fraction_of_mean_tau"].values()), 1.0, places=12
        )

    def test_local_redshift_preserves_energy_at_infinity(self):
        omega_source = 35.0
        lapse_source = 0.74
        lapse_path = 0.91
        omega_path = omega_source*lapse_source/lapse_path
        self.assertAlmostEqual(
            lapse_source*omega_source, lapse_path*omega_path, places=13
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
