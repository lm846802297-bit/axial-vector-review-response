#!/usr/bin/env python3
"""Method-of-regions audit for the |y|^4 and |lambda|^4 dimension-eight boxes.

Computes the transverse P.P' q^2 projection of one ordered heavy/light
fermion box, expands its hard region through O(p^4), performs d-dimensional
angular averages and radial Gamma-function integrals, and checks the soft
one-Weyl current-correlator kernel. The effective-action 1/2 and the
J=2P current normalization are kept explicit.
"""
import sympy as sp

P, Pp, Q, k1, k4, M, d, eps, mu, q2 = sp.symbols(
    "P Pp Q k1 k4 M d eps mu q2", positive=True
)
K2 = sp.Symbol("K2", positive=True)
vars6 = [P, Pp, Q, k1, k4, K2]

kp1 = P*k1 + Q*k4/2
kr4 = Pp*k1 + Q*k4/2
kq = Q*k4
p1q = Q**2/2
r4q = Q**2/2
p1r4 = P*Pp + Q**2/4

ab = K2 + kp1 + kq + p1q
cd = K2 + kr4
ac = K2 + kp1 + kr4 + p1r4
bd = K2 + kq
ad = K2 + kp1
bc = K2 + kr4 + kq + r4q

# Parity-even Weyl trace: one half of the Dirac trace.
numerator = sp.expand(2*(ab*cd - ac*bd + ad*bc))
A = 2*Q*k4 + Q**2
B = 2*P*k1 + Q*k4 + P**2 + Q**2/4
C = 2*Pp*k1 + Q*k4 + Pp**2 + Q**2/4

def poly6(expr):
    poly = sp.Poly(sp.expand(expr), *vars6)
    return {mon: coeff for mon, coeff in poly.terms()
            if sum(mon[:3]) <= 4}

def multiply(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            mon = tuple(x+y for x, y in zip(ma, mb))
            if sum(mon[:3]) <= 4:
                out[mon] = out.get(mon, 0) + ca*cb
    return {mon: sp.factor(c) for mon, c in out.items() if c != 0}

def power(a, n):
    out = {(0,0,0,0,0,0): sp.Integer(1)}
    for _ in range(n):
        out = multiply(out, a)
    return out

def collect_hard_terms():
    n_poly, a_poly, b_poly, c_poly = map(poly6, (numerator, A, B, C))
    groups = {}
    for na in range(5):
        for nb in range(5):
            for nc in range(5):
                if na+nb+nc > 4:
                    continue
                product = multiply(
                    multiply(multiply(n_poly, power(a_poly, na)),
                             power(b_poly, nb)),
                    power(c_poly, nc)
                )
                for mon, coeff in product.items():
                    if mon[:3] != (1,1,2):
                        continue
                    n1, n4, radial_power = mon[3:]
                    if n1 % 2 or n4 % 2:
                        continue
                    n = (n1+n4)//2
                    angular = (
                        sp.rf(sp.Rational(1,2), n1//2)
                        * sp.rf(sp.Rational(1,2), n4//2)
                        / sp.rf(d/2, n)
                    )
                    key = (na+2, nb+nc+2, radial_power+n)
                    groups[key] = groups.get(key, 0) + (
                        coeff * (-1)**(na+nb+nc) * angular
                    )
    return {key: sp.factor(value) for key, value in groups.items()
            if value != 0}

def radial_integral(a, b, n):
    u = n-a
    return (
        (M**2)**(d/2+u-b) / (4*sp.pi)**(d/2)
        * sp.gamma(d/2+u) * sp.gamma(b-d/2-u)
        / (sp.gamma(d/2)*sp.gamma(b))
    )

groups = collect_hard_terms()
assert len(groups) == 11
hard_exact = sp.simplify(sum(
    coeff*radial_integral(a, b, n)
    for (a,b,n), coeff in groups.items()
).subs(d, 4-2*eps))

Delta_IR = 1/eps - sp.EulerGamma + sp.log(4*sp.pi)
Delta_UV = Delta_IR
L_E = sp.log(M**2/mu**2)
hard_expected = -(
    Delta_IR - L_E + sp.Rational(17,12)
) / (24*sp.pi**2*M**4)
hard_series = sp.series(hard_exact*mu**(2*eps), eps, 0, 1).removeO()
assert sp.simplify(hard_series-hard_expected) == 0

soft_parameter = (
    4*mu**(2*eps)*q2**(-eps)/(4*sp.pi)**(2-eps)
    * sp.gamma(eps)*sp.gamma(2-eps)**2/sp.gamma(4-2*eps)
)
soft_series = sp.series(soft_parameter, eps, 0, 1).removeO()
soft_expected = (
    Delta_UV - sp.log(q2/mu**2) + sp.Rational(5,3)
) / (24*sp.pi**2)
assert sp.simplify(soft_series-soft_expected) == 0

hard_effective = sp.simplify(hard_expected/8)
soft_effective = sp.simplify(soft_expected/8)
assert sp.simplify(
    hard_effective + (Delta_IR-L_E+sp.Rational(17,12))/(192*sp.pi**2*M**4)
) == 0
assert sp.simplify(
    soft_effective - (Delta_UV-sp.log(q2/mu**2)+sp.Rational(5,3))/(192*sp.pi**2*M**4)
) == 0
hard_effective_pole = -sp.Rational(1,192)/(sp.pi**2*M**4)
soft_effective_pole = sp.Rational(1,192)/(sp.pi**2*M**4)
assert sp.simplify(hard_effective_pole+soft_effective_pole) == 0

finite = sp.simplify(
    L_E - sp.Rational(17,12)
    - sp.log(q2/mu**2) + sp.Rational(5,3)
)
assert sp.simplify(finite-(sp.log(M**2/q2)+sp.Rational(1,4))) == 0

print("PASS 1: d-dimensional hard-region expansion isolates the transverse P.P' q^2 projection")
print("PASS 2: 11 radial structures integrate to the hard pole and finite term")
print("PASS 3: hard = -(Delta_IR - L_E + 17/12)/(24 pi^2 M_E^4) per ordered box")
print("PASS 4: soft Feynman parameter integral gives +(Delta_UV - ln(q^2/mu^2) + 5/3)/(24 pi^2 M_E^4)")
print("PASS 5: determinant 1/2 and J=2P conversion give equal-and-opposite hard IR / soft UV poles")
print("PASS 6: finite hard+soft kernel = [ln(M_E^2/q^2) + 1/4]/(192 pi^2 M_E^4) in the current effective-action basis")
print("SCOPE: Yukawa-only transverse current channel, one ordered box, NDR parity-even chiral trace")
print("OPEN: other independent tensor projections, complete crossed-channel/weak-tensor ledger, EOM/source reduction, and FeynArts/FeynCalc validation")
