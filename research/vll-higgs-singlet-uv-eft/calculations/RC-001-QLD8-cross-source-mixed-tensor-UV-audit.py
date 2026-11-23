#!/usr/bin/env python3
"""Symbolic UV-Taylor audit of QLD8 mixed rank-two x scalar projections.

This isolates only the antisymmetric (left or right) rank-two projection.
It uses the same common auxiliary-mass IR rearrangement as the scalar
projection audit, but derives the antisymmetric tensor coefficient directly
from the degree-two Taylor expansion and D-dimensional angular averages.
"""
import sympy as sp

D, eps = sp.symbols("D epsilon")
Acoef = D / 4
Bcoef = D * (D + 2) / 24
c = sp.simplify(Acoef - 4 * Bcoef / D)
assert sp.simplify(c - (D - 4) / 12) == 0
assert sp.simplify(2 * Acoef / D - sp.Rational(1, 2)) == 0

# Represent W(u,v)=Gamma^{mu nu} u_mu v_nu by its six independent
# antisymmetric components in four dimensions.
p1 = sp.Matrix(sp.symbols("p1_0:4"))
p2 = sp.Matrix(sp.symbols("p2_0:4"))
p3 = sp.Matrix(sp.symbols("p3_0:4"))
p4 = -p1 - p2 - p3
q = p1 + p2


def wedge(u, v):
    return sp.Matrix([
        sp.expand(u[i] * v[j] - u[j] * v[i])
        for i in range(4) for j in range(i + 1, 4)
    ])


# The left/right momentum order is x=A+s ell, y=B-s ell.
# For (barQ,Q), (barQ,bard), (Q,d), (bard,d), respectively:
pairs = [(p1, p4), (p1, p3), (p2, p4), (p2, p3)]
T = [
    sp.simplify(c * wedge(a, b) + sp.Rational(1, 2) * wedge(q, a + b))
    for a, b in pairs
]
T1, T2, T3, T4 = T

# Direct color weights on the tree singlet: (-1,+1,+1,-1).
# The gamma-chain signs for left rank-two x scalar are (-,-,+,+);
# for scalar x right rank-two they are (-,+,-,+).
left = sp.simplify(T1 - T2 + T3 - T4)
right = sp.simplify(T1 + T2 - T3 - T4)

left_expected = sp.simplify((1 + c) * wedge(q, p4 - p3))
right_expected = sp.simplify(-2 * (1 + c) * wedge(p1, p2))
assert sp.simplify(left - left_expected) == sp.zeros(6, 1)
assert sp.simplify(right - right_expected) == sp.zeros(6, 1)

# D=4 and D=4-2 epsilon limits.
left_4 = sp.simplify(left.subs(D, 4))
right_4 = sp.simplify(right.subs(D, 4))
assert sp.simplify(left_4 - wedge(q, p4 - p3)) == sp.zeros(6, 1)
assert sp.simplify(right_4 + 2 * wedge(p1, p2)) == sp.zeros(6, 1)

factor_eps = sp.series((1 + c).subs(D, 4 - 2 * eps), eps, 0, 2).removeO()
assert sp.simplify(factor_eps - (1 - eps / 6)) == 0

# Independent exact-rational component checks with random integer momenta.
samples = [
    ([1, 2, 0, 1], [0, 1, 1, 0], [2, 0, 1, 1]),
    ([2, -1, 1, 0], [1, 0, 2, -1], [0, 2, 1, 1]),
    ([0, 1, 2, 1], [2, -1, 0, 1], [1, 1, -2, 0]),
]
sample_checks = 0
for a, b, d in samples:
    a, b, d = map(sp.Matrix, (a, b, d))
    e = -a - b - d
    qq = a + b
    pp = [(a, e), (a, d), (b, e), (b, d)]
    tt = [
        sp.simplify(sp.Rational(1, 2) * wedge(qq, x + y))
        for x, y in pp
    ]
    ll = tt[0] - tt[1] + tt[2] - tt[3]
    rr = tt[0] + tt[1] - tt[2] - tt[3]
    assert sp.simplify(ll - wedge(qq, e - d)) == sp.zeros(6, 1)
    assert sp.simplify(rr + 2 * wedge(a, b)) == sp.zeros(6, 1)
    sample_checks += 2

print("RC-001 QLD8 cross-source mixed-tensor UV-Taylor audit")
print("PASS: D-dimensional angular coefficient c=(D-4)/12.")
print("PASS: q-dependent antisymmetric coefficient 2A/D=1/2.")
print("PASS: left rank-two x scalar color-weighted sum:")
print("  (D+8)/12 * Gamma^{mu nu} q_mu (p4-p3)_nu.")
print("PASS: scalar x right rank-two color-weighted sum:")
print("  -(D+8)/6 * Gamma^{mu nu} p1_mu p2_nu.")
print("PASS: D=4 limits and exact rational component identities.")
print(f"PASS: independent momentum samples: {sample_checks}/{sample_checks}.")
print(f"PASS: D=4-2epsilon prefactor (D+8)/12 = {factor_eps}.")
print("LIMIT: rank-two x scalar and scalar x rank-two projections only.")
print("       Tensor x tensor projection, full graph phase, complete Z matrix,")
print("       and finite evanescent-scheme matching remain open.")
