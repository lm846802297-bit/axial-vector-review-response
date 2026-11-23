#!/usr/bin/env python3
"""RC-001-WW-UV-FF-02: graph-specific five-point numerator/phase audit.

Checks the two oriented fermion-line Ward contractions, the two oriented
scalar-line contractions, the scalar seagull algebra, the bare three-W
contraction, its Feynman-gauge propagator-chain remainder, the conjugate
same-vertex numerator relation, and the relative Feynman-rule phases.

This is not a loop integration or a complete summed Slavnov-Taylor identity.
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
GAMMA_DOWN = [ETA[mu] * GAMMA[mu] for mu in range(4)]
METRIC = sp.diag(*ETA)


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def slash(a):
    return sum((ETA[i] * a[i] * GAMMA[i] for i in range(4)), sp.zeros(4))


def matrix_zero(m):
    return all(sp.simplify(m[i, j]) == 0
               for i in range(m.rows) for j in range(m.cols))


def metric(mu, nu):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def K(mu, nu, p):
    return sp.expand(
        dot(p, p) * metric(mu, nu)
        - ETA[mu] * p[mu] * ETA[nu] * p[nu]
    )


def gamma3(alpha, mu, nu, q, k):
    """Gamma_{alpha mu nu}(q,k,-k-q), with all momenta incoming."""
    return (
        metric(alpha, mu) * ETA[nu] * (q[nu] - k[nu])
        + metric(mu, nu) * ETA[alpha] * (2*k[alpha] + q[alpha])
        + metric(nu, alpha) * ETA[mu] * (-k[mu] - 2*q[mu])
    )


def verify_A_fermion_wti():
    # A-side arrow/momentum orientation inherited from the cross-box seed:
    # r_A^W = r_A^Y + q; the physical propagator momenta are -r_A.
    q = list(sp.symbols("qA0:4", real=True))
    r_w = list(sp.symbols("rAW0:4", real=True))
    r_y = [r_w[i] - q[i] for i in range(4)]
    S_w = -slash(r_w) / dot(r_w, r_w)
    S_y = -slash(r_y) / dot(r_y, r_y)
    lhs = S_w * slash(q) * PL * S_y
    rhs = S_w * PR - PL * S_y
    assert matrix_zero(lhs - rhs), "A-oriented fermion WTI"
    return 16


def verify_B_fermion_wti():
    # B-side orientation: r_B^Y = r_B^W + q.
    q = list(sp.symbols("qB0:4", real=True))
    r_w = list(sp.symbols("rBW0:4", real=True))
    r_y = [r_w[i] + q[i] for i in range(4)]
    S_w = slash(r_w) / dot(r_w, r_w)
    S_y = slash(r_y) / dot(r_y, r_y)
    lhs = S_y * slash(q) * PL * S_w
    rhs = PL * S_w - S_y * PR
    assert matrix_zero(lhs - rhs), "B-oriented fermion WTI"
    return 16


def verify_scalar_wtis():
    q = list(sp.symbols("qS0:4", real=True))
    r_w_a = list(sp.symbols("rSAW0:4", real=True))
    r_y_a = [r_w_a[i] - q[i] for i in range(4)]
    # A side: q.(rW+rY) = rW^2-rY^2.
    lhs_a = dot(q, [r_w_a[i] + r_y_a[i] for i in range(4)]) / (
        dot(r_w_a, r_w_a) * dot(r_y_a, r_y_a)
    )
    rhs_a = 1/dot(r_y_a, r_y_a) - 1/dot(r_w_a, r_w_a)
    assert sp.simplify(lhs_a-rhs_a) == 0

    r_w_b = list(sp.symbols("rSBW0:4", real=True))
    r_y_b = [r_w_b[i] + q[i] for i in range(4)]
    # B side has the opposite endpoint order.
    lhs_b = dot(q, [r_w_b[i] + r_y_b[i] for i in range(4)]) / (
        dot(r_w_b, r_w_b) * dot(r_y_b, r_y_b)
    )
    rhs_b = 1/dot(r_w_b, r_w_b) - 1/dot(r_y_b, r_y_b)
    assert sp.simplify(lhs_b-rhs_b) == 0
    return 2


def verify_scalar_seagull():
    checks = 0
    for a, b in product(range(3), repeat=2):
        anti = SIGMA[a]*SIGMA[b]/4 + SIGMA[b]*SIGMA[a]/4
        expected = (sp.Rational(1, 2) if a == b else 0) * sp.eye(2)
        assert anti == expected
        checks += 1
    return checks


def verify_three_w_and_fg_chain():
    q = list(sp.symbols("qW0:4", real=True))
    k = list(sp.symbols("kW0:4", real=True))
    kq = [k[i] + q[i] for i in range(4)]
    checks = 0
    for mu, nu in product(range(4), repeat=2):
        lhs = sp.expand(sum(
            q[alpha] * gamma3(alpha, mu, nu, q, k)
            for alpha in range(4)
        ))
        rhs = K(mu, nu, kq) - K(mu, nu, k)
        assert sp.simplify(lhs-rhs) == 0
        checks += 1

    G = METRIC
    cov_k = sp.Matrix([ETA[i]*k[i] for i in range(4)])
    cov_kq = sp.Matrix([ETA[i]*kq[i] for i in range(4)])
    K_k = dot(k, k)*G - cov_k*cov_k.T
    K_kq = dot(kq, kq)*G - cov_kq*cov_kq.T
    D_k = G/dot(k, k)
    D_kq = G/dot(kq, kq)
    lhs_chain = sp.simplify(D_kq*(K_kq-K_k)*D_k)
    remainder = (
        sp.Matrix(k)*sp.Matrix(k).T
        - sp.Matrix(kq)*sp.Matrix(kq).T
    )/(dot(k, k)*dot(kq, kq))
    rhs_chain = D_k-D_kq+remainder
    assert matrix_zero(lhs_chain-rhs_chain)
    return checks, 16


def verify_same_vertex_conjugation():
    # Dirac-Hermitian conjugation of the left Yukawa-vertex numerator
    # gamma_mu slash(r) V^mu gives V_mu slash(r) gamma^mu.
    r = list(sp.symbols("rHC0:4", real=True))
    V = list(sp.symbols("VHC0:4", real=True))
    N03 = sum((
        GAMMA_DOWN[mu]*slash(r)*V[mu] for mu in range(4)
    ), sp.zeros(4))
    N04 = sum((
        ETA[mu]*V[mu]*slash(r)*GAMMA[mu] for mu in range(4)
    ), sp.zeros(4))
    bar = GAMMA[0]*N03.conjugate().T*GAMMA[0]
    assert matrix_zero(bar-N04)
    return 16


def verify_phase_bookkeeping():
    # D_mu = partial_mu - i g2 t^a W^a_mu:
    # Yukawa vertices -iy,-iy*, fermion/scalar W vertices +ig2,
    # matter propagators i, W propagator -i, and V_3W=+g2 f Gamma.
    base = (-I)**2 * (I**3) * (-I) * (I**2)
    line_relative = I*I
    seagull_relative = (I)/(I)
    three_w_relative = ((-I)**2)/( -I )
    assert sp.simplify(base) == -1
    assert sp.simplify(line_relative) == -1
    assert sp.simplify(seagull_relative) == 1
    assert sp.simplify(three_w_relative) == -I
    return base, line_relative, seagull_relative, three_w_relative


def main():
    a_fermion = verify_A_fermion_wti()
    b_fermion = verify_B_fermion_wti()
    scalar = verify_scalar_wtis()
    seagull = verify_scalar_seagull()
    three_w, fg = verify_three_w_and_fg_chain()
    hc = verify_same_vertex_conjugation()
    phases = verify_phase_bookkeeping()

    graph_counts = {
        "LD-W-01": 3, "LD-W-02": 4, "LD-W-03": 4,
        "LD-W-04": 4, "LD-W-05": 4, "LD-W-06": 5,
    }
    assert sum(graph_counts.values()) == 24

    print("RC-001-WW-UV-FF-02 Stage B2c numerator and phase audit")
    print(f"PASS: A-oriented fermion insertion WTI ({a_fermion}/16 Dirac components).")
    print(f"PASS: B-oriented fermion insertion WTI ({b_fermion}/16 Dirac components).")
    print(f"PASS: oppositely oriented scalar-line WTI ({scalar}/2 identities).")
    print(f"PASS: scalar seagull anticommutator ({seagull}/9 generator pairs).")
    print(f"PASS: bare three-W contraction ({three_w}/16 Lorentz components).")
    print(f"PASS: Feynman-gauge W chain including R_FG ({fg}/16 components).")
    print(f"PASS: LD-W-03/04 Dirac-Hermitian conjugate numerator relation ({hc}/16 components).")
    print(f"PASS: Feynman-rule phase ratios: base={phases[0]}, line={phases[1]}, seagull={phases[2]}, three-W={phases[3]}.")
    print("DIRECT FIVE-POINT GRAPH CENSUS:")
    for key, value in graph_counts.items():
        print(f"  {key}: {value}")
    print("  total: 24 = 12 matter-line + 6 scalar seagull + 6 three-W")
    print("RESULT: oriented line numerators and relative phase building blocks pass.")
    print("BOUNDARY: no complete 24-graph weak/Lorentz sum, no ghost/ST completion,")
    print("          no external-leg/counterterm sum, no loop integration, no Wilson coefficient.")


if __name__ == "__main__":
    main()
