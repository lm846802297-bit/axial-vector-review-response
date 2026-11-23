#!/usr/bin/env python3
"""RC-001 B2c-IVe: raw weak-index bridge for same-vertex WW pairs.

The internal W is oriented from the scalar endpoint S to the fermion
endpoint F. This reverses the three-W weak-index orientation relative to
the cross-vertex A -> B pairs. All weak-index contractions are explicit.
The script checks group/phase factors only, not the Lorentz-kernel sum.
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

# All-incoming tensor slots: (bar L, H, Hdag, L).
R = {
    0: tuple(-t.T for t in TGEN),
    1: TGEN,
    2: tuple(-t.T for t in TGEN),
    3: TGEN,
}

# F is the fermion endpoint and S the scalar endpoint. The internal W flows
# S -> F in both same-vertex routings.
PAIRS = (
    ("LD-W-03", 0, 1, sp.Rational(-3, 4), 4),
    ("LD-W-04", 3, 2, sp.Rational(-3, 4), 4),
)


def T0(i, j, k, l):
    return sp.Integer(i == j) * sp.Integer(k == l)


def apply_R(tensor, slot, generator):
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


def seed_pair(F, S):
    return sum_words([
        (1, [(F, b), (S, b)]) for b in range(3)
    ])


def fermion_line(F, S, ext):
    # The F open-chain ordering is internal-W b, then external-W a.
    return sum_words([
        (1, [(F, b), (F, ext), (S, b)]) for b in range(3)
    ])


def fermion_line_reversed(F, S, ext):
    return sum_words([
        (1, [(F, ext), (F, b), (S, b)]) for b in range(3)
    ])


def scalar_line(F, S, ext):
    # The S open-chain ordering is external-W a, then internal-W b.
    return sum_words([
        (1, [(F, b), (S, ext), (S, b)]) for b in range(3)
    ])


def scalar_line_reversed(F, S, ext):
    return sum_words([
        (1, [(F, b), (S, b), (S, ext)]) for b in range(3)
    ])


def G_FS(F, S, ext):
    terms = []
    for b, c in product(range(3), repeat=2):
        coefficient = EPS(ext, b, c)
        if coefficient:
            terms.append((coefficient, [(F, b), (S, c)]))
    return sum_words(terms)


def G_threeW_S_to_F(F, S, ext):
    # At the three-W vertex the internal index b is on S and c on F:
    # eps^{a b c} R_S^b R_F^c = -eps^{a b c} R_F^b R_S^c.
    return lambda *indices: sp.simplify(-G_FS(F, S, ext)(*indices))


def scalar_seagull(F, S, ext):
    terms = []
    for b in range(3):
        terms.append((1, [(F, b), (S, ext), (S, b)]))
        terms.append((1, [(F, b), (S, b), (S, ext)]))
    return sum_words(terms)


def verify_representation_algebra():
    checks = 0
    for slot in range(4):
        for a, b in product(range(3), repeat=2):
            lhs = R[slot][a] * R[slot][b] - R[slot][b] * R[slot][a]
            rhs = sp.zeros(2)
            for c in range(3):
                rhs += sp.I * EPS(a, b, c) * R[slot][c]
            assert lhs == rhs
            checks += 4
    return checks


def verify_all():
    g2 = sp.symbols("g_2", real=True)
    phase_line = -g2
    phase_seagull = +g2
    phase_threeW = -sp.I * g2

    counts = {
        "seed": 0,
        "F_commutator": 0,
        "S_commutator": 0,
        "F_threeW_group_phase": 0,
        "S_threeW_group_phase": 0,
        "scalar_seagull": 0,
    }
    rows = []

    for name, F, S, coefficient, graph_count in PAIRS:
        seed = seed_pair(F, S)
        for ix in WEAK_INDICES:
            assert sp.simplify(seed(*ix) - coefficient*T0(*ix)) == 0
            counts["seed"] += 1

        for ext in range(3):
            G = G_FS(F, S, ext)
            G3 = G_threeW_S_to_F(F, S, ext)
            WF = fermion_line(F, S, ext)
            WFr = fermion_line_reversed(F, S, ext)
            WS = scalar_line(F, S, ext)
            WSr = scalar_line_reversed(F, S, ext)
            SG = scalar_seagull(F, S, ext)

            for ix in WEAK_INDICES:
                dF = sp.simplify(WF(*ix) - WFr(*ix))
                dS = sp.simplify(WS(*ix) - WSr(*ix))
                gg = G(*ix)
                assert sp.simplify(dF - sp.I*gg) == 0
                assert sp.simplify(dS - sp.I*gg) == 0
                counts["F_commutator"] += 1
                counts["S_commutator"] += 1

                # -g2*(+i G_FS) + (-i g2)*(-G_FS) = 0.
                assert sp.simplify(phase_line*dF + phase_threeW*G3(*ix)) == 0
                assert sp.simplify(phase_line*dS + phase_threeW*G3(*ix)) == 0
                counts["F_threeW_group_phase"] += 1
                counts["S_threeW_group_phase"] += 1

                # The scalar seagull is the anticommutator on S.
                assert sp.simplify(SG(*ix) - WS(*ix) - WSr(*ix)) == 0
                expected = sp.Rational(1, 2)*apply_R(T0, F, ext)(*ix)
                assert sp.simplify(SG(*ix) - expected) == 0
                counts["scalar_seagull"] += 1

        rows.append((name, graph_count, F, S))

    return counts, rows, verify_representation_algebra(), phase_seagull


def main():
    counts, rows, rep_checks, _ = verify_all()
    assert counts == {
        "seed": 32,
        "F_commutator": 96,
        "S_commutator": 96,
        "F_threeW_group_phase": 96,
        "S_threeW_group_phase": 96,
        "scalar_seagull": 96,
    }
    assert rep_checks == 144

    print("RC-001 B2c-IVe raw weak-index bridge: same-vertex WW pairs")
    print(f"PASS: physical representation algebra ({rep_checks}/144 matrix components).")
    print(f"PASS: two same-vertex seed tensors ({counts['seed']}/32 weak components).")
    print(f"PASS: F-line ordered commutators ({counts['F_commutator']}/96 components).")
    print(f"PASS: S-line ordered commutators ({counts['S_commutator']}/96 components).")
    print(f"PASS: F-line commutator phase cancels the S->F three-W group phase ({counts['F_threeW_group_phase']}/96).")
    print(f"PASS: S-line commutator phase cancels the S->F three-W group phase ({counts['S_threeW_group_phase']}/96).")
    print(f"PASS: raw scalar seagull anticommutator ({counts['scalar_seagull']}/96).")
    print("SAME-VERTEX ATTACHMENT CENSUS:")
    for name, graph_count, F, S in rows:
        print(f"  {name}: F=slot {F}; S=slot {S}; {graph_count} graphs")
    print("  total = 8 direct five-point attachments")
    print("ORIENTATION:")
    print("  internal W flows S -> F, so G_3W = -G_FS.")
    print("  matter-line phase-weighted commutator = -i g2 G_FS.")
    print("  three-W phase-weighted tensor = +i g2 G_FS.")
    print("BOUNDARY:")
    print("  Same-vertex raw weak ordering and group-phase relation only.")
    print("  The Lorentz kernels and shifted heavy denominator remain to be summed.")
    print("  No complete Lorentz-weighted 24-graph cancellation, ghost/ST completion,")
    print("  external-leg/CT sum, loop integration, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
