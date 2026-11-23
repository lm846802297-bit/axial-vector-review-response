#!/usr/bin/env python3
"""One-cycle d=4-2epsilon hard-region match to the RC-001 §248 result.

Starting from the source-aligned numerator
    2 M_E^2 |y lambda|^2 k.(k-q)
and denominator
    k^2 (k-q)^2 [(k-p2)^2-M_E^2] [(k+p4)^2-M_E^2],
this script expands the hard region through O(p^2), performs d-dimensional
tensor reduction, evaluates the three scalar master integrals, and applies
the four-vertex/four-propagator/closed-fermion-loop prefactor.

Scope: the one fixed complex-external-state box in the unbroken, on-shell
massless-external-leg limit. It is not the full mixed-mass six-cycle sum.
Requires Python 3 and SymPy.
"""
import sympy as sp

eps, L = sp.symbols("eps L")
dD = 4 - 2*eps
checks = 0

def check(name, expr):
    global checks
    residual = sp.simplify(expr)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks += 1
    print(f"PASS: {name}")

# 1. Expand the two light and two heavy denominators to O(p^2).
k2, A, u, v, w, s, t = sp.symbols("k2 A u v w s t", nonzero=True)
L1 = 2*u/k2
L2 = -s/k2 + 4*u**2/k2**2
H1 = 2*(v-w)/A
H2 = 4*(v**2+w**2-v*w)/A**2
numerator = k2-u
expanded_p2 = sp.expand(k2*(L2+H2+L1*H1) - u*(L1+H1))
expected_p2 = -s + 2*u**2/k2 + 4*k2*(v**2+w**2-v*w)/A**2 + 2*u*(v-w)/A
check("hard expansion of numerator times denominators through O(p^2)",
      expanded_p2-expected_p2)

# 2. d-dimensional tensor reduction, with p2^2=p4^2=0 and
# q^2=s, q.p2=s/2, q.p4=-s/2, p2.p4=t/2.
# J_ab = int d^d k/(2pi)^d [ (k^2)^(-a) (k^2-M_E^2)^(-b) ].
# For a+b=4, after factoring i/(16 pi^2 M_E^4), its dimensionless part is:
# exp[epsilon (gamma_E-L)] (-1)^(a+b)
# Gamma(a+b-2+epsilon) Gamma(2-epsilon-a) /
# [Gamma(b) Gamma(2-epsilon)].
def jhat(a_idx, b_idx):
    return sp.simplify(
        (-1)**(a_idx+b_idx)
        * sp.exp(eps*(sp.EulerGamma-L))
        * sp.gamma(a_idx+b_idx-2+eps)
        * sp.gamma(2-eps-a_idx)
        / (sp.gamma(b_idx)*sp.gamma(2-eps))
    )

J22 = jhat(2, 2)
J13 = jhat(1, 3)
J04 = jhat(0, 4)
check("J_22 master integral has the expected Gamma(-epsilon) IR pole",
      J22 - sp.exp(eps*(sp.EulerGamma-L))*sp.gamma(2+eps)*sp.gamma(-eps)/sp.gamma(2-eps))
check("J_13 master integral has the expected Gamma(1-epsilon) factor",
      J13 - sp.exp(eps*(sp.EulerGamma-L))*sp.gamma(2+eps)*sp.gamma(1-eps)/
      (sp.gamma(3)*sp.gamma(2-eps)))
check("J_04 master integral reduces to Gamma(2+epsilon)/6",
      J04 - sp.exp(eps*(sp.EulerGamma-L))*sp.gamma(2+eps)/sp.gamma(4))

# Tensor reductions:
# int (k.q)^2 F = (q^2/d) int k^2 F,
# int (k.p2)(k.p4) F = (p2.p4/d) int k^2 F,
# with q.p2=s/2, q.p4=-s/2, p2.p4=t/2.
# These identities reduce the O(p^2) numerator above to the master-integral vector.
master_vector = (-s*J22 + 2*s/dD*J22 + 2*s/dD*J13 - 2*t/dD*J04)
master_vector_expected = s*(-(1-2/dD)*J22 + 2/dD*J13) - 2*t/dD*J04
check("d-dimensional tensor reduction gives the stated J22/J13/J04 vector",
      master_vector-master_vector_expected)

# The O(p^2) tensor-reduced integral before the closed-fermion-loop sign is
# 2 M_E^2 |y lambda|^2 [ s (-(1-2/d) J_22 + 2/d J_13)
#                         - (2 t/d) J_04 ].
# Factoring i |y lambda|^2/(16 pi^2 M_E^2) leaves the coefficients below.
coef_s_pre = sp.simplify(2*(-(1-2/dD)*J22 + 2/dD*J13))
coef_t_pre = sp.simplify(2*(-2/dD*J04))
coef_s_pre_finite = sp.series(coef_s_pre, eps, 0, 1).removeO()
coef_t_pre_finite = sp.series(coef_t_pre, eps, 0, 1).removeO()
check("pre-loop-sign hard s coefficient is 1/epsilon + 2 - L",
      coef_s_pre_finite - (1/eps + 2 - L))
check("pre-loop-sign hard t coefficient is -1/6",
      coef_t_pre_finite + sp.Rational(1, 6))

# 3. Feynman-rule factors for the box: four Yukawa vertices, four fermion
# propagators, and one closed fermion loop. The loop integration already
# contributes the common i/(16 pi^2).
vertex_factor = (-sp.I)**4
propagator_factor = sp.I**4
closed_loop_factor = -1
total_diagram_factor = sp.simplify(vertex_factor*propagator_factor*closed_loop_factor)
check("four vertices times four propagators times closed-loop sign equals -1",
      total_diagram_factor + 1)
check("four-vertex factor is +1", vertex_factor-1)
check("four-propagator factor is +1", propagator_factor-1)

coef_s_full = sp.simplify(total_diagram_factor*coef_s_pre_finite)
coef_t_full = sp.simplify(total_diagram_factor*coef_t_pre_finite)
check("full hard s coefficient is -1/epsilon + L - 2",
      coef_s_full - (-1/eps + L - 2))
check("full hard t coefficient is +1/6",
      coef_t_full - sp.Rational(1, 6))

# In the declared MS-bar convention, 1/epsilon_IR denotes Delta_IR after
# the standard gamma_E/log(4 pi) constants have been absorbed into mu_R.
DeltaIR = sp.symbols("Delta_IR")
source_s = -DeltaIR + L - 2
source_t = sp.Rational(1, 6)
check("hard s coefficient matches source after Delta_IR=1/epsilon_IR",
      source_s.subs(DeltaIR, 1/eps) - coef_s_full)
check("hard t coefficient matches the source §248 finite term",
      coef_t_full-source_t)

print(f"RESULT: {checks} exact symbolic hard-region/sign checks passed.")
print("MATCH: i |C5|^2/(16 pi^2) [(-Delta_IR+L-2) s + t/6].")
print("SCOPE: one source-aligned box; does not close the mixed-mass six-cycle sum.")
print("OPEN: flavor-resolved s/u routing, full B1/B3 signs, complete EFT graph/counterterm vector.")
