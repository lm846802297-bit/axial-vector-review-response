#!/usr/bin/env python3
"""RC-001 B2c-IVh: common-k longitudinal Lorentz-kernel comparison.

This audit combines the already-fixed B1 endpoint orientations with the
physical three-W inverse-kernel contraction and the raw weak-phase ledger.

It proves the universal transverse-kernel cancellation for arbitrary endpoint
currents in all six pair classes. In ordinary Feynman gauge the explicit
R_FG remainder is retained. This is not the complete 24-graph amplitude,
the ghost/ST completion, or a loop integration.
"""
from itertools import product
import sympy as sp

I = sp.I
ETA = (1, -1, -1, -1)
METRIC = sp.diag(*ETA)
q = list(sp.symbols("q0:4", real=True))
k = list(sp.symbols("k0:4", real=True))
kq = [k[i] + q[i] for i in range(4)]


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def slash(a, gamma):
    return sum((ETA[i] * a[i] * gamma[i] for i in range(4)), sp.zeros(4))


def matrix_zero(matrix):
    return all(sp.simplify(matrix[i, j]) == 0
               for i in range(matrix.rows) for j in range(matrix.cols))


def metric(mu, nu):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


# Explicit four-dimensional Dirac algebra for the oriented matter-line WTIs.
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


def verify_fermion_endpoint(orientation, suffix):
    r_w = list(sp.symbols(f"rW_{suffix}_0:4", real=True))
    if orientation == "A":
        # Cross-vertex A side: r_Y = r_W - q.
        r_y = [r_w[i] - q[i] for i in range(4)]
        S_w = -slash(r_w, GAMMA) / dot(r_w, r_w)
        S_y = -slash(r_y, GAMMA) / dot(r_y, r_y)
        lhs = S_w * slash(q, GAMMA) * PL * S_y
        rhs = S_w * PR - PL * S_y
    else:
        # Cross-vertex B side and both same-vertex sides: r_Y = r_W + q.
        r_y = [r_w[i] + q[i] for i in range(4)]
        S_w = slash(r_w, GAMMA) / dot(r_w, r_w)
        S_y = slash(r_y, GAMMA) / dot(r_y, r_y)
        lhs = S_y * slash(q, GAMMA) * PL * S_w
        rhs = PL * S_w - S_y * PR
    assert matrix_zero(lhs - rhs)
    return 16


def verify_scalar_endpoint(orientation, suffix):
    r_w = list(sp.symbols(f"sW_{suffix}_0:4", real=True))
    if orientation == "A":
        r_y = [r_w[i] - q[i] for i in range(4)]
        lhs = dot(q, [r_w[i] + r_y[i] for i in range(4)]) / (
            dot(r_w, r_w) * dot(r_y, r_y)
        )
        rhs = 1/dot(r_y, r_y) - 1/dot(r_w, r_w)
    else:
        r_y = [r_w[i] + q[i] for i in range(4)]
        lhs = dot(q, [r_w[i] + r_y[i] for i in range(4)]) / (
            dot(r_w, r_w) * dot(r_y, r_y)
        )
        rhs = 1/dot(r_w, r_w) - 1/dot(r_y, r_y)
    assert sp.simplify(lhs - rhs) == 0
    return 1


def K_down(p):
    p_cov = sp.Matrix([ETA[i] * p[i] for i in range(4)])
    return sp.expand(dot(p, p) * METRIC - p_cov * p_cov.T)


def D_up(p):
    return METRIC / dot(p, p)


def gamma3(alpha, mu, nu):
    """Gamma_{alpha mu nu}(q,k,-k-q), all momenta incoming."""
    return (
        metric(alpha, mu) * ETA[nu] * (q[nu] - k[nu])
        + metric(mu, nu) * ETA[alpha] * (2*k[alpha] + q[alpha])
        + metric(nu, alpha) * ETA[mu] * (-k[mu] - 2*q[mu])
    )


def verify_three_w_contraction(K0, Kq):
    checks = 0
    for mu, nu in product(range(4), repeat=2):
        lhs = sp.expand(sum(
            q[alpha] * gamma3(alpha, mu, nu)
            for alpha in range(4)
        ))
        assert sp.simplify(lhs - (Kq[mu, nu] - K0[mu, nu])) == 0
        checks += 1
    return checks


