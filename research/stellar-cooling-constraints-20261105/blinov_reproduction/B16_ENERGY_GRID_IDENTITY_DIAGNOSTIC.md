# B.16 energy-grid identity diagnostic

## Purpose

This is a read-only diagnostic for the historical B.16 phase-space failure
reported on 2026-11-12:

- archived high-order baseline energy-grid SHA-256:
  \`036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3\`
- historical failed-run energy-grid SHA-256:
  \`db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639\`

The diagnostic reconstructs the energy grid through three routes:

1. the high-order \`run_mass()\` profile/radial-grid setup;
2. the phase-space audit's opacity-profile setup;
3. an independent CSV read and lapse interpolation.

It compares exact float64 arrays and SHA-256 fingerprints against the archived
baseline. It also records the profile and source-code fingerprints and the
Python/NumPy/SciPy versions.

## Run locally

From the repository root:

\`\`\`bash
python -m pip install numpy==2.5.4 scipy==1.18.1
python -m unittest discover \\
  -s research/stellar-cooling-constraints-20261105/blinov_reproduction \\
  -p 'test_b16_energy_grid_identity.py' -v
python research/stellar-cooling-constraints-20261105/blinov_reproduction/diagnose_b16_energy_grid_identity.py \\
  --mass 10 --nr 200 --opacity-order 640 --ne 200 \\
  --energy-offset 1000 --strict-baseline \\
  --output b16_energy_grid_identity_diagnostic.json
\`\`\`

## Acceptance

- All three energy arrays must be exactly equal.
- The source and opacity grid fingerprints are recorded.
- The energy node count and SHA-256 must reproduce the archived high-order
  baseline.
- The profile SHA-256 must reproduce the baseline profile SHA-256.
- No production rates, opacities, luminosities, or axial-vector constraints
  are recalculated or modified.

A failure leaves the JSON diagnostic available as a GitHub Actions artifact.
Do not update the baseline hash to make the check pass. Any mismatch must be
explained from the recorded arrays, inputs, and code fingerprints first.
