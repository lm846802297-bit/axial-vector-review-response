import unittest

import numpy as np

from audit_b16_escape_phase_space import (
    _axis_bins, reconstruct_energy_grid_from_spectral_measure,
    write_phase_space_csv, write_phase_space_svg,
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


    def test_joint_phase_space_csv_export_contains_all_regions(self):
        import csv
        import tempfile
        from pathlib import Path

        fixture = self._export_fixture()
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "phase_space.csv"
            metadata = write_phase_space_csv(fixture, target)
            with target.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(metadata["rows"], 3)
            self.assertEqual(len(rows), 3)
            self.assertEqual(metadata["columns"], 13)
            self.assertEqual(rows[0]["region"], "all_emission_radii")
            self.assertEqual(rows[-1]["region"], "dominant_8_15km_emission")
            self.assertTrue(metadata["sha256"])
            self.assertGreater(metadata["bytes"], 0)

    def test_direction_resolved_svg_export(self):
        import tempfile
        from pathlib import Path

        fixture = self._export_fixture()
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "phase_space.svg"
            metadata = write_phase_space_svg(fixture, target)
            svg = target.read_text(encoding="utf-8")
            self.assertEqual(metadata["panels"], 4)
            self.assertIn("B.16 10 MeV escaping phase space", svg)
            self.assertIn("0 to 1 cos(theta)", svg)
            self.assertIn("escaped-luminosity fraction", svg)
            self.assertTrue(svg.rstrip().endswith("</svg>"))
            self.assertTrue(metadata["sha256"])

    @staticmethod
    def _export_fixture():
        common = {
            "thin_source_erg_s_per_g2": 10.0,
            "escaped_luminosity_erg_s": 1.0,
            "thin_source_fraction_of_global": 0.5,
            "thin_source_fraction_within_region": 0.5,
            "escaped_luminosity_fraction_of_global": 0.5,
            "escaped_luminosity_fraction_within_region": 0.5,
            "mean_escape_probability": 0.1,
            "mean_tau_source_weighted": 2.0,
            "mean_tau_escape_weighted": 1.0,
        }
        all_cells = [
            {
                "emission_shell": "0-5 km",
                "energy_bin": "10-12 MeV",
                "direction_bin": "-1-0 cos(theta)",
                **common,
            },
            {
                "emission_shell": "5-10 km",
                "energy_bin": "12-15 MeV",
                "direction_bin": "0-1 cos(theta)",
                **{**common, "escaped_luminosity_fraction_within_region": 0.25},
            },
        ]
        core_cells = [{
            "emission_shell": "5-10 km",
            "energy_bin": "12-15 MeV",
            "direction_bin": "0-1 cos(theta)",
            **common,
        }]
        return {
            "mass_MeV": 10.0,
            "escape_probability": 1.0e-3,
            "relative_difference_vs_fig7": 0.9,
            "configuration": {
                "emission_shell_edges_km": [0.0, 5.0, 10.0],
                "energy_bin_edges_MeV": [10.0, 12.0, 15.0],
                "direction_edges_4": [-1.0, 0.0, 1.0],
            },
            "regions": [
                {
                    "region": "all_emission_radii",
                    "emission_radius_bins": [{"bin": "0-5 km"}, {"bin": "5-10 km"}],
                    "joint_radius_energy_direction_bins": all_cells,
                },
                {
                    "region": "dominant_8_15km_emission",
                    "emission_radius_bins": [{"bin": "5-10 km"}],
                    "joint_radius_energy_direction_bins": core_cells,
                },
            ],
        }


if __name__ == "__main__":
    unittest.main()
