#!/usr/bin/env python3
"""RC-001 B2c-IVl: explicit pair-dependent R_FG current projections.

The Feynman-gauge remainder is contracted with the actual oriented
fermion/scalar endpoint currents for all six WW pair classes. The central
Dirac-chain ordering and pair-dependent spectator denominators are kept.
This is an exact rational-point audit of the explicit contractions, not a
loop integration or a complete Slavnov-Taylor identity.
"""
from itertools import product
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
GAMMA = [sp.diag(1, 1, -1, -1)]
for sigma in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), sigma),
        sp.Matrix.hstack(-sigma, sp.zeros(2)),
    ))


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def scale(c, a):
    return [sp.expand(c * a[i]) for i in range(4)]


def slash(p):
    return sum((ETA[i] * p[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def as_matrix(value):
    return value if isinstance(value, sp.MatrixBase) else sp.eye(4) * value


def is_fermion_current(current):
    return isinstance(current[0], sp.MatrixBase)


def current_dot(current, p):
    if is_fermion_current(current):
        return slash(p)
    return dot(current, p)


def matrix_zero(matrix):
    return all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def rfg_numerator_direct(JA, left, middle, right, JB, k, q):
    """Contract explicit upper endpoint currents with k^mu k^nu-kq^mu kq^nu."""
    kq = add(k, q)
    out = sp.zeros(4)
    for mu, nu in product(range(4), repeat=2):
        coefficient = ETA[mu] * ETA[nu] * (
            k[mu] * k[nu] - kq[mu] * kq[nu]
        )
        out += (
            as_matrix(JA[mu]) * as_matrix(left) * as_matrix(middle)
            * as_matrix(right) * as_matrix(JB[nu]) * coefficient
        )
    return out


def rfg_numerator_compact(JA, left, middle, right, JB, k, q):
    """Factorized form; matrix order along the open fermion chain is unchanged."""
    kq = add(k, q)
    a0 = as_matrix(current_dot(JA, k))
    a1 = as_matrix(current_dot(JA, kq))
    b0 = as_matrix(current_dot(JB, k))
    b1 = as_matrix(current_dot(JB, kq))
    chain = as_matrix(left) * as_matrix(middle) * as_matrix(right)
    return a0 * chain * b0 - a1 * chain * b1


def cross_pair_data(pair_id, type_a, type_b, p_a, p_b, p1, p2, k, q):
    """Three-W cross-vertex chain: J_A X_A slash(h) X_B^Y J_B."""
    r_a = sub(k, p_a)
    r_b_y = add(add(k, p_b), q)
    h = sub(k, add(p1, p2))

    if type_a == "F":
        j_a = GAMMA
        x_a = -slash(r_a)
    else:
        j_a = sub(scale(2, p_a), k)  # V_A=2 p_A-k
        x_a = sp.eye(4)

    if type_b == "F":
        j_b = GAMMA
        x_b = slash(r_b_y)
    else:
        j_b = scale(-1, add(scale(2, p_b), add(k, q)))
        x_b = sp.eye(4)

    numerator = rfg_numerator_compact(
        j_a, x_a, slash(h), x_b, j_b, k, q
    )
    direct = rfg_numerator_direct(
        j_a, x_a, slash(h), x_b, j_b, k, q
    )
    return numerator, direct, {
        "r_A": r_a, "r_BY": r_b_y, "h": h,
        "J_A": "gamma^mu" if type_a == "F" else "2 p_A^mu-k^mu",
        "J_B": "gamma^nu" if type_b == "F" else "-2 p_B^nu-(k+q)^nu",
        "X_A": "-slash(r_A)" if type_a == "F" else "1",
        "X_B": "slash(r_B^Y)" if type_b == "F" else "1",
    }


def same_pair_data(pair_id, p_f, p_s, k, q):
    """Same-vertex S->F chain, retaining the 03/04 Dirac-Hermitian order."""
    r_f_y = add(add(k, p_f), q)
    r_s = sub(p_s, k)
    v_s = sub(scale(2, p_s), k)
    h_e = add(add(p_f, p_s), q)

    if pair_id == "03":
        # N_03 = gamma_mu slash(r_F) V_S^mu.
        j_a, j_b = GAMMA, v_s
        left, middle, right = sp.eye(4), slash(r_f_y), sp.eye(4)
        order = "gamma^mu slash(r_F^Y) V_S^nu"
    elif pair_id == "04":
        # N_04 = V_S^mu slash(r_F) gamma_mu.
        j_a, j_b = v_s, GAMMA
        left, middle, right = sp.eye(4), slash(r_f_y), sp.eye(4)
        order = "V_S^mu slash(r_F^Y) gamma^nu"
    else:
        raise ValueError(pair_id)

    numerator = rfg_numerator_compact(
        j_a, left, middle, right, j_b, k, q
    )
    direct = rfg_numerator_direct(
        j_a, left, middle, right, j_b, k, q
    )
    return numerator, direct, {
        "r_FY": r_f_y, "r_S": r_s, "h_E": h_e,
        "V_S": "2 p_S^mu-k^mu", "chain_order": order,
    }


PAIR_SPECS = (
    ("01", "F", "F", "cross"),
    ("02", "F", "S", "cross"),
    ("03", "F", "S", "same"),
    ("04", "S", "F", "same"),
    ("05", "S", "F", "cross"),
    ("06", "S", "S", "cross"),
)


def audit_point(k, q, p1, p2, p3, m_e2):
    p4 = scale(-1, add(add(add(q, p1), p2), p3))
    kq = add(k, q)
    wk2, wkq2 = dot(k, k), dot(kq, kq)
    if wk2 == 0 or wkq2 == 0:
        raise AssertionError("singular W propagator at audit point")

    results = {}
    for pair_id, type_a, type_b, family in PAIR_SPECS:
        if family == "cross":
            p_a = p1 if pair_id in ("01", "02") else p2
            p_b = p4 if pair_id in ("01", "05") else p3
            num, direct, data = cross_pair_data(
                pair_id, type_a, type_b, p_a, p_b, p1, p2, k, q
            )
            den = (
                wk2, wkq2, dot(data["r_A"], data["r_A"]),
                dot(data["r_BY"], data["r_BY"]),
                dot(data["h"], data["h"]) - m_e2,
            )
        else:
            p_f = p1 if pair_id == "03" else p4
            p_s = p2 if pair_id == "03" else p3
            num, direct, data = same_pair_data(pair_id, p_f, p_s, k, q)
            den = (
                wk2, wkq2, dot(data["r_FY"], data["r_FY"]),
                dot(data["r_S"], data["r_S"]),
                dot(data["h_E"], data["h_E"]) - m_e2,
            )

        assert matrix_zero(direct - num), f"{pair_id}: explicit tensor vs compact current form"
        assert all(value != 0 for value in den), f"{pair_id}: singular spectator denominator"
        assert any(sp.simplify(x) != 0 for x in num), f"{pair_id}: accidentally zero R_FG numerator"
        results[pair_id] = {"numerator": num, "denominators": den, "data": data}

    return results


def audit_points():
    points = (
        (
            [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)],
            [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)],
        ),
        (
            [sp.Integer(5), sp.Integer(1), sp.Integer(2), sp.Integer(0)],
            [sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Integer(2)],
            [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(0), sp.Integer(2), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(1)],
        ),
    )
    return tuple(
        audit_point(k, q, p1, p2, p3, sp.Integer(400))
        for k, q, p1, p2, p3 in points
    )


def main():
    all_results = audit_points()
    for index, results in enumerate(all_results, start=1):
        print(f"PASS: exact direct-vs-factorized R_FG contractions at rational point {index} (6/6 pairs).")
        for pair_id, result in results.items():
            den = ",".join(str(x) for x in result["denominators"])
            nonzero = sum(sp.simplify(x) != 0 for x in result["numerator"])
            print(f"  LD-W-{pair_id}: nonzero 4x4 numerator entries={nonzero}; denominator factors={den}")
    print("RESULT: explicit pair-dependent R_FG current projections pass for all six pairs.")
    print("MATRIX ORDER: LD-W-01/02/05/06 retain X_A slash(h) X_B; LD-W-03/04 retain")
    print("             the distinct gamma-slash(r_F)-V_S and V_S-slash(r_F)-gamma orientations.")
    print("BOUNDARY:")
    print("  R_FG is not set to zero; its explicit contraction is retained.")
    print("  Same-vertex heavy-channel propagators are spectator factors; their slash(h_E) numerator")
    print("  is kept outside the loop-side R_FG kernel with the seed's chiral orientation.")
    print("  Scalar seagull anticommutator terms are separate and are not folded into R_FG.")
    print("  No ghost/ST completion, loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
