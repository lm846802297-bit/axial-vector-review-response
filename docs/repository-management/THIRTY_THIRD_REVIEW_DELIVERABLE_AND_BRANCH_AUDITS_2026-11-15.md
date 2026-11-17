# Individual review: Higgs-portal handoff and branch audit records

Reviewed baseline: `maintenance/repository-organization-audit-20261114` at commit `c7e2c5b58389c7c9f2720703b29cba240cce907f`; review date: 2026-11-15. Follow-up documentation corrections are committed on the same maintenance branch.

This batch covers three baseline documents. The review is a repository/document-authority audit; it does not rederive the full Higgs-portal calculation or rerun physics calculations.

| Document | Outcome | Findings and disposition |
|---|---|---|
| `deliverables/higgs_portal_mixing_md_with_svg/higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8).md` | `HISTORICAL` | The file identifies itself as a 2026-10-18 consolidation of an earlier reviewer-response guide and staged UV–EFT calculation notes. It is 15,715 lines and approximately 485,025 characters, with sections through §187. Its front matter explicitly says it is not a final referee response, distinguishes candidate/conditional results from established results, and warns against promoting incomplete matching or phenomenological claims. The section numbering contains historical duplicate ranges (notably §§145–152), consistent with its append-only working-record nature. Its only local Markdown asset reference, `higgs_portal_mixing_feynman_diagrams.svg`, resolves to the SVG in the same directory. Preserve the document and SVG for provenance; do not treat this October snapshot as the current Major 1 calculation authority. No formula or numerical result was changed, and no full physics re-derivation is claimed. |
| `research/BRANCH_DISPOSITION_2026-11-13.md` | `PASS_WITH_NOTES` after correction | The tree/blob comparison method and branch-preservation decisions are useful and appropriately distinguish commit Ahead/Behind counts from unique tree content. The post-merge header correctly recorded PRs #106/#113 as merged, but it incorrectly said no PRs were open; later paragraphs also still described PR #106 v2 as active and its P0/P1 additions as belonging to an active PR. Corrected the live statement to identify Draft maintenance PR #115 as open and no research/physics PRs as open; reclassified PR #106 v2 as a merged historical source branch and updated the preservation/P0/P1 wording. |
| `research/BRANCH_INTEGRATION_AUDIT_2026-11-13.md` | `PASS_WITH_NOTES` after correction | The audit preserves useful dated branch inventories, integration chronology, tree-level comparisons and scientific acceptance boundaries. Its 2026-11-14 correction said no PRs remained open, while older dated sections still described PR #106 as active/Draft. Added an explicit historical-record note and clarified that PR #106/#113 are merged, no research/physics PRs remain open, and Draft maintenance PR #115 is the current open PR. Older dated branch metrics remain historical snapshots, not a live branch inventory. |

## Navigation correction

The deliverables README now labels the Higgs-portal package as a historical 2026-10-18 snapshot and points readers to the current Major 1 research README and `PROJECT_STATUS.md` for live work/status. The scientific contents of the historical handoff were not edited.

## Register and status

The baseline register remains 462 documents. After this batch:

- `PASS`: 1
- `PASS_WITH_NOTES`: 136
- `HISTORICAL`: 63
- `REVISION_REQUIRED`: 8
- `PENDING`: 254
- Individually reviewed: 208 / 462

The live project status was updated to 208 reviewed and 254 pending. The earlier 205/257 value is retained only as the checkpoint for the preceding B5 RGE/EFT review batch.

## Validation and limitations

- Confirmed the Higgs-portal SVG target exists at the exact relative path.
- Confirmed the new Major 1 research README target exists.
- Checked the branch audit documents against the current PR #115 status and the recorded PR #106/#113 merge chronology.
- Updated the two branch audit records to remove misleading current-status wording while retaining their dated historical comparisons.
- Updated the deliverables navigation, live project status and baseline register.
- No physics script, numerical output, manuscript source, referee-facing response or scientific result was modified or rerun.
- This review does not independently revalidate the 187 historical calculation sections, the branch-by-branch numerical comparisons, or the underlying physics claims. Their evidentiary limits remain explicit.

