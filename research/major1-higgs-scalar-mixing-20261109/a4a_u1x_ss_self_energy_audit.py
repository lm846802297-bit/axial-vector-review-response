#!/usr/bin/env python3
"""A4a one-loop ss self-energy audit for the Abelian-Higgs U(1)_X sector.

Conventions:
  gA = 2 gX = mX/vS
  d = 4 - 2 eps
  Gamma_E^(2) = p_E^2 + m_s^2 + Pi_E
  A_E(M2) = 16 pi^2 mu^(2 eps) int_E d^d k/(2 pi)^d 1/(k^2+M2)
  B_E = 16 pi^2 mu^(2 eps) int_E d^d k/(2 pi)^d 1/(D1 D2)
Thus A_E|UV = -M2/epsbar and B_E|UV = +1/epsbar.

The script verifies the symbolic identities and reproduces the physical
s -> A' A' width from the sum of gauge-fixed cuts in Feynman gauge.
It does not evaluate the scheme-dependent real finite part or solve poles.
"""
import math
import sympy as sp

# ---------------------------------------------------------------------------
# Symbolic checks
# ---------------------------------------------------------------------------
d = sp.symbols("d")
s2, vS, mX, gA, lamS, xi, pE2 = sp.symbols(
    "s2 v_S m_X g_A lambda_S xi p_E2", positive=True
)
Axi, Bxi = sp.symbols("A_xi B_xi")

# At p_E^2=0 and lambda_S=0, unphysical longitudinal-vector, mixed A-a,
# and ghost contributions cancel for arbitrary xi.
long_vector_tadpole = xi * gA**2 * Axi
long_vector_bubble = -2 * xi**2 * gA**2 * mX**2 * Bxi
ghost_bubble = xi**2 * gA**2 * mX**2 * Bxi
mixed_Aa_p0 = -xi * gA**2 * (Axi - xi * mX**2 * Bxi)
assert sp.simplify(
    long_vector_tadpole + long_vector_bubble + ghost_bubble + mixed_Aa_p0
) == 0

# The longitudinal-vector and U(1)_X ghost one-point functions cancel.
vector_long_tadpole = gA * mX * xi * Axi
ghost_tadpole = -xi * gA * mX * Axi
assert sp.simplify(vector_long_tadpole + ghost_tadpole) == 0

# Mixed A-a numerator reduction:
# (k-p)^2 = 2(k^2+m^2) - ((k+p)^2+m^2) + 2 p^2 - m^2.
k2, kp, p2, m2 = sp.symbols("k2 kp p2 m2")
D1 = k2 + m2
D2 = k2 + 2 * kp + p2 + m2
numerator = k2 - 2 * kp + p2
assert sp.simplify(numerator - (2 * D1 - D2 + 2 * p2 - m2)) == 0

# Feynman-gauge on-shell cut sum. The coefficients multiply pi*beta/(16 pi^2).
C_vector = -2 * 4 * gA**2 * mX**2
C_mixed = gA**2 * (2 * s2 + mX**2)
C_ghost = gA**2 * mX**2
C_goldstone = -2 * lamS**2 * vS**2
C_total = sp.factor(
    (C_vector + C_mixed + C_ghost + C_goldstone).subs(
        {gA: mX / vS, lamS: s2 / (2 * vS**2)}
    )
)
C_expected = -s2**2 / (2 * vS**2) * (
    1 - 4 * mX**2 / s2 + 12 * mX**4 / s2**2
)
assert sp.simplify(C_total - C_expected) == 0

# Feynman-gauge UV pole for X-vector + Goldstone + ghost subset.
uv_X = sp.factor(
    -((d - 1) * gA**2 + lamS) * mX**2
    - (2 * gA**2 * pE2
       + 2 * (d - 1) * gA**2 * mX**2
       + 2 * lamS**2 * vS**2)
)
uv_X_d4 = sp.factor(uv_X.subs(d, 4))
uv_radial = -3 * lamS * (2 * lamS * vS**2) - 18 * lamS**2 * vS**2
assert sp.simplify(uv_radial + 24 * lamS**2 * vS**2) == 0

