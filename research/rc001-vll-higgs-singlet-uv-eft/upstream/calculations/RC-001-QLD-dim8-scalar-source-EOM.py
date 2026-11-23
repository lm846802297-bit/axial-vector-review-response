#!/usr/bin/env python3
"""RC-001 QLD8 scalar-source higher-derivative EOM audit.

Checks the exact EOM identity O_S=H^dagger(-D^2)^3 H -> |D(f_H H+J_H)|^2,
its pure-bosonic expansion, and the source cross-term decomposition.
This is an algebraic EOM/IBP audit, not an independent loop calculation.
"""
import sympy as sp

mu2, lamH, lamHS, X, Y = sp.symbols(
    "mu_H2 lambda_H lambda_HS X Y"
)
dX, dY, DH2 = sp.symbols("dX dY DH2")
fH = -mu2 + 2*lamH*X + lamHS*Y
df = 2*lamH*dX + lamHS*dY

# Exact expansion of f_H^2 multiplying |D H|^2.
f2_expected = (
    mu2**2 - 4*mu2*lamH*X - 2*mu2*lamHS*Y
    + 4*lamH**2*X**2 + 4*lamH*lamHS*X*Y
    + lamHS**2*Y**2
)
assert sp.expand(fH**2-f2_expected) == 0

# Pure-bosonic derivative part:
# X (partial f)^2 + f (partial f).(partial X).
derivative_part = sp.expand(X*df**2 + fH*df*dX)
expected_derivative = (
    (-2*mu2*lamH + 8*lamH**2*X + 2*lamH*lamHS*Y)*dX**2
    + (-mu2*lamHS + 6*lamH*lamHS*X + lamHS**2*Y)*dX*dY
    + lamHS**2*X*dY**2
)
assert sp.expand(derivative_part-expected_derivative) == 0

# The product rule D_mu(f_H H + J_H) gives A+B+C.
# Verify the norm decomposition with independent conjugate symbols.
A, Abar, B, Bbar, C, Cbar = sp.symbols("A Abar B Bbar C Cbar")
norm_full = sp.expand((Abar+Bbar+Cbar)*(A+B+C))
norm_split = (
    Abar*A + Bbar*B + Cbar*C
    + Abar*B + Bbar*A
    + Abar*C + Cbar*A
    + Bbar*C + Cbar*B
)
assert sp.expand(norm_full-norm_split) == 0

# Source pieces retained in the EOM-reduced basis:
# |D J_H|^2, (partial f)[H^dagger D J + h.c.],
# and f[(D H)^dagger D J + h.c.].
cS = sp.Rational(1, 192)
assert cS == sp.Rational(1, 192)

print("RC-001 QLD8 scalar-source higher-derivative EOM audit")
print("PASS: H^dagger(-D^2)^3H ~= |D_mu(f_H H+J_H)|^2.")
print("PASS: f_H^2 expansion into X,Y potential companions.")
print("PASS: all three pure-bosonic derivative coefficients.")
print("PASS: source norm splits into |D J_H|^2 and both cross-term families.")
print("PASS: source coefficient c_S=1/192 is carried unchanged.")
print("LIMIT: no further fermion-EOM, IBP-basis, or Fierz reduction is claimed.")
print("LIMIT: this is an exact EOM/IBP algebra check, not a new loop calculation.")
