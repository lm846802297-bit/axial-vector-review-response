# Workflow review: pinned independent analytic B.2 path integration

Review date: 2026-11-15  
Workflow: `b16-independent-analytic-path-pinned.yml`  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Pinned runtime: Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1

## 1. Workflow contract and static review

- Trigger: path-filtered push to the maintenance review branch, plus manual `workflow_dispatch`.
- Branch guard: the job explicitly requires `GITHUB_REF=refs/heads/maintenance/repository-organization-audit-20261114`; manual dispatch from another branch fails before calculation or write-back.
- Runner: GitHub-hosted `ubuntu-latest`; it does not use the user's Windows self-hosted runner.
- Dependencies: exact versions are pinned by `requirements-b16-audit.txt` and asserted at runtime.
- Tests: runs the five independent analytic B.2 path tests.
- Calculation: full 10 MeV independent analytic chord integration with 40 source-radius nodes, 142 energy nodes after lapse-threshold union, 25 coupling points, path-order convergence \(8,16,32,64,128\), angular Gauss orders \(16,32,64\), Simpson subintervals \(128,256\), and 27 adaptive QUADPACK checks.
- Acceptance: checks source/profile/reference provenance, exact-grid reproduction, path-integral closure, angular cross-checks, final 25-point curve, and the invariant that production axial-vector outputs remain unchanged.
- Write scope: `contents:write` is used only to commit the single generated JSON output to the fixed reviewed branch. The generated-output path is not in the push path filter, preventing a write-back loop.
- Secrets: no repository secrets are consumed.

Outcome: `REVIEWED_WITH_NOTES`.

## 2. Execution history and failure classification

| Run | Result | Interpretation |
|---|---|---|
| [#43649275502](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43649275502) | Failure at output validation | The full calculation and five tests completed. The validator incorrectly treated the scalar `code_sha256` string as a nested dictionary. This was a workflow-schema bug, not a numerical failure. |
| [#43649561490](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43649561490) | Success | Corrected the validator to match the actual JSON schema; full integration, provenance, closure, and output write-back passed. |
| [#43649694860](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43649694860) | Success | Final run after adding the explicit reviewed-branch guard. This is the authoritative run referenced by the audit record. |

## 3. Archived output and numerical acceptance

Output: [`b16_path_independent_analytic_10mev_2026-11-15_numpy_pinned.json`](../../../research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_path_independent_analytic_10mev_2026-11-15_numpy_pinned.json)

- Output Git blob SHA: `b694ef4cde5ef46908a020241205a8b6354ea937`.
- Run commit: `e200faa10e510edfc4bf32990cda08ef26da0ca8`.
- Script SHA-256: `15e7aca16e69d50b57ea265d456b0c302d50a7042a0ed7aaaff8a57860408527`.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Fig. 7 reference SHA-256: `3eb1121da175d89da54a19abbdf0c52669a239be464978ddcfe84887e4d18d06`.
- Archived B.16 baseline SHA-256: `a81832562d1c4a1e92d9219e6e38f37aa43f557cf2825cc3e7fd8a27e59b4d7b`.

Numerical checks:
- Same-grid archived B.16 reproduction: \(2.22\times10^{-16}\) maximum relative difference.
- Exact analytic path versus reference path quadrature at \(N_s=32\): \(4.30698\times10^{-5}\) maximum luminosity shift.
- At \(N_s=128\): source-weighted RMS optical-depth residual \(1.32864\times10^{-5}\), maximum luminosity shift \(1.39626\times10^{-6}\).
- Simpson-256 versus adaptive QUADPACK angular escape average: \(1.1460\times10^{-6}\) maximum relative difference across 27 checks.
- Final Simpson-256 curve versus archived B.16: \(4.52065\times10^{-5}\) maximum relative difference.
- Final Fig. 7 residuals: weak endpoint \(-8.88530\%\), reference peak \(+2.56937\%\), strong endpoint \(+92.24931\%\).

The independent analytic B.2 integration therefore confirms that the path-quadrature algorithm does not explain the order-one strong-endpoint discrepancy, conditional on the shared profile, local opacity, B.1 source measure, and fixed-\(\omega\) Euclidean-chord prescription. This workflow does not independently validate those shared physical inputs and does not perform full-GR ray tracing.

## 4. Scientific disposition and remaining work

No opacity rescaling, source normalization adjustment, profile edit, coupling change, or production axial-vector constraint update is made. The next independent numerical layer is B.1 source-measure and radial/energy-quadrature validation. The reconstructed public-figure profile remains a physical-input limitation; a full-GR extension still requires same-snapshot \(A(r)\) or \(M(r)\) data.

The workflow is suitable as a pinned reproducibility lane for this isolated B.2 analytic path audit. Its status does not imply that the full Fig. 7 discrepancy or the physical SN model has been resolved.
