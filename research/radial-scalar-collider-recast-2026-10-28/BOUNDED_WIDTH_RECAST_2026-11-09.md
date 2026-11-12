# Belle II bounded-width pointwise reinterpretation — 2026-11-09

**PR:** #68  
**Benchmark:** original one-VEV \(S+\mathrm{VLL}\) model, \(\theta_{\mu R}=\theta_{\tau R}=10^{-2}\), negligible Higgs-portal mixing as an explicit collider benchmark, and decoupled VLLs in the scalar-width calculation.  
**Status:** regenerated 73,728-point width scan, bounded branching-fraction propagation, and conditional narrow/prompt grid classification completed. This is not a detector-level recast or a new CLs fit.

## 1. Experimental inputs and provenance

### Four-muon search

Belle II, *Phys. Rev. D* **109**, 112015 (2024), arXiv:2403.02841, searches \(e^+e^-\to\mu^+\mu^-X\), \(X\to\mu^+\mu^-\), over \(m_X=0.212\text{--}9.000\) GeV using \(178\,\mathrm{fb}^{-1}\). The published scalar-specific observed and expected 90% CL coupling limits are used; vector-mediator limits and efficiencies are not substituted.

Source links:
- https://arxiv.org/abs/2403.02841
- https://journals.aps.org/prd/abstract/10.1103/PhysRevD.109.112015

The numerical supplementary table archived in the repository has 2,317 rows. The paper reports 2,315 fits. The discrepancy remains unresolved; the source file is preserved unchanged. All 2,317 tabulated mass values are unique.

### Tau-pair search

Belle II, *Phys. Rev. Lett.* **131**, 121802 (2023), arXiv:2306.12294, searches \(e^+e^-\to\mu^+\mu^-X\), \(X\to\tau^+\tau^-\), over \(m_X=3.6\text{--}10\) GeV using \(62.8\,\mathrm{fb}^{-1}\). The arXiv ancillary file limits.csv supplies the scalar-specific observed and expected coupling limits.

Source links:
- https://arxiv.org/abs/2306.12294
- https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.131.121802

The archived table has 2,384 raw rows and 2,381 unique masses. Three exact duplicate mass rows are retained in the raw source files and deduplicated only for interpolation.

## 2. UV-to-experiment mappings

