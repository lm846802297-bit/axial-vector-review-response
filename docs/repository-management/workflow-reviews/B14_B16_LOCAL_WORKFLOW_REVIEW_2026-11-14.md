# GitHub Actions workflow review — B.14/B.16 local batch (2026-11-14)

## Scope

Reviewed five complete workflow definitions. This was a static YAML review of triggers, branch guards, checkout refs, permissions, numerical commands, output paths, assertions and archival behavior. No workflow was executed or modified.

## Individual outcomes

| Workflow | Outcome | Findings |
|---|---|---|
| `b13-muon-velocity-diagnostic.yml` | REVIEWED_WITH_NOTES | Despite its filename, the workflow is named and executes the B.14 nonrelativistic muon diagnostic. It computes source-weighted velocity moments and shell fractions, checks physical bounds and compares shell fractions with the B.16 baseline. It writes JSON back to the research branch. Keep it as an approximation diagnostic, not a substitute for exact moving-muon Compton rates. |
| `b16-b1-independent-source.yml` | REVIEWED_WITH_NOTES | Independent thin-source B.1 integration with radial, energy and high-energy-tail convergence checks, channel closure, local-vs-infinity energy-variable comparison, and production-output isolation. It uses `contents: write` to commit JSON. Its checkout step hard-codes the research branch rather than checking out `${{ github.sha }}`; this means a rerun or manual dispatch may not use the exact event commit. Pin the triggering SHA if this workflow remains active. |
| `b16-dense-local-kernel-audit.yml` | REVIEWED_WITH_NOTES | Dense 200×320 local grid (64,000 radius-energy points) with production residual thresholds, sign-invariance, angular quadrature and finite-value assertions. Writes a machine-readable result. This is strong local-kernel evidence, but must not be described as global transport or a final SN exclusion. |
| `b16-directional-escape-8-15.yml` | REVIEWED_WITH_NOTES | Explicit 8–15 km source-shell direction-resolved escape calculation with high angular/path/radial orders, geometry tests and production-output isolation. It writes JSON to the branch. No explicit profile SHA check is present in the YAML; verify the script embeds and validates the profile identity. |
| `b16-directional-escape.yml` | REVIEWED_WITH_NOTES | This workflow runs the same 8–15 km script and writes the same output path as `b16-directional-escape-8-15.yml`, but does not pass `--energy-offset 1000`. This creates a plausible output race and an ambiguity in energy convention. Determine whether the omitted flag intentionally selects a default; if not, separate the output filename or retire one workflow after run-history review. |

## Cross-cutting findings

1. The B.14 filename/name mismatch should be corrected in the catalog so users do not mistake it for the exact B.13 kernel.
2. One workflow does not pin the checkout to the event SHA, reducing reproducibility under reruns/manual dispatch.
3. Two directional escape workflows target the same script and same output path with different command-line arguments. This is the most actionable issue in this batch: the output needs a single unambiguous energy convention and writer.
4. All five workflows use `contents: write` because they commit result JSON. This is an elevated permission and should be reduced if outputs are moved to artifacts or a separate trusted archival process.
5. The physical acceptance ladder remains unchanged: local source/kernel checks and directional escape diagnostics do not establish full radial transport or final axial SN1987A exclusion.

## Disposition

All five entries were marked `REVIEWED_WITH_NOTES`. No workflow, script, input, output or scientific result was modified.
