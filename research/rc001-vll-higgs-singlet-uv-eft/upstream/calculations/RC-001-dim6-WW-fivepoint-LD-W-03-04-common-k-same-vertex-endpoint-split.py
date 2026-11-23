#!/usr/bin/env python3
"""RC-001 B2c-IVn-f/04: exact LD-W-03/04 same-vertex endpoint bridge.

Checks the two ordered same-vertex fermion WTIs, the S->F scalar WTI,
the k_old=k+q common-routing map, the scalar-current rebase from
V_S^line=2p_S-(k+q) to V_S^3W=2p_S-k, the physical weak-index phases,
the actual pair-dependent R_FG contractions, and the external heavy
spectator. It does not claim a complete Lorentz-weighted four-attachment
sum, full five-point STI, loop integration, or Wilson coefficient.
"""
from itertools import product
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
METRIC = sp.diag(*ETA)
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
GAMMA5 = I * GAMMA[0] * GAMMA[1] * GAMMA[2] * GAMMA[3]
PL = (sp.eye(4) - GAMMA5) / 2
PR = (sp.eye(4) + GAMMA5) / 2

R = {
    0: tuple(-t.T for t in TGEN),  # bar L
    1: TGEN,                       # H
    2: tuple(-t.T for t in TGEN),  # H dagger
    3: TGEN,                       # L
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


def dirac_bar(m):
    return GAMMA[0] * m.conjugate().T * GAMMA[0]


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


def seed_pair(F, S):
    return sum_words([(1, [(F, b), (S, b)]) for b in range(3)])


def fermion_line(F, S, ext):
    return sum_words([
        (1, [(F, b), (F, ext), (S, b)]) for b in range(3)
    ])


def fermion_line_reversed(F, S, ext):
    return sum_words([
        (1, [(F, ext), (F, b), (S, b)]) for b in range(3)
    ])


def scalar_line(F, S, ext):
    return sum_words([
        (1, [(F, b), (S, ext), (S, b)]) for b in range(3)
    ])


def scalar_line_reversed(F, S, ext):
    return sum_words([
        (1, [(F, b), (S, b), (S, ext)]) for b in range(3)
    ])


def G_FS(F, S, ext):
    return sum_words([
        (sp.LeviCivita(ext, b, c), [(F, b), (S, c)])
        for b, c in product(range(3), repeat=2)
        if sp.LeviCivita(ext, b, c)
    ])


def G_threeW_S_to_F(F, S, ext):
    g = G_FS(F, S, ext)
    return lambda *ix: sp.simplify(-g(*ix))


def scalar_seagull(F, S, ext):
    terms = []
    for b in range(3):
        terms.append((1, [(F, b), (S, ext), (S, b)]))
        terms.append((1, [(F, b), (S, b), (S, ext)]))
    return sum_words(terms)


def verify_fermion_wtis():
    q = list(sp.symbols("qWTI0:4", real=True))
    r_w = list(sp.symbols("rWTIW0:4", real=True))
    r_y = add(r_w, q)
    s_w = slash(r_w) / dot(r_w, r_w)
    s_y = slash(r_y) / dot(r_y, r_y)

    # LD-W-03: left-vertex orientation.
    lhs_03 = s_w * slash(q) * PL * s_y
    rhs_03 = s_w * PR - PL * s_y
    # LD-W-04: Dirac-Hermitian-conjugate orientation.
    lhs_04 = s_y * slash(q) * PL * s_w
    rhs_04 = PL * s_w - s_y * PR
    assert matrix_zero(lhs_03 - rhs_03)
    assert matrix_zero(lhs_04 - rhs_04)
    return 32


def verify_scalar_wti_and_current_rebase():
    k = list(sp.symbols("kS0:4", real=True))
    q = list(sp.symbols("qS0:4", real=True))
    p_s = list(sp.symbols("pS0:4", real=True))
    kap = add(k, q)
    r_s_y = sub(p_s, k)
    r_s_w = sub(p_s, kap)
    delta_y = 1 / dot(r_s_y, r_s_y)
    delta_w = 1 / dot(r_s_w, r_s_w)
    delta_s = sp.factor(delta_y - delta_w)
    v_line = sub(scale(2, p_s), kap)
    v_3w = sub(scale(2, p_s), k)

    # S->F orientation: r_S^Y-r_S^W=q and q.V gives Delta_W-Delta_Y.
    scalar_wti = dot(q, add(r_s_w, r_s_y)) / (
        dot(r_s_w, r_s_w) * dot(r_s_y, r_s_y)
    )
    assert sp.simplify(scalar_wti - (delta_w - delta_y)) == 0
    assert all(sp.simplify(r_s_y[i] - r_s_w[i] - q[i]) == 0
               for i in range(4))
    assert all(sp.simplify(v_line[i] - v_3w[i] + q[i]) == 0
               for i in range(4))

    g2, symmetric, commutator = sp.symbols("g2 S_S G_FS")
    raw = [
        g2 * (
            (sp.Rational(1, 2) * delta_s * v_line[mu]
             + delta_y * q[mu]) * symmetric
            + I * sp.Rational(1, 2) * delta_s * v_line[mu] * commutator
        )
        for mu in range(4)
    ]
    rebased = [
        g2 * (
            (sp.Rational(1, 2) * delta_s * v_3w[mu]
             + (delta_y - sp.Rational(1, 2) * delta_s) * q[mu])
            * symmetric
            + I * sp.Rational(1, 2) * delta_s * v_3w[mu] * commutator
            - I * sp.Rational(1, 2) * delta_s * q[mu] * commutator
        )
        for mu in range(4)
    ]
    assert all(sp.simplify(raw[mu] - rebased[mu]) == 0
               for mu in range(4))
    assert sp.simplify(
        delta_y - sp.Rational(1, 2) * delta_s
        - (delta_y + delta_w) / 2
    ) == 0
    return 1, 4


def verify_common_k_shift_and_denominators():
    k = list(sp.symbols("kRoute0:4", real=True))
    q = list(sp.symbols("qRoute0:4", real=True))
    p_f = list(sp.symbols("pFRoute0:4", real=True))
    p_s = list(sp.symbols("pSRoute0:4", real=True))
    k_old = add(k, q)
    kap = add(k, q)

    # Original scalar-line insertion, before k_old=k+q.
    r_s_w_old = sub(p_s, k_old)
    r_s_y_old = add(r_s_w_old, q)
    r_f_w_old = add(k_old, p_f)
    v_s_old = sub(scale(2, p_s), k_old)

    # Common-k representation used by the three-W reference.
    r_s_w = sub(p_s, kap)
    r_s_y = sub(p_s, k)
    r_f_y = add(add(k, p_f), q)
    v_s_line = sub(scale(2, p_s), kap)
    maps = (
        (r_s_w_old, r_s_w),
        (r_s_y_old, r_s_y),
        (r_f_w_old, r_f_y),
        (v_s_old, v_s_line),
        (k_old, kap),
    )
    assert all(sp.simplify(maps[n][0][mu] - maps[n][1][mu]) == 0
               for n in range(5) for mu in range(4))

    # The scalar seagull has r_S^sg=p_S-k_old+q and the same shifted F line.
    r_s_sg_old = add(sub(p_s, k_old), q)
    assert all(sp.simplify(r_s_sg_old[mu] - r_s_y[mu]) == 0
               for mu in range(4))
    assert all(sp.simplify(r_f_w_old[mu] - r_f_y[mu]) == 0
               for mu in range(4))

    # The Delta_W term in delta_S is Delta_Y(k+q); its other factors shift too.
    r_s_y_at_kq = sub(p_s, add(k, q))
    r_f_w_at_kq = add(add(k, q), p_f)
    v_3w_at_kq = sub(scale(2, p_s), add(k, q))
    assert all(sp.simplify(r_s_y_at_kq[mu] - r_s_w[mu]) == 0
               for mu in range(4))
    assert all(sp.simplify(r_f_w_at_kq[mu] - r_f_y[mu]) == 0
               for mu in range(4))
    assert all(sp.simplify(v_3w_at_kq[mu] - v_s_line[mu]) == 0
               for mu in range(4))

    h_e = add(add(p_f, p_s), q)
    assert all(sp.diff(h_e[mu], k[nu]) == 0
               for mu, nu in product(range(4), repeat=2))

    m_e2 = sp.symbols("M_E2", real=True)
    d_3w = (
        dot(k, k) * dot(kap, kap) * dot(r_f_y, r_f_y)
        * dot(r_s_y, r_s_y) * (dot(h_e, h_e) - m_e2)
    )
    d_seagull = (
        dot(kap, kap) * dot(r_f_y, r_f_y)
        * dot(r_s_y, r_s_y) * (dot(h_e, h_e) - m_e2)
    )
    assert sp.simplify(d_seagull - d_3w / dot(k, k)) == 0
    return 24, 16, 1


def verify_weak_ordering_and_phase():
    g2 = sp.symbols("g_2", real=True)
    counts = {
        "seed": 0, "F_commutator": 0, "S_commutator": 0,
        "F_threeW_phase": 0, "S_threeW_phase": 0,
        "scalar_seagull": 0,
    }
    for F, S in ((0, 1), (3, 2)):
        seed = seed_pair(F, S)
        for ix in WEAK_INDICES:
            assert sp.simplify(seed(*ix) + sp.Rational(3, 4) * T0(*ix)) == 0
            counts["seed"] += 1

        for ext in range(3):
            g = G_FS(F, S, ext)
            g_3w = G_threeW_S_to_F(F, S, ext)
            w_f = fermion_line(F, S, ext)
            w_f_rev = fermion_line_reversed(F, S, ext)
            w_s = scalar_line(F, S, ext)
            w_s_rev = scalar_line_reversed(F, S, ext)
            sg = scalar_seagull(F, S, ext)
            r_f = apply_R(T0, F, ext)

            for ix in WEAK_INDICES:
                d_f = sp.simplify(w_f(*ix) - w_f_rev(*ix))
                d_s = sp.simplify(w_s(*ix) - w_s_rev(*ix))
                gg = g(*ix)
                assert sp.simplify(d_f - I * gg) == 0
                assert sp.simplify(d_s - I * gg) == 0
                counts["F_commutator"] += 1
                counts["S_commutator"] += 1

                # Relative phases: line=-g2, three-W=-i g2, G_3W=-G_FS.
                assert sp.simplify(-g2 * d_f - I * g2 * g_3w(*ix)) == 0
                assert sp.simplify(-g2 * d_s - I * g2 * g_3w(*ix)) == 0
                counts["F_threeW_phase"] += 1
                counts["S_threeW_phase"] += 1

                assert sp.simplify(sg(*ix) - w_s(*ix) - w_s_rev(*ix)) == 0
                assert sp.simplify(
                    sg(*ix) - sp.Rational(1, 2) * r_f(*ix)
                ) == 0
                counts["scalar_seagull"] += 1

    return counts


def verify_heavy_spectator():
    mass = sp.symbols("M_E", real=True)
    h = list(sp.symbols("hE0:4", real=True))
    projected = PR * (slash(h) + mass * sp.eye(4)) * PL
    assert matrix_zero(projected - slash(h) * PL)

    p1 = list(sp.symbols("p1H0:4", real=True))
    p2 = list(sp.symbols("p2H0:4", real=True))
    p3 = list(sp.symbols("p3H0:4", real=True))
    q = list(sp.symbols("qH0:4", real=True))
    p4 = [-p1[i] - p2[i] - p3[i] - q[i] for i in range(4)]
    h_03 = add(add(p1, p2), q)
    h_04 = add(add(p3, p4), q)
    assert all(sp.simplify(h_03[i] + h_04[i] - q[i]) == 0
               for i in range(4))

    k = list(sp.symbols("kH0:4", real=True))
    assert all(
        sp.diff(h_03[i], k[j]) == 0 and sp.diff(h_04[i], k[j]) == 0
        for i, j in product(range(4), repeat=2)
    )
    return 16, 16


def slash_current(current):
    return sum((ETA[mu] * current[mu] * GAMMA[mu]
                for mu in range(4)), sp.zeros(4))


def verify_rfg_and_actual_endpoint_kernels():
    points = (
        (
            [sp.Integer(3), sp.Integer(1), sp.Integer(1), sp.Integer(0)],
            [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(1)],
            [sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(1)],
            [sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(0)],
            [sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(1)],
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
    direct_checks = 0
    endpoint_checks = 0

    for point_id, (k, q, p1, p2, p3) in enumerate(points, start=1):
        p4 = [-q[i] - p1[i] - p2[i] - p3[i] for i in range(4)]
        kap = add(k, q)

        for pair_id, p_f, p_s in (("03", p1, p2), ("04", p4, p3)):
            r_f_y = add(add(k, p_f), q)
            r_f_w = add(k, p_f)
            r_s_y = sub(p_s, k)
            r_s_w = sub(p_s, kap)
            h_e = add(add(p_f, p_s), q)
            v_line = sub(scale(2, p_s), kap)
            v_3w = sub(scale(2, p_s), k)
            delta_y = sp.Rational(1, dot(r_s_y, r_s_y))
            delta_w = sp.Rational(1, dot(r_s_w, r_s_w))
            delta_s = sp.factor(delta_y - delta_w)

            denominators = (
                dot(k, k), dot(kap, kap), dot(r_f_y, r_f_y),
                dot(r_f_w, r_f_w), dot(r_s_y, r_s_y),
                dot(r_s_w, r_s_w), dot(h_e, h_e) - 400,
            )
            assert all(value != 0 for value in denominators)
            assert delta_s != 0

            # Actual R_FG numerators, preserving the two Dirac-Hermitian orders.
            n_03 = (
                slash(k) * slash(r_f_y) * dot(v_3w, k)
                - slash(kap) * slash(r_f_y) * dot(v_3w, kap)
            )
            n_04 = (
                dot(v_3w, k) * slash(r_f_y) * slash(k)
                - dot(v_3w, kap) * slash(r_f_y) * slash(kap)
            )

            direct_03 = sp.zeros(4)
            direct_04 = sp.zeros(4)
            for mu, nu in product(range(4), repeat=2):
                coefficient = ETA[mu] * ETA[nu] * (
                    k[mu] * k[nu] - kap[mu] * kap[nu]
                )
                direct_03 += GAMMA[mu] * slash(r_f_y) * v_3w[nu] * coefficient
                direct_04 += v_3w[mu] * slash(r_f_y) * GAMMA[nu] * coefficient

            numerator = n_03 if pair_id == "03" else n_04
            direct = direct_03 if pair_id == "03" else direct_04
            assert matrix_zero(direct - numerator)
            direct_checks += 16
            nonzero_n = sum(
                sp.simplify(numerator[i, j]) != 0
                for i, j in product(range(4), repeat=2)
            )
            assert nonzero_n == 16

            # The actual scalar-line + seagull current, with S_S=G_FS=g2=1
            # as independent coefficient probes, before and after re-basing.
            raw = [
                sp.Rational(1, 2) * delta_s * v_line[mu]
                + delta_y * q[mu]
                + I * sp.Rational(1, 2) * delta_s * v_line[mu]
                for mu in range(4)
            ]
            rebased = [
                sp.Rational(1, 2) * delta_s * v_3w[mu]
                + (delta_y - sp.Rational(1, 2) * delta_s) * q[mu]
                + I * sp.Rational(1, 2) * delta_s * v_3w[mu]
                - I * sp.Rational(1, 2) * delta_s * q[mu]
                for mu in range(4)
            ]
            assert all(sp.simplify(raw[mu] - rebased[mu]) == 0
                       for mu in range(4))

            if pair_id == "03":
                kernel_raw = slash_current(raw) * slash(r_f_y) / dot(kap, kap)
                kernel_rebased = slash_current(rebased) * slash(r_f_y) / dot(kap, kap)
                q_symmetric = (
                    delta_y - delta_s / 2
                ) * slash(q) * slash(r_f_y) / dot(kap, kap)
                q_commutator = (
                    -I * delta_s / 2
                ) * slash(q) * slash(r_f_y) / dot(kap, kap)
            else:
                kernel_raw = slash(r_f_y) * slash_current(raw) / dot(kap, kap)
                kernel_rebased = slash(r_f_y) * slash_current(rebased) / dot(kap, kap)
                q_symmetric = (
                    delta_y - delta_s / 2
                ) * slash(r_f_y) * slash(q) / dot(kap, kap)
                q_commutator = (
                    -I * delta_s / 2
                ) * slash(r_f_y) * slash(q) / dot(kap, kap)

            assert matrix_zero(kernel_raw - kernel_rebased)
            endpoint_checks += 16
            q_sym_nonzero = sum(
                sp.simplify(q_symmetric[i, j]) != 0
                for i, j in product(range(4), repeat=2)
            )
            q_comm_nonzero = sum(
                sp.simplify(q_commutator[i, j]) != 0
                for i, j in product(range(4), repeat=2)
            )
            assert q_sym_nonzero > 0 and q_comm_nonzero > 0
            rows.append((
                point_id, pair_id, denominators, delta_s,
                sp.simplify(delta_y - delta_s / 2),
                nonzero_n, q_sym_nonzero, q_comm_nonzero,
            ))

    # Dirac-Hermitian order check at generic common r_F and V_S.
    k = list(sp.symbols("kHC0:4", real=True))
    q = list(sp.symbols("qHC0:4", real=True))
    r_f = list(sp.symbols("rFHC0:4", real=True))
    v_s = list(sp.symbols("vSHC0:4", real=True))
    kap = add(k, q)
    n_03 = (
        slash(k) * slash(r_f) * dot(v_s, k)
        - slash(kap) * slash(r_f) * dot(v_s, kap)
    )
    n_04 = (
        dot(v_s, k) * slash(r_f) * slash(k)
        - dot(v_s, kap) * slash(r_f) * slash(kap)
    )
    assert matrix_zero(dirac_bar(n_03) - n_04)
    return rows, direct_checks, endpoint_checks


def main():
    fermion_checks = verify_fermion_wtis()
    scalar_checks = verify_scalar_wti_and_current_rebase()
    route_checks = verify_common_k_shift_and_denominators()
    weak = verify_weak_ordering_and_phase()
    heavy_checks = verify_heavy_spectator()
    rows, rfg_checks, endpoint_checks = verify_rfg_and_actual_endpoint_kernels()

    assert weak == {
        "seed": 32, "F_commutator": 96, "S_commutator": 96,
        "F_threeW_phase": 96, "S_threeW_phase": 96,
        "scalar_seagull": 96,
    }
    assert fermion_checks == 32
    assert scalar_checks == (1, 4)
    assert route_checks == (24, 16, 1)
    assert heavy_checks == (16, 16)
    assert rfg_checks == endpoint_checks == 64

    print("RC-001 B2c-IVn-f/04: LD-W-03/04 same-vertex endpoint bridge")
    print(f"PASS: LD-W-03/04 opposite fermion WTIs ({fermion_checks}/32 Dirac components).")
    print(f"PASS: S->F scalar WTI and current rebase ({scalar_checks[0]}/1 WTI, {scalar_checks[1]}/4 vector components).")
    print(f"PASS: k_old=k+q scalar-line/seagull common-k map ({route_checks[0]}/24 vector components).")
    print(f"PASS: shifted scalar/fermion/current bridge for the Delta_W term ({route_checks[1]}/16 components).")
    print("PASS: seagull denominator equals the three-W denominator divided by k^2 (1/1 exact identity).")
    print(f"PASS: same-vertex weak tensors and S->F group phases: {weak}.")
    print(f"PASS: chiral heavy-propagator projection and k-independent spectator ({heavy_checks[0]}/16 matrix, {heavy_checks[1]}/16 momentum checks).")
    print(f"PASS: actual LD-W-03/04 R_FG direct-vs-factorized contractions ({rfg_checks}/64 matrix components).")
    print(f"PASS: actual scalar endpoint kernels raw-vs-rebased ({endpoint_checks}/64 matrix components).")
    for point_id, pair_id, den, delta, symcoef, n_nonzero, qs, qc in rows:
        print(
            f"  point {point_id}, LD-W-{pair_id}: denominators={den}; "
            f"delta_S={delta}; symmetric q coefficient={symcoef}; "
            f"N_RFG={n_nonzero}/16; q contacts={qs}/16,{qc}/16"
        )
    print("RESULT: the same-vertex scalar endpoint is now in the actual three-W current basis:")
    print("  V_S^line=2p_S-(k+q)=V_S^3W-q, V_S^3W=2p_S-k.")
    print("  The symmetric q contact is (Delta_Y+Delta_W)/2; the commutator q contact is -i delta_S/2.")
    print("  LD-W-03 keeps slash(C_S) slash(r_F^Y); LD-W-04 keeps slash(r_F^Y) slash(C_S).")
    print("BOUNDARY: this does not sum the four longitudinal attachments with all endpoint/LSZ terms.")
    print("          The q contacts and R_FG are retained; no physical non-cancellation, full STI,")
    print("          loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
