# Eighty-second review: C4 EOS response and collision-kernel workflows

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `2416d979e083992afb3079ddf6dd89031df96442`  
Scope: six P1-IIIe C4 workflows covering dynamic EOS scalar response, effective-mass weak tensors/collision kernels, exact outgoing-energy support, and full-angle outgoing-energy/total-scattering convergence.

This is a static workflow review. No workflow, test, or numerical calculation was run. The reported acceptance assertions are code configuration only and do not constitute a new numerical result or complete B.1/B.2 transport validation.

## Inventory

| Workflow | Current Git blob | Scope | Status |
|---|---|---|---|
| `.github/workflows/b16-p1iiie-c4a-eos-dynamic-scalar-response.yml` | `62bd29005fb90c0b0e046efc5549a4fda1105b10` | C4-A EOS dynamic response, q=0 grid and sum rules | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iiie-c4b1-effective-mass-weak-tensor.yml` | `5e7b451608b963ff1697266bc6c9204aa3c2c0e4` | C4-B1 effective-mass weak-tensor and Ward checks | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iiie-c4b2-effective-mass-collision-kernel.yml` | `edb29383587df503644c5f2a452823b96b9ed28a` | C4-B2 local EOS collision-kernel rates | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iiie-c4c1-exact-outgoing-energy-support.yml` | `4c362b88ea04ade818db85eef91ca15cd177626e` | C4-C1 exact support roots and full E′ integrals | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iiie-c4c2-full-angle-eprime-convergence.yml` | `2ae7e0ad77a5748e9df255a787e5087fb97137fa` | C4-C2 full-angle E′ convergence | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-p1iiie-c4c2-full-angle-total-scattering.yml` | `cdf981cb97aa737a96da276cab63532e1de03fb6` | C4-C2 full-angle total-scattering rates and quadrature convergence | `REVIEWED_WITH_NOTES` |

## Shared workflow behavior

All six trigger on pushes to `research/moving-muon-thermal-rates-20261107` and manual dispatch, guard the job to that branch, check out the triggering commit SHA, and run on Ubuntu/Python 3.12. They grant only `contents: read`, use separate non-cancelling concurrency groups, and install unpinned NumPy/SciPy. Work is recomputed into runner-temporary directories. The workflows do not write outputs back to the research branch.

All six have focused tests and explicit in-workflow numerical assertions. Their path filters generally name the workflow, driver, focused test and direct profile/reference inputs. Artifact retention is 90 days for C4-B1, C4-B2, C4-C1 and both C4-C2 workflows. C4-A compares its generated response and sum-rule tables against committed reference files but does not upload a durable run artifact. The C4-B1 output is gated by summary/tensor/Ward limits and file-size checks but is not compared with a committed numerical golden in the workflow.

## Per-workflow checks and boundaries

- **C4-A:** reconstructs EOS dynamic response, detailed-balance/sum-rule diagnostics, and q=0 blocked/unblocked limits. The workflow checks the summary and compares 13,440 q=0 rows plus 56 sum-rule records with committed tables. This validates the encoded response computation and reference agreement at the declared grid.
- **C4-B1:** checks effective-mass Ward and tensor identities over 288 scan cases, 40 vacuum-mass recovery cases, and 8 vector/axial sign cases. It uploads JSON/CSV diagnostics. Acceptance thresholds are explicit, though the workflow does not check a committed golden output.
- **C4-B2:** reconstructs local EOS collision-kernel rates at 16 cases, four legacy-recovery cases, four cold Horowitz comparisons, and local quadrature-convergence diagnostics. It uploads the result and asserts summary acceptance and row counts.
- **C4-C1:** reconstructs exact outgoing-energy support, support roots, 16 local cases and four cold-limit cases. It checks root residuals, two E′ order-comparison thresholds, and the expected row counts, then uploads outputs.
- **C4-C2 E′ convergence:** checks 16 full-angle E′ cases, positive rates, support-root residuals, and the 48-to-72 quadrature comparison, then uploads the result.
- **C4-C2 total scattering:** checks selected radii, 16 local rates, four cold-limit cases, angular convergence, and kernel-order convergence, with explicit Horowitz and convergence limits, then uploads outputs.

These workstreams progressively add EOS response and scattering ingredients. Their individual acceptance checks do not by themselves establish a converged radial B.1 source, a full B.2 optical-depth calculation, Fig. 7 reproduction, or a physical SN1987A exclusion.

## Maintenance notes

- Keep each path filter synchronized with the shared stationary trace, moving Fermi-gas kernel, EOS occupation implementation, profile and C2 reference. The current filters include the explicitly named shared drivers and data paths.
- Pin numerical packages and action versions if bitwise/reproducible reruns are required; current action references use version tags and NumPy/SciPy are installed unpinned.
- Preserve the output artifacts for the four workflows that already upload them. Add equivalent artifact retention to C4-A if future review needs the per-run tables.
- Treat C4-B1 threshold success as a local tensor/Ward gate, not an independent numerical golden comparison or full physical acceptance.
