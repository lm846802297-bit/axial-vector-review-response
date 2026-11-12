import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b1_effective_mass_weak_tensor import analyze

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"


class TestC4B1EffectiveMassWeakTensor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ward, cls.recovery, cls.summary = analyze(load_profile(PROFILE))

    def test_ward_scan_coverage(self):
        self.assertEqual(len(self.ward), 288)
        self.assertLess(
            self.summary["maxima"]["vector_ward_residual"],
            1e-10,
        )

    def test_vector_ward_identity_for_mixed_mass_spinors(self):
        for row in self.ward:
            self.assertLess(row["ward_VV_first_index"], 1e-10)
            self.assertLess(row["ward_VA_vector_first_index"], 1e-10)
            self.assertLess(row["ward_AV_vector_second_index"], 1e-10)

    def test_hermiticity_and_tensor_decomposition(self):
        for row in self.ward:
            self.assertLess(row["hermiticity_VV"], 1e-10)
            self.assertLess(row["hermiticity_AA"], 1e-10)
            self.assertLess(row["hermiticity_total"], 1e-10)
            self.assertLess(row["decomposition_residual"], 1e-14)

    def test_vacuum_mass_limit_recovers_existing_p1iii_b(self):
        self.assertEqual(len(self.recovery), 40)
        for row in self.recovery:
            self.assertLess(row["relative_HVV_difference"], 1e-12)
            self.assertLess(row["relative_HAA_difference"], 1e-12)
            self.assertLess(row["relative_HVA_difference"], 1e-12)

    def test_neutrino_antineutrino_va_sign_structure(self):
        self.assertEqual(self.summary["provenance"]["VA_sign_cases"], 8)
        self.assertLess(
            self.summary["maxima"]["neutrino_antineutrino_VA_sign_residual"],
            1e-10,
        )
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))


if __name__ == "__main__":
    unittest.main()
