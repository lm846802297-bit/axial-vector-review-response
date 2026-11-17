# Final integration review: repository organization PR #115

Date: 2026-11-17  
Reviewed PR head: `a82d7a6b85fc0440f9a76d142890f5ce3b65f1f2`  
Base: `main` at `fbab624435c853e90e3955009a545e28c5f5be98`  
Scope: the seven baseline `REVISION_REQUIRED` records, all 14 `HISTORICAL_CANDIDATE` workflows, and the complete PR file diff.

## Closeout disposition

The repository-organization work is complete at the document and workflow-inventory level. The seven scientific/provenance issues remain explicitly open and are retained in the baseline register; the 14 candidate workflows have verified run histories and are retained because their branch triggers/manual dispatch remain live. No scientific acceptance is inferred from this closeout.

### Seven baseline items retained open

All seven paths remain `REVISION_REQUIRED`; none was silently reclassified as complete. Their missing evidence and exact closure conditions remain in [the action plan](REMAINING_BASELINE_REVISION_REQUIRED_ACTION_PLAN_2026-11-17.md).

| # | Record | Closeout disposition |
|---:|---|---|
| 1 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_ESCAPE_PHASE_SPACE_RUNBOOK_2026-11-10.md` | Retain open: the canonical high-order JSON is blocked by an energy-grid fingerprint mismatch; joint and marginal closure evidence is still required. |
| 2 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/FIG7_10MEV_LOCAL_RATE_POLARIZATION_ESCAPE_AUDIT_2026-11-13.md` | Retain open: the claimed 10 MeV producer/input/CSV/JSON/plot handoff is absent; the 210–510 MeV B.13 package is a different band. |
| 3 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/MUON_CHEMICAL_POTENTIAL_SOURCE_AUDIT_2026-11-07.md` | Retain open: public Fig. 3 does not identify whether plotted density is (n_{\mu^-}) or net (n_{\mu^-}-n_{\mu^+}); preserve both conventions and the separate B.17 source convention. |
| 4 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/PROFILE_INPUT_AUDIT_12_15KM_2026-11-09.md` | Retain open: add the profile CSV fingerprint and same-vertex/same-shell comparisons for both density definitions; keep the plotted convention unresolved if primary evidence does not settle it. |
| 5 | `research/radial-scalar-collider-recast-2026-10-28/data/derived/scan-pr52-thetaR-1e-2/SHA256SUMS.txt` | Retain open: the current decompressed CSV bytes and old reversed-bound run record have not been reconciled in Git. |
| 6 | `research/stellar-cooling-original-uv-model-20261105/validation-results-2026-11-05.md` | Retain open: the CSV producer/reference convention does not match the pinned convergence driver's output schema; keep the table legacy-scoped unless its actual producer is recovered. |
| 7 | `research/stellar-cooling-two-vev-20261105/validation-results-2026-11-05.md` | Retain open: producer/reference provenance is unresolved and (n_{\rm GL}), (n_\phi) vary together; describe the scan only as joint convergence. |

### Fourteen candidate workflow run histories

Read-only GitHub Actions run queries covered the configured branch families through 2026-11-17. The table reports the query's run count and conclusion tally for each workflow; it does not treat a successful workflow run as scientific acceptance. The four referenced branch families still exist. The 14 workflows have no runs on the current maintenance branch, but they do have recorded runs on their configured research/review branches.

