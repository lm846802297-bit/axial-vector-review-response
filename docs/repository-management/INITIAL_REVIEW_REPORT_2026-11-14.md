# Initial document review report — 2026-11-14

## Review scope and reproducibility

- Audited branch: `maintenance/repository-organization-audit-20261114`
- Base `main` commit: `fb705dc74d63ff29681243ec94f303b12b78182a`
- Base inventory: 1,517 Git tree entries; 462 Markdown/text documents; 397 Python files; 261 JSON files; 109 workflow YAML files; 30 PDFs.
- The 462-row register is an inventory, not a declaration that 462 documents have been content-reviewed.
- This first review batch covers 16 high-level entry, governance, decision, and workstream README/status documents. Review was limited to the complete fetched text, headings, internal Markdown links, role, authority and consistency statements. It is not a substitute for equation-by-equation physics review against source papers and numerical data.

## Per-document findings

| Document | Review outcome | Findings / action |
|---|---|---|
| `README.md` | PASS_WITH_NOTES | Good task-oriented entry point and clear authority links. Added repository-management and document-audit links. Its claim that the 2026-11-04 reply TeX is the current sole authoritative letter must continue to be checked against the latest status/PR history before any manuscript-facing edit. |
| `README-先读这里.md` | REVISION_REQUIRED | Contains 2026-11-06 task/PR state presented under a current-work heading despite newer 2026-11-14 status material. Added an explicit warning that dated entries are historical snapshots and pointed readers to current status sources. The detailed old task bullets still require a later content refresh. |
| `AGENTS.md` | PASS_WITH_NOTES | Clear mandatory preflight, task-based reading routes, evidence requirements and merge policy. Several internal links are present; no broken link found in the sampled check. Reconcile its instructions against the new review register in a later governance pass. |
| `PROJECT_STATUS.md` | REVISION_REQUIRED | The file is a large append-only status ledger (~115 kB) with several nested live-status headings and historical snapshots. This preserves provenance but makes the active state difficult to identify. Keep it as the canonical state source for now; next pass should extract a short current dashboard while preserving dated history verbatim. |
| `仓库分类索引.md` | PASS_WITH_NOTES | Useful topic-oriented index with authority and evidence distinctions. It predates the latest research archive organization; needs a post-2026-11-14 refresh and a link to the new management index. |
| `GIT_MERGE_POLICY.md` | PASS | Concise, consistent research-history policy. |
| `research/README.md` | REVISION_REQUIRED | Too short for a directory containing more than one thousand tree entries. Expand it into a workstream map linking all canonical research roots and stating the model/acceptance boundaries. |
| `research/MAIN_RESEARCH_INDEX_2026-11-13.md` | PASS_WITH_NOTES | Strong workstream and scientific-acceptance overview; explicitly distinguishes code validation from physical acceptance. Filename date and content title differ by one day; retain provenance but consider a stable alias such as `research/MAIN_RESEARCH_INDEX.md`. |
| `research/stellar-cooling-constraints-20261105/README.md` | PASS_WITH_NOTES | Detailed scientific scope, reproduction route and conditional-contour caveats. Internal relative links include sibling workstreams and should be checked by a full link validator. |
| `research/stellar-cooling-constraints-20261105/VALIDATION_AND_REVIEW.md` | PASS_WITH_NOTES | Extensive dated validation history and explicit physical gate limitations. It is a cumulative log; do not interpret earlier PASS statements as current global acceptance. |
| `research/stellar-cooling-collaborator-archive-20261113/README.md` | PASS_WITH_NOTES | Clear collaborator-facing entry and handoff boundary. Its relative links are mostly expressed as inline paths; verify referenced files and commands in the next workstream audit. |
| `research/stellar-cooling-collaborator-archive-20261113/STATUS_MATRIX.md` | PASS_WITH_NOTES | Explicit labels and open scientific gates. Keep synchronized with the canonical project status and the underlying validation reports. |
| `research/major1-higgs-scalar-mixing-20261109/README.md` | PASS_WITH_NOTES | Detailed staged research plan and progress record. It is very large (~71 kB) and accumulates dated updates; add a concise current-state summary and avoid treating subcalculation passes as complete gauge-independent mixing/pole validation. |
| `research/radial-scalar-collider-recast-2026-10-28/README.md` | PASS_WITH_NOTES | Scope and acceptance gates are explicit. Preserve the original one-VEV model boundary and do not promote pointwise recast checks to a completed experimental reinterpretation. |
| `archive/reply-letter/README.md` | REVISION_REQUIRED | The document linked a 2026-11-04-r1 manifest that is absent from the current tree. Replaced the dead link with an explicit unresolved historical-reference note. Other archive snapshots remain linked. |
| `审稿意见-gpt/写作规范/审稿回复写作原则.md` | REVISION_REQUIRED | Contains a malformed self-link that resolves to a nonexistent nested path. Replaced it with “本规范”. The substantive separation between reviewer-facing response and internal manuscript checklist is sound. |
| `审稿意见-gpt/项目规范/研究决策与不可回退事项.md` | PASS_WITH_NOTES | Decision hierarchy and original-model/response-only extension boundaries are clear. It is a dynamic decision ledger; each entry must be checked against current author decisions and the latest status before use. |

## Link audit

A sampled Markdown-link scan across the 16 documents found two unresolved local references:

1. `archive/reply-letter/README.md` → `snapshots/2026-11-04-r1/manifest.md`: target absent from the current tree. Replaced with an explicit unresolved historical-reference note; no file was fabricated.
2. `审稿意见-gpt/写作规范/审稿回复写作原则.md` → malformed self-reference. Replaced with “本规范”.

After these corrections, rerun the same link scan and then expand it to all 462 Markdown/text documents. The initial scan was a sample, not a repository-wide link certification.

## Structural findings

1. The `research/` subtree accounts for 1,035 entries and needs a canonical directory index, not a flat list of every file.
2. Root contains 24 files, including formal TeX/PDF, large working notes and duplicate-version candidates. Do not move them until every inbound link, TeX dependency, script path and external handoff reference is checked.
3. `PROJECT_STATUS.md` is too large to function as a quick dashboard even though it remains the designated source of current status.
4. The repository has 109 workflow files. They need an index grouped by scientific purpose and a supersession/active status; do not delete old workflows before checking run history and downstream references.
5. Large similarly named Higgs-portal documents (about 1.57 MB and 1.61 MB) are duplicate candidates, not confirmed duplicates. Compare hashes and semantic/provenance differences before disposition.
6. Legacy `计算脚本/`, `work/`, `弃用/`, and `审稿意见-gpt/旧版本/` need consistent lifecycle labels and README navigation.

## Changes made on this branch

- Added repository structure and navigation guide.
- Added a document-by-document review standard.
- Added a folder catalog.
- Added a 462-row document audit register with all rows initially marked `PENDING`.
- Updated root README navigation to expose these resources.
- Added a 2026-11-14 status-source warning to `README-先读这里.md`.
- Corrected the two unresolved links described above.

## Remaining work

- Review all remaining Markdown/text documents individually; update the register only after full content review.
- Audit the 109 workflows and their scripts, inputs, artifacts and current/superseded state.
- Audit Python/Mathematica source, tests, JSON/CSV inputs and outputs, PDF/TeX/BibTeX dependencies.
- Reconcile all stale README dates and status claims against the current authoritative status.
- Propose safe directory moves only after a complete inbound-reference scan and relocation manifest.
- Run link, import, workflow-path, checksum and LaTeX dependency checks after any migration.

No scientific calculation, numerical output, model assumption or physical conclusion was changed in this review batch.
