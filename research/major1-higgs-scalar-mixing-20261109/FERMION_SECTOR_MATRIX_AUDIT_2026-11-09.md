# Exact-basis one-loop fermion self-energy matrix audit — 2026-11-09

**Scope:** original \(\mu,\tau\) and vector-like-lepton sector only.  
**Benchmarks:** Plan-C A (open \(A'A'\)) and B (closed \(A'A'\) at \(m_s=m_h\)).  
**Convention:** \(\Gamma_{\mathrm{inv}}=p^2 I-\mathcal M_{\mathrm{loc}}^2+\Pi_{\mathrm{RC}}\), with \(\Pi_B=-\Pi_{\mathrm{RC}}\).  
**Status:** exact mass-eigenstate \(hh,hs,ss\) fermion-loop entries and their finite hard momentum differences are evaluated; complete pole calculation remains open.

## 1. Why this calculation is needed

The earlier exact mass-eigenstate calculation evaluates only the off-diagonal \(\Pi_{hs}\). A physical \(2\times2\) propagator also requires the diagonal \(\Pi_{hh}\) and \(\Pi_{ss}\), together with their mass and field-renormalization counterterms.

This audit generalizes the same exact mass-eigenstate formula to all three independent entries. It includes all four internal pairs (heavy-heavy, heavy-light, light-heavy, light-light) for each of the \(\mu\) and \(\tau\) sectors.

## 2. Formula and subtraction

For \(a,b\in\{h,s\}\),
\[
C_{ab}^{ij}=(G_a)_{ij}(G_b)_{ij}^{*}+(G_a)_{ji}^{*}(G_b)_{ji},
\quad
D_{ab}^{ij}=(G_a)_{ij}(G_b)_{ji}+(G_a)_{ji}^{*}(G_b)_{ij}^{*},
\]
\[
K_{ij}=A_0(m_i^2)+A_0(m_j^2)+(m_i^2+m_j^2-p^2)B_0(p^2;m_i^2,m_j^2),
\]
\[
\Pi_{ab}^{F,\ell}(p^2)
=-\frac{1}{16\pi^2}\sum_{i,j=1}^{2}
\left[C_{ab}^{ij}K_{ij}+2m_im_jD_{ab}^{ij}B_0(p^2;m_i^2,m_j^2)\right].
\]

The finite hard momentum difference is defined entry by entry:
\[
\Delta\Pi_{ab,\mathrm{hard}}^{B}
=
-\left[\Pi_{ab,\mathrm{full}}^{RC}(m_h^2)-\Pi_{ab,\mathrm{full}}^{RC}(0)\right]
-\left[\Pi_{ab,\mathrm{light}}^{B}(m_h^2)-\Pi_{ab,\mathrm{light}}^{B}(0)\right].
\]
The light-light term uses the exact light-state Yukawa vertices from the same SVD. The hard difference is real because the external momentum is below every heavy-light and heavy-heavy cut; the light absorptive cut cancels in the subtraction.

## 3. Finite hard momentum differences

All entries are in \(\mathrm{GeV}^2\), in the Plan-B \(\Pi_B=-\Pi_{RC}\) convention.

| Entry | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Delta\Pi_{hh,\mathrm{hard}}^B\) | \(-131.023924966\) | \(-131.023924966\) |
| \(\Delta\Pi_{hs,\mathrm{hard}}^B\) | \(+0.024030444\) | \(+0.005407724\) |
| \(\Delta\Pi_{ss,\mathrm{hard}}^B\) | \(-626.010389903\) | \(-31.702023714\) |

The off-diagonal values reproduce the previously archived exact mass-eigenstate calculation. The \(hh\) hard difference is benchmark independent because the Higgs-side VLL Yukawa and mixing inputs are the same. The \(ss\) entry changes with \(v_s\) through the singlet-side VLL Yukawa.

These are finite fermion-sector matching subcalculations. They are not physical pole shifts and are not a complete matched matrix.

## 4. UV derivative structures

The sums \(\sum_{ij}C_{ab}^{ij}\), which multiply the \(p^2\) UV pole in the unrenormalized loop expression, are:

| Entry | Benchmark A | Benchmark B |
|---|---:|---:|
| \(hh\) | \(2.639206236\) | \(2.639206236\) |
| \(hs\) | \(\simeq0\) | \(\simeq0\) |
| \(ss\) | \(12.610804206\) | \(0.638628400\) |

The off-diagonal derivative divergence cancels in the complete mass-eigenstate sum, while the two diagonal entries have nonzero wave-function divergences. A complete propagator therefore needs the corresponding diagonal field-renormalization counterterms. The diagonal local mass divergences also require their own renormalization conditions; the raw full self-energy values are not physical mass corrections.

## 5. Absorptive matrix and unitarity check

At \(p^2=m_h^2\), the \(\mu,\tau\) fermion cuts give the following \(\operatorname{Im}\Pi_{\mathrm{RC}}\) matrices in \(\mathrm{GeV}^2\):
\[
A:\quad
\begin{pmatrix}
0.0325702561&0.1131333101\\
0.1131333101&0.3929703779
\end{pmatrix},
\qquad
B:\quad
\begin{pmatrix}
0.0325702561&0.02545910995\\
0.02545910995&0.01990055827
\end{pmatrix}.
\]
Both matrices are positive semidefinite to numerical precision. Their smaller eigenvalues are \(6.54\times10^{-13}\) and \(2.69\times10^{-13}\,\mathrm{GeV}^2\); the larger eigenvalues are \(0.425540634\) and \(0.0524708144\,\mathrm{GeV}^2\). The off-diagonal entries saturate
\[
|\operatorname{Im}\Pi_{hs}|^2
=\operatorname{Im}\Pi_{hh}\operatorname{Im}\Pi_{ss}
\]
to the displayed numerical precision.

