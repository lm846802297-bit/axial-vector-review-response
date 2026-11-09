import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_b16_b1_independent import (
    composite_gauss,
    log_energy_rule,
)


class IndependentB1QuadratureTests(unittest.TestCase):
    def test_composite_gauss_integrates_polynomials(self):
        edges = np.array([-2.0, -0.3, 1.1, 4.0])
        nodes, weights = composite_gauss(edges, 4)
        for power in range(8):
            actual = float(np.dot(weights, nodes**power))
            expected = (edges[-1]**(power+1)-edges[0]**(power+1))/(power+1)
            self.assertAlmostEqual(actual, expected, delta=2.0e-11*max(1.0, abs(expected)))

    def test_log_energy_rule_integrates_constant_and_quadratic_exactly(self):
        mass = 10.0
        lower = 13.2
        offset = 1000.0
        upper = mass + offset
        omega, weights = log_energy_rule(mass, lower, offset, 24, 4)
        constant = float(np.sum(weights))
        quadratic = float(np.dot(weights, omega**2))
        self.assertAlmostEqual(constant, upper-lower, delta=2.0e-11*upper)
        expected = (upper**3-lower**3)/3.0
        self.assertAlmostEqual(quadratic, expected, delta=1.0e-10*expected)

    def test_exact_radius_dependent_threshold_is_respected(self):
        mass = 10.0
        lower = mass/0.7363
        omega, weights = log_energy_rule(mass, lower, 1000.0, 40, 4)
        self.assertGreater(float(np.min(omega)), lower)
        self.assertAlmostEqual(float(np.sum(weights)), mass+1000.0-lower, places=9)

    def test_invalid_threshold_and_upper_bound_are_rejected(self):
        with self.assertRaises(ValueError):
            log_energy_rule(10.0, 10.0, 1000.0, 20, 4)
        with self.assertRaises(ValueError):
            log_energy_rule(10.0, 12.0, 1.0, 20, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
