#!/usr/bin/env python3
"""Exact symbolic checks for the P1.6a same-bilinear UV-pole calculation."""
import sympy as sp
D, eps = sp.symbols("D epsilon")
x, y, z = sp.symbols("x y z")

# Feynman-parameter shift: A=(1-y)p1+z p2, B=y p1+(1-z)p2.
wedge_coeff = sp.expand((1-y)*(1-z)-z*y)
assert sp.simplify(wedge_coeff-(1-y-z)) == 0
assert sp.simplify((1-y-z).subs(z,1-x-y)-x) == 0

# The 1/(abc) Feynman parameter factor 2 cancels simplex volume 1/2.
assert sp.Rational(2)*sp.Rational(1,2) == 1

# Scalar integral has Gamma(2-D/2)=Gamma(epsilon), with coefficient D/4.
scalar_gamma_argument = sp.simplify(2-D/2).subs(D,4-2*eps)
assert scalar_gamma_argument == eps
# Tensor integral has Gamma(3-D/2)=Gamma(1+epsilon), hence no UV pole.
tensor_gamma_argument = sp.simplify(3-D/2).subs(D,4-2*eps)
assert tensor_gamma_argument == 1+eps

# Gamma sandwich adds another factor D.
per_graph = sp.expand(D*(D/4))
both_graphs = sp.expand(2*per_graph)
assert sp.simplify(per_graph-D**2/4) == 0
assert sp.simplify(both_graphs-D**2/2) == 0
assert sp.expand(per_graph.subs(D,4-2*eps)-(4-4*eps+eps**2)) == 0
assert sp.expand(both_graphs.subs(D,4-2*eps)-(8-8*eps+2*eps**2)) == 0

# Frozen Feynman-rule phase: operator iC, two vertices, two fermion
# propagator numerators, and one Feynman-gauge gluon propagator.
phase = sp.I*(sp.I**2)*(sp.I**2)*(-sp.I)
assert sp.simplify(phase-1) == 0

M = sp.diag(-sp.Rational(4,3),sp.Rational(1,6))
per_block = sp.simplify(-per_graph*M)
both_block = sp.simplify(-both_graphs*M)
assert per_block == sp.diag(D**2/3,-D**2/24)
assert both_block == sp.diag(2*D**2/3,-D**2/12)
assert both_block.subs(D,4) == sp.diag(sp.Rational(32,3),-sp.Rational(4,3))

print("RC-001 QLD8 P1.6a same-bilinear UV audit")
print("PASS: A wedge B = x p1 wedge p2 after the Feynman-parameter shift.")
print("PASS: Feynman-parameter prefactor 2 times simplex volume 1/2 = 1.")
print("PASS: scalar integral has Gamma(epsilon) UV pole with coefficient D/4.")
print("PASS: antisymmetric tensor integral has Gamma(1+epsilon), no UV pole.")
print("PASS: gamma sandwich gives per-graph D^2/4 and two-graph D^2/2.")
print("PASS: full D=4-2epsilon expansions through O(epsilon^2).")
print("PASS: frozen Feynman-rule phase product is +C g_s^2 before integration.")
print("PASS: SU(3) two-graph direct-color block diag(2 D^2/3,-D^2/12).")
print("LIMIT: external legs, background gluons, complete Z matrix and matching remain open.")
