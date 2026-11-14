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

## Research workstream rules

1. Keep distinct physical models in separate directories (in particular, original one-VEV and two-VEV extensions).
2. Keep source code, immutable inputs, generated outputs, tests and reports distinguishable.
3. Every numerical result must identify source commit, input provenance, parameter point, command, environment and validation status.
4. Do not overwrite a validated result with an older branch copy or a result produced under different conventions.
5. A passing software test is not equivalent to physical validation or a phenomenological exclusion.
6. Preserve original PDFs, raw source data and historical snapshots; add a reviewed/current pointer instead of silently replacing them.

## Document status vocabulary

- `CURRENT`: reviewed and designated as a current authoritative entry.
- `REVIEWED`: content and links checked; no blocking issue found within the stated review scope.
- `REVISE`: actionable content, consistency, citation or navigation issue found.
- `HISTORICAL`: intentionally retained snapshot; not a current instruction or result.
- `DUPLICATE_CANDIDATE`: possible duplicate; compare content and provenance before removal.
- `PENDING`: not yet individually reviewed.
- `NOT_APPLICABLE`: non-prose artifact or generated output; use its own artifact validation record.

## Safe migration policy

Do not move or delete files solely from their names. Before a move, search and update inbound relative links, code imports, workflow paths, LaTeX inputs, scripts, manifests and external handoff instructions. Keep a relocation manifest mapping old path to new path and preserve blob hashes where bytes are unchanged.
