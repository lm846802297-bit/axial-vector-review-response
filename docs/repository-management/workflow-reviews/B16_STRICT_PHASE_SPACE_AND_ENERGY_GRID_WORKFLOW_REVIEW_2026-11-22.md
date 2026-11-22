# B.16 strict phase-space and energy-grid workflow review — corrected record

Review date: 2026-11-22

Main baseline: a7ac6456dafb27492183912fe4abbaa73a9455f7

B.16 validator branch validation commit: 9f5a42fcc756ac18ddd6122136b9b613e3655128

PR #121 source snapshot: e49908762e90271f4bc84be75e19577431febd4c

This report supersedes the permission and run-version statements in the 2026-11-17 B.16 workflow review draft. The successful strict-workflow runs used the earlier single-job, workflow-wide write-permission YAML, not the later split-permission YAML.

## 1. Energy-grid identity diagnostic — PR #121 source only

Workflow: **.github/workflows/b16-energy-grid-identity-diagnostic.yml**

Workflow blob: **93a713d20d6e74430bdeaf3d382b39c2de4ca213**

Disposition: **REVIEWED_WITH_NOTES**.

The workflow has workflow-level contents: read, one guarded diagnostic job, and no repository write-back. Its job runs only on the exact research/b16-energy-grid-diagnostic-20261117 ref. The workflow blob at the successful run commit is byte-identical to the PR #121 source workflow.

