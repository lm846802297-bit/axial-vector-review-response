#!/usr/bin/env python3
"""Decompose the nonexceptional hard polynomial into an off-shell momentum basis.

This is a kinematic linear-algebra projection only. The basis vectors are
chosen to isolate the derivative momentum q_D=p3+p4 and two independent
Higgs-momentum directions. No operator names are assigned to the latter
until the weak-index, IBP and EOM maps are completed.
"""
import sympy as sp

L = sp.symbols("L", real=True)
p1,p2,p3 = sp.symbols("p1 p2 p3")
alpha = (
    sp.Rational(1,2)-L/2,
    sp.Rational(11,16)-sp.Rational(3,8)*L,
    sp.Rational(1,4)-sp.Rational(3,4)*L,
)
vD = -(p1+p2)   # p3+p4 by momentum conservation
vminus = p2-p3
vplus = p2+p3


def decompose():
    a,b,c = sp.symbols("a b c")
    solution = sp.solve(
        sp.Poly(
            sp.expand(a*vD+b*vminus+c*vplus
                      -(alpha[0]*p1+alpha[1]*p2+alpha[2]*p3)),
            p1,p2,p3
        ).coeffs(),
        (a,b,c),
        dict=True,
    )
    assert len(solution)==1
    return tuple(sp.factor(solution[0][x]) for x in (a,b,c))


def main():
    coeffs = decompose()
    expected = (
        -sp.Rational(1,2)+L/2,
        -sp.Rational(1,32)+sp.Rational(7,16)*L,
        sp.Rational(7,32)-sp.Rational(5,16)*L,
    )
    assert tuple(sp.simplify(x-y) for x,y in zip(coeffs,expected)) == (0,0,0)
    a,b,c = coeffs
    reconstructed = sp.expand(a*vD+b*vminus+c*vplus)
    target = sp.expand(alpha[0]*p1+alpha[1]*p2+alpha[2]*p3)
    assert sp.simplify(reconstructed-target)==0
    exceptional = sp.simplify(reconstructed.subs({p1:0,p2:1,p3:0}))
    assert sp.simplify(exceptional-(sp.Rational(11,16)-sp.Rational(3,8)*L))==0
    print("RC-001 nonexceptional hard off-shell momentum decomposition")
    print(f"v_D = p3+p4 = -(p1+p2): coefficient {a}")
    print(f"v_minus = p2-p3: coefficient {b}")
    print(f"v_plus = p2+p3: coefficient {c}")
    print("PASS: exact reconstruction of the three independent slash-p form factors.")
    print("PASS: exceptional projection reproduces 11/16-3L/8.")
    print("BOUNDARY: this is not yet an operator-name, weak-index, IBP or EOM projection.")

if __name__ == "__main__":
    main()
