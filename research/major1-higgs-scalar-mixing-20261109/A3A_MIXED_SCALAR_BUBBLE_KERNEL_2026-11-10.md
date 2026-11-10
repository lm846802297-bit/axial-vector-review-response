# Major Point 1 — A3a mixed scalar-bubble kernel and portal UV counterterm

**Scope:** derive the complete one-loop-topology scalar/Goldstone \(hs\) bubble subset in the gauge basis, at first order in the portal coupling. This is a subcalculation of the \(O(\hbar^2)\) combined expansion when \(\lambda_{HS}=O(\hbar)\). It is not the complete \(O(\hbar^2)\) UV--EFT matching.

## 1. Generic momentum-dependent kernel

Use the cubic derivatives \(\kappa_{ijk}=\partial_i\partial_j\partial_kV|_{\rm vev}\) from A2. With
\[
B_0(p^2;m^2,m^2)=\frac{1}{\bar\epsilon}
-\int_0^1dx\,
\ln\frac{m^2-x(1-x)p^2-i0}{\mu^2},
\]
the mixed scalar-bubble subset is
\[
\boxed{\begin{aligned}
\Pi_{hs}^{\rm scalar}(p^2)=\frac{1}{16\pi^2}\lambda_{HS}vv_S\bigg[&
3\lambda_H B_0(p^2;m_h^2,m_h^2)
+3\lambda_S B_0(p^2;m_s^2,m_s^2)\\
&+2\lambda_H B_0(p^2;\xi_Wm_W^2,\xi_Wm_W^2)\\
&+\lambda_H B_0(p^2;\xi_Zm_Z^2,\xi_Zm_Z^2)\\
&+\lambda_S B_0(p^2;\xi_Xm_X^2,\xi_Xm_X^2)
\bigg],
\end{aligned}}
\]
where the overall sign follows the adopted \(\Gamma_{\rm inv}=p^2I-\mathcal M_0^2+\Pi\) convention. The coefficients include the identical-particle symmetry factors; \(G^+G^-\) has no factor \(1/2\).

The first two terms are the CP-even radial bubbles already present in the archived P2-lite subset. The last three are the Goldstone additions identified by A2. This formula is a gauge-basis expression; it must not be supplemented with physical-state \(sWW\) or \(hA'A'\) vertices.

## 2. UV pole and portal counterterm

The five individual coupling products, including symmetry factors, are
\[
\begin{array}{c|c}
hh&3\lambda_H\lambda_{HS}vv_S\\
ss&3\lambda_S\lambda_{HS}vv_S\\
G^+G^-&2\lambda_H\lambda_{HS}vv_S\\
G^0G^0&\lambda_H\lambda_{HS}vv_S\\
aa&\lambda_S\lambda_{HS}vv_S
\end{array}
\]
and therefore
\[
\boxed{
\Pi_{hs}^{\rm scalar,UV}
=\frac{\lambda_{HS}vv_S}{16\pi^2\bar\epsilon}
(6\lambda_H+4\lambda_S).
}
\]
The corresponding portal counterterm pole has the same coefficient in the convention stated above:
\[
\boxed{
\delta\lambda_{HS}^{\rm scalar}
=\frac{\lambda_{HS}}{16\pi^2\bar\epsilon}
(6\lambda_H+4\lambda_S).
}
\]
This is the scalar-potential contribution only. Gauge and Yukawa terms in the portal renormalization, tadpole/VEV renormalization, and the VLL hard matching must be included before quoting the complete portal beta function or a physical mixed mass counterterm.

The UV pole is independent of \(\xi_W,\xi_Z,\xi_X\), as expected. The finite part depends on the Goldstone masses and is not a physical mixing prediction by itself.

## 3. Matching warning: do not insert the UV portal twice

The reference condition in the existing threshold note is
\[
\lambda_{HS}^{\rm EFT}(M_E)=0,\qquad
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{\rm hard}.
\]
The scalar-bubble formula above is written for a generic renormalized portal vertex before the full matching insertions are assembled. In the UV calculation, the tree portal, VLL hard threshold/counterterm insertion, and portal renormalization must be combined at the same order. In the EFT calculation, the corresponding matched portal vertex is used. It is incorrect to evaluate the UV scalar bubbles with \(\lambda_{HS}^{\rm UV}\), set the EFT scalar bubbles to zero, and call their difference a hard threshold without including the portal matching insertion in the soft subgraphs.

Accordingly, no numerical finite \(hs\) correction is quoted here. The formula is the analytic scalar-bubble kernel and its UV pole; its matched finite contribution is pending the complete two-loop matching ledger.

## 4. Gauge and diagram boundary

There is no one-loop \(hs\) vector or ghost bubble in the gauge basis: \(h\) and \(s\) do not share a vector or ghost species. The \(\xi\)-dependent finite Goldstone terms must be combined with the rest of the same-order calculation and counterterms. They are not separately physical. The genuine two-loop gauge/Yukawa corrections to the fermion-induced portal and the complete diagonal self-energies also remain outside this A3a subset.

## 5. Validation

The accompanying SymPy script independently verifies all five symmetry-weighted coupling products and the sum \(6\lambda_H+4\lambda_S\). It is an algebraic UV-pole audit, not a loop-integral or gauge-independence test.