Successful run: [#44054718118](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44054718118), head 853b0341aa603726c0760d494ec7725b9021e1a0.

Recorded result:
- Three independently constructed 842-node energy arrays agree.
- Energy-grid SHA-256: 036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3.
- SFHo-18.8 profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.

## 2. Strict 10 MeV phase-space workflow: historical runs versus current YAML

Workflow: **.github/workflows/b16-strict-phase-space-reproduction.yml**

PR #121 source workflow blob: **d736265c4c9647f33b83627b4d69aed37b657501**. This workflow is part of PR #121's source snapshot only; it is not present in main or in the separate B.16 validator branch.

Disposition: **REVIEWED_WITH_NOTES; current permission split statically verified, execution pending**.

### Historical successful runs

Both [run #44059347513](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44059347513) and [run #44059773875](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44059773875) completed successfully.

Their exact source heads were:
- 428fe4075bddb0fdcbb594da9bd3e10696de8735
- e5df464dc17acc6314b6ae92e233143690689082

At both heads, the strict workflow blob was **12b5a61523aec6f497144332da5c88267aab6f0a** (110 lines). That version had workflow-wide contents: write and a single phase-space-audit job. The logs confirm GITHUB_TOKEN Contents: write for both runs. Runtime was Python 3.12.16, NumPy 2.5.4 and SciPy 1.18.1.

Those successful runs validate the old single-job workflow and its numerical calculation. They do not validate the later permission split.

### Current permission split

At PR #121 source head e49908762e90271f4bc84be75e19577431febd4c:
- Workflow default permission: contents: read.
- phase-space-audit job: contents: read; performs calculation, validation, tests and artifact upload.
- archive-result job: contents: write; depends on successful audit and is guarded to the exact research/b16-energy-grid-diagnostic-20261117 ref.
- The strict workflow YAML is not included in its own expensive push-path filter.
- The write-back target is the diagnostic branch only.

No successful Actions run has yet been tied to this split-permission workflow blob. Historical run links above must not be cited as execution evidence for the current permission boundary.

## 3. Validator hardening

The validator rejects non-finite values before any closure arithmetic:
- Strict JSON parsing rejects NaN, Infinity and -Infinity tokens.
- A recursive finite-number pass checks nested payloads.
- Required physical scalars must be JSON numbers and finite.
- Escaped, optically thin and reference luminosities must be positive.
- The stored Fig. 7 residual is recomputed as L_calc/L_Fig7 - 1.
- The stored escape probability is recomputed as L_escaped/L_thin.
- SHA-256 fields, grid node counts and non-negative partition fractions are checked.
- Sparse joint tables continue to accept omitted zero-weight bins; missing non-zero bins, unexpected labels and duplicate partition labels fail.

The initial 16-test revision passed in [run #45048853354](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45048853354); it is retained as a superseded validation snapshot.

### Baseline-integrity correction

The code review identified that the earlier validator checked the stored closure residuals and grid/profile fingerprints, but did not independently recompute luminosity closure from the selected high-order baseline point. The validator could therefore trust a stale or incorrectly populated residual field.

The corrected validator now:
- hashes the exact baseline JSON file and compares it with `baseline_json_sha256`;
- checks the baseline mass and selects exactly one point at the requested coupling;
- recomputes the luminosity, optically-thin luminosity and escape-probability residuals from that baseline point;
- checks the Fig. 7 reference luminosity against the baseline;
- requires exactly the two intended regions, with no duplicate region names.

The 23-test revision passed in [push run #45049753048](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45049753048) and [PR run #45049757154](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45049757154). A further API-level hardening then made the baseline digest mandatory whenever a baseline object is supplied, preventing callers from bypassing the digest check by omitting the optional argument.

The first 24-test attempt exposed a missing digest argument in the positive-baseline test fixture (push run #45051097952 and PR run #45051101967); the fixture was corrected. The final exact-head validation is:

- Workflow: `.github/workflows/b16-output-validator-tests.yml`
- Workflow blob: `f28ab2605261b07cef767d0f573c0800578adb9d`
- Successful push run: [#45051207273](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45051207273)
- Successful PR run on the final PR head: [#45054313254](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45054313254)
- Earlier PR run on the preceding metadata head: [#45054043193](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45054043193)
- Validator/test code head: `9f5a42fcc756ac18ddd6122136b9b613e3655128`; final PR head: `e6d8de6b7a021a0e665e2bf23eb793ab3349d423`
- Runner: Ubuntu 24.04; Python 3.13.5
- GITHUB_TOKEN permission: `contents: read`
- Compilation: PASS
- Regression tests: **24/24 PASS**
- Mainline 10 MeV result against the archived high-order baseline: **PASS**

Final source identities:
- Validator Git blob SHA-1: `22aa5fc0ef12a48a5bb65f0dbd1054c182deeb47`
- Validator SHA-256: `1c6cf1973d1ddd87bd1867689c47857da9b97b20e16c3656dfb40aa1e5c71be6`
- Test Git blob SHA-1: `b19c3a1839c8cf28f2010e63b513acc0441b3941`
- Test SHA-256: `05db94b092ff59be9aef3eddd5bca435d804f73560b43c5265091b44db09f3d0`

The earlier 13-test local prototype remains development history only.
## 4. Scientific result and acceptance boundary

The committed 10 MeV mainline result remains:
- Calculated luminosity: 2.439635957361032e52 erg/s.
- Fig. 7 reference: 1.26781475907372e52 erg/s.
- Relative difference: +92.42842378199307%.
- Escape probability: 3.2517740193528985e-4.
- Energy nodes: 842.
- Energy-grid SHA-256: 036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3.

No luminosity, opacity, source, transport prescription, production axial-vector output or constraint curve is changed.

## 5. Remaining review and integration items

1. **B.16 validator verification:** complete for the final 24-test validator revision and the current mainline 10 MeV result. Push run #45051207273 and exact PR-head run #45054313254 both passed. This is validation against mainline data, not a merge into main.
2. **PR #121 synchronization and overlap reconciliation:** pending. PR #121 remains Draft at head `e49908762e90271f4bc84be75e19577431febd4c`, based on the older `9bee9b3410d34195b09a4dff001174fb1d86edee` snapshot. Compared with current main `a7ac6456dafb27492183912fe4abbaa73a9455f7`, it is 27 commits behind and 125 commits ahead. Six paths overlap PR #134; the B.16 validator and test files on this branch are the newer strict revision and should be retained during reconciliation.
3. **Workflow inventory reconciliation:** PR #121's 118-workflow snapshot adds three workflows but omits three workflows now present on current main after PR #122. PR #133 adds the B.13 targeted high-order workflow and PR #134 adds the B.16 validator workflow. The reconciled union is 123 workflow YAMLs; regenerate the workflow catalog and register from the final Git tree rather than choosing either stale inventory wholesale. PR #121's three workflow-only additions are `.github/workflows/b13-local-kernel-artifact-recovery.yml`, `.github/workflows/b16-energy-grid-identity-diagnostic.yml`, and `.github/workflows/b16-strict-phase-space-reproduction.yml`; the three current-main workflows absent from that snapshot are `.github/workflows/b16-escape-phase-space-closeout.yml`, `.github/workflows/b16-local-rate-polarization-samples.yml`, and `.github/workflows/scan-archive-integrity-closeout.yml`. B.13 PR #133 and B.16 PR #134 share three documentation/catalog paths: `.github/workflows/README.md`, `.github/workflows/WORKFLOW_AUDIT_REGISTER.csv`, and `docs/repository-management/README.md`. Merge these files by retaining both workflow links, both register rows and both repository entry points; no calculation source or native output overlaps.
4. **Split-permission strict workflow:** execute the split-permission strict phase-space workflow on its guarded diagnostic branch before describing that YAML as execution-tested. Historical successful runs belong to the earlier workflow-wide write-permission blob.
5. Keep historical successful run IDs linked to their exact workflow blobs.
6. Keep the +92.4284% Fig. 7 discrepancy open as a physical investigation. No opacity rescaling or constraint update is authorized by these validator results.
