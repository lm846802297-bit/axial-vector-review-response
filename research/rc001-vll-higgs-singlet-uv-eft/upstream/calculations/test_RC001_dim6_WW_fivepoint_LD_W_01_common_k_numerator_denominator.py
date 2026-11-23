#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-01-common-k-numerator-denominator.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw01_common_k", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW01CommonKNumeratorDenominator(unittest.TestCase):
    def test_oriented_fermion_wtis(self):
        self.assertEqual(MOD.verify_wti(), 32)

    def test_actual_common_k_maps_and_denominators(self):
        self.assertEqual(MOD.verify_common_routing_and_denominators(), (32, 2))

    def test_three_w_vertex_and_kernel(self):
        self.assertEqual(MOD.verify_three_w_vertex_and_kernel(), (16, 16))

    def test_physical_weak_commutator_phase_alignment(self):
        self.assertEqual(MOD.verify_weak_phase(), (48, 48))

    def test_final_projector_is_after_right_W_current(self):
        self.assertEqual(MOD.verify_final_projector_order(), 16)

    def test_nonsingular_nonzero_rfg_diagnostic(self):
        den, nonzero, chain_checks = MOD.rational_diagnostic()
        self.assertEqual(den, (10, 8, 6, -3, -393))
        self.assertEqual(nonzero, 16)
        self.assertEqual(chain_checks, 32)

    def test_main_reports_boundary_and_retains_rfg(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("actual LD-W-01 Dirac-chain cancellation to R_FG at an exact rational point (32/32", captured)
        self.assertIn("R_FG is retained, not set to zero", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