The rank-one structure follows because, in the adopted mass-proportional benchmark, the light-state \(h\) and \(s\) couplings to each charged-lepton channel are proportional. This provides an optical-theorem/absorptive-matrix cross-check that was absent from the off-diagonal-only calculation.

## 6. Important no-double-counting rule

If these explicit \(\mu,\tau\) absorptive entries are included in a future matrix propagator, their partial widths must not also be added a second time through fixed diagonal widths. In particular:
- the \(\mu,\tau\) contributions already contained in the \(4.07\) MeV SM Higgs width must be removed from any residual width input if the explicit fermion loops are retained;
- the direct \(s\to\mu^+\mu^-,\tau^+\tau^-\) widths must not be duplicated in an externally inserted \(\Gamma_s\).

Other Higgs decay channels, the \(s\to A'A'\) channel where open, and the remaining scalar/gauge sectors still require consistent treatment.

## 7. Validation and limitations

The accompanying script diagonalizes the original charged-lepton/VLL mass matrices by SVD, includes all four internal mass-state pairs, reproduces the previously archived \(\Pi_{hs}\) absorptive and hard-momentum values, checks the positive-semidefinite absorptive matrix, checks the vanishing off-diagonal \(p^2\) UV coefficient and nonzero diagonal coefficients, and verifies that all hard momentum differences are real below the heavy thresholds.

This is not a complete gauge-independent self-energy matrix. It omits top, \(W\), \(Z\), \(A'\), Goldstone, ghost and scalar loops, the complete same-order EFT soft/counterterm set, and the full tadpole/VEV prescription. No complex poles, residues, line shapes, signal strengths, or exclusions are claimed.


## 8. EFT light-loop UV subtraction and matching counterterms

The exact light-light bubble coefficients are now recorded separately from the full mass-eigenstate coefficients. The full-theory off-diagonal derivative pole cancels, but the EFT light-light bubble has a nonzero \(hs\) derivative pole. Consequently, the full-minus-light matching requires a derivative counterterm.

With
\[
\Gamma_{\mathrm{inv}}=p^2 I-\mathcal M_{\mathrm{loc}}^2+\Pi_{\mathrm{RC}},
\qquad
\Delta_{\mathrm{UV}}=\frac1\epsilon-\gamma_E+\ln4\pi,
\]
the field-counterterm coefficient is
\[
\frac{\delta Z_{ab}^{\mathrm{match}}}{\Delta_{\mathrm{UV}}}
=-\frac{C_{ab}^{\mathrm{full}}-C_{ab}^{\mathrm{light}}}{16\pi^2}.
\]

| Entry | Benchmark A | Benchmark B |
|---|---:|---:|
| \(hh\) | \(-0.0167123071\) | \(-0.0167123071\) |
| \(hs\) | \(+2.2983060\times10^{-6}\) | \(+5.1720246\times10^{-7}\) |
| \(ss\) | \(-0.0798508674\) | \(-0.00404375731\) |

The \(hs\) coefficient is the counterterm for the EFT light-bubble subtraction, not a physical mixing angle or a contradiction of the full-theory cancellation. The JSON output also records the local mass-pole coefficients; these require mapping to the scalar-potential parameter counterterms together with the tadpole/VEV prescription.

The fifth automated test validates these field-counterterm coefficients for both benchmarks. GitHub Actions run 42564492356 passes all five tests. This remains a fermion-sector matching subcalculation, not a complete UV--EFT matching result.


## 9. Full-theory tadpole/potential counterterms and leading EFT5 contact completion

The independent VLL effective-potential audit and scalar-potential counterterm map are archived in:

- TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md
- independent_fermion_tadpole_uv_audit.py
- scalar_potential_counterterm_map.py
- test_scalar_potential_counterterm_map.py
- scalar_potential_counterterm_map.json

The full-theory invariant is
\[
F=\sum_{\ell=\mu,\tau}\operatorname{Tr}[(\mathcal M_\ell^\dagger\mathcal M_\ell)^2]
=\sum_\ell\left[
M_E^4+M_E^2|y_\ell|^2\phi_h^2+\frac{|y_\ell|^4}{4}\phi_h^4
+M_E^2|\lambda_\ell|^2\phi_s^2+\frac{|\lambda_\ell|^4}{4}\phi_s^4
\right].
\]
It has no mixed \(\phi_h^2\phi_s^2\) term. Therefore the VLL determinant gives \(\delta\lambda_{HS}=0\) as a divergent full-theory potential counterterm at this order. This does not set the finite portal threshold to zero.

The leading EFT5 mass function \(m_\ell=C_{5,\ell}\phi_h\phi_s/2\) generates
\[
V_{1,\mathrm{EFT5}}^{\mathrm{div}}
=\frac{\Delta_{\mathrm{UV}}}{16\pi^2}
\sum_\ell |C_{5,\ell}|^4(H^\dagger H)^2(S^\dagger S)^2.
\]
The mixed \(hs\) two-point UV pole contains both the light bubble and the second-derivative contact term. Consequently, the earlier light-bubble-only local subtraction is not the complete EFT local UV subtraction. The dimension-eight operator counterterm and contact contribution are now explicit.

The fixed numerical pole coefficients and the perturbative-control caveat for Benchmark A are given in the separate audit report. Finite tadpole/VEV conditions and the complete gauge/Goldstone/ghost/scalar matching remain open.
