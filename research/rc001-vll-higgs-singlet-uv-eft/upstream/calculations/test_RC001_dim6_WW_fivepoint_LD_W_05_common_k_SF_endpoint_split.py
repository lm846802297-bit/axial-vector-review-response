#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-05-common-k-SF-endpoint-split.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw05_endpoint_split", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW05CommonKEndpointSplit(unittest.TestCase):
    def test_B_fermion_wti(self):
        self.assertEqual(MOD.verify_B_fermion_wti(), 16)

    def test_A_scalar_wti_and_current_rebase(self):
        self.assertEqual(MOD.verify_A_scalar_wti_and_current_rebase(), (1, 8))

    def test_B_side_fermion_route_and_denominators(self):
        self.assertEqual(MOD.verify_B_side_fermion_route_to_three_w(), (20, 3))

    def test_physical_A_weak_commutator_and_seagull(self):
        self.assertEqual(MOD.verify_weak_ordering(), (48, 48))

    def test_final_projector_is_after_right_W_current(self):
        self.assertEqual(MOD.verify_final_projector_order(), 16)

    def test_rational_RFG_and_scalar_q_contact(self):
        den, delta, n_nonzero, q_nonzero = MOD.rational_diagnostic()
        self.assertEqual(den, (20, 8, 23, 17, -4, -390))
        self.assertEqual(delta, MOD.sp.Rational(-6, 391))
        self.assertEqual((n_nonzero, q_nonzero), (16, 16))

    def test_main_preserves_unresolved_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("V_A(k+q)=V_A(k)-q", captured)
        self.assertIn("No physical non-cancellation", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
