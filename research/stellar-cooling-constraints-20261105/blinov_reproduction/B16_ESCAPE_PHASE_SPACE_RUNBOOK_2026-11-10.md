# B.16 10 MeV high-order escape phase-space runbook

**Disposition at 2026-11-17: PASS_WITH_NOTES for the archived high-order vector-baseline phase-space decomposition.** The independent Fig. 7 10 MeV strong-absorption discrepancy remains open and is not closed by this runbook.

This runbook documents the strict, reproducible post-processing diagnostic. It does not change the stellar profile, source kernel, opacity prescription, fixed-\(\omega\) transport convention, production axial-vector outputs, or constraint curve.

## 1. Pinned environment

The accepted GitHub Actions run used:

| Component | Version |
|---|---:|
| Python | 3.12.16 |
| NumPy | 2.5.4 |
| SciPy | 1.18.1 |

For a local environment:

\`\`\`bash
python -m pip install numpy==2.5.4 scipy==1.18.1
\`\`\`

The calculation is CPU-based NumPy/SciPy code; it does not use CUDA or the RTX GPU.

## 2. Regression tests and compile check

From the repository root:

\`\`\`bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_b16_escape_phase_space.py' -v
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_b16_energy_grid_identity.py' -v
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_b16_phase_space_output_validation.py' -v
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/validate_b16_escape_phase_space_output.py
\`\`\`

The tests cover region-restricted energy/direction binning, energy-grid construction, and sparse joint-table marginal handling.

## 3. Energy-grid identity preflight

The accepted baseline fingerprints are:

| Grid | Nodes | SHA-256 |
|---|---:|---|
| Source radial grid | 200 | \`1a007702d1f7c8b81200e648a763f7f1a0e3565a39d57c8174dada5aad1a4cb5\` |
| Opacity radial grid | 642 | \`6701fc3fe06bf07879612e591ae62c494f673928bc18f169d4b6f3fabed7d378\` |
| Energy grid | 842 | \`036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3\` |

The independent diagnostic reconstructs the energy array through the high-order driver setup, the phase-space driver setup, and a direct CSV-lapse interpolation. All three arrays must be exactly equal to one another and reproduce the archived baseline hash. The current profile SHA-256 must also match the baseline:

\`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.

Run:

\`\`\`bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/diagnose_b16_energy_grid_identity.py --mass 10 --nr 200 --opacity-order 640 --ne 200 --energy-offset 1000 --strict-baseline
\`\`\`

Do not update a baseline hash to make this check pass.

## 4. Run the high-order 10 MeV decomposition

\`\`\`bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py \
  --mass 10 \
  --nr 200 \
  --opacity-order 640 \
  --ne 200 \
  --na 32 \
  --ns 64 \
  --energy-offset 1000 \
  --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-17.json
\`\`\`

The calculation uses the fixed-\(\omega\) Eq. (B.2) chord convention. Energy-bin edges are reporting partitions; they do not alter the underlying energy quadrature.

## 5. Automated acceptance

Run the validator against the produced JSON:

\`\`\`bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/validate_b16_escape_phase_space_output.py \
  research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-17.json
\`\`\`

Acceptance requires:

- Exact source, opacity, and energy grid identity against the archived high-order baseline.
- Exact profile fingerprint identity.
- Luminosity and optically thin source closure each below \(2\times10^{-10}\).
- Escape-probability closure below \(2\times10^{-13}\).
- Angular quadrature weights summing to one within \(10^{-14}\).
- Regional emission-radius, energy, four-bin direction, and eight-bin direction partitions closing for both thin source and escaped luminosity within \(2\times10^{-10}\).
- The complete non-empty radius-energy-direction joint table closing to the regional thin source and escaped luminosity within \(2\times10^{-10}\).
- Joint-table global fractions reproducing each region's global source and escaped-luminosity fractions.
- The 8–15 km region contributing between 75% and 85% of the global B.1 source.
- Production axial-vector source, transport, JSON, PDF, and PNG outputs remaining unchanged.

**Sparse-table convention:** the joint table stores non-empty cells only. A one-dimensional partition can contain a zero-weight bin absent from the joint table. The validator treats an absent bin as zero only when the stored marginal for that bin is exactly zero. Missing non-zero bins and unexpected joint labels remain hard failures. For this result, the 10–11 MeV bin in the 8–15 km region has exactly zero thin-source and escaped-luminosity weight.

## 6. Accepted result and evidence

The strict production run was repeated with the current validator and ULP-tolerant archived-node comparison on 2026-11-23:

- [Energy-grid identity diagnostic, run #45171900209](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45171900209).
- [Strict 10 MeV phase-space reproduction, run #45172485856](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45172485856).
- [Independent output-validator suite, run #45173157775](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45173157775).

The strict calculation used the original 842-node reference array. The runtime SHA-256 can differ by one ULP on a threshold node; the archived node-by-node comparison uses \(\\mathrm{rtol}=5\\times10^{-15}\), zero absolute tolerance, and retains the original baseline SHA-256 unchanged.

Archived files:

- \`outputs/b16_escape_phase_space_10mev_2026-11-17.json\`: complete machine-readable result, including the full non-empty joint radius-energy-direction table.
- \`B16_ESCAPE_PHASE_SPACE_10MEV_RESULT_2026-11-17.md\`: numerical summary, closure residuals, regional fractions, and interpretation boundary.

Key closure residuals:

| Check | Residual |
|---|---:|
| Luminosity vs archived high-order baseline | \(-2.220446049250313\times10^{-16}\) |
| Optically thin luminosity vs baseline | \(0\) |
| Escape probability vs baseline | \(-5.421010862427522\times10^{-20}\) |
| Maximum joint-to-marginal residual | \(6.661338147750939\times10^{-16}\) |

The 8–15 km region contains 79.6522% of the global thin source and 86.8551% of the escaped luminosity.

## 7. Historical failed-run fingerprint

The earlier workflow run [#43205614274](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43205614274), on commit \`f19a4485a19f1d862d9dcd6f7703bc72259566ae\`, recorded the energy hash \`db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639\` and stopped before producing the canonical JSON.

The 2026-11-23 cross-runner comparison identifies this fingerprint as a one-ULP floating-point variant of the archived 842-node reference, not a different physical grid. In the successful strict run #45172485856, the maximum absolute node difference is \(5.684341886080802\\times10^{-14}\) MeV, the maximum relative difference is \(1.1675488289093305\\times10^{-16}\), and the maximum difference is one ULP. The reference file retains the original SHA-256 \`036e6d77...\`; no baseline hash was changed.

## 8. Interpretation boundary and remaining work

The accepted phase-space result reproduces the archived high-order vector baseline. It does **not** reproduce the digitized Fig. 7 10 MeV strong-absorption endpoint: the calculated luminosity is \(2.439635957361032\times10^{52}\) erg/s, versus the digitized reference \(1.26781475907372\times10^{52}\) erg/s, a \(+92.4284\%\) difference.

That discrepancy remains a separate open audit requiring the local-rate, polarization, and escape evidence package. It is not resolved by the baseline phase-space closure. No empirical opacity rescaling, change of physical convention, or axial-vector constraint update is authorized by this runbook.
