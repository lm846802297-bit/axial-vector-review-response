import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_degeneracy_identity import (
    STEP_FRACTION,
    analyze_profile,
    load_c2_reference,
)
from audit_b16_p1iii_eos_full_radial_occupation import load_profile

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestFullRadialDegeneracyIdentity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = load_profile(PROFILE)
        cls.reference = load_c2_reference(C2_REFERENCE)
        cls.records, cls.summary = analyze_profile(cls.profile, cls.reference)

    def test_full_radial_grid_and_pinned_inputs(self):
        self.assertEqual(len(self.records), 301)
        self.assertEqual(len(self.reference), 301)
        self.assertAlmostEqual(self.records[0]["r_km"], 0.2, places=12)
        self.assertAlmostEqual(self.records[-1]["r_km"], 15.2, places=12)
        self.assertEqual(STEP_FRACTION, 3.0e-5)

    def test_density_derivative_identity_closes_for_both_species(self):
        for species in ("n", "p"):
            self.assertLess(
                self.summary["species"][species]["max_abs_relative_difference"],
                1.0e-8,
            )

    def test_direct_integral_reproduces_archived_c2_factor(self):
        for species in ("n", "p"):
            self.assertLess(
                self.summary["species"][species]["max_abs_direct_vs_C2_reference"],
                5.0e-12,
            )

    def test_local_factors_are_physical_and_summary_passes(self):
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))
        for row in self.records:
            for species in ("n", "p"):
                self.assertGreater(row[f"{species}_F_direct"], 0.0)
                self.assertLess(row[f"{species}_F_direct"], 1.0)
                self.assertGreater(row[f"{species}_F_density_derivative"], 0.0)
                self.assertLess(row[f"{species}_F_density_derivative"], 1.0)


if __name__ == "__main__":
    unittest.main()
