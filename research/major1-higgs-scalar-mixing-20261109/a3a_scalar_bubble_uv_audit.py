#!/usr/bin/env python3
"""A3a symbolic UV-pole audit for the one-loop-topology hs scalar bubbles."""
import sympy as sp
lamH,lamS,lamHS,v,vs=sp.symbols("lambda_H lambda_S lambda_HS v v_S")
# kappa_hphip * kappa_sphip times symmetry factor.
terms={
    "hh":sp.Rational(1,2)*(6*lamH*v)*(lamHS*vs),
    "ss":sp.Rational(1,2)*(lamHS*v)*(6*lamS*vs),
    "GplusGminus":(2*lamH*v)*(lamHS*vs),
    "G0G0":sp.Rational(1,2)*(2*lamH*v)*(lamHS*vs),
    "aa":sp.Rational(1,2)*(lamHS*v)*(2*lamS*vs),
}
expected={
    "hh":3*lamH*lamHS*v*vs,
    "ss":3*lamS*lamHS*v*vs,
    "GplusGminus":2*lamH*lamHS*v*vs,
    "G0G0":lamH*lamHS*v*vs,
    "aa":lamS*lamHS*v*vs,
}
assert terms==expected
total=sp.factor(sum(terms.values()))
assert sp.simplify(total-lamHS*v*vs*(6*lamH+4*lamS))==0
delta_lam=sp.factor(lamHS*(6*lamH+4*lamS)/(16*sp.pi**2))
print("Individual scalar-bubble UV coefficients (before common 1/(16 pi^2 epsbar)):")
for name,value in terms.items(): print(f"  {name}: {value}")
print(f"Sum: {total}")
print("Therefore the portal counterterm pole magnitude in Gamma_inv=p^2-M^2+Pi convention is")
print(f"  delta_lambda_HS = {delta_lam}/epsbar")
print("PASS: all symmetry factors and the total 6 lambda_H + 4 lambda_S coefficient.")
print("LIMIT: scalar-bubble subset only; tadpole/VEV, gauge, fermion and full matching terms remain.")
