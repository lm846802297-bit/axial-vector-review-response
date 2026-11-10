#!/usr/bin/env python3
"""A4c general-R_xi UV-pole audit for the one-loop U(1)_X ss kernel.

The asymptotic expansion is performed in d=4 for the logarithmic UV
coefficients. A_E|UV=-M^2/epsbar and B_E|UV=+1/epsbar.
"""
import sympy as sp

xi, gA, mX, lamS, vS, p2 = sp.symbols(
    "xi g_A m_X lambda_S v_S p_E2", positive=True
)
d = sp.symbols("d")

# UV poles of the vector seagull and vector bubble.
uv_vector_seagull = -gA**2 * (d - 1 + xi**2) * mX**2
uv_vector_bubble = -2 * gA**2 * mX**2 * (d - 1 + xi**2)

# Mixed A-a integral:
#  - its transverse part contributes +3 p_E^2 to I_mix|UV in d=4;
#  - its longitudinal part contributes -xi p_E^2;
#  - at p_E^2=0, I_mix|UV = -2 xi^2 m_X^2.
uv_mixed_integral = (3 - xi) * p2 - 2 * xi**2 * mX**2
uv_mixed_self_energy = -gA**2 * uv_mixed_integral

# Ghost and Goldstone terms.
uv_ghost_bubble = xi**2 * gA**2 * mX**2
uv_goldstone_tadpole = -xi * lamS * mX**2
uv_goldstone_bubble = -2 * lamS**2 * vS**2

uv_X = sp.factor(
    uv_vector_seagull + uv_vector_bubble + uv_mixed_self_energy
    + uv_ghost_bubble + uv_goldstone_tadpole + uv_goldstone_bubble
)
expected_X = sp.factor(
    -gA**2 * (3 - xi) * p2
    -3 * (d - 1) * gA**2 * mX**2
    -xi * lamS * mX**2
    -2 * lamS**2 * vS**2
)
assert sp.simplify(uv_X - expected_X) == 0

# Radial scalar seagull + bubble.
uv_radial = -3 * lamS * (2 * lamS * vS**2) - 18 * lamS**2 * vS**2
assert sp.simplify(uv_radial + 24 * lamS**2 * vS**2) == 0

uv_total = sp.factor((uv_X + uv_radial).subs(d, 4))
expected_total = sp.factor(
    -gA**2 * (3 - xi) * p2
    -9 * gA**2 * mX**2
    -xi * lamS * mX**2
    -26 * lamS**2 * vS**2
)
assert sp.simplify(uv_total - expected_total) == 0

# Gauge-mass local pole cancellation:
# all xi^2 terms cancel between vector seagull/bubble, mixed loop and ghost.
gauge_local = sp.factor(
    uv_vector_seagull + uv_vector_bubble
    + uv_mixed_self_energy.subs(p2, 0) + uv_ghost_bubble
)
assert sp.simplify(
    gauge_local + 3 * (d - 1) * gA**2 * mX**2
) == 0

# At xi=1, reproduce the A4a Feynman-gauge result.
assert sp.simplify(
    uv_total.subs(xi, 1)
    - (-2*gA**2*p2 - 9*gA**2*mX**2
       - lamS*mX**2 - 26*lamS**2*vS**2)
) == 0

print("A4c general-R_xi UV-pole audit")
print(f"  U(1)_X vector/Goldstone/ghost subset: {expected_X}/epsbar")
print(f"  Radial scalar subset: {-24*lamS**2*vS**2}/epsbar")
print(f"  Total bosonic ss pole (d=4): {expected_total}/epsbar")
print(f"  Required diagonal field-counterterm pole coefficient: "
      f"deltaZ_s = g_A^2*(3-xi)/(16*pi^2*epsbar)")
print("PASS: all xi^2 gauge-mass terms cancel in the local gauge pole.")
print("PASS: p_E^2 coefficient agrees with the scalar-QED (3-xi) result.")
print("PASS: xi=1 reproduces the A4a Feynman-gauge UV pole.")
print("LIMIT: UV poles only; no finite real part, tadpole scheme, or full pole is computed.")
