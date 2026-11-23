#!/usr/bin/env python3
"""Exact SU(3) exchange-color matrices for the QLD8 d†d pilot sector.

All four external quark legs are outgoing in the ordered tensor
(bar Q, Q, bar d, d). This computes color generators only, not loop kernels.
"""
from itertools import product
import sympy as sp

I = sp.I
sqrt3 = sp.sqrt(3)
gell_mann = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sqrt3,
]
T = [m / 2 for m in gell_mann]
legs = ("barQ", "Q", "bard", "d")
anti_legs = {"barQ", "bard"}


def delta(a, b):
    return sp.Integer(1 if a == b else 0)


C1, C8, CX = {}, {}, {}
for i, j, k, l in product(range(3), repeat=4):
    key = (i, j, k, l)
    C1[key] = delta(i, j) * delta(k, l)
    C8[key] = sp.simplify(sum(t[i, j] * t[k, l] for t in T))
    CX[key] = delta(i, l) * delta(k, j)

for key in C1:
    assert sp.simplify(
        CX[key] - sp.Rational(1, 3) * C1[key] - 2 * C8[key]
    ) == 0


def leg_generator(leg, A):
    return -T[A].T if leg in anti_legs else T[A]


def apply_exchange(tensor, leg_a, leg_b):
    output = {}
    ia, ib = legs.index(leg_a), legs.index(leg_b)
    for index in product(range(3), repeat=4):
        value = sp.Integer(0)
        for A in range(8):
            ga = leg_generator(leg_a, A)
            gb = leg_generator(leg_b, A)
            for a_prime, b_prime in product(range(3), repeat=2):
                shifted = list(index)
                shifted[ia], shifted[ib] = a_prime, b_prime
                value += (
                    ga[index[ia], a_prime]
                    * gb[index[ib], b_prime]
                    * tensor[tuple(shifted)]
                )
        output[index] = sp.simplify(value)
    return output


def decompose(tensor):
    rows, rhs = [], []
    for key in C1:
        rows.append([C1[key], C8[key]])
        rhs.append(tensor[key])
    solutions = list(sp.linsolve((sp.Matrix(rows), sp.Matrix(rhs))))
    assert len(solutions) == 1
    return sp.Matrix(solutions[0])


pair_order = [
    ("barQ", "Q"),
    ("barQ", "bard"),
    ("barQ", "d"),
    ("Q", "bard"),
    ("Q", "d"),
    ("bard", "d"),
]
expected = {
    ("barQ", "Q"): sp.Matrix([[-sp.Rational(4, 3), 0], [0, sp.Rational(1, 6)]]),
    ("barQ", "bard"): sp.Matrix([[0, sp.Rational(2, 9)], [1, -sp.Rational(1, 3)]]),
    ("barQ", "d"): sp.Matrix([[0, -sp.Rational(2, 9)], [-1, -sp.Rational(7, 6)]]),
    ("Q", "bard"): sp.Matrix([[0, -sp.Rational(2, 9)], [-1, -sp.Rational(7, 6)]]),
    ("Q", "d"): sp.Matrix([[0, sp.Rational(2, 9)], [1, -sp.Rational(1, 3)]]),
    ("bard", "d"): sp.Matrix([[-sp.Rational(4, 3), 0], [0, sp.Rational(1, 6)]]),
}

matrices = {}
for pair in pair_order:
    matrix = sp.Matrix.hstack(
        decompose(apply_exchange(C1, *pair)),
        decompose(apply_exchange(C8, *pair)),
    )
    assert matrix == expected[pair]
    matrices[pair] = matrix

total = sum(matrices.values(), sp.zeros(2))
assert total == -sp.Rational(8, 3) * sp.eye(2)

crossed_vector = sp.Matrix([sp.Rational(1, 3), 2])
for pair, matrix in matrices.items():
    assert matrix * crossed_vector == decompose(apply_exchange(CX, *pair))

print("RC-001 QLD8 d†d SU(3) exchange-color audit")
print("PASS: crossed source tensor C_X = (1/3) C_1 + 2 C_8.")
for pair in pair_order:
    print(f"PASS: T_{pair[0]}·T_{pair[1]} = {matrices[pair].tolist()}")
print("PASS: sum over all six pair exchanges = -(8/3) I = -2 C_F I.")
print("LIMIT: color factors only; no Feynman signs, loop kernels, UV poles, or Z matrix.")
