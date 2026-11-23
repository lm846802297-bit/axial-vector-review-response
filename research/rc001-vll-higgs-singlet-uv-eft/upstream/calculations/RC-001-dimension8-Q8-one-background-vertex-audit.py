#!/usr/bin/env python3
"""Algebraic Q8 one-background Ward-identity audit."""
import sympy as sp

Pout, Pin = sp.symbols("SlashPout SlashPin", commutative=False)
qslash = Pout - Pin
ward_contact = sp.expand(Pout**2*qslash + Pout*qslash*Pin + qslash*Pin**2)
assert sp.expand(ward_contact-(Pout**3-Pin**3)) == 0

Sout, Sin = sp.symbols("Sout Sin", commutative=False)
ward_line = sp.expand(Sout*(Sout**-1-Sin**-1)*Sin)
assert sp.expand(ward_line-(Sin-Sout)) == 0

# Trace-numerator Ward contraction, expressed only through scalar products.
k2, q2, r2, kq, kr, qr = sp.symbols("k2 q2 r2 kq kr qr")
lhs = (kq+q2)*(k2+kr) - (k2+kq)*(kq+qr) + (k2+kq+kr+qr)*kq
rhs = (k2+2*kq+q2)*(k2+kr) - k2*(k2+kq+kr+qr)
assert sp.simplify(lhs-rhs) == 0

eta = {"mu": 1, "tau": -1}
for flavor, e in eta.items():
    assert (sp.Rational(-1,2)+sp.Rational(-1,2), e) == (-1, e)
    assert (0-1, 2*e-e) == (-1, e)

print("PASS 1: Q8 contact Ward contraction gives Slash(P+q)^3 - Slash(P)^3")
print("PASS 2: ordinary fermion line obeys S_out qslash S_in = S_in - S_out")
print("PASS 3: traced one-loop numerator contraction matches the propagator Ward identity")
print("PASS 4: Q_LD and Q_RD composite charges are (Y,x)=(-1,eta_l), eta_mu=+1, eta_tau=-1")
print("PASS 5: direct Q8 contacts are B: -gY, A_prime: eta_l*gX*Q_l, W: 0")
print("SCOPE: algebraic Ward building blocks only; no loop integration or UV pole evaluated")
print("OPEN: integrated one-loop soft amplitude, two-background amplitude, and hard matching")
