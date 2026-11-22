# B.13 targeted high-order rerun — 2026-11-22

## Local primary calculation

The local primary calculation completed with exit status 0: 431 unique `(r,x)` points, 2,155 ordered quadrature evaluations, four workers and 343.5815 s runtime. The local runner was Linux / Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 on AMD EPYC 9V74. The exact source driver, frozen target input, profile and imported dependencies are identified by source commit `e49908762e90271f4bc84be75e19577431febd4c`; all 12 entries in `SOURCE_FILE_IDENTITY.json` match their Git blob SHA-1, SHA-256 and byte count.

## Independent GitHub Actions runs

### Initial archival attempt — run #45041173008

The calculation, validation and artifact upload passed, but the archive job failed because `CI_RUN.log` matched a repository ignore rule. The failed attempt is retained as historical evidence and is not used as the archive acceptance.

### First complete archive — run #45043212683

[Run #45043212683](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45043212683) completed Calculate, Validate and Archive successfully. It reproduced 431/431 task points and archived artifact #14762941323 in commit `8b5d28b58951623e375436478e6a524670e7ee18`. This is the CI run referenced by the original local/CI comparison record.

### Exact-head push reproduction — run #45048755752

[Run #45048755752](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45048755752) completed Calculate, Validate and Archive successfully on branch commit `1ee26f742e9f03cbccdd4237bbc8bb1c790ce91a`. It used Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0 on Ubuntu 24.04 / Intel Xeon 6975P-C, four workers, 485.5 s runtime. Its artifact #14764174323 has ZIP SHA-256:

`5714902f8d44be284e5f067d99dcccff16556a1e9552f9f38a5bf1c993d8ff0d`

The archive commit is `04d7064602b3246e760ba6d80d0c4a0be7744418`. The five artifact files (raw points, acceptance summary, independent validation report, CI environment and CI log) were downloaded and verified: their SHA-256 values match `CI_OUTPUT_HASHES.sha256`, and their Git blob SHA-1 values match the files committed on the B.13 branch (**5/5**).

### Pull-request event reproduction — run #45050501965

[Run #45050501965](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45050501965) validated PR #133's branch head `b328f1bfba935ed50c8aee4ed0c15c1b273e0b33` (event merge SHA `38c2ed77ee95c6c9b3f9741d50dbc3bd5d3851c4`). Calculate, validation, and artifact upload passed; the archive job was intentionally skipped for the `pull_request` event. The job had `contents: read` only. Artifact #14765736550 was downloaded; it is retained as a PR-event artifact, not committed to the branch.

## Numerical cross-checks

The original [local/CI comparison report](../../research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_RERUN_2026-11-22/LOCAL_CI_CROSS_RUN_COMPARISON.json) compares the local run with CI run #45043212683. I also independently compared the archived #45048755752 result with #45043212683, and the PR-event #45050501965 artifact with the archived #45048755752 result.

For each pair:
- 431/431 identical task keys after alignment by `(r_km,x)`;
- identical quadrature order ladders;
- 10,344 charge/mode rate components compared;
- maximum absolute and relative rate differences: 0;
- maximum final-order-change difference: 0;
- maximum detailed-balance residual difference: 0;
- maximum mass-shell residual difference: 0.

The raw JSON files are not byte-identical because row order and run-specific metadata differ. The numerical payloads are identical.

## Numerical acceptance and scientific boundary

`N_(r,x)=431`, `N_eval=2155`. The maximum final successive-order change is `3.29220848525901e-4`; maximum radial midpoint interpolation error is `8.311070322862653e-4`; maximum energy PCHIP error is `6.716564877619043e-4`. Maximum detailed-balance and mass-shell residuals are `5.027846521385086e-15` and `2.0432421890821873e-13`.

This is a targeted high-order audit of the ten worst radial intervals and ten worst low-`x` energy points, not full 1,687-node global high-order acceptance. The provenance retains:

`"full_global_high_order_acceptance": false`

No production rate, opacity, transport output, Fig. 7 result or axial-vector constraint is changed.
