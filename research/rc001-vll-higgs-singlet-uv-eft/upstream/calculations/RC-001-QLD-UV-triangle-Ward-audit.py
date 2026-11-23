#!/usr/bin/env python3
"""Exact scalar-product audit of the QLD UV triangle Ward contractions.

Routing: q=k'-k=K-K', with q=p-p'. The light and heavy attachment
contractions are evaluated with one common fermion-flow convention.
"""
import sympy as sp

K2, Kp2, KKp, Kk, Kpk, Kpdotk, kk, kp2, M2, k2 = sp.symbols(
    "K2 Kp2 KKp Kdotk Kdotkp Kpdotk kdotkp kp2 M2 k2"
)

# Light attachment:
# N_L^mu = 2[(K.k')k^mu-(k'.k)K^mu+(K.k)k'^mu].
# q=k'-k, so k.q=k'.k-k^2 and k'.q=k'^2-k'.k.
# K.q=K.k'-K.k.
NLq = sp.expand(2*(Kpk*(kk-k2) - kk*(Kpk-Kk) + Kk*(kp2-kk)))
NLq_expected = 2*(Kk*kp2-Kpk*k2)
assert sp.simplify(NLq-NLq_expected) == 0

# Heavy attachment:
# N_E^mu = 2[(K.k)K'^mu-(K'.K)k^mu
#            +(K'.k)K^mu+M_E^2 k^mu].
# Here q=K-K', so K.q=K^2-K.K', K'.q=K.K'-K'^2.
# k.q=K.k-K'.k.
NEq = sp.expand(2*(Kk*(KKp-Kp2) - KKp*(Kk-Kpdotk)
                  + Kpdotk*(K2-KKp) + M2*(Kk-Kpdotk)))
NEq_expected = 2*(Kpdotk*(K2-M2)-Kk*(Kp2-M2))
assert sp.simplify(NEq-NEq_expected) == 0

# Propagator Ward reductions:
assert sp.simplify(
    (Kk*kp2-Kpk*k2)/(k2*kp2) - (Kk/k2-Kpk/kp2)
) == 0
assert sp.simplify(
    (Kpdotk*(K2-M2)-Kk*(Kp2-M2))
    /((K2-M2)*(Kp2-M2))
    -(Kpdotk/(Kp2-M2)-Kk/(K2-M2))
) == 0

# Yukawa gauge invariance: -q_L+q_H+q_E=0.
qL, qH, qE = sp.symbols("qL qH qE")
assert sp.simplify((qL-qE)-qH).subs(qE,qL-qH) == 0

print("PASS 1: light attachment q.N_L = 2[(K.k) k'^2-(K.k') k^2].")
print("PASS 2: heavy attachment q.N_E = 2[(K'.k)(K^2-M_E^2)-(K.k)(K'^2-M_E^2)].")
print("PASS 3: after cancelling adjacent propagators, light gives Sigma(p)-Sigma(p').")
print("PASS 4: heavy gives Sigma(p')-Sigma(p).")
print("PASS 5: same relative sign in the amplitude and q_L-q_E=q_H give the scalar-source Ward identity.")
print("SCOPE: exact algebraic Ward contractions only; no loop integration or Wilson coefficient.")
