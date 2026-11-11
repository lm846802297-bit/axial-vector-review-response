import json
import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import (
    analyze,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestC4C1ExactOutgoingEnergySupport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local, cls.support, cls.cold, cls.summary = analyze(
            load_profile(PROFILE),
            load_c2_reference(C2_REFERENCE),
        )

    def test_all_local_species_radius_and_cp_conjugate_cases(self):
        self.assertEqual(len(self.local), 16)
        self.assertEqual(len(self.support), 16)
        self.assertEqual(len(self.cold), 4)
        self.assertEqual(
            sorted(set(row["r_km"] for row in self.local)),
            [0.2, 5.0, 10.0, 15.2],
        )

    def test_support_roots_are_closed(self):
        for row in self.support+self.cold:
            self.assertLess(row["support_root_max_relative_residual"], 1e-7)
            self.assertGreater(row["Eprime_support_max_MeV"], row["Eprime_support_min_MeV"])

    def test_full_energy_quadrature_converges(self):
        for row in self.local:
            self.assertLess(row["relative_convergence_48_to_72"], 1e-2)
            self.assertLess(row["relative_convergence_32_to_72"], 2e-2)
            self.assertGreater(row["gamma_full_order72"], 0.0)

    def test_legacy_window_fraction_is_measured_not_assumed(self):
        for row in self.local:
            self.assertGreaterEqual(row["legacy_window_fraction_of_full_support"], 0.0)
            self.assertLessEqual(row["legacy_window_fraction_of_full_support"], 1.0+1e-8)

    def test_cold_dilute_full_support_recovers_horowitz(self):
        for row in self.cold:
            self.assertLess(abs(row["relative_Horowitz_residual"]), 1e-3)

    def test_strict_json_and_acceptance(self):
        self.assertTrue(all(type(value) is bool for value in self.summary["acceptance"].values()))
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))
        json.dumps(self.summary, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
