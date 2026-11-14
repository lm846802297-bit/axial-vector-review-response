# Root-level file classification and safe migration proposal

Snapshot: `main` at `fbab624435c853e90e3955009a545e28c5f5be98` (2026-11-14); the maintenance branch used for this review is five documentation-only commits behind this main snapshot.

This is a classification proposal, not a move/delete instruction. Root files are deliberately retained in place until all inbound Markdown links, TeX/BibTeX build assumptions, scripts, workflow references and external handoff instructions have been checked.

## 1. Governance and navigation

| File | Role | Proposed treatment |
|---|---|---|
| `README.md` | Main repository entry point | Keep at root. |
| `README-先读这里.md` | Chinese quick-start and reading route | Keep at root; link to README and current status. |
| `AGENTS.md` | Mandatory contributor/agent instructions | Keep at root; tooling expects root-level discovery. |
| `PROJECT_STATUS.md` | Canonical live status plus historical ledger | Keep at root for now; consider splitting a short dashboard from dated history only in a dedicated, link-preserving PR. |
| `GIT_MERGE_POLICY.md` | Research history and merge rules | Keep at root. |
| `仓库分类索引.md` | Cross-project topical index | Keep at root as a stable navigation alias; synchronize with the new management docs. |

## 2. Formal manuscript and response build inputs

| File | Role | Proposed treatment |
|---|---|---|
| `Replies_to_Referee_3_referee_facing_2026-11-04.tex` | Root-level editable response-letter source identified by archive policy | Keep at root until the current authoritative-source decision is reconfirmed from PROJECT_STATUS and latest PR history; moving it can break scripts/workflows and BibTeX lookup. |
| `Replies_to_Referee_3_referee_facing_2026-11-04.pdf` | Compiled response PDF/reference build | Keep at root while README links and build workflow expect it; record its exact source commit and checksum. |
| `Replies_to_Referee_3_stellar_references.bib` | Response bibliography input | Keep at root unless build variables and TeX paths are migrated together. |
| `JHEP.bst` | BibTeX style dependency | Keep at root while root TeX uses `\bibliographystyle{JHEP}`. |
| `references.bib` | Root-level bibliography database | Audit actual references before assigning ownership; do not merge with other .bib files by filename. |
| `Replies_to_Referee_3_referee_facing_2026-10-28.tex` | Historical response source | Candidate for archive/reply-letter/snapshots after checking all links and restoring instructions. |
| `Replies_to_Referee_3_referee_facing_2026-11-03.tex` | Historical response source | Candidate for archive/reply-letter/snapshots after checking all links and restoring instructions. |

## 3. Manuscript/reviewer baseline PDFs and source documents

| File | Role | Proposed treatment |
|---|---|---|
| `axial_vector_model_building-v6.pdf` | Manuscript baseline PDF | Candidate for `archive/manuscript-baselines/` or a pinned source package; keep root until all references and build notes are updated. |
| `dw13678_report_1_a.pdf` | Annotated referee-report PDF variant | 161,829 bytes; SHA-256 `752226d1…`; one highlight annotation was detected. It is distinct from the `(原件)` file; do not assume either is pristine without provenance review. |
| `（原件）dw13678_report_1_a.pdf` | Separate original-named annotated PDF variant | Not byte-identical to `dw13678_report_1_a.pdf` (158,794 bytes; SHA-256 `ac7357aa…` versus 161,829 bytes; SHA-256 `752226d1…`). Both contain highlight annotations (4 versus 1); page/text equivalence is not established. Preserve both; do not label as duplicates or delete. |
| `dw13678_report_1_a.md` | Extracted/annotated referee-report text | Keep adjacent to the source report or under a dedicated referee-report directory after checking links. |

## 4. Internal research notes and large working documents

| File | Role | Proposed treatment |
|---|---|---|
| `higgs_portal_mixing_merged_guide-gemini.md` | Historical Higgs-portal guide / synthesis note | Individually reviewed and marked HISTORICAL. Its conditional soft-loop route, VLL threshold and old response drafts remain useful provenance; current Major 1 progress is in A2–A5. Do not copy the old response text. |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(65).md` | Historical cumulative portal note v65 | Sequential historical snapshot ending at §261.12. Keep as provenance; do not treat as current state or merge mechanically with v66. |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(66).md` | Historical cumulative portal note v66 | Later sequential snapshot; includes new §262 light-fermion two-point/pole-kernel work beyond v65. Keep as provenance; not a duplicate of v65 and not current status authority. |
| `单圈混合推导独立复核报告-协调更新版-20261019.md` | Independent one-loop derivation review | Candidate for Major 1 evidence/review directory after confirming whether a newer authoritative report supersedes it. |
| `中微子扇区电荷分析-hy4-统一更新版-20261019.md` | Neutrino charge analysis | Candidate for Major 3 historical/evidence directory; keep model-extension scope explicit. |
| `审稿意见逐条对照表-统一更新版-20261019.md` | Reviewer-point crosswalk | Candidate for referee-response tracking directory; verify whether newer task maps supersede it. |

## 5. Directories already at root

The 13 root directories are indexed in FOLDER_CATALOG.md. In particular, `research/`, `审稿意见-gpt/`, `archive/`, `deliverables/`, `overleaf-source/`, `计算脚本/` and `work/` have distinct roles and should not be flattened into one generic folder.

## 6. Migration gates

A physical move is allowed only after all of the following are recorded:

1. Search all current Markdown/text documents for inbound links to the old path (baseline register: 462; live tree count is maintained in FOLDER_CATALOG.md).
2. Search all Python/Mathematica/FORM sources and notebooks for hard-coded path strings/imports.
3. Search all 109 workflow YAML files and their shell commands for old paths.
4. Search all TeX `\input`, `\include`, `\includegraphics`, bibliography and `BSTINPUTS/BIBINPUTS` assumptions.
5. Update READMEs, manifests, tests, release notes and collaborator instructions in the same change.
6. Preserve original bytes and record old path → new path, old/new Git blob SHA, SHA-256 when available, and commit.
7. Run link/import/workflow-path/LaTeX build checks after the move.
8. Review the resulting diff and ensure no scientific source, result or model assumption changed accidentally.

## 7. Explicit no-delete list for this phase

No root file is deleted or overwritten by this proposal. v65/v66 are sequential portal snapshots, not duplicates. The two referee-report PDFs are distinct annotated variants, not byte-identical; their page/text equivalence is still unverified. The large v65/v66 files are retained as historical provenance. See [root-file audit report](ROOT_FILE_AUDIT_REPORT_2026-11-14.md).


## 8. Completed root-file audit

The 24 root files have now been individually classified for authority, build dependency, provenance and next action. See [ROOT_FILE_AUDIT_REPORT_2026-11-14.md](ROOT_FILE_AUDIT_REPORT_2026-11-14.md). Four PDF artifacts remain blocked for visual/text extraction in this review environment; their byte hashes and metadata are recorded where available. The current formal reply TeX passed static citation, label, cross-reference and figure-path checks, but the current root PDF still requires a same-source rebuild/render audit.
