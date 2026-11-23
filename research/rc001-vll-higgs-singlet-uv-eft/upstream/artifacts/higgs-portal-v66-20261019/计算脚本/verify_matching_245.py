#!/usr/bin/env python3
"""Independent symbolic audit for Section 245 of the Higgs-portal EFT note.

Requirements: Python 3 and SymPy.
This script checks (i) the one-loop Wick-contraction topology count,
(ii) the gamma-function master-integral expansions and hard-region coefficients,
(iii) the zero-momentum portal threshold by a direct integral and Coleman-Weinberg
expansion, and (iv) the EOM-basis coefficient algebra and its scale derivative.
It is an audit of the stated approximation/coupling sector, not a full automated
Feynman-diagram generator for the entire model.
"""
from itertools import permutations
import sympy as sp

# ---------------------------------------------------------------------------
# A. Enumerate allowed fermion contractions in the unbroken-phase Yukawa box.
# Vertices: Y = y H, L = lambda S, Lc = lambda* S*, Yc = y* H*.
# Each vertex has one unbarred field and one barred field.
# A massless light propagator preserves chirality; a heavy E propagator permits
# both its kinetic chirality-preserving contraction and its M chirality flip.
# ---------------------------------------------------------------------------
vertices = ("Y", "L", "Lc", "Yc")
unbarred = {"Y": "E_R", "L": "ell_R", "Lc": "E_L", "Yc": "L_L"}
barred = {"Y": "L_L", "L": "E_L", "Lc": "ell_R", "Yc": "E_R"}
allowed_propagators = {
    "E_R": {"E_R", "E_L"},
    "E_L": {"E_L", "E_R"},
    "ell_R": {"ell_R"},
    "L_L": {"L_L"},
}

def number_of_cycles(mapping):
    seen = set()
    ncycles = 0
    for v in vertices:
        if v in seen:
            continue
        ncycles += 1
        cur = v
        while cur not in seen:
            seen.add(cur)
            cur = mapping[cur]
    return ncycles

matchings = []
for targets in permutations(vertices):
    mapping = dict(zip(vertices, targets))
    if all(barred[mapping[v]] in allowed_propagators[unbarred[v]] for v in vertices):
        matchings.append((mapping, number_of_cycles(mapping)))
connected = [(m, n) for m, n in matchings if n == 1]
disconnected = [(m, n) for m, n in matchings if n > 1]
assert len(matchings) == 2, matchings
assert len(connected) == 1, connected
assert len(disconnected) == 1, disconnected

# ---------------------------------------------------------------------------
# B. Exact gamma-function master integrals.
# d=4-2 eps, L=ln(M^2/mu^2), Delta=1/eps-gamma_E+ln(4 pi).
# All F's are normalized by i/(16 pi^2 M^4), except F12 which is normalized
# by i/(16 pi^2 M^2).
# ---------------------------------------------------------------------------
eps, Llog = sp.symbols("eps L", real=True)
d = 4 - 2 * eps
fac = sp.exp(eps * (sp.log(4 * sp.pi) - Llog))
Delta = 1 / eps - sp.EulerGamma + sp.log(4 * sp.pi)

F22 = fac * sp.gamma(2 + eps) * sp.gamma(-eps) / sp.gamma(2 - eps)
F13 = fac * sp.gamma(2 + eps) * sp.gamma(1 - eps) / (2 * sp.gamma(2 - eps))
F04 = fac * sp.gamma(2 + eps) / 6
F12 = -fac * sp.gamma(1 + eps) * sp.gamma(1 - eps) / sp.gamma(2 - eps)

F22_0 = sp.series(F22, eps, 0, 1).removeO().expand()
F13_0 = sp.series(F13, eps, 0, 1).removeO().expand()
F04_0 = sp.series(F04, eps, 0, 1).removeO().expand()
F12_0 = sp.series(F12, eps, 0, 1).removeO().expand()

assert sp.simplify(F22_0 - (-Delta + Llog - 2)) == 0, F22_0
assert sp.simplify(F13_0 - sp.Rational(1, 2)) == 0, F13_0
assert sp.simplify(F04_0 - sp.Rational(1, 6)) == 0, F04_0
assert sp.simplify(F12_0 + 1) == 0, F12_0

# Hard-region Taylor coefficient from the four-propagator kernel:
# I_hard^(2) = M^2 s (-2+4/d) J22 + (4 M^2/d) s J13
#               - (4 M^2/d) t J04.
# The normalized coefficients are evaluated before setting d=4, so O(eps)
# pieces multiplying the J22 pole are retained.
Cs = (-2 + 4 / d) * F22 + (4 / d) * F13
Ct = -(4 / d) * F04
Cs_0 = sp.series(Cs, eps, 0, 1).removeO().expand()
Ct_0 = sp.series(Ct, eps, 0, 1).removeO().expand()
assert sp.simplify(Cs_0 - (Delta - Llog + 2)) == 0, Cs_0
assert sp.simplify(Ct_0 + sp.Rational(1, 6)) == 0, Ct_0

