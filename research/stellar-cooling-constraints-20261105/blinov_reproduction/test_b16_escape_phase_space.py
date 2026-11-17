import unittest

import numpy as np

from audit_b16_escape_phase_space import (
    _axis_bins, reconstruct_energy_grid_from_spectral_measure,
)


class EscapePhaseSpaceBinningTests(unittest.TestCase):
    def setUp(self):
        self.r = np.array([6.0, 9.0, 11.0, 14.0, 18.0])
        self.energies = np.array([10.5, 11.5, 12.5, 15.5])
        self.angles = np.array([-0.8, -0.2, 0.2, 0.8])
        self.region_mask = np.array([False, True, True, True, False])
        self.base = np.arange(1, 5 * 4 * 4 + 1, dtype=float).reshape(5, 4, 4)
        survival = np.linspace(0.05, 0.95, self.base.size).reshape(self.base.shape)
        self.escaped = self.base * survival
        self.tau = -np.log(survival)
        self.global_thin = float(np.sum(self.base))
        self.global_escaped = float(np.sum(self.escaped))
        self.region_thin = float(np.sum(self.base[self.region_mask]))
        self.region_escaped = float(np.sum(self.escaped[self.region_mask]))

    def assert_region_partition(self, rows):
        self.assertAlmostEqual(
            sum(x["thin_source_fraction_within_region"] for x in rows), 1.0, places=13
        )
        self.assertAlmostEqual(
            sum(x["escaped_luminosity_fraction_within_region"] for x in rows),
            1.0,
            places=13,
        )
        self.assertAlmostEqual(
            sum(x["thin_source_fraction_of_global"] for x in rows),
            self.region_thin / self.global_thin,
            places=13,
        )
        self.assertAlmostEqual(
            sum(x["escaped_luminosity_fraction_of_global"] for x in rows),
            self.region_escaped / self.global_escaped,
            places=13,
        )

    def test_energy_bins_are_restricted_to_emission_region(self):
        edges = np.array([10.0, 12.0, 14.0, 16.0])
        names = ["10-12", "12-14", "14-16"]
        rows = _axis_bins(
            "energy", edges, names, self.region_mask, self.r, self.energies,
            self.angles, self.base, self.escaped, self.tau,
            self.global_thin, self.global_escaped, self.region_thin,
            self.region_escaped, 1.0
        )
        self.assert_region_partition(rows)

    def test_direction_bins_are_restricted_to_emission_region(self):
        edges = np.array([-1.0, 0.0, 1.0])
        names = ["inward", "outward"]
        rows = _axis_bins(
            "direction", edges, names, self.region_mask, self.r, self.energies,
            self.angles, self.base, self.escaped, self.tau,
            self.global_thin, self.global_escaped, self.region_thin,
            self.region_escaped, 1.0
        )
        self.assert_region_partition(rows)

    def test_all_emission_region_matches_global_partition(self):
        mask = np.ones_like(self.region_mask, dtype=bool)
        rows = _axis_bins(
            "energy", np.array([10.0, 12.0, 14.0, 16.0]),
            ["10-12", "12-14", "14-16"], mask, self.r, self.energies,
            self.angles, self.base, self.escaped, self.tau,
            self.global_thin, self.global_escaped, self.global_thin,
            self.global_escaped, 1.0
        )
        self.assertAlmostEqual(
            sum(x["thin_source_fraction_within_region"] for x in rows), 1.0, places=13
        )
        self.assertAlmostEqual(
            sum(x["escaped_luminosity_fraction_within_region"] for x in rows),
            1.0,
            places=13,
        )

    def test_archived_spectral_measure_reconstructs_842_energy_nodes(self):
        from pathlib import Path
        import json

        here = Path(__file__).resolve().parent
        baseline_path = here / "outputs" / "b16_global_high_order_independent_grid_10mev_2026-11-09.json"
        payload = json.loads(baseline_path.read_text(encoding="utf-8"))
        baseline = payload["result"]
        spectral = np.asarray(baseline["eq_b1_source_measure"]["spectral_measure_MeV3"], float)
        energies = reconstruct_energy_grid_from_spectral_measure(spectral, 10.0, 1000.0)
        self.assertEqual(len(energies), 842)
        self.assertTrue(np.all(np.diff(energies) > 0.0))
        self.assertGreater(float(energies[0]), 10.0)
        self.assertLessEqual(float(energies[-1]), 1010.0 + 1.0e-10)

    def test_spectral_measure_inversion_round_trip(self):
        energies = np.asarray([10.00001, 10.01, 10.5, 12.0, 100.0, 1010.0])
        spectral = energies**2 * np.sqrt(energies**2 - 10.0**2) / (2.0 * np.pi**2)
        reconstructed = reconstruct_energy_grid_from_spectral_measure(spectral, 10.0, 1000.0)
        self.assertTrue(np.allclose(reconstructed, energies, rtol=5.0e-14, atol=1.0e-13))

    def test_spectral_measure_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            reconstruct_energy_grid_from_spectral_measure([1.0, 0.0], 10.0, 1000.0)


if __name__ == "__main__":
    unittest.main()
