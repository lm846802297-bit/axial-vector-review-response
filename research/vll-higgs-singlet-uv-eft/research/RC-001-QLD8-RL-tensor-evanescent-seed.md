# RC-001 QLD8: direct-pairing \(RL\) tensor evanescent seed

**Date:** 2026-11-10  
**Stage:** P1.1c — Dirac-chain decomposition for the \(d^\dagger d\) QCD pilot  
**Status:** the formal \(d\)-dimensional gamma decomposition and the exact 4D vanishing of the opposite-chirality tensor contraction are established. The complete graph numerator and its UV pole are not calculated.

## 1. The two-gamma open-line chain

For the direct source pairing in the \(d^\dagger d\) channel,
\[
(\bar Q P_R d)(\bar d P_L Q),
\]
a two-gamma open-line chain has the Dirac structure
\[
\left(\gamma^\mu\gamma^\nu P_R\right)
\otimes
\left(P_L\gamma_\nu\gamma_\mu\right).
\]
Use
\[
\gamma^\mu\gamma^\nu=g^{\mu\nu}-i\sigma^{\mu\nu},
\qquad
\gamma_\nu\gamma_\mu=g_{\mu\nu}+i\sigma_{\mu\nu},
\qquad
[\sigma^{\mu\nu},\gamma_5]=0.
\]
The cross terms vanish after contraction because the metric is symmetric and
\(\sigma^{\mu\nu}\) is antisymmetric. Thus, in \(D\) dimensions,
\[
\boxed{
\left(\gamma^\mu\gamma^\nu P_R\right)
\otimes
\left(P_L\gamma_\nu\gamma_\mu\right)
=
D\,P_R\otimes P_L
+
\sigma^{\mu\nu}P_R\otimes\sigma_{\mu\nu}P_L.
}
\]
This identity is an algebraic reduction of the displayed gamma chain. It does not by itself assert that a particular complete one-loop graph has this numerator with unit coefficient; that requires the graph's propagator routing, vertex ordering, and Feynman-rule signs.

## 2. The direct \(RL\) tensor contraction is evanescent

In exactly four dimensions, \(\sigma^{\mu\nu}P_R\) and
\(\sigma^{\mu\nu}P_L\) have opposite duality. Therefore
\[
\boxed{
(\bar Q\sigma^{\mu\nu}P_R d)
(\bar d\sigma_{\mu\nu}P_L Q)=0
\qquad (D=4).
}
\]
The exact \(4\times4\) gamma-matrix representation check also verifies the corresponding \(16\times16\) spinor-index tensor product vanishes.

In \(D=4-2\epsilon\), this contraction is not set to zero. A direct-pairing evanescent seed is
\[
E_{T;RL}^{\rm dir}
=
(\bar Q\sigma^{\mu\nu}P_R d)
(\bar d\sigma_{\mu\nu}P_L Q).
\]
No \(O(\epsilon)\) physical-operator admixture is included in this definition.

Combining this with the gamma-chain decomposition gives
\[
(4-2\epsilon)\,O_{S;RL}+E_{T;RL}^{\rm dir},
\qquad
O_{S;RL}=(\bar QP_Rd)(\bar dP_LQ).
\]
The \(-2\epsilon\,O_{S;RL}\) term must be retained: when multiplied by a \(1/\epsilon\) UV pole it contributes to the finite local term. It cannot be replaced by \(4O_{S;RL}\) before the UV subtraction.

## 3. Direct tensor versus crossed odd-rank channels

The scalar–vector Fierz difference \(E_{RL;V}^{\mu,rs}\) is not the direct
Fierz image of this Lorentz-scalar tensor–tensor structure: it starts from
scalar \(\times\) vector and carries one open Lorentz index.

Likewise, distinguish the direct-pairing rank-three seed
\[
E_{3;RL}^{\rm dir}
=(\bar Q\Gamma_{(3)}P_Rd)(\bar d\Gamma_{(3)}P_LQ)
-6\eta_R\eta_L
(\bar Q\gamma^\mu P_Rd)(\bar d\gamma_\mu P_LQ)
\]
from the crossed rank-three channel
\[
X_3^{RL}
=(\Gamma^{\mu\nu\rho}P_R)\widetilde\otimes
(\Gamma_{\mu\nu\rho}P_L).
\]
They have different spinor pairings and must not be identified before the
Grassmann exchange and d-dimensional Fierz map are applied.

The formal crossed odd-rank projection of \(E_{T;RL}^{\rm dir}\) is now
derived in
\`research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md\`.
For odd \(n\), its coefficient is
\[
f_n(D)=
\frac{D(D-1)-4n(D-n)}
{2(-1)^{n(n-1)/2}D(D-1)\cdots(D-n+1)}.
\]
In particular, \(f_1=-3\epsilon/4+O(\epsilon^2)\) and
\(f_3=-5\epsilon/24+O(\epsilon^2)\), while the rank-five projection
coefficient has a \(1/\epsilon\) singularity because its Gram norm vanishes
at \(D=4\). This is a basis-projection singularity, not a loop UV pole.

Therefore the direct tensor cannot be removed by a regular finite basis
change involving only crossed rank-one and rank-three structures. Keep the
direct tensor, the direct-pairing \(E_{3;RL}^{\rm dir}\), and the crossed
odd-rank channels separately labelled until the actual one-loop gamma-rank
closure and the relevant Gram matrix are known. Do not identify the direct
tensor with \(E_{RL;V}\), and do not double-count the direct and crossed
rank-three objects.

## 4. Validation boundary

The companion exact gamma-matrix audit checks:
1. the \(D=4\) direct \(RL\) tensor contraction vanishes;
2. the displayed gamma-chain identity reduces to \(4P_R\otimes P_L+E_{T;RL}^{\rm dir}\) in four dimensions;
3. the chiral projectors and Minkowski metric use the same conventions as the existing QLD8 Fierz audit.

This establishes a candidate evanescent structure and its \(D\)-dependence. It does not calculate the one-loop graph coefficient, the loop integral, the UV pole, the mixing into \(E_{RL}^{(rs)}\) or \(E_{3;RL}\), or the finite matching term.


## 5. P1.2 d-dimensional crossed projection

The formal rank-\(n\) projection and its higher-rank Gram obstruction are
recorded in
\`research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md\`.
The companion symbolic audit passes locally. It checks the explicit
four-dimensional \(\sigma\Gamma^{(n)}\sigma\) eigenvalues for \(n=0,\ldots,4\),
the analytic \(f_1,f_3,f_5\) formulas, and the \(D=4-2\epsilon\) limits.

The rank-five \(1/\epsilon\) in \(f_5\) is purely from inversion of a Gram
direction whose norm vanishes at \(D=4\); it must not be interpreted as a
loop divergence. No finite independent evanescent basis or loop counterterm
matrix is claimed.
