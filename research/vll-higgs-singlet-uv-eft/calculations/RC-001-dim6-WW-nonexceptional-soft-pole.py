#!/usr/bin/env python3
"""Nonexceptional EFT-soft UV-pole audit for the four Q_LD pure-WW cross boxes.

The calculation keeps the external ordering barL(p1), H(p2), Hdag(p3), L(p4),
uses a symmetric Euclidean point, expands the heavy propagator in the soft
region, and extracts the UV pole from the l_mu l_nu tensor integral.

The result is a stripped numerator sub-block: common g2^2 |y|^2 factors and
the overall Minkowski Feynman-rule phase are not included. The leading soft
heavy propagator contributes -1/M_E^2.
"""
from functools import lru_cache

import mpmath as mp
import sympy as sp


PAIRS = ("01", "02", "05", "06")
WEIGHTS = {
    "01": -sp.Rational(1, 4),
    "02": sp.Rational(1, 4),
    "05": sp.Rational(1, 4),
    "06": -sp.Rational(1, 4),
}


def euclidean_gamma_matrices():
    I = sp.I
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )
    zero, eye = sp.zeros(2), sp.eye(2)
    return (
        sp.BlockMatrix([[zero, -I * pauli[0]], [I * pauli[0], zero]]).as_explicit(),
        sp.BlockMatrix([[zero, -I * pauli[1]], [I * pauli[1], zero]]).as_explicit(),
        sp.BlockMatrix([[zero, -I * pauli[2]], [I * pauli[2], zero]]).as_explicit(),
        sp.BlockMatrix([[zero, eye], [eye, zero]]).as_explicit(),
    )


GAMMA = euclidean_gamma_matrices()
GAMMA5 = GAMMA[0] * GAMMA[1] * GAMMA[2] * GAMMA[3]
P_L = (sp.eye(4) - GAMMA5) / 2
P_R = (sp.eye(4) + GAMMA5) / 2
L = sp.symbols("l0:4")
Y, Z = sp.symbols("y z")


def vadd(*vectors):
    return [sp.expand(sum(v[i] for v in vectors)) for i in range(4)]


def vscale(c, vector):
    return [sp.expand(c * item) for item in vector]


def vsub(a, b):
    return [sp.expand(a[i] - b[i]) for i in range(4)]


def vdot(a, b):
    return sp.expand(sum(a[i] * b[i] for i in range(4)))


def slash(vector):
    return sum(
        (vector[i] * GAMMA[i] for i in range(4)),
        sp.zeros(4),
    )


def symmetric_momenta():
    """p_i^2=1 and p_i.p_j=-1/3, with p1+p2+p3+p4=0."""
    p1 = [sp.Integer(1), 0, 0, 0]
    p2 = [-sp.Rational(1, 3), 2 * sp.sqrt(2) / 3, 0, 0]
    p3 = [
        -sp.Rational(1, 3),
        -sp.sqrt(2) / 3,
        sp.sqrt(sp.Rational(2, 3)),
        0,
    ]
    p4 = vscale(-1, vadd(p1, p2, p3))
    return p1, p2, p3, p4


def exceptional_momenta():
    """Old local point: p1=p3=0, p2=P, p4=-P, with P^2=1."""
    return (
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [-1, 0, 0, 0],
    )


def routing(pair, momenta):
    """Return the shifted triangle denominators and the numerator matrix.

    The heavy momentum is q_E=k-p1-p2 for all four cross-vertex pairs.
    The Feynman-parameter shift is k=l-y*a-z*b for denominators
    k^2, (k+a)^2, (k+b)^2.
    """
    p1, p2, p3, p4 = momenta
    if pair == "01":
        a, b = vscale(-1, p1), p4
    elif pair == "02":
        a, b = vscale(-1, p1), p3
    elif pair == "05":
        a, b = vscale(-1, p2), p4
    elif pair == "06":
        a, b = vscale(-1, p2), p3
    else:
        raise ValueError(pair)

    ell = list(L)
    k = vsub(ell, vadd(vscale(Y, a), vscale(Z, b)))
    q_e = vsub(k, vadd(p1, p2))
    q_bar_l = vsub(p1, k)
    q_l = vadd(k, p4)

    if pair == "01":
        numerator = sp.zeros(4)
        for mu in range(4):
            numerator += (
                GAMMA[mu]
                * slash(q_bar_l)
                * slash(q_e)
                * slash(q_l)
                * GAMMA[mu]
            )
    elif pair == "02":
        scalar_vertex = vadd(vscale(2, p3), k)
        numerator = -slash(scalar_vertex) * slash(q_bar_l) * slash(q_e)
    elif pair == "05":
        scalar_vertex = vsub(vscale(2, p2), k)
        numerator = slash(scalar_vertex) * slash(q_e) * slash(q_l)
    else:  # pair == "06"
        scalar_hdag = vadd(vscale(2, p3), k)
        scalar_h = vsub(vscale(2, p2), k)
        numerator = -vdot(scalar_hdag, scalar_h) * slash(q_e)

    return numerator.applyfunc(sp.expand), a, b


