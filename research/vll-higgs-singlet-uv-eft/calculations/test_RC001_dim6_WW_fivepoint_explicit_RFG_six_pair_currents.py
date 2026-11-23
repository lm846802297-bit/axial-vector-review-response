#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-explicit-RFG-six-pair-currents.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_explicit_rfg", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001ExplicitRFGSixPairCurrents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # audit_point performs the direct tensor-vs-factorized matrix assertion
        # for every pair before returning the compact numerators.
        cls.results = MOD.audit_points()

    def test_all_six_pairs_at_two_exact_rational_points(self):
        self.assertEqual(len(self.results), 2)
        expected = ("01", "02", "03", "04", "05", "06")
        for point in self.results:
            self.assertEqual(tuple(point.keys()), expected)

    def test_all_propagator_factors_are_nonsingular_and_rfg_nonzero(self):
        for point in self.results:
            for pair_id, result in point.items():
                self.assertTrue(all(x != 0 for x in result["denominators"]), pair_id)
                self.assertTrue(any(
                    MOD.sp.simplify(x) != 0 for x in result["numerator"]
                ), pair_id)

    def test_main_reports_all_six_pair_classes(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("rational point 1 (6/6 pairs)", captured)
        self.assertIn("rational point 2 (6/6 pairs)", captured)
        for pair_id in ("01", "02", "03", "04", "05", "06"):
            self.assertIn(f"LD-W-{pair_id}", captured)
        self.assertIn("No ghost/ST completion", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
