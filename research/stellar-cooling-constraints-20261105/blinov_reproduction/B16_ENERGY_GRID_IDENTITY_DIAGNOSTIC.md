# B.16 energy-grid identity diagnostic

## Purpose

This is a read-only diagnostic for the historical B.16 phase-space failure
reported on 2026-11-12:

- archived high-order baseline energy-grid SHA-256:
  `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`
- historical failed-run energy-grid SHA-256:
  `db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639`

The diagnostic reconstructs the energy grid through three routes:

1. the high-order `run_mass()` profile/radial-grid setup;
2. the phase-space audit's opacity-profile setup;
3. an independent CSV read and lapse interpolation.

It compares the three reconstructed arrays with one another, then compares all 842 physical energy nodes with the immutable node reference extracted from the archived high-order baseline. The original byte-level SHA-256 remains recorded as provenance; it is not the sole cross-platform equivalence test. The comparison records maximum absolute, relative, and ULP differences, together with profile, source-code, and runtime fingerprints.

## Run locally

From the repository root:

```bash
python -m pip install numpy==2.5.4 scipy==1.18.1
python -m unittest discover \
  -s research/stellar-cooling-constraints-20261105/blinov_reproduction \
  -p 'test_b16_energy_grid_identity.py' -v
python research/stellar-cooling-constraints-20261105/blinov_reproduction/diagnose_b16_energy_grid_identity.py \
  --mass 10 --nr 200 --opacity-order 640 --ne 200 \
  --energy-offset 1000 --strict-baseline \
  --output b16_energy_grid_identity_diagnostic.json
```

## Acceptance

- The high-order, phase-space, and direct-CSV constructions must agree within the declared floating-point tolerance.
- The source and opacity grid fingerprints must match exactly.
- The energy grid must contain 842 sorted nodes and match the immutable archived node reference at relative tolerance 5e-14 and absolute tolerance 1e-13 MeV.
- The original baseline SHA-256 and node-reference file SHA-256 are retained unchanged.
- The profile SHA-256 must reproduce the baseline profile SHA-256.
- No production rates, opacities, luminosities, or axial-vector constraints
  are recalculated or modified.

A failure leaves the JSON diagnostic available as a GitHub Actions artifact.
Do not update the baseline hash to make the check pass. Any mismatch must be
explained from the recorded arrays, inputs, and code fingerprints first.


## Current mainline result — 2026-11-17

The diagnostic workflow passed on the branch based on current `main`:

- [GitHub Actions run #44054718118](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44054718118)
- All three constructions (high-order driver, phase-space driver, and direct CSV lapse interpolation) are exactly equal.
- Energy nodes: 842.
- Energy-grid SHA-256: `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`, equal to the archived baseline.

The exact runtime SHA-256 can differ by last-bit floating-point rounding. Run #45171843071 produced `db6f613c...` while its 842 nodes matched the archived reference with maximum absolute difference 5.684341886080802e-14 MeV, maximum relative difference 1.1675488289093305e-16, and maximum ULP difference 1. Run #45171900209 reproduced the original `036e6d77...` byte hash. Both passed the node-wise identity test. The original baseline and node-reference fingerprints remain unchanged.

The latest integrated-branch diagnostic [#45182871981](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45182871981) again passed all six regression tests and the immutable 842-node comparison. The one-ULP node difference remains within the declared relative and absolute tolerances; the original byte-level baseline SHA-256 was not replaced.
