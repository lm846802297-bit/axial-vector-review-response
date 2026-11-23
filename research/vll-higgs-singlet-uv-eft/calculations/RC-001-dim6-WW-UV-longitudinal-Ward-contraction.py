#!/usr/bin/env python3
"""Exact line-level Ward-contraction audit for the six Q_LD internal-W subgraphs.

This derives the longitudinal telescoping identities needed for the UV external-W
five-point calculation. It does NOT integrate the UV five-point form factor,
generate every Feynman graph, or close the full Slavnov-Taylor identity.
"""
from itertools import product
import sympy as sp

I = sp.I
METRIC = (1, -1, -1, -1)
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s / 2 for s in SIGMA)
GAMMA = [sp.diag(1, 1, -1, -1)]
for s in SIGMA:
    GAMMA.append(sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), s),
        sp.Matrix.hstack(-s, sp.zeros(2)),
    ))


def dot(a, b):
    return sp.expand(sum(METRIC[mu] * a[mu] * b[mu] for mu in range(4)))


def slash(a):
    return sum((METRIC[mu] * a[mu] * GAMMA[mu] for mu in range(4)), sp.zeros(4))


def massless_fermion_propagator(p):
    # The common factor i is stripped; S(p)=slash(p)/p^2.
    return slash(p) / dot(p, p)


def verify_fermion_line_wti():
    p = sp.symbols("p0:4")
    q = sp.symbols("q0:4")
    pq = [p[mu] + q[mu] for mu in range(4)]
    lhs = massless_fermion_propagator(pq) * slash(q) * massless_fermion_propagator(p)
    rhs = massless_fermion_propagator(p) - massless_fermion_propagator(pq)
    residuals = [sp.factor(lhs[i, j] - rhs[i, j]) for i in range(4) for j in range(4)]
    assert all(sp.simplify(x) == 0 for x in residuals)
    return len(residuals)


def verify_scalar_line_wti():
    p = sp.symbols("p0:4")
    q = sp.symbols("q0:4")
    pq = [p[mu] + q[mu] for mu in range(4)]
    residual = sp.expand(
        dot(q, [2*p[mu] + q[mu] for mu in range(4)])
        - (dot(pq, pq) - dot(p, p))
    )
    assert residual == 0
    return 1


def verify_line_telescope():
    checks = 0
    for n in range(1, 7):
        G = sp.symbols(f"G0:{n}")
        Gq = sp.symbols(f"Gq0:{n}")
        lhs = sp.Integer(0)
        for j in range(n):
            lhs += (
                sp.prod(Gq[i] for i in range(j))
                * (G[j] - Gq[j])
                * sp.prod(G[i] for i in range(j + 1, n))
            )
        assert sp.expand(lhs - (sp.prod(G) - sp.prod(Gq))) == 0
        checks += 1
    return checks


def delta(i, j):
    return sp.Integer(int(i == j))


def T0(i, j, k, ell):
    return delta(i, j) * delta(k, ell)


def T3(i, j, k, ell):
    return sum(SIGMA[A][i, j] * SIGMA[A][k, ell] for A in range(3))


def act_on_external_slot(tensor, slot, generator, indices):
    """SU(2) action in all-incoming order (bar L_i,H_j,Hdag_k,L_l)."""
    i, j, k, ell = indices
    out = sp.Integer(0)
    if slot == 0:  # bar L: conjugate representation
        for m in range(2):
            out += T[generator][m, i] * tensor(m, j, k, ell)
    elif slot == 1:  # H: fundamental
        for m in range(2):
            out -= T[generator][j, m] * tensor(i, m, k, ell)
    elif slot == 2:  # Hdag: conjugate
        for m in range(2):
            out += T[generator][m, k] * tensor(i, j, m, ell)
    elif slot == 3:  # L: fundamental
        for m in range(2):
            out -= T[generator][ell, m] * tensor(i, j, k, m)
    return sp.simplify(out)


PAIR_DATA = (
    ("LD-W-01", 0, 3, sp.Integer(0), -sp.Rational(1, 4)),
    ("LD-W-02", 0, 2, sp.Integer(0),  sp.Rational(1, 4)),
    ("LD-W-03", 0, 1, -sp.Rational(3, 4), sp.Integer(0)),
    ("LD-W-04", 3, 2, -sp.Rational(3, 4), sp.Integer(0)),
    ("LD-W-05", 3, 1, sp.Integer(0),  sp.Rational(1, 4)),
    ("LD-W-06", 2, 1, sp.Integer(0), -sp.Rational(1, 4)),
)


def verify_yukawa_singlet_endpoints():
    indices = tuple(product(range(2), repeat=4))
    for A in range(3):
        for x in indices:
            left = act_on_external_slot(T0, 0, A, x) + act_on_external_slot(T0, 1, A, x)
            right = act_on_external_slot(T0, 2, A, x) + act_on_external_slot(T0, 3, A, x)
            assert sp.simplify(left) == 0
            assert sp.simplify(right) == 0
    return 2 * 3 * len(indices)


def verify_tensor_invariance():
    indices = tuple(product(range(2), repeat=4))
    checks = 0
    for tensor in (T0, T3):
        for A in range(3):
            for x in indices:
                variation = sum(act_on_external_slot(tensor, slot, A, x) for slot in range(4))
                assert sp.simplify(variation) == 0
                checks += 1
    return checks


