import csv
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "outputs" / "p1iiie_c4c2_full_angle_eprime_convergence_2026-11-11.csv"
JSON_PATH = HERE / "outputs" / "p1iiie_c4c2_full_angle_eprime_convergence_2026-11-11.json"


class TestC4C2FullAngleEprimeConvergence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        with CSV_PATH.open(newline="", encoding="utf-8") as stream:
            cls.rows = list(csv.DictReader(stream))

    def test_all_16_radius_species_sign_cases(self):
        self.assertEqual(len(self.rows), 16)
        self.assertEqual({float(row["r_km"]) for row in self.rows}, {0.2, 5.0, 10.0, 15.2})
        self.assertEqual({row["species"] for row in self.rows}, {"n", "p"})
        self.assertEqual({row["antinu"] for row in self.rows}, {"True", "False"})

    def test_full_angle_rates_are_positive(self):
        for row in self.rows:
            self.assertGreater(float(row["gamma_full_angle_Eprime48_MeV"]), 0.0)
            self.assertGreater(float(row["gamma_full_angle_Eprime72_MeV"]), 0.0)

    def test_full_angle_energy_quadrature_converges(self):
        self.assertLess(
            self.summary["maxima"]["full_angle_Eprime_48_to_72_relative_difference"],
            1e-2,
        )
        self.assertLess(
            self.summary["maxima"]["support_root_relative_residual"],
            1e-7,
        )

    def test_strict_json_and_acceptance(self):
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))
        self.assertTrue(all(type(value) is bool for value in self.summary["acceptance"].values()))
        json.dumps(self.summary, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
