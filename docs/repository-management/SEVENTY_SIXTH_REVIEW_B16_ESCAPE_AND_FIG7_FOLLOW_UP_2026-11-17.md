# Seventy-sixth review: B.16 escape phase space and 10 MeV Fig. 7 follow-up

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Scope: two baseline documents whose `REVISION_REQUIRED` status depends on reproducible B.16 escape-phase-space output and a complete 10 MeV local-rate/polarization/escape artifact package.

This is a source/document and existing-workflow-log review. It does not execute the failed calculation again or replace the existing physical benchmark.

## 1. B.16 escape phase-space runbook

Document: `research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_ESCAPE_PHASE_SPACE_RUNBOOK_2026-11-10.md`

The existing workflow `.github/workflows/b16-escape-phase-space.yml` does contain an explicit acceptance step that reconstructs all one-dimensional marginals from the full joint radius-energy-direction table and checks both regional and global source/escape fractions. The earlier runbook wording that no such joint-table assertion existed in the inspected driver/tests was too narrow; the workflow is the explicit CI checker.

The latest inspected run is [GitHub Actions run 43205614274](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43205614274), run #12, on commit `f19a4485a19f1d862d9dcd6f7703bc72259566ae` (2026-11-12). Its three phase-space binning tests passed and the driver compiled. The high-order computation then failed before producing the canonical JSON because the generated energy-grid hash did not match the archived B.16 baseline:

| Grid | Expected SHA-256 | Actual SHA-256 | Result |
|---|---|---|---|
| Source | `1a007702d1f7c8b81200e648a763f7f1a0e3565a39d57c8174dada5aad1a4cb5` | same | Match |
| Opacity | `6701fc3fe06bf07879612e591ae62c494f673928bc18f169d4b6f3fabed7d378` | same | Match |
| Energy | `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3` | `db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639` | Mismatch |

No workflow artifacts were uploaded. The strict Python output `outputs/b16_escape_phase_space_10mev_2026-11-10.json` remains absent; the V8 cross-runtime JSON is not a replacement. The run log records Python 3.12.16, NumPy 2.5.4 and SciPy 1.18.1, but the workflow requests Python 3.12 and installs unpinned `numpy scipy` instead of consuming `requirements-b16-audit.txt`.

**Disposition: `REVISION_REQUIRED` remains.** The joint-table acceptance criterion exists, but the workflow never reached it. The next repair is to reconcile the energy-grid construction with the archived high-order baseline, use a pinned runtime, rerun the strict Python driver, and archive its JSON only after the joint-table checks pass.

## 2. 10 MeV local-rate/polarization/escape audit

Document: `research/stellar-cooling-constraints-20261105/blinov_reproduction/FIG7_10MEV_LOCAL_RATE_POLARIZATION_ESCAPE_AUDIT_2026-11-13.md`

A later, separate exact-B.13 package is now archived under `blinov_reproduction/results/P1B_B2_EXACT_B13_2026-11-14/`. It contains a 42-point local polarization audit and a fixed-(omega) global transport comparison restricted to 210–510 MeV. The B.16 scalar high-energy-band baseline is reproduced at relative residual (-1.01\times10^{-7}). The low-(x) pilot completed 7 of 24 planned points; the package explicitly says full-band Fig. 7 transport, the full-profile low-(x) extension, GR-redshifted path energy, the SN1987A limit and the axial exclusion curve are not complete.

This later B.13 band result is relevant context but does not provide the specific missing 10 MeV local-rate/polarization/escape addendum package. The original audit still lacks a single reproducible set of its producer, selected-node CSV, audit JSON, plot, pinned inputs and helper source. It is therefore not valid to substitute the 210–510 MeV B.13 result for the missing local-rate audit or for full Fig. 7 validation.

**Disposition: `REVISION_REQUIRED` remains.** The report now explicitly cross-references the later B.13 evidence and states the non-supersession boundary.

## Cross-cutting outcome

- The explicit joint-table closure checker in the B.16 workflow is confirmed to exist.
- The latest B.16 escape workflow run failed before producing its canonical JSON because of the energy-grid hash mismatch; no artifacts were uploaded.
- The later B.13 high-energy package is a bounded result, not a full-band Fig. 7 replacement.
- Both baseline documents remain `REVISION_REQUIRED`; their review scopes have been updated with this new evidence.
- No production calculation, transport scan, rate, opacity, luminosity, escape fraction, constraint curve, manuscript source or model parameter was changed.
- No GitHub Actions workflow was triggered in this review.

At the time of the initial review, this report was supplemental item 119 and eight baseline `REVISION_REQUIRED` entries remained. Subsequent archive reclassification and the strict B.16 follow-up changed the live baseline queue; the current count is six, as recorded in the updated action plan.


## Post-review update — strict B.16 phase-space evidence (2026-11-17)

This addendum supersedes the B.16 runbook disposition above; it does not supersede the separate Fig. 7 local-rate/polarization/escape finding.

The strict Python phase-space calculation was subsequently run on the diagnostic branch with pinned Python 3.12.16, NumPy 2.5.4, and SciPy 1.18.1:

- [Energy-grid identity run #44054718118](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44054718118) passed. The high-order, phase-space, and independent CSV-lapse constructions all reproduce the archived 842-node energy grid SHA-256 `036e6d77...`; source and opacity grid hashes and the profile fingerprint also match.
- [Strict phase-space run #44059347513](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44059347513) passed. The canonical JSON is committed in the PR branch and the full non-empty joint radius-energy-direction table closes against its regional and global source/escape fractions.
- Luminosity, optically thin source, and escape-probability residuals against the archived high-order baseline are \(-2.22\times10^{-16}\), \(0\), and \(-5.42\times10^{-20}\), respectively. The maximum reconstructed joint-to-marginal residual is \(6.66\times10^{-16}\).
- The 8–15 km region contributes 79.6522% of the global B.1 source and 86.8551% of the escaped luminosity.

The first post-review acceptance attempt exposed a validator edge case: the sparse joint table intentionally omits the 10–11 MeV energy bin in the 8–15 km region because both stored marginal weights are exactly zero. The validator now accepts an omitted bin only when its one-dimensional marginal is exactly zero; missing non-zero bins and unexpected labels still fail. Dedicated regression tests pass.

The old failed-run energy hash `db6f613c...` was not reproduced by the current-main identity diagnostic or final production run. Its exact historical trigger remains unknown; no baseline hash was changed.

**Updated disposition:**

- `B16_ESCAPE_PHASE_SPACE_RUNBOOK_2026-11-10.md`: `PASS_WITH_NOTES`. The phase-space decomposition is accepted against the archived high-order baseline.
- `FIG7_10MEV_LOCAL_RATE_POLARIZATION_ESCAPE_AUDIT_2026-11-13.md`: remains `REVISION_REQUIRED`. The calculated 10 MeV luminosity is still +92.4284% above the digitized Fig. 7 reference, and the dedicated local-rate/polarization evidence package remains incomplete.

The baseline audit register and six-item action plan are updated in the same PR. No axial-vector rate, opacity normalization, physical convention, constraint curve, or manuscript source was changed.
