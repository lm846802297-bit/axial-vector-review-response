#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw0304_endpoint_split", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW0304SameVertexEndpointBridge(unittest.TestCase):
    def test_opposite_fermion_wtis(self):
        self.assertEqual(MOD.verify_fermion_wtis(), 32)

    def test_scalar_wti_and_current_rebase(self):
        self.assertEqual(MOD.verify_scalar_wti_and_current_rebase(), (1, 4))

    def test_common_k_shift_and_denominator_bridge(self):
        self.assertEqual(MOD.verify_common_k_shift_and_denominators(), (24, 16, 1))

    def test_weak_ordering_and_S_to_F_phase(self):
        self.assertEqual(MOD.verify_weak_ordering_and_phase(), {
            "seed": 32, "F_commutator": 96, "S_commutator": 96,
            "F_threeW_phase": 96, "S_threeW_phase": 96,
            "scalar_seagull": 96,
        })

    def test_heavy_spectator_and_chiral_projection(self):
        self.assertEqual(MOD.verify_heavy_spectator(), (16, 16))

    def test_actual_RFG_and_scalar_endpoint_kernels(self):
        rows, rfg_checks, endpoint_checks = MOD.verify_rfg_and_actual_endpoint_kernels()
        self.assertEqual((len(rows), rfg_checks, endpoint_checks), (4, 64, 64))
        self.assertTrue(all(row[5] == 16 and row[6] > 0 and row[7] > 0 for row in rows))

    def test_main_preserves_the_open_STI_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("symmetric q contact is (Delta_Y+Delta_W)/2", captured)
        self.assertIn("no physical non-cancellation", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
