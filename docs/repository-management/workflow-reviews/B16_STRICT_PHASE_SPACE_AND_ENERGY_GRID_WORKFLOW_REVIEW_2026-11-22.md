# B.16 strict phase-space and energy-grid workflow review — corrected record

Review date: 2026-11-22

Main baseline: a7ac6456dafb27492183912fe4abbaa73a9455f7

B.16 validator branch validation commit: 32125a04f4f3b319030f5ab886fbae7325849c30

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

Exact branch-head GitHub Actions verification:

- Workflow: `.github/workflows/b16-output-validator-tests.yml`
- Workflow blob: `f28ab2605261b07cef767d0f573c0800578adb9d`
- Successful run: [#45039964078](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45039964078)
- Exact head: `32125a04f4f3b319030f5ab886fbae7325849c30`
- Runner: Ubuntu 24.04; Python 3.13.5
- GITHUB_TOKEN permission: `contents: read`
- Compilation: PASS
- Regression tests: **16/16 PASS**
- Mainline 10 MeV result against the archived high-order baseline: **PASS**

The preceding [run #45039906417](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45039906417) stopped at Python setup because the Ubuntu 26.04 image did not provide Python 3.13.5; test and validation steps were skipped. Pinning Ubuntu 24.04 resolved the environment mismatch. The successful run above validates the exact branch head.

Exact source identities:
- Validator Git blob SHA-1: `699a34b6c7d29632b2af96df7ee7aeb3084c0eed`
- Validator SHA-256: `b90f981ad01a6ad2e8ddc9b3d5ea363789757c97e5bf444e07c985b73c943d49`
- Test Git blob SHA-1: `85b0434c1dfd77c90819a1127183946fb491891f`
- Test SHA-256: `8cd46f6757571455216682706009189b6a80c555388425c22ab20773a8d11041`

The earlier 13-test local prototype is retained as development history only; it is not the acceptance result.
## 4. Scientific result and acceptance boundary

The committed 10 MeV mainline result remains:
- Calculated luminosity: 2.439635957361032e52 erg/s.
- Fig. 7 reference: 1.26781475907372e52 erg/s.
- Relative difference: +92.42842378199307%.
- Escape probability: 3.2517740193528985e-4.
- Energy nodes: 842.
- Energy-grid SHA-256: 036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3.

No luminosity, opacity, source, transport prescription, production axial-vector output or constraint curve is changed.

## 5. Remaining review items

1. B.16 validator branch exact-head tests and mainline integration: complete.
2. Execute the split-permission strict workflow on its guarded diagnostic branch before describing that YAML as execution-tested.
3. Keep historical successful run IDs linked to their old workflow blob.
4. Keep the +92.4284% Fig. 7 discrepancy open as a physical investigation.
