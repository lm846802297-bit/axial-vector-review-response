import unittest

import numpy as np

from diagnose_b16_energy_grid_identity import build_energy_grid


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


if __name__ == "__main__":
    unittest.main()
