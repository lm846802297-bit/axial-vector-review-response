# A5b — restricted EFT RGE and hard/soft scale-cancellation audit

**Date:** 2026-11-10  
**Upstream calculation source:** high-energy-theory-research, RC-001 PR #11 head, commit ba13cf736d0c1b1bbfef732acfb4f1785162ae88  
**Model-application branch:** PR #69, research/major1-higgs-scalar-mixing-20261109  
**Status:** the \(C_5C_5^\ast\) contribution to the dimension-six mixed-derivative operator has a derived one-loop pole, beta-function contribution, and exact leading-log hard/soft cancellation. The scalar-only linear portal beta contribution is also imported from A3a. This is a **restricted sector result**, not the complete model EFT anomalous-dimension matrix or the complete \(O(\hbar^2)\) scalar-pole calculation.

## 1. Why this is the first A5b block

The upstream RC-001 source explicitly records:
- the leading finite dimension-four VLL portal threshold, with no additive \(|y_\ell|^2|\lambda_\ell|^2\) one-loop UV pole in that VLL determinant sector;
- the EFT \(C_5C_5^\ast\) light-fermion bubble plus the induced \(hs\bar\ell\ell\) contact tadpole;
- the derivative \(s=p^2\) pole and its local counterterm;
- the finite hard derivative coefficient;
- the \(O(M_E^{-4})\) constant pole and its dimension-eight \(X^2Y^2\) assignment.

It does **not** claim that all same-order EFT soft insertions, the complete model-level Wilson vector, or all gauge/Yukawa anomalous dimensions are closed. A5b therefore starts by extracting the RGE information that is actually supported by the existing pole, rather than inventing a complete beta-function matrix.

## 2. Dimension-six derivative operator: pole to beta function

Use the upstream normalization
\[
{\cal L}_{\rm EFT}\supset
\frac{c_{\partial HS}}{M_*^2}
\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S),
\qquad
\Delta\Pi^{(6)}(s)
=\frac{c_{\partial HS}v_hv_s}{M_*^2}s.
\]

For one flavor, the EFT bubble plus contact tadpole has
\[
\Pi_{\rm EFT}^{\ell}(s)\big|_{\rm pole}
=-\frac{q_\ell}{16\pi^2}(8m_\ell^2-s)\Delta_{\rm UV},
\qquad
q_\ell=2g_{h\ell}g_{s\ell}.
\]
The counterterm in the inverse kernel is
\[
\Pi_{\rm local\,CT}^{\ell}(s)\big|_{\rm pole}
=+\frac{q_\ell}{16\pi^2}(8m_\ell^2-s)\Delta_{\rm UV}.
\]
The \(s\)-coefficient therefore requires
\[
\boxed{
\delta c_{\partial HS}
=-\frac{M_*^2}{16\pi^2v_hv_s}
\sum_{\ell=\mu,\tau}q_\ell\,\Delta_{\rm UV}.
}
\]

At leading seesaw order,
\[
m_\ell\simeq\frac{|C_{5,\ell}|v_hv_s}{2},
\qquad
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_E},
\qquad
q_\ell\simeq\frac{2m_\ell^2}{v_hv_s}
=\frac{|C_{5,\ell}|^2v_hv_s}{2}.
\]
Consequently,
\[
\boxed{
\delta c_{\partial HS}
=-\frac{M_*^2}{32\pi^2}
\sum_\ell |C_{5,\ell}|^2\,\Delta_{\rm UV}.
}
\]

With \(M_*=M_E\), the one-loop inhomogeneous beta-function contribution from this fixed sector is
\[
\boxed{
\left.\beta_{c_{\partial HS}}\right|_{C_5C_5^\ast}
\equiv
\left.\mu\frac{dc_{\partial HS}}{d\mu}\right|_{C_5C_5^\ast}
=-\frac{M_E^2}{16\pi^2}\sum_\ell|C_{5,\ell}|^2
=-\frac{1}{16\pi^2}
\sum_\ell|y_\ell|^2|\lambda_\ell|^2.
}
\]
The sign follows the stated inverse-kernel and counterterm convention. This is the inhomogeneous \(C_5C_5^\ast\) contribution only; multiplicative gauge/scalar anomalous dimensions and mixing with the rest of the Wilson vector have not been added.

