# Independent audit of the Belle II scalar-limit mapping — 2026-11-09

**PR:** #68  
**Scope:** external-paper cross-check of the published-limit mapping used by the current pointwise reinterpretation.  
**Result:** the two channel mappings are structurally consistent with the published scalar benchmarks, subject to the explicitly stated narrow/prompt and production-normalization assumptions. This audit does not generate a new exclusion or CLs result.

## 1. Four-muon search: benchmark match

Belle II arXiv:2403.02841 searches \(e^+e^-\to\mu^+\mu^-X\), \(X\to\mu^+\mu^-\), over \(0.212\)--\(9.000\) GeV. The paper treats both the \(L_\mu-L_\tau\) vector and a muonphilic spin-zero scalar as separate signal hypotheses.

The scalar is produced through a p-wave process, whereas the vector benchmark is produced through an s-wave process. The paper explicitly provides separate scalar and vector full-selection efficiencies. Therefore:
- use the published scalar coupling-limit column for the scalar reinterpretation;
- do not substitute the vector efficiency or vector coupling limit;
- do not apply a second scalar-efficiency correction to the published scalar coupling limit, because the scalar signal efficiency is already included in the experimental limit.

The fit variable is
\[
M_R=\sqrt{M_{\mu\mu}^2-4m_\mu^2}.
\]
The width conversion used in the recast follows the local Jacobian:
\[
\Gamma_{M_R}\simeq
\left.\frac{dM_R}{dM_{\mu\mu}}\right|_{M_{\mu\mu}=m_s}\Gamma_s
=\frac{m_s}{\sqrt{m_s^2-4m_\mu^2}}\Gamma_s.
\]
This is a narrow-resonance mapping. It is not a substitute for convolving a finite-width signal with the experimental two-Crystal-Ball response and repeating the fit.

The paper performs 2,315 mass-hypothesis fits, uses a scan step equal to the resolution and a fit interval of \(60\sigma\), and vetoes \(3.07\)--\(3.12\) GeV around the \(J/\psi\). The archived supplement has 2,317 rows; that discrepancy remains unresolved and is not silently repaired.

## 2. Tau-pair search: benchmark match

Belle II arXiv:2306.12294 searches \(e^+e^-\to\mu^+\mu^-X\), \(X\to\tau^+\tau^-\), over \(3.6\)--\(10\) GeV. The paper identifies a leptophilic scalar with Yukawa-like couplings proportional to charged-lepton masses and parameterized by \(\xi\).

The production is predominantly final-state radiation from one of the two tagging muons. The coupling convention used in the mapping is
\[
\mathcal L_{\rm Belle}\supset
-\xi\sum_{\ell=e,\mu,\tau}\frac{m_\ell}{v_h}s\bar\ell\ell,
\qquad
\xi_{\rm UV}=\frac{v_h}{v_s},
\]
so the muon production coupling maps to
\[
g_{s\mu\mu}^{\rm UV}=\frac{m_\mu}{v_s}.
\]

The Belle reference branching fraction includes \(e,\mu,\tau\):
\[
{\rm BR}_{\tau\tau}^{\rm Belle}(m_s)=
\frac{m_\tau^2\beta_\tau^3}
{\sum_{\ell=e,\mu,\tau}m_\ell^2\beta_\ell^3},
\qquad
\beta_\ell=\sqrt{1-\frac{4m_\ell^2}{m_s^2}}.
\]
The original \(L_\mu-L_\tau\) UV scalar has no direct electron Yukawa in the minimal construction. Its UV branching fraction must therefore be compared to, not identified with, the Belle reference branching fraction.

The appropriate narrow/prompt rate ratio is
\[
R_{\tau\tau}=
\left(\frac{\xi_{\rm UV}}{\xi_{90}}\right)^2
\frac{{\rm BR}_{\tau\tau}^{\rm UV}}
{{\rm BR}_{\tau\tau}^{\rm Belle}}.
\]
This confirms the structure implemented in the pointwise mapping.

The paper reports a 10--20% relative signal-efficiency difference when comparing the alternative scalar and ALP models with the \(L_\mu-L_\tau\) vector benchmark. That comparison is not a reason to rescale the scalar-specific published limit: the analysis checks the scalar signal model separately and publishes scalar-specific coupling limits. The paper also reports a mass-dependent trigger efficiency, a \(0.5\) cm transverse and \(2.0\) cm longitudinal track-DCA selection, and a two-Crystal-Ball recoil-mass model. These facts reinforce that the 5 mm mean-flight proxy is only a geometry diagnostic, not a detector efficiency or literal scalar decay-radius cut.

## 3. Pointwise classification logic

The current conservative exclusion rule is logically sufficient for the declared approximation:
1. satisfy the scalar quartic and scalar Yukawa perturbativity criteria;
2. lie within the published mass-limit table and outside the \(J/\psi\) veto where applicable;
3. have a bounded UV branching-fraction interval;
4. pass the full upper width/resolution endpoint below the internal \(0.10\) diagnostic;
5. pass the full upper mean-flight proxy below \(5\) mm;
6. have the lower endpoint of the observed UV/reference signal-strength ratio strictly above one.

The \(0.10\) and \(5\) mm values are internal conservative proxies, not Belle II cuts. Consequently the 2,746 four-muon points remain conditional pointwise exclusions under the published narrow/prompt scalar benchmark, not a new detector-level Belle II CLs result. The zero tau-pair exclusions apply only to the evaluated narrow/prompt subset.

## 4. Independent conclusion and remaining checks

The channel-specific coupling and branching-fraction mapping is supported by the original experimental model definitions. No additional scalar-efficiency rescaling should be applied to the published scalar limits.

The next numerical audit should independently recompute selected grid rows directly from the archived limit tables and width scan, including:
- one four-muon point below the muon threshold, one above it, and one close to the \(J/\psi\) veto;
- one tau-pair point just above \(2m_\tau\), one near 6 GeV, and one near the upper end of the limit table;
- the limiting points nearest \(R_{\rm obs}=1\);
- points nearest the width and prompt-proxy boundaries.

The check should compare interpolated limits, UV couplings, reference and UV branching fractions, width Jacobians, and all classification inequalities. The published tables and the CSV source rows must be retained without extrapolation. Finite-width and displaced cases remain unclassified until the required response and lifetime-dependent efficiency inputs are available.

## 5. Primary sources

- Belle II, arXiv:2403.02841, especially the separate scalar/vector efficiency discussion and the reduced-mass signal fit: https://arxiv.org/abs/2403.02841
- Belle II, arXiv:2306.12294, especially the leptophilic-scalar definition, muon-FSR production, efficiency study, recoil-mass fit, and \(\xi\) interpretation: https://arxiv.org/abs/2306.12294
