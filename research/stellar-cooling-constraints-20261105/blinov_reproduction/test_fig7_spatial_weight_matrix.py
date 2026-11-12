import unittest
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_fig7_spatial_weight_matrix import (
    RADIAL_BINS,
    radial_bin_mask,
    weighted_mean,
)


class Fig7SpatialWeightMatrixTests(unittest.TestCase):
    def test_production_bins_partition_radial_quadrature_nodes(self):
        radii = np.array([0.2, 4.9, 5.0, 9.9, 10.0, 14.9,
                          15.0, 19.9, 20.0, 24.9, 25.0])
        masks = [radial_bin_mask(radii, interval) for interval in RADIAL_BINS]
        membership = np.sum(np.stack(masks, axis=0), axis=0)
        np.testing.assert_array_equal(membership, np.ones_like(radii, dtype=int))

    def test_final_bin_includes_outer_boundary(self):
        radii = np.array([24.999, 25.0])
        mask = radial_bin_mask(radii, RADIAL_BINS[-1])
        np.testing.assert_array_equal(mask, np.array([True, True]))

    def test_half_open_bins_do_not_double_count_interfaces(self):
        radii = np.array([5.0, 10.0, 15.0, 20.0])
        masks = [radial_bin_mask(radii, interval) for interval in RADIAL_BINS]
        locations = [int(np.flatnonzero(mask)[0]) for mask in masks if np.any(mask)]
        self.assertEqual(locations, [0, 1, 2, 3])

    def test_weighted_mean_uses_source_weights(self):
        values = np.array([1.0, 3.0, 8.0])
        weights = np.array([1.0, 2.0, 1.0])
        self.assertAlmostEqual(weighted_mean(values, weights), 3.75, places=14)

    def test_weighted_mean_rejects_empty_source_bin(self):
        with self.assertRaises(ValueError):
            weighted_mean(np.array([1.0, 2.0]), np.array([0.0, 0.0]))


if __name__ == "__main__":
    unittest.main()
