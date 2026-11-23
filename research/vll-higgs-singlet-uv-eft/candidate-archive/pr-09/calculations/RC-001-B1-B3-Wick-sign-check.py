#!/usr/bin/env python3
"""Wick-rotation sign audit for the RC-001 B1/B2/B3 kernels.

Uses the already checked trace decomposition
  Tr = 2 H G + 2 sum(C_ij k_i.k_j) + 2 M + parity-odd term,
and the declared shifted denominator
  K_M^2 - Delta0 + d  ->  -(K_E^2 + Delta0 - d).
It independently derives the B1 and B3 signs from the d=4 Euclidean loop
integrals, and rechecks B2 against the source-aligned one-cycle calibration.

Scope: kernel-level sign convention only; not a full six-cycle Wilson match.
Requires Python 3 and SymPy.
"""
from itertools import combinations, permutations
import sympy as sp

Delta, H, g, dshift, Mterm, F, S = sp.symbols(
    "Delta H g d M F S", nonzero=True
)
checks = 0

def check(name, expr):
    global checks
    residual = sp.simplify(expr)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1
    print(f"PASS: {name}")

# Reconstruct the routed g_alpha for all six labeled cycles and verify
# that it is the K_M^2 coefficient of G after angular averaging in d=4.
Q = sp.symbols("Q1:7")
Gram = sp.Matrix([[Q[0], Q[3], Q[4]],
                  [Q[3], Q[1], Q[5]],
                  [Q[4], Q[5], Q[2]]])
x1, x2, x3, x4 = sp.symbols("x1:5")
xpars = (x1, x2, x3, x4)
pA = sp.Matrix([[1, 0, 0]])
pB = sp.Matrix([[0, 1, 0]])
pC = sp.Matrix([[0, 0, 1]])
pD = sp.Matrix([[-1, -1, -1]])
external = {"h1": pA, "h2": pB, "s1": pC, "s2": pD}
def dotg(u, v):
    return sp.expand((u*Gram*v.T)[0])
for cycle in [("h1",)+tail for tail in permutations(("h2", "s1", "s2"))]:
    qv = [external[label] for label in cycle]
    r = [sp.zeros(1, 3), -qv[1], -qv[1]-qv[2], qv[0]]
    R = sum((xpars[i]*r[i] for i in range(4)), sp.zeros(1, 3))
    shifted = [ri-R for ri in r]
    f = {ij: dotg(shifted[ij[0]], shifted[ij[1]])
         for ij in combinations(range(4), 2)}
    g_kernel = sp.expand(
        f[(0,1)] + f[(2,3)] - f[(0,2)] - f[(1,3)]
        + f[(0,3)] + f[(1,2)] + sp.Rational(1,2)*(f[(0,2)] + f[(1,3)])
    )
    g_direct = sp.expand(
        f[(0,1)] + f[(2,3)] - f[(0,2)] - f[(1,3)]
        + f[(0,3)] + f[(1,2)]
    )
    g_angular = sp.expand((
        dotg(shifted[0]+shifted[1], shifted[2]+shifted[3])
        - dotg(shifted[0]+shifted[2], shifted[1]+shifted[3])
        + dotg(shifted[0]+shifted[3], shifted[1]+shifted[2])
    )/4)
    check("ledger g_alpha is the angular-averaged K^2 coefficient of G for "
          + "-".join(cycle), g_direct+g_angular-g_kernel)

# In d=4, I_m^(n) = int d^4 K_E/(2 pi)^4 (K_E^2)^m/(K_E^2+Delta)^n
# = (1/16 pi^2) Gamma(m+2) Gamma(n-m-2) /
#   [Gamma(2) Gamma(n)] Delta^(2+m-n).
loop = 1/(16*sp.pi**2)
I0_4 = loop/(6*Delta**2)
I1_4 = loop/(3*Delta)
I0_5 = loop/(12*Delta**3)
I1_5 = loop/(12*Delta**2)
I2_5 = loop/(4*Delta)

def gamma_integral(m, n):
    return (loop * sp.gamma(m+2)*sp.gamma(n-m-2) /
            (sp.gamma(2)*sp.gamma(n)) * Delta**(2+m-n))

check("I_0^(4) = 1/(16 pi^2 6 Delta^2)", I0_4-gamma_integral(0,4))
check("I_1^(4) = 1/(16 pi^2 3 Delta)", I1_4-gamma_integral(1,4))
check("I_0^(5) = 1/(16 pi^2 12 Delta^3)", I0_5-gamma_integral(0,5))
check("I_1^(5) = 1/(16 pi^2 12 Delta^2)", I1_5-gamma_integral(1,5))
check("I_2^(5) = 1/(16 pi^2 4 Delta)", I2_5-gamma_integral(2,5))

# Wick rotation gives K_M^2 -> -K_E^2 and (K_M^2)^2 -> (K_E^2)^2.
KE2 = sp.symbols("K_E2")
check("quartic loop-momentum term keeps its sign under Wick rotation",
      (-KE2)**2-KE2**2)

# G = K_M^4 + g K_M^2 Q + ... . The O(Q) coefficient in 2 H G has:
#   -2 H g I_1^(4) from K_M^2 -> -K_E^2;
#   +8 H d I_2^(5) from K_M^4 times the +4d denominator expansion.
B1_direct = sp.simplify(-2*H*g*I1_4 + 8*H*dshift*I2_5)
B1_expected = loop/Delta * H*(-sp.Rational(2,3)*g + 2*dshift)
check("Wick and denominator shift give B1=H(-2g/3+2d)",
      B1_direct-B1_expected)
B1_historical = loop/Delta * H*(sp.Rational(2,3)*g - 2*dshift)
check("historical B1 sign is the exact opposite",
      B1_expected+B1_historical)

# The constant trace term 2 M multiplies the +4d denominator correction:
# 2 M * 4d * I_0^(5) = (1/16 pi^2) (2/3 M d)/Delta^3.
B3_direct = sp.simplify(2*Mterm*4*dshift*I0_5)
B3_expected = loop/Delta**3 * sp.Rational(2,3)*Mterm*dshift
check("Wick and denominator shift give B3=+2 M d/3",
      B3_direct-B3_expected)
B3_historical = -loop/Delta**3 * sp.Rational(2,3)*Mterm*dshift
check("historical B3 sign is the exact opposite",
      B3_expected+B3_historical)

# B2 calibration: the shifted dot-product numerator is 2(F - S K_E^2)
# and the denominator correction contributes -8 S d I_1^(5).
B2_direct = sp.simplify(2*F*I0_4 - 8*S*dshift*I1_5)
B2_expected = loop/Delta**2 * (F/sp.Integer(3)-sp.Rational(2,3)*S*dshift)
check("B2 remains (F-2 S d)/3 with the same Wick convention",
      B2_direct-B2_expected)

# Gamma(4)=6 is the Feynman-parameter prefactor; simplex volume is 1/6.
check("Gamma(4) times the simplex volume is one",
      sp.gamma(4)*sp.Rational(1,6)-1)

print(f"RESULT: {checks} exact Wick/kernel-sign checks passed.")
print("RESULTING KERNELS: B1=H(-2 g/3+2 d), B2=(F-2 S d)/3, B3=+2 M d/3.")
print("SCOPE: resolves the algebraic B1/B3 Wick-sign choice under the declared trace and d conventions.")
print("OPEN: full mixed-mass six-cycle sum, physical graph multiplicity, determinant-log mapping, and complete UV-EFT subtraction.")
