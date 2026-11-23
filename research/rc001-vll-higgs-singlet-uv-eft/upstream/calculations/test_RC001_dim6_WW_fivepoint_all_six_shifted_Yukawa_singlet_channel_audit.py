#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.py"
SPEC = importlib.util.spec_from_file_location("rc001_all_six_shifted_yukawa", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestAllSixShiftedYukawaChannels(unittest.TestCase):
    def test_cross_A_channel(self):
        self.assertEqual(MOD.verify_cross_A_secondary_channel(), 8)

    def test_cross_B_channel(self):
        self.assertEqual(MOD.verify_cross_B_secondary_channel(), 4)

    def test_same_vertex_spectators(self):
        self.assertEqual(MOD.verify_same_vertex_spectators(), (8, 16))

    def test_all_singlet_charge_sums(self):
        self.assertEqual(MOD.verify_all_singlet_charge_sums(), 192)

    def test_rational_heavy_channels(self):
        self.assertEqual(MOD.rational_heavy_channels(), (-377, -389, -365))

    def test_main_reports_boundary(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("all six pair classes preserve the local Yukawa-singlet charge factor", captured)
        self.assertIn("does not establish the full ordinary-matter longitudinal integrand cancellation", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
