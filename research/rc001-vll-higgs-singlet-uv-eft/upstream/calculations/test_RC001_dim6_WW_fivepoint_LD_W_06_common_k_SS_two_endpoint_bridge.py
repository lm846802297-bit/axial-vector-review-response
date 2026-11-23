#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw06_ss_bridge", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW06SSTwoEndpointBridge(unittest.TestCase):
    def test_A_and_B_scalar_wtis_and_rebases(self):
        self.assertEqual(MOD.verify_A_B_scalar_rebases(), ((1, 4), (1, 4)))

    def test_common_k_routes_and_seagull_denominators(self):
        self.assertEqual(MOD.verify_common_k_routes_and_denominators(), (24, 2))

    def test_separate_A_B_weak_tensors(self):
        self.assertEqual(MOD.verify_weak_tensors(), {
            "A_commutator": 48, "B_commutator": 48,
            "A_seagull": 48, "B_seagull": 48,
        })

    def test_actual_S_S_RFG_and_endpoint_kernels(self):
        rows, rfg_checks, endpoint_checks = MOD.verify_rfg_and_endpoint_kernels()
        self.assertEqual((len(rows), rfg_checks, endpoint_checks), (2, 32, 64))
        self.assertTrue(all(row[8] > 0 and all(n > 0 for n in row[9]) for row in rows))

    def test_both_scalar_line_denominators_keep_two_scalar_propagators(self):
        rows, _, _ = MOD.verify_rfg_and_endpoint_kernels()
        for row in rows:
            _, d3, da_line, da_sg, db_line, db_sg, *_ = row
            self.assertEqual(da_line[0:3], (d3[1], d3[3], d3[2]))
            self.assertEqual(db_line[0:3], (d3[0], d3[2], d3[3]))
            self.assertNotEqual(da_line, da_sg)
            self.assertNotEqual(db_line, db_sg)

    def test_main_preserves_separate_endpoints_and_open_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("S_A and S_B remain distinct", captured)
        self.assertIn("no sum with the fermion/Yukawa endpoint variations", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
