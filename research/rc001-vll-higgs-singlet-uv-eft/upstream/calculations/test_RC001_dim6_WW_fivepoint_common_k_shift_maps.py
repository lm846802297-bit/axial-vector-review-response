#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-common-k-shift-maps.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_common_k_shift_maps", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001Dim6WWFivepointCommonKShiftMaps(unittest.TestCase):
    def test_all_shift_maps(self):
        cross = MOD.verify_cross_vertex_maps()
        same = MOD.verify_same_vertex_maps()
        self.assertEqual(cross, (8, 32, 4, 12))
        self.assertEqual(same, (4, 16, 2, 6))

    def test_full_audit(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        self.assertIn("all Yukawa-endpoint maps (12/12", output.getvalue())
        self.assertIn("all scalar-seagull maps (6/6", output.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