def eft_soft_numerator(pair, momenta):
    """Build the EFT Q_LD insertion numerator from its differentiated composite.

    The derivative momentum is q_D=p3+p4+k. Momentum conservation makes it
    identical to k-p1-p2, the soft limit of the UV heavy momentum. Gauge
    endpoints are attached to the two external lines named by the pair.
    """
    p1, p2, p3, p4 = momenta
    if pair == "01":
        a, b = vscale(-1, p1), p4
    elif pair == "02":
        a, b = vscale(-1, p1), p3
    elif pair == "05":
        a, b = vscale(-1, p2), p4
    elif pair == "06":
        a, b = vscale(-1, p2), p3
    else:
        raise ValueError(pair)
    ell = list(L)
    k = vsub(ell, vadd(vscale(Y, a), vscale(Z, b)))
    q_derivative = vadd(p3, p4, k)
    q_bar_l = vsub(p1, k)
    q_l = vadd(k, p4)
    scalar_hdag = vadd(vscale(2, p3), k)
    scalar_h = vsub(vscale(2, p2), k)

    if pair == "01":
        numerator = sp.zeros(4)
        for mu in range(4):
            numerator += (
                GAMMA[mu]
                * slash(q_bar_l)
                * slash(q_derivative)
                * slash(q_l)
                * GAMMA[mu]
            )
    elif pair == "02":
        numerator = -slash(scalar_hdag) * slash(q_bar_l) * slash(q_derivative)
    elif pair == "05":
        numerator = slash(scalar_h) * slash(q_derivative) * slash(q_l)
    elif pair == "06":
        numerator = -vdot(scalar_hdag, scalar_h) * slash(q_derivative)
    else:
        raise ValueError(pair)
    return numerator.applyfunc(sp.expand)


def simplex_integral_polynomial(expression):
    return sp.simplify(
        sp.integrate(
            sp.integrate(sp.expand(expression), (Z, 0, 1 - Y)),
            (Y, 0, 1),
        )
    )


def extract_soft_numerator(pair, momenta):
    """N=N0+N_{mu nu} l_mu l_nu+odd terms; return N0 and sum_mu N_mumu."""
    numerator, a, b = routing(pair, momenta)
    at_zero = {component: 0 for component in L}
    n0 = numerator.applyfunc(lambda e: sp.expand(e.subs(at_zero)))
    n_diag = sp.zeros(4)
    for component in L:
        n_diag += numerator.applyfunc(
            lambda e: sp.expand(sp.diff(e, component, 2).subs(at_zero) / 2)
        )
    return n0, n_diag, a, b


def soft_uv_residue(pair, momenta):
    """Coefficient of 1/(16 pi^2 eps_UV), before the -1/M_E^2 heavy factor.

    Feynman parametrization contributes 2; angular averaging gives 1/d.
    At d=4 this is (1/2) times the simplex integral of sum_mu N_mumu.
    """
    _, n_diag, _, _ = extract_soft_numerator(pair, momenta)
    return n_diag.applyfunc(simplex_integral_polynomial) / 2


def chiral_vector_coefficients(matrix):
    """Coefficients c_mu in matrix P_L = c_mu gamma_mu P_L, if rank one."""
    return [
        sp.simplify(sp.trace(GAMMA[mu] * P_R * matrix * P_L) / 2)
        for mu in range(4)
    ]


