#!/usr/bin/env python3
"""RC-001 B2c-IVd: explicit raw-index SU(2) bridge for cross-vertex WW graphs.

The calculation uses the physical field-representation matrices on the
all-incoming tensor slots (bar L, H, Hdag, L). It explicitly contracts the
weak indices of the ordered generator words; it does not reuse the signed
WTI-action implementation.

Scope: cross-vertex pairs LD-W-01/02/05/06 only. The same-vertex pairs
LD-W-03/04 have a different internal-W orientation (S -> F) and are kept
out of this cross-vertex ordering claim until their raw chains are derived
separately.

This is a weak-index and relative-phase audit, not a Lorentz-weighted
Slavnov-Taylor sum or a loop integration.
"""
from itertools import product
import sympy as sp

I = sp.I
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
TGEN = tuple(s / 2 for s in SIGMA)
EPS = sp.LeviCivita
WEAK_INDICES = tuple(product(range(2), repeat=4))

# Physical representations on the all-incoming amplitude tensor:
# (bar L, H, Hdag, L) = (-t^T, +t, -t^T, +t).
R = {
    0: tuple(-t.T for t in TGEN),
    1: TGEN,
    2: tuple(-t.T for t in TGEN),
    3: TGEN,
}

# Four cross-vertex pair classes. A is attached to the left Yukawa vertex;
# B is attached to the right conjugate Yukawa vertex.
# a_scalar/b_scalar indicate whether that endpoint has a scalar seagull.
PAIRS = (
    ("LD-W-01", 0, 3, sp.Rational(-1, 4), False, False, 3),
    ("LD-W-02", 0, 2, sp.Rational(+1, 4), False, True, 4),
    ("LD-W-05", 1, 3, sp.Rational(+1, 4), True, False, 4),
    ("LD-W-06", 1, 2, sp.Rational(-1, 4), True, True, 5),
)


def T0(i, j, k, l):
    return sp.Integer(i == j) * sp.Integer(k == l)


def apply_R(tensor, slot, generator):
    """Explicit index contraction R^a_{i_slot,m} T(...,m,...)."""
    matrix = R[slot][generator]

    def result(*indices):
        indices = list(indices)
        total = sp.Integer(0)
        for m in range(2):
            internal = indices.copy()
            internal[slot] = m
            total += matrix[indices[slot], m] * tensor(*internal)
        return sp.simplify(total)

    return result


def matrix_word(ops):
    """Build an explicit left-to-right matrix word acting on T0."""
    tensor = T0
    for slot, generator in reversed(ops):
        tensor = apply_R(tensor, slot, generator)
    return tensor


def sum_words(terms):
    built = [(coefficient, matrix_word(ops))
             for coefficient, ops in terms]

    def result(*indices):
        return sp.simplify(sum(
            coefficient * tensor(*indices)
            for coefficient, tensor in built
        ))

    return result


def seed_pair(a, b):
    return sum_words([
        (1, [(a, x), (b, x)]) for x in range(3)
    ])


def graph_A(a, b, ext):
    # Open-chain order on A: internal-W b, then external-W a.
    return sum_words([
        (1, [(a, x), (a, ext), (b, x)]) for x in range(3)
    ])


def graph_A_reversed(a, b, ext):
    return sum_words([
        (1, [(a, ext), (a, x), (b, x)]) for x in range(3)
    ])


def graph_B(a, b, ext):
    # Conjugate-side open-chain order on B: external-W a, then internal-W b.
    return sum_words([
        (1, [(a, x), (b, ext), (b, x)]) for x in range(3)
    ])


def graph_B_reversed(a, b, ext):
    return sum_words([
        (1, [(a, x), (b, x), (b, ext)]) for x in range(3)
    ])


def three_W(a, b, ext):
    terms = []
    for x, y in product(range(3), repeat=2):
        coefficient = EPS(ext, x, y)
        if coefficient:
            terms.append((coefficient, [(a, x), (b, y)]))
    return sum_words(terms)


def seagull_A(a, b, ext):
    # Raw scalar two-gauge vertex: {R_A^a,R_A^b} on endpoint A.
    terms = []
    for x in range(3):
        terms.append((1, [(a, ext), (a, x), (b, x)]))
        terms.append((1, [(a, x), (a, ext), (b, x)]))
    return sum_words(terms)


def seagull_B(a, b, ext):
    terms = []
    for x in range(3):
        terms.append((1, [(a, x), (b, ext), (b, x)]))
        terms.append((1, [(a, x), (b, x), (b, ext)]))
    return sum_words(terms)


def verify_representation_algebra():
    checks = 0
    for slot in range(4):
        for a, b in product(range(3), repeat=2):
            lhs = R[slot][a] * R[slot][b] - R[slot][b] * R[slot][a]
            rhs = sp.zeros(2)
            for c in range(3):
                rhs += I * EPS(a, b, c) * R[slot][c]
            assert lhs == rhs
            checks += 4
    return checks


