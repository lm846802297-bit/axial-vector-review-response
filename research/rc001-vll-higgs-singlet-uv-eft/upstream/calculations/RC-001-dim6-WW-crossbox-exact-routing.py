#!/usr/bin/env python3
"""Explicit numerator/denominator expansion for the fixed-routing Q_LD WW boxes.

Scope:
- ordered amplitude barL(p1) H(p2) Hdag(p3) L(p4);
- p1=p3=0, p2=P, p4=-P, with q=k-P;
- one unit of each cross-vertex attachment class;
- Feynman gauge and d=4-2 eps.

The script derives the four local slash(P) kernels from the stated numerator
chains and denominators. It then performs the scalar-master hard/soft split.
It is not a diagram generator and does not determine additional routing
multiplicities or the complete gauge-invariant Wilson coefficient.
"""
import sympy as sp

eps = sp.symbols("eps", positive=True)
DeltaUV, DeltaIR, L, M2 = sp.symbols(
    "Delta_UV Delta_IR L M_E2", real=True
)
cUV, cIR = sp.symbols("c_UV c_IR", real=True)
d = 4 - 2*eps

# Symbols for x=k^2 and t=k.P. P^2 is dropped after the linear local projection.
x, t = sp.symbols("x t", nonzero=True)
M2_local = sp.symbols("M2_local", nonzero=True)


def _linear_t(expr):
    """Taylor-expand a scalar coefficient through first order in t=k.P."""
    return sp.expand(sp.series(expr, t, 0, 2).removeO())


def _slashP_coefficient(k_coeff, p_coeff, dim):
    """Integrate V_mu = k_mu*k_coeff + P_mu*p_coeff to O(P).

    Odd k terms vanish. For the linear term use
      int k_mu (k.P) f(k^2) = P_mu/d int k^2 f(k^2).
    """
    kc = _linear_t(k_coeff)
    pc = _linear_t(p_coeff)
    k_t = sp.simplify(sp.diff(kc, t).subs(t, 0))
    p_0 = sp.simplify(pc.subs(t, 0))
    return sp.factor(p_0 + x*k_t/dim)


def derive_pair_integrands():
    """Derive each P-slash integrand from its numerator and denominators.

    q=k-P, q^2=x-2t at O(P). The four numerator chains are:
      01: gamma_mu (-k/) q/ q/ gamma^mu;
      02: gamma_mu (-k/) q/ (-k^mu);
      05: (2P-k)_mu q/ q/ gamma^mu;
      06: -[(2P-k).k] q/.

    After gamma contractions, these are represented as Lorentz vectors.
    The returned expressions are the coefficients of P/ before loop
    integration, in terms of the two scalar-master integrands J(x), K(x).
    """
    q2 = x - 2*t
    heavy = x - M2_local - 2*t
    F = 1/(q2*(q2-M2_local))

    # 01: q^2 cancels against the right light-fermion denominator.
    c01 = _slashP_coefficient((d-2)/(x**2*heavy), 0, d)

    # 02: gamma_mu (-k/) q/ (-k^mu) = k^2 q/.
    c02 = _slashP_coefficient(1/(x**2*heavy), -1/(x**2*heavy), d)

    # 05: q/ q/ = q^2, leaving (2P/-k/) / [k^2 q^2(q^2-M^2)].
    c05 = _slashP_coefficient(-F/x, 2*F/x, d)

    # 06: -[(2P-k).k] = k^2-2 k.P = q^2 at O(P);
    # this cancels the scalar q^2 denominator and gives the same vector
    # integral as 02.
    c06 = _slashP_coefficient(1/(x**2*heavy), -1/(x**2*heavy), d)

    Jden = 1/(x**2*(x-M2_local))
    Kden = 1/(x*(x-M2_local)**2)
    return {
        "LD-W-01": (sp.factor(c01), Jden, Kden),
        "LD-W-02": (sp.factor(c02), Jden, Kden),
        "LD-W-05": (sp.factor(c05), Jden, Kden),
        "LD-W-06": (sp.factor(c06), Jden, Kden),
    }


