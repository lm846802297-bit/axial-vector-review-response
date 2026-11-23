#!/usr/bin/env python3
"""RC-001 QLD dimension-eight one-background amplitude-basis projection.

This is an exact SymPy projection of the hard form factors in
research/RC-001-QLD-UV-one-background-triangle.md onto a minimal
three-column off-shell kinematic basis.  It is NOT a complete nonredundant
SMEFT operator-basis reduction: IBP, Higgs/lepton EOM, gauge EOM, non-Abelian
completion, and the remaining model sectors are deliberately not eliminated.

All form factors below are scaled by pi^2 M_E^4; the common
g_A |y_l|^2 factor and the charge weights are restored in the output table.
"""
import sympy as sp

P, Q, R = sp.symbols("P Q R")
epsIR, LM, ellQ = sp.symbols("eps_IR L_M ell_Q")
Pp = P + Q - 2*R
Sigma3 = sp.expand(P**2 + P*Pp + Pp**2)

# Minimal off-shell amplitude tensors:
# T^mu = Q p^mu - R q^mu, q_mu T^mu = 0
# S^mu = -(p+p')^mu (P^2 + P P' + P'^2),
# q_mu S^mu = P'^3 - P^3, with q=p-p' and P'=p'^2.
BP = (Q*(P-R), -R*(P-R))       # (F_p,F_q) for (P-R) T^mu
BQ = (Q**2, -R*Q)               # (F_p,F_q) for Q T^mu
BS = (-2*Sigma3, Sigma3)        # (F_p,F_q) for S^mu
basis = [BP, BQ, BS]

# Flatten the two form factors into the six independent quadratic
# monomials in (P,Q,R), in the order shown.
monomials = [P**2, P*Q, P*R, Q**2, Q*R, R**2]
matrix = sp.Matrix(
    12, 3,
    lambda i, j: sp.expand(basis[j][0 if i < 6 else 1]).coeff(
        monomials[i if i < 6 else i-6]
    )
)
assert matrix.rank() == 3
minor = matrix[[0, 1, 3], :].det()
assert minor == -6
gram_det = sp.factor((matrix.T * matrix).det())
assert gram_det == 3432

# The massless on-shell scalar restriction P=P'=0 implies R=Q/2.
# It collapses the three-column map: B_P=-B_Q/2 and B_S=0.
on_shell = {P: 0, R: Q/2}
BP_os = tuple(sp.factor(x.subs(on_shell)) for x in BP)
BQ_os = tuple(sp.factor(x.subs(on_shell)) for x in BQ)
BS_os = tuple(sp.factor(x.subs(on_shell)) for x in BS)
assert sp.simplify(BP_os[0] + BQ_os[0]/2) == 0
assert sp.simplify(BP_os[1] + BQ_os[1]/2) == 0
assert BS_os == (0, 0)

# Ward identities of the basis columns.
assert sp.expand(R*BP[0] + Q*BP[1]) == 0
assert sp.expand(R*BQ[0] + Q*BQ[1]) == 0
assert sp.expand(R*BS[0] + Q*BS[1] - (Pp**3-P**3)) == 0

# Hard-region form factors quoted in §5D, with pi^2 M_E^4 stripped.
common_X = 30*(P-R)/epsIR + 30*LM*(P-R) + 70*P + 21*Q - 70*R
FpX_hard = Q*common_X/720
FqX_hard = -R*common_X/720

FpL_hard = (
    Q*(P-R)/(24*epsIR)
    + (12*LM*Q*(P-R)-9*P**2+18*P*R+16*P*Q
       -12*R**2-13*R*Q+3*Q**2)/288
)
FqL_hard = (
    -R*(P-R)/(24*epsIR)
    + (-24*LM*P*R+24*LM*R**2+9*P**2-68*P*R
       +9*P*Q+62*R**2-24*R*Q+3*Q**2)/576
)

# The source column is fixed by the scalar two-point Ward difference.
cS = sp.Rational(1, 192)
fX_hard = sp.factor(FpX_hard/Q)
fL_hard = sp.factor((FpL_hard + 2*cS*Sigma3)/Q)
assert sp.simplify(FqX_hard + R*fX_hard) == 0
assert sp.simplify(FqL_hard - cS*Sigma3 + R*fL_hard) == 0
assert sp.simplify(
    R*FpX_hard + Q*FqX_hard
) == 0
assert sp.simplify(
    R*FpL_hard + Q*FqL_hard - (Pp**3-P**3)/192
) == 0

# Coefficients in Gamma_X = a_X B_P + b_X B_Q and
# Gamma_L = a_L B_P + b_L B_Q + c_S B_S.
aX = (30/epsIR + 30*LM + 70)/720
bX = sp.Rational(21, 720)
aL = (12/epsIR + 12*LM + 25)/288
bL = sp.Rational(1, 48)
assert sp.simplify(fX_hard - (aX*(P-R)+bX*Q)) == 0
assert sp.simplify(fL_hard - (aL*(P-R)+bL*Q)) == 0

