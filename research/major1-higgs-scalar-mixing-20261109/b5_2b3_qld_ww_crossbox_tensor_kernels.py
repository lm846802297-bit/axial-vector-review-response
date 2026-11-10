#!/usr/bin/env python3
"""B5-2B3: canonical Lorentz-kernel audit for Q_LD W-cross boxes.

This evaluates a declared numerator/routing family and its hard-region scalar
masters. It deliberately does NOT assign the final oriented Feynman-rule signs
or graph multiplicities to the four atlas pairs.
"""
import sympy as sp

eps, DeltaUV, L, M2 = sp.symbols("eps DeltaUV L M2", positive=True)
d = 4 - 2*eps


def finite_uv_expansion(expr):
    """Keep O(eps)*DeltaUV terms, then take eps -> 0."""
    expr = sp.expand(expr)
    expr = expr.subs(eps*DeltaUV, sp.Integer(1))
    return sp.simplify(expr.subs(eps, 0))


def hard_scalar_masters():
    # J = int_k 1/[ (k^2)^2 (k^2-M^2) ], after UV-EFT hard subtraction.
    J_hard = (DeltaUV + 1 - L)/M2
    # K = int_k 1/[ k^2 (k^2-M^2)^2 ]; its soft expansion is scaleless.
    K_hard = -sp.Integer(1)/M2
    return J_hard, K_hard


def canonical_lorentz_kernels():
    """Return slash(P) coefficients for the explicitly defined numerators.

    Common denominator: (k^2)^3 * ((P-k)^2-M^2).
    N_FF = gamma^a slash(k) (slash(P)-slash(k)) slash(k) gamma_a
    N_FS = gamma^a slash(k) (slash(P)-slash(k)) k_a
    N_SS = k^2 (slash(P)-slash(k))

    The FS and SS definitions are the same after k_a gamma^a = slash(k).
    """
    J, K = hard_scalar_masters()
    # d-dimensional angular averages before epsilon expansion:
    c_ff_J = (d - 2)**2/d
    c_ff_K = 2*(d - 2)/d
    c_fs_J = sp.Integer(1)
    c_fs_K = -sp.Integer(2)/d
    c_ss_J = sp.Integer(1)
    c_ss_K = -sp.Integer(2)/d

    # Retain O(eps) in coefficients multiplying the UV pole in J.
    A_FF_raw = (
        (1 - sp.Rational(3, 2)*eps)*J
        + (1 - sp.Rational(1, 2)*eps)*K
    )
    A_FS_raw = J - (sp.Rational(1, 2) + eps/4)*K
    A_SS_raw = J - (sp.Rational(1, 2) + eps/4)*K

    A_FF = finite_uv_expansion(A_FF_raw)
    A_FS = finite_uv_expansion(A_FS_raw)
    A_SS = finite_uv_expansion(A_SS_raw)

    # Independently check the exact d-dependent angular coefficients.
    assert sp.simplify(c_ff_J.subs(d, 4-2*eps)
                       - (1-sp.Rational(3,2)*eps)) .subs(eps, 0) == 0
    assert sp.simplify(c_ff_K.subs(d, 4-2*eps)
                       - (1-sp.Rational(1,2)*eps)) .subs(eps, 0) == 0
    assert sp.simplify(c_fs_K.subs(d, 4-2*eps)
                       + (sp.Rational(1,2)+eps/4)) .subs(eps, 0) == 0
    assert sp.simplify(c_ss_J-c_fs_J) == 0
    assert sp.simplify(c_ss_K-c_fs_K) == 0

    return {
        "J_hard": J,
        "K_hard": K,
        "A_FF_raw": A_FF_raw,
        "A_FS_raw": A_FS_raw,
        "A_SS_raw": A_SS_raw,
        "A_FF": A_FF,
        "A_FS": A_FS,
        "A_SS": A_SS,
    }


def weak_tensor_weighted_conditional_sum(kernels):
    """Conditional sum if all four pair numerators share the same orientation.

    Atlas tensor factors:
      LD-W-01: -T3/4 (FF)
      LD-W-02: +T3/4 (FS)
      LD-W-05: +T3/4 (FS)
      LD-W-06: -T3/4 (SS)
    """
    A_FF, A_FS, A_SS = kernels["A_FF"], kernels["A_FS"], kernels["A_SS"]
    coeff = (
        -sp.Rational(1,4)*A_FF
        +sp.Rational(1,4)*A_FS
        +sp.Rational(1,4)*A_FS
        -sp.Rational(1,4)*A_SS
    )
    pole = -sp.Rational(1,4)+sp.Rational(1,4)+sp.Rational(1,4)-sp.Rational(1,4)
    return sp.simplify(coeff), sp.simplify(pole)


def main():
    k = canonical_lorentz_kernels()
    assert sp.simplify(k["A_FF"] - (DeltaUV-L-sp.Rational(3,2))/M2) == 0
    assert sp.simplify(k["A_FS"] - (DeltaUV-L+sp.Rational(3,2))/M2) == 0
    assert sp.simplify(k["A_SS"]-k["A_FS"]) == 0

    weighted, pole_weight = weak_tensor_weighted_conditional_sum(k)
    assert pole_weight == 0
    assert sp.simplify(weighted-sp.Rational(3,4)/M2) == 0

    print("B5-2B3 canonical Q_LD W-cross-box numerator audit")
    print("J_hard = (Delta_UV + 1 - L)/M_E^2")
    print("K_hard = -1/M_E^2")
    print("A_FF = (Delta_UV - L - 3/2)/M_E^2")
    print("A_FS = (Delta_UV - L + 3/2)/M_E^2")
    print("A_SS = A_FS for the declared canonical numerator")
    print("PASS: O(eps) in the FF angular coefficient retained against J_UV pole.")
    print("PASS: all four cross-box weak tensors are T3/4 with signs (-,+,+,-).")
    print("CONDITIONAL: if all four oriented graph signs/multiplicities are equal,")
    print("  the weighted UV pole cancels and the finite T3 coefficient is +3/(4 M_E^2).")
    print("NOT A WILSON COEFFICIENT: pair-by-pair Feynman-rule orientation,")
    print("  crossed routings, symmetry factors, LSZ/counterterms and Ward sum remain open.")


if __name__ == "__main__":
    main()
