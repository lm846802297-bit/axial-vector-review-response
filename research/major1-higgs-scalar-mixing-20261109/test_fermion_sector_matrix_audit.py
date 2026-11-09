import unittest
import numpy as np
from fermion_sector_matrix_audit import BENCHMARKS, run_benchmark

class FermionSectorMatrixAuditTests(unittest.TestCase):
    def test_offdiagonal_reproduces_archived_exact_mass_eigenstate_result(self):
        for label,vs,ma in BENCHMARKS:
            result=run_benchmark(label,vs,ma)
            expected={"A_open_AA":(0.11313331009059611,0.0240304439859),
                      "B_closed_AA":(0.02545910994964451,0.00540772399471)}[label]
            self.assertAlmostEqual(result["hs"]["Pi_RC_mh2_GeV2"][1],expected[0],places=9)
            self.assertAlmostEqual(result["hs"]["hard_momentum_difference_PiB_GeV2"][0],expected[1],places=8)

    def test_absorptive_matrix_is_positive_semidefinite_and_rank_one(self):
        for label,vs,ma in BENCHMARKS:
            result=run_benchmark(label,vs,ma)
            eigenvalues=np.asarray(result["absorptive_eigenvalues_GeV2"])
            self.assertGreaterEqual(eigenvalues[0],-1e-10)
            self.assertGreater(eigenvalues[1],0.0)
            self.assertAlmostEqual(result["absorptive_offdiagonal_saturation_ratio"],1.0,places=8)

    def test_diagonal_and_offdiagonal_uv_derivative_structures_differ(self):
        for label,vs,ma in BENCHMARKS:
            result=run_benchmark(label,vs,ma)
            self.assertGreater(abs(result["hh"]["UV_p2_coefficient_sum_C"][0]),1.0)
            self.assertGreater(abs(result["ss"]["UV_p2_coefficient_sum_C"][0]),0.1)
            self.assertLess(abs(result["hs"]["UV_p2_coefficient_sum_C"][0]),1e-12)

    def test_full_minus_light_field_counterterm_coefficients(self):
        expected = {
            "A_open_AA": {
                "hh": -0.016712307066340585,
                "hs": 2.2983060235058633e-06,
                "ss": -0.07985086735189965,
            },
            "B_closed_AA": {
                "hh": -0.016712307066340585,
                "hs": 5.172024552583982e-07,
                "ss": -0.004043757309967427,
            },
        }
        for label,vs,ma in BENCHMARKS:
            result=run_benchmark(label,vs,ma)
            for entry in ("hh","hs","ss"):
                self.assertAlmostEqual(
                    result[entry]["MS_field_counterterm_pole_coefficient_full_minus_light"],
                    expected[label][entry], places=10
                )

    def test_hard_fermion_momentum_differences_are_real_below_heavy_threshold(self):
        for label,vs,ma in BENCHMARKS:
            result=run_benchmark(label,vs,ma)
            for entry in ("hh","hs","ss"):
                self.assertLess(abs(result[entry]["hard_momentum_difference_PiB_GeV2"][1]),1e-9)

if __name__=="__main__":
    unittest.main()
