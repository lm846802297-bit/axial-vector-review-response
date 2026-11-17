#!/usr/bin/env python3
"""A4d exact p_E^2=0 tadpole-improved ss-kernel identity."""
import sympy as sp

d, xi, gA, mX, lamS, vS = sp.symbols(
    "d xi g_A m_X lambda_S v_S", positive=True
)
p2 = sp.symbols("p_E2", real=True)
Am, Axi, As = sp.symbols("A_m A_xi A_s")
Bm, Bxi, Bs = sp.symbols("B_m B_xi B_s")

# Pi_ss,E(0), with all terms normalized to the common 1/(16 pi^2).
vector_seagull = gA**2*((d-1)*Am + xi*Axi)
vector_bubble = -2*gA**2*mX**2*((d-1)*Bm + xi**2*Bxi)
mixed_Aa = -xi*gA**2*(Axi - xi*mX**2*Bxi)
ghost_bubble = xi**2*gA**2*mX**2*Bxi
goldstone_seagull = lamS*Axi
goldstone_bubble = -2*lamS**2*vS**2*Bxi
radial_seagull = 3*lamS*As
radial_bubble = -18*lamS**2*vS**2*Bs

pi0 = sp.expand(
    vector_seagull + vector_bubble + mixed_Aa + ghost_bubble
    + goldstone_seagull + goldstone_bubble
    + radial_seagull + radial_bubble
)

# One-loop tadpole divided by v_S. Longitudinal-vector and ghost
# one-point functions have already cancelled in T_s.
tadpole_over_v = gA**2*(d-1)*Am + lamS*Axi + 3*lamS*As

improved = sp.factor(pi0 - tadpole_over_v)
expected = sp.factor(
    -2*(d-1)*gA**2*mX**2*Bm
    -2*lamS**2*vS**2*Bxi
    -18*lamS**2*vS**2*Bs
)
assert sp.simplify(improved-expected)==0

# UV pole: all B_E functions have unit UV pole.
uv = sp.factor(
    (-2*(d-1)*gA**2*mX**2)
    -2*lamS**2*vS**2
    -18*lamS**2*vS**2
)
assert sp.simplify(uv - (-2*(d-1)*gA**2*mX**2-20*lamS**2*vS**2))==0

# In four dimensions.
uv_d4 = sp.factor(uv.subs(d,4))



# Momentum-dependent tadpole-improved UV pole in d=4.
# T_s/v_S has UV coefficient:
uv_tadpole_over_v = -3*gA**2*mX**2 - xi*lamS*mX**2 - 6*lamS**2*vS**2
uv_full_pole_d4 = (
    -gA**2*(3-xi)*p2 - 9*gA**2*mX**2
    -xi*lamS*mX**2 - 26*lamS**2*vS**2
)
uv_improved_pole_d4 = sp.factor(uv_full_pole_d4-uv_tadpole_over_v)
expected_improved_pole_d4 = (
    -gA**2*(3-xi)*p2 - 6*gA**2*mX**2 - 20*lamS**2*vS**2
)
assert sp.simplify(uv_improved_pole_d4-expected_improved_pole_d4)==0

print("A4d exact tadpole-improved zero-momentum identity")
print(f"  Pi_ss,E(0) - T_s^(1)/v_S = {expected}/(16 pi^2)")
print("  All A_E seagulls cancel against the corresponding tadpole term.")
print("  The xi_X-dependent longitudinal-vector + ghost + mixed sector cancels.")
print(f"  UV pole at general d: {uv}/(16 pi^2 epsbar)")
print(f"  UV pole at d=4: {uv_d4}/(16 pi^2 epsbar)")
print("PASS: exact cancellation identity for arbitrary xi_X.")
print("PASS: the tadpole-improved p_E^2=0 UV pole is gauge independent.")
print(f"  Momentum-dependent UV pole after tadpole improvement (d=4): {expected_improved_pole_d4}/epsbar")
print("PASS: local mass pole is xi_X-independent; only the field pole retains (3-xi_X).")
print("LIMIT: p_E^2=0 identity only; it does not replace the full momentum-dependent pole calculation.")
