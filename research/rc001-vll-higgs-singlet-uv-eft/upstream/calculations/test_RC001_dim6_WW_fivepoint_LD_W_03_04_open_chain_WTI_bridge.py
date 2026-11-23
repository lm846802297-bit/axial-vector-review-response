#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-03-04-open-chain-WTI-bridge.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw0304_open_chain_wti", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW0304OpenChainWTIBridge(unittest.TestCase):
    def test_two_oriented_symbolic_wtis(self):
        self.assertEqual(MOD.verify_symbolic_same_vertex_wtis(), 32)

    def test_heavy_spectator_is_k_independent(self):
        self.assertEqual(MOD.verify_heavy_spectator_independence(), 16)

    def test_LDW03_open_chain(self):
        d = MOD.rational_open_chain_diagnostic("03")
        self.assertEqual(d["open_index_checks"], 64)
        self.assertEqual(d["contracted_entries"], 16)
        self.assertEqual(d["denominators"], (7, 10, 13, 16, 8, 11, -402))

    def test_LDW04_open_chain(self):
        d = MOD.rational_open_chain_diagnostic("04")
        self.assertEqual(d["open_index_checks"], 64)
        self.assertEqual(d["contracted_entries"], 16)
        self.assertEqual(d["denominators"], (7, 10, -10, -5, 2, 5, -401))

    def test_both_endpoint_decompositions(self):
        self.assertEqual(MOD.rational_open_chain_diagnostic("03")["h_E"], [2, 1, 1, 2])
        self.assertEqual(MOD.rational_open_chain_diagnostic("04")["h_E"], [-1, -1, 0, -1])

    def test_main_reports_four_attachment_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("four-attachment same-vertex sum", captured)
        self.assertIn("external-leg/LSZ/ghost-ST completion remain open", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
