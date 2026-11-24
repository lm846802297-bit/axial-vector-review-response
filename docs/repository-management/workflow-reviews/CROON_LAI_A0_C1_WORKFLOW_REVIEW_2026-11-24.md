# Croon/Lai A0/C1 workflow review — 2026-11-24

## Review scope

Static review of the 15 workflow files introduced by PR #123, at branch commit `caf9d8be4bbc04fb2146e98e51e7adf1dcae4b95`. This review covers triggers, branch/path filters, job guards, permissions, dependency/runtime declarations, output write-back, and known Actions run evidence. Static review is not a scientific acceptance statement.

## Findings

- All 15 workflows were inspected individually.
- 10 workflows request `contents: write`. All 10 now have an exact job-level guard for `refs/heads/research/croon-vector-benchmark-and-rate-corrections-20261119`; a manual dispatch from another branch skips the job.
- The 5 read-only workflows use `contents: read`.
- No workflow has a `pull_request` trigger. Push-triggered workflows are restricted to the dedicated research branch and/or explicit path filters.
- Four write-enabled workflows were missing an exact job-level branch guard. These were fixed:
  - `croon-c1-10mev-high-order.yml`
  - `croon-c1-10mev-single-baseline.yml`
  - `croon-c1-adaptive-radial-output-audit.yml`
  - `croon-c1-b13-vector-transport.yml`
- The high-order and single-baseline workflows previously had push filters that only matched their own workflow files. Those ineffective/expensive push triggers were removed; both are now manual-only and branch-guarded.
- The adaptive radial output audit no longer triggers merely because its own workflow YAML is edited; it retains source/output path triggers and a branch guard.
- Write-enabled jobs still hold `contents: write` for the full job rather than using a separate read-only compute job plus a minimal archive job. This is recorded as a least-privilege improvement, not silently described as fully separated.
- Most numerical workflows pin Python 3.13, NumPy 2.5.5 and SciPy 1.18.1. Two read-only regression workflows install unpinned dependencies (`croon-semcompton-rate-regression.yml`: NumPy/SciPy/PyMuPDF; `original-uv-goldstone-ward-regression.yml`: NumPy). Their run environment is therefore not fully locked.
- Actions are referenced by major tags (`checkout@v4`, `setup-python@v5`, `upload-artifact@v4`), not immutable action SHAs.

## Per-workflow disposition

| Workflow | Trigger / permission | Static finding | Latest evidence |
|---|---|---|---|
| `a0-spinor-stability-tests.yml` | push + workflow_dispatch; contents: read | Path-filtered push on research branch; read-only test lane. | Run #44682747697 PASS: 19 A0/C1 tests, 12 thermal-rate tests, 6 explicit-spinor tests. |
| `croon-a0-10mev-adaptive-energy-convergence.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; baseline-ready gate can defer computation. | Run #44673753335 PASS (earlier revision); output acceptance is an A0 interior-profile benchmark. |
| `croon-a0-10mev-adaptive-radial-convergence.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; computes radial refinement. | Run #44671688630 PASS (earlier revision); preserve its reported radial comparison and provenance. |
| `croon-a0-uv-axial-transport.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; A0 interior-profile axial transport. | Run #44681748661 PASS: 101-node A0 interior-profile transport; outer 25–100 km opacity remains unavailable. |
| `croon-c1-10mev-adaptive-energy-convergence.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; computes 32/48 energy-order comparison. | Run #45229265669 PASS: maximum 32/48 energy-order metric 1.3031065e-7; 153 radial nodes. |
| `croon-c1-10mev-adaptive-radial-baseline.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; 103/153 radial comparison. | Run #44650913407 PASS: 103/153 radial comparison; PR reports maximum relevant difference 0.11693%. |
| `croon-c1-10mev-grid-convergence.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; grid convergence benchmark. | Run #44588729217 PASS (earlier revision). |
| `croon-c1-10mev-high-order.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only after review fix; exact branch guard; compute/writeback lane. | Run #45296685605 was in progress at review time; do not claim completion. |
| `croon-c1-10mev-result-archive.yml` | workflow_dispatch; contents: read | Manual-only; read-only archive/schema/integrity validation. | No workflow run located in the inspected branch history; static validation workflow only. |
| `croon-c1-10mev-single-baseline.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only after review fix; exact branch guard; isolated single-mass run. | Run #45296692143 was in progress at review time; do not claim completion. |
| `croon-c1-adaptive-radial-output-audit.yml` | push + workflow_dispatch; contents: write; exact branch guard | Path-filtered push plus manual; exact branch guard; post-processes archived radial outputs. | Run #45296697349 PASS on the guarded revision. |
| `croon-c1-b13-vector-transport.yml` | workflow_dispatch; contents: write; exact branch guard | Manual-only; exact branch guard; compute/writeback lane. | No workflow run located in the inspected branch history; manual compute lane. |
| `croon-semcompton-rate-regression.yml` | push + workflow_dispatch; contents: read | Path-filtered push plus manual; read-only; NumPy/SciPy/PyMuPDF versions unpinned. | No workflow run located in the inspected branch history; dependency versions remain unpinned. |
| `export-a0-energy-source-bundle.yml` | push; contents: read | Path-filtered push; read-only; exports a 14-day source-bundle artifact for local computation. | Runs #45292814610, #45292809288 and #45292803011 PASS; source-bundle export only. |
| `original-uv-goldstone-ward-regression.yml` | push + workflow_dispatch; contents: read | Path-filtered push plus manual; read-only; NumPy version unpinned. | Run #45232538324 PASS: 7 tests; vector/axial Ward residuals 2.252e-9 / 2.159e-9. |

## Scientific interpretation boundaries

- C1 is a pure-vector 10 MeV benchmark. The 153-node/48-energy result is a partial interior-profile transport result; the outer 25–100 km semi-Compton opacity is not included. It is not a final SN1987A exclusion curve and is not an axial-vector constraint.
- A0 is the separate original-UV finite-mixing axial benchmark. Its archived 101/153-node and energy-order comparisons do not supply the missing outer opacity and do not update the final axial-vector constraint.
- Croon Fig. 2 literal transport retains an unresolved outer muon-opacity/profile gap. The literal target convention and the separate antimuon sensitivity must remain distinct.
- Lai 2024 checks are equation-level and thin-shell plateau comparisons, not a full Fig. 4 luminosity reproduction.
- The historical Blinov Fig. 7 10 MeV discrepancy remains +92.4284%; none of these Croon/Lai workflows authorizes an opacity rescaling or an axial-vector constraint update.

## Remaining workflow improvements

1. Split the 10 write-enabled workflows into read-only compute jobs and minimal, separately permissioned archive jobs where practical.
2. Pin NumPy/SciPy/PyMuPDF in the two read-only regression workflows before treating their environment as reproducible.
3. Pin third-party Actions to immutable commit SHAs in a separate maintenance change.
4. Reassess the two in-progress runs before assigning a final execution status.

## Disposition

All 15 YAML files have received individual static review and are registered as `REVIEWED_WITH_NOTES`. This status records the workflow design review only; it does not claim that every workflow has run successfully or that any physical result has passed its independent scientific acceptance gate.
