import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import (
    EXPECTED_PROFILE_SHA256,
    _integrals,
    load_profile,
    state_from_profile_row,
)
from audit_b16_p1iii_eos_nucleon_distribution import (
    HBARC_MEV_FM,
    phase_space_integrals,
    state_from_available_volume_density,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"


class TestFullRadialEOSOccupation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_profile(PROFILE)

    def test_pinned_full_radial_input_and_grid(self):
        self.assertEqual(len(self.rows), 301)
        self.assertAlmostEqual(self.rows[0]["r_km"], 0.2, places=12)
        self.assertAlmostEqual(self.rows[-1]["r_km"], 15.2, places=12)
        for left, right in zip(self.rows[:-1], self.rows[1:]):
            self.assertAlmostEqual(right["r_km"]-left["r_km"], 0.05, places=10)
        self.assertEqual(
            EXPECTED_PROFILE_SHA256,
            "97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59",
        )

    def test_fiorillo_chemical_potential_convention(self):
        row = min(self.rows, key=lambda item: abs(item["r_km"]-8.8))
        state = state_from_profile_row(row, "p")
        expected_nu = row["mu_p_nonrel_MeV"]-row["U_p_MeV"]
        self.assertAlmostEqual(state.effective_chemical_potential_mev, expected_nu, places=13)
        number, blocked = phase_space_integrals(state, order=512)
        self.assertGreater(number, 0.0)
        self.assertGreaterEqual(blocked, 0.0)
        self.assertLessEqual(blocked, number)

    def test_density_matched_diagnostic_reproduces_eos_target(self):
        row = min(self.rows, key=lambda item: abs(item["r_km"]-14.85))
        target_per_available = row["X_p"]*row["nB_fm3"]/row["xi_SPP"]
        matched = state_from_available_volume_density(
            "p", row["T_MeV"], row["mstar_p_MeV"],
            target_per_available, order=512,
        )
        number, _ = phase_space_integrals(matched, order=2048)
        reconstructed = number/HBARC_MEV_FM**3
        self.assertLess(abs(reconstructed/target_per_available-1.0), 1e-8)

    def test_quadrature_convergence_at_core_and_outer_points(self):
        for radius in (1.0, 8.8, 14.85):
            row = min(self.rows, key=lambda item: abs(item["r_km"]-radius))
            for species in ("n", "p"):
                state = state_from_profile_row(row, species)
                n512, b512 = _integrals(state, 512)
                n2048, b2048 = _integrals(state, 2048)
                self.assertLess(abs(n2048/n512-1.0), 1e-10)
                self.assertLess(abs(b2048/n2048-b512/n512), 1e-10)

    def test_free_nucleons_are_not_forced_to_sum_to_total_baryon_density(self):
        row = min(self.rows, key=lambda item: abs(item["r_km"]-14.85))
        self.assertGreater(1.0-row["X_n"]-row["X_p"], 0.08)
        self.assertGreater(row["xi_SPP"], 0.97)


if __name__ == "__main__":
    unittest.main()
