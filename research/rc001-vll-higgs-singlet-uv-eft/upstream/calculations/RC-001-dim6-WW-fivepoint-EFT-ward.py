#!/usr/bin/env python3
"""Exact SU(2) covariance checks for the local EFT one-W vertices.

This checks the gauge-covariant completion of the already matched, fixed
internal-W hard sub-block. It does NOT calculate the UV one-loop five-point
amplitude or close the full Slavnov-Taylor identity.
"""
import itertools
import sympy as sp

I = sp.I
g2, L = sp.symbols("g2 L", real=True)
F = sp.symbols("F", real=True)  # g2^2 |y_l|^2/(16 pi^2 M_E^2)

SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s / 2 for s in SIGMA)
DELTA = sp.eye(2)


def eps(i, j, k):
    return int(sp.LeviCivita(i, j, k))


def cross(a, b):
    return sp.Matrix([
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0],
    ])


def t3(i, j, k, ell):
    return sum((SIGMA[A][i, j] * SIGMA[A][k, ell]
                for A in range(3)), sp.Integer(0))


def verify_adjoint_commutator():
    # [t^J, sigma^I] = -i epsilon^{IJK} sigma^K.
    for J, A in itertools.product(range(3), repeat=2):
        lhs = T[J] * SIGMA[A] - SIGMA[A] * T[J]
        rhs = sp.zeros(2)
        for K in range(3):
            rhs += -I * eps(A, J, K) * SIGMA[K]
        assert lhs == rhs


def verify_local_adjoint_ward_identity():
    # delta X=-g alpha x X, delta Y=-g alpha x Y,
    # delta W=partial(alpha)-g alpha x W,
    # D_adj Y=partial Y+g W x Y.
    alpha = sp.Matrix(sp.symbols("alpha0:3"))
    dalpha = sp.Matrix(sp.symbols("dalpha0:3"))
    gauge = sp.Matrix(sp.symbols("W0:3"))
    Y = sp.Matrix(sp.symbols("Y0:3"))
    dY = sp.Matrix(sp.symbols("dY0:3"))

    delta_dY = -g2 * cross(dalpha, Y) - g2 * cross(alpha, dY)
    delta_gauge_term = g2 * (
        cross(dalpha - g2 * cross(alpha, gauge), Y)
        + cross(gauge, -g2 * cross(alpha, Y))
    )
    delta_covD = sp.simplify(delta_dY + delta_gauge_term)
    expected = -g2 * cross(alpha, dY + g2 * cross(gauge, Y))
    assert all(sp.expand(delta_covD[n] - expected[n]) == 0 for n in range(3))

    X = sp.Matrix(sp.symbols("X0:3"))
    delta_X = -g2 * cross(alpha, X)
    delta_DY = expected
    delta_scalar = sp.expand(delta_X.dot(dY + g2 * cross(gauge, Y))
                              + X.dot(delta_DY))
    assert delta_scalar == 0


def verify_t3_invariance():
    # Infinitesimal SU(2) invariance of T3_(ij,kl) multiplying
    # bar L_i H_j Hdag_k L_l.
    for J in range(3):
        for a, b, c, d in itertools.product(range(2), repeat=4):
            variation = (
                -sum((T[J][a, i] * t3(i, b, c, d)
                      for i in range(2)), sp.Integer(0))
                +sum((t3(a, j, c, d) * T[J][j, b]
                      for j in range(2)), sp.Integer(0))
                -sum((t3(a, b, k, d) * T[J][c, k]
                      for k in range(2)), sp.Integer(0))
                +sum((t3(a, b, c, ell) * T[J][ell, d]
                      for ell in range(2)), sp.Integer(0))
            )
            assert sp.simplify(variation) == 0


def verify_higgs_contact_tensors():
    # T3_(ij,kl) (sigma^J/2)_(jm)
    # = delta_il sigma^J_(km) - 1/2 sigma^J_(im) delta_kl.
    for J in range(3):
        for i, ell, k, m in itertools.product(range(2), repeat=4):
            lhs = sum((t3(i, j, k, ell) * T[J][j, m]
                       for j in range(2)), sp.Integer(0))
            rhs = (DELTA[i, ell] * SIGMA[J][k, m]
                   - sp.Rational(1, 2) * SIGMA[J][i, m] * DELTA[k, ell])
            assert sp.simplify(lhs - rhs) == 0

    # D H = dH - i g t.W H; D Hdag = dHdag + i g Hdag t.W.
    minus_contact = sp.simplify(I * (-I*g2 - I*g2))
    plus_contact = sp.simplify(I * (-I*g2 + I*g2))
    assert minus_contact == 2*g2
    assert plus_contact == 0


def coefficients():
    a = -sp.Rational(1, 2) + L/2
    b = -sp.Rational(1, 32) + sp.Rational(7, 16)*L
    c = sp.Rational(7, 32) - sp.Rational(5, 16)*L
    return a, b, c


def verify_matching_log_slopes():
    a, b, c = coefficients()
    # dL/dln(mu_R)=-2. Explicit-log slopes only; coupling running is
    # higher order for this one-loop matching term.
    slopes = tuple(sp.diff(x, L) * (-2) for x in (a, b, c))
    assert slopes == (-1, -sp.Rational(7, 8), sp.Rational(5, 8))
    return slopes


def main():
    verify_adjoint_commutator()
    verify_local_adjoint_ward_identity()
    verify_t3_invariance()
    verify_higgs_contact_tensors()
    a, b, c = coefficients()
    slopes = verify_matching_log_slopes()

    qd_contact = sp.simplify(sp.I*g2*F*a)
    minus_contact = sp.simplify(2*g2*F*b)
    plus_contact = sp.Integer(0)
    at_match = tuple(sp.simplify(x.subs(L, 0))
                     for x in (qd_contact, minus_contact, plus_contact))
    assert at_match == (-sp.I*g2*F/2, -g2*F/16, 0)

    print("RC-001 EFT local one-W vertex and SU(2) Ward-covariance audit")
    print("PASS: [t^J,sigma^I] = -i epsilon^{IJK} sigma^K for all generators.")
    print("PASS: the inhomogeneous local-gauge variation cancels in D_adj Y.")
    print("PASS: X^I (D_adj Y)^I is locally SU(2)-invariant.")
    print("PASS: T3_(ij,kl) is invariant under all four external doublet transformations.")
    print("PASS: exact T3 times Higgs-generator contraction for I=1,2,3.")
    print("PASS: O_minus contact is +2 g2 Hdag T^J H; O_plus contact is zero.")
    print(f"Coefficients: a={a}, b={b}, c={c}")
    print(f"Explicit-log slopes d(a,b,c)/dln(mu_R)={slopes}")
    print(f"At mu_R=M_E, contact coefficients (including F): {at_match}")
    print("F = g2^2 |y_l|^2/(16 pi^2 M_E^2).")
    print("BOUNDARY: exact local EFT contact/covariance audit only;")
    print("          UV one-loop five-point form factor and full ST sum remain open.")


if __name__ == "__main__":
    main()
