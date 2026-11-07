import unittest
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_eq_b2_path_integral import (
    KM_TO_MEV_INV,
    adaptive_escape_probability,
    exact_piecewise_linear_ray_column,
    ray_breakpoints,
)


class IndependentEqB2PathIntegralTests(unittest.TestCase):
    def test_constant_opacity_matches_analytic_chord_length(self):
        radius = 25.0
        grid = np.array([0.0, 5.0, 10.0, 15.0, 20.0, radius])
        energies = np.array([2.0, 3.0])
        mass = 1.0
        kappa = 2.5e-12
        opacity = np.full((grid.size, energies.size), kappa)
        for source_r in (0.0, 5.0, 17.0, 24.0, 25.0):
            for cosine in (-1.0, -0.7, 0.0, 0.6, 1.0):
                b = source_r * np.sqrt(max(0.0, 1.0 - cosine**2))
                smax = -source_r * cosine + np.sqrt(radius**2 - b**2)
                actual = exact_piecewise_linear_ray_column(
                    source_r, cosine, grid, opacity, mass, energies, radius
                )
                velocity = np.sqrt(1.0 - (mass / energies)**2)
                expected = kappa * smax * KM_TO_MEV_INV / velocity
                np.testing.assert_allclose(actual, expected, rtol=2e-12, atol=1e-14)

    def test_piecewise_linear_ray_integral_matches_split_adaptive_quadrature(self):
        radius = 25.0
        grid = np.array([0.0, 2.0, 5.0, 8.0, 12.0, 15.0, 20.0, 25.0])
        energies = np.array([10.1, 30.0])
        mass = 10.0
        profile = np.exp(-grid / 7.0) * (1.0 + 0.03 * grid)
        opacity = np.column_stack((profile, 1.7 * profile))
        source_r, cosine = 17.0, -0.63
        b = source_r * np.sqrt(1.0 - cosine**2)
        cuts = ray_breakpoints(source_r, cosine, grid, radius)
        direct = np.zeros(energies.size)
        for za, zb in zip(cuts[:-1], cuts[1:]):
            for ie in range(energies.size):
                value = quad(
                    lambda z: np.interp(np.hypot(b, z), grid, opacity[:, ie]),
                    za, zb, epsabs=1e-12, epsrel=2e-12, limit=100,
                )[0]
                direct[ie] += value
        velocity = np.sqrt(1.0 - (mass / energies)**2)
        expected = direct * KM_TO_MEV_INV / velocity
        actual = exact_piecewise_linear_ray_column(
            source_r, cosine, grid, opacity, mass, energies, radius
        )
        np.testing.assert_allclose(actual, expected, rtol=3e-11, atol=1e-12)

    def test_absorber_shell_columns_are_additive(self):
        radius = 25.0
        grid = np.array([0.0, 5.0, 10.0, 15.0, 18.0, 20.0, 22.0, 25.0])
        energies = np.array([10.1, 20.0])
        opacity = np.column_stack((
            np.exp(-grid / 8.0),
            0.4 * np.exp(-grid / 10.0),
        ))
        args = (22.0, -0.47, grid, opacity, 10.0, energies, radius)
        full = exact_piecewise_linear_ray_column(*args)
        inner = exact_piecewise_linear_ray_column(*args, absorber_range=(0.0, 15.0))
        shell_15_20 = exact_piecewise_linear_ray_column(*args, absorber_range=(15.0, 20.0))
        shell_20_25 = exact_piecewise_linear_ray_column(*args, absorber_range=(20.0, 25.0))
        np.testing.assert_allclose(
            inner + shell_15_20 + shell_20_25, full,
            rtol=3e-12, atol=1e-12,
        )

    def test_central_source_has_direction_independent_column(self):
        grid = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0])
        energies = np.array([10.1])
        opacity = np.exp(-grid[:, None] / 8.0)
        values = [
            exact_piecewise_linear_ray_column(
                0.0, mu, grid, opacity, 10.0, energies
            )[0]
            for mu in (-1.0, -0.8, 0.0, 0.7, 1.0)
        ]
        np.testing.assert_allclose(values, np.full(5, values[0]), rtol=0, atol=1e-12)

    def test_surface_outward_ray_is_transparent_and_inward_ray_crosses_diameter(self):
        radius = 25.0
        grid = np.array([0.0, 5.0, 10.0, 15.0, 20.0, radius])
        energies = np.array([10.1])
        mass = 10.0
        kappa = 1.0e-12
        opacity = np.full((grid.size, 1), kappa)
        outward = exact_piecewise_linear_ray_column(
            radius, 1.0, grid, opacity, mass, energies, radius
        )[0]
        inward = exact_piecewise_linear_ray_column(
            radius, -1.0, grid, opacity, mass, energies, radius
        )[0]
        velocity = np.sqrt(1.0 - (mass / energies[0])**2)
        expected_inward = 2.0 * radius * kappa * KM_TO_MEV_INV / velocity
        self.assertAlmostEqual(outward, 0.0, places=14)
        self.assertAlmostEqual(inward / expected_inward, 1.0, places=12)

    def test_adaptive_angle_average_matches_high_order_gauss_legendre(self):
        from numpy.polynomial.legendre import leggauss

        grid = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0])
        energies = np.array([10.1])
        opacity = (1.0e-17 * np.exp(-grid / 12.0))[:, None]
        coupling = 0.5
        adaptive = adaptive_escape_probability(
            17.0, 0, grid, opacity, 10.0, energies, coupling
        )
        mu, weights = leggauss(512)
        columns = np.array([
            exact_piecewise_linear_ray_column(
                17.0, float(x), grid, opacity, 10.0, energies
            )[0]
            for x in mu
        ])
        gauss = float(np.dot(weights / 2.0, np.exp(-coupling**2 * columns)))
        self.assertAlmostEqual(gauss / adaptive, 1.0, delta=2e-7)


if __name__ == "__main__":
    unittest.main()
