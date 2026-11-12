#!/usr/bin/env python3
"""A3b symbolic counterterm/tadpole matrix audit for the h-s system."""
import sympy as sp

v,vs=sp.symbols("v v_S", positive=True)
lH,lS,lHS,muH2,muS2=sp.symbols("lambda_H lambda_S lambda_HS mu_H2 mu_S2")
dv,dvs,dlH,dlS,dlHS,dmuH2,dmuS2=sp.symbols(
    "delta_v delta_vS delta_lambda_H delta_lambda_S delta_lambda_HS delta_mu_H2 delta_mu_S2")
eps=sp.symbols("eps")
# Tree tadpoles after H=(v+h)/sqrt2, S=(vS+s)/sqrt2.
Th=-muH2*v+lH*v**3+sp.Rational(1,2)*lHS*v*vs**2
Ts=-muS2*vs+lS*vs**3+sp.Rational(1,2)*lHS*v**2*vs
subs={
    v:v+eps*dv, vs:vs+eps*dvs,
    lH:lH+eps*dlH, lS:lS+eps*dlS, lHS:lHS+eps*dlHS,
    muH2:muH2+eps*dmuH2, muS2:muS2+eps*dmuS2,
}
dTh=sp.expand(Th.subs(subs)).coeff(eps,1)
dTs=sp.expand(Ts.subs(subs)).coeff(eps,1)
# Use tree stationarity conditions to eliminate mu^2.
dTh_min=sp.factor(dTh.subs(muH2,lH*v**2+lHS*vs**2/2))
dTs_min=sp.factor(dTs.subs(muS2,lS*vs**2+lHS*v**2/2))
expTh=-v*dmuH2+v**3*dlH+sp.Rational(1,2)*v*vs**2*dlHS+2*lH*v**2*dv+lHS*v*vs*dvs
expTs=-vs*dmuS2+vs**3*dlS+sp.Rational(1,2)*v**2*vs*dlHS+2*lS*vs**2*dvs+lHS*v*vs*dv
assert sp.simplify(dTh_min-expTh)==0
assert sp.simplify(dTs_min-expTs)==0

Mhh=2*lH*v**2
Mss=2*lS*vs**2
Mhs=lHS*v*vs
dMhh=sp.diff(Mhh,v)*dv+sp.diff(Mhh,lH)*dlH
dMss=sp.diff(Mss,vs)*dvs+sp.diff(Mss,lS)*dlS
dMhs=sp.diff(Mhs,v)*dv+sp.diff(Mhs,vs)*dvs+sp.diff(Mhs,lHS)*dlHS
assert sp.simplify(dMhh-(4*lH*v*dv+2*v**2*dlH))==0
assert sp.simplify(dMss-(4*lS*vs*dvs+2*vs**2*dlS))==0
assert sp.simplify(dMhs-(lHS*(vs*dv+v*dvs)+v*vs*dlHS))==0

Zhh,Zss,Zhs,Zsh,p2=sp.symbols("deltaZ_hh deltaZ_ss deltaZ_hs deltaZ_sh p2")
field_mass_hs=sp.Rational(1,2)*(Zhh*Mhs+Zsh*Mss+Mhh*Zhs+Mhs*Zss)
field_kin_hs=sp.Rational(1,2)*(Zhs+Zsh)*p2
ct_hs=sp.expand(field_kin_hs-field_mass_hs-dMhs)
ct_zeroportal=sp.simplify(ct_hs.subs(lHS,0))
ct_symmetric=sp.simplify(ct_zeroportal.subs(Zsh,Zhs))
expected=Zhs*(p2-(Mhh+Mss)/2)-v*vs*dlHS
assert sp.simplify(ct_symmetric-expected)==0

print("A3b tadpole counterterm derivatives:")
print(f"  delta T_h = {expTh}")
print(f"  delta T_s = {expTs}")
print("A3b parameter mass counterterms:")
print(f"  delta M_hh^2 = {dMhh}")
print(f"  delta M_ss^2 = {dMss}")
print(f"  delta M_hs^2 = {dMhs}")
print("A3b symmetric off-diagonal field counterterm at zero tree portal:")
print(f"  delta Gamma_hs^ct(p^2) = {expected}")
print("PASS: tadpole derivatives, parameter mass counterterms, and field-renormalization matrix.")
print("LIMIT: this is a counterterm identity map; no tadpole scheme or finite renormalization conditions are imposed.")
