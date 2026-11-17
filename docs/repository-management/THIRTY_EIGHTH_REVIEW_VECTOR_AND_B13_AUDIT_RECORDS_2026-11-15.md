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


## Independent current-tree follow-up (2026-11-16)

**Disposition of this review batch: PASS_WITH_NOTES.** The six source documents and their linked local targets were checked against the current maintenance tree. Their original dispositions remain appropriate: the rescaling audit and package index are PASS_WITH_NOTES; the six-mass vector benchmark, the two profile-specific local B.13 records, and the log-recovered global convergence record remain HISTORICAL. No production calculation was rerun.

### 1. Coupling-axis rescaling: exact historical input pin

The six methods in rescaling_audit/test_rescaling.py are present, and the archived JSON reproduces the values quoted in the 2026-11-07 report: \(\kappa_{10}=1.06675\), global \(\kappa=1.03\), 10-MeV mean/max absolute relative residuals 15.6446%/91.3484%, and mass-specific Fig. 4 boundary shifts −5.9453%/−5.3519%.

A raw-byte SHA-256 check establishes that the three input hashes stored in rescaling_audit/outputs/rescaling_audit.json match the input JSON files at commit b3af69de1b37e2efc9f590e40e03a4ca85434420, the head of Actions run #42302956969. The recorded run.py hash also matches that commit. This pins the archived rescaling result to that historical input set.

The current maintenance tree has subsequently updated all three input JSONs. In particular, the archived result carries the earlier profile-A fingerprint 08d7afce..., whereas the current 1687-row vertex-preserving profile is 9fb14e79...; the literal scan, Fig. 4/7 comparison, and vector luminosity-comparison JSONs also contain later numerical/structural changes. The archived output is therefore **not** a rescaling fit on the current profile-B inputs. The rescaling README now records the exact historical commit and warns that the default script output path would overwrite the archived result; current-input reruns must use a distinct output filename.

This does not change the original interpretation: \(\kappa\) is a diagnostic fit, not a production coupling redefinition. No fitted value is applied to the production scan or constraint curve.

### 2. Collaborator package source-root accounting

The package builder has five SOURCE_ROOTS entries: four primary physics/model roots plus research/stellar-cooling-shared-20261105/, which supplies shared thermal adapters and common support code. The package index previously described only the four primary roots. It now explicitly lists the shared support root and distinguishes it from a separate UV model line. The builder and validation-only workflow remain present; the workflow has no ZIP build or artifact-upload step, and the builder metadata records garching_raw_profile_included: false. The file catalog is intentionally generated inside the local ZIP rather than tracked as a standalone CSV.

### 3. B.13 local radial records: profile identity and point counts

Both local radial JSONs contain 42 points: seven radii (8, 10, 12.5, 15, 18.5, 20, 22 km) by six local energies (12, 15, 20, 30, 50, 80 MeV). The 24 inner-region points are the first four radii, 8–15 km.

- The historical 501-node uniform-profile output is pinned to 08d7afce...; its raw profile is not present in the current tree, so that result remains a historical profile-specific diagnostic.
- The vertex-preserving output is pinned to 9fb14e79.... The current data/sfho188_digitized.csv contains 1687 data rows (plus its header), matching the recorded current-profile variant.
- For the 1687-row result, the maximum mode detailed-balance residual is \(3.05\times10^{-15}\), and the maximum final-muon shell residual is \(1.42\times10^{-13}\). Across the 24 inner points, the B.13 mu-minus production rate is 0.375–0.723 times the B.16 reference; the B.13 change in total local opacity ranges from −24.28% to −0.0622%.

These are local-kernel and local-opacity statements. They do not determine the full escaped luminosity; source and absorption must be updated consistently in a global B.2 calculation.

### 4. Global angular/path convergence: compact log record only

Actions run #42542328275 records numerical_scan_step: success and structural_validation_step: success, but artifact_upload_step: failure; the original full JSON arrays were not archived. The log-recovered summary reports zero same-grid B.16 closure residuals and a maximum luminosity shift of 0.273191% on the combined \(60\times140\times24\times48\) grid. The combined-grid Fig. 7 strong-endpoint residual remains approximately +131.1% for the mu-minus-consistent variant. Thus the grid is numerically stable at the stated project targets, but the literature reproduction gate remains unpassed. The compact summary is not a substitute for the missing full arrays or an independent physical validation.

PR #56, PR #106, and PR #113 are confirmed merged. Their later integration does not retroactively turn the 2026-11-07/09 records into current production inputs or a final SN1987A exclusion.

**Boundary:** all findings above concern document integrity, archived diagnostics, input provenance, and stated local/global validation scope. No production B.13 kernel, B.2 opacity, luminosity curve, axial scan, SN1987A limit, or axial-vector exclusion curve was modified.
