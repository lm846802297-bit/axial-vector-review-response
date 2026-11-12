# Original-UV radial-scalar width scan and Belle II width/promptness audit

**Date:** 2026-11-05  
**Branch:** \`research/radial-scalar-original-model-belleii-20261105\`  
**Scope lock:** the original paper's single-VEV \(S+\mathrm{VLL}\) model only. No extra scalar, extra VEV, right-handed neutrino, or neutrino-sector completion is introduced.  
**Status:** the two-/three-body width scan and a bounded double-virtual four-body calculation have been executed on the stated grid. Belle II width-resolution and promptness diagnostics are added. No detector-level recast, final allowed region, or referee-response change is claimed.

## 1. Model and benchmark

The scan uses the original one-VEV relations
\[
m_{A'}=2g_Xv_s,\qquad
m_s^2=2\lambda_Sv_s^2,\qquad
y_{s\ell\ell}=\frac{m_\ell}{v_s},\quad \ell=\mu,\tau,
\]
so that
\[
v_s=\frac{m_{A'}}{2g_X},\qquad
\lambda_S=\frac{2g_X^2m_s^2}{m_{A'}^2},\qquad
y_{s\ell\ell}=\frac{2g_Xm_\ell}{m_{A'}}.
\]

The benchmark uses \(\theta_{\mu R}=\theta_{\tau R}=10^{-2}\) in the \(A'\) charged-lepton couplings, negligible Higgs-portal mixing, and decoupled VLLs. The portal and VLL assumptions are benchmark choices, not symmetry-enforced statements. The \(\gamma\gamma\) width from muon and tau loops is included; finite-VLL loop contributions are not included. No direct electron Yukawa is introduced.

The perturbativity criterion is applied point by point:
\[
\lambda_S\leq4\pi.
\]

## 2. Primary scalar widths

For the CP-even radial mode with interaction \(-y_{s\ell\ell}s\bar\ell\ell\),
\[
\Gamma_{\ell\ell}=
\frac{|y_{s\ell\ell}|^2m_s}{8\pi}
\left(1-\frac{4m_\ell^2}{m_s^2}\right)^{3/2}.
\]

The original canonical radial-mode interaction is
\[
\mathcal L\supset\frac{m_{A'}^2}{v_s}sA'_\mu A'^\mu,
\qquad g_{sA'A'}=\frac{2m_{A'}^2}{v_s}.
\]
Including the identical-vector factor and all three massive-vector polarizations,
\[
\Gamma(s\to A'A')=
\frac{m_s^3}{32\pi v_s^2}
\sqrt{1-4r_A}\left(1-4r_A+12r_A^2\right),
\quad r_A=\frac{m_{A'}^2}{m_s^2},
\]
for \(m_s>2m_{A'}\). The existing unit tests check this normalization and the threshold.

The scan also includes the leading muon/tau-loop contribution to \(s\to\gamma\gamma\).

## 3. Three kinematic regions

The calculation explicitly separates:

1. \(m_{A'}<m_s/2\): on-shell \(s\to A'A'\);
2. \(m_s/2\leq m_{A'}<m_s\): one on-shell and one virtual \(A'\), with \(s\to A'A'^*\to A'f\bar f\);
3. \(m_{A'}\geq m_s\): both \(A'\) propagators virtual, with four-fermion final states.

The one-on-shell/one-virtual three-body modes reuse \`off_shell_cascades.py\), including \(\nu_\mu,\nu_\tau,\mu,\tau\) final states and the axial-current longitudinal contribution. The code does not double count this contribution when the two-body \(A'A'\) channel is open.

## 4. Double-virtual four-body calculation and its limitation

For \(m_{A'}\geq m_s\), the new \`off_shell_four_body.py\` module evaluates the factorized double-spectral contribution. For each virtual momentum \(q_i\), the integrated fermion-current tensor is decomposed into transverse and longitudinal components,
\[
H_i^{\mu\nu}=H_{T,i}P_{T,i}^{\mu\nu}+H_{L,i}P_{L,i}^{\mu\nu}.
\]
The unitary-gauge propagator multiplies the longitudinal component by
\[
\left(1-\frac{q_i^2}{m_{A'}^2}\right)^2.
\]
The two tensors are contracted with the scalar \(sA'_\mu A'^\mu\) vertex and integrated over
\[
\sqrt{q_1^2}+\sqrt{q_2^2}\leq m_s.
\]

The double-spectral diagonal-pairing contribution is
\[
\Gamma_{4f}^{\rm diag}=
\frac{g_{sA'A'}^2}{128\pi^3m_s^3}
\int_{\mathcal D}dq_1^2\,dq_2^2\,
\frac{\sqrt{\lambda(m_s^2,q_1^2,q_2^2)}\,
\mathcal C(q_1^2,q_2^2)}
{(q_1^2-m_{A'}^2)^2(q_2^2-m_{A'}^2)^2},
\]
where \(\mathcal C\) contains the \(TT\), \(TL\), \(LT\), and \(LL\) contractions. The factor \(1/2\) for the two identical virtual \(A'\) lines is included. The transverse and longitudinal spectral functions are built from the same original-model \(\nu_\mu,\nu_\tau,\mu,\tau\) currents used in the three-body calculation.

**Identical-flavor exchange is not explicitly integrated.** For identical fermion-pair species, the amplitude contains direct and exchanged pairings. A Cauchy-Schwarz bound is therefore reported:
\[
\Gamma_{4f}^{\rm exact}
\leq
\Gamma_{4f}^{\rm distinct}
+2\Gamma_{4f}^{\rm same,diag}.
\]
The code returns the diagonal contribution and this upper bound separately. It does not label the exclusive four-body result exact. This is sufficient to bound the effect on the direct \(\mu\mu\) and \(\tau\tau\) branching fractions in the scan, but it is not a precision exclusive four-body prediction.

For \(m_{A'}\geq m_s\), the absorptive width term in the off-shell propagator is omitted in the four-body integration. Across the 856 unique mass pairs in the scan, its maximum relative correction at \(g_X=0.1\) is \(1.84\times10^{-7}\). With this term omitted, the double-virtual result scales exactly as \(g_X^6\), allowing one calculation per \((m_s,m_{A'})\) pair and rescaling over the \(g_X\) grid.

## 5. Executed grid and numerical convergence

The grid contains
\[
m_s\in[0.212,10]\ {\rm GeV},\quad
m_{A'}\in[10^{-3},10^2]\ {\rm GeV},\quad
g_X\in[10^{-6},10^{-1}],
\]
with \(48\times48\times32=73\,728\) points.

| Quantity | Result |
|---|---:|
| On-shell \(A'A'\) region | 42,240 points |
| One-on-shell/one-virtual three-body region | 4,096 points |
| Double-virtual four-body bounded region | 27,392 points |
| Points satisfying \(\lambda_S\leq4\pi\) | 68,351 |
| Points outside the stated perturbativity criterion | 5,377 |

### Three-body quadrature

All 4,096 three-body grid points were compared at 192, 384, and 768 Gauss-Legendre nodes.

- Maximum relative difference, 192 vs 768: \(1.12\times10^{-4}\).
- 99th percentile: \(1.09\times10^{-4}\).
- Maximum relative difference, 384 vs 768: \(4.95\times10^{-5}\).

The 192-node scan setting is therefore converged at approximately the \(10^{-4}\) relative level on this grid.

### Four-body quadrature

The 856 unique double-virtual mass pairs were compared at 96 and 128 nodes.

- Maximum relative difference: \(1.39\times10^{-3}\).
- 99th percentile: \(1.39\times10^{-3}\).
- Maximum running-width correction at 64 nodes: \(1.84\times10^{-7}\).

The production scan uses 128 nodes for the double-spectral integral.

### Size of the double-virtual four-body contribution

At the largest scanned coupling \(g_X=0.1\), the maximum identical-exchange upper bound relative to the direct \(\mu\mu+\tau\tau+\gamma\gamma\) widths is
\[
\max\frac{\Gamma_{4f}^{\rm upper}}
{\Gamma_{\mu\mu}+\Gamma_{\tau\tau}+\Gamma_{\gamma\gamma}}
=1.85\times10^{-6},
\]
at \((m_s,m_{A'},g_X)=(0.212,0.21899,0.1)\) GeV. The ratio decreases approximately as \(g_X^4\) at smaller \(g_X\). Thus the exact identical-pair interference is not needed to determine the direct \(\mu\mu\) and \(\tau\tau\) branching fractions at phenomenologically relevant precision within this declared benchmark; its effect is bounded at the few-parts-per-million level. The four-body partial width itself remains a bounded, not exact, result.

## 6. Belle II mass resolution: compare to the actual fitted variable

### Four-muon search

Belle II searches over \(m_X=0.212\)--\(9.0\) GeV and fits the reduced dimuon mass
\[
M_R=\sqrt{M_{\mu\mu}^2-4m_\mu^2},
\]
not \(M_{\mu\mu}\) directly. The published reduced-mass resolution is 2--2.5 MeV below 1 GeV, rises to about 5 MeV near 5 GeV, and falls to 2.5 MeV at 9 GeV. The search excludes \(M_{\mu\mu}=3.07\)--\(3.12\) GeV around the \(J/\psi\).

For a narrow intrinsic scalar width, the corresponding reduced-mass width is approximately
\[
\Gamma_{M_R}\simeq\frac{m_s}{M_R}\Gamma_s.
\]
The scan compares this with a conservative envelope of the published \(M_R\) resolution. For broad points, this linearized conversion is only a diagnostic; a full line-shape convolution is required.

Among 65,708 perturbative grid points in the published mass range and outside the \(J/\psi\) veto:

- 55,301 (84.2%) have the conservative upper bound on \(\Gamma_{M_R}/\sigma_{M_R}\) below 0.1;
- 7,429 (11.3%) have the conservative lower bound above 1;
- 2,978 lie between these categories.

The scalar-specific signal efficiency must be used. Belle II generates scalar signal samples separately: the scalar is produced through a p-wave process and has a harder momentum spectrum than the vector benchmark. The collaboration explicitly warns against substituting vector efficiencies.

### Tau-pair search

Belle II searches \(m_X=3.6\)--\(10\) GeV and fits the recoil mass \(M_{\rm recoil}(\mu\mu)\). The paper states a resolution of 30 MeV near the \(2m_\tau\) threshold, decreasing smoothly to 10 MeV at 6 GeV and 1 MeV at 10 GeV. The supplementary example at 6.6 GeV uses a \(\pm50\) MeV window equal to five times the resolution, independently giving 10 MeV there. The scan step is half the mass resolution.

The resolution envelope used in the scan is therefore 10--30 MeV over 3.6--6 GeV, 10 MeV at the 6 and 6.6 GeV anchors, and 1--10 MeV over 6.6--10 GeV. It is an anchor-based conservative interval, not a reconstructed point-by-point resolution curve. Since the fitted variable is the recoil mass, compare \(\Gamma_s\) directly to this resolution.

Among 17,554 perturbative grid points in the tau-search mass range:

- 12,912 (73.6%) have the conservative upper bound on \(\Gamma_s/\sigma_{\rm recoil}\) below 0.1;
- 2,313 (13.2%) have the conservative lower bound above 1;
- 902 (5.1%) straddle 1 within the resolution interval;
- the remaining 1,427 lie between 0.1 and 1.

Belle II simulates the leptophilic scalar as a separate spin-0 signal model and reports 10--20% relative efficiency differences from the \(L_\mu-L_\tau\) vector benchmark. The scalar-specific efficiency, not the \(Z'\) efficiency, is the appropriate input.

## 7. Promptness and flight-distance diagnostics

Both analyses impose track distance-of-closest-approach requirements of 0.5 cm transversely and 2.0 cm longitudinally. The four-muon paper states that the lifetime is negligible compared with experimental resolution for the couplings explored in its muonphilic-scalar benchmark. This does not establish promptness throughout the original UV scan.

For the UV points, the code computes a conservative maximum lab-frame \(\beta\gamma\) for \(e^+e^-\to\mu^+\mu^-s\): the dimuon recoil is placed at threshold, the scalar is emitted along the lab boost, and the SuperKEKB center-of-mass boost \(\beta\gamma\simeq0.28\) is applied. It then reports \(\beta\gamma_{\max}c\tau_s\), and similarly the maximum daughter-\(A'\) flight scale when an on-shell \(A'\) is available.

Among 68,351 perturbative points:

- 56,212 (82.2%) have the conservative scalar mean-flight proxy below 5 mm;
- 58,119 (85.0%) are below 20 mm;
- 12,139 have a proxy at or above 5 mm.

For 40,959 perturbative points with an on-shell \(A'\), 23,496 have the corresponding \(A'\) proxy below 5 mm and 17,463 are at or above 5 mm.

These are geometry-scale diagnostics, not track-DCA efficiencies: the parent flight direction, daughter-track geometry, detector material, reconstruction, and MLP response all matter. Belle II does not publish lifetime-dependent efficiency curves for these searches. Points with flight scales comparable to the DCA cuts require a lifetime-dependent detector simulation or dedicated reinterpretation; they are not automatically excluded.

Two examples show why width and lifetime must be checked separately:

| \(m_s\) | \(m_{A'}\) | \(g_X\) | \(\Gamma_s\) | Resolution comparison |
|---:|---:|---:|---:|---|
| 4.0 GeV | 0.5 GeV | 0.1 | 100.8 MeV | Much broader than the 2.5--5 MeV four-muon resolution |
| 4.0 GeV | 5.0 GeV | 0.1 | 0.0806 MeV | Narrow compared with the four-muon resolution |
| 6.6 GeV | 8.0 GeV | 0.1 | 0.312 MeV | \(\Gamma_s/\sigma_{\rm recoil}\simeq0.031\) at 10 MeV |
| 6.6 GeV | 8.0 GeV | \(10^{-6}\) | \(3.12\times10^{-11}\) MeV | Extremely narrow, but maximum lab mean-flight proxy is about 5.2 mm |

The last two points have the same mass ratio but very different proper lifetimes because the widths scale approximately as \(g_X^2\).

## 8. Current conclusion and next gate

The original-model two-body widths and three-body cascade are evaluated over the full grid. The double-virtual four-body contribution is calculated in a factorized approximation and its identical-pair exchange is bounded; its maximum effect on direct scalar branching fractions is below \(1.9\times10^{-6}\) in the stated scan.

The actual Belle II mass-resolution scales and prompt-selection geometry are now incorporated. This is enough to identify points where the published narrow, prompt signal templates cannot be used without a finite-width or lifetime-dependent treatment. It is not yet a detector-level reinterpretation.

The remaining collider-recast work is:

1. use the published spin-0 production normalizations and mass-dependent scalar efficiencies for the four-muon and tau-pair analyses;
2. translate the original-UV direct branching fractions \(BR(s\to\mu\mu)\) and \(BR(s\to\tau\tau)\) point by point;
3. convolve broad scalar points with the fitted signal resolution, and treat long-lived points with lifetime-dependent efficiencies;
4. classify excluded, evaluated-allowed, unclassified, and theoretically inconsistent points separately.

No formal Major Point 1 response or manuscript text is changed by this independent research calculation.
