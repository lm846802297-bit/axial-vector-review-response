#!/usr/bin/env python3
"""Exact SU(3) audit of direct- and crossed-pairing QLD8 color bases."""
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
    return sp.Integer(int(a == b))


direct_1, direct_8, crossed_1, crossed_8 = {}, {}, {}, {}
for i, j, k, l in product(range(3), repeat=4):
    key = (i, j, k, l)
    direct_1[key] = delta(i, l) * delta(k, j)
    direct_8[key] = sp.simplify(sum(t[i, l] * t[k, j] for t in T))
    crossed_1[key] = delta(i, j) * delta(k, l)
    crossed_8[key] = sp.simplify(sum(t[i, j] * t[k, l] for t in T))

# B_direct = B_crossed R.
R = sp.Matrix([
    [sp.Rational(1, 3), sp.Rational(4, 9)],
    [2, -sp.Rational(1, 3)],
])
assert R.det() != 0
for key in direct_1:
    assert sp.simplify(
        direct_1[key] - R[0, 0] * crossed_1[key] - R[1, 0] * crossed_8[key]
    ) == 0
    assert sp.simplify(
        direct_8[key] - R[0, 1] * crossed_1[key] - R[1, 1] * crossed_8[key]
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


def decompose(tensor, basis_1, basis_8):
    rows, rhs = [], []
    for key in basis_1:
        rows.append([basis_1[key], basis_8[key]])
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
direct_matrices = {}
crossed_matrices = {}
for pair in pair_order:
    md = sp.Matrix.hstack(
        decompose(apply_exchange(direct_1, *pair), direct_1, direct_8),
        decompose(apply_exchange(direct_8, *pair), direct_1, direct_8),
    )
    mx = sp.Matrix.hstack(
        decompose(apply_exchange(crossed_1, *pair), crossed_1, crossed_8),
        decompose(apply_exchange(crossed_8, *pair), crossed_1, crossed_8),
    )
    assert md == R.inv() * mx * R
    direct_matrices[pair] = md
    crossed_matrices[pair] = mx

expected_direct = {
    ("barQ", "Q"): sp.Matrix([[0, -sp.Rational(2, 9)], [-1, -sp.Rational(7, 6)]]),
    ("barQ", "bard"): sp.Matrix([[0, sp.Rational(2, 9)], [1, -sp.Rational(1, 3)]]),
    ("barQ", "d"): sp.diag(-sp.Rational(4, 3), sp.Rational(1, 6)),
    ("Q", "bard"): sp.diag(-sp.Rational(4, 3), sp.Rational(1, 6)),
    ("Q", "d"): sp.Matrix([[0, sp.Rational(2, 9)], [1, -sp.Rational(1, 3)]]),
    ("bard", "d"): sp.Matrix([[0, -sp.Rational(2, 9)], [-1, -sp.Rational(7, 6)]]),
}
for pair in pair_order:
    assert direct_matrices[pair] == expected_direct[pair]

total = sum(direct_matrices.values(), sp.zeros(2))
assert total == -sp.Rational(8, 3) * sp.eye(2)

print("RC-001 QLD8 direct-pairing SU(3) color-basis audit")
print("PASS: direct/crossed basis transformation B_d = B_x R, all 81 color components.")
for pair in pair_order:
    print(f"PASS: direct M_{pair[0]},{pair[1]} = {direct_matrices[pair].tolist()}")
print("PASS: all six direct matrices equal R^{-1} M_cross R.")
print("PASS: sum over six pair exchanges = -(8/3) I.")
print("PASS: tree source is the direct singlet vector (1,0)_d = (1/3,2)_cross.")
print("LIMIT: color factors only; no Dirac numerator, loop kernel, or UV pole.")
