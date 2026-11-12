#!/usr/bin/env python3
"""Symbolic A2 audit for the Higgs--radial-singlet R_xi vertex ledger.

This script checks the scalar-potential cubic/quartic derivatives, gauge-boson
mass-term vertices, and scalar-dependent Faddeev--Popov entries in the
gauge basis. It intentionally does not claim to generate every non-Abelian
ghost-vector vertex or to calculate loop integrals.
"""
import sympy as sp
from itertools import combinations_with_replacement

h,s,G0,Gp,Gm,a = sp.symbols("h s G0 Gp Gm a")
v,vs = sp.symbols("v v_s", positive=True)
lamH,lamS,lamHS = sp.symbols("lambda_H lambda_S lambda_HS")
mW,mZ,mX = sp.symbols("m_W m_Z m_X", positive=True)
xiW,xiZ,xiX = sp.symbols("xi_W xi_Z xi_X")
Wm,Wp,Z,Xv = sp.symbols("Wm Wp Z A_X")
cbW,bcbW,cbZ,bcbZ,cbX,bcbX = sp.symbols("cW cWbar cZ cZbar cX cXbar")

# Gauge-invariant scalar potential in the paper's one-doublet/one-singlet model.
H2 = Gp*Gm + ((v+h)**2 + G0**2)/2
S2 = ((vs+s)**2 + a**2)/2
muH2,muS2 = sp.symbols("mu_H2 mu_S2")
V = -muH2*H2 - muS2*S2 + lamH*H2**2 + lamS*S2**2 + lamHS*H2*S2
fields = [h,s,G0,Gp,Gm,a]
zero = {x:0 for x in fields}
def at_vev(expr): return sp.factor(expr.subs(zero))

cubic={}
for comb in combinations_with_replacement(fields,3):
    d=V
    for f in comb: d=sp.diff(d,f)
    value=at_vev(d)
    if value != 0: cubic[" ".join(map(str,comb))]=value
quartic={}
for comb in combinations_with_replacement(fields,4):
    d=V
    for f in comb: d=sp.diff(d,f)
    value=at_vev(d)
    if value != 0: quartic[" ".join(map(str,comb))]=value

expected_cubic={
"h h h":6*lamH*v, "s s s":6*lamS*vs,
"h h s":lamHS*vs, "h s s":lamHS*v,
"h G0 G0":2*lamH*v, "h Gp Gm":2*lamH*v,
"s G0 G0":lamHS*vs, "s Gp Gm":lamHS*vs,
"h a a":lamHS*v, "s a a":2*lamS*vs,
}
expected_quartic={
"h h h h":6*lamH, "s s s s":6*lamS, "h h s s":lamHS,
"h h G0 G0":2*lamH, "h h Gp Gm":2*lamH,
"s s G0 G0":lamHS, "s s Gp Gm":lamHS,
"h h a a":lamHS, "s s a a":2*lamS,
"G0 G0 G0 G0":6*lamH, "G0 G0 Gp Gm":2*lamH,
"G0 G0 a a":lamHS, "Gp Gp Gm Gm":4*lamH,
"Gp Gm a a":lamHS, "a a a a":6*lamS,
}
assert cubic == expected_cubic, (cubic,expected_cubic)
assert quartic == expected_quartic, (quartic,expected_quartic)

# Gauge-boson mass terms in the gauge basis. Derivatives give vertex
# coefficients in L; the corresponding rule is i times this coefficient.
Lmass = (mW**2*(1+h/v)**2*Wm*Wp
         +mZ**2/2*(1+h/v)**2*Z**2
         +mX**2/2*(1+s/vs)**2*Xv**2)
def d0(expr,*args): 
    for x in args: expr=sp.diff(expr,x)
    return sp.factor(expr.subs(zero_gauge))
zero_gauge={h:0,s:0,Wm:0,Wp:0,Z:0,Xv:0}
gauge_vertices={
"h W+ W-":d0(Lmass,h,Wm,Wp),
"h Z Z":d0(Lmass,h,Z,Z),
"s A' A'":d0(Lmass,s,Xv,Xv),
"h h W+ W-":d0(Lmass,h,h,Wm,Wp),
"h h Z Z":d0(Lmass,h,h,Z,Z),
"s s A' A'":d0(Lmass,s,s,Xv,Xv),
}
expected_gauge={
"h W+ W-":2*mW**2/v, "h Z Z":2*mZ**2/v,
"s A' A'":2*mX**2/vs,
"h h W+ W-":2*mW**2/v**2,
"h h Z Z":2*mZ**2/v**2,
"s s A' A'":2*mX**2/vs**2,
}
assert gauge_vertices==expected_gauge,(gauge_vertices,expected_gauge)
# Gauge-basis absence checks.
for args in [(h,Xv,Xv),(s,Wm,Wp),(s,Z,Z)]:
    assert d0(Lmass,*args)==0

# With delta G^A = -m_A(1+radial/vev) alpha^A and
# F^A = partial.A^A - xi_A m_A G^A, M_FP = delta F/delta alpha.
# L_FP = -bar c M_FP c. These are the scalar-dependent diagonal entries.
Mghost = {
"W": sp.expand(xiW*mW**2*(1+h/v)),
"Z": sp.expand(xiZ*mZ**2*(1+h/v)),
"X": sp.expand(xiX*mX**2*(1+s/vs)),
}
ghost_hs={
"h cWbar cW":sp.diff(Mghost["W"],h),
"h cZbar cZ":sp.diff(Mghost["Z"],h),
"s cXbar cX":sp.diff(Mghost["X"],s),
}
expected_ghost={
"h cWbar cW":xiW*mW**2/v,
"h cZbar cZ":xiZ*mZ**2/v,
"s cXbar cX":xiX*mX**2/vs,
}
assert ghost_hs==expected_ghost,(ghost_hs,expected_ghost)
assert sp.simplify(ghost_hs["s cXbar cX"]-2*xiX*mX*(mX/(2*vs)))==0
# No cross scalar/ghost entries in the gauge basis.
assert sp.diff(Mghost["W"],s)==0
assert sp.diff(Mghost["Z"],s)==0
assert sp.diff(Mghost["X"],h)==0

print("A2 scalar potential cubic vertices (derivatives of V):")
for k,val in cubic.items(): print(f"  {k}: {val}")
print("A2 scalar potential quartic vertices (derivatives of V):")
for k,val in quartic.items(): print(f"  {k}: {val}")
print("A2 gauge-boson vertices (coefficients in L):")
for k,val in gauge_vertices.items(): print(f"  {k}: {val}")
print("A2 scalar-dependent FP operator entries:")
for k,val in ghost_hs.items(): print(f"  {k}: {val}")
print("PASS: scalar potential cubic/quartic derivatives.")
print("PASS: hWW, hZZ, sA'A' and corresponding quartic gauge vertices.")
print("PASS: no gauge-basis hA'A', sWW, or sZZ vertices.")
print("PASS: FP radial coefficients; U(1)_X coefficient is xi_X*m_X^2/v_s = 2*xi_X*m_X*g_X.")
print("SCOPE: no full non-Abelian FP matrix expansion, no loop integrations, no gauge-independence claim.")
