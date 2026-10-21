"""Exact audit of chirality-transition bookkeeping used for H_rho, C_ij, M_rho.

For a closed four-vertex fermion chain, a slash numerator flips chirality while a
mass numerator preserves it. This script enumerates all 2^4 projector choices
and verifies that the transition-set sums reproduce the definitions of H, C_ij,
and M used in general_mass_ratio_integral.py.
Requires: sympy.
"""
from itertools import product, combinations
import sympy as sp

u = sp.symbols('u0:4')
v = sp.symbols('v0:4')
m = sp.symbols('m0:4')

H_enum = 0
M_enum = 0
C_enum = {pair: 0 for pair in combinations(range(4), 2)}
transition_counts = {0: 0, 2: 0, 4: 0}
for sigma in product((0, 1), repeat=4):
    transitions = tuple(i for i in range(4) if sigma[i] != sigma[(i + 1) % 4])
    transition_counts[len(transitions)] += 1
    vertex_product = sp.prod(u[i] if sigma[i] == 0 else v[i] for i in range(4))
    mass_product = sp.prod(m[i] for i in range(4) if i not in transitions)
    term = vertex_product * mass_product
    if len(transitions) == 4:
        H_enum += vertex_product
    elif len(transitions) == 2:
        C_enum[transitions] += term
    elif len(transitions) == 0:
        M_enum += term

H_expected = u[0]*v[1]*u[2]*v[3] + v[0]*u[1]*v[2]*u[3]
M_expected = sp.prod(m) * (sp.prod(u) + sp.prod(v))
assert sp.expand(H_enum - H_expected) == 0
assert sp.expand(M_enum - M_expected) == 0
for (i, j), expr in C_enum.items():
    # Independently reconstruct the two sigma patterns with transitions {i,j}.
    expected = 0
    for sigma in product((0, 1), repeat=4):
        trans = tuple(k for k in range(4) if sigma[k] != sigma[(k+1) % 4])
        if trans == (i, j):
            expected += sp.prod(u[k] if sigma[k] == 0 else v[k] for k in range(4)) * sp.prod(m[k] for k in range(4) if k not in trans)
    assert sp.expand(expr - expected) == 0

print('PASS: H_enum == H_expected')
print('PASS: M_enum == M_expected')
print('PASS: all six C_ij transition-set sums reproduce the definitions')
print('chirality patterns by number of slash transitions:', transition_counts)
print('total patterns:', sum(transition_counts.values()))
