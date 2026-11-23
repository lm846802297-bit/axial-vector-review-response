#!/usr/bin/env python3
"""Exact symbolic checks for the RC-001 tree-level dimension-five matching.

Scope: chiral projector algebra, low-momentum propagator expansion, and the
mass-matrix Schur complement fixing the sign of C5 in the declared operator
convention. This is not a one-loop matching calculation.
"""
import sympy as sp

def check(name, expr, expected=0):
    residual = sp.simplify(expr - expected)
    if isinstance(residual, sp.MatrixBase):
        ok = residual == sp.zeros(*residual.shape)
    else:
        ok = residual == 0
    if not ok:
        raise AssertionError(f"{name}: residual={residual}")
    print(f"PASS: {name}")

I = sp.I
zero = sp.zeros(2)
sigmas = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for sigma in sigmas:
    gamma.append(sp.Matrix.vstack(
        sp.Matrix.hstack(zero, sigma),
        sp.Matrix.hstack(-sigma, zero),
    ))
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
PR = sp.simplify((sp.eye(4) + gamma5) / 2)
PL = sp.simplify((sp.eye(4) - gamma5) / 2)
p = sp.symbols("p0:4", real=True)
slashp = gamma[0]*p[0] - gamma[1]*p[1] - gamma[2]*p[2] - gamma[3]*p[3]
p2 = p[0]**2 - p[1]**2 - p[2]**2 - p[3]**2

check("P_R^2=P_R", PR*PR, PR)
check("P_L^2=P_L", PL*PL, PL)
check("P_R P_L=0", PR*PL, sp.zeros(4))
check("Minkowski Clifford algebra gives slash(p)^2=p^2", slashp*slashp, p2*sp.eye(4))
check("P_R slash(p) P_R=0", PR*slashp*PR, sp.zeros(4))
check("P_R slash(p) P_L=slash(p) P_L", PR*slashp*PL, slashp*PL)

M = sp.symbols("M_E", nonzero=True)
prop3 = -sp.eye(4)/M - slashp/M**2 - p2*sp.eye(4)/M**3
check("mass-numerator P_R propagator through O(p^2/M^3)",
      PR*prop3*PR, -PR/M - p2*PR/M**3)
check("chirality-preserving P_R...P_L propagator starts at O(p/M^2)",
      PR*prop3*PL, -slashp*PL/M**2)

y, lam, vh, vs, C5 = sp.symbols("y lambda vh vs C5", nonzero=True)
mass_matrix = sp.Matrix([
    [0, y*vh/sp.sqrt(2)],
    [lam*vs/sp.sqrt(2), M],
])
schur = sp.simplify(mass_matrix[0, 0] - mass_matrix[0, 1]*mass_matrix[1, 0]/mass_matrix[1, 1])
check("Schur complement of the heavy E block",
      schur, -y*lam*vh*vs/(2*M))
C5_match = sp.solve(sp.Eq(C5*vh*vs/2, schur), C5)[0]
check("declared EFT mass entry C5 vh vs/2 fixes C5=-y lambda/M",
      C5_match, -y*lam/M)

print("RESULT: 10 exact symbolic tree-level matching checks passed.")
print("SCOPE: tree-level C5 coefficient and propagator power counting only.")
print("OPEN: one-loop C5 renormalization, full dimension-six Wilson-vector closure, and B1/B3 physical-amplitude reconciliation.")
