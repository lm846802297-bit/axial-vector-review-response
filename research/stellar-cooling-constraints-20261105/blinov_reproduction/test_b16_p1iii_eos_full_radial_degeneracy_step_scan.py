import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_degeneracy_step_scan import (
    SELECTED_STEP_LABEL,
    STEP_LABELS,
    analyze_profile,
    load_c2_reference,
)
from audit_b16_p1iii_eos_full_radial_occupation import load_profile

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestFullRadialDegeneracyStepScan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        profile = load_profile(PROFILE)
        reference = load_c2_reference(C2_REFERENCE)
        cls.records, cls.summary = analyze_profile(profile, reference)

    def test_full_radial_step_scan_shape(self):
        self.assertEqual(len(self.records), 301*2*9)
        self.assertEqual(tuple(STEP_LABELS), (
            "1e-2", "3e-3", "1e-3", "3e-4", "2e-4",
            "1e-4", "3e-5", "1e-5", "3e-6",
        ))

    def test_selected_step_closes_both_species(self):
        for species in ("n", "p"):
            self.assertLess(
                self.summary["species"][species][SELECTED_STEP_LABEL]["max_abs_relative"],
                1e-8,
            )
        self.assertAlmostEqual(
            self.summary["selected_shared_step"]["step_fraction_h_over_T"],
            3e-5,
            places=14,
        )

    def test_large_step_error_has_second_order_scaling(self):
        for species in ("n", "p"):
            ratio = self.summary["truncation_scaling_ratio"][species][
                "max_error_ratio_1e_2_over_1e_3"
            ]
            self.assertGreater(ratio, 80.0)
            self.assertLess(ratio, 120.0)

    def test_all_factors_and_derivatives_are_physical(self):
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))
        for row in self.records:
            self.assertGreater(row["F_direct"], 0.0)
            self.assertLess(row["F_direct"], 1.0)
            self.assertGreater(row["F_density_derivative"], 0.0)


if __name__ == "__main__":
    unittest.main()
