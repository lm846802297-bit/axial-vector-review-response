#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-01-open-chain-WTI-threeW-common-k-bridge.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw01_open_chain_bridge", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW01OpenChainWTIThreeWBridge(unittest.TestCase):
    def test_actual_open_chain_wtis(self):
        _, wti, chains = MOD.verify_actual_open_chain_wtis()
        self.assertEqual(wti, (16, 16))
        self.assertEqual(chains, (16, 16))

    def test_A_yukawa_endpoint_common_k_map(self):
        self.assertEqual(MOD.verify_A_yukawa_endpoint_common_k_map(), 16)

    def test_denominator_alignment(self):
        self.assertEqual(MOD.verify_denominator_alignment(), 2)

    def test_actual_RFG_remainder(self):
        self.assertEqual(MOD.verify_actual_RFG_remainder(), 16)

    def test_rational_denominators_are_nonsingular(self):
        denominators, _, _ = MOD.verify_actual_open_chain_wtis()
        self.assertTrue(all(value != 0 for value in denominators))

    def test_main_preserves_open_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("first A/B endpoint terms retain their own Yukawa-channel denominators", captured)
        self.assertIn("no full 24-graph or LSZ/ST sum is claimed", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
