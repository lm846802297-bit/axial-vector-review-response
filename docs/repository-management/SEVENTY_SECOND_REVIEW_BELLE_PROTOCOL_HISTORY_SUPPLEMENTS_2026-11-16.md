# Seventy-second review: Belle II protocol, historical scan and supplement records

Review date: 2026-11-16  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head: `9b7fe54baf240c70d24660e16275adff81203722`  
Scope: three later-added repository-management review reports marked `PENDING` in the supplemental document register.

This is a document-level review. It checks the report dispositions against the current evidence ledger, recast protocol, historical scan notes and raw Belle II supplement tables. It does not re-download experimental data, rerun the 73,728-point width scan, or perform a detector-level analysis.

## Individual dispositions

| Document | Outcome | Review findings and disposition |
|---|---|---|
| `TWENTY_SEVENTH_REVIEW_BELLE_PROTOCOLS_2026-11-15.md` | `PASS_WITH_NOTES` | The current `evidence-ledger.md` explicitly labels its 2026-10-28 evidence state as historical and links the later supplement audit and bounded recast; the old statement that mass-dependent Belle rows were not yet extracted is therefore not presented as current. The `recast-protocol.md` correctly fixes the original one-VEV model identities, requires the full open-channel width and lifetime calculation, separates prompt published-limit reinterpretation from displaced acceptance, and says that a procedural protocol is not evidence that all gates have passed. E4 detector-level validation remains open. |
| `TWENTY_SIXTH_REVIEW_BELLE_HISTORY_2026-11-15.md` | `HISTORICAL` | The three reviewed 2026-11-05 documents carry explicit historical/superseded banners. The early implementation note predates the bounded double-virtual calculation; the earlier width audit is superseded by the later scan provenance and corrected width/resolution endpoint ordering; and the 1,852-point narrow/prompt classification is explicitly superseded by the bounded-width procedure. Their original equations and numbers are retained for traceability, not as current limits. The twenty-sixth report is therefore a historical review snapshot. |
| `TWENTY_THIRD_REVIEW_BELLE_SUPPLEMENTS_2026-11-15.md` | `PASS_WITH_NOTES` | The four-muon supplement has 2,317 data rows, strictly increasing mass values, no duplicate masses, and no points in the 3.07–3.12 GeV J/ψ interval. The tau-pair `limits.txt` and `limits.csv` are byte-identical in the current Git tree and contain 2,384 data rows; the three repeated masses (7.73369, 8.06147 and 9.53960 GeV) are exact full-row duplicates. The source-data audit retains the 2,317-versus-2,315 four-muon fit-count discrepancy and explicitly avoids silently deleting rows. The original source files remain unchanged. The SHA-256 strings recorded by the prior audit were not independently recomputed in this meta-review. |

## Cross-cutting conclusions

1. The source tables are archived and structurally usable, but the 2,317-row four-muon supplement versus 2,315 published fits remains unresolved.
2. The tau-pair `limits.txt` and `limits.csv` are one byte-identical dataset, not two independent measurements; the three duplicate rows are retained in the raw source.
3. The 2026-11-05 width-scan and 1,852-point classification records are historical. The later 73,728-point bounded-width scan and 2,746 conditional four-muon classifications are the current archived pointwise result; they remain a published narrow/prompt benchmark reinterpretation, not a detector-level CLs result.
4. The recast protocol is a set of requirements, not evidence that every requirement has been satisfied. Finite-width and lifetime-sensitive points remain unclassified, and detector-level E4 validation remains open.

## Execution boundary

- Three review reports were read in full.
- The evidence ledger, recast protocol, source-data audit, historical scan notes, four-muon raw supplement and tau-pair TXT/CSV tables were inspected.
- Raw-table row counts, mass ordering, duplicate rows and TXT/CSV identity were checked from the committed files.
- No raw source file, production width scan, detector response, likelihood, exclusion classification, manuscript source or physical constraint was changed.
- No GitHub Actions workflow was triggered.

The next supplemental batch should cover the remaining workflow-review reports, followed by the outstanding README, manifest and calculation-log records.