def _decompose_JK(expr, Jden, Kden):
    aJ, aK = sp.symbols("aJ aK")
    numerator = sp.together(expr-aJ*Jden-aK*Kden).as_numer_denom()[0]
    solution = sp.solve(
        sp.Poly(sp.expand(numerator), x).coeffs(), (aJ, aK), dict=True
    )
    if len(solution) != 1:
        raise AssertionError(f"Could not uniquely decompose in J,K: {expr}")
    return sp.simplify(solution[0][aJ]), sp.simplify(solution[0][aK])


def derive_pair_kernels(J, K):
    """Return integrated pair kernels, obtained from explicit numerator chains."""
    result = {}
    for pair, (integrand, Jden, Kden) in derive_pair_integrands().items():
        aJ, aK = _decompose_JK(integrand, Jden, Kden)
        result[pair] = sp.simplify(aJ*J+aK*K)
    return result


def derive_longitudinal_pair_integrands():
    """Derive P-slash kernels after replacing g_munu by k_mu k_nu/k^2.

    This is the longitudinal projector entering a general R_xi W propagator.
    The returned coefficients are obtained from the same explicit momentum
    routing and numerator chains as derive_pair_integrands().
    """
    q2 = x-2*t
    heavy = x-M2_local-2*t
    F = 1/(q2*(q2-M2_local))

    # 01: k_mu gamma^mu (-k/) q/ q/ k_nu gamma^nu / k^2
    #     = -q^2 k/; cancel q^2 in the two-fermion/heavy denominator.
    c01 = _slashP_coefficient(-1/(x**2*heavy), 0, d)

    # 02: the fermion and scalar endpoint contractions each supply k^2;
    #     after the projector 1/k^2, this equals the Feynman-gauge numerator.
    c02 = _slashP_coefficient(1/(x**2*heavy), -1/(x**2*heavy), d)

    # 05: (a.k) q^2 k/ / k^2 with a=2P-k; retain the O(P) expansion.
    c05 = _slashP_coefficient((2*t-x)*F/x**2, 0, d)

    # 06: the two scalar endpoint contractions give q^2 at O(P), same as 02.
    c06 = _slashP_coefficient(1/(x**2*heavy), -1/(x**2*heavy), d)

    Jden = 1/(x**2*(x-M2_local))
    Kden = 1/(x*(x-M2_local)**2)
    return {
        "LD-W-01": (sp.factor(c01), Jden, Kden),
        "LD-W-02": (sp.factor(c02), Jden, Kden),
        "LD-W-05": (sp.factor(c05), Jden, Kden),
        "LD-W-06": (sp.factor(c06), Jden, Kden),
    }


def derive_longitudinal_pair_kernels(J, K):
    result = {}
    for pair, (integrand, Jden, Kden) in derive_longitudinal_pair_integrands().items():
        aJ, aK = _decompose_JK(integrand, Jden, Kden)
        result[pair] = sp.simplify(aJ*J+aK*K)
    return result


def longitudinal_weighted_sum(kernels):
    return sp.simplify((
        -kernels["LD-W-01"]
        +kernels["LD-W-02"]
        +kernels["LD-W-05"]
        -kernels["LD-W-06"]
    )/4)


def scalar_masters():
    """Common scalar-master expansion by regions through O(M_E^-2)."""
    J_hard = (DeltaUV + 1 - L) / M2
    J_soft = (-DeltaUV + DeltaIR) / M2
    J_full = (DeltaIR + 1 - L) / M2

    # K = int 1/[k^2 (k^2-M_E^2)^2] = -1/M_E^2 + O(eps);
    # its soft expansion at O(M_E^-2) is a scaleless power integral.
    K_hard = -sp.Integer(1) / M2
    K_soft = sp.Integer(0)
    K_full = K_hard
    return {
        "hard": (J_hard, K_hard),
        "soft": (J_soft, K_soft),
        "full": (J_full, K_full),
    }


