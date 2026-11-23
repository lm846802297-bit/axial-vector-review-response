#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-05-projector-order-reconciliation.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw05_projector_order", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW05ProjectorOrder(unittest.TestCase):
    def test_chiral_intertwining(self):
        self.assertEqual(MOD.verify_chiral_intertwining(), 10)

    def test_actual_B_endpoint_order(self):
        checks, _, _, _ = MOD.verify_B_endpoint_projector_order()
        self.assertEqual(checks, 128)

    def test_RFG_is_separate_from_single_W_endpoint(self):
        rfg, endpoint_w, endpoint_y, _, _ = MOD.verify_RFG_order_is_separate()
        self.assertEqual(rfg, 16)
        self.assertEqual(endpoint_w, 16)
        self.assertEqual(endpoint_y, 16)

    def test_main_preserves_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("not an equality of the single-W WTI endpoints and R_FG", captured)
        self.assertIn("complete longitudinal", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
