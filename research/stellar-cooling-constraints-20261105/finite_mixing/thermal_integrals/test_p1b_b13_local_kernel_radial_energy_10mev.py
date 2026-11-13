import math
import unittest

import numpy as np

from blinov_reproduction.reference import DEFAULT_PROFILE, load_profile
from finite_mixing.moving_muon_compton import moving_muon_compton_rates
from finite_mixing.thermal_integrals.audit_b13_local_kernel_radial_energy_10mev import (
    ENERGIES_MEV,
    ENERGY_INTEGRAL_X_MAX,
    EXPECTED_PROFILE_SHA256,
    MASS_MEV,
    RADII_KM,
    _bilinear_log_value,
    _interpolate_pair,
    _max_relative_difference,
    interpolate_cell,
    sha256,
)


class P1BB13LocalKernelRadialEnergyTests(unittest.TestCase):
    def test_profile_identity_and_grid_cover_existing_anchor_points(self):
        self.assertEqual(sha256(DEFAULT_PROFILE), EXPECTED_PROFILE_SHA256)
        self.assertIn(8.0, RADII_KM)
        self.assertIn(12.5, RADII_KM)
        self.assertIn(15.0, RADII_KM)
        self.assertEqual(len(RADII_KM), 17)
        self.assertEqual(len(ENERGIES_MEV), 25)
        self.assertIn(2.5, RADII_KM)
        self.assertIn(10.125, ENERGIES_MEV)
        self.assertIn(15.0, ENERGIES_MEV)
        self.assertIn(20.0, ENERGIES_MEV)
        self.assertIn(30.0, ENERGIES_MEV)
        self.assertEqual(MASS_MEV, 10.0)

    def test_threshold_and_high_energy_coverage(self):
        self.assertEqual(ENERGIES_MEV[0], MASS_MEV)
        profile = load_profile(DEFAULT_PROFILE, np.asarray(RADII_KM, dtype=float))
        required = MASS_MEV + ENERGY_INTEGRAL_X_MAX * float(np.max(profile["T"]))
        self.assertGreaterEqual(ENERGIES_MEV[-1], required)
        self.assertGreaterEqual(ENERGIES_MEV[-1], 720.0)
        self.assertTrue(all(b > a for a, b in zip(ENERGIES_MEV, ENERGIES_MEV[1:])))

    def test_geometric_bilinear_interpolation(self):
        # At the cell center, log-bilinear interpolation is the geometric mean.
        self.assertAlmostEqual(_bilinear_log_value([1.0, 4.0, 9.0, 36.0]), 6.0)

    def test_zero_corner_falls_back_to_linear_interpolation(self):
        self.assertAlmostEqual(_bilinear_log_value([0.0, 2.0, 4.0, 6.0]), 3.0)
        self.assertAlmostEqual(_interpolate_pair(0.0, 4.0, 0.5), 2.0)

    def test_positive_rate_pair_uses_log_linear_interpolation(self):
        self.assertAlmostEqual(_interpolate_pair(1.0, 9.0, 0.5), 3.0)

    def test_interpolated_production_and_reduced_opacity_obey_exact_local_balance(self):
        corners = []
        for scale in (1.0, 4.0, 9.0, 16.0):
            corners.append({
                "charge_resolved": {
                    "mu_minus": {"absorption": [scale, 2.0 * scale, 3.0 * scale]},
                    "mu_plus": {"absorption": [2.0 * scale, 3.0 * scale, 4.0 * scale]},
                }
            })
        omega = 20.0
        temperature = 10.0
        result = interpolate_cell(*corners, omega, temperature)
        boltzmann = math.exp(-omega / temperature)
        reduced = -math.expm1(-omega / temperature)
        prefactor = omega**2 * math.sqrt(omega**2 - MASS_MEV**2) / (2.0 * math.pi**2)
        for charge in ("mu_minus", "mu_plus"):
            absorption = np.asarray(result[charge]["absorption"])
            production = np.asarray(result[charge]["production"])
            reduced_absorption = np.asarray(result[charge]["reduced_absorption"])
            spectral_source = np.asarray(result[charge]["spectral_source"])
            np.testing.assert_allclose(production, boltzmann * absorption, rtol=1e-14)
            np.testing.assert_allclose(reduced_absorption, reduced * absorption, rtol=1e-14)
            np.testing.assert_allclose(spectral_source, prefactor * production, rtol=1e-14)

    def test_relative_difference_is_symmetric_and_zero_safe(self):
        self.assertAlmostEqual(
            _max_relative_difference([1.0, 0.0], [1.1, 0.0]),
            _max_relative_difference([1.1, 0.0], [1.0, 0.0]),
        )
        self.assertEqual(_max_relative_difference([0.0], [0.0]), 0.0)

    def test_exact_local_kernel_smoke_both_charges_and_three_modes(self):
        result = moving_muon_compton_rates(
            MASS_MEV,
            15.0,
            20.0,
            50.0,
            g_vector=1.0,
            g_axial=0.0,
            orders=(8, 4, 4, 4),
        )
        self.assertEqual(result["mode_order"], ["L", "+", "-"])
        self.assertEqual(set(result["charge_resolved"]), {"mu_minus", "mu_plus"})
        for charge in ("mu_minus", "mu_plus"):
            item = result["charge_resolved"][charge]
            production = np.asarray(item["production"], dtype=float)
            absorption = np.asarray(item["absorption"], dtype=float)
            self.assertEqual(production.shape, (3,))
            self.assertEqual(absorption.shape, (3,))
            self.assertTrue(np.all(np.isfinite(production)))
            self.assertTrue(np.all(np.isfinite(absorption)))
            self.assertTrue(np.all(production >= 0.0))
            self.assertTrue(np.all(absorption >= 0.0))
            expected = math.exp(-15.0 / 20.0) * absorption
            residual = np.max(
                np.abs(production - expected)
                / np.maximum(np.maximum(np.abs(production), np.abs(expected)), 1e-300)
            )
            self.assertLess(residual, 2e-10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
