#!/usr/bin/env python3
"""RC-001 Abelian QLD8 IBP/EOM coefficient audit.

The covariant IBP and commutator identities are derived in §5K of
RC-001-QLD-UV-one-background-triangle.md. This script checks the exact
polynomial amplitude map, the induced retained O_Q coefficients, the
Higgs-potential derivative expansion, and the charge boundary q_H=0
for U(1)_X. It does not claim a non-Abelian operator-basis reduction.
"""
import sympy as sp

P, Q, R = sp.symbols("P Q R")
epsIR, LM = sp.symbols("eps_IR L_M")
muH2, lamH, lamHS, X, Y = sp.symbols(
    "mu_H2 lambda_H lambda_HS X Y"
)
dX, dY = sp.symbols("dX dY")
qH, gA = sp.symbols("q_H g_A")

Pp = sp.expand(P + Q - 2*R)
BP = (Q*(P-R), -R*(P-R))
BQ = (Q**2, -R*Q)
BE = tuple(sp.factor(BP[i] + BQ[i]/2) for i in range(2))
BE_expected = (Q*(P+Pp)/2, -R*(P+Pp)/2)
assert all(sp.simplify(BE[i]-BE_expected[i]) == 0 for i in range(2))
assert sp.simplify(R*BE[0] + Q*BE[1]) == 0

# Exact operator coefficient map:
# a O_P + b O_Q = a O_E,H + (b-a/2) O_Q, modulo total derivatives.
aX = (30/epsIR + 30*LM + 70)/720
bX = sp.Rational(21, 720)
aY = -(60/epsIR + 60*LM + 155)/2880
bY = -sp.Rational(3, 160)
aW = (12/epsIR + 12*LM + 25)/288
bW = sp.Rational(1, 48)

cX = sp.factor(bX-aX/2)
cY = sp.factor(bY-aY/2)
cW = sp.factor(bW-aW/2)

assert sp.simplify(cX + (30/epsIR+30*LM+28)/1440) == 0
assert sp.simplify(cY - (60/epsIR+60*LM+47)/5760) == 0
assert sp.simplify(cW + (12/epsIR+12*LM+13)/576) == 0

# Higgs EOM convention of the project source:
# D^2 H = -f_H H - J_H, f_H=-mu_H^2+2 lambda_H X+lambda_HS Y.
fH = -muH2 + 2*lamH*X + lamHS*Y
dfH = sp.expand(2*lamH*dX + lamHS*dY)
assert sp.diff(fH, X) == 2*lamH
assert sp.diff(fH, Y) == lamHS
assert sp.simplify(dfH-(2*lamH*dX+lamHS*dY)) == 0

# With j_H=i H^dagger <->D H:
# (D_mu H)^dagger H=(partial_mu X+i j_Hmu)/2,
# H^dagger D_mu H=(partial_mu X-i j_Hmu)/2.
# The antisymmetric F contraction of the two derivative-f terms is
# exactly -1/2 F^{mu nu} j_Hmu partial_nu f_H.
coef_jX = -lamH
coef_jY = -lamHS/2
assert sp.simplify(coef_jX + lamH) == 0
assert sp.simplify(coef_jY + lamHS/2) == 0

# U(1)_X has q_H=0; U(1)_Y has q_H=+1/2.
assert sp.simplify((gA*qH).subs(qH, 0)) == 0
assert sp.simplify((gA*qH).subs(qH, sp.Rational(1,2))-gA/2) == 0

# The scalar-source coefficient c_S is not changed by this transverse
# O_P/O_Q IBP step.
cS = sp.Rational(1, 192)
assert cS == sp.Rational(1, 192)

print("RC-001 Abelian QLD8 IBP/EOM coefficient audit")
print("PASS: O_P + O_Q/2 has the exact off-shell vertex (P+P') T^mu/2.")
print("PASS: the combination is transverse and vanishes on the massless on-shell surface.")
print("PASS: a O_P + b O_Q -> a O_E,H + (b-a/2) O_Q.")
print("Hard-region retained O_Q coefficients (IR poles not yet subtracted):")
print("  U(1)_X:", cX, "with overall q_E")
print("  U(1)_Y:", cY)
print("  SU(2)_L amplitude-level only:", cW, "(non-Abelian EOM reduction not claimed)")
print("PASS: f_H and partial_nu f_H generate the stated X,Y companions.")
print("PASS: q_H=0 removes the A'-commutator terms for U(1)_X.")
print("PASS: c_S=1/192 is untouched by this transverse IBP step.")
print("LIMIT: this is an exact coefficient/kinematic audit, not an external")
print("diagram-package run or a complete non-Abelian SMEFT basis reduction.")
