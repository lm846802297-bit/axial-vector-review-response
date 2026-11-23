#!/usr/bin/env python3
"""Matching-scale derivative check for the nonexceptional WW hard polynomial."""
import sympy as sp

L, mu = sp.symbols("L mu", positive=True)
p1,p2,p3 = sp.symbols("p1 p2 p3")
C = (
    (sp.Rational(1,2)-L/2)*p1
    +(sp.Rational(11,16)-sp.Rational(3,8)*L)*p2
    +(sp.Rational(1,4)-sp.Rational(3,4)*L)*p3
)
R = sp.Rational(1,2)*p1+sp.Rational(3,8)*p2+sp.Rational(3,4)*p3

def main():
    # L=ln(M_E^2/mu_R^2), so d/d ln(mu_R) = -2 d/dL.
    dC_dlnmu = sp.factor(-2*sp.diff(C,L))
    assert sp.simplify(dC_dlnmu-2*R)==0
    log_coeff = sp.factor(sp.diff(C,L))
    assert sp.simplify(log_coeff+R)==0
    # The exceptional p2 projection recovers the previously checked log.
    exceptional = sp.simplify(C.subs({p1:0,p2:1,p3:0}))
    assert sp.simplify(exceptional-(sp.Rational(11,16)-sp.Rational(3,8)*L))==0
    print("RC-001 nonexceptional WW hard matching-scale check")
    print(f"Coefficient of L: {log_coeff}")
    print(f"d C_hard^fin / d ln(mu_R): {dC_dlnmu}")
    print(f"2 x hard-pole residue: {2*R}")
    print("PASS: the logarithmic coefficient is minus the nonexceptional pole residue.")
    print("PASS: the matching-scale derivative is twice that residue.")
    print("PASS: the exceptional 11/16-3L/8 projection is recovered.")
    print("BOUNDARY: this is a sub-block scale check, not the full EFT RG cancellation.")

if __name__ == "__main__":
    main()
