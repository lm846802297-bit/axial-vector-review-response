#!/usr/bin/env python3
"""RC-001 B2c-IVk: exact projection of the Feynman-gauge remainder.

For arbitrary endpoint currents J_L and J_R, reduce J_L R_FG J_R
to endpoint-current contractions with k and q. The script also checks
the sufficient transversality condition under which the remainder vanishes.
It does not assert that the off-shell matter currents obey that condition.
"""
from itertools import product
import sympy as sp

ETA = (1, -1, -1, -1)
k = sp.symbols("k0:4", real=True)
q = sp.symbols("q0:4", real=True)
JL = sp.symbols("JL0:4", real=True)
JR = sp.symbols("JR0:4", real=True)
kq = tuple(k[i] + q[i] for i in range(4))


def dot(a, b):
    return sp.expand(sum(ETA[i] * a[i] * b[i] for i in range(4)))


def main():
    k2 = dot(k, k)
    kq2 = dot(kq, kq)
    left_k, left_q = dot(JL, k), dot(JL, q)
    right_k, right_q = dot(JR, k), dot(JR, q)
    left_kq = dot(JL, kq)
    right_kq = dot(JR, kq)

    direct = sp.expand(
        (left_k*right_k-left_kq*right_kq)/(k2*kq2)
    )
    endpoint_form = sp.expand(
        -(left_k*right_q+left_q*right_k+left_q*right_q)/(k2*kq2)
    )
    assert sp.simplify(direct-endpoint_form) == 0

    # Use independent endpoint contractions to test a sufficient
    # transversality condition without substituting composite expressions.
    X, Y, U, V = sp.symbols("X Y U V")
    numerator = X*Y-(X+U)*(Y+V)
    assert sp.simplify(numerator.subs({X: 0, Y: -V})) == 0

    # Generic rational diagnostic: nonzero even for a simple pair of currents.
    kv = (sp.Integer(3), sp.Integer(2), sp.Integer(0), sp.Integer(0))
    qv = (sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0))
    jlv = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
    jrv = (sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(0))
    k2v = dot(kv, kv)
    kq2v = dot(tuple(kv[i]+qv[i] for i in range(4)),
               tuple(kv[i]+qv[i] for i in range(4)))
    value = sp.simplify(
        (dot(jlv,kv)*dot(jrv,kv)
         -dot(jlv,tuple(kv[i]+qv[i] for i in range(4)))
          *dot(jrv,tuple(kv[i]+qv[i] for i in range(4))))
        /(k2v*kq2v)
    )
    assert value == sp.Rational(2,55)

    print("RC-001 B2c-IVk exact R_FG current projection")
    print("PASS: J_L^mu R_FG,mu nu J_R^nu equals")
    print("  -[(J_L.k)(J_R.q)+(J_L.q)(J_R.k)+(J_L.q)(J_R.q)]/[k^2(k+q)^2].")
    print("PASS: sufficient condition J_L.k=0 and J_R.(k+q)=0 implies zero.")
    print("IMPORTANT: no such transversality condition is assumed for off-shell matter currents.")
    print(f"PASS: generic rational diagnostic gives {value} (nonzero).")
    print("BOUNDARY:")
    print("  This identifies the exact current projection of the Feynman-gauge remainder.")
    print("  It does not calculate the pair-specific fermion/scalar currents or the ghost/ST terms.")
    print("  No loop integration, UV-EFT subtraction, or Wilson coefficient is claimed.")


if __name__ == "__main__":
    main()
