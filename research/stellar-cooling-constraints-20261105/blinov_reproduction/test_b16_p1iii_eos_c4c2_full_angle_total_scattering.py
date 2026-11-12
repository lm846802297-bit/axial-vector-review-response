import json
import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4c2_full_angle_total_scattering import (
    analyze,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestC4C2FullAngleTotalScattering(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (
            cls.local,
            cls.cold,
            cls.angle_local,
            cls.kernel_order,
            cls.angle_cold,
            cls.summary,
        ) = analyze(load_profile(PROFILE), load_c2_reference(C2_REFERENCE))

    def test_full_phase_space_case_counts(self):
        self.assertEqual(len(self.local), 16)
        self.assertEqual(len(self.cold), 4)
        self.assertEqual(len(self.angle_local), 4)
        self.assertEqual(len(self.kernel_order), 2)
        self.assertEqual(len(self.angle_cold), 4)

    def test_cold_dilute_total_horowitz_recovery(self):
        for row in self.cold:
            self.assertLess(abs(row["relative_total_Horowitz_residual"]), 1e-3)
            self.assertGreater(row["sigma_dynamic_total_MeV_minus2"], 0.0)

    def test_horowitz_angle_quadrature(self):
        for row in self.angle_cold:
            self.assertLess(
                row["relative_cos16_to_cos32_difference"],
                1e-4,
            )

    def test_local_angle_quadrature(self):
        for row in self.angle_local:
            self.assertLess(
                row["relative_cos8_to_cos12_difference"],
                1e-2,
            )

    def test_local_initial_momentum_and_azimuth_quadrature(self):
        for row in self.kernel_order:
            self.assertLess(
                row["relative_kernel_order_difference"],
                1e-2,
            )

    def test_all_local_total_rates_are_positive(self):
        for row in self.local:
            self.assertGreater(row["gamma_total_available_volume_MeV"], 0.0)
            self.assertGreater(row["sigma_total_per_target_MeV_minus2"], 0.0)
            self.assertGreater(row["xi_times_gamma_total_MeV"], 0.0)

    def test_strict_json_and_all_acceptance_criteria(self):
        self.assertTrue(all(type(value) is bool for value in self.summary["acceptance"].values()))
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))
        json.dumps(self.summary, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
