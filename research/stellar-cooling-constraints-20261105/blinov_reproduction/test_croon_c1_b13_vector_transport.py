import math
import unittest
from pathlib import Path

import numpy as np

from rates import neutrino_rates
from finite_mixing.moving_muon_compton import moving_muon_compton_rates
from adaptive_radial_transport import AdaptiveRadialProfile

from croon_c1_b13_vector_transport import (
    DEFAULT_PROFILE,
    PROFILE_SHA256,
    energy_quadrature,
    integrate_spherical_source,
    integrate_spherical_source_by_mode,
    neutrinosphere_radius,
    outer_vacuum_neutrino_opacity_per_g2,
    radial_optical_depth,
    sample_profile,
)


class CroonC1B13VectorTransportTests(unittest.TestCase):
    def test_profile_identity_and_neutrinosphere_boundary(self):
        self.assertEqual(
            __import__("hashlib").sha256(DEFAULT_PROFILE.read_bytes()).hexdigest(),
            PROFILE_SHA256,
        )
        profile = sample_profile(DEFAULT_PROFILE, radial_points=31)
        self.assertAlmostEqual(profile["temperature_MeV"][-1], 3.0, places=12)
        self.assertAlmostEqual(profile["R_nu_km"], 25.1511683, places=5)
        self.assertIn(profile["r_mu_last_nonzero_km"], profile["r_km"])
        self.assertIn(profile["r_mu_first_zero_km"], profile["r_km"])

    def test_energy_quadrature_has_positive_threshold_adapted_nodes(self):
        omega, weights, phase = energy_quadrature(10.0, 39.0, order=24)
        self.assertEqual(omega.shape, (24,))
        self.assertEqual(weights.shape, (24,))
        self.assertEqual(phase.shape, (24,))
        self.assertTrue(np.all(omega > 10.0))
        self.assertTrue(np.all(weights > 0.0))
        self.assertTrue(np.all(phase > 0.0))
        self.assertTrue(np.all(np.diff(omega) > 0.0))

    def test_outer_vacuum_tail_is_two_flavour_per_mode(self):
        mass = 10.0
        omega = np.array([12.0, 20.0, 50.0])
        length_km = 75.0
        result = outer_vacuum_neutrino_opacity_per_g2(mass, omega, length_km)
        expected = (
            length_km * 1.0e5 / (197.3269804e-13)
            * mass**2 / (12.0 * np.pi * omega)
        )
        np.testing.assert_allclose(result, expected, rtol=1e-14)
        self.assertTrue(np.all(result > 0.0))
        np.testing.assert_array_equal(
            outer_vacuum_neutrino_opacity_per_g2(mass, omega, 0.0),
            np.zeros_like(omega),
        )

    def test_radial_optical_depth_for_constant_mode_resolved_opacity(self):
        r = np.array([0.0, 1.0, 2.0, 3.0])
        kappa = np.ones((4, 2, 3))
        tau = radial_optical_depth(kappa, r)
        expected = np.array([3.0, 2.0, 1.0, 0.0])[:, None, None]
        np.testing.assert_allclose(tau, np.broadcast_to(expected, (4, 2, 3)), rtol=1e-13, atol=1e-13)

    def test_three_mode_source_integral_closes_to_mode_sum(self):
        radius = np.array([0.0, 1.0, 2.0, 3.0])
        source = np.zeros((4, 5, 3))
        source[:, :, 0] = 1.0
        source[:, :, 1] = 2.0
        source[:, :, 2] = 4.0
        energy_weights = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
        by_mode = integrate_spherical_source_by_mode(
            source, radius, energy_weights
        )
        total = integrate_spherical_source(source, radius, energy_weights)
        self.assertEqual(by_mode.shape, (3,))
        np.testing.assert_allclose(by_mode, [4.5, 9.0, 18.0], rtol=1e-13)
        self.assertAlmostEqual(float(np.sum(by_mode)), total, places=13)

    def test_b7_two_flavour_mode_rates_obey_detailed_balance(self):
        mass, temperature, mu_numu = 10.0, 20.0, -15.0
        omega = np.array([12.0, 20.0, 50.0])
        production, absorption = neutrino_rates(
            mass, omega, temperature, mu_numu, order=96
        )
        expected = np.exp(-omega / temperature)[:, None] * absorption
        residual = np.max(
            np.abs(production - expected)
            / np.maximum(np.maximum(np.abs(production), np.abs(expected)), 1e-300)
        )
        self.assertLess(residual, 2e-12)
        self.assertEqual(production.shape, (3, 3))

    def test_b13_both_muon_charges_and_modes_obey_detailed_balance(self):
        mass, omega, temperature, mu_mu = 10.0, 20.0, 20.0, 40.0
        result = moving_muon_compton_rates(
            mass, omega, temperature, mu_mu,
            g_vector=1.0, g_axial=0.0, orders=(8, 4, 4, 4)
        )
        self.assertEqual(result["mode_order"], ["L", "+", "-"])
        self.assertEqual(set(result["charge_resolved"]), {"mu_minus", "mu_plus"})
        for charge in ("mu_minus", "mu_plus"):
            production = np.asarray(result["charge_resolved"][charge]["production"])
            absorption = np.asarray(result["charge_resolved"][charge]["absorption"])
            self.assertEqual(production.shape, (3,))
            self.assertTrue(np.all(production >= 0.0))
            self.assertTrue(np.all(absorption >= 0.0))
            expected = math.exp(-omega / temperature) * absorption
            residual = np.max(
                np.abs(production - expected)
                / np.maximum(np.maximum(np.abs(production), np.abs(expected)), 1e-300)
            )
            self.assertLess(residual, 2e-10)
        self.assertLess(
            result["diagnostics"]["final_muon_shell_relative_error"], 2e-10
        )



