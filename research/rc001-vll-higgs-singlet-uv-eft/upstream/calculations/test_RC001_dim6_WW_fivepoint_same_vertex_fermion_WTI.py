#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-same-vertex-fermion-WTI.py"
SPEC = importlib.util.spec_from_file_location("rc001_same_vertex_fermion_wti", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001SameVertexFermionWTI(unittest.TestCase):
    def test_both_oriented_line_wtis(self):
        self.assertEqual(MOD.verify_same_vertex_fermion_wti(), 32)

    def test_full_insertion_and_seed_conjugation(self):
        self.assertEqual(MOD.verify_full_open_chain_conjugation(), 32)

    def test_common_k_route_and_heavy_spectator(self):
        self.assertEqual(MOD.verify_common_k_momentum_and_spectator(), (4, 16))

    def test_main_reports_both_orientations(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("LD-W-03/04 opposite open-line WTI identities", captured)
        self.assertIn("LD-W-03:", captured)
        self.assertIn("LD-W-04:", captured)
        self.assertIn("no full 24-graph sum", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
