#!/usr/bin/env python3
"""Symbolic audit of the one-Higgs-doublet/one-complex-singlet scalar potential."""
import sympy as sp

v, vs, h, s, G0, a = sp.symbols("v v_s h s G0 a", real=True)
G1, G2, G3 = sp.symbols("G1 G2 G3", real=True)
muH2, muS2, lH, lS, lHS = sp.symbols("mu_H2 mu_S2 lambda_H lambda_S lambda_HS", real=True)

# H^dagger H and S^dagger S in a real-component parametrization.
H2 = (v+h)**2/2 + (G0**2+G1**2+G2**2)/2
S2 = ((vs+s)**2+a**2)/2
V = -muH2*H2 - muS2*S2 + lH*H2**2 + lS*S2**2 + lHS*H2*S2

tad_h = sp.diff(V,h).subs({h:0,s:0,G0:0,G1:0,G2:0,a:0})
tad_s = sp.diff(V,s).subs({h:0,s:0,G0:0,G1:0,G2:0,a:0})
muH_sol = sp.solve(sp.Eq(tad_h,0),muH2)[0]
muS_sol = sp.solve(sp.Eq(tad_s,0),muS2)[0]
assert sp.simplify(muH_sol-(lH*v**2+lHS*vs**2/2)) == 0
assert sp.simplify(muS_sol-(lS*vs**2+lHS*v**2/2)) == 0

subs_tad={muH2:muH_sol,muS2:muS_sol}
fields=(h,s)
M=sp.Matrix([[sp.diff(V,x,y).subs(subs_tad).subs({h:0,s:0,G0:0,G1:0,G2:0,a:0}) for y in fields] for x in fields])
M_expected=sp.Matrix([[2*lH*v**2,lHS*v*vs],[lHS*v*vs,2*lS*vs**2]])
assert all(sp.simplify(M[i,j]-M_expected[i,j])==0 for i in range(2) for j in range(2))

cubic={}
for key,inds in {
 "hhh":(h,h,h),"sss":(s,s,s),"hhs":(h,h,s),"hss":(h,s,s),
 "hG0G0":(h,G0,G0),"sG0G0":(s,G0,G0),"haa":(h,a,a),"saa":(s,a,a)
}.items():
    val=sp.diff(V,*inds).subs(subs_tad).subs({h:0,s:0,G0:0,G1:0,G2:0,a:0})
    cubic[key]=sp.simplify(val)

expected={
 "hhh":6*lH*v,"sss":6*lS*vs,"hhs":lHS*vs,"hss":lHS*v,
 "hG0G0":2*lH*v,"sG0G0":lHS*vs,"haa":lHS*v,"saa":2*lS*vs
}
for k in expected:
    assert sp.simplify(cubic[k]-expected[k])==0

# Quartic portal derivatives: h h s s and Goldstone pairs.
quartic_hhss=sp.diff(V,h,h,s,s).subs(subs_tad).subs({h:0,s:0,G0:0,G1:0,G2:0,a:0})
assert sp.simplify(quartic_hhss-lHS)==0

print("PASS: both tadpole equations.")
print("PASS: CP-even mass matrix and off-diagonal portal entry.")
print("PASS: hhh, sss, hhs, hss cubic vertices.")
print("PASS: electroweak and U(1)_X Goldstone cubic vertices.")
print("PASS: hhss portal quartic.")
print("LIMIT: tree-level potential algebra only; no loop renormalization or physical pole claim.")
