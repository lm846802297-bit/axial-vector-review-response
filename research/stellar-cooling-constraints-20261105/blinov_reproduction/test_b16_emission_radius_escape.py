import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_b16_emission_radius_escape import (
    source_radial_summary, emission_shell_escape_summary,
    emission_absorption_tau_matrix,
)


class B16EmissionRadiusEscapeTests(unittest.TestCase):
    def setUp(self):
        self.radius = np.array([0.5, 1.5, 2.5, 3.5])
        self.edges = [0.0, 2.0, 4.0]
        self.labels = ["0-2 km", "2-4 km"]
        self.source = np.array([
            [1.0, 2.0],
            [3.0, 1.0],
            [2.0, 2.0],
            [1.0, 1.0],
        ])
        self.angle_weights = np.array([0.25, 0.75])

    def test_source_radial_shell_fractions_sum_to_one(self):
        result = source_radial_summary(
            self.radius, self.source, self.edges, self.labels
        )
        self.assertAlmostEqual(
            sum(x["source_fraction"] for x in result["shells"]), 1.0
        )
        self.assertAlmostEqual(result["mean_emission_radius_km"], 2.0)

    def test_emission_shell_escape_probabilities_and_fractions_close(self):
        escape = np.array([
            [0.9, 0.8],
            [0.8, 0.7],
            [0.5, 0.4],
            [0.2, 0.1],
        ])
        result = emission_shell_escape_summary(
            self.radius, self.source, escape, self.edges, self.labels
        )
        self.assertAlmostEqual(
            sum(x["thin_source_fraction"] for x in result), 1.0
        )
        self.assertAlmostEqual(
            sum(x["escaped_luminosity_fraction"] for x in result), 1.0
        )
        self.assertGreater(
            result[0]["mean_escape_probability"],
            result[1]["mean_escape_probability"]
        )

    def test_emission_absorption_tau_matrix_rows_reconstruct_total_tau(self):
        # (absorption shell, source radius, angle, energy)
        columns = np.zeros((2, 4, 2, 2))
        columns[0] = 0.5
        columns[1] = 1.5
        result = emission_absorption_tau_matrix(
            self.radius, self.source, self.angle_weights,
            columns, self.edges, self.labels
        )
        self.assertEqual(len(result), 2)
        for row in result:
            self.assertAlmostEqual(row["mean_total_tau_per_g2"], 2.0)
            self.assertAlmostEqual(
                sum(x["mean_tau_per_g2"] for x in row["mean_tau_by_absorption_shell"]),
                row["mean_total_tau_per_g2"]
            )

    def test_zero_source_shell_returns_none_mean_tau_without_nan(self):
        source = self.source.copy()
        source[:2] = 0.0
        result = source_radial_summary(
            self.radius, source, self.edges, self.labels
        )
        self.assertEqual(result["shells"][0]["source_fraction"], 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
