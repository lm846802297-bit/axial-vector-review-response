#!/usr/bin/env python3
"""Audit Section 301: off-shell EOM completion reconciles the 4/3 coefficient gap.

Checks exact coefficient algebra and the mapping from redundant T_H/T_S
operators to the derivative basis. It does not independently reintegrate the
underlying box graph.
"""
import sympy as sp

a, L = sp.symbols("a L", real=True)
Sigma, x1, x2, x3, x4, s, t = sp.symbols("Sigma x1 x2 x3 x4 s t", real=True)

old_poly = a*((L-2)*s + sp.Rational(1,6)*t - Sigma/sp.Integer(12))
off_poly = a*((L-2)*s + sp.Rational(1,6)*t + Sigma/sp.Integer(4))
assert sp.simplify(off_poly-old_poly-a*Sigma/sp.Integer(3)) == 0

completion_sum = sp.expand(a*(x1+x2+x3+x4)/3)
Sigma_definition = x1+x2+x3+x4
assert sp.simplify(completion_sum-a*Sigma_definition/3) == 0

etaH = etaS = -a/sp.Integer(3)
T_H_vertex = -(x1+x3)
T_S_vertex = -(x2+x4)
completion = sp.expand(etaH*T_H_vertex+etaS*T_S_vertex)
assert sp.simplify(completion-completion_sum) == 0

cH_old = a*(L-sp.Rational(13,6))
cS_old = a*(L-sp.Rational(13,6))
cD_old = a/sp.Integer(2)*(L-2)
dcH = -2*etaH
dcS = -2*etaS
dcD = -etaH-etaS
assert sp.simplify(dcH-2*a/sp.Integer(3)) == 0
assert sp.simplify(dcS-2*a/sp.Integer(3)) == 0
assert sp.simplify(dcD-2*a/sp.Integer(3)) == 0

cH_new = sp.simplify(cH_old+dcH)
cS_new = sp.simplify(cS_old+dcS)
cD_new = sp.simplify(cD_old+dcD)
cH_2p = a*(L-sp.Rational(3,2))
cS_2p = a*(L-sp.Rational(3,2))
cD_2p = a/sp.Integer(2)*(L-sp.Rational(2,3))
assert sp.simplify(cH_new-cH_2p) == 0
assert sp.simplify(cS_new-cS_2p) == 0
assert sp.simplify(cD_new-cD_2p) == 0

nr_old = sp.simplify(cD_old-(cH_old+cS_old)/2)
nr_new = sp.simplify(cD_new-(cH_new+cS_new)/2)
assert sp.simplify(nr_new-nr_old) == 0
assert sp.simplify(nr_new-a*(sp.Rational(7,6)-L/2)) == 0

print("PASS 1: off-shell minus old on-shell representative is a*Sigma/3")
print("PASS 2: eta_H=eta_S=-a/3 supplies exactly +a*sum_i(p_i^2)/3")
print("PASS 3: EOM shifts cH,cS,cD by equal amounts 2*a/3")
print("PASS 4: completed cH,cS,cD exactly match the two-point hard coefficients")
print("PASS 5: cD - (cH+cS)/2 is unchanged")
print("LIMIT: coefficient mapping only; underlying box integral not independently reintegrated.")