| Workflow | Runs | Success / failure / cancelled / action-required | Latest recorded run (UTC) |
|---|---:|---|---|
| `.github/workflows/b16-full-b1b2-independent.yml` | 7 | 6 / 1 / 0 / 0 | [#43197376759](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43197376759), success, Nov 12 |
| `.github/workflows/b16-global-polarization-transport.yml` | 3 | 0 / 3 / 0 / 0 | [#43205614338](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43205614338), failure, Nov 12 |
| `.github/workflows/b16-p1iii-eos-full-profile.yml` | 5 | 3 / 2 / 0 / 0 | [#42960145972](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42960145972), success, Nov 11 |
| `.github/workflows/b2-path-energy-convergence.yml` | 3 | 3 / 0 / 0 / 0 | [#42585105236](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42585105236), success, Nov 9 |
| `.github/workflows/bollig-profile-vector-audit.yml` | 8 | 6 / 2 / 0 / 0 | [#42702589368](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42702589368), failure, Nov 9 |
| `.github/workflows/caputo-muon-density-vector-audit.yml` | 3 | 1 / 2 / 0 / 0 | [#42763750725](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42763750725), failure, Nov 10 |
| `.github/workflows/fig7-six-mass-reproduction.yml` | 8 | 5 / 3 / 0 / 0 | [#43125499382](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43125499382), success, Nov 12 |
| `.github/workflows/fig7-ultrafine-0p1.yml` | 1 | 1 / 0 / 0 / 0 | [#42321883610](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42321883610), success, Nov 7 |
| `.github/workflows/finite-mixing-model-map.yml` | 116 | 73 / 27 / 16 / 0 | [#43206544272](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544272), success, Nov 12 |
| `.github/workflows/major44-eft-regression.yml` | 246 | 162 / 38 / 46 / 0 | [#43206544367](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544367), success, Nov 12 |
| `.github/workflows/moving-muon-thermal-rates.yml` | 84 | 21 / 37 / 25 / 1 | [#43206544350](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544350), success, Nov 12 |
| `.github/workflows/pr55-latex-build.yml` | 10 | 5 / 4 / 1 / 0 | [#42446563788](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42446563788), success, Nov 8 |
| `.github/workflows/pure-vector-benchmark-audit.yml` | 4 | 1 / 3 / 0 / 0 | [#43125499479](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43125499479), failure, Nov 12 |
| `.github/workflows/transport-prescription-audit.yml` | 1 | 1 / 0 / 0 / 0 | [#42321549465](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42321549465), success, Nov 7 |

Total observed attempts: 499. Several workflows have failed or cancelled runs; those outcomes and dates are part of their record and are not hidden by the latest status. They remain `HISTORICAL_CANDIDATE`, not `HISTORICAL` or disabled: their configured branch refs still exist, many accept manual dispatch, and several have write-back behavior. Run-history verification is complete; external/API dispatch callers cannot be exhaustively established from repository contents, so retention is the safe recorded disposition. No candidate workflow was run during this review.

## Full PR diff review

The GitHub PR files API returned all 385 changed paths across four pages. The aggregate is 166 added, 217 modified and 2 renamed files; no files were removed. The two moves are workflow-review Markdown records relocated under `docs/repository-management/workflow-reviews/`. The diff contains 23,077 added and 731 deleted lines; the deletions occur within modified files and were reviewed as replacements, corrections, or moves, not file removals.

Key findings:

- The response-letter TeX changes move the original 2,253-character Fig. 1 caption into the immediately following explanatory paragraph. The committed audit records an exact text match and SHA-256 `3e042139e73f73b39ac42081ff494bccafe0345a1135c33eaf990cbd38d2c8c3`; the replacement figure caption is short and points readers to that paragraph. The current PDF was independently read from the PR head: SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`, 64 A4 pages, no blank pages. This review did not rerun LaTeX or re-render pages.
- The reply-letter preservation audit and PR description cite the required writing rules §§3.1, 6 and 7 and state a substantive deletion/merge ledger of “none.” No independent scientific conclusion, applicability condition, or formula is identified as deleted by the caption relocation.
- The B.1/B.2 research tree contains new audit scripts and JSON evidence, plus edits to audit drivers. Two edits are computational-method changes rather than navigation-only changes: `exact_momentum_fermion_pole_audit.py` replaces SciPy QUADPACK integration with composite Gauss–Legendre endpoint/root panels; `audit_b16_global_redshift.py` recomputes local source/absorption kernels and local vector speed along the lapse-redshift path. They are clearly scoped as diagnostics in the surrounding records, but this review did not execute their code or validate scientific acceptance.
- Workflow changes include correction of escaped GitHub Actions expressions and artifact paths in the C4-C3 workflow, plus stricter reply-letter layout gates and artifact retention. The C4-C3 workflow was not run in this review.
- Repository indexes, audit registers, checksums, and historical warnings are additions/updates; the organization diff does not delete any research file or scientific output.

## Disposition

No unexplained file deletion, unregistered move, or caption-content loss was found. Repository navigation, document dispositions, and candidate-workflow history now have a documented closeout. The seven scientific/provenance blockers remain visible and unchanged in the baseline register. This is an integration review of the PR diff, not approval of the two computational-method edits, a full numerical reproduction, or a production-physics validation. PR #115 remains open Draft pending normal review; this closeout does not merge it or advance any physics claim.

The 73 baseline fingerprint-difference flags (72 content and one size metadata) remain intentionally preserved as historical reviewed-version versus current-version fingerprints; all live blob/size metadata still match the PR Git tree. They are audit-trail distinctions, not missing inventory entries.

No tests, workflows, or physics calculations were run in this review.
