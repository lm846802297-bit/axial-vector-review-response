#!/usr/bin/env python3
"""Exact charge-trace and threshold-log checks for RC-001 B-A' mixing."""
from fractions import Fraction
import sympy as sp

etas = {"mu": 1, "tau": -1}

def main():
    light_trace = {}
    heavy_dirac_trace = {}
    for flavor, eta in etas.items():
        # L doublet: two Weyl components, each Y=-1/2 and x=eta.
        trace_L = 2 * Fraction(-1, 2) * eta
        # Right-handed charged lepton: Y=-1 and x=-eta.
        trace_lR = Fraction(-1) * (-eta)
        # Light trace cancels separately for each flavor.
        assert trace_L + trace_lR == 0
        light_trace[flavor] = trace_L + trace_lR

        # A Dirac E has two Weyl components with Y=-1 and x=eta.
        heavy_dirac_trace[flavor] = 2 * Fraction(-1) * eta

    assert all(v == 0 for v in light_trace.values())
    assert sum(heavy_dirac_trace.values(), Fraction(0)) == 0

    Mmu, Mtau = sp.symbols("M_E_mu M_E_tau", positive=True)
    threshold = sp.log(Mmu**2) - sp.log(Mtau**2)
    assert sp.simplify(threshold - sp.log(Mmu**2 / Mtau**2)) == 0
    equal_mass_threshold = sp.simplify(threshold.subs(Mtau, Mmu))
    assert equal_mass_threshold == 0

    print("Light Weyl trace: sum(Y*x)=0 separately for mu and tau")
    print("Heavy Dirac trace: sum(Y*x)=-2*eta_mu-2*eta_tau=0")
    print("Additive one-loop UV pole proportional to Tr(YX): CANCELS")
    print("Finite heavy threshold: gY*gX*Q_l/(12*pi^2)*ln(M_E_mu^2/M_E_tau^2)")
    print("Equal-heavy-mass threshold: 0")
    print("SCOPE: does not set the independent renormalized chi boundary condition.")

if __name__ == "__main__":
    main()
