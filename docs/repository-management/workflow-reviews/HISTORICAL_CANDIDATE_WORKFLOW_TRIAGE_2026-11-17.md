# Eighty-eighth review: historical-candidate workflow triage

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `dc29c9bebdc2c184f93858294f704c9dcea7b55c`  
Scope: all 15 workflows previously labeled `HISTORICAL_CANDIDATE`. Their YAML triggers, branch guards, checkout refs, runtime, permissions, commands and write-back behavior have now been statically reviewed. Configured branch refs were checked; the four referenced branch families exist. This report does not authorize deletion.

No workflows, tests or calculations were run. The available run-history query does not expose a general branch/workflow run listing for these refs, so these 15 remain candidates rather than being declared confirmed historical or deleted. A candidate label records a disposition and a follow-up boundary; it is not a claim that a workflow is already disabled.

## Inventory and disposition

| Workflow | Current Git blob | Static scope and wiring | Disposition |
|---|---|---|---|
| `.github/workflows/b16-full-b1b2-independent.yml` | `96faad137ad0b590773a759d733774f39dbedbac` | Moving-muon branch push/manual; branch-guarded; 90-minute B.1+B.2 integration, tests, profile/baseline closure gates; writes JSON. Checkout uses branch name. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/b16-global-polarization-transport.yml` | `f0dcea586bdc8d9f2d7734b7aa9cb656836362b7` | Moving-muon push/manual; guarded; 240-minute 10 MeV polarization-resolved diagnostic with regression and closure checks; writes JSON. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/b16-p1iii-eos-full-profile.yml` | `478e5f5aed3be96e69e772df263ccf8e544ab975` | Moving-muon push/manual; guarded; downloads hash-checked Caputo/SFHo inputs, maps the dense radial profile, applies C1 gates and archives generated inputs/results. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/b2-path-energy-convergence.yml` | `636b83394f4e553e31e9c3d8b07554aff6bfa810` | Moving-muon push/manual; guarded; 120-minute three-mass path-energy/redshift convergence with tests and production isolation; archives report. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/bollig-profile-vector-audit.yml` | `6c3d27ce6854a571829b8d0a5e521f2c17dc8eee` | Moving-muon push/manual; guarded; extracts Bollig Fig. 3/4 vector paths, checks production files, commits source geometry. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/caputo-muon-density-vector-audit.yml` | `331cd8ec8dee59c0b9a1fa287cc74a973aefe58b` | Moving-muon push/manual; guarded; extracts Caputo Fig. 1 muon-density vector path, checks production files, commits audit. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/fig7-six-mass-reproduction.yml` | `b1ff3019a800a4001f0a3fef7724cce345d445bb` | Legacy codex push/manual; guarded; source-PDF digitization, six-mass scalar reproduction and boundary comparison; commits outputs. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/fig7-ultrafine-0p1.yml` | `66f74d8752da40781b9998f4a7fda45350c8aa68` | Legacy codex push/manual; guarded; 0.1 MeV ultrafine scalar scan and comparison; commits outputs. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/finite-mixing-model-map.yml` | `8f37e0e66d6841a838bc9ab1ba14ad9a5c75e733` | Legacy codex push/manual; checks out event SHA and runs finite-mixing endpoint tests; read-only permissions, no result write-back. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/major44-eft-regression.yml` | `85d9ace4bd64d0dce8cc242b4f70eac404bfaf85` | Broad codex regression/manual workflow; 90-minute tests, manifest/release verification, scans and figure regeneration; workflow-wide write access. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/moving-muon-thermal-rates.yml` | `ad3a2b8c33cf03ca67329cb0e6d63fce53d31d7b` | Moving-muon and codex branch pushes/manual; extensive thermal/matrix-element checks and scans; writes outputs. No job-level branch guard is shown. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/pr55-latex-build.yml` | `600944de52eaf41c62b2fc48bc0ad2500598d79a` | Push-only PR55 response branch; compiles, checks citations, renders pages, and pushes the PDF to that fixed branch. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/pr55-referee-letter-build.yml` | `5bfc462d4778c0917109e90891ad91e04d710a97` | Push/manual on response, codex and current maintenance branches; guarded; full LaTeX/source/PDF audit, retained artifact and PDF write-back. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/pure-vector-benchmark-audit.yml` | `4a729673e1f7bd026db0bf35f3734d43d8a94fa1` | Legacy codex push/manual; guarded; refreshes Fig. 7 comparison, validates pure-vector benchmark provenance and commits JSON. | `HISTORICAL_CANDIDATE` |
| `.github/workflows/transport-prescription-audit.yml` | `4b8f32d286f9468ddb8929f90343e082beb0c0a2` | Legacy codex push/manual; guarded; analyzes transport-prescription input and commits a comparison JSON. | `HISTORICAL_CANDIDATE` |

## Cross-cutting findings

- The `research/moving-muon-thermal-rates-20261107`, `codex/major44-axial-cooling-constraints-20261105`, `research/major1-scalar-pole-belleii-20261109`, `review/response-point-conclusions-20261106`, and current maintenance branch refs all still exist. Existence does not establish that a workflow is current or that its last run passed.
- Most candidates are manually dispatchable and several write outputs with `contents: write`; changing their status or deleting them should follow run-history and caller review.
- The branch-fixed B.1+B.2 workflow checks out a branch name instead of the event SHA. The broad Major 4.4 workflow has a wide write scope. The moving-muon workflow lacks a job-level branch guard. The old PR55 compile workflow writes to a fixed review branch, while the newer PR55/56 workflow also includes the current maintenance branch.
- Several candidates overlap with more specific successor workflows already recorded in the workflow register. Keep the historical source and outputs until commit/run provenance, callers, branch reachability and replacement coverage have been checked.

## Follow-up boundary

Static YAML review for all 115 workflows is now complete: 100 entries are `REVIEWED_WITH_NOTES`, 15 are individually documented `HISTORICAL_CANDIDATE`, and 0 remain `PENDING`. The 15 candidates are retained. This review does not convert them to `HISTORICAL`, remove them, or claim their last Actions runs were successful. Final cleanup decisions require the missing workflow-run and caller/history evidence.
