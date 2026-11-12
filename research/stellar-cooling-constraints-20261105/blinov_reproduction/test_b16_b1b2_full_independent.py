import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_b16_b1b2_full_independent import (
    angular_escape_factors,
)


class FullB1B2IntegrationTests(unittest.TestCase):
    def test_zero_optical_depth_gives_unit_escape_probability(self):
        tau = np.zeros((16, 11))
        weights = np.full(16, 1.0/16.0)
        couplings = np.geomspace(1.0e-10, 1.0e-4, 7)
        escape = angular_escape_factors(tau, weights, couplings)
        np.testing.assert_allclose(escape, 1.0, rtol=0.0, atol=2.0e-15)

    def test_escape_probability_decreases_with_coupling(self):
        tau = np.linspace(0.0, 100.0, 16*11).reshape(16, 11)
        weights = np.full(16, 1.0/16.0)
        couplings = np.geomspace(1.0e-5, 1.0e-1, 9)
        escape = angular_escape_factors(tau, weights, couplings)
        self.assertTrue(np.all(np.diff(escape, axis=0) <= 1.0e-14))
        self.assertTrue(np.all((escape >= 0.0) & (escape <= 1.0)))

    def test_escape_is_one_at_zero_coupling_limit(self):
        tau = np.ones((8, 5))*2.0
        weights = np.full(8, 1.0/8.0)
        escape = angular_escape_factors(tau, weights, np.array([1.0e-12]))
        np.testing.assert_allclose(escape, 1.0, rtol=0.0, atol=1.0e-14)

    def test_invalid_negative_optical_depth_is_rejected(self):
        with self.assertRaises(ValueError):
            angular_escape_factors(
                np.array([[0.0, -1.0]]), np.array([1.0]), np.array([1.0e-4])
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
