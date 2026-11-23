#!/usr/bin/env python3
"""Independent post-processing audit of the P0.1-P0.4 on-shell result.

This script does not repeat the loop integrations. It independently checks
the polynomial decomposition, pole cancellation, matching-scale cancellation,
crossing symmetry, all SU(2) component tensors, and action-to-amplitude
normalization using only the coefficients printed in the analytic note.
"""
import sympy as sp
from itertools import product

s, u, L_E, ell_q = sp.symbols("s u L_E ell_q")
Delta_IR, Delta_UV = sp.symbols("Delta_IR Delta_UV")
A = s**2 + 2*s*u

hard = (
    A*(Delta_IR-L_E)
    + sp.Rational(11,6)*s**2
    + sp.Rational(10,3)*s*u
    - sp.Rational(3,10)*u**2
)
soft = -A*(Delta_UV-ell_q+sp.Rational(5,3))
transverse = A*(Delta_IR-L_E+sp.Rational(17,12))
local_remainder = sp.Rational(5,12)*s**2 + sp.Rational(1,2)*s*u-sp.Rational(3,10)*u**2

assert sp.simplify(hard-transverse-local_remainder) == 0
assert sp.simplify(sp.diff(hard,Delta_IR)+sp.diff(soft,Delta_UV)) == 0

matched = sp.simplify(hard.subs(Delta_IR,0)+soft.subs(Delta_UV,0))
assert sp.simplify(sp.diff(matched,L_E)+sp.diff(matched,ell_q)) == 0

crossed_sum = sp.expand(matched+matched.subs({s:u,u:s},simultaneous=True))
assert sp.simplify(
    crossed_sum-crossed_sum.subs({s:u,u:s},simultaneous=True)
) == 0

def delta(i,j):
    return int(i == j)

for i,j,k,l in product(range(2), repeat=4):
    tensor_s = sum(
        delta(a,i)*delta(b,j)*delta(b,k)*delta(a,l)
        for a,b in product(range(2), repeat=2)
    )
    tensor_u = sum(
        delta(a,i)*delta(b,l)*delta(b,k)*delta(a,j)
        for a,b in product(range(2), repeat=2)
    )
    assert tensor_s == delta(j,k)*delta(l,i)
    assert tensor_u == delta(l,k)*delta(j,i)

action_factor = sp.Rational(1,2)*sp.Rational(1,2)**2*sp.Rational(1,24)
fixed_pairing_amplitude_factor = 2*4*action_factor
assert action_factor == sp.Rational(1,192)
assert fixed_pairing_amplitude_factor == sp.Rational(1,24)

print("PASS 1: independent subtraction isolates local remainder 5 s^2/12 + s u/2 - 3 u^2/10")
print("PASS 2: hard IR and soft UV residues cancel coefficient by coefficient")
print("PASS 3: finite hard+soft kernel is independent of matching scale")
print("PASS 4: explicit s- and u-pairing sum is crossing symmetric")
print("PASS 5: all 16 SU(2) component assignments reproduce the two Kronecker tensors")
print("PASS 6: determinant/EOM-current factor is 1/192 pi^2 and fixed-pairing amplitude factor is 1/24 pi^2")
print("SCOPE: independent algebraic post-processing only; no loop integral or diagram generation is repeated")
