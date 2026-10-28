# Direct-search source matrix — two UV benchmarks

**Date:** 2026-10-28  
**Branch:** research/higgs-signal-strength-two-benchmarks-2026-10-28  
**Status:** source applicability audit and conservative rate screening; not a detector-level recast.

## Executive result

A directly relevant published search has been identified: ATLAS HDBS-2021-13, *Search for a new scalar decaying into new spin-1 bosons in four-lepton final states with the ATLAS detector*, Phys. Lett. B 865 (2025) 139472, DOI 10.1016/j.physletb.2025.139472; arXiv:2410.16781. The paper's numerical results are also deposited in the official HEPData record: https://www.hepdata.net/record/145171.

The analysis searches for a prompt scalar \(S\to Z_dZ_d\to4\ell\), with \(\ell=e,\mu\), and reports 95% CL upper limits on \(\sigma(gg\to S)\,\mathrm{BR}(S\to Z_dZ_d\to4\ell)\). The paper's abstract describes the analysis regions as \(30<m_S<115\) GeV and \(130<m_S<800\) GeV, with \(15<m_{Z_d}<300\) GeV. **Important qualification:** the paper's signal-simulation section states that the generated high-mass signal samples cover \(150\le m_S\le800\) GeV, not a dedicated generated point at \(m_S=130\) GeV. The \(m_{4\ell}>130\) GeV requirement is the signal-region boundary; it must not be confused with a generated \(m_S=130\) GeV signal sample.

