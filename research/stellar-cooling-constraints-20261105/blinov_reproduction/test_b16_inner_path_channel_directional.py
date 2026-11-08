import sys
import unittest
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import KM_TO_MEV_INV, local_rates
from blinov_reproduction.audit_b16_inner_path_channel_directional import (
    SHELL_EDGES_KM,
    analytic_ray_shell_columns,
    reduced_absorption_channels,
)


def direct_s_shell_integral(
    source_radius, cosine, radial_grid, reduced_by_channel,
    mass, energies, radius_km=25.0, shell_edges=SHELL_EDGES_KM, order=32,
):
    """Independent s-coordinate quadrature split at every radial/shell crossing."""
    energies = np.asarray(energies, float)
    angles_x, angles_w = leggauss(order)
    impact = source_radius * np.sqrt(max(1.0 - cosine * cosine, 0.0))
    s_max = -source_radius * cosine + np.sqrt(radius_km**2 - impact**2)
    breaks = [0.0, s_max]
    if cosine < 0.0:
        turn = -source_radius * cosine
        if 0.0 < turn < s_max:
            breaks.append(turn)
    for radius in np.unique(np.r_[radial_grid, shell_edges]):
        if radius < impact:
            continue
        root = np.sqrt(max(radius * radius - impact * impact, 0.0))
        for value in (-source_radius * cosine - root,
                      -source_radius * cosine + root):
            if 0.0 < value < s_max:
                breaks.append(value)
    breaks = np.unique(np.asarray(breaks, float))
    names = tuple(reduced_by_channel)
    result = np.zeros((len(names), len(shell_edges) - 1, len(energies)))
    velocity = np.sqrt(1.0 - (mass / energies) ** 2)
    for s_a, s_b in zip(breaks[:-1], breaks[1:]):
        if s_b <= s_a:
            continue
        half = 0.5 * (s_b - s_a)
        mid = 0.5 * (s_b + s_a)
        s = mid + half * angles_x
        position = np.sqrt(
            source_radius**2 + s**2 + 2.0 * source_radius * s * cosine
        )
        position_mid = np.sqrt(
            source_radius**2 + mid**2 + 2.0 * source_radius * mid * cosine
        )
        shell = int(np.searchsorted(shell_edges, position_mid, side="right") - 1)
        shell = min(max(shell, 0), len(shell_edges) - 2)
        for ic, name in enumerate(names):
            for ie in range(len(energies)):
                values = np.interp(position, radial_grid, reduced_by_channel[name][:, ie])
                result[ic, shell, ie] += (
                    half * np.sum(angles_w * values) * KM_TO_MEV_INV / velocity[ie]
                )
    return result


class B16InnerPathChannelDirectionalTests(unittest.TestCase):
    def setUp(self):
        self.mass = 10.0
        self.energies = np.array([10.5, 15.0, 30.0])
        self.radial_grid = np.linspace(0.0, 25.0, 51)
        self.shell_edges = SHELL_EDGES_KM.copy()

    def test_constant_opacity_reproduces_exact_chord_length(self):
        reduced = {
            "nu_mu": np.full((len(self.radial_grid), len(self.energies)), 2.0),
            "compton": np.full((len(self.radial_grid), len(self.energies)), 0.5),
        }
        r0, cosine = 12.0, -0.6
        columns = analytic_ray_shell_columns(
            r0, cosine, self.radial_grid, reduced,
            self.mass, self.energies, 25.0, self.shell_edges
        )
        chord = -r0 * cosine + np.sqrt(
            25.0**2 - r0**2 * (1.0 - cosine**2)
        )
        velocity = np.sqrt(1.0 - (self.mass / self.energies) ** 2)
        expected = np.array([2.0, 0.5])[:, None] * chord * KM_TO_MEV_INV / velocity[None, :]
        np.testing.assert_allclose(np.sum(columns, axis=1), expected, rtol=3e-14, atol=1e-12)

    def test_piecewise_linear_radial_integral_matches_independent_s_quadrature(self):
        rng = np.random.default_rng(20261109)
        reduced = {
            "nu_mu": rng.uniform(0.1, 1.5, (len(self.radial_grid), len(self.energies))),
            "nu_tau": rng.uniform(0.1, 1.2, (len(self.radial_grid), len(self.energies))),
            "compton": rng.uniform(0.01, 0.3, (len(self.radial_grid), len(self.energies))),
        }
        for cosine in (-0.73, -0.18, 0.37, 0.82):
            analytic = analytic_ray_shell_columns(
                12.0, cosine, self.radial_grid, reduced,
                self.mass, self.energies, 25.0, self.shell_edges
            )
            direct = direct_s_shell_integral(
                12.0, cosine, self.radial_grid, reduced,
                self.mass, self.energies, 25.0, self.shell_edges, order=32
            )
            np.testing.assert_allclose(analytic, direct, rtol=3e-11, atol=1e-11)

    def test_outer_shell_column_is_even_under_direction_reversal(self):
        reduced = {
            "nu_mu": np.tile((0.2 + 0.01 * self.radial_grid)[:, None], (1, len(self.energies))),
            "compton": np.tile((0.05 + 0.002 * self.radial_grid)[:, None], (1, len(self.energies))),
        }
        outward = analytic_ray_shell_columns(
            12.0, 0.6, self.radial_grid, reduced,
            self.mass, self.energies, 25.0, self.shell_edges
        )
        inward = analytic_ray_shell_columns(
            12.0, -0.6, self.radial_grid, reduced,
            self.mass, self.energies, 25.0, self.shell_edges
        )
        np.testing.assert_allclose(outward[:, -1, :], inward[:, -1, :], rtol=3e-13, atol=1e-12)

    def test_channel_reduced_absorption_closes_to_reference_total(self):
        profile = {
            "T": np.array([35.0, 22.0, 12.0]),
            "mu_mu": np.array([75.0, 42.0, 8.0]),
            "mu_numu": np.array([-15.0, -4.0, 0.0]),
        }
        rates = local_rates(
            self.mass, self.energies[None, :],
            profile["T"][:, None], profile["mu_numu"][:, None],
            profile["mu_mu"][:, None]
        )
        _, reduced, closure = reduced_absorption_channels(
            self.mass, self.energies, profile, rates
        )
        np.testing.assert_allclose(
            sum(reduced.values()), rates["reduced_absorption"],
            rtol=2e-13, atol=1e-300
        )
        self.assertLess(closure["reduced_absorption_channel_sum_max_relative_residual"], 2e-13)

    def test_inward_ray_counts_inner_radii_twice(self):
        reduced = {
            "nu_mu": np.ones((len(self.radial_grid), len(self.energies))),
        }
        inward = analytic_ray_shell_columns(
            12.0, -1.0, self.radial_grid, reduced,
            self.mass, self.energies, 25.0, self.shell_edges
        )
        outward = analytic_ray_shell_columns(
            12.0, 1.0, self.radial_grid, reduced,
            self.mass, self.energies, 25.0, self.shell_edges
        )
        # The 0--5 km shell is crossed twice by the inward ray and not at all
        # by the outward ray; the 22--25 km shell is crossed once by both.
        self.assertGreater(float(np.sum(inward[:, 0, :])), 0.0)
        self.assertEqual(float(np.sum(outward[:, 0, :])), 0.0)
        np.testing.assert_allclose(inward[:, -1, :], outward[:, -1, :], rtol=2e-13, atol=1e-12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