# ---------------------------------------------------------------------------
# Numerical optical-theorem check
# ---------------------------------------------------------------------------
benchmarks = {
    "A": {"vS": 70.886458, "mX": 10.0},
    "B": {"vS": 315.0, "mX": 63.0},
}
scan_masses = (10.0, 100.0, 125.25, 150.0)

def direct_vector_width(ms, vS_value, mX_value):
    if ms <= 2.0 * mX_value:
        return 0.0
    x = (mX_value / ms) ** 2
    beta = math.sqrt(1.0 - 4.0 * x)
    return (
        ms**3 / (32.0 * math.pi * vS_value**2)
        * (1.0 - 4.0 * x + 12.0 * x**2)
        * beta
    )

def cut_width_from_self_energy(ms, vS_value, mX_value):
    if ms <= 2.0 * mX_value:
        return 0.0
    s_value = ms**2
    x = mX_value**2 / s_value
    beta = math.sqrt(1.0 - 4.0 * x)
    g = mX_value / vS_value
    lam = s_value / (2.0 * vS_value**2)  # m_s^2 = 2 lambda_S v_S^2

    c_vector = -8.0 * g**2 * mX_value**2
    c_mixed = g**2 * (2.0 * s_value + mX_value**2)
    c_ghost = g**2 * mX_value**2
    c_goldstone = -2.0 * lam**2 * vS_value**2
    c_sum = c_vector + c_mixed + c_ghost + c_goldstone

    # In Gamma_E convention: Im Pi_E(-m_s^2-i0) = c_sum beta/(16 pi),
    # and Gamma(s -> A'A') = -Im Pi_E/m_s.
    im_pi_magnitude = -c_sum * beta / (16.0 * math.pi)
    return im_pi_magnitude / ms

print("A4a symbolic checks:")
print("  PASS: general-xi p_E^2=0 cancellation of unphysical longitudinal sector.")
print("  PASS: longitudinal-vector / ghost tadpole cancellation.")
print("  PASS: mixed A-a numerator reduction to A_E and B_E.")
print("  PASS: Feynman-gauge optical-theorem identity.")
print(f"  UV pole X+Goldstone+ghost (d=4): {uv_X_d4}/epsbar")
print(f"  UV pole radial-scalar subset: {sp.factor(uv_radial)}/epsbar")

print("\nA4a Feynman-gauge cut validation")
print("All widths in GeV; closed channels are exactly zero.")
for name, pars in benchmarks.items():
    vS_value, mX_value = pars["vS"], pars["mX"]
    gX_value = mX_value / (2.0 * vS_value)
    print(f"\nBenchmark {name}: vS={vS_value:.9f}, mX={mX_value:.6g}, "
          f"gX={gX_value:.9g}, gA={mX_value/vS_value:.9g}")
    print("m_s       Gamma_from_cut       Gamma_direct        relative_residual")
    for ms in scan_masses:
        w_cut = cut_width_from_self_energy(ms, vS_value, mX_value)
        w_dir = direct_vector_width(ms, vS_value, mX_value)
        if w_dir == 0.0:
            assert w_cut == 0.0
            residual = 0.0
        else:
            residual = abs(w_cut - w_dir) / w_dir
            assert residual < 5e-14
        print(f"{ms:7.2f}  {w_cut:18.11e}  {w_dir:18.11e}  {residual:18.11e}")

    ms_max = math.sqrt(8.0 * math.pi) * vS_value
    w_max = direct_vector_width(ms_max, vS_value, mX_value)
    print(f"perturbative cap m_s,max={ms_max:.9f} GeV; "
          f"Gamma_AA/m_s={w_max/ms_max:.9f}")

print("\nPASS: cut-derived width agrees with the independent tree-level vector width.")
print("LIMIT: no scheme-dependent real finite part, complete tadpole scheme, or complex pole is evaluated.")
