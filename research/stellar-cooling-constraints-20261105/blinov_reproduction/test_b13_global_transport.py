import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import blinov_reproduction.audit_b13_global_transport as audit


class B13GlobalTransportTests(unittest.TestCase):
    def setUp(self):
        self.source = np.array([[1.0, 2.0], [3.0, 4.0]])
        audit._B16_SOURCE = self.source.copy()
        self.couplings = np.array([0.1, 0.2])
        self.reference = np.array([0.1, 0.2])
        self.angle_weights = np.array([0.25, 0.75])


    def test_archived_baseline_selects_matching_mass(self):
        archived = {
            "results": [
                {"mass_MeV": 0.1, "tag": "low"},
                {"mass_MeV": 1.0, "tag": "intermediate"},
                {"mass_MeV": 10.0, "tag": "high"},
            ]
        }
        selected = audit._select_archived_baseline_result(archived, 1.0)
        self.assertEqual(selected["tag"], "intermediate")

    def test_archived_baseline_rejects_missing_or_duplicate_mass(self):
        with self.assertRaises(ValueError):
            audit._select_archived_baseline_result(
                {"results": [{"mass_MeV": 0.1}]}, 1.0
            )
        with self.assertRaises(ValueError):
            audit._select_archived_baseline_result(
                {"results": [
                    {"mass_MeV": 1.0}, {"mass_MeV": 1.0}
                ]}, 1.0
            )

    def test_zero_opacity_gives_unit_escape_probability(self):
        columns = np.zeros((2, 2, 2))
        result = audit._luminosity_curve(
            self.source, columns, self.couplings,
            self.reference, self.angle_weights
        )
        for row in result["points"]:
            self.assertAlmostEqual(row["escape_fraction"], 1.0, places=14)
            self.assertAlmostEqual(
                row["calculated_luminosity_erg_s"],
                row["optically_thin_luminosity_erg_s"],
                places=14,
            )

    def test_positive_opacity_suppresses_escape(self):
        columns = np.full((2, 2, 2), 3.0)
        result = audit._luminosity_curve(
            self.source, columns, self.couplings,
            self.reference, self.angle_weights
        )
        for row in result["points"]:
            self.assertGreater(row["escape_fraction"], 0.0)
            self.assertLess(row["escape_fraction"], 1.0)

    def test_curve_metrics_identify_peak_and_endpoints(self):
        reference = np.array([1.0, 4.0, 2.0])
        calculated = np.array([1.1, 3.8, 2.4])
        metrics = audit._curve_metrics(calculated, reference)
        self.assertAlmostEqual(metrics["weak_endpoint_relative_difference"], 0.1)
        self.assertAlmostEqual(metrics["reference_peak_relative_difference"], -0.05)
        self.assertAlmostEqual(metrics["strong_endpoint_relative_difference"], 0.2)


if __name__ == "__main__":
    unittest.main()
