# Seventy-first review: Belle II, profile provenance and pole/RGE review records

Review date: 2026-11-16  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head: `aa252dbbb5ef3f72fcdf6b3ee238554092f8acaf`  
Scope: six later-added repository-management review reports currently marked `PENDING` in the supplemental document register.

This is a document-level review of six prior review records. It checks the claims against the referenced committed notes, summary JSON/CSV artifacts, test log, and later superseding audit records. It does not rerun production calculations, detector fits, stellar transport, or pole integrals.

## Individual dispositions

| Document | Outcome | Review findings and disposition |
|---|---|---|
| `TWENTY_EIGHTH_REVIEW_BELLE_MAPPING_2026-11-15.md` | `PASS_WITH_NOTES` | The reviewed benchmark-mapping note explicitly identifies the original one-VEV S+VLL model, keeps the Belle scalar and vector signal hypotheses separate, and does not turn the published scalar-specific coupling limits into a detector-level UV exclusion. Its threshold-dependent tau branching fractions and the possible s → A'A' dilution are clearly distinguished from a full width/acceptance calculation. The 2,317-row four-muon supplement versus 2,315 published fits remains unresolved and is correctly retained rather than silently repaired. |
| `TWENTY_FIFTH_REVIEW_BELLE_RECAST_2026-11-15.md` | `PASS_WITH_NOTES` | The bounded-width summary JSON independently confirms the report's classification totals: 70,656 four-muon rows and 19,968 tau-pair rows, from a 73,728-point width scan. The two recast CSVs and summary are present. The report correctly distinguishes conditional narrow/prompt pointwise classifications from a new Belle II CLs result; finite-width and lifetime-sensitive points remain unclassified. The original 2,317-versus-2,315 four-muon table discrepancy remains visible. |
| `TWENTY_FIRST_REVIEW_PROFILE_PROVENANCE_2026-11-15.md` | `PASS_WITH_NOTES` | The uncompressed Caputo PDF-vertex payload exists in `audit_provenance/`. It has 731 data rows plus a header, with path-index counts 158:245, 159:186, 160:198 and 161:102. The off-frame thermodynamic JSON records 45 temperature and 48 muon-chemical-potential vertices in 20–22 km, consistent with the report. The B.2 interpolation JSON retains failed coarse-grid pairs and passing 240→320 and finer pairs; the report does not misstate the coarse-grid result as converged. This meta-review checked file presence and row counts, not the payload's SHA-256 or any new luminosity integration. |
| `TWENTY_FOURTH_REVIEW_BELLE_METHOD_2026-11-15.md` | `PASS_WITH_NOTES` | The detector-response input audit correctly separates what is available for the narrow/prompt mapping from what is missing for a validated finite-width or displaced reinterpretation. In particular, the published scalar-specific limits already fold in prompt scalar selection efficiency; the full Crystal-Ball response parameters, event-level response kernel and lifetime-dependent efficiency map are not supplied by the inspected public inputs. The report correctly leaves finite-width and lifetime-sensitive points unclassified. |
| `TWENTY_NINTH_REVIEW_POLE_AND_RGE_OUTPUTS_2026-11-15.md` | `HISTORICAL` | Its 2026-11-15 `REVISION_REQUIRED` dispositions for the exact-momentum pole driver and dependent CMS cascade were correct for the evidence then available. They were superseded on 2026-11-16 by the thirtieth pole-research follow-up and the independent endpoint-quadrature audit: composite Gauss–Legendre and mpmath tanh-sinh checks close the numerical warning for the declared two-benchmark/six-pole-pair fermion-sector grid. The later audit still records three SHA-256 provenance mismatches, no dedicated Actions acceptance for the five-test module, and substantial missing gauge/EFT/physical-width sectors. Preserve the twenty-ninth report as a dated history; do not use its old warning status as the current numerical-integration status or overstate the later result as a gauge-complete physical pole. |
| `TWENTY_SECOND_REVIEW_BELLE_SCAN_LOGS_2026-11-15.md` | `PASS_WITH_NOTES` | The stored `unit-tests.txt` contains 69 successful test cases and ends with `Ran 69 tests in 10.599s` / `OK`. The scan README confirms that the 73,728-row width scan is stored compressed, with 80,770,035 uncompressed bytes; the directly usable expanded CSV is not committed. It also distinguishes the current archive from the earlier 58-test run and different source/hash snapshot. The review report correctly treats the log as a historical local run, not a new scan execution or physical validation. The uncompressed scan-file handoff remains open. |

## Cross-cutting conclusions

1. Five reports remain valid scoped review records and are classified `PASS_WITH_NOTES`; the twenty-ninth report is classified `HISTORICAL` because its numerical warning status was superseded by a later independent audit.
2. The Belle II pointwise recast remains conditional on the published narrow/prompt scalar benchmark. It is not a new detector-level likelihood or CLs analysis.
3. The 2,317-versus-2,315 four-muon supplement/fit-count discrepancy remains unresolved and must stay visible.
4. The Caputo vertex payload and B.2 interpolation records support provenance and interpolation diagnostics; they do not by themselves validate a new SN luminosity or transport result.
5. The pole-quadrature warning is numerically closed only for the declared fermion-sector benchmark/grid. Gauge/Goldstone/ghost completion, full diagonal self-energies and counterterms, complete EFT matching, mixing-induced SM widths, and detector-level coherent likelihood remain outside that result.
6. The compressed 73,728-row width scan has not yet been committed as a directly usable uncompressed CSV; the repository README explicitly records this handoff limitation.

## Execution boundary

- Six review reports were read in full.
- The Belle II benchmark/response notes, bounded-width summary JSON, Caputo vertex CSV, off-frame thermodynamic JSON, B.2 interpolation JSON, pole follow-up, independent pole-quadrature audit, and Belle scan test log were inspected.
- No production collider, stellar-cooling, or pole calculation was rerun.
- No GitHub Actions workflow was triggered.
- No source physics code, numerical output, manuscript text, exclusion classification, or physical constraint was changed.

The next review batch should cover the remaining Belle II protocol/history/supplement records, then the workflow-review reports and outstanding README/manifest documents.

## Post-review register and tree consistency check (2026-11-16)

A recursive Git-tree comparison was performed at branch head `337b09e87c32fac075c05226b3875ceee1e51a77` after the document-status updates:

- The live tree contains 477 Markdown and 99 text files (576 total).
- All 462 baseline-register rows have current blob SHA and byte-size fields matching the Git tree (462/462).
- All 114 supplemental-register rows have blob SHA and byte-size fields matching the Git tree (114/114).
- Supplemental outcomes are 80 `PASS_WITH_NOTES`, 4 `HISTORICAL`, 29 `PENDING`, and 1 `REVISION_REQUIRED`.
- One stale supplemental size entry for the sixty-ninth review was corrected from 22,690 to 23,036 bytes; its blob SHA was already correct.
- Four live fingerprints in the baseline register were refreshed for the two extracted deliverable packages' provenance notes and current checksum manifests. Their original reviewed `blob_sha` and `size_bytes` values were preserved; their `fingerprint_status` remains `CONTENT_FINGERPRINT_DIFFERS`.

This is a metadata reconciliation only. It changes no source physics, archived numerical output, manuscript equation, or physical conclusion.
