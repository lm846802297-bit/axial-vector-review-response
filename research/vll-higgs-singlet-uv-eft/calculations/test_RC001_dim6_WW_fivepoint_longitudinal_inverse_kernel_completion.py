#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-longitudinal-inverse-kernel-completion.py"
SPEC = importlib.util.spec_from_file_location("rc001_longitudinal_inverse_completion", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001LongitudinalInverseKernelCompletion(unittest.TestCase):
    def test_transverse_kernel_remainder(self):
        self.assertEqual(MOD.verify_transverse_kernel_remainder(), 16)

    def test_longitudinal_piece_is_minus_rfg(self):
        self.assertEqual(MOD.verify_longitudinal_piece_cancels_rfg(), 16)

    def test_full_feynman_gauge_inverse_kernel(self):
        self.assertEqual(MOD.verify_full_feynman_gauge_inverse_kernel(), 32)

    def test_main_reports_boundary(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("16 components", captured)
        self.assertIn("32 components", captured)
        self.assertIn("not a ghost/ST diagram calculation", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