def verify_common_kernels():
    K0, Kq = K_down(k), K_down(kq)
    D0, Dq = D_up(k), D_up(kq)
    Rfg = (
        sp.Matrix(k) * sp.Matrix(k).T
        - sp.Matrix(kq) * sp.Matrix(kq).T
    ) / (dot(k, k) * dot(kq, kq))

    # Cross-vertex orientation: W momenta at A,B are k,k+q.
    C_cross = sp.simplify(Dq * (Kq - K0) * D0)
    # Same-vertex orientation: W momenta at S,F are k,k+q; the
    # endpoint order is reversed, so the matrix chain is transposed.
    C_same = sp.simplify(D0 * (Kq - K0) * Dq)

    expected = D0 - Dq + Rfg
    assert matrix_zero(C_cross - expected)
    assert matrix_zero(C_same - expected)
    assert matrix_zero(C_cross - C_same)
    return D0, Dq, Rfg, C_cross, C_same, verify_three_w_contraction(K0, Kq)


PAIR_DATA = (
    # id, left endpoint, right endpoint, internal-W orientation
    ("LD-W-01", "F", "F", "A->B"),
    ("LD-W-02", "F", "S", "A->B"),
    ("LD-W-03", "F", "S", "S->F"),
    ("LD-W-04", "S", "F", "S->F"),
    ("LD-W-05", "S", "F", "A->B"),
    ("LD-W-06", "S", "S", "A->B"),
)


def verify_six_pair_current_kernels(D0, Dq, Rfg, C_cross, C_same):
    g2, GAB, GFS = sp.symbols("g_2 G_AB G_FS")
    checks = 0
    for n, (pair_id, left_type, right_type, orientation) in enumerate(PAIR_DATA):
        if orientation == "A->B":
            # The A and B line WTIs have opposite endpoint orientation.
            # After the B1 common-k routing their commutator kernel is D(k+q)-D(k).
            line_kernel = Dq - D0
            line_phase = -I*g2*GAB
            three_w_phase = -I*g2*GAB
            chain = C_cross
            residual_phase = -I*g2*GAB
        else:
            # Both same-vertex matter lines have r_Y=r_W+q, while W flows S->F.
            # The endpoint order is reversed: the line kernel is D(k)-D(k+q).
            line_kernel = D0 - Dq
            line_phase = -I*g2*GFS
            three_w_phase = +I*g2*GFS
            chain = C_same
            residual_phase = +I*g2*GFS

        # Arbitrary Lorentz currents: this is tensorial and also applies when
        # the entries are Dirac matrices or scalar derivative currents.
        J_left = sp.Matrix(sp.symbols(f"Jleft_{n}_0:4", real=True))
        J_right = sp.Matrix(sp.symbols(f"Jright_{n}_0:4", real=True))
        line_term = line_phase * (J_left.T * line_kernel * J_right)[0]
        three_w_term = three_w_phase * (J_left.T * chain * J_right)[0]
        total = sp.expand(line_term + three_w_term)
        expected = sp.expand(
            residual_phase * (J_left.T * Rfg * J_right)[0]
        )
        assert sp.simplify(total - expected) == 0, pair_id
        checks += 16

        print(
            f"PASS: {pair_id} ({left_type}-{right_type}, {orientation}) "
            "phase-weighted transverse-kernel cancellation"
        )
    return checks


def verify_scalar_seagull_decompositions():
    g2, DY, DW, VA, VB, qmu, SA, SB, GAB, GFS = sp.symbols(
        "g_2 Delta_Y Delta_W V_A V_B q_mu S_A S_B G_AB G_FS"
    )

    # Cross-vertex A scalar endpoint: W_A = S_A/2 + i G_AB/2.
    W_A = SA/2 + I*GAB/2
    A_raw = -g2*(DY-DW)*VA*W_A + g2*DY*qmu*SA
    A_split = g2*(
        (-sp.Rational(1, 2)*(DY-DW)*VA + DY*qmu)*SA
        - I*sp.Rational(1, 2)*(DY-DW)*VA*GAB
    )
    assert sp.simplify(A_raw - A_split) == 0

    # Cross-vertex B scalar endpoint: W_B = S_B/2 + i G_AB/2.
    W_B = SB/2 + I*GAB/2
    B_raw = g2*(DY-DW)*VB*W_B + g2*DY*qmu*SB
    B_split = g2*(
        (sp.Rational(1, 2)*(DY-DW)*VB + DY*qmu)*SB
        + I*sp.Rational(1, 2)*(DY-DW)*VB*GAB
    )
    assert sp.simplify(B_raw - B_split) == 0

    # Same-vertex S endpoint: use G_FS, not the cross-vertex G_AB.
    W_S = SB/2 + I*GFS/2
    S_raw = g2*(DY-DW)*VB*W_S + g2*DY*qmu*SB
    S_split = g2*(
        (sp.Rational(1, 2)*(DY-DW)*VB + DY*qmu)*SB
        + I*sp.Rational(1, 2)*(DY-DW)*VB*GFS
    )
    assert sp.simplify(S_raw - S_split) == 0
    return 3


