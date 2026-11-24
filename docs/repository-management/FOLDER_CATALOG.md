# Folder catalog

Inventory snapshot measured on PR #142 review branch `maintenance/92nd-document-review-20261124`, based on main after PR #123 merge and updated through the ninety-eighth individual document review. Counts are structural Git-tree entries, not unique scientific results.

## Repository footprint

- **2,551 Git-tree entries:** 2,385 files and 166 directories.
- **915 Markdown/text files:** 664 `.md` and 251 `.txt`.
- **Baseline register:** 462/462 dispositioned — 304 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, 0 `REVISION_REQUIRED`, 0 `PENDING`.
- **Supplemental register:** 453 entries — 221 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 223 `PENDING`, 3 `REVISION_REQUIRED`.
- **Document coverage:** all 915 Markdown/text paths are registered exactly once. The 93rd–96th review reports now state static source/output inspection only; their previous unsupported execution claims were withdrawn. The 98th review executed nine dimension-six source scripts and two independent regression scripts locally, with exact source fingerprints and output comparisons recorded. The old 28/20/20 degree-five output remains historical; the corrected 31/12/12 and 14/3/3 angular-reduction structures were reproduced by the degree-five regression. Eight of the nine existing dimension-six validation outputs matched stdout byte-for-byte; the nonexceptional-kinematics archive is a curated summary. The broader nonexceptional WW research note and full UV-EFT subtraction ledger remain PENDING.
- **Workflow inventory:** 140 YAML workflows — 125 `REVIEWED_WITH_NOTES`, 1 `ACTIVE`, 14 `HISTORICAL_CANDIDATE`, 0 `PENDING`.

| Area | Git-tree entries | Responsibility |
|---|---:|---|
| `.freebuff/` | 2 | Tool/project metadata; do not treat as research content. |
| `.github/` | 145 | Actions workflows, catalogs, audit registers and templates. |
| `archive/` | 37 | Frozen reply versions, historical research, referee analysis and manuscript baselines. |
| `deliverables/` | 22 | Extracted handoff packages and instructions. |
| `docs/` | 151 | Governance, document registers, review standards and audit reports. |
| `overleaf-source/` | 29 | Pinned manuscript source package; read-only source archive. |
| `research/` | 1,845 | Current scientific workstreams, inputs, scripts, tests, outputs and evidence. |
| `work/` | 18 | Intermediate and temporary material; not authoritative until promoted. |
| `审稿意见-gpt/` | 128 | Internal referee analysis, decisions, writing rules, current execution and original reviewer materials. |
| `导出/` | 3 | Exported artifacts; identify source and lifecycle before promotion. |
| `弃用/` | 7 | Explicitly deprecated material; retain pending provenance/link checks. |
| `计算脚本/` | 112 | Legacy calculation scripts, outputs and audit records. |
| `附件/` | 4 | Supporting historical attachments. |
| `[root]` | 13 files + 14 top-level directories | Governance/navigation, current status, formal reply TeX/PDF and bibliography/style dependencies. |

The root has 13 files and 14 top-level directories. The Croon/Lai PR adds no root files. Counts include each top-level directory node.

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
3. The seven baseline items dispositioned by the 90th review are `PASS_WITH_NOTES`; reopen any item only when new evidence changes its recorded disposition.
4. Do not delete or disable workflows based only on filenames or old branch references.
5. Before moving files, audit Markdown links, code imports, workflow shell paths, TeX/BibTeX dependencies and manifests.
6. A move must preserve original blob/size and be recorded in a path/SHA manifest.
7. CI success is not equivalent to physical acceptance or a validated phenomenological exclusion.

Registers: [baseline](DOCUMENT_AUDIT_REGISTER.csv), [supplemental](SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv), [workflow](../../.github/workflows/WORKFLOW_AUDIT_REGISTER.csv).

## 90th-review closeout integration

The seven baseline `REVISION_REQUIRED` records now have evidence-based `PASS_WITH_NOTES` dispositions. The 90th review, thermal-convergence provenance note, and closeout workflow review are included as supplemental records. The pure-vector Fig. 7 10 MeV physical discrepancy remains +92.4284%; no opacity rescaling or axial-vector constraint update is authorized.
