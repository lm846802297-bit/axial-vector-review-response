# Repository instructions — axial-vector paper revision project

## 1. Minimal preflight: every task

Before starting any task in this repository, read:

1. [PROJECT_STATUS.md](PROJECT_STATUS.md) — current project stage, verified repository state, open work, and next actions.
2. [README-先读这里.md](README-先读这里.md) — repository navigation and task-based reading routes.
3. The [central standards index](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/governance/CENTRAL_STANDARDS_INDEX.md) and [research/standards-lock.yaml](research/standards-lock.yaml) — the exact adopted shared standards revision and profiles.
4. [RESEARCH_COMPUTE_POLICY.md](RESEARCH_COMPUTE_POLICY.md) — the local compatibility pointer to the pinned central compute policy.

This file (AGENTS.md) defines mandatory project rules. Shared governance, task handoff, compute, archival, RCRPS, document review, referee-response, and Git requirements are maintained centrally at the pinned revision. Do not load every research document by default; follow the task routes below.

For substantive research, derivation, numerical, code, validation, or referee-response work, follow the [central Research Task Handoff Standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/RESEARCH_TASK_HANDOFF_STANDARD.md) and use the [central Research Task Brief template](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/templates/research-task-brief.md). Trivial editorial/maintenance changes may omit a brief when the PR explains why it is not applicable.

## Task-level central standards provenance

For every substantive task, create a machine-readable record at `research/standards-provenance/tasks/<task-id>.json` using the central Standards Adoption schema. Bind the exact standards-lock and finalized task-brief bytes by SHA-256; record the locked central commit, only the profiles actually applied, project-local extensions, and predeclared acceptance criteria. For numerical runs, repeat the same provenance in `run_manifest.extensions.standards_provenance`. The `.github/workflows/standards-adoption-validation.yml` workflow validates the lock and any task/run provenance records. A lock file alone does not prove task-level application.


## 2. Task-based reading routes

### Referee-response writing, editing, or audit

Read:
- [中央审稿回复与论文同步规范](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/REFEREE_RESPONSE_AND_MANUSCRIPT_SYNCHRONIZATION_STANDARD.md)
- [轴矢量项目审稿回复写作扩展](审稿意见-gpt/写作规范/审稿回复写作原则.md)
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

## 5. Numerical research and result archival

The shared rules for primary execution environment, run provenance, GitHub archival, native outputs, extraction, SHA-256 verification, and structured numerical records are governed by the pinned central [Research Compute Policy](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/RESEARCH_COMPUTE_POLICY.md), [Calculation-result Archival Policy](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/CALCULATION_RESULT_ARCHIVAL_POLICY.md), and [RCRPS v1.0.1](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/STRUCTURED_RESULT_DATA_STANDARD_v1.0.1.md).

The axial-vector project-specific RCRPS extension is [docs/repository-management/STRUCTURED_RESULT_DATA_STANDARD.md](docs/repository-management/STRUCTURED_RESULT_DATA_STANDARD.md). It defines only the `supernova_transport` and `uv_eft` fields. Preserve existing C1/A0 JSON, CSV, figures, and historical calculation outputs; new substantial runs must use the v1.0.1 source-control provenance contract and retain the project-specific physical metadata.

The local `RESEARCH_COMPUTE_POLICY.md` remains as a stable compatibility entry point; it is not a second copy of the shared policy.


## CI and independent verification

Follow the pinned central [Research Compute Policy](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/RESEARCH_COMPUTE_POLICY.md). GitHub Actions is optional supporting infrastructure unless the task owner explicitly requires a particular run. It does not replace the primary calculation or scientific validation. Record the exact status and commit for checks actually run; do not treat a queued workflow as a blocker or an unrun check as passed.


## GitHub PR review and merge

Follow the pinned central [Git Merge Policy](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/governance/GIT_MERGE_POLICY.md). This repository retains **Create a merge commit** as its default for substantive research, numerical, validation, referee-response, and archival work. The local [GIT_MERGE_POLICY.md](GIT_MERGE_POLICY.md) is a compatibility pointer, not an independent second policy.


## Research communication and decision policy

Follow the pinned central [Research Governance Standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/RESEARCH_GOVERNANCE_STANDARD.md) and the [Research reporting standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/scientific-diff-workflow.md#11-research-reporting-and-communication-standard). For referee-response work, also follow the central [Referee Response and Manuscript Synchronization Standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/14155487afc075d301fa7f6cf452c7bff137e869/docs/REFEREE_RESPONSE_AND_MANUSCRIPT_SYNCHRONIZATION_STANDARD.md) and the stricter axial-vector [local writing profile](审稿意见-gpt/写作规范/审稿回复写作原则.md).

The [研究决策与不可回退事项](审稿意见-gpt/项目规范/研究决策与不可回退事项.md) remains the project-specific author-approved decision register. It records current model choices and historical decision changes; it does not replace the central source hierarchy.


### Axial-vector referee-response boundary

Apply this standard to internal research discussion, progress reports, calculations, reviews, and task handoffs. Formal referee-facing response letters and manuscript text remain governed by the repository's dedicated referee-response writing rules. Retain genuine physical and experimental applicability qualifications where they are scientifically relevant, while avoiding repetitive defensive wording. Never insert internal task status, branch/PR/CI details, or workflow notes into the referee-facing letter.
