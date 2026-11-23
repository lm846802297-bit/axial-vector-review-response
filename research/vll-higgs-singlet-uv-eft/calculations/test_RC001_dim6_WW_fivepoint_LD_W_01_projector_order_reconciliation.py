#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw01_projector_order", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW01ProjectorOrder(unittest.TestCase):
    def test_chiral_intertwining(self):
        self.assertEqual(MOD.check_chiral(), 10)

    def test_actual_endpoint_projector_reductions(self):
        counts, den = MOD.check_endpoints()
        self.assertEqual(counts, dict(A_W=256, A_Y=256, B_W=256, B_Y=256))
        self.assertTrue(all(x != 0 for x in den))

    def test_common_k_second_endpoint_match(self):
        self.assertEqual(MOD.check_common_k_second_endpoints(), (256, 16, 2))

    def test_rfg_final_projector_order(self):
        self.assertEqual(MOD.check_rfg_order(), (16, 16, 64))

    def test_exact_rational_denominators(self):
        _, den = MOD.check_endpoints()
        self.assertEqual(den, (10, 8, 6, 2, -13, -3, -393, -405))

    def test_main_preserves_scientific_boundary(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("R_FG remains nonzero", captured)
        self.assertIn("no six-pair sum", captured)
        self.assertIn("or Wilson coefficient", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
