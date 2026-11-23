#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-yukawa-singlet-endpoint-cancellation.py"
SPEC = importlib.util.spec_from_file_location("rc001_yukawa_singlet_endpoint", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001YukawaSingletEndpointCancellation(unittest.TestCase):
    def test_left_and_right_singlet_charge_sums(self):
        self.assertEqual(MOD.verify_yukawa_singlet_charge_sums(), 96)

    def test_cross_vertex_heavy_channel_shifts(self):
        self.assertEqual(MOD.verify_cross_vertex_heavy_channel_maps(), 8)

    def test_same_vertex_heavy_channel_is_shared(self):
        self.assertEqual(MOD.verify_same_vertex_heavy_channel_maps(), 12)

    def test_common_heavy_factor_preserves_zero_charge_sum(self):
        self.assertEqual(MOD.verify_common_heavy_factor_cancellation(), 96)

    def test_main_reports_local_boundary(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("96/96 weak components", captured)
        self.assertIn("8/8 vector components", captured)
        self.assertIn("12/12 vector components", captured)
        self.assertIn("not the full external-leg/LSZ sum", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
