#!/usr/bin/env python3
"""RC-001-WW-UV-FF-02: five-point routing and longitudinal numerator audit.

This is an exact symbolic routing/line-identity audit. It does not integrate
any five-point loop, fix the complete graph phases/multiplicities, or close
the Slavnov-Taylor identity.
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
GAMMA5 = I * GAMMA[0] * GAMMA[1] * GAMMA[2] * GAMMA[3]
PL = (sp.eye(4) - GAMMA5) / 2
PR = (sp.eye(4) + GAMMA5) / 2
METRIC = sp.diag(*ETA)


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def zero_vector(v):
    return all(sp.simplify(x) == 0 for x in v)


def check_route(equations, label):
    assert all(zero_vector(eq) for eq in equations), label


def check_matrix_zero(matrix, label):
    assert all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols)), label


p1 = list(sp.symbols("p1_0:4"))
p2 = list(sp.symbols("p2_0:4"))
p3 = list(sp.symbols("p3_0:4"))
q = list(sp.symbols("q_0:4"))
k = list(sp.symbols("k_0:4"))
# Five-point all-incoming conservation: p1+p2+p3+p4+q=0.
p4 = [sp.expand(-q[i] - p1[i] - p2[i] - p3[i]) for i in range(4)]
# Four-point seed routing is the q=0 limit.
p4_0 = [sp.expand(-p1[i] - p2[i] - p3[i]) for i in range(4)]
P_L = [sp.expand(p1[i] + p2[i]) for i in range(4)]

# Cross-vertex cycle: A is attached to the left Yukawa vertex, B to the
# right Yukawa vertex. A' and B' are the spectator external fields.
CROSS = (
    ("01", "barL", "L", "F", "F", p1, p4, p2, p3),
    ("02", "barL", "Hdag", "F", "S", p1, p3, p2, p4),
    ("05", "H", "L", "S", "F", p2, p4, p1, p3),
    ("06", "H", "Hdag", "S", "S", p2, p3, p1, p4),
)
SAME = (
    ("03", "barL", "H", p1, p2),
    ("04", "L", "Hdag", p4, p3),
)


def verify_cross_routes():
    base = 0
    five = 0
    for pid, _, _, kind_a, kind_b, p_a, p_b, p_ap, p_bp in CROSS:
        # q=0 four-point seed.
        p_b0 = p4_0 if pid in ("01", "05") else p_b
        p_bp0 = p3 if pid in ("01", "05") else p4_0
        r_a0 = [k[i] - p_a[i] for i in range(4)]
        r_b0 = [k[i] + p_b0[i] for i in range(4)]
        h0 = [k[i] - P_L[i] for i in range(4)]
        check_route([
            [p_a[i] + r_a0[i] - k[i] for i in range(4)],
            [p_b0[i] + k[i] - r_b0[i] for i in range(4)],
            [p_ap[i] + h0[i] - r_a0[i] for i in range(4)],
            [p_bp0[i] + r_b0[i] - h0[i] for i in range(4)],
        ], f"{pid} four-point seed")
        base += 1

        r_a = [k[i] - p_a[i] for i in range(4)]
        r_b = [k[i] + p_b[i] for i in range(4)]
        h = [k[i] - P_L[i] for i in range(4)]

        # External W on A matter propagator: r_A^Y -> r_A^W=r_A^Y+q.
        r_a_y = [k[i] - p_a[i] - q[i] for i in range(4)]
        h_a = [k[i] - P_L[i] - q[i] for i in range(4)]
        check_route([
            [r_a_y[i] + q[i] - r_a[i] for i in range(4)],
            [p_a[i] + r_a[i] - k[i] for i in range(4)],
            [p_ap[i] + h_a[i] - r_a_y[i] for i in range(4)],
            [p_bp[i] + r_b[i] - h_a[i] for i in range(4)],
        ], f"{pid} A-line insertion")
        five += 1

        # External W on B matter propagator.
        r_b_y = [k[i] + p_b[i] + q[i] for i in range(4)]
        check_route([
            [r_b[i] + q[i] - r_b_y[i] for i in range(4)],
            [p_b[i] + k[i] - r_b[i] for i in range(4)],
            [p_ap[i] + h[i] - r_a[i] for i in range(4)],
            [p_bp[i] + r_b_y[i] - h[i] for i in range(4)],
        ], f"{pid} B-line insertion")
        five += 1

        # External W on the internal W line; k_A=k, k_B=k+q.
        k_a = k
        k_b = [k[i] + q[i] for i in range(4)]
        r_b_w = [k[i] + p_b[i] + q[i] for i in range(4)]
        check_route([
            [q[i] + k_a[i] - k_b[i] for i in range(4)],
            [p_a[i] + r_a[i] - k_a[i] for i in range(4)],
            [p_b[i] + k_b[i] - r_b_w[i] for i in range(4)],
            [p_ap[i] + h[i] - r_a[i] for i in range(4)],
            [p_bp[i] + r_b_w[i] - h[i] for i in range(4)],
        ], f"{pid} three-W insertion")
        five += 1

        # Scalar two-gauge seagull at A, when A is H.
        if kind_a == "S":
            r_a_sg = [k[i] - p_a[i] - q[i] for i in range(4)]
            h_sg = [k[i] - P_L[i] - q[i] for i in range(4)]
            check_route([
                [p_a[i] + q[i] + r_a_sg[i] - k[i] for i in range(4)],
                [p_ap[i] + h_sg[i] - r_a_sg[i] for i in range(4)],
                [p_bp[i] + r_b[i] - h_sg[i] for i in range(4)],
                [p_b[i] + k[i] - r_b[i] for i in range(4)],
            ], f"{pid} A scalar seagull")
            five += 1

        # Scalar two-gauge seagull at B, when B is H or Hdag.
        if kind_b == "S":
            r_b_sg = [k[i] + p_b[i] + q[i] for i in range(4)]
            check_route([
                [p_b[i] + k[i] + q[i] - r_b_sg[i] for i in range(4)],
                [p_ap[i] + h[i] - r_a[i] for i in range(4)],
                [p_bp[i] + r_b_sg[i] - h[i] for i in range(4)],
                [p_a[i] + r_a[i] - k[i] for i in range(4)],
            ], f"{pid} B scalar seagull")
            five += 1

    return base, five


def verify_same_vertex_routes():
    base = 0
    five = 0
    for pid, _, _, p_f, p_s in SAME:
        # q=0 seed, with the heavy line outside the loop.
        p_f0 = p4_0 if pid == "04" else p_f
        r_f0 = [k[i] + p_f0[i] for i in range(4)]
        r_s0 = [p_s[i] - k[i] for i in range(4)]
        h0 = [p_f0[i] + p_s[i] for i in range(4)]
        check_route([
            [p_f0[i] + k[i] - r_f0[i] for i in range(4)],
            [p_s[i] - r_s0[i] - k[i] for i in range(4)],
            [r_f0[i] + r_s0[i] - h0[i] for i in range(4)],
        ], f"{pid} four-point seed")
        base += 1

        # External W on fermion line.
        r_f_y = [k[i] + p_f[i] + q[i] for i in range(4)]
        h_q = [p_f[i] + p_s[i] + q[i] for i in range(4)]
        r_f = [k[i] + p_f[i] for i in range(4)]
        r_s = [p_s[i] - k[i] for i in range(4)]
        check_route([
            [r_f[i] + q[i] - r_f_y[i] for i in range(4)],
            [p_f[i] + k[i] - r_f[i] for i in range(4)],
            [p_s[i] - r_s[i] - k[i] for i in range(4)],
            [r_f_y[i] + r_s[i] - h_q[i] for i in range(4)],
        ], f"{pid} fermion insertion")
        five += 1

        # External W on scalar line.
        r_s_y = [p_s[i] - k[i] + q[i] for i in range(4)]
        check_route([
            [r_s[i] + q[i] - r_s_y[i] for i in range(4)],
            [p_f[i] + k[i] - r_f[i] for i in range(4)],
            [p_s[i] - r_s[i] - k[i] for i in range(4)],
            [r_f[i] + r_s_y[i] - h_q[i] for i in range(4)],
        ], f"{pid} scalar insertion")
        five += 1

        # External W on the internal W line; W flows B(scalar)->A(fermion).
        k_b = k
        k_a = [k[i] + q[i] for i in range(4)]
        r_f_w = [k[i] + p_f[i] + q[i] for i in range(4)]
        check_route([
            [q[i] + k_b[i] - k_a[i] for i in range(4)],
            [p_f[i] + k_a[i] - r_f_w[i] for i in range(4)],
            [p_s[i] - r_s[i] - k_b[i] for i in range(4)],
            [r_f_w[i] + r_s[i] - h_q[i] for i in range(4)],
        ], f"{pid} three-W insertion")
        five += 1

        # Scalar seagull at the scalar endpoint.
        r_s_sg = [p_s[i] - k[i] + q[i] for i in range(4)]
        check_route([
            [p_s[i] + q[i] - r_s_sg[i] - k[i] for i in range(4)],
            [p_f[i] + k[i] - r_f[i] for i in range(4)],
            [r_f[i] + r_s_sg[i] - h_q[i] for i in range(4)],
        ], f"{pid} scalar seagull")
        five += 1

    return base, five


def verify_fermion_wti():
    r = list(sp.symbols("r_0:4"))
    rq = [r[i] + q[i] for i in range(4)]
    sf = lambda p: slash(p) / dot(p, p)
    residual = sf(rq) * slash(q) * PL * sf(r) - (
        PL * sf(r) - sf(rq) * PR
    )
    check_matrix_zero(residual, "massless chiral fermion WTI")
    return 16


def verify_scalar_wti():
    r = list(sp.symbols("s_0:4"))
    rq = [r[i] + q[i] for i in range(4)]
    residual = sp.factor(
        dot(q, [2*r[i] + q[i] for i in range(4)])
        - (dot(rq, rq) - dot(r, r))
    )
    assert residual == 0
    return 1


def verify_scalar_seagull():
    checks = 0
    for a, b in product(range(3), repeat=2):
        anti = SIGMA[a] * SIGMA[b] / 4 + SIGMA[b] * SIGMA[a] / 4
        expected = (sp.Rational(1, 2) if a == b else 0) * sp.eye(2)
        assert anti == expected
        checks += 1
    return checks


def metric(mu, nu):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def transverse_kernel(mu, nu, p):
    return sp.expand(
        dot(p, p) * metric(mu, nu)
        - ETA[mu] * p[mu] * ETA[nu] * p[nu]
    )


def three_w_vertex(alpha, mu, nu, qv, kv):
    return (
        metric(alpha, mu) * ETA[nu] * (qv[nu] - kv[nu])
        + metric(mu, nu) * ETA[alpha] * (2*kv[alpha] + qv[alpha])
        + metric(nu, alpha) * ETA[mu] * (-kv[mu] - 2*qv[mu])
    )


def verify_three_w_and_feynman_gauge_chain():
    kv = list(sp.symbols("w_0:4"))
    kq = [kv[i] + q[i] for i in range(4)]
    # q^alpha Gamma_{alpha mu nu}=K_mu nu(k+q)-K_mu nu(k).
    for mu, nu in product(range(4), repeat=2):
        lhs = sp.expand(sum(
            q[alpha] * three_w_vertex(alpha, mu, nu, q, kv)
            for alpha in range(4)
        ))
        rhs = transverse_kernel(mu, nu, kq) - transverse_kernel(mu, nu, kv)
        assert sp.simplify(lhs - rhs) == 0

    # In Feynman gauge, D=g/k^2. The contracted propagator chain is
    # D(k)-D(k+q)+R_FG, not merely the difference of Feynman propagators.
    G = METRIC
    cov_k = sp.Matrix([ETA[i] * kv[i] for i in range(4)])
    cov_kq = sp.Matrix([ETA[i] * kq[i] for i in range(4)])
    K_k = dot(kv, kv) * G - cov_k * cov_k.T
    K_kq = dot(kq, kq) * G - cov_kq * cov_kq.T
    D_k = G / dot(kv, kv)
    D_kq = G / dot(kq, kq)
    lhs_chain = sp.simplify(D_kq * (K_kq - K_k) * D_k)
    remainder = (
        sp.Matrix(kv) * sp.Matrix(kv).T
        - sp.Matrix(kq) * sp.Matrix(kq).T
    ) / (dot(kv, kv) * dot(kq, kq))
    rhs_chain = D_k - D_kq + remainder
    check_matrix_zero(lhs_chain - rhs_chain, "Feynman-gauge W propagator chain")
    return 16, 16


def verify_fivepoint_reference_kinematics():
    # Proposed nonexceptional Euclidean point in units of mu_IR:
    # p1=e1, p2=e2, p3=e3, q=e4, p4=-(e1+e2+e3+e4).
    euclid_dot = lambda a, b: sum(a[i]*b[i] for i in range(4))
    e1 = [1, 0, 0, 0]
    e2 = [0, 1, 0, 0]
    e3 = [0, 0, 1, 0]
    e4 = [0, 0, 0, 1]
    p4e = [-1, -1, -1, -1]
    vectors = (e1, e2, e3, p4e, e4)
    assert [euclid_dot(v, v) for v in vectors] == [1, 1, 1, 4, 1]
    assert all(any(component != 0 for component in v) for v in vectors)
    assert all(
        any(vectors[i][mu] + vectors[j][mu] != 0 for mu in range(4))
        for i, j in product(range(5), repeat=2) if i < j
    )
    assert [euclid_dot(e1, e2), euclid_dot(e1, e3),
            euclid_dot(e1, e4), euclid_dot(e2, e3)] == [0, 0, 0, 0]
    assert [e1[i] + e2[i] + e3[i] + p4e[i] + e4[i]
            for i in range(4)] == [0, 0, 0, 0]
    return (1, 1, 1, 4, 1)


def main():
    cross_base, cross_five = verify_cross_routes()
    same_base, same_five = verify_same_vertex_routes()
    assert cross_base + same_base == 6
    assert cross_five + same_five == 24
    assert verify_fermion_wti() == 16
    assert verify_scalar_wti() == 1
    assert verify_scalar_seagull() == 9
    w_checks, d_checks = verify_three_w_and_feynman_gauge_chain()
    assert w_checks == d_checks == 16
    verify_fivepoint_reference_kinematics()

    counts = {
        "01": 3, "02": 4, "03": 4,
        "04": 4, "05": 4, "06": 5,
    }
    assert sum(counts.values()) == 24

    print("RC-001-WW-UV-FF-02 Stage B1/B2 routing and longitudinal numerator audit")
    print("PASS: six four-point seed routings satisfy vertex momentum conservation (6/6).")
    print("PASS: five-point attachment routings satisfy vertex momentum conservation (24/24).")
    print("PASS: massless chiral fermion line contraction (16/16 Dirac components).")
    print("PASS: complex-scalar line contraction (1/1 identity).")
    print("PASS: scalar two-gauge seagull anticommutator {t^a,t^b}=delta^ab I/2 (9/9).")
    print("PASS: bare three-W contraction to transverse inverse-kernel difference (16/16 Lorentz components).")
    print("PASS: Feynman-gauge contracted W propagator chain including R_FG (16/16 components).")
    print("ATTACHMENTS: 12 matter-line + 6 scalar seagull + 6 three-W = 24 five-point graphs.")
    print("PER-PAIR COUNTS: " + ", ".join(f"LD-W-{key}: {value}" for key, value in counts.items()))
    print("PROPOSED 5-POINT EUCLIDEAN POINT: p_i^2/mu_IR^2=(1,1,1,4), q^2/mu_IR^2=1.")
    print("RESULT: B1 routing and B2 line-level longitudinal numerator identities pass.")
    print("BOUNDARY: no five-point loop integration, complete weak/phase sum, ghost/ST completion, external-leg/CT sum, transverse form factor, or Wilson coefficient.")
    print("NOTE: Goldstone terms are absent in this unbroken, massless SU(2)_L sub-block; restore them in a broken-phase calculation.")


if __name__ == "__main__":
    main()