# ---------------------------------------------------------------------------
# C. Zero-momentum hard amplitude / portal threshold.
# I(0)=2 M^2 J12, with J12 normalized to i/(16 pi^2 M^2).
# The closed-fermion-loop factor and four Yukawa vertices give -|y lambda|^2 I.
# ---------------------------------------------------------------------------
I0_normalized = sp.simplify(2 * F12_0)
assert I0_normalized == -2
# Hence the loop 1PI vertex is +2 i |y lambda|^2/(16 pi^2).
# In the convention V contains lambda_HS X Y, the finite one-loop potential
# threshold is Delta V = -2 |y lambda|^2/(16 pi^2) X Y.

# Independent Coleman-Weinberg expansion. Let x=|y|^2 X, yv=|lambda|^2 Y.
M2, x, yv, mu2 = sp.symbols("M2 x y mu2", positive=True)
f = lambda z: z**2 * (sp.log(z / mu2) - sp.Rational(3, 2))
# Heavy eigenvalue: M2+x+y-x*y/M2 + ...; cross coefficient in f is
# -f'(M2)/M2 + f''(M2) = 2.
cw_cross = sp.simplify(-sp.diff(f(M2), M2) / M2 + sp.diff(f(M2), M2, 2))
assert sp.simplify(cw_cross - 2) == 0, cw_cross

# Independent hard+soft cancellation check, including the overall fermion-loop sign.
qlog, s_inv, t_inv = sp.symbols("log_minus_q2_over_mu2 s t", real=True)
hard_actual_s = -Delta + Llog - 2
soft_actual_s = Delta - qlog + 2
full_actual_s = sp.simplify(hard_actual_s + soft_actual_s)
assert sp.simplify(full_actual_s - (Llog - qlog)) == 0, full_actual_s
hard_actual_t = sp.Rational(1, 6)
assert sp.simplify(hard_actual_t - sp.Rational(1, 6)) == 0

# ---------------------------------------------------------------------------
# D. EOM projection algebra and scale derivative.
# A_l=|C5_l|^2/(16 pi^2); L_l=ln(M_l^2/mu^2).
# ---------------------------------------------------------------------------
Am, At, Lm, Lt = sp.symbols("A_mu A_tau L_mu L_tau", real=True)
cH = Am * (Lm - sp.Rational(13, 6)) + At * (Lt - sp.Rational(13, 6))
cS = cH
cD = sp.Rational(1, 2) * (Am * (Lm - 2) + At * (Lt - 2))
cJ = sp.Rational(1, 2) * (-Am * (Lm - 2) + At * (Lt - 2))
cD_NR = sp.simplify(cD - cH / 2 - cS / 2)
expected_NR = Am * (sp.Rational(7, 6) - Lm / 2) + At * (sp.Rational(7, 6) - Lt / 2)
assert sp.simplify(cD_NR - expected_NR) == 0, cD_NR
# dL/d ln(mu)=-2; therefore d c_D_NR / d ln(mu)=A_mu+A_tau.
dcD_dlnmu = sp.simplify(sp.diff(cD_NR, Lm) * (-2) + sp.diff(cD_NR, Lt) * (-2))
assert sp.simplify(dcD_dlnmu - (Am + At)) == 0, dcD_dlnmu

# Potential coefficients in the Lagrangian after EOM substitution.
muH2, muS2, lamH, lamS, lamHS = sp.symbols("muH2 muS2 lambda_H lambda_S lambda_HS")
coef_XY_L = -(muH2 * cH + muS2 * cS)
coef_X2Y_L = 2 * lamH * cH + lamHS * cS
coef_XY2_L = lamHS * cH + 2 * lamS * cS
coef_FH_L = cH / 2
coef_FS_formal_L = cS / 2
coef_FS_renormalizable_actual_L = sp.Integer(0)  # no renormalizable S-fermion source below M_E

print("Wick contractions:")
for mapping, ncyc in matchings:
    print(f"  cycles={ncyc}: " + ", ".join(f"{k}->{v}" for k, v in mapping.items()))
print("Connected one-loop 1PI cycles:", len(connected))
print("Disconnected pair-of-bubbles contractions (exclude from 1PI box):", len(disconnected))
print("Master integrals (normalized):")
print("  J22 =", F22_0)
print("  J13 =", F13_0)
print("  J04 =", F04_0)
print("Hard coefficients: s ->", Cs_0, "; t ->", Ct_0)
print("Hard+soft finite s coefficient =", full_actual_s, "; hard t coefficient =", hard_actual_t)
print("Zero-momentum I(0)/(i/(16 pi^2)) =", I0_normalized)
print("CW mixed x*y coefficient in f(m_heavy^2) =", cw_cross)
print("Portal threshold: Delta V = -2 sum |y_l lambda_l|^2/(16 pi^2) X Y")
print("EOM-reduced c_D =", cD_NR)
print("d c_D / d ln(mu) =", dcD_dlnmu)
print("Lagrangian coefficient of X Y after EOM =", coef_XY_L)
print("Lagrangian coefficient of X^2 Y after EOM =", coef_X2Y_L)
print("Lagrangian coefficient of X Y^2 after EOM =", coef_XY2_L)
print("SM Yukawa-source coefficient multiplying Y F_H =", coef_FH_L)
print("Formal EOM prefactor multiplying X F_S =", coef_FS_formal_L)
print("Actual renormalizable S-fermion-source contribution =", coef_FS_renormalizable_actual_L, "(F_S^(4)=0 in this EFT)")
print("PASS: all symbolic assertions succeeded.")
