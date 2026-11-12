# Belle II narrow-width / prompt benchmark reinterpretation of the original UV radial scalar

**Date:** 2026-11-05  
**Branch:** research/radial-scalar-original-model-belleii-20261105  
**Status:** first conditional, pointwise narrow-width/prompt reinterpretation completed from the archived Belle II scalar limits and the available 73,728-point width-scan artifact. This is not a detector-level recast, a new CLs result, or a complete exclusion map.

## 1. Scope and frozen model

This calculation uses only the original paper's one-VEV \(S+\mathrm{VLL}\) construction:
\[
m_{A'}=2g_Xv_s,\qquad
m_s^2=2\lambda_Sv_s^2,\qquad
y_{s\ell\ell}=\frac{m_\ell}{v_s}.
\]
No additional scalar, VEV, \(\sigma\), or right-handed neutrino is introduced. The pointwise theoretical condition is \(\lambda_S\leq4\pi\).

The reinterpretation assumes the zero/negligible portal and decoupled-VLL benchmark used by the current width scan. It compares each channel independently and does not alter the paper, formal referee response, or Major Point 1.

## 2. Experimental benchmark normalizations

### 2.1 Four-muon search

Belle II, *Phys. Rev. D* **109**, 112015 (2024), arXiv:2403.02841, uses \(178\,\mathrm{fb}^{-1}\), searches \(m_S=0.212\text{--}9.0\,\mathrm{GeV}\), and publishes observed and expected 90% CL limits on the muonphilic scalar coupling \(g_S\). The benchmark interaction is
\[
\mathcal L\supset g_S S\bar\mu\mu,
\]
with the scalar benchmark coupling only to muons; its reference direct dimuon branching fraction is therefore taken as \(\mathrm{BR}_{\mu\mu}^{\rm ref}=1\) to the accuracy of the published benchmark. The collaboration generated scalar signal samples separately from the vector sample; the scalar is p-wave produced and has a different efficiency. The scalar-specific \(g_S\) limit is used here, not a vector efficiency or vector limit.

The UV mapping is
\[
g_S^{\rm UV}=y_{s\mu\mu}=\frac{m_\mu}{v_s}.
\]
At fixed mass and matched spin-0 muon-FSR production normalization, the signal-strength ratio against the observed published limit is
\[
R_{4\mu}^{\rm obs}
=
\frac{(g_S^{\rm UV})^2\,\mathrm{BR}_{\mu\mu}^{\rm UV}}
     {(g_{S,90}^{\rm Belle})^2\,\mathrm{BR}_{\mu\mu}^{\rm ref}}
=
\left(\frac{m_\mu/v_s}{g_{S,90}^{\rm Belle}}\right)^2
\mathrm{BR}_{\mu\mu}^{\rm UV}.
\]
A value above one is above the published 90% CL coupling limit **under the narrow, prompt, unchanged-scalar-acceptance assumptions**. It is not a new CLs fit.

The paper fits the reduced dimuon mass
\[
M_R=\sqrt{M_{\mu\mu}^2-4m_\mu^2}
\]
and reports a reduced-mass resolution of 2--2.5 MeV below 1 GeV, rising smoothly to about 5 MeV near 5 GeV and falling to 2.5 MeV at 9 GeV. Its signal shape is a sum of two Crystal Ball functions with a common mean. The published mass scan excludes the \(J/\psi\) dimuon-mass interval 3.07--3.12 GeV. These experimental conditions are applied as a conservative resolution envelope and an explicit \(J/\psi\) veto in the pointwise table.

### 2.2 Tau-pair search

Belle II, *Phys. Rev. Lett.* **131**, 121802 (2023), arXiv:2306.12294, uses \(62.8\,\mathrm{fb}^{-1}\), searches \(m_S=3.6\text{--}10\,\mathrm{GeV}\), and publishes scalar-specific observed and expected 90% CL limits on \(\xi\). Its mass-proportional leptophilic scalar benchmark is
\[
\mathcal L\supset
-\xi\sum_{\ell=e,\mu,\tau}\frac{m_\ell}{v}S\bar\ell\ell,
\qquad v=246\,\mathrm{GeV}.
\]
The original UV model matches the muon and tau Yukawa normalization with
\[
\xi_{\rm UV}=\frac{v}{v_s}=\frac{2vg_X}{m_{A'}}.
\]
The benchmark reference branching fraction is calculated with its \(e,\mu,\tau\) channels:
\[
\mathrm{BR}_{\tau\tau}^{\rm ref}(m_s)
=
\frac{m_\tau^2\beta_\tau^3}
{m_e^2\beta_e^3+m_\mu^2\beta_\mu^3+m_\tau^2\beta_\tau^3},
\qquad
\beta_\ell=\sqrt{1-\frac{4m_\ell^2}{m_s^2}}.
\]
The UV branching fraction is taken from the original-model width scan, which has no direct electron Yukawa. The resulting electron-only normalization difference between the benchmark and UV \(\mathrm{BR}_{\tau\tau}\) is at most \(1.09\times10^{-5}\) over 3.6--10 GeV when no additional UV decay mode is open. The potentially important differences are the UV \(s\to A'A'\) and off-shell \(A'\) cascades, which enter the UV total width and branching fraction.

The pointwise signal-strength ratio is
\[
R_{\tau\tau}^{\rm obs}
=
\frac{\xi_{\rm UV}^2\,\mathrm{BR}_{\tau\tau}^{\rm UV}}
{\xi_{90,\rm obs}^{2}\,\mathrm{BR}_{\tau\tau}^{\rm ref}}.
\]
Again, \(R_{\tau\tau}^{\rm obs}>1\) is a conditional comparison with the published scalar coupling limit, not a rerun of the experiment's likelihood.

The experiment fits the recoil mass against the two tagging muons. The paper reports a resolution of 30 MeV near \(2m_\tau\), decreasing smoothly to 10 MeV at 6 GeV and 1 MeV at 10 GeV. Signal recoil-mass distributions are parameterized from simulation by two Crystal Ball functions sharing a common mean. The collaboration applied the full selection to the scalar signal and reports 10--20% relative efficiency differences from the \(L_\mu-L_\tau\) vector benchmark. The scalar-specific \(\xi\) limits are used here; the vector efficiencies are not substituted.

## 3. Width and promptness screens

The four-muon fitted variable is \(M_R\), so for a narrow scalar the natural width is converted using
\[
\Gamma_{M_R}\simeq
\frac{m_s}{\sqrt{m_s^2-4m_\mu^2}}\Gamma_s.
\]
The tau-pair recoil-mass fit uses \(m_s\) directly, so \(\Gamma_{\rm recoil}\simeq\Gamma_s\).

For both channels the script uses the conservative lower end of the published resolution envelope to form the largest possible \(\Gamma/\sigma\). A point is retained in the narrow-template subset only if
\[
\max_{\sigma\ {\rm in\ published\ envelope}}\frac{\Gamma}{\sigma}<0.10.
\]
The 0.10 value is an internal numerical tolerance for this reinterpretation, **not** a Belle II cut or a published narrow-width criterion. Points failing it are classified as finite-width-sensitive and deferred to the line-shape convolution stage.

For promptness, the script computes a kinematic maximum for the scalar lab \(\beta\gamma\) in \(e^+e^-\to\mu^+\mu^-s\), placing the dimuon recoil at threshold and applying the SuperKEKB \(\beta\gamma\simeq0.28\) boost. It reports the corresponding maximum mean lab flight length and compares it with the 5 mm transverse DCA scale. This is a geometry proxy only: mean flight length is not track DCA, the exponential decay tail remains, and no detector-level lifetime-dependent efficiency is inferred. Points with this proxy at or above 5 mm are marked lifetime-sensitive.

## 4. Pointwise result from the available scan artifact

The archived input scan contains 73,728 points. It has 33 columns and was generated before the later double-virtual four-body update was reflected in the scan output file. In particular, 27,392 rows in the double-virtual \(m_{A'}\geq m_s\) region are marked branching_fractions_complete=False; the CSV has no four-body contribution columns. The current scan code has since been extended with a bounded double-spectral four-body calculation, but the old CSV must not be treated as if it had been regenerated. **All such rows are kept unclassified here.**

The tau limit table has 2,384 rows, 2,381 unique mass points, and three exact duplicate mass rows. Duplicate masses are removed only in the interpolation copy; the archived raw file is not modified. The four-muon table has 2,317 unique mass rows. The pointwise coupling limits are interpolated linearly in \(\log g\) versus \(\log m_s\), with no extrapolation beyond the numerical mass grid.

### 4.1 Four-muon result

| Classification | Grid points |
|---|---:|
| Excluded under published narrow/prompt benchmark (conditional) | 1,852 |
| Evaluated; not excluded by this channel (conditional) | 24,828 |
| Finite-width-sensitive | 11,330 |
| Lifetime-sensitive | 946 |
| Theoretically inconsistent, \(\lambda_S>4\pi\) | 4,948 |
| Unclassified: incomplete width sum | 26,752 |
| **Total within experimental mass window** | **70,656** |

The conditional excluded points occur at the sampled masses from 0.212 to 3.444 GeV. This is a pointwise grid result, not a continuous excluded mass interval. The largest \(\Gamma_{M_R}/\sigma_{\min}\) among these points is 0.09979, and the largest maximum-kinematic mean flight proxy is 0.209 mm, below the 5 mm screening scale. The observed signal-strength ratio reaches \(5.01\times10^3\) at the most signal-rich sampled point.

The result is physically consistent with the original model structure: above the \(\tau\)-pair threshold, the UV \(\mathrm{BR}_{\mu\mu}\) decreases, weakening the four-muon constraint. The table accounts for the \(A'A'\) and three-body cascade contributions where the width artifact marks the branching fractions complete.

### 4.2 Tau-pair result

| Classification | Grid points |
|---|---:|
| Excluded under published narrow/prompt benchmark (conditional) | 0 |
| Evaluated; not excluded by this channel (conditional) | 7,396 |
| Finite-width-sensitive | 4,152 |
| Lifetime-sensitive | 15 |
| Theoretically inconsistent, \(\lambda_S>4\pi\) | 2,414 |
| Unclassified: incomplete width sum | 4,992 |
| Unclassified: outside numerical limit grid | 999 |
| **Total within experimental mass window** | **19,968** |

No perturbative, width-complete, narrow-template, prompt-proxy point in the sampled grid exceeds the published scalar \(\xi\) limit after the UV/reference \(\tau\tau\) branching-fraction correction. This statement is limited to the evaluated benchmark points; it does not cover the finite-width, lifetime-sensitive, incomplete-width, or mass-grid-edge points.

The maximum raw observed signal-strength ratio in the full tau sample is above one only in points that fail the narrow-width screen; among the narrow/prompt-proxy evaluated points, the maximum is 0.1353. Therefore the tau search does not exclude any point in the currently evaluated narrow/prompt subset.

## 5. Interpretation and limits of the result

The pointwise table supports a **conditional narrow-width/prompt reinterpretation** of the two published scalar coupling-limit curves:

- The four-muon search conditionally excludes 1,852 sampled UV points in its narrow/prompt proxy subset.
- The tau-pair search excludes no sampled UV points in its corresponding narrow/prompt proxy subset.
- Neither result is a full detector-level recast or an event-level CLs calculation.
- The 5 mm flight comparison does not establish detector acceptance for displaced decays.
- The \(\Gamma/\sigma<0.10\) tolerance is an internal screen, not an experimental cut.
- The coupling-limit interpolation is log-log between published mass points.
- The production-rate mapping assumes the same spin-0 muon-FSR matrix element normalization as the experimental scalar benchmark. A separate MadGraph cross-section validation is still required.
- No full Crystal Ball response parameter sets are available in the archived numerical supplements, so no finite-width convolution has been performed.
- No lifetime-dependent scalar selection efficiencies are published for the UV model.
- The double-virtual four-body region is not included in this pointwise classification because the currently archived scan CSV predates the bounded four-body update. Those points remain unclassified until the updated scan is executed and exported.

The full pointwise outputs are generated by narrow_prompt_benchmark_recast.py and stored as separate four-muon and tau-pair CSV files. This research result does not modify the formal referee response or the manuscript.

## 6. Reproduction

Run:
- narrow_prompt_benchmark_recast.py
- test_narrow_prompt_benchmark_recast.py

The tests cover the coupling mappings, the reference tau branching fraction, the \(J/\psi\) veto, the incomplete-width guard, and the no-extrapolation rule.

## 7. Sources

1. Belle II Collaboration, *Search for a \(\mu^+\mu^-\) resonance in four-muon final states at Belle II*, Phys. Rev. D **109**, 112015 (2024), arXiv:2403.02841: https://arxiv.org/abs/2403.02841. The paper documents the 178 fb\(^{-1}\) sample, dedicated scalar simulation, p-wave scalar production, reduced-mass fit, 2--5 MeV resolution, double-Crystal-Ball signal model, and 90% CL scalar coupling limits.
2. Belle II four-muon supplementary numerical table, archived in this PR at data/raw/belleii/four-muon/S_supplemental.txt; official publication record: https://docs.belle2.org/pub_data/publications/4383/.
3. Belle II Collaboration, *Search for a \(\tau^+\tau^-\) resonance in \(e^+e^-\to\mu^+\mu^-\tau^+\tau^-\) events with the Belle II experiment*, Phys. Rev. Lett. **131**, 121802 (2023), arXiv:2306.12294: https://arxiv.org/abs/2306.12294. The paper documents the 62.8 fb\(^{-1}\) sample, scalar benchmark, recoil-mass fit, mass-dependent resolution, scalar efficiency comparison, and 90% CL coupling limits.
4. Belle II tau-pair supplementary numerical table, archived in this PR at data/raw/belleii/tau-pair/limits.csv; official publication record: https://docs.belle2.org/pub_data/documents/4407/.
5. Mass-proportional leptophilic-scalar normalization, \(\mathcal L\supset-\xi\sum_\ell(m_\ell/v)S\bar\ell\ell\), \(v=246\) GeV: https://link.springer.com/article/10.1140/epjc/s10052-022-10207-1.
6. Muonphilic scalar coupling normalization, \(\mathcal L\supset g_SS\bar\mu\mu\): Belle II conference material https://docs.belle2.org/files/2204/BELLE2-TALK-CONF-2023-116/1/BELLE2-TALK-CONF-2023-116.pdf and the Belle II publication above.
