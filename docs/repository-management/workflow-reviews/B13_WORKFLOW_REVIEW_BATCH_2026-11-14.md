# GitHub Actions workflow review — B.13 batch 2 (2026-11-14)

## Scope

Reviewed the complete YAML for ten B.13 workflows on `maintenance/repository-organization-audit-20261114`. Inspected triggers, branch guards, path filters, permissions, runner/Python setup, timeouts, numerical commands, assertions, output archival and production-output isolation. Confirmed that the pinned `research/moving-muon-thermal-rates-20261107` branch exists. This review did not inspect every workflow run or execute the calculations.

## Individual outcomes

| Workflow | Outcome | Review |
|---|---|---|
| `b13-exact-compton-radial.yml` | REVIEWED_WITH_NOTES | Exact B.13 radial opacity diagnostic at 10 MeV; runs thermal-rate tests and compares radial B.13 against B.16. It writes a JSON result to the research branch using `contents: write`. Branch guard is explicit. Retain the profile and source provenance in the output; reconsider write-back if artifacts suffice. |
| `b13-exact-compton-vertex-preserving.yml` | REVIEWED_WITH_NOTES | Profile-specific radial audit with an explicit SHA-256 assertion for the vertex-preserving profile. The fixed-profile fingerprint is a valuable guard. It also writes results to the branch. Keep separate from generic-profile checks; consider least-privilege artifact-only output. |
| `b13-global-convergence-audit.yml` | REVIEWED_WITH_NOTES | Read-only 360-minute global quadrature audit. Runs four orthogonal/combined scans and asserts same-grid B.16 closure and expected scan labels before uploading a 90-day artifact. Its read-only permission is appropriate. Convergence of the audit grid does not itself close the physical Fig. 7 gate. |
| `b13-global-convergence.yml` | REVIEWED_WITH_NOTES | Multi-grid B.13/B.16 comparison with nine matrix cases and an aggregate job. It commits per-grid summaries and aggregate reports, so `contents: write` is functional but broad. Concurrent matrix jobs rebase and retry; preserve the collision-handling logic and inspect actual run outcomes before changing it. |
| `b13-global-grid-convergence.yml` | REVIEWED_WITH_NOTES | Dedicated radial/energy grid scan with a pinned profile SHA, expected three configurations and production-output isolation. Writes its JSON to the branch. Keep distinct from angular/path quadrature convergence because it probes a different numerical dimension. |
| `b13-global-transport-summary.yml` | REVIEWED_WITH_NOTES | A downstream compaction workflow, not a transport calculation. It waits for three full-mass inputs and only generates summaries if all exist; manual dispatch can therefore finish without producing output when prerequisites are missing. Make that no-op state visible in the run summary. |
| `b13-global-transport-vertex-preserving.yml` | REVIEWED_WITH_NOTES | Full 0.1, 1 and 10 MeV B.13 source-and-opacity transport on a fixed profile. It checks the profile hash, mass labels, B.16 baseline residual and unchanged production axial outputs, then commits JSON outputs. These are valuable controls, but do not by themselves establish final axial SN exclusion or close the strong-absorption physical benchmark. |
| `b13-local-kernel-convergence-audit.yml` | REVIEWED_WITH_NOTES | Local 10 MeV kernel convergence and thermal-rate regression tests. This is a local-kernel gate, not a radial/global transport validation. The workflow commits the JSON output; confirm that the result needs to be durable in Git rather than retained as an artifact. |
| `b13-local-kernel-low-mass-convergence.yml` | REVIEWED_WITH_NOTES | Matrix variant for 0.1 and 1 MeV local kernels. It has similar logic to the single-mass local audit but extends mass coverage. Unlike the neighboring workflows, it does not test whether the staged diff is empty before committing; unchanged output may lead to an empty-commit failure. |
| `b13-low-mass-global-convergence.yml` | REVIEWED_WITH_NOTES | Global 0.1 and 1 MeV convergence matrix with profile and B.16 closure assertions. It has a 240-minute timeout and writes outputs to the branch. It also lacks an explicit staged-diff guard before `git commit`; add one if this workflow is maintained. Numerical convergence remains separate from physical acceptance. |

## Cross-cutting findings

1. All ten workflows are pinned to the extant `research/moving-muon-thermal-rates-20261107` branch and also allow manual dispatch; each job has an explicit branch-name guard.
2. Six workflows use `contents: write` to commit JSON or reports. This is intentional archival behavior but should be treated as an elevated permission, not a default.
3. The read-only global quadrature audit is a good least-privilege pattern: upload a versioned artifact without write access.
4. B.13 workflow names encode separate validation layers: local kernel, radial opacity, global transport, multi-grid convergence and summary generation. Do not merge them into one broad “B.13 passed” status.
5. The three-mass transport workflow explicitly verifies B.16 baseline closure and fixed-profile identity. This is an implementation/consistency check, not proof that the physical 10 MeV strong-absorption endpoint is correct.
6. Two matrix workflows omit an explicit empty-staged-diff guard before committing. This is a reliability issue to fix only in a dedicated workflow change, not silently during documentation review.

## Disposition

All ten files are marked `REVIEWED_WITH_NOTES` in the workflow register. No YAML, runner permission, trigger, branch, script or calculation was changed.
