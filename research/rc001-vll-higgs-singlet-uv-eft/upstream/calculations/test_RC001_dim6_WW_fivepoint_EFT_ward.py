#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

SOURCE = pathlib.Path(__file__).with_name("RC-001-dim6-WW-fivepoint-EFT-ward.py")
SPEC = importlib.util.spec_from_file_location("rc001_ww_fivepoint_ward", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestWWFivepointEFTWard(unittest.TestCase):
    def test_adjoint_commutator(self):
        MOD.verify_adjoint_commutator()

    def test_local_adjoint_ward_identity(self):
        MOD.verify_local_adjoint_ward_identity()

    def test_t3_invariance(self):
        MOD.verify_t3_invariance()

    def test_higgs_contact_tensors(self):
        MOD.verify_higgs_contact_tensors()

    def test_matching_log_slopes(self):
        self.assertEqual(
            MOD.verify_matching_log_slopes(),
            (-1, -MOD.sp.Rational(7, 8), MOD.sp.Rational(5, 8)),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
