# Root-level file classification and safe migration proposal

Snapshot: `main` at `fb705dc74d63ff29681243ec94f303b12b78182a`, reviewed against the 2026-11-14 organization branch.

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
| `dw13678_report_1_a.pdf` | Original referee report | Candidate for `archive/referee-reports/`; immutable baseline, retain exact hash. |
| `（原件）dw13678_report_1_a.pdf` | Original-named duplicate candidate | Compare byte hash with the canonical referee PDF; if identical, retain one canonical file plus a provenance note, but do not delete until inbound references are checked. |
| `dw13678_report_1_a.md` | Extracted/annotated referee-report text | Keep adjacent to the source report or under a dedicated referee-report directory after checking links. |

## 4. Internal research notes and large working documents

| File | Role | Proposed treatment |
|---|---|---|
| `higgs_portal_mixing_merged_guide-gemini.md` | Higgs-portal guide / synthesis note | Compare against the dated 65/66 versions; classify as current, source synthesis or historical. Do not infer duplicate status from title. |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(65).md` | Large versioned portal note | Candidate for a dated Major 1 history folder after semantic diff and inbound-link audit. |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(66).md` | Large versioned portal note | Candidate for a dated Major 1 history folder after semantic diff and inbound-link audit. |
| `单圈混合推导独立复核报告-协调更新版-20261019.md` | Independent one-loop derivation review | Candidate for Major 1 evidence/review directory after confirming whether a newer authoritative report supersedes it. |
| `中微子扇区电荷分析-hy4-统一更新版-20261019.md` | Neutrino charge analysis | Candidate for Major 3 historical/evidence directory; keep model-extension scope explicit. |
| `审稿意见逐条对照表-统一更新版-20261019.md` | Reviewer-point crosswalk | Candidate for referee-response tracking directory; verify whether newer task maps supersede it. |

## 5. Directories already at root

The 13 root directories are indexed in FOLDER_CATALOG.md. In particular, `research/`, `审稿意见-gpt/`, `archive/`, `deliverables/`, `overleaf-source/`, `计算脚本/` and `work/` have distinct roles and should not be flattened into one generic folder.

## 6. Migration gates

A physical move is allowed only after all of the following are recorded:

1. Search all 469 Markdown/text documents for inbound links to the old path.
2. Search all Python/Mathematica/FORM sources and notebooks for hard-coded path strings/imports.
3. Search all 109 workflow YAML files and their shell commands for old paths.
4. Search all TeX `\input`, `\include`, `\includegraphics`, bibliography and `BSTINPUTS/BIBINPUTS` assumptions.
5. Update READMEs, manifests, tests, release notes and collaborator instructions in the same change.
6. Preserve original bytes and record old path → new path, old/new Git blob SHA, SHA-256 when available, and commit.
7. Run link/import/workflow-path/LaTeX build checks after the move.
8. Review the resulting diff and ensure no scientific source, result or model assumption changed accidentally.

## 7. Explicit no-delete list for this phase

No root file is deleted or overwritten by this proposal. The two large Higgs-portal documents and the two referee-report PDFs remain duplicate candidates only; exact content comparison is required before any deduplication.
