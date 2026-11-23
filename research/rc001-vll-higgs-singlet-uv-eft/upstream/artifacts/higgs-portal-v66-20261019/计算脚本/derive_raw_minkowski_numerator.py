#!/usr/bin/env python3
"""Symbolic raw Minkowski Dirac numerator for a labelled four-vertex fermion loop.

Uses explicit Dirac matrices for metric (+---), four independent chiral vertices
Gamma_i = u_i P_R + v_i P_L, and propagator numerators (slash{k_i}+m_i).
Expands all 2^4 slash/mass choices before any Feynman parameterization or Wick
rotation. This isolates the trace algebra; it does NOT assign model-specific
Yukawa matrix elements to u_i,v_i, nor perform loop integration/matching.
Requires SymPy.
"""
from itertools import product
import sympy as sp

I2 = sp.eye(2)
Z2 = sp.zeros(2)
sigma = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for s in sigma:
    gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(Z2, s), sp.Matrix.hstack(-s, Z2)))
gamma5 = sp.I * gamma[0] * gamma[1] * gamma[2] * gamma[3]
PR = (sp.eye(4) + gamma5) / 2
PL = (sp.eye(4) - gamma5) / 2

u = sp.symbols('u1:5')
v = sp.symbols('v1:5')
m = sp.symbols('m1:5')
k = [[sp.symbols(f'k{i}{mu}') for mu in range(4)] for i in range(1, 5)]

def slash(vec):
    return gamma[0]*vec[0] - gamma[1]*vec[1] - gamma[2]*vec[2] - gamma[3]*vec[3]

vertices = [u[i]*PR + v[i]*PL for i in range(4)]
kslash = [slash(vec) for vec in k]

# Each mask chooses slash numerator at True positions and mass numerator otherwise.
# Product ordering is Gamma_1 N_1 Gamma_2 N_2 Gamma_3 N_3 Gamma_4 N_4.
by_mask = {}
for mask in product((0, 1), repeat=4):
    mats = []
    for i, use_slash in enumerate(mask):
        numerator = kslash[i] if use_slash else m[i]*sp.eye(4)
        mats.extend((vertices[i], numerator))
    prodmat = sp.eye(4)
    for mat in mats:
        prodmat = prodmat * mat
    by_mask[mask] = sp.trace(prodmat)

# Verify expected gamma-count parity: odd number of slash numerators must vanish.
for mask, expr in by_mask.items():
    if sum(mask) % 2:
        assert expr == 0 or sp.expand(expr) == 0, (mask, expr)

print('PASS: all 16 slash/mass masks evaluated with explicit Minkowski Dirac matrices')
print('PASS: all odd-slash masks vanish')
for nslash in (0, 2, 4):
    masks = [mask for mask in by_mask if sum(mask) == nslash]
    nonzero = sum(1 for mask in masks if by_mask[mask] != 0 and sp.expand(by_mask[mask]) != 0)
    print(f'slash_count={nslash}: masks={len(masks)}, nonzero_traces={nonzero}')

# Export all exact expressions for reproducibility, rather than dumping a huge trace to stdout.
out = []
out.append('# Exact symbolic traces by slash/mass mask')
out.append('# metric (+---); vertex order Gamma1 N1 Gamma2 N2 Gamma3 N3 Gamma4 N4')
for mask in product((0, 1), repeat=4):
    out.append(f'mask={"".join(map(str, mask))} nslash={sum(mask)}')
    out.append(str(by_mask[mask]))
    out.append('')
from pathlib import Path
path = Path('/mnt/data/derive_raw_minkowski_numerator_output.txt')
path.write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'WROTE: {path}')
print('BOUNDARY: model-specific vertex orientations/conjugations and Wick rotation are not yet applied.')
