#!/usr/bin/env python3
"""Audit the C5-squared EFT soft-potential pole in the X^2Y^2 representative.

This checks the leading-seesaw reduction of the C5^2 light-fermion soft pole
to the X^2Y^2 potential counterterm identified in master §§262.5 and 264.4.
It does not determine the complete dimension-eight hard Wilson coefficient
or include all higher-dimensional EFT soft insertions.
"""
import sympy as sp

Y2, Lam2, vh, vs, ME, Delta = sp.symbols(
    "abs_y_squared abs_lambda_squared v_h v_s M_E Delta_UV", positive=True
)
h, s, c8 = sp.symbols("h s c8", real=True)

# Leading seesaw counting, with ME the heavy mass (not its square).
q_lead = Y2 * Lam2 * vh * vs / (2 * ME**2)
x_lead = Y2 * Lam2 * vh**2 * vs**2 / (4 * ME**2)
subset_pole = sp.simplify(8 * q_lead * x_lead * Delta / (16 * sp.pi**2))
expected_pole = Y2**2 * Lam2**2 * vh**3 * vs**3 * Delta / (16 * sp.pi**2 * ME**4)
assert sp.simplify(subset_pole - expected_pole) == 0
print("PASS 1: 8 q_l x_l Delta/(16 pi^2) scales as |y|^4 |lambda|^4 v_h^3 v_s^3/(16 pi^2 M_E^4)")

X = (vh + h)**2 / 2
Y = (vs + s)**2 / 2
mixed_hessian = sp.diff(X**2 * Y**2, h, s).subs({h: 0, s: 0})
assert sp.simplify(mixed_hessian - vh**3 * vs**3) == 0
print("PASS 2: mixed Hessian of (H^dagger H)^2(S^dagger S)^2 is v_h^3 v_s^3")

# Gamma_inv = p^2 - M_loc^2 + Pi. A potential counterterm enters Pi as
# minus the mixed Hessian of V_ct, since L_ct = -V_ct.
Pi_ct_from_potential = -c8 * mixed_hessian / ME**4
c8_ct = -Y2**2 * Lam2**2 * Delta / (16 * sp.pi**2)
assert sp.simplify(Pi_ct_from_potential.subs(c8, c8_ct) - expected_pole) == 0
print("PASS 3: the C5^2 subset potential CT is delta c_8 = -|y|^4 |lambda|^4 Delta/(16 pi^2) in V, equivalently positive in L")

assert sp.simplify(subset_pole * ME**4 / (vh**3 * vs**3) - Y2**2 * Lam2**2 * Delta / (16 * sp.pi**2)) == 0
print("PASS 4: the candidate is dimension-eight order O(M_E^-4), not the leading portal threshold")
print("LIMIT: reproduces the C5^2 soft-potential counterterm in the X^2Y^2 representative; not the complete dimension-eight Wilson vector.")
print("OPEN: higher-dimensional tree-level EFT soft insertions and the complete dimension-eight hard matching remain outstanding.")
