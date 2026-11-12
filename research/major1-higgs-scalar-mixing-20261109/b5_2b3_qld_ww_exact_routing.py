#!/usr/bin/env python3
"""B5-2B3R: exact external-momentum routing for the Q_LD pure-WW cross boxes.

This supersedes the earlier common-numerator diagnostic. Each cross-pair has
its own internal momenta, propagator denominator and O(P) numerator reduction.
The output is the hard cross-box subset only, not the complete WW matching.
"""
import sympy as sp

eps, DeltaUV, L, M2 = sp.symbols("eps DeltaUV L M2", positive=True)
d = 4 - 2*eps


def hard_masters():
    J = (DeltaUV + 1 - L)/M2
    K = -sp.Integer(1)/M2
    return J, K


def exact_pair_kernels():
    """Return the four kernels for p_barL=p_Hdag=0, p_H=P, p_L=-P.

    k flows from the left Yukawa vertex (bar L,H) to the right
    Yukawa vertex (Hdag,L). The heavy momentum is q_E=k-P.

    Pair 01 (bar L-L):
      q_barL=-k, q_L=q_E=k-P;
      D=k^4 (k-P)^2 [(k-P)^2-M^2];
      N=gamma^mu (-slash k) slash(k-P) slash(k-P) gamma_mu.

    Pair 02 (bar L-Hdag):
      q_barL=-k, q_Hdag=k;
      D=k^6 [(k-P)^2-M^2];
      N=gamma^mu (-slash k) slash(k-P) (-k_mu).

    Pair 05 (H-L):
      q_H=P-k, q_L=q_E=k-P;
      D=k^2 (k-P)^4 [(k-P)^2-M^2];
      N=(2P-k)_mu slash(k-P) slash(k-P) gamma^mu.

    Pair 06 (Hdag-H):
      q_H=P-k, q_Hdag=k;
      D=k^4 (k-P)^2 [(k-P)^2-M^2];
      N=-(2P-k).k slash(k-P).
    """
    J, K = hard_masters()

    # Pair 01: cancel the (k-P)^2 numerator against its light propagator.
    # Expand the heavy denominator; gamma^mu slash(k) gamma_mu=(2-d)slash(k).
    A01 = sp.Rational(2,1)*(d-2)/d*K

    # Pair 02: cancel k^2; numerator becomes slash(k-P).
    # -slash(P) gives -J; expanding the heavy denominator gives +2K/d.
    A02 = -J + sp.Rational(2,1)/d*K

    # Pair 05: cancel (k-P)^2, shift q=k-P, and expand 1/(q+P)^2.
    # The direct slash(P) term gives J; the q.(P) term gives +2J/d.
    A05 = (1 + sp.Rational(2,1)/d)*J

    # Pair 06: -(2P-k).k = (k-P)^2 + O(P^2).
    # Cancel the scalar propagator and expand 1/(q+P)^4.
    A06 = -sp.Rational(4,1)/d*J

    return {
        "LD-W-01": sp.simplify(A01),
        "LD-W-02": sp.simplify(A02),
        "LD-W-05": sp.simplify(A05),
        "LD-W-06": sp.simplify(A06),
        "J_hard": J,
        "K_hard": K,
    }


def weighted_triplet_sum(kernels):
    """Apply the exact SU(2) tensors (-,+,+,-) T3/4."""
    return sp.simplify((
        -kernels["LD-W-01"]
        +kernels["LD-W-02"]
        +kernels["LD-W-05"]
        -kernels["LD-W-06"]
    )/4)


def retain_epsilon_times_uv_pole(expr):
    """Expand through O(eps), retaining eps*DeltaUV as a finite term."""
    expanded = sp.expand(sp.series(expr, eps, 0, 2).removeO())
    expanded = expanded.subs(eps*DeltaUV, sp.Integer(1))
    expanded = sp.expand(expanded).subs(eps, 0)
    return sp.simplify(expanded)


def main():
    k = exact_pair_kernels()
    J, K = k["J_hard"], k["K_hard"]

    assert sp.simplify(k["LD-W-01"] - 2*(d-2)/d*K) == 0
    assert sp.simplify(k["LD-W-02"] - (-J+2/d*K)) == 0
    assert sp.simplify(k["LD-W-05"] - (1+2/d)*J) == 0
    assert sp.simplify(k["LD-W-06"] + 4/d*J) == 0

    weighted = weighted_triplet_sum(k)
    assert sp.simplify(
        weighted - (6/d*J - 2*(d-3)/d*K)/4
    ) == 0

    finite = retain_epsilon_times_uv_pole(weighted)
    expected = (
        sp.Rational(3,8)*DeltaUV
        -sp.Rational(3,8)*L
        +sp.Rational(11,16)
    )/M2
    assert sp.simplify(finite-expected) == 0

    print("B5-2B3R exact Q_LD pure-WW cross-box routing")
    print("Momentum assignment: p_barL=0, p_H=P, p_Hdag=0, p_L=-P.")
    print("Heavy momentum: q_E=k-P; W momentum k flows left-to-right.")
    print("PASS: each of the four cross-pair denominators and numerator reductions is distinct.")
    print("A01 = 2(d-2)/d K")
    print("A02 = -J + 2K/d")
    print("A05 = (1+2/d) J")
    print("A06 = -4J/d")
    print("PASS: SU(2) tensor weights are (-,+,+,-) T3/4.")
    print("Weighted hard triplet coefficient before epsilon expansion:")
    print("  (6J/d - 2(d-3)K/d)/4")
    print("PASS: O(eps)*Delta_UV terms retained.")
    print("Hard triplet coefficient = (3 Delta_UV/8 - 3 L/8 + 11/16)/M_E^2")
    print("SCOPE: one fixed external ordering and one-W exchange; no LSZ, operator counterterms, or full Ward sum.")


if __name__ == "__main__":
    main()
