#!/usr/bin/env python3
"""Exact algebra audit for the non-Abelian QLD8 IBP/EOM completion.

Checks:
  * SU(2) fundamental-generator products;
  * the adjoint product rule for H^dagger T^a G;
  * the matrix-ordered [D^2,D_mu] commutator contribution;
  * the delta/epsilon decomposition of the SU(2) derivative and F^2 terms;
  * the retained coefficient b-a/2.

This is an algebraic identity audit, not a loop calculation, a full
SMEFT basis reduction, or a UV--EFT Wilson-coefficient determination.
"""
import sympy as sp

I = sp.I
g = sp.symbols("g", real=True)
T = [
    sp.Matrix([[0, 1], [1, 0]]) / 2,
    sp.Matrix([[0, -I], [I, 0]]) / 2,
    sp.Matrix([[1, 0], [0, -1]]) / 2,
]
eps = sp.LeviCivita

# 1. SU(2) generator algebra.
for a in range(3):
    for b in range(3):
        rhs = sp.KroneckerDelta(a, b) * sp.eye(2) / 4
        rhs += I * sum((eps(a, b, c) * T[c] for c in range(3)),
                       sp.zeros(2)) / 2
        assert sp.simplify(T[a] * T[b] - rhs) == sp.zeros(2)

# 2. Adjoint product rule:
# D_adj K^a = partial K^a - g eps^{abc} W^b K^c
#           = (D H)^dagger T^a G + H^dagger T^a D G.
Acomp = sp.symbols("A1 A2 A3", real=True)
A_mat = sum((Acomp[b] * T[b] for b in range(3)), sp.zeros(2))
h1, h2, gp1, gp2 = sp.symbols("h1 h2 gp1 gp2")
hp1, hp2 = sp.symbols("hp1 hp2")
G1, G2 = sp.symbols("G1 G2")
H = sp.Matrix([h1, h2])
Gv = sp.Matrix([G1, G2])
dH_partial = sp.Matrix([hp1, hp2])
dG_partial = sp.Matrix([gp1, gp2])
DH = dH_partial + I * g * A_mat * H
DG = dG_partial + I * g * A_mat * Gv

for a in range(3):
    K = (H.H * T[a] * Gv)[0]
    dK = (dH_partial.H * T[a] * Gv)[0] + (H.H * T[a] * dG_partial)[0]
    D_adj_K = dK - g * sum(
        eps(a, b, c) * Acomp[b] * (H.H * T[c] * Gv)[0]
        for b in range(3) for c in range(3)
    )
    product_rule = (DH.H * T[a] * Gv)[0] + (H.H * T[a] * DG)[0]
    assert sp.simplify(sp.expand_complex(D_adj_K - product_rule)) == 0

# 3. Matrix-ordered commutator contribution.
# F_mu and G_mu are arbitrary Hermitian matrices in u(2), allowing
# both hypercharge identity and SU(2) pieces.
f0s = sp.symbols("f01 f02 f03", real=True)
f1s = sp.symbols("f11 f12 f13", real=True)
g0s = sp.symbols("g01 g02 g03", real=True)
g1s = sp.symbols("g11 g12 g13", real=True)
b0, b1, c0, c1 = sp.symbols("b0 b1 c0 c1", real=True)
F0 = b0 * sp.eye(2) + sum((f0s[k] * T[k] for k in range(3)), sp.zeros(2))
F1 = b1 * sp.eye(2) + sum((f1s[k] * T[k] for k in range(3)), sp.zeros(2))
G0m = c0 * sp.eye(2) + sum((g0s[k] * T[k] for k in range(3)), sp.zeros(2))
G1m = c1 * sp.eye(2) + sum((g1s[k] * T[k] for k in range(3)), sp.zeros(2))
r1, r2 = sp.symbols("r1 r2")
d01, d02, d11, d12 = sp.symbols("d01 d02 d11 d12")
DrH = sp.Matrix([r1, r2])
D0H = sp.Matrix([d01, d02])
D1H = sp.Matrix([d11, d12])
w = sp.symbols("w", real=True)
C0 = I * (G0m * H + 2 * F0 * DrH)
C1 = I * (G1m * H + 2 * F1 * DrH)

