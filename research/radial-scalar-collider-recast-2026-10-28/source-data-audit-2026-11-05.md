# Belle II numerical supplement audit and scalar-benchmark reconstruction

**Record date:** 2026-11-05  
**Branch:** research/radial-scalar-original-model-belleii-20261105  
**Model scope:** the original paper's one-VEV radial scalar and original VLL sector only.  
**Status:** official source files archived verbatim; published scalar benchmark curves reconstructed from the numerical tables; conditional UV/perturbativity overlay completed. No detector-level reanalysis or complete UV exclusion is claimed.

## 1. Official raw files retrieved and archived

The three files supplied for this pass were read locally, hashed, and committed to this PR branch. The Git blob SHA-1 returned after fetching each archived path matches the Git blob SHA-1 computed from the original downloaded bytes. The source files are therefore preserved byte-for-byte, including their original line endings and trailing newlines.

| Analysis | Official file | Bytes | Data rows | Columns | Mass range (GeV) | SHA-256 |
|---|---|---:|---:|---:|---:|---|
| Four-muon scalar | S_supplemental.txt | 317,888 | 2,317 | 15 | 0.212–8.999862 | ef12682b…f5658fec2 |
| Tau-pair scalar | limits.csv | 821,015 | 2,384 | 27 | 3.600–9.99943 | ee968c65…59fe7cfb |
| Tau-pair scalar | limits.txt | 821,015 | 2,384 | 27 | 3.600–9.99943 | ee968c65…59fe7cfb |

Archive paths:

- data/raw/belleii/four-muon/S_supplemental.txt
- data/raw/belleii/tau-pair/limits.csv
- data/raw/belleii/tau-pair/limits.txt

The tau-pair CSV and TXT files are byte-identical. Both official filenames are retained for provenance, but they are one numerical dataset, not two independent measurements. Exact hashes and Git blob hashes are recorded in the data manifest.

## 2. Structural and numerical checks

### 2.1 Four-muon supplement

- All 2,317 rows parse into 15 finite numerical columns.
- The mass grid is strictly increasing and has no duplicate mass values.
- No row lies in the \(3.07\text{--}3.12\,\mathrm{GeV}\) interval around the \(J/\psi\) exclusion window; the adjacent mass points are 3.069131 and 3.121821 GeV.
- All five expected quantiles are ordered correctly for both the cross-section and \(g_S\) limits.
- The six published cross-section/\(g_S\) limit pairs obey the expected quadratic normalization \(\sigma_{\rm UL}(m_S)\propto g_{S,\rm UL}^2(m_S)\). The relative spread among the six independently inferred per-mass normalizations has median \(1.31\times10^{-4}\) and maximum \(9.78\times10^{-4}\).
- The signed best-fit central values give a second consistency check: the median relative residual against the same per-mass normalization is \(5.28\times10^{-5}\), and the 99th percentile is \(7.81\times10^{-4}\). Three rows have central values rounded to zero, so those rows are excluded from this central-fit check; their published upper limits remain finite and are retained.

**Source discrepancy:** the supplement contains 2,317 mass rows, whereas the paper text reports 2,315 fits. The supplement has no duplicated mass points, and no evidence has been found to identify two rows that should be removed. The raw table is preserved unchanged; the two-row discrepancy remains open rather than being silently corrected.

The observed \(g_S\) limit ranges from 0.001818 to 0.479759 over the full mass interval. Below 6 GeV, the observed range is 0.001818–0.040342, consistent with the paper's quoted approximate range 0.0018–0.040. The observed cross-section limits range from 0.055977 to 1.275175 fb, consistent with the paper's quoted approximate range 0.055–1.3 fb.

### 2.2 Tau-pair supplement

