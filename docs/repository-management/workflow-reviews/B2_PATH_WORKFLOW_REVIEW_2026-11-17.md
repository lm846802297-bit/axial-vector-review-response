# Seventy-eighth review: B.2 path and source workflow wiring

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `e1f155169e2612b609c5d496fea3f022cac59143`  
Scope: four pending GitHub Actions workflows for local absorption, opacity interpolation, radial source convergence, and lapse-boundary sensitivity. Workflow YAML was compared with each referenced driver, test, input and research note.

This is a static workflow and provenance review. No workflow was dispatched, no test or calculation was run, and no scientific output was changed. Workflow completion is not treated as numerical convergence or physical acceptance.

## Inventory and findings

| Workflow | Current Git blob | Disposition |
|---|---|---|
| `.github/workflows/b16-local-absorption.yml` | `e366098d7baeef229cf9bd5072bdaf37d203e0d5` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b2-opacity-interpolation-convergence.yml` | `ff079ac4cddc1c5e89c6a3b7b284fbb955761855` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b2-radial-source-convergence.yml` | `54400a6ea7a007556560333e7858312d0af01dcd` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-lapse-boundary-sensitivity.yml` | `493b87948aaafc4b07a5172961616f5b84e58458` | `REVIEWED_WITH_NOTES` |

### B.16 local absorption

The workflow checks out the triggering SHA, restricts the job to `research/moving-muon-thermal-rates-20261107`, uses read-only contents permission and runs the named local-absorption and reference tests before a 10 MeV local audit. The script writes `outputs/b16_local_absorption_10mev_2026-11-09.json`, but the workflow neither uploads it as an artifact nor commits it. The output is therefore ephemeral in an ordinary Actions run. This is consistent with a read-only audit only if the output is intentionally disposable; otherwise add an artifact step or remove the output-producing invocation. The test code checks analytic detailed-balance and kernel identities, but those tests do not exercise B.2 transport.

### B.2 opacity interpolation

The workflow fixes source, energy, angular and path quadratures while varying the opacity interpolation grid for 0.1, 1 and 10 MeV. The driver pins the reconstructed profile SHA and separately reports its convergence assessment. The workflow validates the profile, masses, fixed quadratures and eight opacity-grid configurations, then prints each result's `overall_passed` and acceptance fields; it does not fail the job when a reported convergence assessment is false. Its path filters include the driver, redshift helper, reference module and digitized profile, but omit the default Fig. 7 input `research/stellar-cooling-constraints-20261105/outputs/vector_audit/luminosity_comparison.json`. A change to that input alone will not trigger the push workflow. Workflow-wide `contents: write` is broader than needed before the archive step, and an unchanged generated report can make `git commit` fail because no staged-diff guard is present.

### B.2 radial-source convergence

The matrix varies source radial orders 80, 100, 120, 160 and 200 for each of 0.1, 1 and 10 MeV, while fixing the opacity grid at 640 and the energy/angular/path quadratures at 100/16/32. The driver checks the reconstructed-profile SHA and records separate source, opacity and energy grid fingerprints. The workflow prints adjacent-order changes and the JSON's 1% screening target but does not assert that the target is met; a green run means the diagnostic completed, not that radial convergence passed. Its path filters also omit the default Fig. 7 input used through `audit_b16_global_redshift.py`. Workflow-wide write permission should be narrowed to the archive step. `cancel-in-progress: true` can discard a long-running matrix when a newer run starts; use non-cancelling concurrency or document why replacing an in-progress run is desired. The output commit loop handles concurrent pushes by rebasing, and the staged-diff guard avoids empty commits.

### B.16 lapse-boundary sensitivity

The workflow is branch-guarded, checks out the triggering SHA, scans three lapse continuations at 10 MeV and archives one JSON. The driver imports the global-redshift and shell-luminosity helpers and reads the default Fig. 7 luminosity comparison, but the push path filters list only the driver, profile CSV and workflow file. Changes to those imported helpers or the Fig. 7 input alone will not trigger it. The workflow grants write permission to the full job although only the archive step needs it. The driver labels the alternatives as source-sensitivity diagnostics and holds the opacity columns fixed; this does not test full GR transport or select a preferred metric.

## Cross-cutting disposition

All four jobs are branch-scoped and check out `${{ github.sha }}`. Python is fixed at 3.12, while NumPy/SciPy versions are unpinned; the referenced Actions are major-version tags rather than immutable commit SHAs. No static review here establishes that any workflow has passed its own latest run. The B.2 reports distinguish fixed-`omega` baselines from redshift-only sensitivity and record unresolved global convergence at lower masses; these workflow configurations do not close the pure-vector Fig. 7 acceptance gate.

## Follow-up

1. Add missing Fig. 7/helper dependencies to the B.2 path filters, or document another mechanism that guarantees runs when those inputs change.
2. Decide whether the local-absorption JSON is disposable or should be retained as an artifact.
3. Narrow write permission to archive jobs in the three workflows that commit outputs.
4. Add explicit failure criteria only where the workflow is intended to enforce a numerical convergence gate; otherwise label the run as diagnostic.
5. Disable cancellation for the expensive radial-source matrix unless superseding an active run is an intentional policy.
6. Pin numerical package versions and consider immutable action references for long-term provenance.

No workflow, calculation source, numerical output, opacity, luminosity, constraint curve, manuscript text or physical parameter was changed.
