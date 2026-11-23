# B.16 strict phase-space and energy-grid workflow review

Review date: 2026-11-17  
Reviewed PR source head: `c7c8084e93316c8880da5c57f951b825d1ec3f87`  
Review type: static workflow/YAML and source-path review; both files parsed successfully with PyYAML 6.0.3 (syntax check only); no workflow was run as part of this review.

## Scope

The review covers:

- `.github/workflows/b16-energy-grid-identity-diagnostic.yml`
- `.github/workflows/b16-strict-phase-space-reproduction.yml`
- The diagnostic driver, strict phase-space driver, validators, regression tests, profile input, and archived high-order baseline JSON referenced by the workflows.

The workflow files were reviewed after the branch-guard and permission-scope changes. Their final Git blob identities are recorded in the workflow register.

## 1. Energy-grid identity diagnostic

**Disposition: `REVIEWED_WITH_NOTES`.**

The workflow is read-only (`contents: read`) and performs a bounded diagnostic rather than the full production phase-space calculation. It reconstructs the 10 MeV energy grid through the independent driver paths, checks the archived baseline fingerprint, runs the focused regression tests, and uploads the machine-readable diagnostic JSON.

The push-path filter now includes the driver, regression test, `reference.py`, the reconstructed SFHo-18.8 profile, and the archived high-order baseline JSON. This closes the material input-path omissions found in the initial static pass. Manual dispatch is restricted by a job-level exact-ref guard to `research/b16-energy-grid-diagnostic-20261117`; dispatching from another branch skips the job rather than running against a different or incomplete input tree.

The artifact upload occurs only after a successful diagnostic and treats a missing JSON as an error. The workflow uses Python 3.12 with NumPy 2.5.4 and SciPy 1.18.1 pinned.

## 2. Strict 10 MeV phase-space reproduction

**Disposition: `REVIEWED_WITH_NOTES`.**

The workflow retains the successful production sequence: compile the B.16 audit and validator, run the high-order 10 MeV decomposition, validate baseline and joint/marginal closure, execute the three focused regression suites, and verify that the production axial-vector rate/transport outputs remain unchanged.

The permission boundary is now split by job:

- Workflow default: `contents: read`.
- `phase-space-audit`: `contents: read`; it performs the calculation, validation, tests, and artifact upload only.
- `archive-result`: `contents: write`, and it runs only when the audit job succeeded **and** `github.ref` is exactly `refs/heads/research/b16-energy-grid-diagnostic-20261117`.

The write-back job downloads the validated artifact, copies the canonical JSON to its repository path, and pushes only to the diagnostic branch. It does not grant write permission to the calculation job. The exact branch guard also prevents a manual dispatch from `main` or another branch from reaching the write-back job.

The strict workflow YAML itself was removed from the push path filter so a configuration-only edit does not automatically launch the expensive 180-minute calculation. Source, test, profile, and baseline-input changes remain covered by the push filter; the workflow can still be manually dispatched on its guarded branch. The generated JSON is not a trigger path, preventing a write-back loop.

## 3. Remaining implementation notes

- The action references use major-version tags (`actions/checkout@v4`, `actions/setup-python@v5`, and artifact actions `@v4`) rather than immutable commit SHAs. This is recorded as a supply-chain hardening opportunity, not a blocker for this focused repository review.
- The numerical libraries are pinned, while the pip installer itself is upgraded without an exact version pin. The runtime record prints the actual Python/NumPy/SciPy versions.
- The workflows are scoped to the research branch. Their successful execution does not establish full Fig. 7 reproduction or a physical SN1987A exclusion.

## 4. Execution and scientific boundary

No workflow was triggered during this static review. The previously recorded energy-grid identity run [#44054718118](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44054718118) and strict phase-space run [#44059347513](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44059347513) passed on their recorded source commit; those results are not represented as a rerun of the amended YAML.

The archived phase-space result reproduces the 842-node high-order energy grid and closes the global luminosity, optically thin source, escape probability, joint radius-energy-direction table, and checked one-dimensional marginals. It does **not** reproduce the digitized Fig. 7 10 MeV strong-absorption endpoint: the luminosity remains +92.4284% above the reference. The separate local-rate/polarization/escape audit remains `REVISION_REQUIRED`.

No opacity rescaling, physical convention, production axial-vector output, constraint curve, or manuscript source was changed by this workflow review.

