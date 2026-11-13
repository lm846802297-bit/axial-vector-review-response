# Review-package numerical validation (2026-11-13)

## Scope

This validation was run against the extracted review package at the fixed calculation source baseline `81d9b2faf16eb39879b759b05afce46732c925d7`. It validates software identities, saved numerical outputs, and the independent literature matrix-element implementation. It does not regenerate the axial/vector scan or redraw the exclusion plot.

## Test results

| Test group | Tests | Result |
|---|---:|---|
| Core production, profile, detailed-balance and digitization | 52 | PASS |
| Independent Blinov and B.13/B.16 transport reference | 88 | PASS |
| Moving-muon, finite-mixing and thermal-integral supplement | 81 | PASS |
| **Total targeted tests** | **221** | **221 PASS, 0 FAIL** |

The exact test modules and commands are implemented in the repository-level `research/stellar-cooling-constraints-20261105/run_review_validation.py`. When run, it writes individual stdout/stderr logs and a machine-readable summary under `research/stellar-cooling-constraints-20261105/outputs/review_package_validation_2026-11-13/`. The original 2026-11-13 stdout/stderr logs were not retained in this handoff; the human-readable report and machine-readable summary are preserved in this package.

## Saved-output validation

`validate_outputs.py` returned exit code 0. It checked the saved scan arrays and reported:

- Baseline mass points: 75
- Plotted axial mass points: 80
- Coupling points: 301
- Optimized-column luminosity relative closure above (10^{40},mathrm{erg,s^{-1}}): (2.03	imes10^{-15})

The archived convergence and sensitivity checks remain distinct. In particular, the radius-20 km sensitivity has a large upper-boundary change (about 92.7%); it is a sensitivity diagnostic, not a numerical-convergence claim.

## Independent literature-kernel comparison

The independent spinor implementation was compared with the literature matrix-element kernel at 28 points. The comparison passed, with maximum relative error (2.88	imes10^{-12}). The reference file SHA-256 is:

`315ca0d79e20b0ec1c52b5664d58fd7e65f9b30c5c7db56f48db8632ee9c9a5e`

This validates the tested matrix-element implementation at those points; it does not validate the stellar background or global transport.

## Data-format issue disclosed

The package's `JSON_FORMAT_AUDIT.csv` flags one historical supplemental file:

`blinov_reproduction/outputs/p1iii_eos_kernel_self_test_2026-11-11.json`

It contains literal escaped newline sequences between object members and is therefore not strict JSON. The file is preserved byte-for-byte, its hash is recorded, and it is not consumed by the plotted axial scan. It has not been silently rewritten.

## Incomplete test scope

A full recursive discovery also enters the supplemental EOS/C4 test modules and exceeded the 120-second local execution budget. No claim is made that every test in that broader tree passed. The 221 explicitly selected and completed tests above are the acceptance set for this review handoff.

## Physical validation boundary

The pure-vector Blinov Fig. 7 comparison at the 10 MeV strong-absorption endpoint remains **NOT PASSED** (about +92.24% in the literal fixed-energy comparison). Therefore this package is a fixed-profile ballistic-cooling benchmark and review record, not a final unconditional SN1987A exclusion. No opacity rescaling, physical input adjustment, or new axial-limit claim is introduced by this packaging validation.


## Handoff provenance and validation scope

- The 221-test record and saved-output checks refer to the pinned calculation source baseline `81d9b2faf16eb39879b759b05afce46732c925d7`.
- PR #94 performed archive extraction and integrity checks only; it did not rerun the 221 tests or regenerate scans and figures.
- The historical 221-test summary is copied to `package_metadata/validation_summary_2026-11-13.json`. Individual stdout/stderr logs from that historical run were not retained.
- The repository-level rerun entry point is `research/stellar-cooling-constraints-20261105/run_review_validation.py`. A future rerun must be interpreted against the exact execution-tree commit recorded by the script; it must not be conflated with the historical pinned-baseline result.