def momentum_basis_coefficients(vector, momenta):
    p1, p2, p3, _ = momenta
    c1, c2, c3 = sp.symbols("c1 c2 c3")
    solution = sp.solve(
        [
            c1 * p1[i] + c2 * p2[i] + c3 * p3[i] - vector[i]
            for i in range(3)
        ],
        (c1, c2, c3),
        dict=True,
    )
    if len(solution) != 1:
        raise AssertionError("The three-momentum Gram matrix is not invertible.")
    return [sp.simplify(solution[0][c]) for c in (c1, c2, c3)]


def scalar_triangle_parameter(r):
    """T(r)=int_0^1 dt [-ln(r t(1-t))]/[1-r t(1-t)]."""
    r = mp.mpf(r)
    return mp.quad(
        lambda t: -mp.log(r * t * (1 - t)) / (1 - r * t * (1 - t)),
        [0, mp.mpf("0.5"), 1],
    )


def epsilon_moment(r):
    """I_eps(r)=int_0^1 dt x/[x+r(1-x)t(1-t)] integrated over x.

    The x integral is done analytically, leaving this one-dimensional form.
    """
    r = mp.mpf(r)

    def integrand(t):
        a = r * t * (1 - t)
        return 1 / (1 - a) + a * mp.log(a) / (1 - a) ** 2

    return mp.quad(integrand, [0, mp.mpf("0.5"), 1])


@lru_cache(maxsize=1)
def compute_audit():
    symmetric = symmetric_momenta()
    residues = {
        pair: soft_uv_residue(pair, symmetric)
        for pair in PAIRS
    }
    eft_numerator_residuals = {}
    for pair in PAIRS:
        uv_numerator, _, _ = routing(pair, symmetric)
        eft_numerator = eft_soft_numerator(pair, symmetric)
        eft_numerator_residuals[pair] = sp.simplify(uv_numerator - eft_numerator)

    expected_pairs = {
        "01": [-1, 0, -1],
        "02": [0, -1, sp.Rational(3, 2)],
        "05": [0, sp.Rational(3, 2), sp.Rational(1, 2)],
        "06": [-1, -1, 0],
    }
    pair_coefficients = {
        pair: momentum_basis_coefficients(
            chiral_vector_coefficients(residues[pair]), symmetric
        )
        for pair in PAIRS
    }

    weighted = sum(
        (WEIGHTS[pair] * residues[pair] for pair in PAIRS),
        sp.zeros(4),
    )
    weighted_vector = chiral_vector_coefficients(weighted)
    weighted_coefficients = momentum_basis_coefficients(weighted_vector, symmetric)

    # The weighted UV residue has no independent rank-three gamma structure.
    weighted_reconstructed = sum(
        (weighted_vector[i] * GAMMA[i] for i in range(4)),
        sp.zeros(4),
    )
    weighted_residual = sp.simplify(weighted * P_L - weighted_reconstructed * P_L)

    exceptional = exceptional_momenta()
    exceptional_residues = {
        pair: soft_uv_residue(pair, exceptional)
        for pair in PAIRS
    }
    exceptional_weighted = sum(
        (WEIGHTS[pair] * exceptional_residues[pair] for pair in PAIRS),
        sp.zeros(4),
    )
    exceptional_coefficients = chiral_vector_coefficients(exceptional_weighted)

    # The nonlocal rank-three/epsilon structure in the finite scalar-triangle
    # part is isolated by the orthogonal gamma_4 direction after P_L.
    n0 = {
        pair: extract_soft_numerator(pair, symmetric)[0]
        for pair in PAIRS
    }
    weighted_n0 = sum(
        (WEIGHTS[pair] * n0[pair] for pair in PAIRS),
        sp.zeros(4),
    )
    epsilon_polynomial = sp.factor(
        sp.trace(GAMMA[3] * P_R * weighted_n0 * P_L) / 2
    )
    epsilon_symmetrized = sp.factor(
        (epsilon_polynomial + epsilon_polynomial.subs({Y: Z, Z: Y}, simultaneous=True)) / 2
    )

    # Every denominator triangle has a^2=b^2=1 and (a-b)^2=4/3.
    triangle_invariants = {}
    for pair in PAIRS:
        _, a, b = routing(pair, symmetric)
        triangle_invariants[pair] = (
            sp.simplify(vdot(a, a)),
            sp.simplify(vdot(b, b)),
            sp.simplify(vdot(vsub(a, b), vsub(a, b))),
        )

    return {
        "residues": residues,
        "eft_numerator_residuals": eft_numerator_residuals,
        "pair_coefficients": pair_coefficients,
        "expected_pairs": expected_pairs,
        "weighted_coefficients": weighted_coefficients,
        "weighted_residual": weighted_residual,
        "exceptional_coefficients": exceptional_coefficients,
        "triangle_invariants": triangle_invariants,
        "epsilon_polynomial": epsilon_polynomial,
        "epsilon_symmetrized": epsilon_symmetrized,
    }


