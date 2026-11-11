# Repository instructions — axial-vector paper revision project

## 1. Minimal preflight: every task

Before starting any task in this repository, read:

1. [PROJECT_STATUS.md](PROJECT_STATUS.md) — current project stage, verified repository state, open work, and next actions.
2. [README-先读这里.md](README-先读这里.md) — repository navigation and task-based reading routes.

This file (AGENTS.md) defines mandatory rules. Do not load every research document by default; follow the task routes below.

## 2. Task-based reading routes

### Referee-response writing, editing, or audit

Read:
- [审稿回复信与论文修改清单写作规范](审稿意见-gpt/写作规范/审稿回复写作原则.md)
- [Current referee-facing response](Replies_to_Referee_3_referee_facing_2026-11-04.tex)
- [Internal manuscript synchronization checklist](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)
- The relevant original referee-report passage and relevant meeting summary/transcript where needed.

Rules:
- The response letter is written only for the PRD referee. Directly answer every point and retain necessary derivations, equations, benchmarks, quantitative comparisons, citations, and scientific scope qualifications.
- Do not put internal task status, version mismatches, pending manuscript edits, branch/PR/CI information, or workflow notes in the referee-facing letter.
- Never claim a manuscript edit has been completed unless the actual selected manuscript source has been changed and checked.
- If the task is limited to the referee-response letter or its internal checklist, do not modify the manuscript source.
- A genuine scientific limitation is not an internal progress report. State physical and experimental applicability boundaries accurately.
- Preserve complete scientific reasoning. Do not delete or condense content based on textual similarity alone: first establish that the passages have the same physical proposition, applicability conditions, and argument function. Follow §3.1 of [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md); argument completeness takes priority over brevity.
- For every PR that modifies the referee-facing response or its supporting argument record, the PR description must cite [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md) §3.1, §6, and §7 and include a before/after preservation audit plus an explicit deletion/merge ledger (write “none” if there are no substantive deletions or merges). The reviewer’s formal review record must also cite those sections and record the compliance result and unresolved items. Any removal of an independent scientific conclusion, calculation evidence, validation result, or applicability condition requires the author's explicit approval.
- PR reviewers must inspect the actual diff and compare it with the deletion/merge ledger; do not rely solely on the PR author's summary. Distinguish static source checks, full compilation, PDF visual inspection, numerical reproduction, script tests, and CI; do not claim checks that were not run.
- Check that related Major and Minor points use the same model assumptions, conventions, and scope.

### Manuscript editing or manuscript/reply consistency

Read:
- The internal manuscript synchronization checklist.
- The exact manuscript source version selected by the author, plus its dependencies.
- The archived v6 PDF/source only as the identified baseline, not automatically as the active Overleaf version.
- Relevant technical derivations and source evidence.

Do not infer that a paper edit is complete from a response-letter statement or a proposed Diff.

### Physics derivation, numerical work, or phenomenology

Read:
- [Living research-decision register](审稿意见-gpt/项目规范/研究决策与不可回退事项.md).
- The relevant sections of [v5.7 technical reference](审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md) and/or the [v5.6 execution manual](审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md).
- The original manuscript Lagrangian/equations, the specific calculation ledger/scripts, and primary literature.

Read only relevant sections and evidence. The decision register records the author's current working position; it does not replace physical derivation or source verification.

### GitHub and repository maintenance

Read:
- This file, [PROJECT_STATUS.md](PROJECT_STATUS.md), and the README for the directory being changed.
- The actual current main/PR/branch state and relevant validation instructions.

Do not claim CI, compilation, or tests passed unless the exact current commit has corresponding evidence.

## 3. Authority and decision changes

- The author's **latest explicit instruction or confirmed revised view takes precedence** over older chats, meeting notes, historical drafts, and earlier decision-register entries.
- [研究决策与不可回退事项.md](审稿意见-gpt/项目规范/研究决策与不可回退事项.md) is a **living, editable register**, not an immutable rulebook. When the author clearly changes a decision, update the register, mark the former position as superseded/revoked, preserve its history, and update PROJECT_STATUS when relevant.
- Do not interpret a question or exploratory suggestion as a confirmed change unless the author clearly approves it. If the intended decision is ambiguous and materially affects the work, ask one concise clarification.
- A change in research strategy does not by itself change a physical fact. Physics claims still require a correct derivation, reproducible calculation, or reliable primary source.
- Historical meeting summaries record what was discussed at that time; they do not override the author's latest decision or replace physics verification.