For the same benchmark,
\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_\ell|y_\ell|^2|\lambda_\ell|^2,
\]
so a useful exact normalization check is
\[
\boxed{
\left.\beta_{c_{\partial HS}}\right|_{C_5C_5^\ast}
=\frac12\,\Delta\lambda_{HS}^{E}
\quad(M_*=M_E).
}
\]
This relation is specific to the declared operator normalization and the leading-seesaw benchmark; it is not a general identity between unrelated Wilson coefficients.

## 3. Direct hard/soft logarithm cancellation

The source-aligned two-point hard difference is, in the RC-001 convention,
\[
\Pi_{\rm hard}^{(2{\rm pt})\,\prime}(0)
=\frac{q_\ell}{16\pi^2}
\left[
\ln\frac{M_E^2}{\mu_R^2}-\frac23
\right]
+O(M_E^{-4}\ln M_E).
\]
The derivative of the EFT contact tadpole vanishes. The light bubble gives
\[
\Pi_{\rm soft}^{\prime}(0)
=\frac{q_\ell}{16\pi^2}
\ln\frac{\mu_R^2}{m_\ell^2}
\]
for the displayed leading logarithm. Thus
\[
\begin{aligned}
\Pi_{\rm hard}^{\prime}(0)+\Pi_{\rm soft}^{\prime}(0)
&=\frac{q_\ell}{16\pi^2}
\left[
\ln\frac{M_E^2}{\mu_R^2}
-\frac23
+\ln\frac{\mu_R^2}{m_\ell^2}
\right]\\
&=\frac{q_\ell}{16\pi^2}
\left[
\ln\frac{M_E^2}{m_\ell^2}-\frac23
\right],
\end{aligned}
\]
so
\[
\boxed{
\frac{d}{d\ln\mu_R}
\left(\Pi_{\rm hard}^{\prime}+\Pi_{\rm soft}^{\prime}\right)=0
}
\]
for this restricted leading \(O(M_E^{-2})\) sector. Equivalently, the scale derivative of the finite hard Wilson coefficient reproduces the beta function derived from the EFT pole:
\[
\mu_R\frac{d}{d\mu_R}
\left[
\frac{M_E^2}{v_hv_s}\Pi_{\rm hard}^{(2{\rm pt})\,\prime}(0)
\right]
=
-\frac{M_E^2}{16\pi^2}\sum_\ell|C_{5,\ell}|^2.
\]

This is the central A5b result: the hard logarithm and the soft logarithm are not independent corrections to be added with arbitrary scales. They are two parts of one matched quantity.

**Double-counting rule:** if the hard coefficient is evaluated at \(\mu_R=M_E\) and then evolved with the beta function, do not add the same explicit hard logarithm a second time. Conversely, if the hard coefficient is evaluated directly at a lower \(\mu_R\), retain the matching logarithm and the soft loop at that same scale. These are alternative organizations of the same result.

## 4. Benchmark evaluation

Using \(M_E=M_*=20\) TeV, \(v_h=246.22\) GeV, the existing \(v_s\) values, and the leading-seesaw relation \(q_\ell=2m_\ell^2/(v_hv_s)\):

| Quantity | Benchmark A | Benchmark B |
|---|---:|---:|
| \(q_\mu\) | \(1.27924\times10^{-6}\) | \(2.87875\times10^{-7}\) |
| \(q_\tau\) | \(3.61784\times10^{-4}\) | \(8.14146\times10^{-5}\) |
| \(\beta_{c_{\partial HS}}^{(\mu)}\) | \(-3.71309\times10^{-4}\) | \(-1.88036\times10^{-5}\) |
| \(\beta_{c_{\partial HS}}^{(\tau)}\) | \(-1.05011\times10^{-1}\) | \(-5.31788\times10^{-3}\) |
| \(\beta_{c_{\partial HS}}^{\rm total}\) | \(-1.05382\times10^{-1}\) | \(-5.33669\times10^{-3}\) |
| \(\Delta\lambda_{HS}^{E}\) | \(-0.21076398\) | \(-0.01067338\) |
| \(\beta_c-\Delta\lambda_{HS}^{E}/2\) | \(<2\times10^{-17}\) | \(<3\times10^{-18}\) |

The tau contribution dominates this particular RGE source. The equality in the final row is an independent normalization/sign check against the already archived portal threshold.

