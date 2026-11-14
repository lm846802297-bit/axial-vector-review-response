# Individual review: Belle II supplement data and audit

Baseline `d3980bf511a995ec2b54a1ca1f691e09227ca63f`, 2026-11-15. Three records were examined individually. Local text tables were fully parsed with NumPy 2.3.5; hashes, dimensions, finite entries, mass grids and duplicate rows were checked. This review did not re-download the experimental supplements, independently compare every interpretation against the publications or conduct a detector-level analysis.

| Document/data path under `research/radial-scalar-collider-recast-2026-10-28/` | Individual findings and disposition |
|---|---|
| `data/raw/belleii/four-muon/S_supplemental.txt` | Numeric table parses as 2317×15 finite values; mass is strictly increasing from 0.212 to 8.999862 GeV with no points in the quoted J/psi gap. SHA-256 `ef12682be45c07263ed9b27be7c988b34cb152267da6d933121d448f5658fec2` agrees with the existing audit. The 2317-versus-2315 fit-count discrepancy remains unresolved; raw data retained unchanged. PASS_WITH_NOTES. |
| `data/raw/belleii/tau-pair/limits.txt` | 2384×27 finite numeric values, 3.6–9.99943 GeV; three duplicate masses (7.73369, 8.06147, 9.53960 GeV) are full-row duplicates. It is byte-identical to the retained `limits.csv` with SHA-256 `ee968c65096393129d03b018493ddb721072b2a1c048609003c3918259fe7cfb`; not an independent dataset. Original rows remain intact. PASS_WITH_NOTES. |
| `source-data-audit-2026-11-05.md` | The source hashes, counts, ranges, gap and duplicate statements were checked against local files. The conditional UV mapping and detector-efficiency limitations are explicitly stated; no claim of an independent event-level reanalysis is made here. Added a stage note that later pointwise width scans exist, without claiming complete exclusion. The stated historical paper text/figure comparisons were not freshly rederived in this review. PASS_WITH_NOTES. |

The prior 69-test rerun checks selected software properties but does not substitute for the missing detector response and likelihood. The source-table fit-count discrepancy remains open.
