#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-02-open-chain-WTI-bridge.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw02_open_chain_wti", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW02OpenChainWTIBridge(unittest.TestCase):
    def test_oriented_A_fermion_wti(self):
        self.assertEqual(MOD.verify_oriented_A_fermion_wti(), 16)

    def test_common_k_yukawa_endpoint_route(self):
        self.assertEqual(MOD.verify_common_k_A_yukawa_endpoint_route(), 16)

    def test_open_lorentz_index_chain(self):
        self.assertEqual(MOD.rational_open_chain_diagnostic()["open_index_checks"], 64)

    def test_feynman_gauge_scalar_current_contraction(self):
        self.assertEqual(MOD.rational_open_chain_diagnostic()["contracted_entries"], 16)

    def test_all_rational_denominators_are_nonsingular(self):
        d = MOD.rational_open_chain_diagnostic()["denominators"]
        self.assertEqual(d, (20, 8, 11, 5, 38, 20, -390, -402))
        self.assertTrue(all(x != 0 for x in d))

    def test_endpoint_split_is_exact(self):
        d = MOD.rational_open_chain_diagnostic()
        self.assertEqual(d["open_chain"].shape, (4, 4))


if __name__ == "__main__":
    unittest.main(verbosity=2)
