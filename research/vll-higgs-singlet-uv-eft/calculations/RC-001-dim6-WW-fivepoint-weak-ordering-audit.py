#!/usr/bin/env python3
"""Exact SU(2) weak-index ordering audit for RC-001 external-W attachments."""
from itertools import product
import sympy as sp

I = sp.I
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s / 2 for s in SIGMA)
EPS = sp.LeviCivita
INDICES = tuple(product(range(2), repeat=4))


def delta(i, j):
    return sp.Integer(int(i == j))


def T0(i, j, k, ell):
    return delta(i, j) * delta(k, ell)


def T3(i, j, k, ell):
    return sum(SIGMA[a][i, j] * SIGMA[a][k, ell] for a in range(3))


def act(tensor, slot, generator, indices):
    """Signed external-index action in the fixed all-incoming convention."""
    i, j, k, ell = indices
    out = sp.Integer(0)
    if slot == 0:  # bar L
        for m in range(2):
            out += T[generator][m, i] * tensor(m, j, k, ell)
    elif slot == 1:  # H
        for m in range(2):
            out -= T[generator][j, m] * tensor(i, m, k, ell)
    elif slot == 2:  # H dagger
        for m in range(2):
            out += T[generator][m, k] * tensor(i, j, m, ell)
    elif slot == 3:  # L
        for m in range(2):
            out -= T[generator][ell, m] * tensor(i, j, k, m)
    return sp.simplify(out)


def apply(tensor, slot, generator):
    return lambda *indices: act(tensor, slot, generator, indices)


PAIR_DATA = (
    ("LD-W-01", 0, 3, sp.Integer(0), -sp.Rational(1, 4)),
    ("LD-W-02", 0, 2, sp.Integer(0),  sp.Rational(1, 4)),
    ("LD-W-03", 0, 1, -sp.Rational(3, 4), sp.Integer(0)),
    ("LD-W-04", 3, 2, -sp.Rational(3, 4), sp.Integer(0)),
    ("LD-W-05", 3, 1, sp.Integer(0),  sp.Rational(1, 4)),
    ("LD-W-06", 2, 1, sp.Integer(0), -sp.Rational(1, 4)),
)


def pair_tensor(slot_a, slot_b):
    def tensor(*indices):
        return sp.simplify(sum(
            act(apply(T0, slot_b, b), slot_a, b, indices)
            for b in range(3)
        ))
    return tensor


def verify_pair_projections():
    checks = 0
    for pair_id, a, b, c0, c3 in PAIR_DATA:
        tensor = pair_tensor(a, b)
        for indices in INDICES:
            expected = c0*T0(*indices) + c3*T3(*indices)
            assert sp.simplify(tensor(*indices) - expected) == 0, (
                pair_id, indices, tensor(*indices), expected
            )
            checks += 1
    return checks


def verify_ordering_commutators():
    checks = 0
    for pair_id, slot_a, slot_b, _, _ in PAIR_DATA:
        tensor = pair_tensor(slot_a, slot_b)
        for external_a in range(3):
            triple = lambda *indices: sp.simplify(sum(
                EPS(external_a, b, c)
                * act(apply(T0, slot_b, c), slot_a, b, indices)
                for b, c in product(range(3), repeat=2)
            ))

            # External W lies on the A line.
            outer_a = apply(tensor, slot_a, external_a)
            inner_a = lambda *indices: sp.simplify(sum(
                act(
                    apply(apply(T0, slot_a, external_a), slot_b, b),
                    slot_a, b, indices
                )
                for b in range(3)
            ))
            for indices in INDICES:
                assert sp.simplify(
                    outer_a(*indices) - inner_a(*indices)
                    - I*triple(*indices)
                ) == 0, (pair_id, "A", external_a, indices)
                checks += 1

            # External W lies on the B line.
            outer_b = apply(tensor, slot_b, external_a)
            inner_b = lambda *indices: sp.simplify(sum(
                act(
                    apply(apply(T0, slot_b, external_a), slot_a, b),
                    slot_b, b, indices
                )
                for b in range(3)
            ))
            for indices in INDICES:
                assert sp.simplify(
                    outer_b(*indices) - inner_b(*indices)
                    + I*triple(*indices)
                ) == 0, (pair_id, "B", external_a, indices)
                checks += 1
    return checks


def verify_scalar_seagull_group_factors():
    checks = 0
    for pair_id, slot_a, slot_b, _, _ in PAIR_DATA:
        for scalar_slot, other_slot in ((slot_a, slot_b), (slot_b, slot_a)):
            if scalar_slot not in (1, 2):
                continue
            for external_a in range(3):
                def seagull(*indices):
                    total = sp.Integer(0)
                    for internal_b in range(3):
                        after_other = apply(T0, other_slot, internal_b)
                        total += act(
                            apply(after_other, scalar_slot, internal_b),
                            scalar_slot, external_a, indices
                        )
                        total += act(
                            apply(after_other, scalar_slot, external_a),
                            scalar_slot, internal_b, indices
                        )
                    return sp.simplify(total)

                for indices in INDICES:
                    expected = sp.Rational(1, 2) * act(
                        T0, other_slot, external_a, indices
                    )
                    assert sp.simplify(seagull(*indices) - expected) == 0, (
                        pair_id, scalar_slot, external_a, indices
                    )
                    checks += 1
    return checks


def main():
    pair_checks = verify_pair_projections()
    ordering_checks = verify_ordering_commutators()
    seagull_checks = verify_scalar_seagull_group_factors()
    assert pair_checks == 96
    assert ordering_checks == 576
    assert seagull_checks == 288

    print("RC-001-WW-UV-FF-02 weak-index ordering audit")
    print(f"PASS: six internal-W pair tensors reproduce T0/T3 projections ({pair_checks}/96).")
    print(f"PASS: both matter-line generator orderings reduce to the three-W commutator tensor ({ordering_checks}/576).")
    print(f"PASS: six scalar-seagull group tensors reduce to one-half the other-endpoint generator ({seagull_checks}/288).")
    print("PAIR PROJECTIONS:")
    for pair_id, _, _, c0, c3 in PAIR_DATA:
        print(f"  {pair_id}: {c0} T0 + ({c3}) T3")
    print("RESULT: exact SU(2) weak-index ordering identities pass.")
    print("BOUNDARY: this fixes group tensors only; no Lorentz numerator phases, loop integrals, or full STI cancellation are claimed.")


if __name__ == "__main__":
    main()
