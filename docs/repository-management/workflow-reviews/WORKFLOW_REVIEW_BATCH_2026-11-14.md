# GitHub Actions workflow review — first sample (2026-11-14)

## Scope

Reviewed the full YAML text of 10 representative workflows on `maintenance/repository-organization-audit-20261114`. The review covers triggers, branch/path filters, permissions, concurrency, runner/timeouts, dependency setup, source checkout, execution steps, artifact/write-back behavior and consistency with the 2026-11-14 project status. It does not inspect every historical run or all 109 workflows.

## Per-workflow findings

| Workflow | Outcome | Findings |
|---|---|---|
| `major1-higgs-scalar-mixing.yml` | REVIEWED_WITH_NOTES | Push-triggered on the dedicated Major 1 research branch and narrowly path-filtered to selected subcalculations. Uses exact triggering SHA and test/audit scripts. Its broad, evolving path list and write-back/artifact behavior should be compared with the latest branch state before reuse. Does not establish full scalar-pole acceptance. |
| `major44-eft-regression.yml` | HISTORICAL_CANDIDATE | Push-filtered to the old `codex/major44-axial-cooling-constraints-20261105` branch plus manual dispatch; it grants `contents: write`. Current project status says the old research PR line has been integrated and no open PR remains. Check branch existence and recent runs before any manual use; likely a retained historical workflow. |
| `moving-muon-thermal-rates.yml` | HISTORICAL_CANDIDATE | Triggered on two named research branches, includes write permission and writes numerical results. The branch set appears historical relative to the current main status. Retain pending branch/run-history audit; do not dispatch on main without verifying output destinations and source contract. |
| `p1-b13-exact-polarization-kernel.yml` | REVIEWED_WITH_NOTES | Read-only permissions, exact triggering commit checkout, targeted compile and explicit-spinor/kernel tests. The push trigger points to a named historical research branch; manual dispatch behavior should be checked against current status and its run records. Its pointwise amplitude checks do not validate global transport. |
| `p1b-b13-local-kernel-radial-energy.yml` | REVIEWED_WITH_NOTES | Read-only permissions for the primary audit and a special source-bundle artifact path; 360-minute timeout reflects expensive numerical work. Verify that the `[source-bundle]` conditional and artifact retention are still needed, and ensure the regular path does not produce unreviewed output commits. Local-kernel convergence is not a global SN transport result. |
| `pure-vector-benchmark-audit.yml` | HISTORICAL_CANDIDATE | Branch-restricted to the older Major 4.4 research branch; grants `contents: write` and commits comparison/provenance outputs. Preserve its historical run evidence. Do not interpret a successful provenance audit as passing the 10 MeV Fig. 7 physical benchmark. |
| `transport-prescription-audit.yml` | HISTORICAL_CANDIDATE | Branch-restricted to the same older research branch; write-enabled and commits a comparison output. The project status still records the physical prescription as open. Check whether this is a one-time historical audit or still needed before reusing. |
| `pr55-referee-letter-build.yml` | HISTORICAL_CANDIDATE | LaTeX build workflow is pinned to PR #55/#56-era branches and uses write permission to archive generated artifacts. Current response package has since been rebuilt/extracted under later PRs. Retain as historical until a single current letter-build workflow is designated. |
| `pr55-latex-build.yml` | HISTORICAL_CANDIDATE | Older PR #55-only branch trigger, no manual dispatch, write permission, and duplicate build scope overlapping the later `pr55-referee-letter-build.yml`. Candidate for deprecation after checking workflow run history and whether any active branch still relies on it. |
| `axial-goldstone-pmns-regression.yml` | REVIEWED_WITH_NOTES | Main-branch push filter is limited to the separate two-VEV extension; read-only permissions and targeted tests. The workflow is correctly scoped to the two-VEV branch, but the README/report should explicitly preserve the boundary that these checks do not modify the original one-VEV manuscript model. |

## Cross-cutting findings

1. There are 109 workflow YAML files, dominated by B.13/B.16/B.2 and EOS/transport variants. The initial filename classifier was too coarse; this catalog now groups the complete list by more specific provisional prefixes.
2. Several older workflows are pinned to branch names associated with completed/merged PRs. They must be checked against actual branch refs and run history before being classified as superseded or deleted.
3. Multiple numerical workflows use `contents: write`. This may be necessary for result archival, but should be narrowed to read-only wherever no commit-back occurs.
4. The repository has distinct physical gates: exact amplitude, local thermal/radial kernel, opacity, transport prescription, full luminosity and physical Fig. 7 comparison. Do not consolidate them into one “pass” label.
5. The two PR55 letter-build workflows overlap and are likely legacy candidates. The current authoritative letter build path must be explicitly identified before retiring either.
6. This review does not change any workflow, branch, runner permission, trigger, or calculation.

## Next audit

Inspect the remaining 99 YAML files in batches, resolve branch existence and workflow-run recency for each candidate, map every referenced script and output path, then prepare a separate proposed deprecation list. No workflow should be deleted as part of a documentation-only pass.
