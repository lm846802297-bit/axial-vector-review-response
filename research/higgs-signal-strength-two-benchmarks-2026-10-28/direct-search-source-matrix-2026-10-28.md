# Direct-search source matrix — two UV benchmarks

**Date:** 2026-10-28  
**Branch:** research/higgs-signal-strength-two-benchmarks-2026-10-28  
**Status:** source applicability audit and conservative rate screening; not a detector-level recast.

## Executive result

A directly relevant published search has been identified: ATLAS HDBS-2021-13, *Search for a new scalar decaying into new spin-1 bosons in four-lepton final states with the ATLAS detector*, Phys. Lett. B 865 (2025) 139472, DOI 10.1016/j.physletb.2025.139472; arXiv:2410.16781.

The analysis searches for a prompt scalar \(S\to Z_dZ_d\to4\ell\), with \(\ell=e,\mu\), over \(30<m_S<115\) GeV and \(130<m_S<800\) GeV, with \(15<m_{Z_d}<300\) GeV. It reports 95% CL upper limits on \(\sigma(gg\to S)\,\mathrm{BR}(S\to Z_dZ_d\to4\ell)\) ranging from 0.14–3.1 fb in the lower-mass region and 0.05–0.60 fb in the higher-mass region.

**Benchmark A (\(m_{A'}=10\) GeV):** this search is not directly applicable. The intermediate mass is below the analysis's generated \(m_{Z_d}\ge15\) GeV range, and the event selection requires every dilepton pairing to have invariant mass above 11.105 GeV. A prompt \(A'\to\ell^+\ell^-\) pair at 10 GeV fails that requirement. Do not extrapolate the published limit to this benchmark.

**Benchmark B (\(m_{A'}=63\) GeV):** for \(m_s<126\) GeV, the \(s\to A'A'\) channel is closed, so this particular topology is absent. For \(m_s\gtrsim130\) GeV, the on-shell cascade is open and the ATLAS search is a relevant source-level constraint. A conservative rate screen using the current non-degenerate self-energy proxy places the predicted rate far below the published limit scale. This is encouraging but remains an indicative comparison until the physical pole mixing and exact model branching fractions are validated.

## 1. Verified source details

- ATLAS Collaboration, HDBS-2021-13, arXiv:2410.16781; Phys. Lett. B 865 (2025) 139472.
- Official/preprint source: https://arxiv.org/abs/2410.16781
- Full text and event selection: https://escholarship.org/uc/item/9g9590fs
- DOI: https://doi.org/10.1016/j.physletb.2025.139472
- The analysis uses 139 fb\(^{-1}\) of \(pp\) data at \(\sqrt{s}=13\) TeV and requires prompt decays.
- The observable is the total scalar production cross section times the branching fraction into the selected four-lepton final state, not a universal bound on a scalar mixing angle.
- The analysis selects \(4e\), \(2e2\mu\), and \(4\mu\) candidates; every dilepton pairing must satisfy \(m_{\ell\ell}>11.105\) GeV. The higher-mass signal region also applies a \(Z\)-mass veto to the dilepton pairings.
- Published observed 95% CL limit ranges: 0.14–3.1 fb for the lower-mass region and 0.05–0.60 fb for the higher-mass region. These are overall ranges across the mass plane, not the exact limit at a specific \((m_s,m_{A'})\) point.

## 2. Benchmark-by-benchmark applicability

| Requirement | Benchmark A: \(m_{A'}=10\) GeV | Benchmark B: \(m_{A'}=63\) GeV |
|---|---|---|
| On-shell \(s\to A'A'\) near \(m_s=125.25\) GeV | Open | Closed because \(2m_{A'}=126\) GeV |
| ATLAS intermediate-vector mass range \(15\)–\(300\) GeV | **Fails** | Passes |
| ATLAS pair-mass requirement \(m_{\ell\ell}>11.105\) GeV | **Fails** for direct \(A'\to\ell\ell\) pairs at 10 GeV | Passes for 63 GeV pairs |
| Scalar mass region with on-shell \(A'A'\) and ATLAS coverage | \(m_s>20\) GeV kinematically, but this analysis fails the intermediate-mass/pair-mass cuts | \(m_s>126\) GeV; use the higher-mass signal region for \(m_s>130\) GeV |
| Promptness | Expected for the stated \(g_X\), but does not fix the mass-selection mismatch | Expected for the stated \(g_X=0.1\); see width estimate below |
| Four-lepton branching pattern | Not directly constrained by this analysis because the 10 GeV pair is rejected | Different from the HAHM dark-photon benchmark; compute \(A'\) branching fractions explicitly |
| Present classification from this source | **Not applicable; no exclusion inferred** | Relevant search identified; preliminary rate screen is far below the limit scale; no formal recast claimed |

## 3. Conservative non-degenerate rate screen for Benchmark B

Use the inherited matched self-energy \(\Pi_B=(-0.09300-0.02547i)\,\mathrm{GeV}^2\), \(m_h=125.25\) GeV, and \(m_s=130\) GeV only as a non-degenerate screening proxy:

\[
\epsilon_{\mathrm{nd}}
=\frac{|\Pi_B|}{|m_h^2-m_s^2|}
\simeq7.95\times10^{-5},
\qquad
\epsilon_{\mathrm{nd}}^2\simeq6.32\times10^{-9}.
\]

This is not a pole-scheme mixing angle. If the scalar is produced only through Higgs mixing, the isolated-state estimate is

\[
\sigma(gg\to s)\simeq \epsilon_{\mathrm{nd}}^2
\,\sigma_{\mathrm{ggF}}^{\mathrm{SM}}(m_s).
\]

For a conservative upper envelope, take \(\sigma_{\mathrm{ggF}}^{\mathrm{SM}}(130\,\mathrm{GeV})<50\) pb, consistent with the scale of the LHC Higgs Cross Section Working Group's 13 TeV recommendation. Then

\[
\sigma(gg\to s)\lesssim
6.32\times10^{-9}\times50\,\mathrm{pb}
=3.16\times10^{-4}\,\mathrm{fb}.
\]

This is an upper bound on the inclusive production estimate before multiplying by any branching fraction. Even setting \(\mathrm{BR}(s\to A'A'\to4\ell)=1\), it is below the smallest published high-mass limit value (0.05 fb) by a factor of about 160. The model's actual four-lepton branching fraction is less than one, so its predicted selected rate is smaller still.

At \(m_s=130\) GeV, the tree-level width from the inherited radial-scalar normalization is

\[
\Gamma(s\to A'A')=
\frac{m_s^3}{32\pi v_s^2}
\sqrt{1-\frac{4m_{A'}^2}{m_s^2}}
\left(1-\frac{4m_{A'}^2}{m_s^2}
+12\frac{m_{A'}^4}{m_s^4}\right)
\simeq 3.92\times10^{-2}\,\mathrm{GeV}.
\]

This is a prompt decay. For \(A'\) at 63 GeV with \(g_X=0.1\), the leading \(L_\mu-L_\tau\) partial widths to \(\mu^+\mu^-\), \(\tau^+\tau^-\), and the two active neutrino flavours give \(\mathrm{BR}(A'\to\mu^+\mu^-)\simeq1/3\), neglecting loop-induced electron couplings and any additional open states. Thus the direct \(4\mu\) branch alone is approximately

\[
\mathrm{BR}(s\to A'A'\to4\mu)
\simeq \mathrm{BR}(s\to A'A')\,[\mathrm{BR}(A'\to\mu^+\mu^-)]^2
\lesssim \frac{1}{9}.
\]

With this tree-level branching estimate, the selected \(4\mu\) rate is at most about \(3.5\times10^{-5}\) fb under the conservative 50 pb production envelope. This is about \(1.4\times10^3\) below the most sensitive published limit value of 0.05 fb. The exact \(4e\) and \(2e2\mu\) contributions require the model's loop-induced kinetic-mixing normalization and are not included here.

**Interpretation:** this is a robustly small *screening estimate* for the stated non-degenerate benchmark, not a formal exclusion test. The comparison uses the most sensitive value in the whole ATLAS mass plane rather than the exact point-specific limit, and the production rate still uses a proxy instead of a physical pole mixing angle. A final result should use the exact observed limit at \((m_s,m_{A'})\), a consistent pole prescription, and model-specific branching fractions.

## 4. Other constraints: what can and cannot be imported

### Higgs signal strength

ATLAS-CONF-2025-006 reports the global signal strength \(\mu=1.023^{+0.056}_{-0.053}\). This is useful for an approximate inclusive-rate sanity check, but it does not constrain the full scalar parameter space by itself. Benchmark A additionally has the \(h\to A'A'\) channel open through the singlet admixture, while Benchmark B has \(2m_{A'}>m_h\). Near \(m_s\simeq m_h\), a single-angle \(\mu\simeq\cos^2\theta\) treatment is invalid without a pole-consistent two-state calculation.

### Generic LEP singlet-scalar limits

Published LEP limits commonly assume SM-Higgs-like branching fractions or a specified visible/invisible final state. They are not automatically transferable to Benchmark A, where \(s\to A'A'\) is open throughout the 65–115 GeV region, or to Benchmark B without a point-specific branching-ratio calculation. A separate LEP reinterpretation would need the actual search observable and efficiencies for the relevant \(A'A'\) final states. No LEP exclusion is assigned here.

### Other LHC scalar searches

The ATLAS \(S\to Z_dZ_d\to4\ell\) analysis is the closest directly matched public search found for Benchmark B above threshold. Searches of the 125 GeV Higgs for \(H\to Z_dZ_d\) are not interchangeable with direct production of a separate \(s\) resonance: the parent mass, production rate, and signal selection differ. Generic heavy-scalar \(ZZ\) searches also do not directly match a pair of 63 GeV \(A'\) bosons with \(L_\mu-L_\tau\) branching fractions.

## 5. Evidence ledger and next actions

1. **Verified:** a relevant ATLAS direct-search analysis exists and publishes cross-section-times-four-lepton-branching-ratio limits.
2. **Verified:** Benchmark A fails the \(A'\) mass coverage and explicit dilepton-mass requirement of that analysis.
3. **Verified:** Benchmark B's on-shell cascade is closed below 126 GeV and open in the ATLAS high-mass signal region above 130 GeV.
4. **Preliminary analytic screen:** Benchmark B's non-degenerate mixing proxy makes the predicted \(gg\to s\to A'A'\to4\ell\) rate much smaller than the published limit scale, even before detailed acceptance corrections.
5. **Not yet done:** point-specific digitization/retrieval of the ATLAS limit at \(m_{A'}=63\) GeV; exact physical pole mixing; complete \(A'\) branching fractions including kinetic mixing; detector-level acceptance validation; a dedicated LEP recast for Benchmark A.
6. **Do not claim:** a complete UV-allowed scalar-mass interval or a global experimental exclusion.

## Sources

- ATLAS Collaboration, *Search for a new scalar decaying into new spin-1 bosons in four-lepton final states with the ATLAS detector*, Phys. Lett. B 865 (2025) 139472, https://doi.org/10.1016/j.physletb.2025.139472 ; https://arxiv.org/abs/2410.16781
- LHC Higgs Cross Section Working Group, 13 TeV SM Higgs production cross sections, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/HiggsXSBR
- ATLAS Collaboration, ATLAS-CONF-2025-006, https://cds.cern.ch/record/2937634/files/ATLAS-CONF-2025-006.pdf