class AdaptiveRadialBoundaryLayerTests(unittest.TestCase):
    def test_constant_source_and_opacity_match_analytic_integral(self):
        radius = np.linspace(0.0, 2.0, 103)
        source = np.full_like(radius, 3.2)
        opacity = np.full_like(radius, 0.7)
        profile = AdaptiveRadialProfile(radius, source, opacity)
        for coupling in (1.0e-11, 1.0e-5, 0.1, 1.0, 100.0):
            value, error = profile.integrate(coupling)
            expected = (
                3.2 / 0.7
                * (-math.expm1(-coupling**2 * 0.7 * 2.0))
            )
            self.assertAlmostEqual(value / expected, 1.0, delta=2.0e-8)
            self.assertLessEqual(error, 2.0e-8 * abs(value) + 1.0e-300)

    def test_high_coupling_reaches_surface_source_over_opacity(self):
        radius = np.linspace(0.0, 1.0, 103)
        source = 2.0 + 0.3 * radius
        opacity = 0.7 + 0.1 * radius
        profile = AdaptiveRadialProfile(radius, source, opacity)
        value, _ = profile.integrate(1.0e3)
        expected = source[-1] / opacity[-1]
        self.assertAlmostEqual(value / expected, 1.0, delta=2.0e-7)
        self.assertAlmostEqual(
            profile.surface_source_over_opacity, expected, places=14
        )

    def test_outer_optical_depth_is_an_exact_multiplicative_tail(self):
        radius = np.linspace(0.0, 1.0, 103)
        profile = AdaptiveRadialProfile(
            radius, 1.0 + radius, 0.5 + 0.2 * radius
        )
        coupling = 0.7
        inside, _ = profile.integrate(coupling)
        with_tail, _ = profile.integrate(coupling, tau_outer=0.3)
        self.assertAlmostEqual(
            with_tail / inside,
            math.exp(-coupling**2 * 0.3),
            places=14,
        )

    def test_adaptive_integral_removes_fixed_simpson_endpoint_artifact(self):
        from scipy.integrate import simpson

        legacy_values = []
        adaptive_values = []
        for count in (103, 153):
            radius = np.linspace(0.0, 1.0, count)
            source = np.ones_like(radius)
            opacity = np.ones_like(radius)
            tau_sampled = 1.0 - radius
            coupling = 100.0
            legacy = coupling**2 * simpson(
                source * np.exp(-coupling**2 * tau_sampled),
                x=radius,
            )
            adaptive, _ = AdaptiveRadialProfile(
                radius, source, opacity
            ).integrate(coupling)
            legacy_values.append(legacy)
            adaptive_values.append(adaptive)

        # The fixed-grid Simpson endpoint weight scales with dr. The adaptive
        # integral instead approaches the exact surface limit S/kappa = 1.
        self.assertAlmostEqual(
            legacy_values[1] / legacy_values[0], 102.0 / 152.0, delta=2.0e-3
        )
        np.testing.assert_allclose(
            adaptive_values, [1.0, 1.0], rtol=2.0e-8, atol=1.0e-12
        )

    def test_surface_centered_coordinate_resolves_sub_ulp_escape_layer(self):
        # kappa*R is so large that the physical escape layer is only
        # O(10^-16) of the stellar radius. A center-to-surface coordinate
        # would place it next to x=1, where double precision loses resolution.
        radius = np.linspace(0.0, 1.0e17, 103)
        source = np.full_like(radius, 2.0)
        opacity = np.full_like(radius, 0.2)
        profile = AdaptiveRadialProfile(radius, source, opacity)
        value, error = profile.integrate(1.0)
        expected = (
            2.0 / 0.2
            * (-math.expm1(-0.2 * 1.0e17))
        )
        self.assertAlmostEqual(value / expected, 1.0, delta=2.0e-8)
        self.assertLess(error, 2.0e-8 * expected)

    def test_zero_opacity_outer_interval_remains_finite(self):
        radius = np.linspace(0.0, 1.0, 103)
        source = np.ones_like(radius)
        opacity = np.where(radius < 0.6, 1.0, 0.0)
        profile = AdaptiveRadialProfile(radius, source, opacity)
        value, error = profile.integrate(3.0)
        self.assertTrue(math.isfinite(value))
        self.assertGreaterEqual(value, 0.0)
        self.assertTrue(math.isfinite(error))
        self.assertGreaterEqual(error, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