The scale interval is
\[
\ln\frac{M_E^2}{m_h^2}=10.146351625.
\]
Integrating the restricted beta function from \(20\) TeV down to \(m_h=125.25\) GeV gives
\[
\Delta c_{\partial HS}
=\beta_c\ln\frac{m_h}{M_E}
=
\begin{cases}
+0.5346214 &(A),\\
+0.0270740 &(B).
\end{cases}
\]
The corresponding leading-log contribution to the mixed inverse kernel at \(p^2=m_h^2\) is
\[
\Delta\Pi_{\rm LL}^{(6)}(m_h^2)
=\frac{v_hv_s}{M_E^2}\Delta c_{\partial HS}\,m_h^2
=
\begin{cases}
+0.3659556~{\rm GeV}^2 &(A),\\
+0.0823533~{\rm GeV}^2 &(B).
\end{cases}
\]
These are scale-evolution contributions to the derivative operator, not new independent threshold corrections.

### 4.1 Explicit factor-two scale check at fixed physical \(M_E\)

To make the cancellation visible numerically, hold the physical heavy mass fixed at \(M_E=20\) TeV and evaluate the hard and soft logarithms at a common scale \(\mu=10,20,40\) TeV. Define the derivative coefficients
\[
H'(\mu)=\sum_\ell\frac{q_\ell}{16\pi^2}
\left[\ln\frac{M_E^2}{\mu^2}-\frac23\right],
\qquad
S'(\mu)=\sum_\ell\frac{q_\ell}{16\pi^2}
\ln\frac{\mu^2}{m_\ell^2}.
\]
The sum is constant to numerical precision:

| Benchmark | \(\mu\) [TeV] | \(H'(\mu)\) | \(S'(\mu)\) | \(H'+S'\) |
|---|---:|---:|---:|---:|
| A | 10 | \(+1.65452\times10^{-6}\) | \(+3.97539\times10^{-5}\) | \(4.14084\times10^{-5}\) |
| A | 20 | \(-1.53275\times10^{-6}\) | \(+4.29412\times10^{-5}\) | \(4.14084\times10^{-5}\) |
| A | 40 | \(-4.72002\times10^{-6}\) | \(+4.61285\times10^{-5}\) | \(4.14084\times10^{-5}\) |
| B | 10 | \(+3.72326\times10^{-7}\) | \(+8.94608\times10^{-6}\) | \(9.31840\times10^{-6}\) |
| B | 20 | \(-3.44925\times10^{-7}\) | \(+9.66333\times10^{-6}\) | \(9.31840\times10^{-6}\) |
| B | 40 | \(-1.06218\times10^{-6}\) | \(+1.03806\times10^{-5}\) | \(9.31840\times10^{-6}\) |

Multiplying the invariant sum by \(m_h^2\) gives \(+0.6495974\ {\rm GeV}^2\) (A) and \(+0.1461830\ {\rm GeV}^2\) (B) for this derivative-only projection. These are not full self-energies or physical pole shifts. The check is a fixed-sector matching/subtraction-scale identity, **not** the final full-model factor-two \(\mu_M\) uncertainty test.

## 5. Portal running: what is and is not established

### 5.1 VLL contribution

The one-loop VLL determinant obeys
\[
\left[\operatorname{Tr}({\cal M}^\dagger{\cal M})^2\right]_{h^2s^2}=0
\]
for the mass matrix used in RC-001. Therefore the fixed VLL Yukawa sector has no additive one-loop UV pole proportional to \(|y_\ell|^2|\lambda_\ell|^2\) in the renormalizable portal. The finite threshold
\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_\ell|y_\ell|^2|\lambda_\ell|^2
\]
is nonzero; a finite threshold is not a beta-function pole.

The \(q_\ell m_\ell^2\) constant pole in the broken-phase EFT subset scales as \(M_E^{-4}\). It belongs to the dimension-eight \(X^2Y^2\) potential sector, not to the dimension-four \(\lambda_{HS}\) beta function. At strict dimension six it must be dropped consistently.

### 5.2 Scalar-only UV portal contribution

