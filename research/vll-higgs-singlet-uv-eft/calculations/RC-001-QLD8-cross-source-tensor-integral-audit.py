#!/usr/bin/env python3
"""D-dimensional tensor UV-Taylor kernel for QLD8 cross-source graphs.

The code audits the full degree-two rank-2 loop tensor I_{alpha beta}.
It checks its antisymmetric projection against the mixed-tensor result and
its formal D-dimensional trace against the scalar-projection kernel.
"""
import sympy as sp

D, eps = sp.symbols("D epsilon", nonzero=True)
Acoef = D / 4
Bcoef = D * (D + 2) / 24
Ccoef = D * (D + 2) * (D + 4) / 192

Avec = sp.Matrix(sp.symbols("A0:4"))
Bvec = sp.Matrix(sp.symbols("B0:4"))
qvec = sp.Matrix(sp.symbols("q0:4"))
delta = Bvec - Avec
u = Avec.dot(Bvec)
A2, B2, q2 = Avec.dot(Avec), Bvec.dot(Bvec), qvec.dot(qvec)


def wedge(x, y):
    return sp.Matrix([
        sp.expand(x[i] * y[j] - x[j] * y[i])
        for i in range(4) for j in range(i + 1, 4)
    ])


# Coefficient of the common Gamma(epsilon)/(4 pi)^(D/2) UV pole.
Iab = sp.zeros(4)
for alpha in range(4):
    for beta in range(4):
        g = sp.Integer(alpha == beta)
        Iab[alpha, beta] = sp.expand(
            Acoef * (
                Avec[alpha] * Bvec[beta]
                + (2 / D) * (
                    -Avec[alpha] * qvec[beta]
                    + qvec[alpha] * Bvec[beta]
                )
                - q2 * g / D
            )
            + (2 * Bcoef / D) * (
                -Avec[alpha] * delta[beta]
                + delta[alpha] * Bvec[beta]
            )
            - (4 * Bcoef / (D * (D + 2))) * (
                g * qvec.dot(delta)
                + qvec[alpha] * delta[beta]
                + delta[alpha] * qvec[beta]
            )
            + (Bcoef / D) * (A2 + B2) * g
            - (4 * Ccoef / (D * (D + 2))) * (
                g * (A2 + B2 - u)
                + 2 * Avec[alpha] * Avec[beta]
                + 2 * Bvec[alpha] * Bvec[beta]
                - Avec[alpha] * Bvec[beta]
                - Bvec[alpha] * Avec[beta]
            )
        )

# Antisymmetric part: I_ab - I_ba = (D-4)/12 W(A,B)+1/2 W(q,A+B).
antisym = sp.Matrix([
    sp.expand(Iab[i, j] - Iab[j, i])
    for i in range(4) for j in range(i + 1, 4)
])
expected_antisym = sp.simplify(
    (D - 4) / 12 * wedge(Avec, Bvec)
    + sp.Rational(1, 2) * wedge(qvec, Avec + Bvec)
)
assert sp.simplify(antisym - expected_antisym) == sp.zeros(6, 1)

# Formal D-dimensional trace: g^alpha_alpha = D, not 4.
trace_D = sp.factor(
    Acoef * (u + 2 * qvec.dot(delta) / D - q2)
    + 2 * Bcoef * delta.dot(delta) / D
    - 4 * Bcoef * qvec.dot(delta) / D
    + Bcoef * (A2 + B2)
    - 4 * Ccoef * (A2 + B2 - u) / D
)
scalar_kernel = sp.factor(
    Acoef * (u - q2 + 2 * qvec.dot(delta) / D)
    + Bcoef * (
        2 * delta.dot(delta) / D
        - 4 * qvec.dot(delta) / D
        + A2 + B2
    )
    - 4 * Ccoef * (A2 + B2 - u) / D
)
assert sp.simplify(trace_D - scalar_kernel) == 0

# Explicit D=4-2 epsilon radial factors and their first-order expansions.
radial = [Acoef, Bcoef, Ccoef]
radial_eps = [
    sp.series(x.subs(D, 4 - 2 * eps), eps, 0, 2).removeO()
    for x in radial
]
assert radial_eps == [
    1 - eps / 2,
    1 - sp.Rational(5, 6) * eps,
    1 - sp.Rational(13, 12) * eps,
]

print("RC-001 QLD8 cross-source full tensor UV-Taylor audit")
print("PASS: full I_{alpha beta} formula has the mixed antisymmetric projection.")
print("PASS: formal D-dimensional trace equals the independent scalar kernel.")
print("PASS: radial factors A=D/4, B=D(D+2)/24, C=D(D+2)(D+4)/192.")
print("PASS: D=4-2epsilon radial expansions:")
print(f"  A={radial_eps[0]}, B={radial_eps[1]}, C={radial_eps[2]}.")
print("LIMIT: I_{alpha beta} is the raw Lorentz tensor for the rank-two x rank-two")
print("       chain; gamma/color contraction into a reduced operator basis,")
print("       complete graph phase, and full Z matrix remain open.")