# Charge-resolved hard coefficients, in the same common normalization.
# U(1)_X: q_H=0; hypercharge: q_E=-1,q_H=+1/2;
# SU(2)_L: q_E=0 and q_H is the appropriate doublet generator.
aY = sp.factor(-aX + sp.Rational(1,2)*aL)
bY = sp.factor(-bX + sp.Rational(1,2)*bL)
cY = sp.factor(sp.Rational(1,2)*cS)
assert sp.simplify(aY + (60/epsIR+60*LM+155)/2880) == 0
assert sp.simplify(bY + sp.Rational(3,160)) == 0
assert cY == sp.Rational(1,384)

# Independent scalar two-point source check. Extend the exact B0(p^2;0,M_E^2)
# expansion by one term beyond the p^4 term displayed in the baseline note.
z2, DeltaUV, L2, h2, y2 = sp.symbols("z2 DeltaUV L2 h2 y2")
B0_series = DeltaUV - L2 + 1 + z2/2 + z2**2/6 + z2**3/12
Pi_over_M2 = -h2*((DeltaUV-L2+1) + (1-z2)*B0_series)
p6_coefficient = sp.expand(Pi_over_M2).coeff(z2,3)
assert sp.simplify(p6_coefficient-h2/12) == 0
assert sp.simplify(
    p6_coefficient.subs(h2,y2/(16*sp.pi**2))
    - y2/(192*sp.pi**2)
) == 0

# Independent finite full-amplitude cross-check against §5G.
FpX_full = Q*(30*(P-R)*ellQ + 20*(P-R) + 21*Q)/720
FqX_full = -R*(30*(P-R)*ellQ + 20*(P-R) + 21*Q)/720
FpL_full = (
    Q*(P-R)*ellQ/24
    + (-9*P**2-4*P*Q+18*P*R+3*Q**2+7*Q*R-12*R**2)/288
)
FqL_full = (
    -R*(P-R)*ellQ/24
    + (9*P**2+9*P*Q-28*P*R+3*Q**2-24*Q*R+22*R**2)/576
)
fX_full = (30*ellQ+20)*(P-R)/720 + sp.Rational(21,720)*Q
fL_full = (12*ellQ+5)*(P-R)/288 + sp.Rational(1,48)*Q
assert sp.simplify(FpX_full-Q*fX_full) == 0
assert sp.simplify(FqX_full+R*fX_full) == 0
assert sp.simplify(FpL_full-(Q*fL_full-2*cS*Sigma3)) == 0
assert sp.simplify(FqL_full-(-R*fL_full+cS*Sigma3)) == 0
assert sp.simplify(R*FpL_full+Q*FqL_full-(Pp**3-P**3)/192) == 0

print("RC-001 QLD dimension-eight one-background amplitude projection")
print("Normalization: all form factors are multiplied by pi^2 M_E^4;")
print("the common g_A |y_l|^2 and charge factors are omitted here.")
print()
print("Basis columns (F_p,F_q):")
print("B_P =", BP)
print("B_Q =", BQ)
print("B_S =", BS)
print("Sigma_3 =", Sigma3)
print()
print("12x3 polynomial coefficient matrix (rows: F_p then F_q;")
print("within each: P^2, P Q, P R, Q^2, Q R, R^2):")
print(matrix)
print("PASS: exact amplitude-map rank =", matrix.rank())
print("PASS: massless on-shell restriction collapses B_P=-B_Q/2 and B_S=0.")
print("PASS: minor using rows (F_p:P^2, F_p:PQ, F_p:Q^2) =", minor)
print("PASS: Gram determinant =", gram_det)
print()
print("Hard-region coefficient vectors:")
print("Gamma_X: (a_X,b_X,c_X) =", (sp.factor(aX), bX, 0))
print("Gamma_L: (a_L,b_L,c_L) =", (sp.factor(aL), bL, cS))
print("Hypercharge (-Gamma_X + Gamma_L/2):", (aY,bY,cY))
print("SU(2)_L: T^a times Gamma_L")
print()
print("PASS: pure-X hard Ward identity is transverse.")
print("PASS: L-source hard Ward identity equals (P'^3-P^3)/192.")
print("PASS: hard form factors reconstruct exactly in the three-column basis.")
print("PASS: finite full amplitudes in §5G reconstruct in the same basis.")
print("PASS: exact B0 extension gives Pi|p^6 = h_y p^6/(12 M_E^4) = |y|^2 p^6/(192 pi^2 M_E^4).")
print()
print("LIMIT: rank 3 establishes independence only in this restricted")
print("off-shell one-background amplitude projection. It is not an IBP/EOM-")
print("reduced dimension-eight SMEFT basis and does not close other channels.")
print("LIMIT: hard coefficients still carry hard-region IR poles; they are")
print("not presented as finite renormalized Wilson coefficients.")