The original-model direct scalar Yukawa is
\[
y_{s\ell\ell}^{\rm UV}=\frac{m_\ell}{v_s},\qquad
v_s=\frac{m_{A'}}{2g_X}.
\]

For the four-muon search, the published muonphilic scalar reference has \(\mathrm{BR}_{\mu\mu}^{\rm ref}=1\). The signal-strength ratio is
\[
R_{4\mu}^{\rm obs}
=
\left(\frac{y_{s\mu\mu}^{\rm UV}}{g_{S,90}^{\rm obs}}\right)^2
\mathrm{BR}_{\mu\mu}^{\rm UV}.
\]

For the tau-pair search, the published mass-proportional scalar reference includes \(e,\mu,\tau\):
\[
\mathrm{BR}_{\tau\tau}^{\rm ref}(m_s)
=
\frac{m_\tau^2\beta_\tau^3}
{m_e^2\beta_e^3+m_\mu^2\beta_\mu^3+m_\tau^2\beta_\tau^3},
\qquad
\beta_\ell=\sqrt{1-\frac{4m_\ell^2}{m_s^2}}.
\]
The original UV model has no direct electron Yukawa in this construction. Its mapping is
\[
\xi_{\rm UV}=\frac{v_h}{v_s},\qquad
R_{\tau\tau}^{\rm obs}
=
\left(\frac{\xi_{\rm UV}}{\xi_{90}^{\rm obs}}\right)^2
\frac{\mathrm{BR}_{\tau\tau}^{\rm UV}}
{\mathrm{BR}_{\tau\tau}^{\rm ref}}.
\]
The UV branching fractions are taken from the regenerated width scan, including the on-shell, three-body, and bounded double-virtual \(A'\) cascade contributions.

Observed and expected coupling limits are interpolated in log-log mass, with no extrapolation outside the numerical limit tables.

## 3. Width and promptness classification

The four-muon fit uses reduced mass
\[
M_R=\sqrt{M_{\mu\mu}^2-4m_\mu^2},
\qquad
\Gamma_{M_R}\simeq
\frac{m_s}{\sqrt{m_s^2-4m_\mu^2}}\Gamma_s.
\]
The tau-pair recoil-mass fit uses \(m_s\) directly.

The full width and branching-fraction intervals from the scan are propagated. The four-muon interval endpoints are now ordered as
\[
\left(\frac{\Gamma}{\sigma}\right)_{\min}
=
\frac{\Gamma_{\min}}{\sigma_{\max}},
\qquad
\left(\frac{\Gamma}{\sigma}\right)_{\max}
=
\frac{\Gamma_{\max}}{\sigma_{\min}}.
\]
A point enters the narrow-template subset only if the full interval obeys
\[
\left(\frac{\Gamma}{\sigma}\right)_{\max}<0.10.
\]
The value 0.10 is an internal conservative diagnostic, not a Belle II selection cut.

For promptness, the maximum-kinematic scalar mean-flight interval is compared with 5 mm, the transverse-DCA scale used as a geometry proxy. This is not a literal decay-radius cut and is not a detector efficiency. A point is labelled prompt-proxy only if the upper flight-length bound is below 5 mm.

For a point to be called conditionally excluded, the conservative lower endpoint of the UV signal-strength ratio must exceed one and the complete width and flight intervals must pass these proxies.

## 4. Results on the regenerated grid

The width scan contains \(48\times48\times32=73,728\) points. The narrow/prompt recast outputs and summary are archived in the derived recast directory.

### Four-muon channel

| Classification | Grid points |
|---|---:|
| Excluded under the published narrow/prompt benchmark, conditionally | **2,746** |
| Evaluated but not excluded by this channel | 39,534 |
| Finite-width-sensitive | 8,673 |
| Width interval straddles the 0.10 threshold | 933 |
| Lifetime-sensitive | 12,088 |
| Scalar-Yukawa perturbativity failure | 1,734 |
| Scalar-quartic perturbativity failure | 4,948 |

The 2,746 conditional exclusions occupy 35 discrete scalar-mass grid values spanning \(0.212\text{--}3.444\) GeV. They are not a continuous excluded mass interval. Across these points, the maximum upper width/resolution ratio is \(0.0997875\), and the maximum upper mean-flight proxy is \(2.0922\times10^{-4}\) m (0.209 mm), both below the internal narrow/prompt thresholds.

For the 39,534 points classified as evaluated but not excluded, the largest conservative observed signal-strength ratio is \(0.999912\).

### Tau-pair channel

| Classification | Grid points |
|---|---:|
| Excluded under the evaluated narrow/prompt benchmark, conditionally | **0** |
| Evaluated but not excluded by this channel | 11,337 |
| Finite-width-sensitive | 3,286 |
| Width interval straddles the 0.10 threshold | 891 |
| Lifetime-sensitive | 721 |
| Scalar-quartic perturbativity failure | 2,414 |
| Outside the numerical limit grid | 1,319 |

The 11,337 evaluated-but-not-excluded points occupy 12 discrete mass values spanning \(3.738\text{--}9.213\) GeV. Their largest conservative observed signal-strength ratio is \(0.1353\). The 1,319 outside-grid points all lie at \(m_s=10\) GeV, just beyond the last ancillary-table mass value \(9.99943\) GeV; no extrapolation is made.

The zero count applies only to the evaluated narrow/prompt subset. It does not establish that finite-width or lifetime-sensitive points are allowed.

## 5. Why the previous 1,852-point number is superseded

The 2026-11-05 pointwise result used an earlier width-scan artifact and did not propagate the newly available double-virtual four-body branching-fraction intervals. The updated scan also exposed a swapped four-muon width/resolution endpoint assignment. That assignment is corrected in the scan code and covered by an explicit regression test. The 1,852-point number is historical and must not be quoted as the current result.

The current run regenerates the width scan, runs 60 unit tests, applies the corrected interval definitions, propagates the branching-fraction bounds, and archives the resulting CSV/JSON and SHA-256 manifests.

## 6. Explicit limitations

1. The double-virtual four-body width uses a diagonal-pairing spectral calculation and a Cauchy--Schwarz upper bound on identical-flavour exchange. It is not an exact exclusive four-body calculation.
2. The 0.10 narrow-width threshold is an internal diagnostic, not a Belle II cut.
3. The 5 mm comparison is a geometry proxy, not a detector efficiency or a literal decay-radius cut.
4. No mass-dependent lifetime efficiency map is available in this calculation. Displaced and long-lived points remain unclassified.
5. No finite-width Crystal-Ball convolution or event-level likelihood/CLs fit is performed. Finite-width-sensitive points remain unclassified.
6. No independent MadGraph production recalculation is performed. The mapping assumes the same spin-zero muon-FSR coupling normalization as the published scalar benchmark.
7. The four-muon 2,317-versus-2,315 row/fit discrepancy remains unresolved; the tau ancillary table's three duplicate rows are deduplicated for interpolation only.
8. The negligible Higgs-portal mixing and decoupled-VLL choices are explicit collider benchmark assumptions. This workstream does not calculate or import Higgs--scalar mixing results from PR #69.
9. The classifications are pointwise grid comparisons with published scalar coupling limits, not new Belle II CLs results or a global UV-parameter-space exclusion.

## 7. Reproducibility

- Width scan run: GitHub Actions run 42564306112.
- Scan archive: the scan-pr52-thetaR-1e-2 derived directory.
- Pointwise recast: the recast-pr52-thetaR-1e-2 derived directory.
- 60 unit tests pass.
- The scan and recast outputs include CSV/JSON files and SHA-256 manifests.