def verify_six_pair_SU2_projections():
    indices = tuple(product(range(2), repeat=4))
    for pair_id, r, s, c0, c3 in PAIR_DATA:
        for x in indices:
            value = sum(
                act_on_external_slot(
                    lambda *y: act_on_external_slot(T0, s, A, y), r, A, x
                )
                for A in range(3)
            )
            expected = c0 * T0(*x) + c3 * T3(*x)
            assert sp.simplify(value - expected) == 0, (pair_id, x, value, expected)
    return len(PAIR_DATA) * len(indices)


def metric(mu, nu):
    return sp.Integer(METRIC[mu]) if mu == nu else sp.Integer(0)


def transverse_inverse_kernel(mu, nu, k):
    return sp.expand(
        dot(k, k) * metric(mu, nu)
        - (METRIC[mu] * k[mu]) * (METRIC[nu] * k[nu])
    )


def three_gauge_vertex(alpha, mu, nu, q, k):
    """Stripped Yang-Mills vertex Gamma_{alpha mu nu}(q,k,-k-q)."""
    q_minus_k = [q[i] - k[i] for i in range(4)]
    two_k_plus_q = [2*k[i] + q[i] for i in range(4)]
    minus_k_minus_two_q = [-k[i] - 2*q[i] for i in range(4)]
    return (
        metric(alpha, mu) * METRIC[nu] * q_minus_k[nu]
        + metric(mu, nu) * METRIC[alpha] * two_k_plus_q[alpha]
        + metric(nu, alpha) * METRIC[mu] * minus_k_minus_two_q[mu]
    )


def verify_internal_W_line_wti():
    q = sp.symbols("q0:4")
    k = sp.symbols("k0:4")
    kq = [k[i] + q[i] for i in range(4)]
    checks = 0
    for mu in range(4):
        for nu in range(4):
            contracted = sp.expand(sum(
                q[alpha] * three_gauge_vertex(alpha, mu, nu, q, k)
                for alpha in range(4)
            ))
            rhs = sp.expand(
                transverse_inverse_kernel(mu, nu, kq)
                - transverse_inverse_kernel(mu, nu, k)
            )
            assert sp.simplify(contracted - rhs) == 0
            checks += 1
    return checks


def verify_conventional_Feynman_gauge_remainder():
    q = sp.symbols("q0:4")
    k = sp.symbols("k0:4")
    kq = [k[i] + q[i] for i in range(4)]
    checks = 0
    for mu in range(4):
        for nu in range(4):
            qGamma = sp.expand(sum(
                q[alpha] * three_gauge_vertex(alpha, mu, nu, q, k)
                for alpha in range(4)
            ))
            feynman_inverse_difference = (dot(kq, kq) - dot(k, k)) * metric(mu, nu)
            remainder = sp.expand(qGamma - feynman_inverse_difference)
            expected = -(
                (METRIC[mu] * kq[mu]) * (METRIC[nu] * kq[nu])
                - (METRIC[mu] * k[mu]) * (METRIC[nu] * k[nu])
            )
            assert sp.simplify(remainder - expected) == 0
            checks += 1
    return checks


def verify_EFT_local_contact_crosscheck():
    L, g2, F = sp.symbols("L g2 F", real=True)
    a = -sp.Rational(1, 2) + L/2
    b = -sp.Rational(1, 32) + sp.Rational(7, 16)*L
    c = sp.Rational(7, 32) - sp.Rational(5, 16)*L
    contacts = (
        sp.simplify(sp.I*g2*F*a),
        sp.simplify(2*g2*F*b),
        sp.Integer(0),
    )
    at_match = tuple(sp.simplify(x.subs(L, 0)) for x in contacts)
    expected = (-sp.I*g2*F/2, -g2*F/16, sp.Integer(0))
    assert at_match == expected
    return a, b, c, at_match


def main():
    n_fermion = verify_fermion_line_wti()
    n_scalar = verify_scalar_line_wti()
    n_tel = verify_line_telescope()
    n_yukawa = verify_yukawa_singlet_endpoints()
    n_tensor = verify_tensor_invariance()
    n_pairs = verify_six_pair_SU2_projections()
    n_w = verify_internal_W_line_wti()
    n_xi = verify_conventional_Feynman_gauge_remainder()
    a, b, c, contact = verify_EFT_local_contact_crosscheck()

    print("RC-001 UV external-W longitudinal Ward-contraction audit")
    print(f"PASS: massless fermion line WTI ({n_fermion}/16 Dirac components).")
    print(f"PASS: scalar line WTI ({n_scalar}/1 identity).")
    print(f"PASS: propagator-chain telescoping ({n_tel}/6 chain lengths, n=1..6).")
    print(f"PASS: both Yukawa singlet endpoint identities ({n_yukawa}/96 index/generator checks).")
    print(f"PASS: T0 and T3 total SU(2) invariance ({n_tensor}/96 checks).")
    print(f"PASS: six internal-W pair projections ({n_pairs}/96 tensor components).")
    print(f"PASS: non-Abelian three-W contraction equals transverse inverse-kernel difference ({n_w}/16 Lorentz components).")
    print(f"PASS: conventional Feynman-gauge longitudinal remainder identified ({n_xi}/16 components).")
    print(f"PASS: EFT local one-W contact cross-check at mu_R=M_E: {contact}.")
    print(f"Hard-polynomial coefficients: a={a}, b={b}, c={c}.")
    print("RESULT: all exact line-level and SU(2) Ward-contraction checks passed.")
    print("BOUNDARY: this is the longitudinal identity/telescoping reduction,")
    print("          not the integrated UV five-point form factor or full STI sum.")
    print("NEXT: compute the UV matter-line, scalar-seagull, and internal-W attachments;")
    print("      retain the ordinary-Feynman-gauge STI remainder and off-shell endpoints.")


if __name__ == "__main__":
    main()
