#!/usr/bin/env python3
"""Exact algebraic checks for RC-001 dimension-eight soft current bubbles.

Checks:
  * Feynman-parameter integrals for one massless Weyl-current correlator;
  * the 1/2! and two 1/2 EOM-current factors giving 1/(192 pi^2);
  * vanishing of the mixed left/right chiral current trace;
  * S_tau = S* implies j_(S_tau) = -j_S, so the squared-current kernels add.

This is an analytic-kernel audit, not a FeynArts/FeynCalc diagram generation
or a UV hard-region matching calculation.
"""
import sympy as sp

I = sp.I
x = sp.symbols("x", positive=True)
pi = sp.pi

# Exact Feynman-parameter integrals.
i0 = sp.integrate(x * (1 - x), (x, 0, 1))
ilog = sp.integrate(x * (1 - x) * sp.log(x * (1 - x)), (x, 0, 1))
assert i0 == sp.Rational(1, 6)
assert ilog == -sp.Rational(5, 18)
assert sp.simplify(-ilog / i0) == sp.Rational(5, 3)

# One Weyl fermion is one half of the parity-even Dirac vector-current loop.
weyl_pole_coeff = sp.Rational(1, 4) / pi**2 * i0
assert sp.simplify(weyl_pole_coeff - 1 / (24 * pi**2)) == 0

# Two identical Q6 insertions: 1/2! times (1/2)^2 from the two EOM reductions.
soft_action_coeff = sp.Rational(1, 2) * sp.Rational(1, 2)**2 * weyl_pole_coeff
assert sp.simplify(soft_action_coeff - 1 / (192 * pi**2)) == 0

# Dirac representation gamma matrices, exact rational/complex arithmetic.
zero = sp.zeros(2)
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])

def block(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))

gamma = [
    sp.diag(1, 1, -1, -1),
    block(zero, sigma1, -sigma1, zero),
    block(zero, sigma2, -sigma2, zero),
    block(zero, sigma3, -sigma3, zero),
]
gamma5 = I * gamma[0] * gamma[1] * gamma[2] * gamma[3]
PL = (sp.eye(4) - gamma5) / 2
PR = (sp.eye(4) + gamma5) / 2

k = sp.symbols("k0:4")
q = sp.symbols("q0:4")
slash_k = gamma[0] * k[0] - gamma[1] * k[1] - gamma[2] * k[2] - gamma[3] * k[3]
slash_kq = (
    gamma[0] * (k[0] + q[0])
    - gamma[1] * (k[1] + q[1])
    - gamma[2] * (k[2] + q[2])
    - gamma[3] * (k[3] + q[3])
)

mixed_traces = []
for mu in range(4):
    gamma_mu = gamma[mu] if mu == 0 else -gamma[mu]
    for nu in range(4):
        gamma_nu = gamma[nu] if nu == 0 else -gamma[nu]
        trace = sp.simplify(
            sp.trace(gamma_mu * PL * slash_k * gamma_nu * PR * slash_kq)
        )
        mixed_traces.append(trace)
assert all(value == 0 for value in mixed_traces)

# The conjugate scalar S_tau = S* reverses the U(1) scalar current.
S, dS, Sd, dSd = sp.symbols("S dS Sd dSd", commutative=True)
j_mu = I * (Sd * dS - dSd * S)
j_tau = I * (S * dSd - dS * Sd)
assert sp.simplify(j_tau + j_mu) == 0
assert sp.simplify(j_tau**2 - j_mu**2) == 0

print("PASS: integral_0^1 dx x(1-x) = 1/6")
print("PASS: integral_0^1 dx x(1-x) log[x(1-x)] = -5/18")
print("PASS: finite massless Weyl-current constant = 5/3")
print("PASS: one-Weyl transverse-polarization pole coefficient = 1/(24 pi^2)")
print("PASS: two-insertion effective-action coefficient = 1/(192 pi^2)")
print("PASS: all 16 mixed L/R chiral-current traces vanish exactly")
print("PASS: S_tau=S* gives j_tau=-j_S and equal squared-current kernels")
print("SCOPE: EOM-reduced EFT soft kernels only; no UV hard matching or diagram-package validation")