def verify_rfg_nonzero():
    k0 = [sp.Integer(3), sp.Integer(2), sp.Integer(0), sp.Integer(0)]
    q0 = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    kq0 = [k0[i] + q0[i] for i in range(4)]
    k2 = dot(k0, k0)
    kq2 = dot(kq0, kq0)
    R0 = (
        sp.Matrix(k0) * sp.Matrix(k0).T
        - sp.Matrix(kq0) * sp.Matrix(kq0).T
    ) / (k2*kq2)
    assert (k2, kq2, R0[0, 0]) == (
        sp.Integer(5), sp.Integer(11), -sp.Rational(7, 55)
    )
    return k2, kq2, R0


def main():
    # Recheck each pair's actual A/B or S->F endpoint WTI orientation.
    wti_checks = 0
    for n, (pair_id, left_type, right_type, orientation) in enumerate(PAIR_DATA):
        if orientation == "A->B":
            if left_type == "F":
                wti_checks += verify_fermion_endpoint("A", f"{n}_A")
            else:
                wti_checks += verify_scalar_endpoint("A", f"{n}_A")
            if right_type == "F":
                wti_checks += verify_fermion_endpoint("B", f"{n}_B")
            else:
                wti_checks += verify_scalar_endpoint("B", f"{n}_B")
        else:
            if left_type == "F":
                wti_checks += verify_fermion_endpoint("B", f"{n}_F")
            else:
                wti_checks += verify_scalar_endpoint("B", f"{n}_S")
            if right_type == "F":
                wti_checks += verify_fermion_endpoint("B", f"{n}_F2")
            else:
                wti_checks += verify_scalar_endpoint("B", f"{n}_S2")

    D0, Dq, Rfg, C_cross, C_same, three_w_checks = verify_common_kernels()
    pair_checks = verify_six_pair_current_kernels(
        D0, Dq, Rfg, C_cross, C_same
    )
    seagull_checks = verify_scalar_seagull_decompositions()
    k2, kq2, R0 = verify_rfg_nonzero()

    assert wti_checks == 6*16 + 6  # Six fermion matrix WTIs plus six scalar WTIs.
    assert three_w_checks == 16
    assert pair_checks == 96
    assert seagull_checks == 3

    print("RC-001 B2c-IVh common-k longitudinal Lorentz-kernel audit")
    print(f"PASS: oriented matter-line WTI inputs ({wti_checks}=6*16 Dirac + 6 scalar checks).")
    print(f"PASS: three-W contraction to K(k+q)-K(k) ({three_w_checks}/16).")
    print("PASS: both W-propagator orientations give D(k)-D(k+q)+R_FG (32/32).")
    print(f"PASS: six pairwise arbitrary-current contractions ({pair_checks}/96 components).")
    print(f"PASS: scalar-line/seagull weak-tensor decompositions ({seagull_checks}/3).")
    print("GROUP-PHASED RESULT:")
    print("  cross A->B: line + three-W = -i g2 G_AB * J_left.R_FG.J_right")
    print("  same S->F: line + three-W = +i g2 G_FS * J_left.R_FG.J_right")
    print(f"R_FG diagnostic: k^2={k2}, (k+q)^2={kq2}, R_FG^00={R0[0,0]}")
    print("BOUNDARY:")
    print("  The D(k)-D(k+q) transverse-kernel pieces cancel pairwise.")
    print("  R_FG is nonzero and is retained; no ghost/ST cancellation is claimed.")
    print("  Arbitrary endpoint currents are used; explicit pair numerators are not integrated.")
    print("  No external-leg/LSZ, counterterm, full 24-graph, UV-EFT subtraction,")
    print("  transverse form factor, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
