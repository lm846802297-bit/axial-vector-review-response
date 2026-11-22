# B.16 strict phase-space and energy-grid workflow review — corrected record

Review date: 2026-11-22

Main baseline: a7ac6456dafb27492183912fe4abbaa73a9455f7

PR #121 source snapshot: e49908762e90271f4bc84be75e19577431febd4c

This report supersedes the permission and run-version statements in the 2026-11-17 B.16 workflow review draft. The successful strict-workflow runs used the earlier single-job, workflow-wide write-permission YAML, not the later split-permission YAML.

## 1. Energy-grid identity diagnostic

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

PR #121 source workflow blob: **d736265c4c9647f33b83627b4d69aed37b657501**. The B.16 review branch carries the same permission structure, removes one stale path-filter entry, and has branch blob **4eed19b894d1250429995f98828540f70d2cdb50**.

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

Local prototype verification:
- 13/13 tests passed.
- Tests cover nested NaN, positive infinity, negative infinity, invalid JSON constants, inconsistent Fig. 7 residual, inconsistent escape probability, negative fractions, baseline-grid mismatch and sparse zero-bin handling.
- The downloaded artifact from run #44059773875 (artifact 14317158089) passed a local hardened-validator integration check in no-baseline mode.
- Artifact ZIP SHA-256: 0bd67edea604e92b0fdaed69681beb107a61107acfd3ad6098a884aff2f2b9ad.
- Extracted JSON SHA-256: 0c919c883e9399f8570393fd7b2e959834da38bb7e67f66113a46fc5ae7c57d4.

The new read-only validator-test workflow runs the negative tests and validates the committed mainline 10 MeV result against the archived high-order baseline. Its exact branch-head run is pending.

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

1. Run the new read-only validator workflow on this branch and inspect the exact head SHA.
2. Execute the split-permission strict workflow on its guarded diagnostic branch before describing that YAML as execution-tested.
3. Keep historical successful run IDs linked to their old workflow blob.
4. Keep the +92.4284% Fig. 7 discrepancy open as a physical investigation.
