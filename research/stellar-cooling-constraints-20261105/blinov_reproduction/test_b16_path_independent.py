import sys
import unittest
from pathlib import Path

import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_b16_path_independent import (
    chord_integral_piecewise_linear,
    simpson_angle_rule,
)


class IndependentB2PathTests(unittest.TestCase):
    def _quad_chord(self, r0, cosine, grid, values):
        impact = r0*np.sqrt(max(0.0, 1.0-cosine*cosine))
        z0 = r0*cosine
        z1 = np.sqrt(grid[-1]**2-impact**2)
        smax = z1-z0

        def integrand(s):
            z = z0+s
            rho = np.hypot(z, impact)
            return float(np.interp(rho, grid, values))

        points = []
        for knot in grid:
            if knot < impact:
                continue
            zabs = np.sqrt(max(0.0, knot*knot-impact*impact))
            for zc in (zabs, -zabs):
                sc = zc-z0
                if 0.0 < sc < smax:
                    points.append(sc)
        value, error = quad(
            integrand, 0.0, smax, points=sorted(set(points)),
            epsabs=0.0, epsrel=2.0e-12, limit=500
        )
        return value, error

    def test_constant_opacity_is_exact_for_radial_and_inward_chords(self):
        radius = 25.0
        grid = np.array([0.0, 2.0, 5.0, 12.0, 18.0, 25.0])
        gamma = 2.7e-9
        values = np.full(len(grid), gamma)
        for r0, cosine in ((3.0, 1.0), (3.0, -1.0), (8.0, -0.45), (17.0, 0.3)):
            impact = r0*np.sqrt(max(0.0, 1.0-cosine*cosine))
            z0 = r0*cosine
            z1 = np.sqrt(radius*radius-impact*impact)
            expected = gamma*(z1-z0)
            actual = chord_integral_piecewise_linear(r0, cosine, grid, values)[0]
            self.assertAlmostEqual(actual/expected, 1.0, delta=2.0e-13)

    def test_piecewise_linear_analytic_integral_matches_adaptive_quad(self):
        grid = np.array([0.0, 1.5, 3.0, 5.5, 8.0, 10.0])
        values = 0.4 + 0.03*grid + 0.002*grid**2
        for r0, cosine in ((3.2, -0.6), (6.0, 0.25), (1.0, -0.98), (9.0, 0.99)):
            exact = chord_integral_piecewise_linear(r0, cosine, grid, values)[0]
            reference, error = self._quad_chord(r0, cosine, grid, values)
            self.assertLess(error, max(1.0e-11*abs(reference), 1.0e-13))
            self.assertAlmostEqual(exact/reference, 1.0, delta=2.0e-11)

    def test_b_zero_primitive_handles_central_crossing(self):
        grid = np.array([0.0, 2.0, 5.0, 10.0])
        values = 1.0 + 0.2*grid
        exact = chord_integral_piecewise_linear(3.0, -1.0, grid, values)[0]
        reference, _ = self._quad_chord(3.0, -1.0, grid, values)
        self.assertAlmostEqual(exact/reference, 1.0, delta=2.0e-11)

    def test_simpson_rule_is_normalized_and_exact_for_quadratic(self):
        nodes, weights = simpson_angle_rule(128)
        self.assertAlmostEqual(float(np.sum(weights)), 1.0, places=14)
        self.assertAlmostEqual(float(np.dot(weights, nodes)), 0.0, places=14)
        self.assertAlmostEqual(float(np.dot(weights, nodes**2)), 1.0/3.0, places=14)

    def test_simpson_rejects_odd_interval_count(self):
        with self.assertRaises(ValueError):
            simpson_angle_rule(127)


if __name__ == "__main__":
    unittest.main(verbosity=2)