**Benchmark A (\(m_{A'}=10\) GeV):** this search is not directly applicable. The intermediate mass is below the analysis's generated \(m_{Z_d}\ge15\) GeV range, and every dilepton pairing must satisfy \(m_{\ell\ell}>11.105\) GeV. A direct \(A'\to\ell^+\ell^-\) pair at 10 GeV fails that requirement. Do not extrapolate this published limit to Benchmark A.

**Benchmark B (\(m_{A'}=63\) GeV):** the on-shell \(s\to A'A'\) channel opens at \(m_s>126\) GeV. The ATLAS high-mass analysis is therefore a relevant search topology above its \(m_{4\ell}>130\) GeV selection threshold, but the first generated high-mass scalar sample stated in the paper is at \(m_S=150\) GeV. A conservative rate screen should therefore be evaluated at \(m_s=150\) GeV, the first documented generated scalar mass, rather than at 130 GeV. The exact point-specific observed limit near \(m_{A'}=63\) GeV remains to be extracted from HEPData Table 15; the direct CSV retrieval was blocked in this pass, so no point-specific number is invented.

## 1. Verified source details

- ATLAS Collaboration, HDBS-2021-13, arXiv:2410.16781; Phys. Lett. B 865 (2025) 139472.
- Preprint: https://arxiv.org/abs/2410.16781
- Full text: https://escholarship.org/uc/item/9g9590fs
- Official numerical record: https://www.hepdata.net/record/145171
- HEPData Table 15 is identified as the observed 95% CL limit in SR2, i.e. the high-mass region with the \(Z\)-mass veto.
- The analysis uses \(139\,\mathrm{fb}^{-1}\) of \(pp\) data at \(\sqrt{s}=13\) TeV and requires prompt decays.
- The observable is the scalar production cross section times branching fraction into the selected four-lepton final state, not a universal bound on a scalar mixing angle.
- The analysis selects \(4e\), \(2e2\mu\), and \(4\mu\) candidates; every dilepton pairing must satisfy \(m_{\ell\ell}>11.105\) GeV. The higher-mass signal region also applies a \(Z\)-mass veto to the dilepton pairings.
- Published observed 95% CL limit ranges are 0.14–3.1 fb in the lower-mass region and 0.05–0.60 fb in the higher-mass region. These are overall ranges across the mass plane, not the exact limit at a specific \((m_s,m_{A'})\) point.
- The paper states that its high-mass simulated signal samples span \(150\le m_S\le800\) GeV and \(15\le m_{Z_d}\le300\) GeV, subject to \(m_S>2m_{Z_d}\).

## 2. Benchmark-by-benchmark applicability

| Requirement | Benchmark A: \(m_{A'}=10\) GeV | Benchmark B: \(m_{A'}=63\) GeV |
|---|---|---|
| On-shell \(s\to A'A'\) near \(m_s=125.25\) GeV | Open | Closed because \(2m_{A'}=126\) GeV |
| ATLAS intermediate-vector mass range \(15\)–\(300\) GeV | **Fails** | Passes |
| ATLAS pair-mass requirement \(m_{\ell\ell}>11.105\) GeV | **Fails** for direct \(A'\to\ell\ell\) pairs at 10 GeV | Passes for 63 GeV pairs |
| Kinematic opening of \(s\to A'A'\) | \(m_s>20\) GeV | \(m_s>126\) GeV |
| First documented high-mass scalar MC point | Not applicable to this \(A'\) mass | \(m_S=150\) GeV; the \(m_{A'}=63\) GeV limit requires the table grid/interpolation to be checked |
| Promptness | Expected for the stated \(g_X\), but does not fix the mass-selection mismatch | Expected for the stated \(g_X=0.1\); scalar width is evaluated below |
| Present classification from this source | **Not applicable; no exclusion inferred** | Relevant topology; preliminary production-rate screen is far below the published sensitivity scale; no formal recast claimed |

## 3. Corrected conservative non-degenerate rate screen for Benchmark B

Use the inherited matched self-energy
\[
\Pi_B=(-0.09300-0.02547i)\,\mathrm{GeV}^2,
\qquad |\Pi_B|=0.096425\,\mathrm{GeV}^2,
\]
with \(m_h=125.25\) GeV. Because the documented high-mass signal simulation starts at \(m_S=150\) GeV, evaluate the non-degenerate screening proxy at \(m_s=150\) GeV:

\[
\epsilon_{\mathrm{nd}}(150)
=\frac{|\Pi_B|}{|m_h^2-(150\,\mathrm{GeV})^2|}
\simeq1.415\times10^{-5},
\]

\[
\epsilon_{\mathrm{nd}}^2\simeq2.003\times10^{-10}.
\]

This is **not** a pole-scheme physical mixing angle. It is only a fixed-self-energy estimate away from pole overlap. If the scalar is produced only through Higgs mixing, the isolated-state production estimate is

\[
\sigma(gg\to s)\simeq \epsilon_{\mathrm{nd}}^2
\,\sigma_{\mathrm{ggF}}^{\mathrm{SM}}(m_s).
\]

For a conservative upper envelope, take \(\sigma_{\mathrm{ggF}}^{\mathrm{SM}}(150\,\mathrm{GeV})<50\) pb, which is above the recommended 13 TeV SM gluon-fusion cross section at this mass. Then

\[
\sigma(gg\to s)\lesssim
2.003\times10^{-10}\times50\,\mathrm{pb}
\simeq1.00\times10^{-5}\,\mathrm{fb}.
\]

This is the inclusive scalar production estimate **before** multiplying by any branching fraction. The smallest published observed upper limit reported over the entire high-mass plane is 0.05 fb. Therefore the conservative production estimate is at least a factor of about \(5.0\times10^3\) below that global best-sensitivity value, even under the extreme assumption \(\mathrm{BR}(s\to A'A'\to4\ell)=1\). This comparison is a robust order-of-magnitude screening statement, not a point-specific exclusion test.

For orientation, with the inherited tree-level radial-scalar normalization at \(m_s=150\) GeV, \(m_{A'}=63\) GeV and \(v_s=315\) GeV,

\[
\Gamma(s\to A'A')=
\frac{m_s^3}{32\pi v_s^2}
\sqrt{1-\frac{4m_{A'}^2}{m_s^2}}
\left(1-\frac{4m_{A'}^2}{m_s^2}
+12\frac{m_{A'}^4}{m_s^4}\right)
\simeq0.123\,\mathrm{GeV}.
\]

This is prompt and narrow relative to the 150 GeV mass, but it is larger than the SM-Higgs width assumed in the ATLAS signal generation. A final reinterpretation should check whether this width difference changes the signal shape or acceptance; do not silently assume the generated width matches the model.

For the leading \(L_\mu-L_\tau\) couplings at \(m_{A'}=63\) GeV and \(g_X=0.1\), the tree-level branching fraction \(\mathrm{BR}(A'\to\mu^+\mu^-)\simeq1/3\) follows when the open channels are \(\mu^+\mu^-\), \(\tau^+\tau^-\), and the two active neutrino flavours, neglecting loop-induced electron couplings and additional states. The direct \(4\mu\) branching factor is then approximately
\[
\mathrm{BR}(s\to A'A'\to4\mu)
\simeq \mathrm{BR}(s\to A'A')
[\mathrm{BR}(A'\to\mu^+\mu^-)]^2
\lesssim\frac19.
\]
Using the conservative production envelope gives
\[
\sigma(gg\to s\to4\mu)\lesssim1.1\times10^{-6}\,\mathrm{fb}.
\]
This is only a partial-final-state estimate; the exact \(4e\) and mixed-flavour contributions require the model's loop-induced kinetic-mixing normalization. The more conservative inclusive-rate comparison above does not depend on those branching-fraction details because every selected four-lepton rate is bounded by the inclusive production rate.

## 4. Exact point-specific limit: retrieval status

The official HEPData record lists Table 15 as the observed 95% CL limit in SR2:
https://www.hepdata.net/record/145171

The HEPData record page and paper's table inventory were accessible, but direct retrieval of the CSV/YAML payload for Table 15 was blocked by the current browsing environment. Accordingly:

- no exact observed limit at \((m_s,m_{A'})=(150,63)\) GeV is quoted here;
- no value is digitized from the figure and mislabelled as exact;
- the global minimum 0.05 fb is used only as a conservative sensitivity scale;
- the final source-specific check still needs the Table 15 data grid and a justified interpolation in \(m_{A'}\), if \(63\) GeV is not itself a published grid point.

This limitation does not undermine the preliminary rate hierarchy: the estimated inclusive production rate at 150 GeV is already thousands of times below the best observed limit scale, before applying any four-lepton branching fraction. It does mean that the result should not be described as a completed experimental recast.

## 5. Other constraints: what can and cannot be imported

### Higgs signal strength

ATLAS-CONF-2025-006 reports the global signal strength \(\mu=1.023^{+0.056}_{-0.053}\). This is useful for an approximate inclusive-rate sanity check, but it does not constrain the full scalar parameter space by itself. Benchmark A additionally has the \(h\to A'A'\) channel open through the singlet admixture, while Benchmark B has \(2m_{A'}>m_h\). Near \(m_s\simeq m_h\), a single-angle \(\mu\simeq\cos^2\theta\) treatment is invalid without a pole-consistent two-state calculation.

### Generic LEP singlet-scalar limits

Published LEP limits commonly assume SM-Higgs-like branching fractions or a specified visible/invisible final state. They are not automatically transferable to Benchmark A, where \(s\to A'A'\) is open throughout the 65–115 GeV region, or to Benchmark B without a point-specific branching-ratio calculation. A separate LEP reinterpretation would need the actual search observable and efficiencies for the relevant \(A'A'\) final states. No LEP exclusion is assigned here.

### Other LHC scalar searches

The ATLAS \(S\to Z_dZ_d\to4\ell\) analysis is the closest directly matched public search identified for Benchmark B above threshold. Searches of the 125 GeV Higgs for \(H\to Z_dZ_d\) are not interchangeable with direct production of a separate \(s\) resonance: the parent mass, production rate, and signal selection differ. Generic heavy-scalar \(ZZ\) searches also do not directly match a pair of 63 GeV \(A'\) bosons with \(L_\mu-L_\tau\) branching fractions.

### New CMS heavy-resonance search for \(m_{A'}\simeq10\) GeV

A newer, relevant topology has also been identified: CMS-EXO-24-006, *Search for heavy resonances decaying into four-lepton final states via light bosons in proton-proton collisions at \(\sqrt{s}=13\) TeV*, arXiv:2604.14236 (submitted to PRL in April 2026). It uses \(138\,\mathrm{fb}^{-1}\), covers \(m_X=250\text{--}2000\) GeV and \(m_Y>0.4\) GeV, and explicitly includes generated hypotheses at \(m_Y=10\) GeV. The publication reports model-independent limits on \(\sigma(pp\to X)\times\mathrm{BR}(X\to YY\to4\ell)\), including exclusive \(4\mu\) results. Source: https://arxiv.org/abs/2604.14236 and CMS result page https://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-24-006/index.html.

This search is a candidate for Benchmark A only in the high-mass scalar region \(m_s\gtrsim250\) GeV; it does not cover the \(m_s=65\text{--}115\) GeV region that failed the ATLAS HDBS-2021-13 selection. More importantly, CMS generated \(X\) and \(Y\) with a narrow-width assumption \(\Gamma/M=10^{-4}\). For the present Benchmark A, the tree-level \(s\to A'A'\) width is approximately \(30.6\) GeV at \(m_s=250\) GeV, i.e. \(\Gamma_s/m_s\simeq0.12\), using \(v_s=70.9\) GeV and \(m_{A'}=10\) GeV. This is orders of magnitude broader than the signal model used in the CMS limit. The published narrow-width limit therefore **must not be applied directly** to this benchmark without a broad-resonance reinterpretation.

The CMS analysis is valuable evidence that a low-mass \(A'\) four-lepton topology has been searched for at high \(m_s\), but it does not close the model-specific constraint gap by itself. The exact pointwise \(4\mu\) limit is also not extracted in this pass. The \(s\to A'A'\) width and the validity of the one-loop mixing/production proxy must be assessed consistently before this channel can be used quantitatively.

## 6. The 125 GeV Higgs exotic-decay searches and the \(m_{A'}=10\) GeV benchmark

A separate class of searches constrains the **125 GeV Higgs-like state** decaying as \(h\to A'A'\to4\ell\). These searches are relevant to the loop-induced Higgs-singlet admixture, but they are not searches for direct production of the separate scalar \(s\) with \(m_s=65\text{--}115\) GeV. The two topologies must not be conflated.

### ATLAS H→XX→4μ (139 fb⁻¹)

ATLAS 2110.13673 covers \(1<m_X<15\) GeV in its low-mass \(H\to XX\to4\mu\) analysis. However, the low-mass selection explicitly rejects events if either reconstructed dimuon mass lies in \(8\text{--}12\) GeV. Therefore the benchmark \(m_{A'}=10\) GeV falls inside the quarkonium-veto window and **does not receive a valid point-specific constraint from that four-muon limit**. Source: https://arxiv.org/abs/2110.13673; the selection and veto are described in the paper's Table 2 and low-mass event-selection section.

### CMS HIG-19-007 (137 fb⁻¹)

CMS also searches for \(H\to XX\to4\ell\) and reports limits on products of Higgs branching fractions and \(X\to\ell\ell\) branching fractions. Its published limit plots mark the excluded \(\Upsilon\)-resonance region. The \(m_X=10\) GeV benchmark lies in that resonance-veto region, so the plotted limit should not be read as a normal exclusion at this exact mass. Source: https://cms-results.web.cern.ch/cms-results/public-results/publications/HIG-19-007/index.html and https://arxiv.org/abs/2111.01299.

### Conditional estimate of the exotic Higgs branching fraction

For Benchmark A, take the inherited fixed one-loop self-energy
\[
|\Pi_{hs}(m_h^2)|=|{-0.4133-0.1132i}|\,\mathrm{GeV}^2
\simeq0.42852\,\mathrm{GeV}^2.
\]
Away from degeneracy, use only as a proxy
\[
\epsilon_{\rm nd}(m_s)=
\frac{|\Pi_{hs}(m_h^2)|}{|m_h^2-m_s^2|},
\qquad
\Gamma(s\to A'A';m_h)\simeq3.742\,\mathrm{GeV}.
\]
Then
\[
\Gamma(h_{\rm like}\to A'A')
\simeq \epsilon_{\rm nd}^2\,
\Gamma(s\to A'A';m_h),
\]
and, with \(\Gamma_h^{\rm SM}=4.07\) MeV, the small-mixing branching-fraction proxy is
\[
\mathrm{BR}(h_{\rm like}\to A'A')
\simeq
\frac{\epsilon_{\rm nd}^2\Gamma(s\to A'A';m_h)}
{\Gamma_h^{\rm SM}+\epsilon_{\rm nd}^2\Gamma(s\to A'A';m_h)}.
\]

| \(m_s\) (GeV) | \(\epsilon_{\rm nd}\) | \(\mathrm{BR}(h_{\rm like}\to A'A')\) proxy | \(\Delta\mu_{\rm visible}\) proxy | \(4\mu\) proxy if \(\mathrm{BR}(A'\to\mu\mu)\simeq1/3\) |
|---:|---:|---:|---:|---:|
| 65 | \(3.74\times10^{-5}\) | \(1.29\times10^{-6}\) | \(1.29\times10^{-6}\) | \(1.43\times10^{-7}\) |
| 80 | \(4.61\times10^{-5}\) | \(1.96\times10^{-6}\) | \(1.96\times10^{-6}\) | \(2.17\times10^{-7}\) |
| 100 | \(7.53\times10^{-5}\) | \(5.22\times10^{-6}\) | \(5.23\times10^{-6}\) | \(5.80\times10^{-7}\) |
| 110 | \(1.19\times10^{-4}\) | \(1.31\times10^{-5}\) | \(1.31\times10^{-5}\) | \(1.46\times10^{-6}\) |
| 115 | \(1.74\times10^{-4}\) | \(2.78\times10^{-5}\) | \(2.79\times10^{-5}\) | \(3.09\times10^{-6}\) |

These numbers are **conditional screening estimates**, not a pole-scheme prediction: they hold \(\Pi_{hs}(m_h^2)\) fixed, use a tree-level mass denominator, and neglect a self-consistent two-pole treatment. The \(4\mu\) values also assume the approximate tree-level \(\mathrm{BR}(A'\to\mu^+\mu^-)\simeq1/3\). Most importantly, the ATLAS \(4\mu\) selection vetoes the \(m_{A'}=10\) GeV point, and the CMS plots likewise mark the \(\Upsilon\) region. These tiny rates are useful for assessing the inclusive Higgs-rate impact away from degeneracy; they do **not** convert the vetoed four-lepton searches into exclusions.

The direct-\(s\) scalar width in the same \(m_s=65\text{--}115\) GeV interval is approximately \(0.47\text{--}2.88\) GeV under the benchmark normalization. The ATLAS separate-scalar search in the 2025 paper also fails the \(m_{A'}=10\) GeV mass/pair-selection requirements, so no direct-\(s\) limit is assigned from that search.

## 7. Evidence ledger and next actions

1. **Verified:** a relevant ATLAS direct-search analysis exists and publishes cross-section-times-four-lepton-branching-ratio limits.
2. **Verified:** Benchmark A fails the \(A'\) mass coverage and explicit dilepton-mass requirement of the 2025 separate-scalar ATLAS analysis. The 2022 ATLAS \(H\to XX\to4\mu\) selection also explicitly vetoes \(m_{\mu\mu}=8\text{--}12\) GeV, so it does not constrain the exact \(m_{A'}=10\) GeV point; CMS HIG-19-007 marks the \(\Upsilon\) region as excluded as well.
3. **Verified:** Benchmark B's on-shell cascade is closed below 126 GeV and open above threshold.
4. **Verified correction:** the high-mass signal MC samples documented in the paper begin at \(m_S=150\) GeV; the \(m_{4\ell}>130\) GeV event-selection boundary is not itself a generated signal mass point.
5. **Preliminary analytic screen:** at \(m_s=150\) GeV, Benchmark B's non-degenerate mixing proxy gives an inclusive production estimate below \(1.1\times10^{-5}\) fb under the conservative 50 pb envelope, well below the overall 0.05 fb best-sensitivity scale even before branching fractions.
6. **New source identified, not yet applicable as a direct limit:** CMS-EXO-24-006 covers \(m_Y=10\) GeV and \(m_X\ge250\) GeV, but assumes \(\Gamma_X/m_X=10^{-4}\); the Benchmark A scalar has \(\Gamma_s/m_s\simeq0.12\) at 250 GeV. A broad-resonance reinterpretation would be required.
7. **Not yet done:** retrieve HEPData Table 15's numeric payload and determine the exact observed limit/interpolation at \(m_{A'}=63\) GeV; validate the pole-scheme mixing; complete \(A'\) branching fractions including kinetic mixing; validate detector-level acceptance; search for a non-vetoed direct-\(s\) search for Benchmark A; evaluate whether a broad-width CMS reinterpretation is worth pursuing.
8. **Do not claim:** a complete UV-allowed scalar-mass interval or a global experimental exclusion.

## Sources

- ATLAS Collaboration, *Search for a new scalar decaying into new spin-1 bosons in four-lepton final states with the ATLAS detector*, Phys. Lett. B 865 (2025) 139472, https://doi.org/10.1016/j.physletb.2025.139472 ; https://arxiv.org/abs/2410.16781
- Official numerical results: HEPData record 145171, Table 15 (observed 95% CL limit in SR2), https://www.hepdata.net/record/145171
- LHC Higgs Cross Section Working Group, 13 TeV SM Higgs production cross sections, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/HiggsXSBR
- ATLAS Collaboration, ATLAS-CONF-2025-006, https://cds.cern.ch/record/2937634/files/ATLAS-CONF-2025-006.pdf

- ATLAS Collaboration, *Search for Higgs bosons decaying into new spin-0 or spin-1 particles in four-lepton final states*, JHEP 03 (2022) 041, https://arxiv.org/abs/2110.13673
- CMS Collaboration, *Search for low-mass dilepton resonances in Higgs boson decays to four-lepton final states*, Eur. Phys. J. C 82 (2022) 290, https://arxiv.org/abs/2111.01299
