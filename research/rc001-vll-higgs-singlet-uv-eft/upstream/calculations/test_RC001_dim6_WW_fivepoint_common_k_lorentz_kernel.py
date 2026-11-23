#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-common-k-lorentz-kernel.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_common_k_kernel", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001Dim6WWFivepointCommonKKernel(unittest.TestCase):
    def test_oriented_endpoint_wtis_and_full_audit(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        self.assertIn("PASS: six pairwise arbitrary-current contractions", output.getvalue())
        self.assertIn("R_FG diagnostic", output.getvalue())

    def test_both_propagator_orientations_have_same_remainder(self):
        D0, Dq, Rfg, cross, same, checks = MOD.verify_common_kernels()
        self.assertEqual(checks, 16)
        self.assertTrue(MOD.matrix_zero(cross - same))
        self.assertTrue(MOD.matrix_zero(cross - (D0 - Dq + Rfg)))

    def test_six_pair_current_contractions(self):
        D0, Dq, Rfg, cross, same, _ = MOD.verify_common_kernels()
        self.assertEqual(
            MOD.verify_six_pair_current_kernels(D0, Dq, Rfg, cross, same),
            96,
        )

    def test_scalar_seagull_tensors_are_kept_separate(self):
        self.assertEqual(MOD.verify_scalar_seagull_decompositions(), 3)

    def test_feynman_gauge_remainder_is_nonzero(self):
        k2, kq2, Rfg = MOD.verify_rfg_nonzero()
        self.assertEqual((k2, kq2), (5, 11))
        self.assertEqual(Rfg[0, 0], -MOD.sp.Rational(7, 55))


if __name__ == "__main__":
    unittest.main(verbosity=2)
