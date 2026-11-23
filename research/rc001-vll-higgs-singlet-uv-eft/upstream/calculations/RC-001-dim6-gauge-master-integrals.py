#!/usr/bin/env python3
"""Exact-rational checks for RC-001 gauge-loop master-integral reductions.

This verifies Feynman-parameter algebra, epsilon-expansion coefficients,
partial fractions, and the stated UV/IR split of a scalar box master. It does
not generate diagrams or determine their complete Lorentz/group coefficients.
"""
import sympy as sp

x, D, L, eps, z, M2 = sp.symbols("x D L eps z M2", positive=True)

def main():
    iv = sp.integrate((1 - x) * (D - L - sp.log(x)), (x, 0, 1))
    is_ = sp.integrate(D - L - sp.log(x), (x, 0, 1))
    assert sp.simplify(iv - (D / 2 - L / 2 + sp.Rational(3, 4))) == 0
    assert sp.simplify(is_ - (D - L + 1)) == 0

    # Keep the O(epsilon) part of d=4-2*epsilon against the B0 UV pole.
    gamma, log4pi = sp.symbols("gamma_E log4pi")
    Dexpr = 1 / eps - gamma + log4pi
    dB0 = sp.series((4 - 2 * eps) * (Dexpr + 1 - L), eps, 0, 1).removeO()
    assert sp.simplify(dB0 - (4 * Dexpr + 2 - 4 * L)) == 0

    sig_v_raw = sp.expand((-2 + 2 * eps) * iv)
    sig_s_raw = sp.expand((4 - 2 * eps) * is_)
    # Since D contains 1/epsilon, eps*D contributes +1 to the finite part.
    sig_v = -D + L - sp.Rational(1, 2)
    sig_s = 4 * D - 4 * L + 2
    assert sp.simplify((sig_v_raw - sig_v).subs(eps * D, 1).subs(eps, 0)) == 0
    assert sp.simplify((sig_s_raw - sig_s).subs(eps * D, 1).subs(eps, 0)) == 0
    prop = sp.simplify(-sig_v - 2 * sig_s)
    assert prop == -7 * D + 7 * L - sp.Rational(7, 2)

    lhs = 1 / (z**2 * (z - M2))
    rhs = -1 / (M2**2 * z) - 1 / (M2 * z**2) + 1 / (M2**2 * (z - M2))
    assert sp.simplify(lhs - rhs) == 0

    uv, ir = sp.symbols("Delta_UV Delta_IR")
    j_full = ir + 1 - L
    j_soft = -uv + ir
    j_hard = uv + 1 - L
    assert sp.simplify(j_full - j_soft - j_hard) == 0

    print("Feynman-parameter integrals: PASS")
    print("Heavy-light vertex numerator d*B0: 4*Delta+2-4*L (O(epsilon)*UV-pole retained)")
    print("Heavy self-energy: Sigma_V(0)=-Delta+L-1/2; Sigma_S(0)=4Delta-4L+2")
    print("Chirality-preserving propagator insertion: -7Delta+7L-7/2")
    print("Crossed-box partial-fraction identity: PASS")
    print("UV/IR split: J_full-J_soft=J_hard= (Delta_UV+1-L)/M_E^2")
    print("SCOPE: no complete vertex/box amplitude, diagram multiplicity, or Wilson coefficient.")

if __name__ == "__main__":
    main()
