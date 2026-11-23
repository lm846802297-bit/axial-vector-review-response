#!/usr/bin/env python3
"""Exact charge-algebra check for conditional B-A' parameter-counterterm poles."""
import sympy as sp

eta, rho = sp.symbols("eta rho")
Y_L, x_L = -sp.Rational(1, 2), eta
Y_E, x_E = -1, eta
Y_l, x_l = -1, -eta

def main():
    sum_LD = sp.simplify(Y_L*x_L + Y_E*x_E)
    sum_RD = sp.simplify(Y_E*x_E + Y_l*x_l)
    dM = sp.simplify(-6*rho*Y_E*x_E)
    dy_LD = sp.simplify(-3*rho*sum_LD)
    dy_RD = sp.simplify(-3*rho*sum_RD)
    dC_LD = sp.simplify(2*dy_LD - 2*dM)
    dC_RD = sp.simplify(2*dy_RD - 2*dM)
    assert sum_LD == -sp.Rational(3, 2)*eta
    assert sum_RD == 0
    assert dM == 6*rho*eta
    assert dy_LD == sp.Rational(9, 2)*rho*eta
    assert dy_RD == 0
    assert dC_LD == -3*rho*eta
    assert dC_RD == -12*rho*eta
    for flavor_eta in (1, -1):
        assert dC_LD.subs(eta, flavor_eta) == -3*rho*flavor_eta
        assert dC_RD.subs(eta, flavor_eta) == -12*rho*flavor_eta
    print("LD mixed Yukawa parameter pole: +9/2 rho*eta: PASS")
    print("RD mixed Yukawa parameter pole: 0: PASS")
    print("Heavy-mass mixed parameter pole: +6 rho*eta: PASS")
    print("Coefficient parameter sub-blocks: LD=-3 rho*eta; RD=-12 rho*eta: PASS")
    print("SCOPE: parameter counterterms only; no full mixed-gauge Wilson coefficient.")

if __name__ == "__main__":
    main()
