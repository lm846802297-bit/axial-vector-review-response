# Folder catalog

Inventory snapshot measured on PR #142 review branch `maintenance/92nd-document-review-20261124`, based on main after PR #123 merge and the ninety-second document review. Counts are structural Git-tree entries, not unique scientific results.

## Repository footprint

- **2,543 Git-tree entries:** 2,378 files and 165 directories.
- **910 Markdown/text files:** 661 `.md` and 249 `.txt`.
- **Baseline register:** 462/462 dispositioned — 304 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, 0 `REVISION_REQUIRED`, 0 `PENDING`.
- **Supplemental register:** 448 entries — 193 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 246 `PENDING`, 3 `REVISION_REQUIRED`.
- **Document coverage:** all 910 Markdown/text paths are registered exactly once. Five older pending documents were individually reviewed in the 91st review; five RC-001 records were inspected in the 92nd review (four PENDING, one Q8 REVISION_REQUIRED); five more were inspected in the 93rd review: four exact source reruns passed with byte-identical output, and the mixed-kinetic threshold output remains REVISION_REQUIRED because its printed finite coefficient is not derived by the script. The 94th review executed five further scripts: four exact source/output pairs pass, while the P1.5c direct-singlet color-projection claim is REVISION_REQUIRED because the code only checks hard-coded sign arrays. The remaining 246 PENDING records comprise 223 RC-001 archive files, four low-mass axial-vector package documents and 19 Croon/C1 checksum/archive records. Of the 26 new Croon/C1 documents, 7 are `PASS_WITH_NOTES` and 19 remain `PENDING`. The separately generated C1 high-order `SHA256SUMS` text manifest is also registered as `PASS_WITH_NOTES`.
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