for t_ext in [sp.eye(2)] + T:
    direct = -I * w / 2 * (
        (C0.H * t_ext * D1H)[0]
        + (D0H.H * t_ext * C1)[0]
        - (C1.H * t_ext * D0H)[0]
        - (D1H.H * t_ext * C0)[0]
    )
    ordered = -w / 2 * (
        (H.H * G0m * t_ext * D1H)[0]
        + (D1H.H * t_ext * G0m * H)[0]
        - (H.H * G1m * t_ext * D0H)[0]
        - (D0H.H * t_ext * G1m * H)[0]
    ) - w * (
        (DrH.H * F0 * t_ext * D1H)[0]
        + (D1H.H * t_ext * F0 * DrH)[0]
        - (DrH.H * F1 * t_ext * D0H)[0]
        - (D0H.H * t_ext * F1 * DrH)[0]
    )
    assert sp.simplify(sp.expand_complex(direct - ordered)) == 0

# 4. SU(2) delta/epsilon decomposition of the derivative-current bracket.
for a in range(3):
    for b in range(3):
        singlet_derivative = (H.H * D0H)[0] + (D0H.H * H)[0]
        lhs = (H.H * T[b] * T[a] * D0H)[0] + (D0H.H * T[a] * T[b] * H)[0]
        eps_current = 0
        for c in range(3):
            Ac = (H.H * T[c] * D0H)[0]
            Bc = (D0H.H * T[c] * H)[0]
            jc = I * (Ac - Bc)
            eps_current += eps(a, b, c) * jc
        rhs = sp.KroneckerDelta(a, b) * singlet_derivative / 4 - eps_current / 2
        assert sp.simplify(sp.expand_complex(lhs - rhs)) == 0

# 5. SU(2) delta/epsilon decomposition of the two-background F^2 bracket.
for a in range(3):
    for b in range(3):
        lhs = (DrH.H * T[b] * T[a] * D1H)[0] + (D1H.H * T[a] * T[b] * DrH)[0]
        symmetric = (DrH.H * D1H)[0] + (D1H.H * DrH)[0]
        eps_K = 0
        for c in range(3):
            Kc = I * (
                (D1H.H * T[c] * DrH)[0]
                - (DrH.H * T[c] * D1H)[0]
            )
            eps_K += eps(a, b, c) * Kc
        rhs = sp.KroneckerDelta(a, b) * symmetric / 4 + eps_K / 2
        assert sp.simplify(sp.expand_complex(lhs - rhs)) == 0

# 6. Derivative-of-f Higgs-EOM identity for singlet and adjoint insertions.
f0, f1 = sp.symbols("f0 f1", real=True)
for t_ext in [sp.eye(2)] + T:
    A0 = (H.H * t_ext * D0H)[0]
    B0 = (D0H.H * t_ext * H)[0]
    A1 = (H.H * t_ext * D1H)[0]
    B1 = (D1H.H * t_ext * H)[0]
    j0 = I * (A0 - B0)
    j1 = I * (A1 - B1)
    direct_df = I * w / 2 * (f0 * A1 + f1 * B0 - f1 * A0 - f0 * B1)
    eom_df = -w / 2 * (j0 * f1 - j1 * f0)
    assert sp.simplify(sp.expand_complex(direct_df - eom_df)) == 0

# 7. Hard coefficient reparameterization remains exact.
epsIR, LM = sp.symbols("eps_IR L_M")
aW = (12 / epsIR + 12 * LM + 25) / 288
bW = sp.Rational(1, 48)
retained = sp.factor(bW - aW / 2)
assert sp.simplify(
    retained + (12 / epsIR + 12 * LM + 13) / 576
) == 0

print("RC-001 QLD8 non-Abelian IBP/EOM algebra audit")
print("PASS 1: all SU(2) fundamental-generator products T^a T^b.")
print("PASS 2: adjoint product rule for H^dagger T^a G.")
print("PASS 3: matrix-ordered [D^2,D_mu] commutator formula for")
print("        singlet and SU(2)-adjoint external insertions.")
print("PASS 4: SU(2) derivative-current bracket decomposes into")
print("        delta^{ab} partial X / 4 - epsilon^{abc} j_H^c / 2.")
print("PASS 5: SU(2) two-background bracket decomposes into")
print("        delta^{ab} S_{rho nu} / 4 + epsilon^{abc} K_{rho nu}^c / 2.")
print("PASS 6: derivative-of-f Higgs-EOM identity for singlet and adjoint")
print("        external insertions.")
print("PASS 7: retained SU(2) hard coefficient is b_W-a_W/2.")
print("SCOPE: exact algebraic identities only; no loop integration,")
print("       complete current-basis reduction, counterterms, or")
print("       independent FeynArts/FeynCalc validation.")