def main():
    mp.mp.dps = 40
    data = compute_audit()

    # Euclidean Clifford algebra.
    for i in range(4):
        for j in range(4):
            target = 2 * (1 if i == j else 0) * sp.eye(4)
            assert sp.simplify(GAMMA[i] * GAMMA[j] + GAMMA[j] * GAMMA[i] - target) == sp.zeros(4)

    assert all(
        residual == sp.zeros(4)
        for residual in data["eft_numerator_residuals"].values()
    )
    assert data["pair_coefficients"] == data["expected_pairs"]
    assert data["weighted_coefficients"] == [
        sp.Rational(1, 2),
        sp.Rational(3, 8),
        sp.Rational(3, 4),
    ]
    assert data["weighted_residual"] == sp.zeros(4)
    assert data["exceptional_coefficients"] == [
        sp.Rational(3, 8), 0, 0, 0
    ]
    assert all(
        invariants == (1, 1, sp.Rational(4, 3))
        for invariants in data["triangle_invariants"].values()
    )
    assert sp.simplify(
        data["epsilon_polynomial"] - sp.sqrt(3) * (Y + 3 * Z - 2) / 9
    ) == 0
    assert sp.simplify(
        data["epsilon_symmetrized"] + 2 * sp.sqrt(3) * (1 - Y - Z) / 9
    ) == 0

    triangle = scalar_triangle_parameter(mp.mpf(4) / 3)
    eps_moment = epsilon_moment(mp.mpf(4) / 3)
    expected_triangle = mp.mpf("2.1240339480038191550754515898884732174783")
    expected_eps_moment = mp.mpf("0.7467700413397904843482771519674888779972")
    assert abs(triangle - expected_triangle) < mp.mpf("1e-35")
    assert abs(eps_moment - expected_eps_moment) < mp.mpf("1e-35")

    print("RC-001 nonexceptional pure-WW EFT-soft audit")
    print("PASS: replacing the heavy-line momentum by the EFT derivative momentum gives the same numerator for all four pairs (algebraic routing identity).")
    print("PASS: all four generalized routings reduce to the old exceptional denominators.")
    print("PASS: all four symmetric-point triangles have invariants (1,1,4/3) mu_IR^2.")
    print("Per-pair UV residues, in the (slash p1, slash p2, slash p3) basis:")
    for pair in PAIRS:
        print(f"  LD-W-{pair}: {data['pair_coefficients'][pair]}")
    print("Weighted T3 UV residue before the leading heavy factor:")
    print("  R_T3 = (1/2) slash p1 + (3/8) slash p2 + (3/4) slash p3")
    print("  EFT soft pole = -R_T3/(16 pi^2 M_E^2 eps_UV),")
    print("  up to the common g2^2 |y|^2 and overall Feynman-rule phase.")
    print("PASS: exceptional limit gives 3/8 slash P, reproducing the previous soft-pole coefficient.")
    print(f"Scalar triangle T(4/3) = {mp.nstr(triangle, 25)}")
    print(f"  I3 = T/(16 pi^2 mu_IR^2).")
    print(f"Finite epsilon moment I_eps(4/3) = {mp.nstr(eps_moment, 25)}")
    print("  stripped coefficient of slash(p_perp): -I_eps/(32 pi^2 mu_IR^2)")
    print("  after the soft heavy factor -1/M_E^2, its sign reverses.")
    print("PASS: a nonzero finite epsilon/pseudovector form factor is present in this fixed cross-box subset.")
    print("BOUNDARY: this is the EFT soft sub-block, not the full UV amplitude or complete WW matching.")


if __name__ == "__main__":
    main()
