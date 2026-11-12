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

# Independent one-loop effective-potential cross-check in the O(4) x O(2)
# real-field basis: H has four real components, S has two.
x,y=sp.symbols("background_H background_S")
A=3*lamH*x**2 + lamHS*y**2/2
D=lamH*x**2 + lamHS*y**2/2
C=3*lamS*y**2 + lamHS*x**2/2
B=lamS*y**2 + lamHS*x**2/2
off=lamHS*x*y
tr_mass4=sp.expand(A**2+3*D**2+C**2+B**2+2*off**2)
cross=sp.factor(tr_mass4.coeff(x,2).coeff(y,2))
expected_cross=2*lamHS*(3*lamH+lamHS+2*lamS)
assert sp.simplify(cross-expected_cross)==0
delta_lam_full=sp.factor(lamHS*(6*lamH+2*lamHS+4*lamS)/(16*sp.pi**2))
assert sp.simplify(delta_lam_full-delta_lam-lamHS**2/(8*sp.pi**2))==0
print("PASS: independent O(4)xO(2) effective-potential Tr[M^4] cross term.")
print(f"  [Tr M^4]_(H^2 S^2) = {cross}")
print(f"  Full scalar-only delta_lambda_HS = {delta_lam_full}/epsbar")
print("  Linear-in-portal part agrees with the A3a bubble pole.")
print("  The additional 2*lambda_HS^2 term is beyond the adopted lambda_HS=O(hbar), O(hbar^2) truncation.")

print("LIMIT: gauge/Yukawa counterterms, tadpole/VEV, fermion matching and full gauge completion remain.")
