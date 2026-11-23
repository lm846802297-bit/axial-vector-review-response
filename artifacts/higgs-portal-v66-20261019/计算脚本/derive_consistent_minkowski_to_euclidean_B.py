#!/usr/bin/env python3
"""Derive B kernels from a single consistent Minkowski denominator convention.
Requires Python 3 + SymPy. Keeps path labels abstract; no path sums or EFT matching.
"""
import sympy as sp
F,H,S,M,g,d,Delta=sp.symbols('F H S M g d Delta')
# O(q^2) numerator after shift K=k+R, before Wick rotation:
# 2 F + 2 H g K_M^2. Zero-external-momentum numerator is
# 2 H K_M^4 + 2 S K_M^2 + 2 M.
# Denominator: D_M = K_M^2 - Delta_0 + deltaDelta.
# Expand D_M^-4 = D0^-4 - 4 deltaDelta D0^-5 + O(q^4).
terms_minkowski = [
    ('F', 2*F, 0, 4),
    ('H_g', 2*H*g, 1, 4),
    ('H_d', -8*H*d, 2, 5),
    ('S_d', -8*S*d, 1, 5),
    ('M_d', -8*M*d, 0, 5),
]
print('Term | coefficient before Wick | r | n | Wick sign (-1)^(n+r) | coefficient after factoring common i')
coeffs={}
for name,c,r,n in terms_minkowski:
    sign=(-1)**(n+r)
    ce=sp.expand(c*sign)
    coeffs[name]=ce
    print(f'{name} | {c} | {r} | {n} | {sign:+d} | {ce}')
# Positive Euclidean integral normalizations (in units 1/(16 pi^2)).
I04=1/(6*Delta**2)
I14=1/(3*Delta)
I25=1/(4*Delta)
I15=1/(12*Delta**2)
I05=1/(12*Delta**3)
K=sp.expand(coeffs['F']*I04+coeffs['H_g']*I14+coeffs['H_d']*I25+coeffs['S_d']*I15+coeffs['M_d']*I05)
B1=H*(-sp.Rational(2,3)*g+2*d)
B2=sp.Rational(1,3)*F-sp.Rational(2,3)*S*d
B3=sp.Rational(2,3)*M*d
B=sp.expand(B1/Delta+B2/Delta**2+B3/Delta**3)
assert sp.simplify(K-B)==0
print('\nReduced kernel:')
print('B1 = H*(-2*g/3 + 2*d)')
print('B2 = F/3 - 2*S*d/3')
print('B3 = +2*M*d/3')
print('PASS: termwise Minkowski expansion + Wick signs + Euclidean integral reduction reproduce the candidate B kernel.')
print('BOUNDARY: assumes numerator decomposition stated in the script; does not derive model-specific numerator coefficients, sum external-leg permutations, or perform EFT subtraction.')
