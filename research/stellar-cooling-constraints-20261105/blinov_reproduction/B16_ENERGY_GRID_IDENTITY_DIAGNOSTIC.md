# B.16 energy-grid identity diagnostic

## Purpose

This read-only diagnostic investigates the energy-grid fingerprint mismatch seen in the B.16 10 MeV phase-space workflow.

The archived high-order baseline has 842 energy nodes and SHA-256:

`036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`.

The fingerprint `db6f613c...` is also observed on a runner that evaluates one threshold node one ULP differently. It is therefore retained as a recorded floating-point variant, not treated as a different physical grid.

The diagnostic reconstructs the energy grid through three routes:

1. the high-order `run_mass()` profile/radial-grid setup;
2. the phase-space audit's opacity-profile setup;
3. an independent CSV read and lapse interpolation.

The three routes must agree within a single run. The resulting 842-node array is then compared with the archived reference node array using a declared relative tolerance. Source and opacity radial-grid fingerprints remain exact checks.

## Archived reference

- Reference file: `outputs/b16_energy_grid_reference_10mev_2026-11-09.json`
- Reference file SHA-256: `3a99a994d9cab96fd194cf540d75ef698f871354839c8f55f05eeaa11f02d957`
- Reference energy-grid SHA-256: `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`
- Nodes: 842
- Reference reconstruction: Actions run [#45165988653](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45165988653), commit `e8e467c768c240b6a295a61790a5240701950e65)
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`

The reference array is immutable evidence derived from a run whose raw little-endian float64 node hash exactly matches the original baseline. The reference file also records its reconstruction environment and original baseline commit.

## Numerical comparison

The comparison uses

$$
\mathrm{rtol}=5\times10^{-15},\qquad \mathrm{atol}=0\ \mathrm{MeV}.
$$

This tolerance is applied to every energy node, not to the luminosity or physical observables. The original SHA-256 remains recorded and checked against the reference file; the current runtime's exact node SHA is reported separately.

The strict phase-space production run [#45172485856](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45172485856) produced:

- 842 energy nodes;
- runtime energy SHA-256 `db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639`;
- maximum absolute node difference: (5.684341886080802\times10^{-14}) MeV;
- maximum relative node difference: (1.1675488289093305\times10^{-16});
- maximum difference: 1 ULP;
- comparison result: PASS.

The three constructions within the same run agree exactly. The diagnostic run [#45171900209](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45171900209) also reproduced the original SHA exactly. Both outcomes satisfy the same node-level acceptance.

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
  --grid-reference research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_energy_grid_reference_10mev_2026-11-09.json \
  --output b16_energy_grid_identity_diagnostic.json
```

## Acceptance

- All three energy arrays reconstructed within one run must be exactly equal.
- The source and opacity radial-grid fingerprints must match the archived baseline exactly.
- The energy-node count must be 842.
- Every energy node must agree with the archived reference array at the declared tolerance.
- The reference file's internal SHA-256 must equal the original archived energy-grid SHA-256.
- The profile SHA-256 must match the archived profile.
- No production rates, opacities, luminosities, or axial-vector constraints are modified by the diagnostic.

A failed node comparison remains a hard failure. Do not update the baseline hash or widen the tolerance to make a run pass; inspect the node arrays and provenance first.