The A3a gauge-basis scalar/Goldstone bubbles give
\[
\delta\lambda_{HS}^{\rm scalar}
=\frac{\lambda_{HS}}{16\pi^2\bar\epsilon}
(6\lambda_H+4\lambda_S)
+O(\lambda_{HS}^2).
\]
For a dimensionless quartic in \(d=4-2\epsilon\), the corresponding one-loop scalar-only beta contribution is
\[
\boxed{
\left.\beta_{\lambda_{HS}}\right|_{\rm scalar,linear}
=\frac{\lambda_{HS}}{16\pi^2}
(12\lambda_H+8\lambda_S).
}
\]
The portal-squared term contributes \(4\lambda_{HS}^2/(16\pi^2)\) to the scalar-only beta function if the portal is counted as an ordinary tree-level coupling. In the current combined counting \(\lambda_{HS}^{\rm UV}=O(\hbar)\), that term is beyond the retained \(O(\hbar^2)\) order.

This is still only the scalar contribution. The complete UV portal beta function also requires gauge and Yukawa pieces and a consistent VEV/tadpole scheme. The EFT boundary \(\lambda_{HS}^{\rm EFT}(\mu_M)=0\) and the UV boundary \(\lambda_{HS}^{\rm UV}(\mu_M)=-\Delta\lambda_{HS}^{E}\) must not be interchanged.

For orientation only, setting \(m_s=m_h\) gives \(\lambda_S=m_h^2/(2v_s^2)\), and the scalar-only linear beta contributions are \(+1.8740\times10^{-2}\) (A) and \(+1.4768\times10^{-4}\) (B). These values are not generic benchmark predictions because \(\lambda_S\) changes with \(m_s\).

## 6. Reconciliation with the archived 0.1421% scale residual

The previous Plan-C-lite archive reports a change of \(0.1421\%\) in the real part of the selected hard-plus-soft \(\Pi_{hs}\) between \(\mu_R=M_E\) and \(\mu_R=m_h\):
- A: \(-0.413263168\to-0.413850308\ {\rm GeV}^2\);
- B: \(-0.092999245\to-0.093131373\ {\rm GeV}^2\).

The leading logarithm isolated here is much larger before hard/soft cancellation: \(0.36596\ {\rm GeV}^2\) (A) and \(0.08235\ {\rm GeV}^2\) (B). The restricted analytic identity shows that this leading log cancels exactly between the source-aligned hard derivative term and the displayed EFT soft bubble.

It does **not** yet explain the remaining \(0.1421\%\) residual in the archived exact-mass Plan-C-lite total. That residual must remain an open diagnostic until the exact-mass terms, the same-order EFT soft insertions, and the counterterm/field-renormalization conventions are compared term by term. It must not be labelled automatically as a higher-order uncertainty or as proof of complete scale independence.

## 7. A5b acceptance boundary and next tasks

**Passed in this restricted sector**
1. Convert the EFT derivative pole to the \(c_{\partial HS}\) counterterm.
2. Derive the inhomogeneous \(\beta_{c_{\partial HS}}\) contribution.
3. Verify that its coefficient equals the explicit scale derivative of the hard Wilson coefficient.
4. Verify exact cancellation of the displayed leading hard and soft logarithms.
5. Reproduce the result numerically for benchmarks A and B.
6. Import the A3a scalar-only linear portal beta contribution without calling it the full portal beta.

**Still open before claiming A5b closure**
1. Gauge and Yukawa contributions to the UV portal beta function, including the VLL and light-lepton sectors.
2. One-loop running/mixing of \(C_5\), \(Q_{LD}\), \(Q_{RD}\), and the relevant current operators in the declared basis.
3. The remaining same-order EFT soft insertions and their UV poles; the present \(C_5C_5^\ast\) bubble/contact subset is not the complete set.
4. Full EOM/source projection and field/VEV renormalization in the same scheme.
5. Matching of the UV scalar-only portal running to the EFT with the conditional zero-portal boundary.
6. A5b factor-two \(\mu_M\) stability test only after items 1–5 are closed.
7. Dimension-eight hard/soft closure separately; do not mix its \(O(M_E^{-4})\) pole into the strict dimension-six RGE.

**Conclusion:** the first inhomogeneous EFT running block is now explicit and numerically checked. The result supports the use of \(20\) TeV as the hard matching scale, but it does not yet justify a full-model matching-scale uncertainty or a physical scalar pole. The next calculation should close the missing anomalous dimensions and portal/tadpole counterterms, not simply widen the scale scan.
