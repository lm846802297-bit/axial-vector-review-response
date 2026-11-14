# Individual review: vector benchmark and B.13 audit records

Review date: 2026-11-15. Baseline branch: maintenance/repository-organization-audit-20261114. This batch reviews the next six pending records in register order. It checks provenance, saved outputs, test assets and the boundary between local-kernel checks and global transport; no production scan was rerun.

| Document | Outcome | Findings and disposition |
|---|---|---|
| research/stellar-cooling-constraints-20261105/RESCALING_AUDIT_2026-11-07.md | PASS_WITH_NOTES | The post-processing fit is correctly isolated from rates, transport and luminosity integration. Its six-test module and archived JSON exist; the saved output reproduces the quoted mass-specific \(\kappa_{10}=1.06675\), global \(\kappa=1.03\), 10-MeV baseline mean/max residuals (15.64%/91.35%), and the Fig. 4 boundary degradation after mass-specific rescaling (-5.95%/-5.35%). The result correctly rejects a universal coupling-axis correction and explicitly forbids applying fitted \(\kappa\) to production scans. Dated PR #56 Draft wording was corrected to say it later merged. |
| research/stellar-cooling-constraints-20261105/REVIEW_PACKAGE_INDEX_2026-11-13.md | PASS_WITH_NOTES | The canonical four-root source layout, deduplication policy, local-only ZIP handoff, and exclusion of restricted Garching data are clear. The package README, bounded requirements file, builder and validation-only workflow exist. The catalog is generated inside the ZIP at 00_START_HERE/SOURCE_FILE_CATALOG.csv by build_archive.py; its absence as a standalone tracked file is intentional. The index remains a 2026-11-13 package snapshot, not a live scientific-status dashboard. |
| research/stellar-cooling-constraints-20261105/VECTOR_BENCHMARK_AUDIT_2026-11-07.md | HISTORICAL | This is a valuable six-mass Fig. 7/Fig. 4 and polarization-transport diagnostic. It correctly separates scalar-summed literal Appendix-B propagation from mode-resolved propagation and does not infer a factor-of-three correction from curve matching. The 10-MeV high-absorption residual remains about 92%, while 1 and 200 MeV full curves meet the provisional comparison tolerance. Corrected escaped inline-code delimiters and made PR #56's later merge explicit. PR #106/#113 later added B.2/B.13 work; the vector Fig. 7 gate remains unpassed. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_EXACT_COMPTON_RADIAL_OPACITY_AUDIT_2026-11-09.md | HISTORICAL | The local B.13/B.16 comparison uses the 501-node uniform profile and has its own charge-resolved JSON. The note explicitly warns not to mix these values with the separate 1687-row vertex-preserving rerun. Its physical conclusion is directionally important: B.13 lowers inner Compton opacity, which by itself increases escape probability and therefore cannot explain a discrepancy that requires smaller escape probability. Added a link-forward note to the later full-profile PR #113 work. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_EXACT_COMPTON_RADIAL_OPACITY_AUDIT_VERTEX_PRESERVING_2026-11-09.md | HISTORICAL | The 1687-row vertex-preserving profile fingerprint matches the stated current-profile variant; the paired output exists. The 24 sampled inner-region points show a non-negligible B.13/B.16 difference, with detailed-balance residuals below \(3.1\times10^{-15}\) and final-muon shell residual \(1.42\times10^{-13}\). The document correctly refuses to infer a global luminosity correction from local opacity alone and requires updating source and absorption together. PR #113 later carries the full-profile global B.13/B.2 work. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_GLOBAL_ANGULAR_PATH_CONVERGENCE_AUDIT_2026-11-09.md | HISTORICAL | The recovered run log reports a maximum 0.273191% luminosity shift on the combined \(60\times140\times24\times48\) grid and zero same-grid B.16 closure residuals. However, the original full JSON arrays were not archived because the Actions artifact upload failed; the file is explicitly a compact log-recovered summary. Its Fig. 7 B.13 strong-endpoint residual remains about +131.1%, so convergence is not reproduction. Added a historical notice linking later full-profile B.13/B.2 work in PR #113 and clarified that the old PR #57 status is a snapshot. |

## Cross-document conclusions

- A fitted coupling-axis shift is not a physically accepted correction: the mass-specific 10-MeV shift worsens the already-close Fig. 4 boundaries, and the global fit leaves a large Fig. 7 residual.
- The two B.13 radial reports are different profile versions. The 501-node uniform-profile values and the 1687-row vertex-preserving values must remain separate.
- Local B.13/B.16 opacity differences do not determine the escaped luminosity. Production and absorption must be replaced consistently before a global B.2 comparison is meaningful.
- The old angular/path convergence record is numerically converged on its tested grid but is not a complete data archive and does not pass the Fig. 7 reproduction gate.
- PR #56 merged on 2026-11-12; PR #113 later archived full-profile B.13/B.2 work. The historical documents retain their own dated results and limitations.

## Updated baseline register

The register remains 462 documents. After this batch:

- PASS: 2
- PASS_WITH_NOTES: 147
- HISTORICAL: 83
- REVISION_REQUIRED: 8
- PENDING: 222
- Individually reviewed: 240 / 462

No production rate, transport solver, opacity, coupling, scan, or constraint figure was modified or rerun. Changes are limited to historical-status notes, package-catalog clarification, escaped Markdown delimiters, and the individual-review register/report.
