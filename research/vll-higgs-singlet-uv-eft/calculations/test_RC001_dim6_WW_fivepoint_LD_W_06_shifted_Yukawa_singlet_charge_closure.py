#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw06_shifted_yukawa", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW06ShiftedYukawaChargeClosure(unittest.TestCase):
    def test_A_and_B_secondary_heavy_channels(self):
        self.assertEqual(MOD.verify_secondary_heavy_channels(), (8, 8))

    def test_shifted_singlet_charge_sums(self):
        self.assertEqual(MOD.verify_shifted_singlet_charge_sums(), 96)

    def test_rational_heavy_channels(self):
        self.assertEqual(MOD.rational_heavy_channels(), (-377, -389, -365))

    def test_local_charge_sum_survives_arbitrary_heavy_factors(self):
        self.assertEqual(MOD.verify_shifted_singlet_charge_sums(), 96)

    def test_main_preserves_LSZ_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("do not spoil the local Yukawa-singlet charge cancellation", captured)
        self.assertIn("does not cancel the full scalar-line/three-W integrand", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