def verify_all():
    g2 = sp.symbols("g_2", real=True)
    phase_line = -g2
    phase_seagull = +g2
    phase_threeW = -I * g2

    counts = {
        "seed": 0,
        "A_commutator": 0,
        "B_commutator": 0,
        "A_phase": 0,
        "B_phase": 0,
        "A_seagull": 0,
        "B_seagull": 0,
        "A_seagull_decomposition": 0,
        "B_seagull_decomposition": 0,
    }
    rows = []

    for name, a, b, coefficient, a_scalar, b_scalar, graph_count in PAIRS:
        seed = seed_pair(a, b)
        for ix in WEAK_INDICES:
            expected = coefficient * sum(
                SIGMA[A][ix[0], ix[1]] * SIGMA[A][ix[2], ix[3]]
                for A in range(3)
            )
            assert sp.simplify(seed(*ix) - expected) == 0
            counts["seed"] += 1

        for ext in range(3):
            G = three_W(a, b, ext)
            WA, WA_rev = graph_A(a, b, ext), graph_A_reversed(a, b, ext)
            WB, WB_rev = graph_B(a, b, ext), graph_B_reversed(a, b, ext)

            for ix in WEAK_INDICES:
                da = sp.simplify(WA(*ix) - WA_rev(*ix))
                db = sp.simplify(WB(*ix) - WB_rev(*ix))
                gg = G(*ix)

                assert sp.simplify(da - I * gg) == 0
                assert sp.simplify(db - I * gg) == 0
                counts["A_commutator"] += 1
                counts["B_commutator"] += 1

                # Relative phases: P_line/P_4=-g2, P_3W/P_4=-i g2.
                assert sp.simplify(phase_line * da - phase_threeW * gg) == 0
                assert sp.simplify(phase_line * db - phase_threeW * gg) == 0
                counts["A_phase"] += 1
                counts["B_phase"] += 1

                if a_scalar:
                    SA = seagull_A(a, b, ext)
                    expected_SA = sp.Rational(1, 2) * apply_R(T0, b, ext)(*ix)
                    assert sp.simplify(SA(*ix) - expected_SA) == 0
                    assert sp.simplify(SA(*ix) - WA(*ix) - WA_rev(*ix)) == 0
                    assert sp.simplify(
                        WA(*ix) - sp.Rational(1, 2)*SA(*ix)
                        - sp.Rational(1, 2)*I*gg
                    ) == 0
                    counts["A_seagull"] += 1
                    counts["A_seagull_decomposition"] += 1

                if b_scalar:
                    SB = seagull_B(a, b, ext)
                    expected_SB = sp.Rational(1, 2) * apply_R(T0, a, ext)(*ix)
                    assert sp.simplify(SB(*ix) - expected_SB) == 0
                    assert sp.simplify(SB(*ix) - WB(*ix) - WB_rev(*ix)) == 0
                    assert sp.simplify(
                        WB(*ix) - sp.Rational(1, 2)*SB(*ix)
                        - sp.Rational(1, 2)*I*gg
                    ) == 0
                    counts["B_seagull"] += 1
                    counts["B_seagull_decomposition"] += 1

        rows.append((name, graph_count, a_scalar, b_scalar))

    return counts, rows, verify_representation_algebra(), phase_seagull


def main():
    counts, rows, rep_checks, phase_seagull = verify_all()
    assert counts == {
        "seed": 64,
        "A_commutator": 192,
        "B_commutator": 192,
        "A_phase": 192,
        "B_phase": 192,
        "A_seagull": 96,
        "B_seagull": 96,
        "A_seagull_decomposition": 96,
        "B_seagull_decomposition": 96,
    }
    assert rep_checks == 144

    print("RC-001 B2c-IVd explicit raw-index bridge: cross-vertex WW pairs")
    print(f"PASS: physical representation algebra ({rep_checks}/144 matrix components).")
    print(f"PASS: four seed pair tensors ({counts['seed']}/64 weak components).")
    print(f"PASS: A-line ordered commutator ({counts['A_commutator']}/192 components).")
    print(f"PASS: B-line ordered commutator ({counts['B_commutator']}/192 components).")
    print(f"PASS: A-line phase-weighted commutator = three-W group-phase factor ({counts['A_phase']}/192).")
    print(f"PASS: B-line phase-weighted commutator = three-W group-phase factor ({counts['B_phase']}/192).")
    print(f"PASS: raw A scalar seagull anticommutator ({counts['A_seagull']}/96).")
    print(f"PASS: raw B scalar seagull anticommutator ({counts['B_seagull']}/96).")
    print(f"PASS: A scalar line tensor = 1/2 seagull tensor + i/2 three-W tensor ({counts['A_seagull_decomposition']}/96).")
    print(f"PASS: B scalar line tensor = 1/2 seagull tensor + i/2 three-W tensor ({counts['B_seagull_decomposition']}/96).")
    print("CROSS-VERTEX ATTACHMENT CENSUS:")
    for name, graph_count, a_scalar, b_scalar in rows:
        print(f"  {name}: {graph_count} graphs; A seagull={a_scalar}; B seagull={b_scalar}")
    print("  total = 16 direct five-point attachments")
    print("RELATIVE PHASES (relative to the four-point seed):")
    print("  ordinary matter-line insertion: -g2")
    print("  scalar seagull: +g2")
    print("  internal-W three-gauge insertion: -i g2")
    print("GROUP-PHASE RESULT:")
    print("  -g2*(W_A-W_A_rev) = -i g2*G_AB")
    print("  -g2*(W_B-W_B_rev) = -i g2*G_AB")
    print("  This matches the three-W group-phase factor, but is not a Lorentz-kernel cancellation.")
    print("BOUNDARY:")
    print("  Cross-vertex weak-index ordering and relative phases only.")
    print("  Same-vertex LD-W-03/04 raw ordering remains separate because its internal W flows S -> F.")
    print("  No complete Lorentz-weighted 24-graph sum, ghost/ST completion, external-leg/CT sum,")
    print("  loop integration, transverse form factor, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
