#!/usr/bin/env python3
"""Exact SU(2) generator-contraction check for the Q_LD attachment atlas.

Checks only representation-generator contractions on the tree weak tensor.
It does not compute loop integrals, diagram multiplicities, or Wilson coefficients.
"""
from itertools import product
import sympy as sp

pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
t = [matrix / 2 for matrix in pauli]
representations = {
    "Lbar": [-matrix.T for matrix in t],
    "H": [matrix for matrix in t],
    "Hbar": [-matrix.T for matrix in t],
    "L": [matrix for matrix in t],
}
field_order = ["Lbar", "H", "Hbar", "L"]

def tree_tensor(i, j, k, l):
    return sp.Integer(i == j) * sp.Integer(k == l)

def contracted_tensor(field_a, field_b):
    out = {indices: sp.Integer(0) for indices in product(range(2), repeat=4)}
    pos_a, pos_b = field_order.index(field_a), field_order.index(field_b)
    for generator in range(3):
        for indices in out:
            total = sp.Integer(0)
            for a_prime in range(2):
                for b_prime in range(2):
                    replaced = list(indices)
                    replaced[pos_a] = a_prime
                    replaced[pos_b] = b_prime
                    total += (
                        representations[field_a][generator][indices[pos_a], a_prime]
                        * representations[field_b][generator][indices[pos_b], b_prime]
                        * tree_tensor(*replaced)
                    )
            out[indices] += sp.simplify(total)
    return out

def T0(indices):
    return tree_tensor(*indices)

def Tx(indices):
    i, j, k, l = indices
    return sp.Integer(i == l) * sp.Integer(k == j)

def T3(indices):
    return 2 * Tx(indices) - T0(indices)

# Coefficients are (T0, T3), using atlas line-pair ordering.
expected = [
    ("LD-W-01", "Lbar", "L", 0, -sp.Rational(1, 4)),
    ("LD-W-02", "Lbar", "Hbar", 0, sp.Rational(1, 4)),
    ("LD-W-03", "Lbar", "H", -sp.Rational(3, 4), 0),
    ("LD-W-04", "L", "Hbar", -sp.Rational(3, 4), 0),
    ("LD-W-05", "L", "H", 0, sp.Rational(1, 4)),
    ("LD-W-06", "Hbar", "H", 0, -sp.Rational(1, 4)),
]

def main():
    for pair_id, field_a, field_b, c0, c3 in expected:
        actual = contracted_tensor(field_a, field_b)
        for indices, value in actual.items():
            predicted = c0 * T0(indices) + c3 * T3(indices)
            assert sp.simplify(value - predicted) == 0, (
                pair_id, indices, value, predicted
            )
        print(f"{pair_id}: exact SU(2) tensor identity PASS")
    print("RESULT: all six Q_LD weak-generator contractions PASS.")
    print("SCOPE: group-theory tensors only; no loop integrals or Wilson coefficients.")

if __name__ == "__main__":
    main()
