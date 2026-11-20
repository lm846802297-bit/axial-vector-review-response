from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

import archive_croon_c1_10mev as archive


class C1ArchiveUnitTests(unittest.TestCase):
    def test_flatten_nested_coupling_record(self):
        flattened = archive.flatten({
            "g_X": 1.0e-5,
            "Rfar": {"L": 1.0, "+": 2.0, "-": 3.0},
            "relative_error": 1.0e-8,
        })
        self.assertEqual(list(flattened), ["g_X", "Rfar_L", "Rfar_+", "Rfar_-", "relative_error"])
        self.assertEqual(flattened["Rfar_+"], 2.0)
        self.assertEqual(archive.unit_curve("Rfar_Rnu_adaptive_quad"), "erg s^-1")
        self.assertEqual(archive.unit_curve("Rfar_Rnu_adaptive_quad_relative_error_estimate"), "1")

    def test_profile_units_are_explicit(self):
        self.assertEqual(archive.unit_profile("r_km"), "km")
        self.assertEqual(archive.unit_profile("T_MeV"), "MeV")
        self.assertEqual(archive.unit_profile("chi_mu_minus_MeV3"), "MeV^3")
        self.assertEqual(archive.unit_profile("Q_B13_mu_minus_per_g2_MeV5"), "MeV^5")
        self.assertEqual(archive.unit_profile("B13_mu_pm_over_Croon_Eq47"), "1")
        with self.assertRaises(ValueError):
            archive.unit_profile("unlabelled_column")

    def test_validation_status_does_not_hide_partial_scope(self):
        checks = [{"status": "passed"}, {"status": "partial"}, {"status": "not_run"}]
        self.assertEqual(archive.status(checks), "partial")
        self.assertEqual(archive.status([{"status": "passed"}]), "passed")
        self.assertEqual(archive.status([{"status": "failed"}]), "failed")

    def test_export_all_121_coupling_points(self):
        root = Path(__file__).resolve().parents[3]
        final_path = root / archive.P["finalj"]
        if not final_path.is_file():
            self.skipTest("C1 archived output is not present in this checkout")
        final = archive.load(final_path)
        curve = final["masses"]["10"]["coupling_curve"]
        self.assertEqual(len(curve), 121)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "coupling_curve.csv"
            columns, units, rows = archive.write_curve(path, curve)
            self.assertEqual(rows, 121)
            self.assertEqual(len(columns), len(units))
            self.assertEqual(set(columns), set(units))
            with path.open(newline="", encoding="utf-8") as handle:
                csv_rows = list(csv.DictReader(handle))
            self.assertEqual(len(csv_rows), 121)
            self.assertEqual(float(csv_rows[0]["g_X"]), curve[0]["g_X"])
            self.assertEqual(float(csv_rows[-1]["g_X"]), curve[-1]["g_X"])

    def test_existing_convergence_records_meet_acceptance(self):
        root = Path(__file__).resolve().parents[3]
        radial_path = root / archive.P["radial"]
        energy_path = root / archive.P["energy"]
        if not radial_path.is_file() or not energy_path.is_file():
            self.skipTest("C1 convergence reports are not present in this checkout")
        radial = archive.load(radial_path)
        energy = archive.load(energy_path)
        radial_grid = radial["radial_grid_convergence"]
        self.assertTrue(radial_grid["one_percent_target_met"])
        self.assertTrue(radial_grid["all_boundaries_and_modes_below_0_12_percent"])
        self.assertLess(radial_grid["max_relevant_pointwise_relative_difference_all_boundaries_and_modes"], 0.0012)
        self.assertEqual(energy["status"], "PASS")
        self.assertLess(energy["maximum_over_all_reported_metrics"], energy["target"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
