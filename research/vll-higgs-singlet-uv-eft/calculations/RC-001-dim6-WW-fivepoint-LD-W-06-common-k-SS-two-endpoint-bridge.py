#!/usr/bin/env python3
"""RC-001 B2c-IVn-f/05: exact LD-W-06 S-S two-endpoint common-k bridge.

Keeps the A and B scalar-line/seagull sub-blocks separate, rebases each
actual scalar current into its own three-W current basis, checks the
distinct seagull weak tensors, and verifies the actual S-S R_FG numerator.
No complete five-point Ward/ST cancellation is claimed.
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
TGEN = tuple(s / 2 for s in SIGMA)
GAMMA = [sp.diag(1, 1, -1, -1)]
for sigma in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), sigma),
        sp.Matrix.hstack(-sigma, sp.zeros(2)),
    ))
R = {
    0: tuple(-t.T for t in TGEN),
    1: TGEN,
    2: tuple(-t.T for t in TGEN),
    3: TGEN,
}
WEAK_INDICES = tuple(product(range(2), repeat=4))


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def add(a, b):
    return [sp.expand(a[i] + b[i]) for i in range(4)]


def sub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def scale(c, a):
    return [sp.expand(c * a[i]) for i in range(4)]


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i in range(m.rows) for j in range(m.cols))


def T0(i, j, k, ell):
    return sp.Integer(int(i == j and k == ell))


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


def G_AB(ext):
    return sum_words([
        (sp.LeviCivita(ext, b, c), [(1, b), (2, c)])
        for b, c in product(range(3), repeat=2)
        if sp.LeviCivita(ext, b, c)
    ])


def verify_A_B_scalar_rebases():
    k = list(sp.symbols("k06S0:4", real=True))
    q = list(sp.symbols("q06S0:4", real=True))
    p_a = list(sp.symbols("pA06S0:4", real=True))
    p_b = list(sp.symbols("pB06S0:4", real=True))
    kap = add(k, q)

    # A-side scalar endpoint: A-oriented WTI.
    r_a_y = sub(k, p_a)
    r_a_w = sub(kap, p_a)
    delta_a_y = 1 / dot(r_a_y, r_a_y)
    delta_a_w = 1 / dot(r_a_w, r_a_w)
    delta_a = sp.factor(delta_a_y - delta_a_w)
    v_a_line = sub(scale(2, p_a), kap)
    v_a_3w = sub(scale(2, p_a), k)
    wti_a = dot(q, add(r_a_w, r_a_y)) / (
        dot(r_a_w, r_a_w) * dot(r_a_y, r_a_y)
    )
    assert sp.simplify(wti_a - delta_a) == 0
    assert all(sp.simplify(v_a_line[i] - v_a_3w[i] + q[i]) == 0
               for i in range(4))

    # B-side scalar endpoint: oppositely oriented B WTI.
    r_b_y = add(kap, p_b)
    r_b_w = add(k, p_b)
    delta_b_y = 1 / dot(r_b_y, r_b_y)
    delta_b_w = 1 / dot(r_b_w, r_b_w)
    delta_b = sp.factor(delta_b_y - delta_b_w)
    v_b_line = scale(-1, add(scale(2, p_b), k))
    v_b_3w = scale(-1, add(scale(2, p_b), kap))
    wti_b = dot(q, add(r_b_w, r_b_y)) / (
        dot(r_b_w, r_b_w) * dot(r_b_y, r_b_y)
    )
    assert sp.simplify(wti_b - (delta_b_w - delta_b_y)) == 0
    assert all(sp.simplify(v_b_line[i] - v_b_3w[i] - q[i]) == 0
               for i in range(4))

    g2, s_a, s_b, g_ab = sp.symbols("g2 S_A S_B G_AB")
    c_a_raw = [
        g2 * (
            (-sp.Rational(1, 2) * delta_a * v_a_line[i]
             + delta_a_y * q[i]) * s_a
            - I * sp.Rational(1, 2) * delta_a * v_a_line[i] * g_ab
        )
        for i in range(4)
    ]
    c_a_rebased = [
        g2 * (
            (-sp.Rational(1, 2) * delta_a * v_a_3w[i]
             + (delta_a_y + delta_a / 2) * q[i]) * s_a
            + (-I * sp.Rational(1, 2) * delta_a * v_a_3w[i]
               + I * sp.Rational(1, 2) * delta_a * q[i]) * g_ab
        )
        for i in range(4)
    ]
    c_b_raw = [
        g2 * (
            (sp.Rational(1, 2) * delta_b * v_b_line[i]
             + delta_b_y * q[i]) * s_b
            + I * sp.Rational(1, 2) * delta_b * v_b_line[i] * g_ab
        )
        for i in range(4)
    ]
    c_b_rebased = [
        g2 * (
            (sp.Rational(1, 2) * delta_b * v_b_3w[i]
             + (delta_b_y + delta_b / 2) * q[i]) * s_b
            + (I * sp.Rational(1, 2) * delta_b * v_b_3w[i]
               + I * sp.Rational(1, 2) * delta_b * q[i]) * g_ab
        )
        for i in range(4)
    ]
    assert all(sp.simplify(c_a_raw[i] - c_a_rebased[i]) == 0
               for i in range(4))
    assert all(sp.simplify(c_b_raw[i] - c_b_rebased[i]) == 0
               for i in range(4))
    return (1, 4), (1, 4)


def verify_common_k_routes_and_denominators():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p_a = list(sp.symbols("pARoute0:4", real=True))
    p_b = list(sp.symbols("pBRoute0:4", real=True))
    p1 = list(sp.symbols("p1Route0:4", real=True))
    p2 = list(sp.symbols("p2Route0:4", real=True))
    k_old = add(k, q)
    kap = add(k, q)

    # A scalar-line/seagull route: k_old=k+q.
    r_a_y_old = sub(k_old, add(p_a, q))
    r_a_w_old = sub(k_old, p_a)
    h_a_old = sub(sub(k_old, add(p1, p2)), q)
    r_b_old = add(k_old, p_b)
    v_a_old = sub(scale(2, p_a), k_old)
    r_a_y = sub(k, p_a)
    r_a_w = sub(kap, p_a)
    h = sub(k, add(p1, p2))
    r_b_y = add(kap, p_b)
    v_a_line = sub(scale(2, p_a), kap)
    a_maps = (
        (r_a_y_old, r_a_y), (r_a_w_old, r_a_w),
        (h_a_old, h), (r_b_old, r_b_y),
        (v_a_old, v_a_line), (k_old, kap),
    )
    assert all(sp.simplify(a_maps[n][0][mu] - a_maps[n][1][mu]) == 0
               for n in range(6) for mu in range(4))

    # A seagull's scalar propagator and B spectator map to r_A^Y and r_B^Y.
    r_a_sg_old = sub(k_old, add(p_a, q))
    assert all(sp.simplify(r_a_sg_old[mu] - r_a_y[mu]) == 0
               for mu in range(4))

    # B scalar-line/seagull stays unshifted.
    r_b_y_b = add(kap, p_b)
    r_b_w_b = add(k, p_b)
    r_a_b = sub(k, p_a)
    v_b_line = scale(-1, add(scale(2, p_b), k))
    assert all(sp.simplify(r_b_y_b[mu] - (k[mu] + q[mu] + p_b[mu])) == 0
               for mu in range(4))
    assert all(sp.simplify(r_b_w_b[mu] - (k[mu] + p_b[mu])) == 0
               for mu in range(4))
    assert all(sp.simplify(r_a_b[mu] - r_a_y[mu]) == 0
               for mu in range(4))

    h_e2 = sp.symbols("H2", real=True)
    d_3w = (
        dot(k, k) * dot(kap, kap) * dot(r_a_y, r_a_y)
        * dot(r_b_y, r_b_y) * h_e2
    )
    d_a_line = (
        dot(kap, kap) * dot(r_b_y, r_b_y)
        * dot(r_a_y, r_a_y) * dot(r_a_w, r_a_w) * h_e2
    )
    d_a_sg = (
        dot(kap, kap) * dot(r_b_y, r_b_y)
        * dot(r_a_y, r_a_y) * h_e2
    )
    r_b_w = add(k, p_b)
    d_b_line = (
        dot(k, k) * dot(r_a_y, r_a_y)
        * dot(r_b_y, r_b_y) * dot(r_b_w, r_b_w) * h_e2
    )
    d_b_sg = (
        dot(k, k) * dot(r_a_y, r_a_y)
        * dot(r_b_y, r_b_y) * h_e2
    )
    assert sp.simplify(d_a_sg - d_3w / dot(k, k)) == 0
    assert sp.simplify(d_b_sg - d_3w / dot(kap, kap)) == 0
    return 24, 2


def verify_weak_tensors():
    counts = {"A_commutator": 0, "B_commutator": 0,
              "A_seagull": 0, "B_seagull": 0}
    a_slot, b_slot = 1, 2  # H and H dagger in LD-W-06
    for ext in range(3):
        g = G_AB(ext)
        w_a = sum_words([
            (1, [(a_slot, b), (a_slot, ext), (b_slot, b)])
            for b in range(3)
        ])
        w_a_rev = sum_words([
            (1, [(a_slot, ext), (a_slot, b), (b_slot, b)])
            for b in range(3)
        ])
        w_b = sum_words([
            (1, [(a_slot, b), (b_slot, ext), (b_slot, b)])
            for b in range(3)
        ])
        w_b_rev = sum_words([
            (1, [(a_slot, b), (b_slot, b), (b_slot, ext)])
            for b in range(3)
        ])
        r_a = apply_R(T0, a_slot, ext)
        r_b = apply_R(T0, b_slot, ext)
        for ix in WEAK_INDICES:
            gg = g(*ix)
            assert sp.simplify(w_a(*ix) - w_a_rev(*ix) - I * gg) == 0
            assert sp.simplify(w_b(*ix) - w_b_rev(*ix) - I * gg) == 0
            assert sp.simplify(
                w_a(*ix) + w_a_rev(*ix) - sp.Rational(1, 2) * r_b(*ix)
            ) == 0
            assert sp.simplify(
                w_b(*ix) + w_b_rev(*ix) - sp.Rational(1, 2) * r_a(*ix)
            ) == 0
            counts["A_commutator"] += 1
            counts["B_commutator"] += 1
            counts["A_seagull"] += 1
            counts["B_seagull"] += 1
    return counts


def verify_rfg_and_endpoint_kernels():
    points = (
        (
            [sp.Integer(4), sp.Integer(1), sp.Integer(2), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(2)],
            [sp.Integer(2), sp.Integer(1), sp.Integer(1), sp.Integer(1)],
        ),
        (
            [sp.Integer(6), sp.Integer(1), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(0)],
            [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(0), sp.Integer(2), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(2), sp.Integer(0), sp.Integer(1), sp.Integer(0)],
        ),
    )
    rows = []
    rfg_checks = 0
    endpoint_checks = 0

    for point_id, (k, q, p1, p2, p3) in enumerate(points, start=1):
        kap = add(k, q)
        h = sub(k, add(p1, p2))
        r_a = sub(k, p2)
        r_a_w = sub(kap, p2)
        r_b_y = add(kap, p3)
        r_b_w = add(k, p3)
        v_a_line = sub(scale(2, p2), kap)
        v_a_3w = sub(scale(2, p2), k)
        v_b_line = scale(-1, add(scale(2, p3), k))
        v_b_3w = scale(-1, add(scale(2, p3), kap))

        delta_a_y = sp.Rational(1, dot(r_a, r_a))
        delta_a_w = sp.Rational(1, dot(r_a_w, r_a_w))
        delta_a = sp.factor(delta_a_y - delta_a_w)
        delta_b_y = sp.Rational(1, dot(r_b_y, r_b_y))
        delta_b_w = sp.Rational(1, dot(r_b_w, r_b_w))
        delta_b = sp.factor(delta_b_y - delta_b_w)

        m_e2 = sp.Integer(400)
        d_3w = (
            dot(k, k), dot(kap, kap), dot(r_a, r_a),
            dot(r_b_y, r_b_y), dot(h, h) - m_e2,
        )
        d_a_line = (
            dot(kap, kap), dot(r_b_y, r_b_y),
            dot(r_a, r_a), dot(r_a_w, r_a_w), dot(h, h) - m_e2,
        )
        d_a_sg = (
            dot(kap, kap), dot(r_b_y, r_b_y),
            dot(r_a, r_a), dot(h, h) - m_e2,
        )
        d_b_line = (
            dot(k, k), dot(r_a, r_a), dot(r_b_y, r_b_y),
            dot(r_b_w, r_b_w), dot(h, h) - m_e2,
        )
        d_b_sg = (
            dot(k, k), dot(r_a, r_a), dot(r_b_y, r_b_y),
            dot(h, h) - m_e2,
        )
        assert all(value != 0 for value in d_3w + d_a_line + d_a_sg + d_b_line + d_b_sg)
        assert delta_a != 0 and delta_b != 0

        # Actual S-S R_FG numerator and direct tensor contraction.
        n_06 = (
            dot(v_a_3w, k) * slash(h) * dot(v_b_3w, k)
            - dot(v_a_3w, kap) * slash(h) * dot(v_b_3w, kap)
        )
        direct = sp.zeros(4)
        for mu, nu in product(range(4), repeat=2):
            coefficient = ETA[mu] * ETA[nu] * (
                k[mu] * k[nu] - kap[mu] * kap[nu]
            )
            direct += v_a_3w[mu] * slash(h) * v_b_3w[nu] * coefficient
        assert matrix_zero(direct - n_06)
        rfg_checks += 16
        n_nonzero = sum(
            sp.simplify(n_06[i, j]) != 0
            for i, j in product(range(4), repeat=2)
        )
        assert n_nonzero > 0

        # Independent S_A, S_B, and G_AB coefficient probes (g2=1).
        c_a_raw = [
            (-sp.Rational(1, 2) * delta_a * v_a_line[i]
             + delta_a_y * q[i])
            - I * sp.Rational(1, 2) * delta_a * v_a_line[i]
            for i in range(4)
        ]
        c_a_rebased = [
            (-sp.Rational(1, 2) * delta_a * v_a_3w[i]
             + (delta_a_y + delta_a / 2) * q[i])
            - I * sp.Rational(1, 2) * delta_a * v_a_3w[i]
            + I * sp.Rational(1, 2) * delta_a * q[i]
            for i in range(4)
        ]
        c_b_raw = [
            (sp.Rational(1, 2) * delta_b * v_b_line[i]
             + delta_b_y * q[i])
            + I * sp.Rational(1, 2) * delta_b * v_b_line[i]
            for i in range(4)
        ]
        c_b_rebased = [
            (sp.Rational(1, 2) * delta_b * v_b_3w[i]
             + (delta_b_y + delta_b / 2) * q[i])
            + I * sp.Rational(1, 2) * delta_b * v_b_3w[i]
            + I * sp.Rational(1, 2) * delta_b * q[i]
            for i in range(4)
        ]
        assert all(sp.simplify(c_a_raw[i] - c_a_rebased[i]) == 0
                   for i in range(4))
        assert all(sp.simplify(c_b_raw[i] - c_b_rebased[i]) == 0
                   for i in range(4))

        # The actual contracted scalar endpoint kernels keep their own W momentum.
        k_a_raw = slash(h) * dot(v_b_3w, c_a_raw) / dot(kap, kap)
        k_a_new = slash(h) * dot(v_b_3w, c_a_rebased) / dot(kap, kap)
        k_b_raw = dot(v_a_3w, c_b_raw) * slash(h) / dot(k, k)
        k_b_new = dot(v_a_3w, c_b_rebased) * slash(h) / dot(k, k)
        assert matrix_zero(k_a_raw - k_a_new)
        assert matrix_zero(k_b_raw - k_b_new)
        endpoint_checks += 32

        # Four q contacts are distinct: A/B x symmetric/commutator tensors.
        q_a_s = (
            (delta_a_y + delta_a / 2) * dot(v_b_3w, q)
            * slash(h) / dot(kap, kap)
        )
        q_a_c = (
            I * delta_a / 2 * dot(v_b_3w, q)
            * slash(h) / dot(kap, kap)
        )
        q_b_s = (
            (delta_b_y + delta_b / 2) * dot(v_a_3w, q)
            * slash(h) / dot(k, k)
        )
        q_b_c = (
            I * delta_b / 2 * dot(v_a_3w, q)
            * slash(h) / dot(k, k)
        )
        nonzero = lambda m: sum(
            sp.simplify(m[i, j]) != 0
            for i, j in product(range(4), repeat=2)
        )
        contacts = (nonzero(q_a_s), nonzero(q_a_c),
                    nonzero(q_b_s), nonzero(q_b_c))
        assert all(n > 0 for n in contacts)
        rows.append((
            point_id, d_3w, d_a_line, d_a_sg, d_b_line, d_b_sg,
            delta_a, delta_b, n_nonzero, contacts,
        ))

    return rows, rfg_checks, endpoint_checks


def main():
    a_rebase, b_rebase = verify_A_B_scalar_rebases()
    route_checks = verify_common_k_routes_and_denominators()
    weak = verify_weak_tensors()
    rows, rfg_checks, endpoint_checks = verify_rfg_and_endpoint_kernels()

    assert a_rebase == b_rebase == (1, 4)
    assert route_checks == (24, 2)
    assert weak == {
        "A_commutator": 48, "B_commutator": 48,
        "A_seagull": 48, "B_seagull": 48,
    }
    assert rfg_checks == 32
    assert endpoint_checks == 64

    print("RC-001 B2c-IVn-f/05: LD-W-06 S-S two-endpoint common-k bridge")
    print(f"PASS: A-side scalar WTI/current rebase ({a_rebase[0]}/1, {a_rebase[1]}/4).")
    print(f"PASS: B-side scalar WTI/current rebase ({b_rebase[0]}/1, {b_rebase[1]}/4).")
    print(f"PASS: A scalar shift and B unshifted common-k routes ({route_checks[0]}/24 vector components).")
    print(f"PASS: distinct A/B seagull denominator relations ({route_checks[1]}/2 exact identities).")
    print(f"PASS: A/B commutators and separate seagull tensors ({weak}).")
    print(f"PASS: actual S-S R_FG direct-vs-factorized contraction ({rfg_checks}/32 matrix components).")
    print(f"PASS: A/B scalar endpoint kernels raw-vs-rebased ({endpoint_checks}/64 matrix components).")
    for row in rows:
        point, d3, da_line, da_sg, db_line, db_sg, da, db, nnz, contacts = row
        print(
            f"  point {point}: D3W={d3}; DA-line={da_line}; DA-sg={da_sg}; "
            f"DB-line={db_line}; DB-sg={db_sg}; "
            f"delta_A={da}; delta_B={db}; N06={nnz}/16; "
            f"(A_sym,A_comm,B_sym,B_comm)={contacts}"
        )
    print("RESULT: the two LD-W-06 scalar endpoints have separate rebased currents:")
    print("  A: V_A^line=V_A^3W-q; B: V_B^line=V_B^3W+q.")
    print("  Both symmetric q coefficients are Delta_Y+delta/2; both commutator coefficients are +i delta/2.")
    print("  S_A and S_B remain distinct; the common G_AB tensor does not identify the two seagulls.")
    print("BOUNDARY: no sum with the fermion/Yukawa endpoint variations, three-W D(k)-D(k+q),")
    print("          external legs/LSZ, or ghost/ST terms is claimed. No Wilson coefficient is extracted.")


if __name__ == "__main__":
    main()
