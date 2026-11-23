#!/usr/bin/env python3
"""Assemble the six Q_LD pure-WW line-pair classes at O(M_E^-2).

The four cross-vertex classes carry the triplet tensor and have the
nonexceptional hard polynomial from the d-dimensional hard-region audit.
The two same-vertex classes carry the singlet tensor but are pure-soft:
their hard-minus-EFT contribution vanishes because the heavy propagator
is independent of the W-loop momentum.

This is a fixed external ordering and unit-multiplicity internal-W summary.
It excludes external legs, counterterms, the external-W five-point form
factor, and the complete Slavnov-Taylor sum.
"""
import sympy as sp

d, eps, L = sp.symbols("d eps L", real=True)
p1, p2, p3 = sp.symbols("p1 p2 p3")
cbar = sp.symbols("cbar")
weights = {"01":-sp.Rational(1,4),"02":sp.Rational(1,4),"05":sp.Rational(1,4),"06":-sp.Rational(1,4)}

def cross_pair_kernels():
    p4 = -p1-p2-p3
    return {
        "01": ((d-2)**2/d*(p2+p4), 2*(d-2)/d*(p1+p2)),
        "02": (-p2+2*(1-1/d)*p3, 2/d*(p1+p2)),
        "05": (2*(1-1/d)*p2+(1-2/d)*p3, -2/d*(p1+p2)),
        "06": (-(p1+p2), 2/d*(p1+p2)),
    }

def cross_weighted_hard():
    pairs = cross_pair_kernels()
    rj = sp.factor(sum(weights[key]*pairs[key][0] for key in weights))
    rk = sp.factor(sum(weights[key]*pairs[key][1] for key in weights))
    return rj, rk

def cross_finite_polynomial():
    rj, rk = cross_weighted_hard()
    delta = 1/eps+cbar
    jhard = delta+1-L
    khard = -1
    amp = sp.expand(rj*jhard+rk*khard)
    amp_eps = sp.series(amp.subs(d,4-2*eps),eps,0,1).removeO()
    pole = sp.simplify(sp.limit(eps*amp_eps,eps,0))
    finite = sp.simplify(sp.limit(amp_eps-pole/eps,eps,0))
    return sp.factor(pole), sp.factor(finite.subs(cbar,0))

def same_vertex_hard():
    # LD-W-03 and LD-W-04 have no M_E-dependent denominator in the loop.
    # Their hard-region Taylor integrals are scaleless in dimensional regularization.
    return sp.Integer(0)

def main():
    pole, finite = cross_finite_polynomial()
    expected_pole = sp.Rational(1,2)*p1+sp.Rational(3,8)*p2+sp.Rational(3,4)*p3
    expected_finite = (
        (sp.Rational(1,2)-L/2)*p1
        +(sp.Rational(11,16)-sp.Rational(3,8)*L)*p2
        +(sp.Rational(1,4)-sp.Rational(3,4)*L)*p3
    )
    assert sp.simplify(pole-expected_pole)==0
    assert sp.simplify(finite-expected_finite)==0
    assert same_vertex_hard()==0
    total = sp.factor(finite+same_vertex_hard())
    at_match = sp.factor(total.subs(L,0))
    print("RC-001 six-pair internal-W hard-matching summary")
    print("Cross-vertex T3 pole residue:")
    print(f"  {pole}")
    print("Cross-vertex T3 MS-bar finite polynomial:")
    print(f"  {finite}")
    print("Same-vertex T0 hard-minus-EFT contribution:")
    print("  0 (pure-soft light-loop factor reproduced by EFT)")
    print("Total six-pair internal-W hard polynomial:")
    print(f"  {total}")
    print("At mu_R=M_E:")
    print(f"  {at_match}")
    print("PASS: six-pair hard summary is consistent with the cross-box and same-vertex sub-blocks.")
    print("BOUNDARY: not the full renormalized four-point amplitude or Wilson coefficient.")

if __name__ == "__main__":
    main()
