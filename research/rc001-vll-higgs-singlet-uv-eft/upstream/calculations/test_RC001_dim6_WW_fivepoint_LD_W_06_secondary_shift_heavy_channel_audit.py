#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.py"
SPEC = importlib.util.spec_from_file_location("rc001_ldw06_secondary_shift", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestLDW06SecondaryShiftHeavyChannel(unittest.TestCase):
    def test_A_negative_deltaW_shift(self):
        self.assertEqual(MOD.verify_A_negative_DeltaW_shift(), (16, 4))

    def test_B_negative_deltaW_shift(self):
        self.assertEqual(MOD.verify_B_negative_DeltaW_shift(), (16, 4))

    def test_generic_heavy_denominator_differences(self):
        self.assertEqual(MOD.verify_shifted_heavy_denominators(), 2)

    def test_rational_heavy_channels_are_distinct(self):
        d = MOD.rational_diagnostic()
        self.assertEqual((d["H0"], d["HA"], d["HB"]), (-377, -389, -365))
        self.assertNotEqual(d["A_minus_den"][-1], d["A_shifted_den"][-1])
        self.assertNotEqual(d["B_minus_den"][-1], d["B_shifted_den"][-1])

    def test_shifted_scalar_and_current_factors(self):
        d = MOD.rational_diagnostic()
        self.assertEqual(d["A_minus_den"][:3], (44, 75, 49))
        self.assertEqual(d["A_shifted_den"][:3], (34, 61, 35))
        self.assertEqual(d["B_minus_den"][:3], (34, 35, 61))
        self.assertEqual(d["B_shifted_den"][:3], (44, 49, 75))

    def test_main_keeps_heavy_channel_open(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("heavy channel becomes h-q and h+q", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
