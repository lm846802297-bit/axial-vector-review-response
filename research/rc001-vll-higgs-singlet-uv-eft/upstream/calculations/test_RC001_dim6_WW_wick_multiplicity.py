#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-wick-multiplicity.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_wick", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001WWWickMultiplicity(unittest.TestCase):
    def test_six_unordered_pairs(self):
        self.assertEqual(len(MOD.ALL_PAIRS), 6)

    def test_two_same_vertex_four_cross_vertex(self):
        self.assertEqual(len(MOD.SAME_VERTEX), 2)
        self.assertEqual(len(MOD.CROSS_PAIRS), 4)
        self.assertEqual(set(MOD.SAME_VERTEX).intersection(MOD.CROSS_PAIRS), set())

    def test_each_unordered_pair_has_unit_second_order_multiplicity(self):
        for pair in MOD.ALL_PAIRS:
            self.assertEqual(len(MOD.ordered_endpoint_assignments(pair)), 2)
            self.assertEqual(MOD.multiplicity_after_second_order_factor(pair), 1)

    def test_su2_composite_has_no_direct_w_contact(self):
        self.assertEqual(MOD.audit_composite_singlet(), [0, 0, 0])

    def test_hermitian_conjugate_is_same_action_operator_mod_ibp(self):
        self.assertTrue(MOD.audit_hc_operator_identity())


if __name__ == "__main__":
    unittest.main(verbosity=2)
