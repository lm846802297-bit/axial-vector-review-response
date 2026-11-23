#!/usr/bin/env python3
"""Correct d-dimensional invariant-tensor reduction of the Q8 line graph.

This replaces the earlier planar-component averaging, which omitted
transverse loop components in scalar factors such as (k+r)^2.
Euclidean invariants: Q2=q.q, R2=r.r, QR=q.r.
The trace tr(1)=4 is included. Overall Wilson/gauge factors are omitted.
"""
import sympy as sp

L, u, v, x, Q2, R2, QR, d = sp.symbols(
    "L u v x Q2 R2 QR d"
)
Delta = x*(1-x)*Q2

# k=l-x q, a=k+r, b=k+q.
k2 = L - 2*x*u + x**2*Q2
a2 = L + 2*v - 2*x*u + R2 - 2*x*QR + x**2*Q2
b2 = L + 2*(1-x)*u + (1-x)**2*Q2
ka = L + v - 2*x*u - x*QR + x**2*Q2
bk = L + (1-2*x)*u - x*(1-x)*Q2
ba = L + v + (1-2*x)*u + (1-x)*QR - x*(1-x)*Q2

qb = u + (1-x)*Q2
qk = u - x*Q2
qa = u + QR - x*Q2
rb = v + (1-x)*QR
rk = v - x*QR
ra = v + R2 - x*QR

# Contract the vector numerator with q_mu and r_mu.
qN = sp.expand(4*a2*(qb*ka - bk*qa + ba*qk))
rN = sp.expand(4*a2*(rb*ka - bk*ra + ba*rk))

def angular_moment(i, j):
    """< (l.q)^i (l.r)^j > at fixed l^2=L in d dimensions."""
    n = i+j
    if n % 2:
        return 0
    if n == 0:
        return 1
    if n == 2:
        return {
            (2,0): L*Q2/d,
            (1,1): L*QR/d,
            (0,2): L*R2/d,
        }[(i,j)]
    if n == 4:
        den = d*(d+2)
        return {
            (4,0): 3*L**2*Q2**2/den,
            (3,1): 3*L**2*Q2*QR/den,
            (2,2): L**2*(Q2*R2+2*QR**2)/den,
            (1,3): 3*L**2*QR*R2/den,
            (0,4): 3*L**2*R2**2/den,
        }[(i,j)]
    raise AssertionError(f"unexpected loop-momentum rank {n}")

def angular_average(expr):
    poly = sp.Poly(sp.expand(expr), L, u, v)
    result = 0
    for (il, iu, iv), coeff in poly.terms():
        result += coeff * L**il * angular_moment(iu, iv)
    return sp.factor(result)

qavg = sp.factor(angular_average(qN).subs(d, 4))
ravg = sp.factor(angular_average(rN).subs(d, 4))

# <N^mu>=A(L,x) q^mu+B(L,x) r^mu, inferred from q.N and r.N.
Aavg = sp.factor((qavg*R2-ravg*QR)/(Q2*R2-QR**2))
Bavg = sp.factor((ravg*Q2-qavg*QR)/(Q2*R2-QR**2))
Ap = sp.Poly(Aavg, L)
Bp = sp.Poly(Bavg, L)
A = [sp.factor(Ap.coeff_monomial(L**n)) for n in range(3)]
B = [sp.factor(Bp.coeff_monomial(L**n)) for n in range(3)]

# UV residues of J_0,J_1,J_2 are 1,-2 Delta,+3 Delta^2
# in units of 1/(16 pi^2 epsilon).
Ares = sp.factor(sp.integrate(A[0]-2*Delta*A[1]+3*Delta**2*A[2], (x,0,1)))
Bres = sp.factor(sp.integrate(B[0]-2*Delta*B[1]+3*Delta**2*B[2], (x,0,1)))

expected_A = 4*QR*(QR-R2)/3
expected_B = -4*Q2*(QR-R2)/3
assert sp.simplify(Ares-expected_A) == 0
assert sp.simplify(Bres-expected_B) == 0
assert sp.simplify(Q2*Ares+QR*Bres) == 0

# Independent integrand-level Ward identity:
# q.N = 4 a^2 [ b^2(k.a) - k^2(b.a) ].
qN_direct = sp.expand(4*a2*(b2*ka-k2*ba))
assert sp.simplify(qN-qN_direct) == 0

print("A0 =", A[0])
print("A2 =", A[1])
print("A4 =", A[2])
print("B0 =", B[0])
print("B2 =", B[1])
print("B4 =", B[2])
print("UV coefficient of q^mu =", Ares)
print("UV coefficient of r^mu =", Bres)
print("q_mu times UV vector residue =", sp.factor(Q2*Ares+QR*Bres))
print("PASS: full d-dimensional invariant angular averages")
print("PASS: Feynman-parameter integration")
print("PASS: transverse UV residue")
print("SCOPE: ordinary-line graph only; contact/R* subtraction and hard matching remain open")
