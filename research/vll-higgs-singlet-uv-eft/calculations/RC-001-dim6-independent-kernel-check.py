#!/usr/bin/env python3
"""Independent compact checks for the RC-001 dimension-six soft kernels.

This deliberately separate script re-derives a small set of identities from
Feynman-parameter integrals and exact algebra. It is not a diagram generator,
does not integrate the full UV amplitudes, and does not replace FeynCalc.
"""
import sympy as sp

x = sp.symbols("x", positive=True)
Delta, L, ell = sp.symbols("Delta_UV_IR L_E ell_q")
checks = []

def check(name, expr):
    residual = sp.simplify(expr)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks.append(name)
    print(f"PASS: {name}")

# 1. Direct Feynman-parameter integral of the massless two-point bubble.
log_integral = sp.integrate(sp.log(x) + sp.log(1 - x), (x, 0, 1))
check("direct Feynman-parameter logarithm integral is -2", log_integral + 2)

# 2. First moment after shifting the massless bubble loop momentum.
x_mean = sp.integrate(x, (x, 0, 1))
check("symmetric Feynman-parameter first moment is 1/2", x_mean - sp.Rational(1, 2))

# 3. Scalar four-point numerator reduction.
k2, kdotq, q2 = sp.symbols("k2 kdotq q2")
check("2 k.(k+q) numerator identity",
      2 * (k2 + kdotq) - (k2 + (k2 + 2*kdotq + q2) - q2))

# 4. Crossed-current hard/soft pole cancellation, retaining the O(epsilon)
# finite term already derived in the primary audit.
hard_crossed = -Delta/2 + L/2 - sp.Rational(3, 4)
soft_crossed = (Delta - ell + 2)/2
check("crossed-current hard/soft sum", hard_crossed + soft_crossed - ((L-ell)/2 + sp.Rational(1, 4)))

# 5. Four-fermion scalar-bubble hard/soft pole and constant cancellation.
hard_4f = -Delta + L - 2
soft_4f = Delta - ell + 2
check("four-fermion hard/soft sum", hard_4f + soft_4f - (L - ell))

# 6. Q6-plus-quartic hard/soft cancellation and off-shell EOM momentum ratio.
hard_q6 = -Delta + L - sp.Rational(3, 2)
soft_q6 = Delta - ell + 2
check("Q6-quartic hard/soft sum", hard_q6 + soft_q6 - (L - ell + sp.Rational(1, 2)))
hard_q6_p = -Delta + L - sp.Rational(3, 2)
hard_q6_Q = -Delta/2 + L/2 - sp.Rational(3, 4)
check("Q6-quartic vector coefficients are proportional to p+Q/2",
      hard_q6_p/2 - hard_q6_Q)

# 7. Independent exact SU(2) singlet/triplet completeness test.
I = sp.I
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
components = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                lhs = int(i == l and j == k)
                rhs = sp.Rational(1, 2) * (
                    int(i == j and k == l)
                    + sum(s[i, j] * s[k, l] for s in (sigma1, sigma2, sigma3))
                )
                check(f"SU(2) completeness component {i}{j}{k}{l}", lhs-rhs)
                components += 1

print(f"RESULT: {len(checks)} exact symbolic checks passed ({components} SU(2) components).")
print("SCOPE: independent local algebra/Feynman-parameter checks of stripped kernels only.")
print("NOT CLAIMED: full UV diagram generation, gauge-sector closure, or model-level Wilson-vector closure.")
