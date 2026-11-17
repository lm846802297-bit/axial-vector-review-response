# Seventy-fifth review: baseline archive classification and revision-queue reduction

Review date: 2026-11-17  
Reviewed branch at start of this follow-up: `6aa4fa38d48d2613c6334b4dfa1a3d114c1d92b7`  
Scope: three baseline entries still marked `REVISION_REQUIRED` whose current repository context establishes that they are intentionally retained historical artifacts, not current authoritative deliverables.

This review changes lifecycle classification only. It does not claim that the archived technical content is free of the issues recorded in earlier reviews, and it does not modify any scientific calculation or manuscript conclusion.

## Individual dispositions

| Baseline document | Previous status | New status | Reason |
|---|---|---|---|
| `research/major1-higgs-scalar-mixing-20261109/independent_fermion_sector_audit_snapshot_20261113/SHA256SUMS.txt` | `REVISION_REQUIRED` | `HISTORICAL` | The snapshot README explicitly identifies this original manifest as historical evidence and warns that its README entry is not a current integrity assertion. The separate `SHA256SUMS_CURRENT_2026-11-14.txt` was independently checked against exact Git bytes in this review: all 7/7 entries match. The original manifest is preserved unchanged; the current sidecar is the only manifest to use for present snapshot integrity. |
| `work/v57_reconstructed_1007_final.md` | `REVISION_REQUIRED` | `HISTORICAL` | `work/README.md` explicitly identifies `work/` as the 2026-10-20 v5.7 historical workspace, not the current task state or formal referee response. The final variant differs from the original reconstruction only by correction of one duplicated word. The known notation, cross-reference, absorptive-threshold, two-pole momentum-dependence and provenance issues remain documented in the sixty-fifth review; they are retained as historical limitations, not silently declared fixed. |
| `work/v57_reconstructed_1007_fixed.md` | `REVISION_REQUIRED` | `HISTORICAL` | The fixed variant differs from the final variant by one whitespace character only and contains no additional physics repair. It is retained as a historical variant, not a canonical or accepted technical reference. The work README now links directly to the sixty-fifth review for its known unresolved issues. |

## Cross-checks

1. The current fermion-sector snapshot sidecar has seven entries. Each referenced Git file was fetched as base64 and its SHA-256 recomputed over the exact bytes; all seven match. This verifies the current snapshot files only and does not rehabilitate the mismatched historical manifest.
2. The work README states that the v5.7 files are historical, warns that `final` is only a filename from that time, and identifies the current technical reference elsewhere in the repository.
3. The sixty-fifth review confirms that the `final` and `fixed` files are both 5,666 lines; `final` differs from the original only at the duplicated-text correction, while `fixed` differs from `final` by one whitespace character. It also records the still-open physics/document issues.
4. The work README was updated with a direct link to the sixty-fifth review. No archived v5.7 file was deleted or rewritten.

## Resulting baseline status

The 462-document baseline now has:

- 296 `PASS_WITH_NOTES`
- 2 `PASS`
- 156 `HISTORICAL`
- 8 `REVISION_REQUIRED`
- 0 `PENDING`

The three reclassifications do **not** close their underlying scientific questions. They only prevent obsolete, explicitly historical artifacts from being treated as active deliverables. The remaining eight baseline `REVISION_REQUIRED` entries retain their substantive action items.

## Execution boundary

- No production Python calculation, numerical integration, transport scan, detector recast, or GitHub Actions workflow was run.
- No manuscript source, referee response, production rate, opacity, luminosity, constraint curve, or model parameter was changed.
- The only content edit outside the audit registers was a navigation/scope clarification in `work/README.md`.
- The supplemental-document review queue remains closed; this report is added as supplemental item 118.

The next baseline review should prioritize the still-current reproducibility gaps in the B.16 escape phase-space runbook and the missing artifact package for the 10 MeV local-rate/polarization/escape audit, without changing the published Fig. 7 or axial-vector constraint.
