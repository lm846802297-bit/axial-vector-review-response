# Belle II scalar-benchmark normalization and original-UV mapping

**Record date:** 2026-11-05  
**Research scope:** the original paper's single-VEV \(S+\mathrm{VLL}\) model only.  
**Status:** source-level model mapping and analytic branching-ratio diagnostics completed; supplemental numerical files not yet downloaded or transcribed; no experimental recast claimed.

## 1. Model-scope lock

The UV model used throughout this note is the original paper's one-VEV construction:

\[
m_{A'}=2g_Xv_s,\qquad
m_s^2=2\lambda_Sv_s^2,\qquad
y_{s\ell\ell}=\frac{m_\ell}{v_s},\quad \ell=\mu,\tau.
\]

The electron has no corresponding direct \(U(1)_{L_\mu-L_\tau}\)-breaking Yukawa in this model. No second scalar VEV, right-handed neutrino, or alternative neutrino completion enters this analysis.

## 2. Belle II four-muon search: a muonphilic-scalar benchmark

**Source:** I. Adachi et al. (Belle II), *Search for a \(\mu^+\mu^-\) resonance in four-muon final states at Belle II*, Phys. Rev. D **109**, 112015 (2024), arXiv:2403.02841, DOI: 10.1103/PhysRevD.109.112015.

The analysis searches for
\[
e^+e^-\to\mu^+\mu^-X,\qquad X\to\mu^+\mu^-,
\]
using \(178\,\mathrm{fb}^{-1}\), at \(\sqrt{s}=10.58\,\mathrm{GeV}\), over \(m_X=0.212\text{--}9.0\,\mathrm{GeV}\). It reports observed 90% CL limits on \(\sigma(e^+e^-\to\mu^+\mu^-X)\,\mathrm{BR}(X\to\mu^+\mu^-)\), and a corresponding muonphilic-scalar coupling \(g_S\). The abstract-level scalar ranges are \(0.055\text{--}1.3\,\mathrm{fb}\) and \(g_S\simeq0.0018\text{--}0.040\) below \(6\,\mathrm{GeV}\); these ranges are not a substitute for the mass-by-mass supplement.

Important analysis facts:

- The scalar is emitted as final-state radiation from a muon. Its production rate scales as \(g_S^2\) for the same scalar interaction and fixed mass.
- The collaboration generated scalar signal samples separately from the vector benchmark. The scalar is produced through a p-wave process, whereas the vector benchmark is s-wave; the scalar has a harder momentum spectrum and different selection efficiency, particularly at low mass.
- The paper explicitly cautions that reinterpretations which borrow vector efficiencies can miss these differences.
- The scalar lifetime is negligible compared with detector resolution for the coupling range studied by the collaboration.

**Mapping to the original UV scalar:** the UV muon coupling is \(y_{s\mu\mu}=m_\mu/v_s\). Below the tau threshold, if \(s\to A'A'\) is closed and portal-mediated modes are negligible, the direct dimuon topology can approach the muonphilic benchmark. Above \(2m_\tau\), the UV scalar also has \(s\to\tau^+\tau^-\), which reduces \(\mathrm{BR}(s\to\mu^+\mu^-)\). If \(m_s>2m_{A'}\), the additional \(s\to A'A'\) channel can reduce it further. Therefore the published \(g_S\) curve is not a direct UV limit without a branching-fraction and lifetime check.

For the same scalar production matrix element and acceptance, a coupling limit inferred from a published \(\sigma\times\mathrm{BR}_{\mu\mu}\) curve rescales as
\[
g_{\mu,\mathrm{lim}}^{\mathrm{UV}}
=
g_{S,\mathrm{lim}}^{\mathrm{Belle}}
\sqrt{
\frac{\mathrm{BR}_{\mu\mu}^{\mathrm{Belle}}}
     {\mathrm{BR}_{\mu\mu}^{\mathrm{UV}}}
     }.
\]
The Belle muonphilic benchmark has \(\mathrm{BR}_{\mu\mu}^{\mathrm{Belle}}\simeq1\) under its benchmark assumptions. The UV branching fraction must be computed from the complete set of open channels; an incomplete partial-width sum is not sufficient.

## 3. Belle II tau-pair search: a mass-proportional leptophilic-scalar benchmark

**Source:** I. Adachi et al. (Belle II), *Search for a \(\tau^+\tau^-\) resonance in \(e^+e^-\to\mu^+\mu^-\tau^+\tau^-\) events with the Belle II experiment*, Phys. Rev. Lett. **131**, 121802 (2023), arXiv:2306.12294, DOI: 10.1103/PhysRevLett.131.121802.

The analysis searches for
\[
e^+e^-\to\mu^+\mu^-X,\qquad X\to\tau^+\tau^-,
\]
using \(62.8\,\mathrm{fb}^{-1}\), at \(\sqrt{s}=10.58\,\mathrm{GeV}\), over \(m_X=3.6\text{--}10\,\mathrm{GeV}\). The observed 90% CL limits are on \(\sigma(e^+e^-\to\mu^+\mu^-X)\,\mathrm{BR}(X\to\tau^+\tau^-)\). The abstract gives an overall range of approximately \(0.7\text{--}24\,\mathrm{fb}\); it is not a pointwise dataset.

The leptophilic scalar benchmark uses mass-proportional charged-lepton Yukawa couplings:
\[
\mathcal L_{\mathrm{Belle}}\supset
-\xi\sum_{\ell=e,\mu,\tau}
\frac{m_\ell}{v}\,S\bar\ell\ell,
\qquad v=246\,\mathrm{GeV}.
\]
The same normalization is documented in the Belle II thesis associated with this analysis. The original UV model has
\[
y_{s\mu\mu}=\frac{m_\mu}{v_s},\qquad
y_{s\tau\tau}=\frac{m_\tau}{v_s}.
\]
Consequently, for the muon and tau couplings,
\[
\boxed{\xi_{\mathrm{UV}}=\frac{v}{v_s}
=\frac{2vg_X}{m_{A'}}.}
\]
This is a coupling-normalization match, not yet a full collider reinterpretation. The Belle benchmark also includes an electron Yukawa, whereas the original \(L_\mu-L_\tau\) model does not; in this mass range the electron partial width is negligible relative to the muon/tau widths. The more important differences are additional UV decay channels, especially \(s\to A'A'\), and any portal-mediated widths.

The collaboration applies the full selection to the scalar signal samples. Its scalar efficiencies differ from the \(Z'\) efficiencies by 10–20%; the vector efficiency must not be substituted for the scalar one. The search reconstructs one-prong tau decays and uses a recoil-mass peak against the two tagging muons.

### 3.1 Threshold effect in the original UV model

For the mass-proportional UV Yukawas and with only the \(\mu^+\mu^-\) and \(\tau^+\tau^-\) channels open,
\[
\Gamma(s\to\ell^+\ell^-)
=\frac{m_\ell^2}{v_s^2}\frac{m_s}{8\pi}
\left(1-\frac{4m_\ell^2}{m_s^2}\right)^{3/2}.
\]
Thus
\[
\mathrm{BR}_{\tau\tau}^{(\mu+\tau)}
=
\frac{m_\tau^2\beta_\tau^3}
     {m_\tau^2\beta_\tau^3+m_\mu^2\beta_\mu^3},
\qquad
\beta_\ell=\sqrt{1-\frac{4m_\ell^2}{m_s^2}}.
\]
The result is independent of \(v_s\) in this restricted two-channel limit.

| \(m_s\) (GeV) | \(\mathrm{BR}_{\tau\tau}^{(\mu+\tau)}\) | \(\mathrm{BR}_{\mu\mu}^{(\mu+\tau)}\) |
|---:|---:|---:|
| 3.6 | 0.5372 | 0.4628 |
| 3.7 | 0.8598 | 0.1402 |
| 4.0 | 0.9649 | 0.0351 |
| 5.0 | 0.9900 | 0.0100 |
| 6.0 | 0.9933 | 0.0067 |
| 8.0 | 0.9951 | 0.0049 |
| 10.0 | 0.9957 | 0.0043 |

The rapid change immediately above \(2m_\tau\) is important. A constant approximation \(\mathrm{BR}_{\tau\tau}\simeq1\) is not valid at the lower edge of the Belle II tau-search window.

For the same production normalization, the coupling-limit translation is
\[
\xi_{\mathrm{lim}}^{\mathrm{UV}}
=
\xi_{\mathrm{lim}}^{\mathrm{Belle}}
\sqrt{
\frac{\mathrm{BR}_{\tau\tau}^{\mathrm{Belle}}}
     {\mathrm{BR}_{\tau\tau}^{\mathrm{UV}}}
     }.
\]
This expression is usable only after both branching fractions and the scalar-specific acceptance/lifetime assumptions have been validated.

## 4. The \(s\to A'A'\) channel can dominate

In the original one-VEV model, the radial-mode width is
\[
\Gamma(s\to A'A')
=\frac{m_s^3}{32\pi v_s^2}
\sqrt{1-4r_A}\,(1-4r_A+12r_A^2),
\qquad r_A=\frac{m_{A'}^2}{m_s^2},
\]
for \(m_s>2m_{A'}\). Comparing with the tau width gives
\[
\frac{\Gamma_{A'A'}}{\Gamma_{\tau\tau}}
=
\frac{m_s^2}{4m_\tau^2}
\frac{
\sqrt{1-4r_A}(1-4r_A+12r_A^2)
}{
(1-4m_\tau^2/m_s^2)^{3/2}
}.
\]
For illustration, in the limit \(m_{A'}\ll m_s\) (so the vector-pair phase-space factor approaches one), this ratio is approximately 251 at \(m_s=3.6\,\mathrm{GeV}\), 13.1 at 4 GeV, 5.69 at 5 GeV, and 9.70 at 10 GeV. These are analytic ratios, not an exclusion. They show that once the channel is open it can substantially suppress both direct \(\mu\mu\) and \(\tau\tau\) branching fractions. The subsequent \(A'\) decays define different final states and cannot be counted as the Belle II direct-resonance signal without a separate acceptance analysis.

## 5. Recast equation and acceptance requirements

For a fixed scalar mass, the leading production process in both analyses is scalar final-state radiation from a tagged muon. If the Lorentz structure and selection acceptance are matched, the production rate scales as \(|y_{s\mu\mu}|^2\) or \(\xi^2\). For an observable \(\sigma\times\mathrm{BR}_f\), the coupling rescaling is
\[
g_{\mathrm{lim}}^{\mathrm{UV}}
=
g_{\mathrm{lim}}^{\mathrm{benchmark}}
\sqrt{\frac{\mathrm{BR}_f^{\mathrm{benchmark}}}
           {\mathrm{BR}_f^{\mathrm{UV}}}},
\]
where \(g\) denotes the corresponding scalar Yukawa normalization. This relation must not be used if the signal kinematics, lifetime, or efficiency differs. In that case the UV signal yield must be recomputed using the published scalar efficiency or a validated detector-level simulation.

The two analyses are not interchangeable:

- Four-muon: use the dedicated muonphilic-scalar efficiency and \(\mathrm{BR}_{\mu\mu}\); do not use the \(Z'\) efficiency.
- Tau-pair: use the dedicated mass-proportional scalar efficiency and \(\mathrm{BR}_{\tau\tau}\); do not use the \(Z'\) efficiency.
- Recast the two channels independently. Do not combine their limits by taking the smaller quoted coupling number.
- Check the prompt-lifetime assumption at each UV point. A partial-width sum cannot certify promptness.

## 6. Numerical supplement retrieval and benchmark-reproduction status

The official source pages identify the required mass-dependent data files:

1. Four-muon scalar supplement: S_supplemental.txt, from https://journals.aps.org/prd/supplemental/10.1103/PhysRevD.109.112015
2. Tau-pair supplement: limits.csv and limits.txt, from https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802

The four-muon paper states that the supplement contains the observed cross sections and observed 90% CL upper limits on the cross section and \(g_S\) as functions of mass. The tau-pair paper states that its supplement contains numerical cross-section and coupling results, and the arXiv record lists limits.csv as an ancillary file.

**Not yet done:** raw files have not been retrieved into this repository, no per-mass rows have been transcribed, and neither experimental scalar benchmark has been numerically reproduced. The abstract-level ranges above are orientation only. No values have been digitized from plots and presented as exact numerical data.

## 7. Acceptance gates

- [x] Original single-VEV model boundary stated.
- [x] Belle II scalar benchmark normalizations and channel topologies audited at source level.
- [x] Analytic \(\mu\mu/\tau\tau\) branching-ratio threshold effect evaluated.
- [x] Analytic importance of \(s\to A'A'\) identified.
- [ ] Download the exact official supplemental files and record SHA-256 hashes.
- [ ] Parse and archive the mass grid, units, observed/expected status, confidence level, and all coupling/cross-section columns.
- [ ] Reproduce the Belle II scalar benchmark curves from the source files.
- [ ] Validate the original-UV total width, branching fractions, lifetime, and production normalization point by point.
- [ ] Apply each published limit independently with the scalar-specific acceptance.
- [ ] Classify points as excluded / passes evaluated constraints / unclassified / theoretically inconsistent.
- [ ] Do not modify the formal Major Point 1 response unless the author separately approves a specific validated result for inclusion.

## Sources

- Belle II four-muon search, arXiv:2403.02841v2: https://arxiv.org/html/2403.02841
- Belle II four-muon published paper: https://doi.org/10.1103/PhysRevD.109.112015
- Belle II four-muon supplemental page: https://journals.aps.org/prd/supplemental/10.1103/PhysRevD.109.112015
- Belle II tau-pair search, arXiv:2306.12294v2: https://arxiv.org/html/2306.12294v2
- Belle II tau-pair published paper: https://doi.org/10.1103/PhysRevLett.131.121802
- Belle II tau-pair supplemental page: https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802
- Belle II thesis recording the scalar interaction normalization and \(v=246\,\mathrm{GeV}\): https://docs.belle2.org/files/4004/BELLE2-PTHESIS-2022-007/1/BELLE2-PTHESIS-2022-007.pdf
- Batell et al., *Muon anomalous magnetic moment and leptophilic scalar*, arXiv:1606.04943: https://arxiv.org/abs/1606.04943
