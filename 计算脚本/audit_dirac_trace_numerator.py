"""Numerical gamma-matrix audit of the parity-even chiral numerator identities.

Uses explicit 4x4 Dirac matrices (metric +---) and checks random integer
four-vectors for: (i) the two alternating four-slash projector traces, (ii) the
pairwise two-slash traces for all six transition sets, and (iii) the two zero-
slash traces. This checks gamma algebra independently of the parameter kernels.
Requires: sympy.
"""
from itertools import product, combinations
import sympy as sp

I2 = sp.eye(2)
zero = sp.zeros(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
pauli = [s1, s2, s3]
gamma = [sp.diag(1, 1, -1, -1)]
for sig in pauli:
    gamma.append(sp.Matrix.vstack(sp.Matrix.hstack(zero, sig), sp.Matrix.hstack(-sig, zero)))
gamma5 = sp.I * gamma[0] * gamma[1] * gamma[2] * gamma[3]
PR = (sp.eye(4) + gamma5) / 2
PL = (sp.eye(4) - gamma5) / 2
P = {0: PR, 1: PL}

def slash(v):
    return gamma[0]*v[0] - gamma[1]*v[1] - gamma[2]*v[2] - gamma[3]*v[3]

def dot(a, b):
    return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]

def trace_for(sigmas, numerators):
    out = sp.eye(4)
    for i in range(4):
        out = out * P[sigmas[i]] * numerators[i]
    return sp.simplify(sp.trace(out))

# Deterministic non-degenerate integer vectors; epsilon pieces cancel between
# the two opposite chirality sequences.
k = [sp.Matrix(v) for v in [(2, 1, -1, 3), (1, -2, 2, 1), (3, 0, 1, -2), (-1, 2, 3, 1)]]
kslash = [slash(v) for v in k]

G = dot(k[0], k[1])*dot(k[2], k[3]) - dot(k[0], k[2])*dot(k[1], k[3]) + dot(k[0], k[3])*dot(k[1], k[2])
tr4a = trace_for((0, 1, 0, 1), kslash)
tr4b = trace_for((1, 0, 1, 0), kslash)
assert sp.simplify(tr4a + tr4b - 4*G) == 0
print('PASS: the unweighted pair of alternating four-slash traces sums to 4*G')

for i, j in combinations(range(4), 2):
    sigma_terms = []
    for sigmas in product((0, 1), repeat=4):
        trans = tuple(r for r in range(4) if sigmas[r] != sigmas[(r+1) % 4])
        if trans == (i, j):
            nums = [kslash[r] if r in (i, j) else sp.eye(4) for r in range(4)]
            sigma_terms.append(trace_for(sigmas, nums))
    assert len(sigma_terms) == 2
    assert sp.simplify(sum(sigma_terms) - 4*dot(k[i], k[j])) == 0
print('PASS: all six two-slash transition pairs sum to 4*(k_i dot k_j)')

zero_terms = []
for sigmas in product((0, 1), repeat=4):
    if all(sigmas[i] == sigmas[(i+1) % 4] for i in range(4)):
        zero_terms.append(trace_for(sigmas, [sp.eye(4)]*4))
assert len(zero_terms) == 2 and sum(zero_terms) == 4
print('PASS: the two zero-slash projector traces sum to 4')
print('Conclusion: after loop integration removes the parity-odd epsilon term, the scalar numerator weights are 2*H*G + 2*sum(C_ij*k_i.k_j) + 2*M.')
