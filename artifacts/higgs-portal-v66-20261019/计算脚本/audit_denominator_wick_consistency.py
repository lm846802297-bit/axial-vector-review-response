#!/usr/bin/env python3
"""Audit the Feynman-parameter denominator sign before/after Wick rotation.
Requires Python 3 + SymPy. Checks algebraic expansions through O(q^2).
This is a convention audit, not a full matching calculation.
"""
import sympy as sp
K2, DE0, dDE, eps = sp.symbols('K2 DE0 dDE eps')
# Metric (+---), propagators (k+r)^2-m^2+i0, r_i Minkowski vectors.
# After Feynman parameters and K=k+R:
# sum x_i[(k+r_i)^2-m_i^2] = K_M^2 + dDE - DE0,
# where dDE = sum x_i r_i^2 - R^2 and DE0=sum x_i m_i^2.
D_M = K2 - DE0 + dDE
# Wick: K_M^2 -> -K_E^2, with overall minus extracted from each denominator.
KE2 = sp.symbols('KE2', nonnegative=True)
D_E_correct = KE2 + DE0 - dDE
D_E_old = KE2 + DE0 + dDE
# Check: -(D_M)|K_M^2=-K_E^2 equals the correct Euclidean denominator.
assert sp.expand(-(D_M.subs(K2, -KE2)) - D_E_correct) == 0
# Expansion of Euclidean denominator to O(dDE): the sign is negative.
series_correct = sp.series((KE2 + DE0 - dDE)**-4, dDE, 0, 2).removeO()
series_expected = (KE2 + DE0)**-4 + 4*dDE*(KE2 + DE0)**-5
assert sp.simplify(series_correct-series_expected) == 0
# The previously recorded +dDE denominator convention has opposite linear term.
series_old = sp.series((KE2 + DE0 + dDE)**-4, dDE, 0, 2).removeO()
series_old_expected = (KE2 + DE0)**-4 - 4*dDE*(KE2 + DE0)**-5
assert sp.simplify(series_old-series_old_expected) == 0
print('PASS: Minkowski denominator after shift is K_M^2 - Delta_0 + deltaDelta.')
print('PASS: Wick rotation gives Euclidean denominator K_E^2 + Delta_0 - deltaDelta.')
print('PASS: correct Euclidean expansion has +4 deltaDelta/(K_E^2+Delta_0)^5 for the n=4 denominator.')
print('PASS: the previously recorded K_E^2 + Delta_0 + deltaDelta convention has the opposite linear term.')
print('CONSEQUENCE: the d_alpha sign in the Euclidean denominator expansion must be reconciled before accepting any B^(1), B^(2), B^(3) kernel.')
print('BOUNDARY: does not recalculate the complete numerator, graph multiplicities, EFT subtraction, or Wilson coefficients.')
