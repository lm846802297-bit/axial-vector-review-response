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
- Preserve complete scientific reasoning. Remove repetition, redundant definitions, unrelated background, and disclaimers that add no argument.
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
