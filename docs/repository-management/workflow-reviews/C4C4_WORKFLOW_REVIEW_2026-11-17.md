# Seventy-seventh review: C4-C4 workflow wiring and archival boundaries

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `bad740f00537db341f91d43848cbec8b052c0878`  
Scope: the three C4-C4 Actions workflows, their branch and path triggers, test/compute/archive stages, permissions, and links to the current C4-C4 research records.

This is a static workflow and provenance review. No workflow was dispatched, no tests or calculations were run, and no scientific output was changed. The existing C4-C4 reports describe local-scattering and quadrature checks; this review does not independently reproduce those results or promote them to transport or supernova-cooling acceptance.

## Workflow inventory

| Workflow | Current Git blob | Trigger and reviewed scope |
|---|---|---|
| `.github/workflows/b16-p1iiie-c4c4-energy-dependence.yml` | `e130b0814fc2b598e5672119481122a9644481f5` | Push to `research/c4c4-energy-dependence-20261112` with a path filter; five incident-energy jobs, merge/validation, artifact upload and branch archive commit. |
| `.github/workflows/b16-p1iiie-c4c4-quadrature-convergence.yml` | `86a8a7fec115ddf6e8b137d9645f326ff8c472be` | Push to the same branch with a path filter; five high-order energy shards, merge, convergence-summary gate, artifact upload and branch archive commit. |
| `.github/workflows/b16-p1iiie-c4c4b-full-radial-energy-dependence.yml` | `ee4b593c9d072ce0d8637dc61de6f00f4b3cc5ac` | Push to the same branch with a path filter and `workflow_dispatch`; 25 energy/radial shards, merge checks, archive artifact and branch archive commit. The target branch currently exists at `6bcfbee90543543bd8b0d3c7422cf2c3f1c431da`, and the referenced output directory contains a README and checksum manifest. This was listed as a historical candidate in the prior inventory; the existing branch/workflow/output evidence supports reviewing it as a current workflow record. |

## Findings

### C4-C4-A anchor scan

- The workflow runs the named C4-C4-A unit-test module before computation, then scans 10, 20, 40, 60 and 150 MeV across a five-job energy matrix. Its merge command receives the generated shards and records `GITHUB_SHA`; the archive is uploaded and committed under the dated C4-C4-A output directory.
- Every job checks the target branch name. The workflow has no manual-dispatch trigger, so recovery currently depends on a qualifying push to the research branch.
- The workflow grants `contents: write` at workflow scope, including to test and compute jobs. The archive-commit stage needs write access; the earlier jobs do not visibly need it. Consider narrowing the token permission to the archive job.
- NumPy and SciPy are installed without version pins. The workflow does not install a repository requirements file. Runtime variation can therefore affect repeatability even though the source checkout is pinned to the triggering commit.
- The workflow's path filter names its driver, test, report, kernel dependencies and the pinned profile/occupation inputs. No physical transport or literature-reproduction gate is asserted by the workflow.

### C4-C4-Aq quadrature comparison

- The workflow runs the named convergence tests, compares five energy shards at base and combined higher quadrature orders, merges the 80 comparisons and invokes the explicit summary gate after archiving the generated diagnostic.
- Every job checks the target branch. Like C4-C4-A, it has no `workflow_dispatch` trigger and installs unpinned NumPy/SciPy under a workflow-wide write permission.
- The archive-before-gate ordering preserves diagnostic output even when the convergence threshold fails. This is appropriate for auditability; the archived result must still be labeled by the actual gate result.

### C4-C4-B full-radial scan

- The workflow has a test stage, 25 shards (five energies by five radial shards), an explicit merge/check command, 30-day shard artifacts and a 90-day merged artifact. The research note identifies the bounded 301-point, fixed-local-energy calculation and distinguishes the stratified 340-case higher-order check from pointwise convergence at all radii.
- Unlike the two A-stage workflows, the manual-dispatch path has no job-level branch guard. A manual run selected from another branch could compute against different files and, because the merge job commits with `contents: write`, archive results onto that selected branch. Add a branch-name guard to every job before using manual dispatch for recovery.
- `concurrency.cancel-in-progress: true` can cancel an earlier same-ref full-radial run when another run starts. That can discard in-progress shard work; consider disabling cancellation for this expensive archival workflow.
- As in the A-stage workflows, `contents: write` is declared at workflow scope and NumPy/SciPy/Numba are installed without version pins. Narrow write permission to the archive job and pin the runtime dependencies used for archived numerical results.

## Document and provenance cross-check

The three YAML files, their named scripts/tests, C4-C4 reports and the current C4-C4-B output README/checksum manifest are present in the reviewed branch. The research records state that C4-C4-A has 96 anchor cases, C4-C4-Aq compares 80 newly computed rows, and C4-C4-B extends the diagnostic to 301 radii. Those are statements from the linked records; this workflow-only review did not recompute their counts or checksums.

The current research notes limit C4-C4-B to fixed-local-energy, flat-space local scattering and radial optical-depth diagnostics. They do not establish gravitational redshift, energy redistribution, angular transport, escape probabilities, supernova luminosity, or reproduction of Blinov Fig. 7. The workflow review does not change that scientific boundary.

## Dispositions

| Workflow | Outcome | Reason |
|---|---|---|
| C4-C4-A energy dependence | `REVIEWED_WITH_NOTES` | Trigger, branch guards, matrix, tests, artifacts and write-back path are represented; permissions and dependency pins should be narrowed. |
| C4-C4-Aq quadrature convergence | `REVIEWED_WITH_NOTES` | Explicit post-archive convergence gate is present; permissions and dependency pins should be narrowed. |
| C4-C4-B full-radial energy dependence | `REVIEWED_WITH_NOTES` | The archival stages and target branch are identifiable; manual dispatch needs a branch guard and cancellation/permissions/dependency choices need follow-up. |

These dispositions mean the workflow files and their described behavior were statically reviewed. They do not mean any workflow passed, any archived numerical output was independently validated, or the physical C4-C4 calculation is accepted.

## Follow-up

1. Add a target-branch guard to all C4-C4-B jobs before relying on manual dispatch.
2. Consider setting `contents: read` by default and granting `contents: write` only to archive-commit jobs.
3. Pin the Python numerical dependencies or document the intended lock/requirements file.
4. Keep C4-C4's local scattering and fixed-local-energy radial diagnostic separate from B.2 GR transport and the Blinov Fig. 7 acceptance gate.

No workflow, calculation source, numerical output, opacity, luminosity, constraint curve, manuscript text or physical parameter was changed.
