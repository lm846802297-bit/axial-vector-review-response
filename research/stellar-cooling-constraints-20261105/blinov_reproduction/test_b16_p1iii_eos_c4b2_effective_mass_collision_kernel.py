import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import (
    analyze,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestC4B2EOSCollisionKernel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local, cls.recovery, cls.cold, cls.summary = analyze(
            load_profile(PROFILE),
            load_c2_reference(C2_REFERENCE),
        )

    def test_mstar_equals_M_recovers_legacy_kernel(self):
        self.assertEqual(len(self.recovery), 4)
        self.assertLess(
            self.summary["maxima"]["mstar_equals_M_P1IIIb_recovery_residual"],
            1e-10,
        )

    def test_cold_dilute_horowitz_limit(self):
        self.assertEqual(len(self.cold), 4)
        self.assertLess(
            self.summary["maxima"]["cold_dilute_Horowitz_relative_residual"],
            1e-3,
        )

    def test_eos_local_grid_and_positive_rates(self):
        self.assertEqual(len(self.local), 16)
        for row in self.local:
            self.assertGreaterEqual(row["gamma_available_volume"], 0.0)
            self.assertGreaterEqual(row["sigma_per_target_MeV_minus2"], 0.0)
            self.assertGreater(row["nprime_fm3"], 0.0)
            self.assertGreater(row["xi_SPP"], 0.0)

    def test_local_fermi_factor_detailed_balance(self):
        self.assertLess(
            self.summary["maxima"]["local_detailed_balance_residual"],
            1e-10,
        )

    def test_quadrature_convergence_and_acceptance(self):
        self.assertLess(
            self.summary["maxima"]["core_local_quadrature_convergence_relative_difference"],
            1e-2,
        )
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))


if __name__ == "__main__":
    unittest.main()
