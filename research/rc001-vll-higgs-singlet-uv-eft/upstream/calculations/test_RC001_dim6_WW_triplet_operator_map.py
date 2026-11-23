#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-triplet-operator-map.py"
SPEC = importlib.util.spec_from_file_location("rc001_triplet_map", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestTripletOperatorMap(unittest.TestCase):
    def test_explicit_pauli_component_identity(self):
        self.assertEqual(MOD.component_operator_identity(), 0)

    def test_derivative_current_decomposition(self):
        self.assertEqual(MOD.derivative_current_identity(), 0)

    def test_eom_ibp_yukawa_source_reduction(self):
        self.assertEqual(MOD.eom_ibp_reduction_identity(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
