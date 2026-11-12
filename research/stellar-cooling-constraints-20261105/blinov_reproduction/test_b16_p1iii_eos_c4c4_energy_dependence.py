import unittest

from audit_b16_p1iii_eos_c4c4_energy_dependence import (
    ENERGY_GRID_MEV,
    NEW_ENERGIES_MEV,
    build_energy_ratios,
    expected_case_keys,
    opacity_and_mean_free_path,
    validate_records,
    git_blob_sha,
    C4C2_REFERENCE_PATH,
    EXPECTED_C4C2_REFERENCE_GIT_BLOB,
    write_csv,
)


class TestC4C4EnergyDependence(unittest.TestCase):
    def test_exploratory_energy_grid_and_reused_baseline(self):
        self.assertEqual(ENERGY_GRID_MEV, (10.0, 20.0, 40.0, 60.0, 100.0, 150.0))
        self.assertEqual(NEW_ENERGIES_MEV, (10.0, 20.0, 40.0, 60.0, 150.0))

    def test_expected_anchor_case_count(self):
        keys = expected_case_keys((0.2, 5.0, 10.0, 15.2))
        self.assertEqual(len(keys), 96)

    def test_opacity_and_mean_free_path_units(self):
        kappa, lam_km = opacity_and_mean_free_path(2.0e-13, 0.5)
        self.assertAlmostEqual(kappa, 1.0e-13, places=27)
        self.assertAlmostEqual(lam_km, 1.973269804e-3, places=15)

    def test_energy_ratios_use_matched_target_and_sign(self):
        rows = []
        for radius in (0.2, 5.0, 10.0, 15.2):
            for species in ("n", "p"):
                for anti in (False, True):
                    for energy, gamma in ((100.0, 2.0), (10.0, 1.0)):
                        rows.append({
                            "E_MeV": energy, "r_km": radius, "species": species,
                            "antinu": str(anti), "gamma_available_volume_MeV": gamma,
                            "sigma_per_target_MeV_minus2": gamma / 10.0,
                            "kappa_sc_MeV": gamma, "lambda_sc_km": 1.0 / gamma,
                            "nprime_fm3": 1.0,
                        })
        ratios = build_energy_ratios(rows)
        ten = next(row for row in ratios if row["E_MeV"] == 10.0 and row["r_km"] == 0.2
                   and row["species"] == "n" and row["antinu"] == "False")
        self.assertAlmostEqual(ten["gamma_over_gamma_100MeV"], 0.5)
        self.assertAlmostEqual(ten["sigma_over_sigma_100MeV"], 0.5)

    def test_c4c2_reference_blob_uses_canonical_git_nul_header(self):
        self.assertEqual(git_blob_sha(C4C2_REFERENCE_PATH), EXPECTED_C4C2_REFERENCE_GIT_BLOB)

    def test_csv_writer_emits_real_newlines(self):
        from tempfile import TemporaryDirectory
        from pathlib import Path
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "probe.csv"
            write_csv(path, [{"a": 1}, {"a": 2}])
            self.assertEqual(path.read_bytes().count(b"\n"), 3)

    def test_structural_acceptance_rejects_duplicate_or_missing_cases(self):
        radii = (0.2, 5.0, 10.0, 15.2)
        rows = []
        for energy in ENERGY_GRID_MEV:
            for radius in radii:
                for species in ("n", "p"):
                    for anti in (False, True):
                        gamma = 1.0e-13
                        xi = 0.8
                        rows.append({
                            "E_MeV": energy, "r_km": radius, "species": species,
                            "antinu": str(anti), "gamma_available_volume_MeV": gamma,
                            "sigma_per_target_MeV_minus2": 1.0e-19,
                            "kappa_sc_MeV": xi * gamma, "lambda_sc_km": 1.0e-3,
                            "support_root_max_relative_residual": 1.0e-12,
                            "xi_SPP": xi,
                            "source": "C4-C2 archived baseline" if energy == 100.0 else "C4-C4 direct recomputation",
                        })
        result = validate_records(rows, radii)
        self.assertTrue(result["numerical_integrity_pass"])
        duplicated = rows + [dict(rows[0])]
        self.assertFalse(validate_records(duplicated, radii)["numerical_integrity_pass"])


if __name__ == "__main__":
    unittest.main()
