# Folder catalog

Live Git-tree inventory for branch `maintenance/repository-organization-audit-20261114`, updated 2026-11-17. Counts are structural entries, not counts of unique scientific results.

## Repository footprint

- **1,676 Git-tree entries:** 1,553 files and 123 directories.
- **579 Markdown/text files:** 480 `.md` and 99 `.txt`.
- **Baseline document register:** 462/462 individually reviewed; 296 `PASS_WITH_NOTES`, 2 `PASS`, 153 `HISTORICAL`, 11 `REVISION_REQUIRED`, 0 `PENDING`. Current fingerprints: 390 match, 71 content hashes differ from the recorded reviewed version, and 1 size-only metadata discrepancy; reconciliation is open.
- **Supplemental document register:** 117 post-baseline Markdown/text files; 110 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 0 `PENDING`, and 1 `REVISION_REQUIRED`. Every supplemental document has an individual review disposition; the remaining issue is the current section-log checksum sidecar.
- **115 GitHub Actions workflow YAML files:** 47 `REVIEWED_WITH_NOTES`, 16 `HISTORICAL_CANDIDATE`, 52 `PENDING`.
- **274 JSON files** and **410 Python files** (file counts only; not all are production code).

| Top-level area | Git-tree entries | Responsibility | Management rule |
|---|---:|---|---|
| `.github/` | 120 | 115 Actions workflows plus workflow catalog, audit register, review notes, templates and metadata | Keep workflow YAML in `.github/workflows/`; review triggers, permissions, paths and write-back behavior before deprecation. |
| `archive/` | 20 | Frozen source snapshots and historical response-letter packages | Immutable; add new dated snapshots instead of editing old ones. |
| `deliverables/` | 22 | Extracted handoff packages and instructions | Keep file-level hashes, extraction provenance and import instructions. Do not store generated ZIP/Base64 bundles as substitutes for extracted contents. |
| `docs/` | 106 | Repository management, review standards and audit records | Keep navigation, governance, baseline and supplemental audit records here. |
| `overleaf-source/` | 28 | Pinned manuscript source snapshots | Treat as versioned source archives; confirm active Overleaf source before editing. |
| `research/` | 1,074 | Scientific workstreams, inputs, scripts, tests, outputs and evidence | Use one directory per physical model/workstream; preserve original one-VEV vs two-VEV separation. |
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

The seventy-fourth review completed the last 12 pending supplemental documents; see [the review report](SEVENTY_FOURTH_REVIEW_FINAL_RESEARCH_READMES_AND_MANIFESTS_2026-11-17.md).

1. Keep root `README.md`, `PROJECT_STATUS.md` and the living decision register as concise governance entry points.
2. All **117 supplemental Markdown/text files** now have individual review dispositions (0 `PENDING`); resolve the one supplemental `REVISION_REQUIRED` current section-log checksum sidecar from exact intended bytes.
3. Resolve or explicitly retain the **11 baseline `REVISION_REQUIRED`** items only after evidence-based review; never bulk-promote them.
4. Continue triage of the **52 pending workflows**. Do not disable or delete a workflow based only on its filename or an old branch reference.
5. Audit relative links, Python imports, workflow paths, LaTeX inputs, bibliography lookup and manifests before any physical relocation.
6. Refresh the PR-vs-main comparison before integration; this catalog does not authorize merge or scientific acceptance.

The baseline and supplemental registers are deliberately separate: [baseline register](DOCUMENT_AUDIT_REGISTER.csv), [supplemental register](SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv), and [workflow register](../../.github/workflows/WORKFLOW_AUDIT_REGISTER.csv).
