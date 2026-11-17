# Folder catalog

Live Git-tree inventory for branch `maintenance/close-baseline-revision-required-20261117`, updated 2026-11-17 after the ninetieth review. Counts are structural entries, not counts of unique scientific results.

## Repository footprint

- **1,710 Git-tree entries:** 1,587 files and 123 directories.
- **599 Markdown/text files:** 500 `.md` and 99 `.txt`.
- **Baseline document register:** 462/462 individually dispositioned; 304 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, 0 `REVISION_REQUIRED`, 0 `PENDING`. Current fingerprints: 385 match, 76 content hashes differ from the originally reviewed version, and 1 size-only metadata discrepancy; differences are retained and described in each row.
- **Supplemental document register:** 137 post-baseline Markdown/text files; 131 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 0 `PENDING`, and 0 `REVISION_REQUIRED`. Every supplemental document has an individual review disposition.
- **118 GitHub Actions workflow YAML files:** 103 `REVIEWED_WITH_NOTES`, 14 `HISTORICAL_CANDIDATE`, 1 `ACTIVE`, 0 `PENDING`.
- **277 JSON files** and **414 Python files** (file counts only; not all are production code).

| Top-level area | Git-tree entries | Responsibility | Management rule |
|---|---:|---|---|
| `.github/` | 123 | 118 Actions workflows plus workflow catalog, audit register, review notes, templates and metadata | Keep workflow YAML in `.github/workflows/`; review triggers, permissions, paths and write-back behavior before deprecation. |
| `archive/` | 20 | Frozen source snapshots and historical response-letter packages | Immutable; add new dated snapshots instead of editing old ones. |
| `deliverables/` | 22 | Extracted handoff packages and instructions | Keep file-level hashes, extraction provenance and import instructions. Do not store generated ZIP/Base64 bundles as substitutes for extracted contents. |
| `docs/` | 126 | Repository management, review standards and audit records | Keep navigation, governance, baseline and supplemental audit records here. |
| `overleaf-source/` | 28 | Pinned manuscript source snapshots | Treat as versioned source archives; confirm active Overleaf source before editing. |
| `research/` | 1,085 | Scientific workstreams, inputs, scripts, tests, outputs and evidence | Use one directory per physical model/workstream; preserve original one-VEV vs two-VEV separation. |
| `work/` | 18 | Intermediate and temporary research material | Not authoritative until promoted and reviewed. |
| `审稿意见-gpt/` | 122 | Referee analysis, current execution notes, decisions, meeting records and historical work | Keep reviewer-facing text separate from internal notes; dated status snapshots remain history. |
| `导出/` | 3 | Exported artifacts | Identify source and lifecycle before promotion to deliverables. |
| `弃用/` | 7 | Explicitly deprecated material | Retain unless provenance and inbound references are audited. |
| `计算脚本/` | 126 | Legacy calculation scripts, outputs and audit records | Preserve historical paths until imports and references are migrated and checked. |
| `附件/` | 4 | Supporting attachments | Link from owning document; avoid duplicate authoritative copies. |
| `[root]` | 24 files + 13 top-level directories | Project entry points, formal TeX/PDF, bibliographies, manuscript/reviewer PDFs and legacy notes | Keep only build-critical/authority files at root; use the root-file audit before proposing moves. |
| `.freebuff/` | 2 | Tool/project metadata (one directory and one metadata file) | Do not edit or relocate as ordinary research content. |

Directory counts include each top-level directory node. The `[root]` row lists the 24 root files and notes the 13 top-level directories for orientation; those directory nodes are already included in their respective subtree counts and must not be added twice. All counts refer to the same recursive Git-tree snapshot.

## Root-level file classification

See [ROOT_FILE_CLASSIFICATION.md](ROOT_FILE_CLASSIFICATION.md) for the 24 root files and safe migration proposal. No root files have been moved in this phase because TeX, BibTeX, relative links and historical provenance may depend on their current paths.

## Review coverage and current priorities

The seventy-fourth through eighty-ninth reviews completed the supplemental documentation and workflow triage. The ninetieth review closes the seven baseline `REVISION_REQUIRED` records with evidence-based dispositions; see the [ninetieth report](NINETIETH_REVIEW_B16_AND_REPOSITORY_BASELINE_CLOSEOUT_2026-11-17.md), [thermal-convergence provenance note](THERMAL_CONVERGENCE_CSV_PROVENANCE_2026-11-17.md), and [new closeout workflow review](workflow-reviews/B16_LOCAL_RATE_ESCAPE_AND_SCAN_ARCHIVE_WORKFLOW_REVIEW_2026-11-17.md).

1. Keep root `README.md`, `PROJECT_STATUS.md` and the living decision register as concise governance entry points.
2. All **137 supplemental Markdown/text files** now have individual review dispositions (0 `PENDING`, 0 `REVISION_REQUIRED`). The current section-log sidecar has been regenerated from exact Git bytes and matches 8/8; its superseded hash set remains in Git history.
3. All **462 baseline records** now have explicit dispositions; 0 remain `REVISION_REQUIRED`. Preserve `PASS_WITH_NOTES` and `HISTORICAL` where scientific or provenance limitations remain.
4. The 118-workflow register now has 0 `PENDING`; 14 historical candidates remain retained, and one PR response build is active. Do not disable or delete a workflow based only on its filename or an old branch reference.
5. Audit relative links, Python imports, workflow paths, LaTeX inputs, bibliography lookup and manifests before any physical relocation.
6. Refresh the PR-vs-main comparison before integration; this catalog does not authorize merge or scientific acceptance.

The baseline and supplemental registers are deliberately separate: [baseline register](DOCUMENT_AUDIT_REGISTER.csv), [supplemental register](SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv), and [workflow register](../../.github/workflows/WORKFLOW_AUDIT_REGISTER.csv).
