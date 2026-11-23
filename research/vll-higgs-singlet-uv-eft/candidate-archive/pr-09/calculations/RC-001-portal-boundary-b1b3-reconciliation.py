#!/usr/bin/env python3
"""Exact algebra checks for the RC-001 portal boundary and legacy B1/B3 audit.

This script verifies formulas and convention mappings already written in the
frozen research record. It does NOT calculate a loop integral, regenerate the
complete labeled UV amplitude, perform the full EFT subtraction, or resolve
the physical B1/B3 sign question.
Requires Python 3 and SymPy.
"""
import sympy as sp

checks = []

def check(name, expr, expected=0):
    residual = sp.simplify(expr - expected)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks.append(name)
    print(f"PASS: {name}")

# A. One-loop, zero-momentum portal matching in the recorded potential convention.
y_mu, lam_mu, y_tau, lam_tau = sp.symbols(
    "y_mu lambda_mu y_tau lambda_tau", positive=True
)
lambda_uv, v_h, v_s = sp.symbols("lambda_HS_UV v_h v_s", real=True)
sum_yukawa = y_mu**2 * lam_mu**2 + y_tau**2 * lam_tau**2
delta_lambda = -sum_yukawa / (8 * sp.pi**2)
lambda_eft = lambda_uv + delta_lambda

check("portal matching relation is UV boundary plus finite threshold",
      lambda_eft - (lambda_uv - sum_yukawa / (8 * sp.pi**2)))
check("UV-zero boundary leaves the negative finite EFT threshold",
      lambda_eft.subs(lambda_uv, 0) - delta_lambda)
lambda_uv_for_eft_zero = sp.solve(sp.Eq(lambda_eft, 0), lambda_uv)[0]
check("EFT-zero benchmark requires the positive UV boundary",
      lambda_uv_for_eft_zero - sum_yukawa / (8 * sp.pi**2))

# Under Gamma_inv = p^2 I - M_loc^2 + Pi, the potential-Hessian
# threshold and the source-convention hard Pi(0) have opposite signs.
delta_M_hs_sq = v_h * v_s * delta_lambda
Pi_hs_hard_0 = -v_h * v_s * delta_lambda
check("potential Hessian and hard Pi(0) are opposite in the stated convention",
      delta_M_hs_sq + Pi_hs_hard_0)

# B. The documented 4/3 difference is an old on-shell representative issue.
a, L = sp.symbols("a L", real=True)
cH_old = a * (L - sp.Rational(13, 6))
cS_old = cH_old
cD_old = a * (L - 2) / 2
cH_off = a * (L - sp.Rational(3, 2))
cS_off = cH_off
cD_off = a * (L - sp.Rational(2, 3)) / 2
check("off-shell/EOM completion shifts c_H by 2a/3", cH_off - cH_old - 2*a/3)
check("off-shell/EOM completion shifts c_S by 2a/3", cS_off - cS_old - 2*a/3)
check("off-shell/EOM completion shifts c_D by 2a/3", cD_off - cD_old - 2*a/3)
check("EOM-reduced derivative combination is invariant",
      (cD_off - (cH_off + cS_off)/2)
      - (cD_old - (cH_old + cS_old)/2))

# C. Compare the legacy candidate B kernels to the kernel obtained from the
# explicitly stated Minkowski numerator + Wick-rotation assumptions in §84.
# The algebraic sign flip is real; it is NOT, by itself, a physical verdict.
H, g, d, F, S, M = sp.symbols("H g d F S M", real=True)
B1_legacy = H * (sp.Rational(2, 3) * g - 2*d)
B1_wick = H * (-sp.Rational(2, 3) * g + 2*d)
B2_legacy = sp.Rational(1, 3) * F - sp.Rational(2, 3) * S*d
B2_wick = sp.Rational(1, 3) * F - sp.Rational(2, 3) * S*d
B3_legacy = -sp.Rational(2, 3) * M*d
B3_wick = sp.Rational(2, 3) * M*d
check("B1 candidate definitions are algebraic negatives under the same d convention",
      B1_wick + B1_legacy)
check("B2 candidate definition is unchanged under that comparison",
      B2_wick - B2_legacy)
check("B3 candidate definitions are algebraic negatives under the same d convention",
      B3_wick + B3_legacy)

# Denominator convention check: D_M = K_M^2 - Delta_0 + deltaDelta.
# With K_M^2 = -K_E^2, D_M = -(K_E^2 + Delta_0 - deltaDelta).
K_E2, Delta0, deltaDelta = sp.symbols(
    "K_E2 Delta0 deltaDelta", positive=True
)
D_M_after_wick = (-K_E2) - Delta0 + deltaDelta
A_E = K_E2 + Delta0
check("Minkowski denominator maps to -(K_E^2 + Delta0 - deltaDelta)",
      D_M_after_wick + (A_E - deltaDelta))
expanded = sp.series(1 / (A_E - deltaDelta)**4, deltaDelta, 0, 2).removeO()
check("corrected Euclidean n=4 denominator has +4 deltaDelta term",
      expanded - (A_E**-4 + 4*deltaDelta*A_E**-5))

# D. Fixed-sector hard/soft log bookkeeping from §248.
s, t = sp.symbols("s t", real=True)
ell_s, eps = sp.symbols("ell_s eps", real=True)
Delta_IR, Delta_UV = sp.symbols("Delta_IR Delta_UV", real=True)
hard = (-Delta_IR + L - 2) * s + t/6
soft = (Delta_UV - ell_s + 2) * s
check("hard plus soft cancels the matching pole residues and finite constants",
      hard.subs(Delta_IR, eps) + soft.subs(Delta_UV, eps)
      - (L - ell_s)*s - t/6)

print(f"RESULT: {len(checks)} exact symbolic checks passed.")
print("STATUS: portal boundary alternatives and sign bookkeeping are verified algebraically.")
print("STATUS: the historical B1/B3 physical sign remains UNRESOLVED.")
print("LIMIT: no loop integration, complete external-leg sum, counterterm closure,")
print("       or end-to-end FeynArts/FeynCalc calculation was performed.")
