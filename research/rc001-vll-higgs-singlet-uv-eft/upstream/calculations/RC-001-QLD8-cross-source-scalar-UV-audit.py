#!/usr/bin/env python3
"""Exact scalar-projector and UV-Taylor audit for the four QLD8 cross-source graphs.

The script computes only the physical P_R x P_L scalar projection of the
four cross-source one-gluon kernels. It does not claim the full Dirac
counterterm matrix or the finite evanescent-scheme matching.
"""
import sympy as sp

I = sp.I
zero2 = sp.zeros(2)
pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for sigma in pauli:
    gamma.append(sp.BlockMatrix([[zero2, sigma], [-sigma, zero2]]).as_explicit())
eta = [1, -1, -1, -1]
gamma_lower = [eta[mu] * gamma[mu] for mu in range(4)]
identity = sp.eye(4)
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
PR = sp.simplify((identity + gamma5) / 2)
PL = sp.simplify((identity - gamma5) / 2)


def slash(v):
    """Slash a covariant four-vector: gamma^mu v_mu."""
    return sum((gamma[mu] * v[mu] for mu in range(4)), sp.zeros(4))


def dot(a, b):
    """Minkowski product for covariant components."""
    return sp.expand(sum(eta[mu] * a[mu] * b[mu] for mu in range(4)))


def kron(a, b):
    return sp.kronecker_product(a, b)


def topology_data(top, p1, p2, p3):
    p4 = -p1 - p2 - p3
    if top == 1:  # (barQ,Q)
        return p1, p4, 1
    if top == 2:  # (barQ,bard)
        return p1, p3, 1
    if top == 3:  # (Q,d)
        return p4, p2, -1
    if top == 4:  # (bard,d)
        return p3, p2, -1
    raise ValueError(top)


def scalar_projected_chain(top, p1, p2, p3, ell):
    """Return Tr[(PR x PL) N]/4 for the exact open-line numerator."""
    pa, pb, _ = topology_data(top, p1, p2, p3)
    ra, rb = pa + ell, pb - ell
    chain = sp.zeros(16)
    for rho in range(4):
        if top == 1:
            left = gamma[rho] * slash(ra) * PR
            right = PL * slash(rb) * gamma_lower[rho]
        elif top == 2:
            left = gamma[rho] * slash(ra) * PR
            right = gamma_lower[rho] * slash(rb) * PL
        elif top == 3:
            left = PR * slash(rb) * gamma[rho]
            right = PL * slash(ra) * gamma_lower[rho]
        else:
            left = PR * slash(rb) * gamma[rho]
            right = gamma_lower[rho] * slash(ra) * PL
        chain += kron(left, right)
    projector = kron(PR, PL)
    return sp.simplify(sp.trace(projector * chain) / 4), dot(ra, rb)


def scalar_uv_kernel_D(top, p1, p2, p3, D):
    """UV-log coefficient after a common auxiliary mass in all denominators.

    The three massive Euclidean radial integrals have common Gamma(epsilon)
    prefactor and relative factors
      A=D/4, B=D(D+2)/24, C=D(D+2)(D+4)/192.
    """
    pa, pb, sign = topology_data(top, p1, p2, p3)
    q = p1 + p2
    delta = pb - pa
    pa2, pb2 = dot(pa, pa), dot(pb, pb)
    q2, u = dot(q, q), dot(pa, pb)
    qdelta, delta2 = dot(q, delta), dot(delta, delta)
    A = D / 4
    B = D * (D + 2) / 24
    C = D * (D + 2) * (D + 4) / 192
    return sp.factor(
        A * (u - q2 + 2 * sign * qdelta / D)
        + B * (2 * delta2 / D - 4 * sign * qdelta / D + pa2 + pb2)
        - 4 * (pa2 + pb2 - u) * C / D
    )


