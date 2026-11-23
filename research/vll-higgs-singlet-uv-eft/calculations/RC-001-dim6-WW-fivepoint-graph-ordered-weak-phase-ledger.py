#!/usr/bin/env python3
"""Exact signed-action SU(2) algebra check for RC-001 B2c.

The script verifies candidate ordered products in the signed WTI-action basis.
It does NOT establish their mapping to the raw weak-index products of every
Feynman graph; that is the separate B2c-IV raw-index bridge.
"""
from itertools import product
import sympy as sp

I = sp.I
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s/2 for s in SIGMA)
EPS = sp.LeviCivita
INDICES = tuple(product(range(2), repeat=4))


def delta(i, j):
    return sp.Integer(int(i == j))


def T0(i, j, k, ell):
    return delta(i, j)*delta(k, ell)


def T3(i, j, k, ell):
    return sum(SIGMA[a][i, j]*SIGMA[a][k, ell] for a in range(3))


def act(tensor, slot, generator, indices):
    i, j, k, ell = indices
    out = sp.Integer(0)
    if slot == 0:
        for m in range(2):
            out += T[generator][m, i]*tensor(m, j, k, ell)
    elif slot == 1:
        for m in range(2):
            out -= T[generator][j, m]*tensor(i, m, k, ell)
    elif slot == 2:
        for m in range(2):
            out += T[generator][m, k]*tensor(i, j, m, ell)
    elif slot == 3:
        for m in range(2):
            out -= T[generator][ell, m]*tensor(i, j, k, m)
    return sp.simplify(out)


def apply(tensor, slot, generator):
    return lambda *indices: act(tensor, slot, generator, indices)


PAIRS = (
    ("LD-W-01", 0, 3, 0, -sp.Rational(1,4)),
    ("LD-W-02", 0, 2, 0,  sp.Rational(1,4)),
    ("LD-W-03", 0, 1, -sp.Rational(3,4), 0),
    ("LD-W-04", 3, 2, -sp.Rational(3,4), 0),
    ("LD-W-05", 3, 1, 0,  sp.Rational(1,4)),
    ("LD-W-06", 2, 1, 0, -sp.Rational(1,4)),
)


def pair_tensor(slot_a, slot_b):
    return lambda *ix: sp.simplify(sum(
        act(apply(T0, slot_b, b), slot_a, b, ix)
        for b in range(3)
    ))


def G_tensor(slot_a, slot_b, external_a):
    return lambda *ix: sp.simplify(sum(
        EPS(external_a, b, c)
        * act(apply(T0, slot_b, c), slot_a, b, ix)
        for b, c in product(range(3), repeat=2)
    ))


def verify_candidate_signed_action_orderings():
    pair_checks = a_checks = b_checks = 0
    for pair_id, slot_a, slot_b, c0, c3 in PAIRS:
        T_ab = pair_tensor(slot_a, slot_b)
        for ix in INDICES:
            expected = c0*T0(*ix) + c3*T3(*ix)
            assert sp.simplify(T_ab(*ix)-expected) == 0, (pair_id, ix)
            pair_checks += 1

        for external_a in range(3):
            G = G_tensor(slot_a, slot_b, external_a)
            graph_A = lambda *ix: sp.simplify(sum(
                act(
                    apply(apply(T0, slot_a, external_a), slot_b, b),
                    slot_a, b, ix
                )
                for b in range(3)
            ))
            yukawa_A = apply(T_ab, slot_a, external_a)
            for ix in INDICES:
                assert sp.simplify(graph_A(*ix)-yukawa_A(*ix)+I*G(*ix)) == 0
                a_checks += 1

            graph_B = apply(T_ab, slot_b, external_a)
            yukawa_B = lambda *ix: sp.simplify(sum(
                act(
                    apply(apply(T0, slot_b, external_a), slot_a, b),
                    slot_b, b, ix
                )
                for b in range(3)
            ))
            for ix in INDICES:
                assert sp.simplify(graph_B(*ix)-yukawa_B(*ix)+I*G(*ix)) == 0
                b_checks += 1
    return pair_checks, a_checks, b_checks


def verify_candidate_seagulls():
    checks = 0
    for _, slot_a, slot_b, _, _ in PAIRS:
        for scalar_slot, other_slot in ((slot_a, slot_b), (slot_b, slot_a)):
            if scalar_slot not in (1, 2):
                continue
            for external_a in range(3):
                def sg(*ix):
                    total = sp.Integer(0)
                    for b in range(3):
                        after_other = apply(T0, other_slot, b)
                        total += act(
                            apply(after_other, scalar_slot, b),
                            scalar_slot, external_a, ix
                        )
                        total += act(
                            apply(after_other, scalar_slot, external_a),
                            scalar_slot, b, ix
                        )
                    return sp.simplify(total)
                for ix in INDICES:
                    expected = sp.Rational(1,2)*act(
                        T0, other_slot, external_a, ix
                    )
                    assert sp.simplify(sg(*ix)-expected) == 0
                    checks += 1
    return checks


def main():
    pair, a, b = verify_candidate_signed_action_orderings()
    seagull = verify_candidate_seagulls()
    assert (pair, a, b, seagull) == (96, 288, 288, 288)

    print("RC-001 signed-action SU(2) algebra check (B2c-III)")
    print(f"PASS: six seed pair tensors reproduce T0/T3 projections ({pair}/96).")
    print(f"PASS: candidate A-order commutator identity ({a}/288).")
    print(f"PASS: candidate B-order commutator identity ({b}/288).")
    print(f"PASS: candidate scalar-seagull signed-action identity ({seagull}/288).")
    print("BOUNDARY: signed-action algebra only.")
    print("The raw weak-index ordering of each Feynman graph is not established here.")
    print("Map the explicit t^a index contractions and fermion/scalar arrows before")
    print("combining these candidate tensors with the Feynman-rule phase ratios.")


if __name__ == "__main__":
    main()
