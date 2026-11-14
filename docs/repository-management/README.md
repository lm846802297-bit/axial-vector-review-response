# Repository structure and navigation

This document describes the current repository organization and the intended ownership of each area. It is an organizational map, not a claim that every file has passed scientific review.

## Canonical top-level layout

| Path | Responsibility | Rules |
|---|---|---|
| `README.md`, `README-先读这里.md` | Project entry points | Keep short; link to authoritative sources rather than duplicating status. |
| `AGENTS.md` | Mandatory contributor/agent rules | Normative workflow instructions. |
| `PROJECT_STATUS.md` | Current project status | Single current status source; dated historical snapshots must be labeled. |
| `GIT_MERGE_POLICY.md` | Research history and merge policy | Preserve scientific provenance. |
| `research/` | Scientific workstreams, calculations, validation and evidence | Each workstream owns a README, inputs, code, tests, outputs and limitations. |
| `审稿意见-gpt/` | Referee-response analysis, writing rules, meeting records and revision history | Separate reviewer-facing text from internal notes. |
| `deliverables/` | Extracted, directly usable handoff files | Preserve manifests and extraction provenance. |
| `archive/` | Frozen historical packages and snapshots | Read-only unless a new dated snapshot is explicitly created. |
| `overleaf-source/` | Pinned manuscript source snapshots | Treat as source archives; do not silently overwrite. |
| `计算脚本/` | Legacy calculation materials and their audit records | Preserve historical paths until cross-references are migrated. |
| `work/` | Temporary or intermediate working material | Never treat as authoritative without promotion and review. |
| `.github/workflows/` | Reproducible automation | Each workflow must identify its scientific scope, inputs, outputs and acceptance criteria. |

工作流 YAML 保留在 `.github/workflows/`；静态审查报告现集中于 [workflow-reviews](workflow-reviews/README.md)，迁移清单记录原路径和文件哈希。历史工作目录、附件和已停用材料分别见 [work](../../work/README.md)、[附件](../../附件/README.md)、[弃用](../../弃用/README.md)。

## Research workstream rules

1. Keep distinct physical models in separate directories (in particular, original one-VEV and two-VEV extensions).
2. Keep source code, immutable inputs, generated outputs, tests and reports distinguishable.
3. Every numerical result must identify source commit, input provenance, parameter point, command, environment and validation status.
4. Do not overwrite a validated result with an older branch copy or a result produced under different conventions.
5. A passing software test is not equivalent to physical validation or a phenomenological exclusion.
6. Preserve original PDFs, raw source data and historical snapshots; add a reviewed/current pointer instead of silently replacing them.

## Review coverage and reports

The baseline inventory contains 462 Markdown/text documents. Current register counts are: 61 `PASS_WITH_NOTES`, 1 `PASS`, 5 `REVISION_REQUIRED`, 38 `HISTORICAL`, and 357 `PENDING` (105 individually reviewed). Only documents read individually are assigned a non-pending review outcome. See the [audit register](DOCUMENT_AUDIT_REGISTER.csv) and the dated review reports:

- [Initial governance and entry review](INITIAL_REVIEW_REPORT_2026-11-14.md)
- [Second review batch](SECOND_REVIEW_REPORT_2026-11-14.md)
- [Third workstream review](THIRD_REVIEW_REPORT_2026-11-14.md)
- [Major 1 derivation review](FOURTH_REVIEW_REPORT_MAJOR1_2026-11-14.md)
- [Referee and neutrino history review](FIFTH_REVIEW_REPORT_REFEREE_NEUTRINO_2026-11-14.md)
- [Major 1 portal reference review](SIXTH_REVIEW_REPORT_MAJOR1_PORTAL_2026-11-14.md)
- [Root-file and build-dependency review](ROOT_FILE_AUDIT_REPORT_2026-11-14.md)
- [Navigation, workflow catalog and reply archive review](EIGHTH_REVIEW_REPORT_NAVIGATION_ARCHIVE_2026-11-14.md)
- [PR template and coherent spectral-area diagnostic review](NINTH_REVIEW_SPECTRAL_AREA_2026-11-14.md)
- [Historical attachment review](TENTH_REVIEW_ATTACHMENTS_2026-11-14.md)
- [Manifest and checksum review](MANIFEST_REVIEW_2026-11-14.md)
- [Legacy calculation-log review](LEGACY_LOG_REVIEW_2026-11-14.md)
- [Root PDF extraction audit](ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md) (supplementary technical audit)
- [Link and relocation audit](LINK_AND_RELOCATION_AUDIT_2026-11-14.md) (supplementary technical audit)

The 462-row register covers Markdown/text documents. Root-level TeX, BibTeX, bibliography styles and binary PDFs are additionally covered by the [root-file audit report](ROOT_FILE_AUDIT_REPORT_2026-11-14.md); workflow YAML files are covered by the separate workflow register.

## Status vocabulary

**Review outcome** (what the individual review established):
- `PASS`: all applicable checks completed within the recorded scope.
- `PASS_WITH_NOTES`: usable within scope, with caveats recorded.
- `REVISION_REQUIRED`: actionable content, consistency, citation or formatting issue found.
- `BLOCKED`: cannot validate because required source, data or context is unavailable.
- `HISTORICAL`: retained as historical material; not a current instruction/result.
- `PENDING`: inventory only; no individual content review completed.

**Lifecycle/authority** (a separate property): current authoritative, working draft, superseded, duplicate candidate, archival, or generated. A document may be historically important while still having a revision-required formatting issue; do not conflate lifecycle with review outcome.

## Safe migration policy

Do not move or delete files solely from their names. Before a move, search and update inbound relative links, code imports, workflow paths, LaTeX inputs, scripts, manifests and external handoff instructions. Keep a relocation manifest mapping old path to new path and preserve blob hashes where bytes are unchanged.

- [Portal A2–A3 individual review](ELEVENTH_REVIEW_PORTAL_A2_A3_2026-11-15.md)
- [C4-C3/C4-C4 individual archive review](TWELFTH_REVIEW_C4C3_C4C4_2026-11-15.md)
- [C4-C4 research-report review](THIRTEENTH_REVIEW_C4C4_REPORTS_2026-11-15.md)
- [Global-06 individual protocol review](FOURTEENTH_REVIEW_GLOBAL06_2026-11-15.md)
- [Portal A4–A5 output review](FIFTEENTH_REVIEW_PORTAL_A4_A5_2026-11-15.md)
- [Portal A4–A5 research-note review](SIXTEENTH_REVIEW_PORTAL_A4_A5_NOTES_2026-11-15.md)
- [Portal A5b/B5 output review](SEVENTEENTH_REVIEW_PORTAL_B5_OUTPUTS_2026-11-15.md)
- [B5 triplet output review](EIGHTEENTH_REVIEW_TRIPLET_OUTPUTS_2026-11-15.md)
- [B5 triplet research-note review](NINETEENTH_REVIEW_TRIPLET_NOTES_2026-11-15.md)
- [B.16 sensitivity note review](TWENTIETH_REVIEW_B16_SENSITIVITY_2026-11-15.md)
- [Profile provenance and B.2 interpolation review](TWENTY_FIRST_REVIEW_PROFILE_PROVENANCE_2026-11-15.md)
- [Belle II scan logs and metadata review](TWENTY_SECOND_REVIEW_BELLE_SCAN_LOGS_2026-11-15.md)
- [Belle II raw supplement review](TWENTY_THIRD_REVIEW_BELLE_SUPPLEMENTS_2026-11-15.md)
