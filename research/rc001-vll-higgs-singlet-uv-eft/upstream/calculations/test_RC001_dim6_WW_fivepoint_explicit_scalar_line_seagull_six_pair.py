#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_scalar_seagull", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001ExplicitScalarLineSeagullKernels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.points = MOD.audit_points()

    def test_raw_and_decomposed_scalar_endpoint_tensors(self):
        self.assertEqual(MOD.verify_endpoint_decompositions(), 12)

    def test_oriented_scalar_wtis(self):
        # The symbolic endpoint audit checks A, B and same-vertex S orientations.
        self.assertEqual(MOD.verify_endpoint_decompositions(), 12)

    def test_six_actual_scalar_endpoints_at_two_rational_points(self):
        expected = ("02-B", "05-A", "06-A", "06-B", "03-S", "04-S")
        self.assertEqual(len(self.points), 2)
        for point in self.points:
            self.assertEqual(tuple(point.keys()), expected)
            for label, (kernel, denominators, _) in point.items():
                self.assertTrue(all(x != 0 for x in denominators), label)
                self.assertTrue(any(
                    MOD.sp.simplify(x) != 0 for x in kernel
                ), label)

    def test_main_reports_explicit_endpoint_kernels(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("12/12 component identities", captured)
        self.assertIn("3/3", captured)
        self.assertIn("rational point 1 (6/6 scalar endpoints)", captured)
        self.assertIn("rational point 2 (6/6 scalar endpoints)", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
