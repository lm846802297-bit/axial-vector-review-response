# GitHub Actions workflow review — B.16 high-order and inner-path batch (2026-11-14)

## Scope

Reviewed five complete workflow YAML files, including matrix dimensions, input dependencies, grid/profile assertions, tests, checkout SHA, permissions and output commits. No workflows or calculations were executed or modified.

## Individual outcomes

| Workflow | Outcome | Findings |
|---|---|---|
| `b16-high-order-independent-grid.yml` | REVIEWED_WITH_NOTES | Runs independent source/opacity grids at 0.1, 1 and 10 MeV with 200 radial/energy nodes, 640 opacity nodes, 32 angular nodes and 64 path nodes. It asserts grid identities, profile hash and the stated B.14 nonrelativistic-muon/no-recoil method. This must remain distinct from the exact B.13 moving-muon Compton path. |
| `b16-independent-grid-quadrature-convergence.yml` | REVIEWED_WITH_NOTES | Varies energy, angular and path orders around the independent-grid high-order baseline at three masses. It checks grid identity and finite diagnostics. It depends on baseline JSON files already in the branch; verify that they were generated from the same source commit and current profile before manual dispatch. |
| `b16-inner-numu-branch-sensitivity.yml` | REVIEWED_WITH_NOTES | Studies the negative muon-neutrino branch for 8–12 km inner sources at 10 MeV and archives both JSON and Markdown. The YAML has no explicit unit-test step, profile SHA check or finite-value assertion; confirm whether these are enforced in the script/report before relying on the result. |
| `b16-inner-path-channel-directional.yml` | REVIEWED_WITH_NOTES | Analytic inner-path channel×shell×direction audit, with tests, direct path order 256 versus legacy 32, energy offset 1000 and production-output isolation. It writes a generic-profile result. |
| `b16-inner-path-vertex-preserving.yml` | REVIEWED_WITH_NOTES | Runs the same path/channel/direction calculation against a vertex-preserving profile, adds a SHA-256 assertion and writes a distinct profile-specific output. This is a good separation of profile-specific provenance from the generic-profile audit. |

## Cross-cutting findings

1. The independent-grid high-order workflow explicitly labels the B.14 no-recoil approximation. That method label is important: a high-order grid does not remove a physical approximation in the kernel.
2. The quadrature-convergence workflow is only as reproducible as its archived baseline inputs. Its dependencies should be recorded by exact blob hashes or source commit, not only filenames.
3. The two inner-path workflows are complementary, not duplicates: one is generic-profile and one pins the vertex-preserving profile. Their outputs must not overwrite each other.
4. The inner muon-neutrino branch sensitivity YAML has a lighter explicit validation envelope than the neighboring workflows. The script's own validation must be inspected before this entry can be upgraded beyond REVIEWED_WITH_NOTES.
5. All five workflows use `contents: write` for durable branch archival; keep this as a deliberate permission and not a blanket default.

## Disposition

All five entries were marked `REVIEWED_WITH_NOTES`. No scientific source, output, branch, workflow or physical conclusion was modified.
