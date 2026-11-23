import unittest

import numpy as np

from diagnose_b16_energy_grid_identity import build_energy_grid
from energy_grid_identity import compare_energy_grid


class EnergyGridIdentityTests(unittest.TestCase):
    def test_grid_is_sorted_unique_and_above_threshold(self):
        lapse = np.array([0.90, 0.85, 0.80])
        grid, details = build_energy_grid(
            mass=10.0, energy_order=200, energy_offset=1000.0, lapse=lapse
        )
        self.assertTrue(np.all(np.diff(grid) > 0.0))
        self.assertTrue(np.all(grid > 10.0 * (1.0 + 1.0e-10)))
        self.assertEqual(details["seed_node_count"], 200)
        self.assertEqual(details["lapse_threshold_node_count"], 3)
        self.assertEqual(details["filtered_node_count"], len(grid))

    def test_lapse_thresholds_are_included(self):
        lapse = np.array([0.90, 0.80])
        grid, _ = build_energy_grid(
            mass=10.0, energy_order=20, energy_offset=100.0, lapse=lapse
        )
        for threshold in 10.0 / lapse:
            self.assertTrue(np.any(grid == threshold))

    def test_identical_lapse_gives_identical_hashable_grid(self):
        lapse = np.linspace(0.70, 0.95, 642)
        first, _ = build_energy_grid(10.0, 200, 1000.0, lapse)
        second, _ = build_energy_grid(10.0, 200, 1000.0, lapse.copy())
        np.testing.assert_array_equal(first, second)

    def test_one_ulp_platform_roundoff_is_accepted(self):
        reference_nodes = np.linspace(10.0, 1010.0, 842)
        actual_nodes = reference_nodes.copy()
        actual_nodes[486] = np.nextafter(actual_nodes[486], np.inf)
        report = compare_energy_grid(actual_nodes, {"_nodes": reference_nodes})
        self.assertTrue(report["matches"])
        self.assertLessEqual(report["max_relative_difference"], 5.0e-15)
        self.assertGreater(report["max_ulp_difference"], 0.0)

    def test_material_energy_grid_shift_is_rejected(self):
        reference_nodes = np.linspace(10.0, 1010.0, 842)
        actual_nodes = reference_nodes.copy()
        actual_nodes[486] *= 1.0 + 1.0e-10
        report = compare_energy_grid(actual_nodes, {"_nodes": reference_nodes})
        self.assertFalse(report["matches"])

    def test_energy_grid_node_count_mismatch_is_rejected(self):
        reference_nodes = np.linspace(10.0, 1010.0, 842)
        report = compare_energy_grid(reference_nodes[:-1], {"_nodes": reference_nodes})
        self.assertFalse(report["matches"])
        self.assertEqual(report["actual_node_count"], 841)
        self.assertEqual(report["reference_node_count"], 842)


if __name__ == "__main__":
    unittest.main()
