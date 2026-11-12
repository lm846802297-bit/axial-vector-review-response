import unittest

from audit_b16_p1iii_eos_c4c4_quadrature_convergence import (
    NEW_ENERGIES_MEV,
    RELATIVE_TOLERANCE,
    evaluate_rows,
    expected_keys,
    relative_difference,
)


class TestC4C4QuadratureConvergence(unittest.TestCase):
    def test_five_energy_grid_and_80_cases(self):
        self.assertEqual(NEW_ENERGIES_MEV, (10.0, 20.0, 40.0, 60.0, 150.0))
        self.assertEqual(len(expected_keys((0.2, 5.0, 10.0, 15.2))), 80)

    def test_relative_difference_is_symmetric_absolute_fraction(self):
        self.assertAlmostEqual(relative_difference(1.01, 1.0), 0.01)
        self.assertAlmostEqual(relative_difference(0.99, 1.0), 0.01)

    def test_combined_quadrature_threshold(self):
        radii = (0.2, 5.0, 10.0, 15.2)
        rows = []
        for energy in NEW_ENERGIES_MEV:
            for radius in radii:
                for species in ("n", "p"):
                    for anti in (False, True):
                        rows.append({
                            "E_MeV": energy, "r_km": radius, "species": species,
                            "antinu": str(anti), "gamma_base_MeV": 1.0,
                            "gamma_high_MeV": 1.002, "relative_difference": 0.002,
                            "support_root_max_relative_residual": 1e-12,
                        })
        result = evaluate_rows(rows, radii)
        self.assertTrue(result["numerical_integrity_pass"])
        self.assertTrue(result["quadrature_convergence_pass"])
        self.assertLess(result["max_relative_difference"], RELATIVE_TOLERANCE)
        rows[0]["relative_difference"] = 0.02
        result = evaluate_rows(rows, radii)
        self.assertTrue(result["numerical_integrity_pass"])
        self.assertFalse(result["quadrature_convergence_pass"])

    def test_duplicate_or_missing_case_is_detected(self):
        radii = (0.2, 5.0, 10.0, 15.2)
        rows = []
        for energy in NEW_ENERGIES_MEV:
            for radius in radii:
                for species in ("n", "p"):
                    for anti in (False, True):
                        rows.append({
                            "E_MeV": energy, "r_km": radius, "species": species,
                            "antinu": str(anti), "gamma_base_MeV": 1.0,
                            "gamma_high_MeV": 1.0, "relative_difference": 0.0,
                            "support_root_max_relative_residual": 1e-12,
                        })
        self.assertTrue(evaluate_rows(rows, radii)["numerical_integrity_pass"])
        self.assertFalse(evaluate_rows(rows[:-1], radii)["numerical_integrity_pass"])
        self.assertFalse(evaluate_rows(rows + [dict(rows[0])], radii)["numerical_integrity_pass"])


if __name__ == "__main__":
    unittest.main()