def weak_weighted_sum(kernels):
    """Apply the exact SU(2) triplet weights (-,+,+,-)/4."""
    return sp.simplify((
        -kernels["LD-W-01"]
        +kernels["LD-W-02"]
        +kernels["LD-W-05"]
        -kernels["LD-W-06"]
    ) / 4)


def pole_expansion(expr):
    """Expand UV and IR pole labels separately, retaining eps*1/eps terms."""
    substituted = expr.subs({
        DeltaUV: 1/eps + cUV,
        DeltaIR: 1/eps + cIR,
    })
    return sp.simplify(sp.series(substituted, eps, 0, 1).removeO())


def gamma_function_j_minus_k():
    """Direct gamma-function evaluation of J_full-K_full.

    The explicit (4*pi)^eps factor fixes the same Delta=1/eps-gamma+ln(4*pi)
    pole convention used by the scalar-master record.
    """
    return (
        -sp.exp(eps*(sp.log(4*sp.pi)-L))
        *sp.gamma(2+eps)*sp.gamma(-eps)
        /sp.gamma(2-eps)/M2
    )


def expected_hard():
    return (
        sp.Rational(3,8)*(1/eps+cUV)
        -sp.Rational(3,8)*L
        +sp.Rational(11,16)
    )/M2


def expected_soft():
    return sp.Rational(3,8)*(cIR-cUV)/M2


def expected_full():
    return (
        sp.Rational(3,8)*(1/eps+cIR)
        -sp.Rational(3,8)*L
        +sp.Rational(11,16)
    )/M2


