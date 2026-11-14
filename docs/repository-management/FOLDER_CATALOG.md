# Folder catalog

Historical 2026-11-14 Git-tree snapshot for branch `maintenance/repository-organization-audit-20261114`; counts below predate subsequent report relocation and new audit files. See the current register and Git tree for live counts.

## Repository footprint

- **1,541 Git tree entries** (1,420 files and 121 directories).
- **482 Markdown/text documents** in the current organization branch; the 462-row baseline register tracks the original inventory, with new review reports and indexes tracked separately.
- **412 source-code files** with Python/Mathematica/FORM-like extensions counted by the inventory.
- **261 JSON files**.
- **109 GitHub Actions workflow YAML files**.

| Top-level area | Git tree entries | Responsibility | Management rule |
|---|---:|---|---|
| `.github/` | 120 | 109 Actions workflows plus workflow catalog, review notes, templates and metadata | Workflow catalog/register under `.github/workflows/`; inspect callers and run history before deprecation. |
| `archive/` | 19 | Frozen source snapshots and historical response-letter packages | Immutable; add new dated snapshots instead of editing old ones. |
| `deliverables/` | 21 | Extracted handoff packages and instructions | Keep file-level hashes, extraction provenance and import instructions. Do not store generated ZIP/Base64 bundles. |
| `docs/` | 14 | Repository management, review standards and audit records | Keep navigation and governance documentation here. |
| `overleaf-source/` | 27 | Pinned manuscript source snapshots | Treat as versioned source archives; confirm active Overleaf source before editing. |
| `research/` | 1,035 | Scientific workstreams, inputs, scripts, tests, outputs and evidence | Use one directory per physical model/workstream; preserve original one-VEV vs two-VEV separation. |
| `work/` | 16 | Intermediate and temporary research material | Not authoritative until promoted and reviewed. |
| `审稿意见-gpt/` | 121 | Referee analysis, current execution notes, decisions, meeting records and historical work | Keep reviewer-facing text separate from internal notes; old status documents remain dated history. |
| `导出/` | 2 | Exported artifacts | Identify source and lifecycle before promotion to deliverables. |
| `弃用/` | 5 | Explicitly deprecated material | Retain unless provenance and inbound references are audited. |
| `计算脚本/` | 121 | Legacy calculation scripts, outputs and audit records | Current README appears to describe legacy section 250–262 material; verify ownership before merging with research/. |
| `附件/` | 2 | Supporting attachments | Link from owning document; avoid duplicate authoritative copies. |
| `[root]` | 37 entries (24 files + 13 directories) | Project entry points, formal TeX/PDF, bibliographies, manuscript/reviewer PDFs and legacy notes | Keep only build-critical/authority files at root; migration proposals are recorded separately. |
| `.freebuff/` | 1 directory + 1 metadata file | Tool/project metadata | Do not edit or relocate as ordinary research content. |

Counts include nested files and directory entries as represented by the Git tree. They are not counts of unique scientific results. Counts may change as this branch adds documentation.

## Root-level file classification

See [ROOT_FILE_CLASSIFICATION.md](ROOT_FILE_CLASSIFICATION.md) for a file-by-file grouping of the 24 root files and a safe migration proposal. No root files have been moved in this phase because TeX, BibTeX, relative links and historical provenance may depend on their current paths.

## Immediate priorities

1. Keep root README, PROJECT_STATUS and decision ledger as the concise governance entry points.
2. Refresh old subdirectory READMEs that still expose PR/task states from October or early November.
3. Review similarly named Higgs-portal and referee-analysis files by content/provenance; different Git blob IDs do not prove duplication.
4. Complete the 109-workflow audit and identify current versus historical workflows before changing triggers or permissions.
5. Continue the 462-row baseline Markdown/text review: 105 individually reviewed, 357 still `PENDING` at the latest recorded baseline snapshot; newly added review reports and indexes are tracked separately.
6. Audit all relative links, Python imports, workflow paths, LaTeX inputs, bibliography lookup and manifests before any physical relocation. The maintenance branch was synchronized with main at merge commit `e4dd7ec`; refresh the comparison before integration.
