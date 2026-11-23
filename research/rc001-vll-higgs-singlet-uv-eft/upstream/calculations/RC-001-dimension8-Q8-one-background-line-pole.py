#!/usr/bin/env python3
"""Reproduce the d=4 UV residue of the Q8 ordinary fermion-line graph.

Euclidean convention. The trace numerator includes tr(1)=4. The script
computes the angular average after k=l-x q and integrates the Feynman
parameter. It deliberately does not include gauge charges/couplings,
Wilson coefficients, or the Q8 contact graph.
"""
import sympy as sp

l1, l2, x, Q2, R2, QR, L, d = sp.symbols(
    "l1 l2 x Q2 R2 QR L d", nonzero=True
)
Q = sp.sqrt(Q2)
r_parallel = QR / Q
r_perp = sp.sqrt(R2 - QR**2 / Q2)

# Choose q=(Q,0), r=(r_parallel,r_perp), k=l-x q.
k1, k2 = l1 - x*Q, l2
a1, a2 = k1 + r_parallel, k2 + r_perp  # k+r
b1, b2 = k1 + Q, k2                  # k+q

k_dot_a = k1*a1 + k2*a2
b_dot_k = b1*k1 + b2*k2
b_dot_a = b1*a1 + b2*a2
a_sq = a1**2 + a2**2

# tr[(slash(k+q)) gamma^mu slash(k) slash(k+r)^3],
# using slash(p)^2=p^2 and tr[slash(a) gamma^mu slash(b) slash(c)].
Nq = 4*a_sq*(b1*k_dot_a - b_dot_k*a1 + b_dot_a*k1)
Nr = 4*a_sq*(b2*k_dot_a - b_dot_k*a2 + b_dot_a*k2)

def angular_average(expr):
    """O(d)-average for q,r lying in the 1-2 plane."""
    poly = sp.Poly(sp.expand(expr), l1, l2)
    out = 0
    for (i, j), coeff in poly.terms():
        n = i + j
        if n % 2:
            continue
        if n == 0:
            moment = 1
        elif n == 2:
            moment = L/d if (i, j) in ((2, 0), (0, 2)) else 0
        elif n == 4:
            if (i, j) in ((4, 0), (0, 4)):
                moment = 3*L**2/(d*(d+2))
            elif (i, j) == (2, 2):
                moment = L**2/(d*(d+2))
            else:
                moment = 0
        else:
            raise AssertionError(f"unexpected rank {n}")
        out += coeff*moment
    return sp.factor(out)

Nq_avg = angular_average(Nq)
Nr_avg = angular_average(Nr)

# Decompose N^mu = a q^mu + b r^mu:
# N_transverse=b*r_perp, N_parallel=a*Q+b*r_parallel.
bL = sp.factor(Nr_avg.subs(d, 4) / r_perp)
aL = sp.factor((Nq_avg.subs(d, 4) - bL*r_parallel) / Q)
a = [sp.factor(sp.expand(aL).coeff(L, n)) for n in range(3)]
b = [sp.factor(sp.expand(bL).coeff(L, n)) for n in range(3)]

Delta = x*(1-x)*Q2
a_residue = sp.factor(sp.integrate(a[0]-2*Delta*a[1]+3*Delta**2*a[2], (x, 0, 1)))
b_residue = sp.factor(sp.integrate(b[0]-2*Delta*b[1]+3*Delta**2*b[2], (x, 0, 1)))

expected_a = (Q2**2 - 8*Q2*QR + 5*Q2*R2 + 20*QR**2 - 20*QR*R2)/15
expected_b = Q2*(Q2 - 10*QR + 10*R2)/15
assert sp.simplify(a_residue-expected_a) == 0
assert sp.simplify(b_residue-expected_b) == 0

ward_residue = sp.factor(Q2*a_residue + QR*b_residue)
expected_ward = Q2*(Q2-2*QR)*(Q2-5*QR+5*R2)/15
assert sp.simplify(ward_residue-expected_ward) == 0

print("a0 =", a[0])
print("a2 =", a[1])
print("a4 =", a[2])
print("b0 =", b[0])
print("b2 =", b[1])
print("b4 =", b[2])
print("UV residue coefficient of q^mu =", a_residue)
print("UV residue coefficient of r^mu =", b_residue)
print("q_mu contraction of ordinary-line residue =", ward_residue)
print("PASS: all six angular coefficients and both Feynman-parameter integrals")
print("SCOPE: ordinary-line graph only; no Q8 contact graph or full matching")
