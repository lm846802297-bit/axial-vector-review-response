# Seventy-third review: GitHub Actions workflow-audit records

Review date: 2026-11-16  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Scope: workflow-review reports and index records that were still marked `PENDING` in the supplemental document register.

This review checks the document records against the actual workflow YAML files in `.github/workflows/`, focusing on whether the described workflow names exist and whether branch guards, manual dispatch, permissions, test steps, profile checks and output behavior are represented accurately. It does not dispatch workflows, rerun scientific calculations, or claim that static review equals a successful workflow execution.

## Individual dispositions

| Document | Outcome | Findings and disposition |
|---|---|---|
| `workflow-reviews/B13_WORKFLOW_REVIEW_BATCH_2026-11-14.md` | `PASS_WITH_NOTES` | All ten named B.13 YAML files exist. Current YAMLs have manual dispatch and branch guards; the global quadrature audit is read-only while the others archive outputs with write permission. The report was corrected during this review: `b13-local-kernel-low-mass-convergence.yml` already has an empty-staged-diff guard (`git diff --cached --quiet && exit 0)); only `b13-low-mass-global-convergence.yml` lacks a visible equivalent. The report now states this accurately. |
| `workflow-reviews/B14_B16_LOCAL_WORKFLOW_REVIEW_2026-11-14.md` | `PASS_WITH_NOTES` | All five named workflows exist. The B.14 diagnostic is indeed distinct from exact moving-muon B.13. The two directional-escape YAMLs write the same JSON path; one passes `--energy-offset 1000`, the other omits it. Both currently have empty-diff guards, but the shared output path and differing energy-argument contract remain a genuine ambiguity/race risk. One B.1 workflow checks out a named research branch rather than the triggering SHA. |
| `workflow-reviews/B16_ESCAPE_BENCHMARK_WORKFLOW_REVIEW_2026-11-14.md` | `PASS_WITH_NOTES` | All five named workflow files exist. The phase-space, emission-radius, flavor/redshift and global-redshift checks are distinct diagnostics. The vertex-preserving global Fig. 7 workflow pins the profile SHA; the other reviewed YAMLs do not visibly assert the same fingerprint. Their static success claims remain separate from axial-current acceptance. |
| `workflow-reviews/B16_HIGH_ORDER_INNER_PATH_REVIEW_2026-11-14.md` | `PASS_WITH_NOTES` | All five named workflows exist. The high-order B.14 no-recoil method is explicitly distinct from exact B.13 moving-muon Compton. The generic and vertex-preserving inner-path workflows write distinct outputs; the latter has a profile-hash assertion. The negative-(
u_mu) branch YAML has no explicit unit-test step or profile-hash assertion, so its report appropriately leaves script-level validation as a follow-up. |
| `workflow-reviews/B16_INDEPENDENT_ANALYTIC_PATH_PINNED_WORKFLOW_REVIEW_2026-11-15.md` | `PASS_WITH_NOTES` | The pinned analytic-path YAML exists and contains a branch guard, manual dispatch, unit-test step, timeout and output archival. Its report distinguishes the earlier validator-schema failure from later successful runs and does not claim that the Fig. 7 physical discrepancy or shared inputs are resolved. |
| `workflow-reviews/B16_INDEPENDENT_B1_PINNED_WORKFLOW_REVIEW_2026-11-15.md` | `PASS_WITH_NOTES` | The pinned B.1 YAML exists and has a branch guard, tests, profile/reference validation, production-output isolation and output archival. The report correctly limits the result to the thin-source integral for the adopted profile and shared kernels. |
| `workflow-reviews/B16_FULL_B1B2_PINNED_WORKFLOW_REVIEW_2026-11-15.md` | `PASS_WITH_NOTES` | The pinned full B.1+B.2 YAML exists and has a branch guard, unit tests, pinned inputs, profile/reference checks, finite-value and production-output assertions. The report's numerical comparison is explicitly conditional on shared source/profile/kernel inputs and fixed-(omega) Euclidean-chord transport; it is not full-GR transport or an axial limit. |
| `workflow-reviews/B16_HIGH_ENERGY_KERNEL_REGRESSION_REVIEW_2026-11-15.md` | `PASS_WITH_NOTES` | The read-only kernel-regression YAML exists, uses a branch guard and manual dispatch, and has a 20-minute timeout. Its 20-test result is scoped to the listed helper kernels and generic geometry tests, not a full B.16 transport run. |
| `workflow-reviews/B16_HIGH_ENERGY_STRICT_NUMPY_WORKFLOWS_REVIEW_2026-11-15.md` | `PASS_WITH_NOTES` | Both named strict-NumPy YAMLs exist. The reproduction and global-sensitivity workflows have branch guards, manual dispatch, test steps and archival write-back. Their V8 agreement is limited to the archived high-energy diagnostics; it does not remove the strong-endpoint Fig. 7 discrepancy or establish full-GR transport. |
| `workflow-reviews/B16_OUTER_PROFILE_AND_POLARIZATION_WORKFLOW_REVIEW_2026-11-15.md` | `PASS_WITH_NOTES` | All six named YAMLs exist. They use manual dispatch and research-branch guards, and archive JSON outputs with `contents: write`. The polarization workflow visibly pins the profile hash; the other reviewed YAMLs do not visibly do so. The inverse-decay pair uses a historical 501-node profile and must not be conflated with the current-profile transport baseline. The report correctly records unpinned numerical dependencies and missing test steps in two workflows. |
| `workflow-reviews/README.md` | `PASS_WITH_NOTES` | All listed review-record links resolve to files in the directory. It correctly distinguishes static workflow review from execution success and physical acceptance. The index should remain a navigation document, not a second source of status truth. |
| `workflow-reviews/WORKFLOW_REVIEW_BATCH_2_2026-11-14.md` | `PASS_WITH_NOTES` | The full 15-workflow report records a useful mixed set of historical candidates and reviewed-with-notes workflows. Its caution against deleting workflows before branch, run-history, caller and provenance checks remains appropriate. The individual entries are historical static assessments; current workflow status must be read from the live YAML and workflow register. |
| `workflow-reviews/WORKFLOW_REVIEW_BATCH_2026-11-14.md` | `PASS_WITH_NOTES` | The initial ten-workflow report is a dated first sample, not a complete inventory of all workflows. Its separation of local kernels, opacity, transport, full luminosity and physical Fig. 7 acceptance is sound. It should not be read as a current exhaustive workflow inventory. |
| `workflow-reviews/WORKFLOW_REVIEW_BATCH_2.md` | `HISTORICAL` | This is a condensed duplicate of the dated 15-workflow second-batch report. Its content is useful as a historical summary, but the dated full report is the canonical detailed record. Retain it for traceability; direct new readers to the dated full report. |

## Cross-cutting conclusions

1. The workflow-review records are static configuration audits; they are not substitutes for run-history checks, CI acceptance, or scientific validation.
2. The actual B.13/B.16 YAMLs generally use explicit branch guards and manual dispatch. Many write generated JSON back to the branch with `contents: write`; the read-only global quadrature and high-energy kernel regression lanes demonstrate a narrower alternative.
3. A confirmed ambiguity remains between `b16-directional-escape-8-15.yml` and `b16-directional-escape.yml`: both write the same output path while differing in whether `--energy-offset 1000` is supplied. This is recorded for a separate workflow fix; neither YAML was changed here.
4. The B.13 report contained one stale finding about the low-mass local-kernel workflow's empty-commit guard. The report was corrected after direct inspection of the current YAML. The low-mass global-convergence workflow still lacks a visible guard.
5. Pinned B.1/B.2 workflows provide stronger reproducibility controls, but their scientific conclusions remain conditional on shared profile, local kernels and the stated fixed-(omega) prescription. They do not close the physical Fig. 7 discrepancy or authorize axial-curve updates.
6. No workflow should be deleted or have permissions/branch guards changed based only on these static records. Such changes require a separate workflow-focused PR and run-history/caller audit.

## Execution boundary

- Fourteen workflow-review/index documents were read.
- The actual YAMLs for the B.13 batch, B.14/B.16 local and escape batches, high-order/inner-path workflows, pinned B.1/B.2 workflows, high-energy workflows and outer-profile/polarization workflows were inspected.
- No workflow was triggered and no production calculation was run.
- No workflow YAML, runner permission, branch, scientific output, manuscript, or physical constraint was changed.
- One documentation-only correction was made to the B.13 workflow review to fix its inaccurate empty-commit-guard statement.

The next batch should audit the remaining pending workflow-review summaries and README/manifest/calculation-log records, then reconcile the workflow audit register with the live 100+ workflow inventory.