def main():
    derived = derive_pair_integrands()
    Jden, Kden = 1/(x**2*(x-M2_local)), 1/(x*(x-M2_local)**2)
    expected_integrands = {
        "LD-W-01": 2*(d-2)/d*Kden,
        "LD-W-02": -Jden+2*Kden/d,
        "LD-W-05": 2*(1-1/d)*Jden-2*Kden/d,
        "LD-W-06": -Jden+2*Kden/d,
    }
    for pair, (integrand, _, _) in derived.items():
        assert sp.simplify(integrand-expected_integrands[pair]) == 0

    # This equality follows from the explicit numerator cancellation q^2
    # = k^2 - 2 k.P at the retained order, not from an assumed symmetry.
    assert sp.simplify(
        expected_integrands["LD-W-02"]-expected_integrands["LD-W-06"]
    ) == 0

    masters = scalar_masters()
    kernels = {
        region: derive_pair_kernels(*masters[region])
        for region in ("hard", "soft", "full")
    }
    sums = {
        region: weak_weighted_sum(kernels[region])
        for region in ("hard", "soft", "full")
    }

    # The longitudinal R_xi projector cancels in the weak-triplet sum.
    longitudinal = derive_longitudinal_pair_kernels(
        sp.Symbol("J"), sp.Symbol("K")
    )
    assert sp.simplify(longitudinal_weighted_sum(longitudinal)) == 0

    # The weighted integrand collapses to (d-1)/(2d) (J-K).
    for region in ("hard", "soft", "full"):
        J, K = masters[region]
        assert sp.simplify(
            sums[region]-(d-1)*(J-K)/(2*d)
        ) == 0

    # Pairwise and master-level hard/soft/full closure.
    for pair in kernels["hard"]:
        assert sp.simplify(
            kernels["full"][pair]
            -kernels["hard"][pair]
            -kernels["soft"][pair]
        ) == 0
    JH, KH = masters["hard"]
    JS, KS = masters["soft"]
    JF, KF = masters["full"]
    assert sp.simplify(JF-JH-JS) == 0
    assert sp.simplify(KF-KH-KS) == 0

    hard_exp = pole_expansion(sums["hard"])
    soft_exp = pole_expansion(sums["soft"])
    full_exp = pole_expansion(sums["full"])
    assert sp.simplify(hard_exp-expected_hard()) == 0
    assert sp.simplify(soft_exp-expected_soft()) == 0
    assert sp.simplify(full_exp-expected_full()) == 0
    assert sp.simplify(hard_exp+soft_exp-full_exp) == 0

    # Independent direct gamma-function evaluation of the combined full
    # integral: J-K = -M_E^2 int d^d k/[k^4 (k^2-M_E^2)^2].
    gamma_master = gamma_function_j_minus_k()
    gamma_master_exp = sp.simplify(
        sp.series(gamma_master, eps, 0, 1).removeO()
    )
    expected_gamma_master = (
        1/eps-sp.EulerGamma+sp.log(4*sp.pi)+2-L
    )/M2
    assert sp.simplify(gamma_master_exp-expected_gamma_master) == 0
    gamma_weighted_exp = sp.simplify(
        sp.series((d-1)/(2*d)*gamma_master, eps, 0, 1).removeO()
    )
    expected_gamma_weighted = (
        sp.Rational(3,8)*(1/eps-sp.EulerGamma+sp.log(4*sp.pi))
        -sp.Rational(3,8)*L+sp.Rational(11,16)
    )/M2
    assert sp.simplify(gamma_weighted_exp-expected_gamma_weighted) == 0

    # f(d)=(d-1)/(2d)=3/8-eps/16+... . The hard master J-K has
    # Delta_UV+2-L, so the eps*Delta_UV term is -1/16.
    f_series = sp.series((d-1)/(2*d), eps, 0, 2).removeO()
    assert sp.simplify(f_series-(sp.Rational(3,8)-eps/sp.Integer(16))) == 0
    assert sp.simplify(
        sp.Rational(3,8)*2-sp.Rational(1,16)-sp.Rational(11,16)
    ) == 0

    print("RC-001 Q_LD pure-WW cross-box explicit numerator audit")
    print("External ordering: barL(p1) H(p2) Hdag(p3) L(p4)")
    print("Local projection: p1=p3=0, p2=P, p4=-P; q=k-P.")
    print("Explicit numerator/denominator reduction:")
    print("  LD-W-01 = 2(d-2) K/d")
    print("  LD-W-02 = -J + 2K/d")
    print("  LD-W-05 = 2(1-1/d) J - 2K/d")
    print("  LD-W-06 = -J + 2K/d")
    print("PASS: LD-W-02 and LD-W-06 agree after q^2 cancellation at O(P).")
    print("PASS: weak-weighted sum = (d-1)(J-K)/(2d).")
    print("Longitudinal R_xi kernels:")
    print("  LD-W-01: -2K/d")
    print("  LD-W-02: -J + 2K/d")
    print("  LD-W-05: -2K/d")
    print("  LD-W-06: -J + 2K/d")
    print("PASS: longitudinal triplet projection vanishes; this cross-box sub-block is xi-independent.")
    print("Weighted hard:")
    print("  A_hard = (3 Delta_UV/8 - 3 L/8 + 11/16)/M_E^2")
    print("Weighted soft:")
    print("  A_soft = 3(-Delta_UV + Delta_IR)/(8 M_E^2)")
    print("Weighted full:")
    print("  A_full = (3 Delta_IR/8 - 3 L/8 + 11/16)/M_E^2")
    print("PASS: hard/soft/full master split and pole bookkeeping.")
    print("O(eps) audit: f(d)=3/8-eps/16; the hard finite shift is -1/16.")
    print("SCOPE: one fixed ordered tree contraction, unit multiplicity.")
    print("NOT CLAIMED: second routing, diagram-generator multiplicities, full Ward sum, or complete Wilson coefficient.")


if __name__ == "__main__":
    main()