def invariant_coefficients(expr, p1, p2, p3):
    variables = list(p1) + list(p2) + list(p3)
    invariants = [
        dot(p1, p1), dot(p2, p2), dot(p3, p3),
        dot(p1, p2), dot(p1, p3), dot(p2, p3),
    ]
    coeff = sp.symbols("c0:6")
    ansatz = sum(coeff[i] * invariants[i] for i in range(6))
    poly = sp.Poly(sp.expand(expr - ansatz), *variables)
    solution = sp.solve(poly.coeffs(), coeff, dict=True)
    if len(solution) != 1:
        raise AssertionError("Could not uniquely express result in Lorentz invariants")
    return [sp.factor(solution[0][c]) for c in coeff]


def main():
    p1 = sp.Matrix(sp.symbols("p10:14"))
    p2 = sp.Matrix(sp.symbols("p20:24"))
    p3 = sp.Matrix(sp.symbols("p30:34"))
    p4 = -p1 - p2 - p3
    D = sp.symbols("D")
    eps = sp.symbols("epsilon")

    # Exact gamma-matrix check of the scalar projection for all four chains.
    samples = [
        ([1, 2, 0, 1], [0, 1, 1, 0], [2, 0, 1, 1], [1, 0, 2, -1]),
        ([2, -1, 1, 0], [1, 0, 2, -1], [0, 2, 1, 1], [-1, 1, 0, 2]),
        ([0, 1, 2, 1], [2, -1, 0, 1], [1, 1, -2, 0], [2, 0, 1, -1]),
    ]
    nchecks = 0
    for p1s, p2s, p3s, ells in samples:
        a, b, c, ell = map(sp.Matrix, (p1s, p2s, p3s, ells))
        for top in range(1, 5):
            projected, expected = scalar_projected_chain(top, a, b, c, ell)
            assert sp.simplify(projected - expected) == 0
            nchecks += 1

    # Compute each topology's scalar-scalar UV logarithmic coefficient.
    kernels_D = [
        scalar_uv_kernel_D(top, p1, p2, p3, D)
        for top in range(1, 5)
    ]
    kernels_4 = [sp.factor(k.subs(D, 4)) for k in kernels_D]
    coeffs = [invariant_coefficients(k, p1, p2, p3) for k in kernels_4]

    # Tree-singlet -> direct-octet color actions:
    # (barQ,Q):-1, (barQ,bard):+1, (Q,d):+1, (bard,d):-1.
    weights = [-1, 1, 1, -1]
    total_D = sp.factor(sum(weights[i] * kernels_D[i] for i in range(4)))
    expected_total = sp.factor(
        (D**2 + 10 * D - 8) / 48 * dot(p1 - p2, p3 - p4)
    )
    assert sp.expand(total_D - expected_total) == 0
    total_4 = sp.factor(total_D.subs(D, 4))
    assert sp.expand(total_4 - dot(p1 - p2, p3 - p4)) == 0

    eps_form = sp.factor(total_D.subs(D, 4 - 2 * eps))
    eps_series = sp.series(
        eps_form / dot(p1 - p2, p3 - p4), eps, 0, 3
    ).removeO()

    print("RC-001 QLD8 cross-source scalar UV-Taylor audit")
    print(f"PASS: exact gamma-trace scalar projection: {nchecks}/{nchecks} topology/sample checks.")
    print("Scalar projection identity: Tr[(PR x PL) N_ab]/4 = r_a.r_b.")
    print("Common auxiliary-mass UV radial factors: A=D/4, B=D(D+2)/24, C=D(D+2)(D+4)/192.")
    labels = ["(barQ,Q)", "(barQ,bard)", "(Q,d)", "(bard,d)"]
    names = ["p1^2", "p2^2", "p3^2", "p1.p2", "p1.p3", "p2.p3"]
    for label, coeff in zip(labels, coeffs):
        print(label + ": " + ", ".join(
            f"{name}={value}" for name, value in zip(names, coeff)
        ))
    print("PASS: tree-color-weighted scalar projection is")
    print("  K_SS,total(D) = (D^2+10D-8)/48 * (p1-p2).(p3-p4).")
    print("  At D=4: K_SS,total = (p1-p2).(p3-p4).")
    print(f"  D=4-2epsilon factor = {sp.factor(eps_series)}.")
    print("LIMIT: scalar-scalar projection only; no tensor projections, complete Z matrix,")
    print("       full graph phase/sign convention, or finite evanescent-scheme matching.")


if __name__ == "__main__":
    main()