- The CSV parses into 2,384 rows and 27 finite numerical columns.
- The mass range is 3.600–9.99943 GeV.
- The 90% CL observed limits and all expected quantile bands are present; expected bands are correctly ordered for the cross-section, \(g'\), scalar \(\xi\), and ALP-coupling columns.
- The file contains three exact duplicate mass rows: 7.73369, 8.06147, and 9.53960 GeV. In each case, the entire numerical row is identical. The raw file remains untouched. Duplicate rows are removed only for plotting and unique-mass summaries.
- The 2,384 raw rows match the paper's stated 2,384 fits; the three duplicate rows are nevertheless flagged as a source-table feature.

The observed scalar-coupling limits \(\xi_{\rm UL}^{\rm obs}\) range from 53.5592 at 4.29355 GeV to 2,944.70 at 9.69438 GeV. The expected median ranges from 75.2296 at 3.87196 GeV to 1,803.36 at 9.91859 GeV. The observed cross-section limits range from 0.692016 to 24.2138 fb, consistent with the paper's approximate 0.7–24 fb summary.

**Normalization rule:** use the published xi_UL columns directly for the leptophilic-scalar benchmark. Do not infer the scalar \(\xi\) curve from the cross-section columns alone. The analysis applies its full selection to separate scalar samples and reports scalar/vector efficiency differences of 10–20%; a vector-reference normalization is not a substitute for the scalar-specific result.

## 3. Published benchmark curves reconstructed

Two numerical curves were reconstructed directly from the official supplemental columns:

1. **Four-muon scalar benchmark:** observed 90% CL \(g_S\) limit, expected median, and expected \(\pm1\sigma\)/\(\pm2\sigma\) bands from S_supplemental.txt. The six-quantile quadratic-normalization check above validates the internal cross-section-to-coupling conversion.
2. **Tau-pair leptophilic-scalar benchmark:** observed 90% CL \(\xi\) limit, expected median, and expected \(\pm1\sigma\)/\(\pm2\sigma\) bands from the xi_UL columns of limits.csv. The three exact duplicate rows are removed only in the plotting copy.

The parser, structural checks, coupling-normalization checks, conditional perturbativity overlay, and plot generation are implemented in [audit_belleii_supplements.py](audit_belleii_supplements.py). From this directory, run `python audit_belleii_supplements.py --data-dir data/raw/belleii --output-json data/derived/audit-summary.json --plots-dir data/derived/figures` to regenerate the numerical audit and both plots. This command was executed locally under Python 3.13.5 and returned exit code 0; no GitHub Actions/CI run is claimed. The resulting plots reproduce the shapes and mass dependence of the published scalar panels (four-muon Fig. 14 and tau-pair Fig. 4). This is **table-driven benchmark-curve reconstruction**. It is not a new Belle II analysis: no event samples, detector response, signal efficiency, likelihood fit, or \(CL_s\) procedure has been rerun.

## 4. Conditional mapping to the original one-VEV UV model

The original UV relations are
\[
v_s=\frac{m_{A'}}{2g_X},\qquad
y_{s\mu\mu}=\frac{m_\mu}{v_s},\qquad
y_{s\tau\tau}=\frac{m_\tau}{v_s},\qquad
\xi_{\rm UV}=\frac{v}{v_s}.
\]
For the adopted perturbativity criterion \(\lambda_S\leq4\pi\), with \(m_s^2=2\lambda_Sv_s^2\),
\[
\xi_{\rm UV}\leq\frac{\sqrt{8\pi}\,v}{m_s},
\qquad
y_{s\mu\mu}\leq\frac{\sqrt{8\pi}\,m_\mu}{m_s}.
\]

A first pointwise comparison was made under all of the following restrictive assumptions:

- \(s\to A'A'\) is closed;
- portal-mediated and other additional widths are negligible;
- the scalar remains prompt and narrow;
- the Belle II scalar-specific efficiency is applicable without modification;
- the original mass-proportional \(\mu,\tau\) Yukawas are used.

Under these assumptions:

### Four-muon channel

Above \(2m_\tau\), the original UV scalar has a \(\tau^+\tau^-\) decay mode, unlike the muonphilic benchmark. The UV dimuon branching fraction falls from approximately 0.451 at 3.60 GeV to 0.0349 at 4.00 GeV and 0.0100 at 5.00 GeV. The coupling-limit translation is therefore
\[
g_{S,\rm lim}^{\rm UV}
=
g_{S,\rm lim}^{\rm Belle}
\frac{1}{\sqrt{\mathrm{BR}_{\mu\mu}^{\rm UV}}}
\]
in the closed-\(A'A'\), two-lepton approximation.

After this branching-fraction correction, the observed pointwise limit remains below the \(\lambda_S\leq4\pi\) perturbativity envelope through the last grid point at 4.997842 GeV; the expected median remains below it through 4.552977 GeV. These are grid-level crossings of fluctuating curves, not sharp or universal mass boundaries.

### Tau-pair channel

For the mass-proportional scalar benchmark, the original UV \(\mu,\tau\) branching fraction is nearly the same as Belle II's benchmark branching fraction. The difference caused by the benchmark's additional electron Yukawa is at most \(1.09\times10^{-5}\) in relative terms over the supplied mass grid. With \(A'A'\) closed, the \(\xi\) normalization therefore maps almost directly:
\[
\xi_{\rm UV,lim}
=
\xi_{\rm lim}^{\rm Belle}
\sqrt{\frac{\mathrm{BR}_{\tau\tau}^{\rm Belle}}
{\mathrm{BR}_{\tau\tau}^{\rm UV}}}
\simeq\xi_{\rm lim}^{\rm Belle}.
\]

The expected median remains below the \(\lambda_S\leq4\pi\) perturbativity envelope through 6.11868 GeV. The observed curve has local statistical fluctuations; its last grid point below the envelope is 6.44291 GeV. Again, this is not a hard mass cutoff.

### Limitation of this overlay

The results above are conditional. If \(m_s>2m_{A'}\), the \(s\to A'A'\) channel opens and can dominate, reducing both direct \(\mu\mu\) and \(\tau\tau\) branching fractions. Portal-induced widths can also alter branching fractions and lifetime. Those effects must be included point by point before classifying any UV parameter point. No global allowed scalar-mass interval follows from this overlay.

## 5. What has and has not been established

**Established in this pass**

- The three official supplements are downloaded and archived byte-for-byte.
- Exact source hashes, byte counts, row counts, and archive paths are recorded.
- The published four-muon \(g_S\) and tau-pair \(\xi\) benchmark curves are reconstructed from the numerical tables.
- Expected-band ordering and the four-muon quadratic coupling normalization are checked.
- The two source-table count/duplicate issues are explicitly recorded.
- A conditional original-UV/perturbativity overlay is calculated with its assumptions stated.

**Not established**

- No detector-level efficiency or acceptance recalculation has been performed.
- No event-level likelihood or \(CL_s\) calculation has been rerun.
- The four-muon 2-row count discrepancy is unresolved.
- No point-by-point \(s\to A'A'\) opening-channel scan has been completed.
- Portal-induced widths and all possible UV decay modes have not been included.
- No complete lifetime/promptness map or full UV-model collider exclusion has been produced.
- No model-independent or universal allowed interval in \(m_s\) is claimed.

## 6. Next work

1. Use the existing radial-scalar width calculator to scan \((m_s,m_{A'},g_X)\), including \(s\to A'A'\), and calculate complete branching fractions only after all relevant open channels are accounted for.
2. Check the prompt/narrow-width assumption against the total UV width at each benchmark.
3. Map the two Belle II analyses independently, using their own scalar benchmark curves and final states.
4. Keep this follow-up separate from the formal Major Point 1 referee response. No response-letter edit is authorized by this research result alone.

## Sources

- Four-muon search: I. Adachi et al. (Belle II), Phys. Rev. D **109**, 112015 (2024), [arXiv:2403.02841](https://arxiv.org/abs/2403.02841), [DOI: 10.1103/PhysRevD.109.112015](https://doi.org/10.1103/PhysRevD.109.112015).
- Four-muon official supplement: https://journals.aps.org/prd/supplemental/10.1103/PhysRevD.109.112015/S_supplemental.txt
- Tau-pair search: I. Adachi et al. (Belle II), Phys. Rev. Lett. **131**, 121802 (2023), [arXiv:2306.12294](https://arxiv.org/abs/2306.12294), [DOI: 10.1103/PhysRevLett.131.121802](https://doi.org/10.1103/PhysRevLett.131.121802).
- Tau-pair official supplements: https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802/limits.csv and https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802/limits.txt
