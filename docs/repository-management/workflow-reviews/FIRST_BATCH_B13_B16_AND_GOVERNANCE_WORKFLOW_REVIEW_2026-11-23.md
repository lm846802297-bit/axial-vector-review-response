# First-batch B.13/B.16 and governance workflow review — 2026-11-23

## Scope and inventory

This review covers the five workflows introduced by the B.13/B.16 first-batch integration and the two governance workflows that were already present on main but absent from the workflow catalog and audit register.

The reconciled integration tree contains **125 workflow YAML files**. The register is updated to 125 unique paths. No workflow is deleted or disabled.

## Individual workflow review

### 1. Axial structured-result validation

- Path: \`.github/workflows/axial-structured-result-validation.yml\`
- Workflow blob: \`67b1c22137a03dae7d8fc765a8b642ea419596f1\`
- Triggers: pull requests and main pushes touching the structured-result standard, schemas, or workflow; manual dispatch.
- Permissions: \`contents: read\`.
- Runtime: Python 3.12; dependency pinned through \`schemas/requirements-result-validation.txt\`.
- Checks: structured-result regression tests and schema-package compilation.
- Execution evidence: [run #45147116682](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45147116682), successful.

Disposition: \`REVIEWED_WITH_NOTES\`. The workflow is read-only and its test scope is limited to the local structured-result schema/validator package; it does not validate arbitrary historical scientific outputs.

### 2. Central standards adoption validation

- Path: \`.github/workflows/standards-adoption-validation.yml\`
- Workflow blob: \`843cb6ceccb786cf18200e4841b334c0f7d96012\`
- Triggers: pull requests and main pushes touching \`research/standards-lock.yaml\`, standards provenance, task briefs, run manifests, \`AGENTS.md\`, or the workflow; manual dispatch.
- Permissions: \`contents: read\`.
- Runtime/dependencies: Python 3.12; pinned PyYAML and JSON Schema dependencies; central validator source is fetched at the commit pinned by the workflow.
- Checks: standards lock, provenance records, task briefs, and run-manifest adoption.
- Execution evidence: [run #45173283303](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45173283303), successful.

Disposition: \`REVIEWED_WITH_NOTES\`. This validates the declared adoption interface and metadata contract; it does not certify the scientific correctness of each downstream calculation.

### 3. B.13 local-kernel artifact recovery

- Path: \`.github/workflows/b13-local-kernel-artifact-recovery.yml\`
- Workflow blob: \`665ab3343e9c8f2f99a8f42d4a36b18361f2c093\`
- Trigger/guard: push and manual dispatch on the exact B.16 diagnostic branch.
- Permissions: recovery/calculation job is read-only; only the separate archive job receives \`contents: write\`.
- Runtime: Python 3.12.16.
- Checks: downloads the original historical artifact, verifies its JSON SHA-256, constructs the CSV/plots/provenance package, and tests charge/mode coverage and preservation of failed acceptance.
- Execution evidence: [run #44098486569](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44098486569), successful.

Disposition: \`REVIEWED_WITH_NOTES\`. This is artifact recovery and post-processing, not a new local-kernel calculation or physical acceptance.

### 4. B.16 energy-grid identity diagnostic

- Path: \`.github/workflows/b16-energy-grid-identity-diagnostic.yml\`
- Workflow blob: \`09caaab039accaa13a221e69bc1f3b6bebd7913d\`
- Trigger/guard: push path filters and manual dispatch on the exact B.16 diagnostic branch.
- Permissions: \`contents: read\`; no repository write-back.
- Runtime: Python 3.12 with NumPy 2.5.4 and SciPy 1.18.1.
- Checks: reconstructs the energy grid through the high-order driver, phase-space driver, and direct CSV interpolation; compares against the archived 842-node reference.
- Numerical contract: source and opacity grid hashes remain exact; energy nodes are compared individually with \(5\times10^{-15}\) relative tolerance and zero absolute tolerance. The original reference SHA-256 is retained.
- Execution evidence: [run #45171900209](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45171900209), successful.

Disposition: \`REVIEWED_WITH_NOTES\`. The one-ULP runner variation is explicitly covered by the node-reference comparison; the tolerance does not apply to source/opacity grids or physical observables.

### 5. B.16 strict 10 MeV phase-space reproduction

- Path: \`.github/workflows/b16-strict-phase-space-reproduction.yml\`
- Workflow blob: \`e5a27b1b7eca62059edb134eb086c3c196625b40\`
- Trigger/guard: source/input path filters on the exact B.16 diagnostic branch.
- Permissions: phase-space calculation and validation are read-only; the separate archive job receives \`contents: write\` only after success.
- Runtime: Python 3.12 with NumPy 2.5.4 and SciPy 1.18.1.
- Archive safeguards: the archive job re-fetches the branch, checks that all calculation/validator inputs still match the event commit, retries concurrent branch updates, and refuses stale write-back.
- Execution evidence: [run #45172485856](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45172485856), calculation, baseline validation, regression tests, and archival successful.

Disposition: \`REVIEWED_WITH_NOTES\`. The accepted result closes the 10 MeV phase-space bookkeeping against the archived high-order baseline. It does not reproduce the digitized Fig. 7 luminosity: the +92.4284% discrepancy remains open.

### 6. B.16 output-validator hardening tests

- Path: \`.github/workflows/b16-output-validator-tests.yml\`
- Workflow blob: \`d67a64b1a9a78ae47a56bf60943637aa3b84fd3d\`
- Trigger/guard: push and manual dispatch on the exact B.16 branch; read-only pull-request validation on main.
- Permissions: \`contents: read\`.
- Runtime: Python 3.13.5 with NumPy 2.5.4 and SciPy 1.18.1.
- Checks: compiles the validator, runs the 24-test strict numeric/sparse-marginal regression suite, and independently validates the archived 10 MeV result against the node reference.
- Execution evidence: [run #45173157775](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45173157775), all steps successful.

Disposition: \`REVIEWED_WITH_NOTES\`. The test suite validates the declared output schema and numerical closure rules; the workflow does not update production constraints.

### 7. B.13 targeted high-order provenance validation

- Path: \`.github/workflows/b13-high-order-provenance-validation.yml\`
- Workflow blob: \`00ed87993fb775cb5800ce81697c03870ff2e245\`
- Triggers: exact-branch push, read-only PR-open/reopen/ready-for-review events, and manual dispatch.
- Permissions: calculation/validation job is read-only; a separate guarded archive job receives \`contents: write\`.
- Runtime: Ubuntu 24.04, Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0; four workers.
- Source identity: calculation checks out exact source commit \`e49908762e90271f4bc84be75e19577431febd4c\`.
- Archive safeguards: verifies event-input blob identities before write-back and on retries; refuses stale outputs and retries at most five times.
- Execution evidence: [run #45172924204](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45172924204), Calculate, Validate, and Archive successful.

The run reproduced 431/431 targeted \((r,x)\) points and 2,155 ordered evaluations. Maximum final successive-order change was \(3.29220848525901\times10^{-4}\); maximum detailed-balance residual was \(5.027846521385086\times10^{-15}\); maximum mass-shell residual was \(2.0432421890821873\times10^{-13}\). All targeted quadrature and finite/nonnegative-rate checks passed.

The new output was compared with the preceding AMD EPYC 7763 reproduction #45054965537 after exact \((r,x)\) alignment. All 431 keys and order ladders matched; 28,446 numerical leaf fields were compared with zero differences.

Disposition: \`REVIEWED_WITH_NOTES\`. This remains a targeted 431-point acceptance. The full 1,687-node global high-order acceptance remains false.

## Register reconciliation

The two previously omitted governance workflows and the five first-batch workflows are now registered. The resulting inventory is:

- 125 workflow YAML files;
- 125 unique workflow-register entries;
- 110 \`REVIEWED_WITH_NOTES\`;
- 1 \`ACTIVE\`;
- 14 \`HISTORICAL_CANDIDATE\`;
- 0 \`PENDING\`.

No workflow is removed or promoted to a scientific acceptance merely because its CI run is green.
