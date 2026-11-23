# B.13 / B.16 / standards workflow static review — 2026-11-23

Review scope: seven workflows absent from the previous 118-row register. This is a static source/YAML review plus run-history checks where listed; it does not convert CI success into scientific acceptance.

| Workflow | Trigger and scope | Permissions / environment | Review disposition |
|---|---|---|---|
| `axial-structured-result-validation.yml` | PR/push path filters for local structured-result schemas and standard, plus manual dispatch; compiles validator and runs schema regression tests | `contents: read`; Python 3.12; pinned `jsonschema[format]==4.26.0`; no artifact write-back | `REVIEWED_WITH_NOTES`; focused tests and compile only, not validation of all historical result files |
| `standards-adoption-validation.yml` | PR/push path filters for standards lock, provenance records, task briefs, run manifests and AGENTS; manual dispatch; validates lock, task provenance, reports and manifests | `contents: read`; Python 3.12; central validator fetched at pinned commit `db503f0eb579bdbcac702e44237a6610c34690e7`; central standards fetched at the commit in the lock | `REVIEWED_WITH_NOTES`; pinned central source is reproducible, but this workflow is a governance validator, not a scientific calculation |
| `b13-high-order-provenance-validation.yml` | Push to exact B.13 provenance branch; PR opened/reopened/ready-for-review; manual dispatch; reproduces frozen 431-point set | Calculate uses `contents: read`; separate guarded archive job uses `contents: write`; Ubuntu 24.04, Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 | `REVIEWED_WITH_NOTES`; exact-head run #45172924204 passed calculation, validation and archive; source/input identity and five archived outputs are fingerprinted |
| `b13-local-kernel-artifact-recovery.yml` | Push path filters on builder/test or manual dispatch, exact B.16 branch guard; recovers the original historical artifact | Recovery job uses `actions: read`, `contents: read`; separate archive job uses `contents: write`; Python 3.12.16 | `REVIEWED_WITH_NOTES`; historical input SHA is checked, tests preserve the original failed physical acceptance; no new kernel calculation is claimed |
| `b16-energy-grid-identity-diagnostic.yml` | Push path filters for diagnostic, profile, baseline, immutable node reference, and tests; manual dispatch; read-only grid reconstruction | `contents: read`; Python 3.12, NumPy 2.5.4, SciPy 1.18.1; artifact only | `REVIEWED_WITH_NOTES`; exact-head run #45182871981 passed six tests and the 842-node reference comparison |
| `b16-output-validator-tests.yml` | Push/PR path filters for validator, tests, baseline, node reference and strict result; manual dispatch | `contents: read`; Ubuntu 24.04, Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; no write-back | `REVIEWED_WITH_NOTES`; 24/24 tests and strict result validation passed in runs #45182874320 and #45182872035 |
| `b16-strict-phase-space-reproduction.yml` | Push path filters for B.16 source, validator, tests, profile, baseline and node reference; manual dispatch; exact branch guard | Calculation job uses `contents: read`; separate archive job uses `contents: write` only after all checks pass; Python 3.12, NumPy 2.5.4, SciPy 1.18.1 | `REVIEWED_WITH_NOTES`; exact-head run #45182871998 passed calculation, validation, regression tests and archive |

## Cross-cutting findings

1. All seven workflows use `contents: read` by default. Write permission is isolated to the two result-recovery/archive workflows and is guarded by successful validation plus an exact branch check.
2. The B.13 high-order workflow checks exact source commit and source-file identities before calculation and before archive retry. It intentionally skips archive write-back for pull-request events.
3. The B.16 strict workflow preserves the original 842-node baseline hash and validates the complete energy-node array against the immutable node reference. Cross-runner one-ULP differences are accepted only within the declared numeric tolerance; the reference is not rewritten.
4. The structured-result and standards-adoption workflows validate governance metadata and schemas. Their passing tests do not constitute physics validation of the research outputs.
5. The B.13 local-kernel recovery workflow reconstructs an existing historical artifact. Its documented quadrature/interpolation acceptance remains failed; the workflow must not be described as a new accepted B.13 kernel calculation.
6. No workflow writes production axial-vector rates, opacity tables, transport results, constraint curves, or manuscript physics.

## Register update

The seven rows are added to `.github/workflows/WORKFLOW_AUDIT_REGISTER.csv`. The reconciled recursive tree contains 125 YAML workflows; the register and README are regenerated from that tree. Status totals after this review: 110 `REVIEWED_WITH_NOTES`, 1 `ACTIVE`, 14 `HISTORICAL_CANDIDATE`, 0 `PENDING`.
