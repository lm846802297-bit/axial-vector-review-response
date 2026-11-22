# B.13 targeted high-order rerun — 2026-11-22

The local primary calculation completed with exit status 0: 431 unique `(r,x)` points, 2,155 ordered quadrature evaluations, four workers and 343.5815 s runtime. All targeted quadrature, radial midpoint interpolation, energy PCHIP, detailed-balance, mass-shell and finite/non-negative rate checks passed. The native local raw JSON, summary and independent validation report are archived in the branch.

## Independent GitHub Actions reproduction

The first attempt, [run #45041173008](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45041173008), completed calculation, validation and artifact upload, but its archive job failed because `CI_RUN.log` matched a repository ignore rule. This attempt is retained as historical evidence and is not used as the final archive acceptance.

The corrected second attempt, [run #45043212683](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45043212683), completed **Calculate + Validate + Archive** successfully. It checked out the exact source commit `e49908762e90271f4bc84be75e19577431febd4c`, used Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0, and reproduced all 431 target points in 475.1 s with four workers. The regression suite passed 8/8 tests.

The CI artifact is `b13-high-order-431-point-reproduction` (artifact ID `14762941323`). Its ZIP SHA-256 is:

`20cb282c2f43237d9190b59a2056e1fd8b5a405410a83238e900121b22ff9e70`

All five files in the downloaded artifact were independently checked against the Git blobs on this branch: raw targeted points, acceptance summary, independent validation report, CI environment and CI run log — **5/5 byte-identical**. The successful archive commit is `8b5d28b58951623e375436478e6a524670e7ee18`.

## Local-versus-CI numerical comparison

The raw JSON files are not byte-identical because their record ordering differs. After aligning records by unique `(r,x)` keys, an independent comparison gives:

- 431/431 identical task keys and identical quadrature-order ladders;
- 10,344 charge/mode rate components compared;
- maximum absolute and relative rate differences: 0;
- maximum final-order-change difference: 0;
- maximum detailed-balance residual difference: 0;
- maximum mass-shell residual difference: 0.

The comparison is archived in [`LOCAL_CI_CROSS_RUN_COMPARISON.json`](../../research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_RERUN_2026-11-22/LOCAL_CI_CROSS_RUN_COMPARISON.json), with the current successful run and the initial archival failure distinguished in the provenance record.

## Source identity and acceptance boundary

The exact source driver, target input, profile and imported dependencies were checked against PR #121 source commit `e49908762e90271f4bc84be75e19577431febd4c`. All 12 entries in `SOURCE_FILE_IDENTITY.json` match their Git blob SHA-1, SHA-256 and byte count.

This remains a targeted high-order audit of the ten worst radial intervals and ten worst low-`x` energy points, not full 1,687-node global high-order acceptance. The provenance therefore retains:

`"full_global_high_order_acceptance": false`

No production rate, opacity, transport output, Fig. 7 result or axial-vector constraint is changed.
