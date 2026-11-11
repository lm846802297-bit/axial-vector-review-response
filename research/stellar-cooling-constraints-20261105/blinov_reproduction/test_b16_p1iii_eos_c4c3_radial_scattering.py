import unittest
import numpy as np
from audit_b16_p1iii_eos_c4c3_radial_scattering import KM_TO_MEV_INV, shard_indices, tau_from_kappa


class TestC4C3RadialScattering(unittest.TestCase):
    def test_km_to_natural_length_conversion(self):
        self.assertAlmostEqual(KM_TO_MEV_INV, 5.067730716e15, delta=1e7)

    def test_constant_opacity_trapezoid(self):
        r = np.array([0.2, 0.7, 1.2])
        k = np.full(3, 2e-15)
        tau = tau_from_kappa(r, k)
        self.assertAlmostEqual(tau[0], 2e-15 * KM_TO_MEV_INV, delta=1e-12)
        self.assertAlmostEqual(tau[1], 1e-15 * KM_TO_MEV_INV, delta=1e-12)
        self.assertEqual(tau[-1], 0.0)

    def test_linear_opacity_exact_trapezoid(self):
        r = np.array([0.0, 0.5, 1.0])
        k = 1e-15 * (1.0 + r)
        tau = tau_from_kappa(r, k)
        self.assertAlmostEqual(tau[0], 1.5e-15 * KM_TO_MEV_INV, delta=1e-12)

    def test_shards_partition_301_points(self):
        for count in (1, 4, 20, 40):
            indices = [i for shard in range(count) for i in shard_indices(shard, count)]
            self.assertEqual(indices, list(range(301)))

    def test_tau_nonnegative_and_monotone(self):
        r = np.linspace(0.2, 15.2, 301)
        tau = tau_from_kappa(r, 1e-13 * np.exp(-r / 4.0))
        self.assertTrue(np.all(tau >= 0))
        self.assertTrue(np.all(np.diff(tau) <= 0))
        self.assertEqual(tau[-1], 0.0)


if __name__ == "__main__":
    unittest.main()
