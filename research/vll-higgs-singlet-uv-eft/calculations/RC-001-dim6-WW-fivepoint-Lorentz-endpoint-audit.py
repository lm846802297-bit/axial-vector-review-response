#!/usr/bin/env python3
"""RC-001 B2c-IVc: exact Lorentz endpoint audit.

This script checks stripped Lorentz identities before loop integration.
It does not identify the scalar-line weak tensor with the seagull tensor;
those are audited separately in the explicit raw-index bridge. It does not
perform the full weak-index/phase-weighted 24-graph sum or claim a complete
Slavnov-Taylor identity.

Index convention in the three-W chain:
  D^{mu nu}(k) = g^{mu nu}/k^2,
  K_{mu nu}(k) = k^2 g_{mu nu} - k_mu k_nu,
  R_FG^{mu nu} = [k^mu k^nu-(k+q)^mu(k+q)^nu]/[k^2(k+q)^2].
Thus the propagator chain is D^{mu alpha}(k+q) K_{alpha beta} D^{beta nu}(k).
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


def K_down(mu, nu, p):
    """K_{mu nu}=p^2 g_{mu nu}-p_mu p_nu."""
    return sp.expand(
        dot(p, p) * metric(mu, nu)
        - ETA[mu] * p[mu] * ETA[nu] * p[nu]
    )


def gamma3(alpha, mu, nu, q, k):
    """Gamma_{alpha mu nu}(q,k,-k-q), all momenta incoming."""
    return (
        metric(alpha, mu) * ETA[nu] * (q[nu] - k[nu])
        + metric(mu, nu) * ETA[alpha] * (2*k[alpha] + q[alpha])
        + metric(nu, alpha) * ETA[mu] * (-k[mu] - 2*q[mu])
    )


def verify_fermion_endpoints():
    q = list(sp.symbols("qF0:4", real=True))
    r = list(sp.symbols("rF0:4", real=True))
    r_w = r
    r_y_a = [r[i] - q[i] for i in range(4)]
    r_y_b = [r[i] + q[i] for i in range(4)]

    # A orientation: (-slash rW) slash q (-slash rY) over both denominators.
    lhs_a = slash(r_w) * slash(q) * slash(r_y_a) / (
        dot(r_w, r_w) * dot(r_y_a, r_y_a)
    )
    rhs_a = slash(r_y_a) / dot(r_y_a, r_y_a) - slash(r_w) / dot(r_w, r_w)
    assert matrix_zero(lhs_a - rhs_a), "A fermion endpoint"

    # B orientation: slash rY slash q slash rW over both denominators.
    lhs_b = slash(r_y_b) * slash(q) * slash(r_w) / (
        dot(r_y_b, r_y_b) * dot(r_w, r_w)
    )
    rhs_b = slash(r_w) / dot(r_w, r_w) - slash(r_y_b) / dot(r_y_b, r_y_b)
    assert matrix_zero(lhs_b - rhs_b), "B fermion endpoint"
    return 16, 16


def verify_scalar_endpoints():
    q = list(sp.symbols("qS0:4", real=True))
    r = list(sp.symbols("rS0:4", real=True))
    r_w = r
    r_y_a = [r[i] - q[i] for i in range(4)]
    r_y_b = [r[i] + q[i] for i in range(4)]

    lhs_a = dot(q, [r_w[i] + r_y_a[i] for i in range(4)]) / (
        dot(r_w, r_w) * dot(r_y_a, r_y_a)
    )
    rhs_a = 1/dot(r_y_a, r_y_a) - 1/dot(r_w, r_w)
    assert sp.simplify(lhs_a - rhs_a) == 0

    lhs_b = dot(q, [r_w[i] + r_y_b[i] for i in range(4)]) / (
        dot(r_w, r_w) * dot(r_y_b, r_y_b)
    )
    rhs_b = 1/dot(r_w, r_w) - 1/dot(r_y_b, r_y_b)
    assert sp.simplify(lhs_b - rhs_b) == 0
    return 2


def verify_seagull_metric_contraction():
    # The scalar seagull carries g^{alpha mu}; contracting the external
    # momentum q_alpha gives q^mu. Its weak tensor is audited separately
    # in the explicit raw-index bridge, not factored as the scalar-line tensor.
    q = list(sp.symbols("qSG0:4", real=True))
    q_lower = [ETA[i] * q[i] for i in range(4)]
    checks = 0
    for mu in range(4):
        contracted = sp.expand(sum(
            q_lower[alpha] * metric(alpha, mu)
            for alpha in range(4)
        ))
        assert sp.simplify(contracted - q[mu]) == 0
        checks += 1
    return checks


def verify_three_w_and_feynman_gauge_chain():
    q = list(sp.symbols("qW0:4", real=True))
    k = list(sp.symbols("kW0:4", real=True))
    kq = [k[i] + q[i] for i in range(4)]

    # q^alpha Gamma_{alpha mu nu}=K_{mu nu}(k+q)-K_{mu nu}(k).
    checks = 0
    for mu, nu in product(range(4), repeat=2):
        lhs = sp.expand(sum(
            q[alpha] * gamma3(alpha, mu, nu, q, k)
            for alpha in range(4)
        ))
        rhs = K_down(mu, nu, kq) - K_down(mu, nu, k)
        assert sp.simplify(lhs-rhs) == 0
        checks += 1

    # D^{mu alpha} K_{alpha beta} D^{beta nu}:
    # D is upper-upper, K is lower-lower, and R_FG is upper-upper.
    cov_k = sp.Matrix([ETA[i] * k[i] for i in range(4)])
    cov_kq = sp.Matrix([ETA[i] * kq[i] for i in range(4)])
    K_k = dot(k, k)*METRIC - cov_k*cov_k.T
    K_kq = dot(kq, kq)*METRIC - cov_kq*cov_kq.T
    D_k = METRIC/dot(k, k)
    D_kq = METRIC/dot(kq, kq)
    lhs_chain = sp.simplify(D_kq*(K_kq-K_k)*D_k)
    remainder = (
        sp.Matrix(k)*sp.Matrix(k).T
        - sp.Matrix(kq)*sp.Matrix(kq).T
    )/(dot(k, k)*dot(kq, kq))
    rhs_chain = D_k-D_kq+remainder
    assert matrix_zero(lhs_chain-rhs_chain)
    return checks, 16


def verify_nonzero_remainder_diagnostic():
    # One generic nonsingular point demonstrates that R_FG is not identically zero.
    k = [sp.Integer(3), sp.Integer(2), sp.Integer(0), sp.Integer(0)]
    q = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    kq = [k[i]+q[i] for i in range(4)]
    rem = (
        sp.Matrix(k)*sp.Matrix(k).T
        - sp.Matrix(kq)*sp.Matrix(kq).T
    )/(dot(k, k)*dot(kq, kq))
    assert any(rem[i, j] != 0 for i in range(4) for j in range(4))
    return rem


def pair_census():
    # (A type, B type, scalar seagulls, three-W insertions).
    pairs = {
        "LD-W-01": ("F", "F", 0, 1),
        "LD-W-02": ("F", "S", 1, 1),
        "LD-W-03": ("F", "S", 1, 1),
        "LD-W-04": ("S", "F", 1, 1),
        "LD-W-05": ("S", "F", 1, 1),
        "LD-W-06": ("S", "S", 2, 1),
    }
    matter = sum(2 for _ in pairs)
    seagulls = sum(v[2] for v in pairs.values())
    three_w = sum(v[3] for v in pairs.values())
    assert (matter, seagulls, three_w) == (12, 6, 6)
    return pairs, matter, seagulls, three_w


def main():
    a_f, b_f = verify_fermion_endpoints()
    scalar = verify_scalar_endpoints()
    seagull_lorentz = verify_seagull_metric_contraction()
    three_w, fg = verify_three_w_and_feynman_gauge_chain()
    remainder = verify_nonzero_remainder_diagnostic()
    pairs, matter, seagulls, n3w = pair_census()

    print("RC-001 B2c-IVc Lorentz endpoint audit")
    print(f"PASS: A-side fermion numerator difference ({a_f}/16 Dirac components).")
    print(f"PASS: B-side fermion numerator difference ({b_f}/16 Dirac components).")
    print(f"PASS: A/B scalar propagator differences ({scalar}/2).")
    print(f"PASS: scalar seagull metric contraction q_alpha g^(alpha mu)=q^mu ({seagull_lorentz}/4 Lorentz components).")
    print("NOTE: scalar-line and seagull weak tensors are distinct; see the raw-index bridge.")
    print(f"PASS: three-W contraction ({three_w}/16 Lorentz components).")
    print(f"PASS: Feynman-gauge W-chain decomposition including R_FG ({fg}/16 components).")
    print("PASS: R_FG is generically nonzero (explicit rational diagnostic point).")
    print("PAIR CENSUS:")
    for name, (a_type, b_type, nsg, _) in pairs.items():
        print(f"  {name}: A={a_type}, B={b_type}, scalar seagulls={nsg}, three-W=1")
    print(f"TOTAL: {matter} matter-line insertions + {seagulls} scalar seagulls + {n3w} three-W insertions = 24")
    print("BOUNDARY: exact Lorentz endpoint identities and topology census only.")
    print("No complete weak-index/phase-weighted 24-graph cancellation, ghost/ST closure,")
    print("external-leg/counterterm sum, loop integration, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
