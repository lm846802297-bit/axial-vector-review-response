#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-triplet-current-contact.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_triplet", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001WWTripletCurrentContact(unittest.TestCase):
    def test_pauli_completeness_is_T3(self):
        self.assertTrue(MOD.audit_pauli_completeness())

    def test_adjoint_covariant_derivative_contact(self):
        self.assertTrue(MOD.audit_adjoint_derivative())

    def test_triplet_tensor_normalization(self):
        self.assertTrue(MOD.audit_triplet_tensor_normalization())

    def test_adjoint_contact_matrix_is_nonzero_generic(self):
        matrix = MOD.adjoint_contact_matrix()
        self.assertTrue(any(matrix[i, j] != 0 for i in range(2) for j in range(2)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
