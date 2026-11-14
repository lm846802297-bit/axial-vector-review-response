# Workflow review: pinned full independent B.1+B.2 luminosity

Review date: 2026-11-15  
Workflow: `b16-full-b1b2-independent-pinned.yml`  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Pinned runtime: Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1

## 1. Static workflow review

- Trigger: path-filtered push to the maintenance review branch and manual `workflow_dispatch`.
- Branch guard: the job explicitly requires `GITHUB_REF=refs/heads/maintenance/repository-organization-audit-20261114`; manual dispatch from another branch fails before calculation or write-back.
- Runner: GitHub-hosted `ubuntu-latest`; it does not use the user's Windows self-hosted runner.
- Dependencies: exact Python, NumPy, and SciPy versions are pinned and asserted.
- Inputs: the workflow explicitly supplies the pinned B.1 thin-source JSON and pinned B.2 analytic-path JSON. The validator cross-checks their file SHA-256 values, run commits, profile hash, archived B.16 baseline hash, and Fig. 7 reference hash.
- Tests: four unit tests cover the angular escape factor's zero-depth limit, coupling monotonicity, zero-coupling limit, and rejection of negative optical depth.
- Calculation: complete fixed-\(\omega\) Appendix-B B.1+B.2 luminosity for the 10 MeV benchmark, with 100/200 source radial nodes, 320 energy nodes per source radius, 16 angular nodes, and 25 digitized coupling vertices.
- Acceptance: checks B.1 source closure against the pinned 400-node source, sub-percent agreement with archived B.16, finite values, expected persistence of the Fig. 7 discrepancy, and invariance of production axial-vector outputs.
- Write scope: `contents:write` is used only to commit the generated full-curve JSON to the fixed reviewed branch. The output path is excluded from the push path filter to prevent a write-back loop.
- Secrets: no repository secrets are used.

Outcome: `REVIEWED_WITH_NOTES`.

## 2. Execution

Run: [#43651020195](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43651020195)  
Result: success; all steps completed.

- Four unit tests passed.
- Full 25-coupling B.1+B.2 calculation completed.
- Pinned B.1/B.2 input provenance and baseline/figure hashes matched.
- Source closure, full-curve comparisons, and finite-value checks passed.
- Production axial-vector outputs were unchanged.
- Output JSON was archived on the reviewed branch.

## 3. Output and numerical results

Output: [`b16_full_b1b2_independent_10mev_2026-11-15_numpy_pinned.json`](../../../research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_full_b1b2_independent_10mev_2026-11-15_numpy_pinned.json)

- Output Git blob SHA: `f6a61a337474167fa0819f5435eb595e10df7ea5`.
- Run commit: `1aa2697356b01c499f1801dc0eddf60581795b3b`.
- Script SHA-256: `85bb5bc4a3dfc8a5060a297eab32d795a96ebf737bc3b0d3e05fe5938e45d771`.
- Pinned B.1 input SHA-256: `64a45d1764c41a056a828c518118dba99ad919752668cb031b428827d45779cf`.
- Pinned B.2 input SHA-256: `f1e059db7d8180b4d5752c9a3d3687f8082309548b2001d2679132c3e9591732`.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

| Metric | vs archived B.16 | vs digitized Fig. 7 |
|---|---:|---:|
| Mean absolute relative difference | 0.397526% | 15.88556% |
| Maximum absolute relative difference | 0.445059% | 92.05416% |
| Weak endpoint | -0.445059% | -9.290812% |
| Reference peak | -0.406173% | +2.152171% |
| Strong-absorption endpoint | -0.096994% | +92.05416% |

The final 200-node thin source is \(4.3042760061\times10^{70}\) erg/s per \(g^2\), within \(2.14115\times10^{-5}\) relative of the separately pinned 400-node B.1 source. The 100-to-200-node full-luminosity radial refinement has a maximum shift of 0.19867%.

## 4. Scientific scope and limitations

The full independent B.1+B.2 implementation reproduces the archived B.16 curve to better than 0.45% at all 25 coupling points, while retaining the order-one strong-endpoint discrepancy with Fig. 7. This closes the old B.1/B.2 numerical quadrature implementation gates for the adopted inputs.

The calculation still shares the reconstructed stellar profile, local production/absorption kernels, negative-muon density convention, and fixed-\(\omega\) Appendix-B energy prescription. It is not full-GR ray tracing, not a new axial-vector constraint, and not evidence that the original Garching raw snapshot has been reproduced. No fitted opacity/source correction is authorized.