## 4. File-role separation

- Referee-facing response letter: reviewer-facing scientific argument only.
- Manuscript synchronization checklist: internal record of manuscript locations, proposed edits, before/after text, and actual status.
- PROJECT_STATUS: concise current project state and next actions.
- Research-decision register: current author-approved positions and their revision history.
- v5.6/v5.7 manuals: task map and technical reference; neither is a substitute for current project status.

Do not merge these file roles or copy internal workflow content into the referee-facing letter.

## 5. Numerical calculation result submission and reproducibility

The following rules are mandatory for numerical research, phenomenology, data processing, and computational validation carried out for this project.

### 5.1 Commit completed research results to GitHub

- A completed calculation that is used to support a scientific statement, comparison, figure, benchmark, parameter limit, or a declared research milestone must be committed to the project GitHub repository. Do not leave the only copy on a local machine, in a temporary workspace, chat attachment, or expiring CI artifact.
- Submit the actual result files in their native, directly usable formats (for example CSV, JSON/JSONL, TXT, ROOT, HDF5, or the native format required by the calculation). **Do not package calculation outputs into a newly created ZIP/TAR archive as a substitute for committing the extracted files.** If an upstream archive is supplied, extract it first and commit the required extracted files; preserve their meaningful filenames and directory structure. Compression is not required for routine result submission.
- Place results under the relevant research topic directory. Use a dated, task-specific subdirectory when this avoids collisions or preserves a stable historical snapshot. Do not scatter one calculation across unrelated directories or create duplicate competing “authoritative” copies.
- Commit the calculation script or exact source revision needed to reproduce the result. If the script already exists in repository history, record its repository path and immutable commit/blob SHA rather than copying an identical source file without reason.
- Include the necessary inputs, or identify their immutable repository/source locations and record their SHA-256 checksums. Record the calculation settings and conventions that affect interpretation: units, parameter values, physical approximations, grids/quadrature, boundary conditions, and random seeds where applicable.
- Include a concise README or run record stating the purpose, input provenance, exact command or entry point, relevant software/runtime versions, output-file descriptions, and the validation performed. Preserve useful machine-readable outputs and the logs/checkpoints needed to resume or audit a long calculation; omit disposable caches, temporary build products, and unrelated scratch files.
- Add a SHA-256 manifest for submitted data files when practical, and especially for multi-file datasets or externally sourced inputs. Do not alter line endings, precision, column ordering, units, or source data silently during transfer; document any deliberate transformation.

### 5.2 Large, external, or restricted data

- Prefer directly committed, uncompressed files when their size and licensing permit. If a file exceeds GitHub's normal size limits or the repository's agreed storage policy, do not silently omit it or replace it with an opaque archive. Use Git LFS or another repository-approved durable storage location, and commit a manifest containing the exact filename, immutable retrieval location, byte size, format, and SHA-256 checksum.
- For externally hosted, licensed, or otherwise non-redistributable inputs, do not commit a prohibited copy. Record the original citation/source, version or release identifier, retrieval instructions, file identity, and checksum so that an authorized researcher can obtain and verify the same input.
- Never commit credentials, access tokens, private keys, personal data, or unrelated machine-specific configuration.

### 5.3 Submission and verification workflow

1. Finish the calculation locally and retain the exact output produced by the run.
2. Check file completeness, row/record counts, units, numerical finiteness, and the calculation-specific validation criteria. Record failed or incomplete checks explicitly; do not label a partial run as complete.
3. Organize the uncompressed deliverables and add the README/run record, provenance, and checksum manifest.
4. Commit to the appropriate task branch and submit through the relevant pull request. Do not push research changes directly to `main` unless the author explicitly instructs otherwise.
5. After the push, inspect the actual PR diff and retrieve the committed files from GitHub. Compare the remote file contents or Git blob identities against the local submission; verify the expected paths, file count, and checksums before reporting that the upload is complete.
6. Report repository submission status separately from scientific validation status. A successful commit, checksum match, or passing CI job does not by itself establish that the physical calculation is correct or that the research task is complete.

These rules apply to all future calculations in this repository, not only to the stellar-cooling work or the current PR.

