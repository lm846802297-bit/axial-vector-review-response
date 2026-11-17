# Folder catalog

Updated 2026-11-17. Counts describe the audited tree for PR #117 on branch `chore/migrate-major2-major3-major42-scripts-20261117`, based on `main` commit `39814f992c1aa60fed04ab9cf01459f5ea205236`.

## Repository footprint

- **1,712 Git-tree entries:** 1,581 files and 131 directories.
- **605 Markdown/text files:** 506 `.md` and 99 `.txt`.
- **Baseline register:** 462/462 individually reviewed — 297 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, 7 `REVISION_REQUIRED`, 0 `PENDING`.
- **Supplemental register:** 143 entries — 137 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 0 `PENDING`, 0 `REVISION_REQUIRED`.
- **Workflow inventory:** 115 YAML workflows — 100 `REVIEWED_WITH_NOTES`, 1 `ACTIVE`, 14 `HISTORICAL_CANDIDATE`, 0 `PENDING`.

| Area | Git-tree entries | Responsibility |
|---|---:|---|
| `.freebuff/` | 2 | Tool/project metadata; do not treat as research content. |
| `.github/` | 120 | Actions workflows, catalogs, audit registers and templates. |
| `archive/` | 37 | Frozen reply versions, historical research, referee analysis and manuscript baselines. |
| `deliverables/` | 22 | Extracted handoff packages and instructions. |
| `docs/` | 127 | Governance, document registers, review standards and audit reports. |
| `overleaf-source/` | 29 | Pinned manuscript source package; read-only source archive. |
| `research/` | 1,091 | Current scientific workstreams, inputs, scripts, tests, outputs and evidence. |
| `work/` | 18 | Intermediate and temporary material; not authoritative until promoted. |
| `审稿意见-gpt/` | 128 | Internal referee analysis, decisions, writing rules, current execution and original reviewer materials. |
| `导出/` | 3 | Exported artifacts; identify source and lifecycle before promotion. |
| `弃用/` | 7 | Explicitly deprecated material; retain pending provenance/link checks. |
| `计算脚本/` | 112 | Legacy calculation scripts, outputs and audit records. |
| `附件/` | 4 | Supporting historical attachments. |
| `[root]` | 12 files + 13 top-level directories | Governance, current status, formal reply TeX/PDF and its BibTeX/style dependencies. |

The root has 12 files after the PR #116 historical-file moves; the active-script relocation does not change the root file count. The original 24-file audit remains a historical baseline; see [the relocation audit](ROOT_RELOCATION_AUDIT_2026-11-17.md) and [blob/size manifest](ROOT_RELOCATION_MANIFEST_2026-11-17.csv). Counts include each top-level directory node.

## Directory ownership and migration boundaries

- The three response-support packages are indexed under `research/`; see the [active-script relocation audit](ACTIVE_SCRIPT_RELOCATION_AUDIT_2026-11-17.md) and [path/blob manifest](ACTIVE_SCRIPT_RELOCATION_MANIFEST_2026-11-17.csv).

- `research/` owns current physical workstreams and reproducible scientific evidence.
- `计算脚本/` retains legacy scripts and historical outputs until all imports and consumers are traced.
- `审稿意见-gpt/` owns internal referee-response analysis; original referee materials are under `原始审稿材料/`.
- `archive/` owns historical snapshots, not current task status; see [archive README](../../archive/README.md).
- `overleaf-source/` owns the pinned source package; see [source README](../../overleaf-source/README.md).
- Major 2, Major 3 response-only and Major 4.2 packages now live in `research/major2-parameter-window-20261117/`, `research/major3-neutrino-response-optional-seesaw-20261117/` and `research/major4-2-kinetic-mixing-20261117/`. The remaining `计算脚本/` tree retains Major 1 tools and Section 250–262/DeepSeek66 history.

## Maintenance rules

1. Keep root `README.md`, `PROJECT_STATUS.md` and the living decision register as concise entry points.
2. Keep the baseline and supplemental registers non-overlapping and synchronized with the current Git tree.
3. Resolve the seven baseline `REVISION_REQUIRED` items only after row-specific evidence is committed and independently checked.
4. Do not delete or disable workflows based only on filenames or old branch references.
5. Before moving files, audit Markdown links, code imports, workflow shell paths, TeX/BibTeX dependencies and manifests.
6. A move must preserve original blob/size and be recorded in a path/SHA manifest.
7. CI success is not equivalent to physical acceptance or a validated phenomenological exclusion.

Registers: [baseline](DOCUMENT_AUDIT_REGISTER.csv), [supplemental](SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv), [workflow](../../.github/workflows/WORKFLOW_AUDIT_REGISTER.csv).
