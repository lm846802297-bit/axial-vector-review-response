# 50th review — B.16 and repository baseline closeout

Date: 2026-11-17  
Branch: `maintenance/close-baseline-revision-required-20261117`

## Executive disposition

This review closes the seven baseline `REVISION_REQUIRED` records carried
forward by the previous repository audit, but it does **not** claim that every
underlying physical question is solved. The distinction is:

- **Repository deliverable / provenance gate:** the missing producers,
  inputs, tests, artifact archives, and documented limitations now have
  explicit evidence or a bounded, transparent disposition.
- **Physical acceptance gate:** the pure-vector 10 MeV Fig. 7 benchmark
  remains discrepant by (+92.4284\%). No opacity rescaling, fitted
  correction, or axial-vector constraint update is authorized.

No manuscript, referee-response result, production axial source/transport
code, or axial constraint curve was modified in this closeout.

## 1. Seven baseline revision-required records

| Previous record | Closeout evidence | Disposition |
|---|---|---|
| PR52 `SHA256SUMS.txt` — decompressed CSV not available | Streaming extractor and verifier; workflow [#44033029862](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44033029862) verified the 20,156,701-byte gzip and the 80,770,035-byte decompressed CSV, 73,728 rows × 77 columns, no malformed rows. | `PASS_WITH_NOTES`: canonical compressed archive retained; exact decompression is reproducible on demand; no 80.8 MB duplicate added to Git history. |
| B.16 escape phase-space runbook — energy-grid mismatch / missing strict JSON | Energy grid reconstructed from the archived B.1 spectral measure; 842 nodes, exact SHA-256 match and max relative node difference (2.69\times10^{-16}\). Workflow [#44035746636](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44035746636) passed 8 tests and all closure/normalization checks. JSON, 660-row CSV and 8-panel SVG archived. | `PASS_WITH_NOTES` for reproducible artifact package; physical Fig. 7 mismatch remains. |
| FIG7 10 MeV local-rate/polarization/escape audit — missing complete handoff | Local-rate/polarization 54-point package passed in [#44031506218](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44031506218); global B.1/B.2 escape phase-space package passed in [#44035746636](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44035746636). Both have source, inputs, tests, JSON and CSV/SVG outputs. | `PASS_WITH_NOTES` for package completeness; no claim of physical Fig. 7 acceptance. |
| Muon chemical-potential source audit — charge convention and profile mismatch | Both (n_{\mu^-}), (n_{\mu^+}), net and total densities are tabulated at common 12–15 km vertices. The largest (\mu^+) fraction is 0.0856%; the charge convention changes the Fig. 3 comparison by at most about 0.09 percentage points. | `PASS_WITH_NOTES`: charge-convention diagnostic is closed; public Fig. 3 label convention and the 6–10% absolute density offset remain unresolved source-level issues. |
| Profile input audit — missing profile fingerprint / common-vertex charge check | The composite profile is pinned to SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`, Git blob `e41df78c8035540760fbcb7ef592cd830171822e`, 1687 rows; both charge definitions are recorded. | `PASS_WITH_NOTES`: identity and diagnostic are complete; reconstructed public-figure profile is not raw Garching data and the absolute-density discrepancy is not rescaled away. |
| Original-UV convergence validation — reference convention / producer attribution | Legacy order-sweep CSV uses order 10 as its reference; the current driver uses the highest requested order. Exact historical producer is unrecovered, so direct attribution is withdrawn. Separate width-code fingerprints and historical-blob limitation are recorded. | `PASS_WITH_NOTES`: provenance ambiguity is explicitly bounded; no model-specific convergence claim is inferred from the legacy generic-kernel CSV. |
| Two-VEV convergence validation — reference convention / coupled azimuthal scan | Same shared legacy CSV and order-10 reference convention documented. (n_\phi=2n_{\rm GL}) at every row, so the scan is joint quadrature refinement, not independent azimuthal convergence. | `PASS_WITH_NOTES`: the historical benchmark is retained with its limitations; no independent (n_\phi) convergence or supernova exclusion is claimed. |

## 2. B.16 numerical closeout

The strict high-order 10 MeV configuration is:

- (n_r=200), (n_{\rm opacity}=640), (n_E=842), angular order 32,
  path order 64.
- Python 3.12.16, NumPy 2.5.4, SciPy 1.18.1.
- Profile SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Energy grid exact SHA-256 matches the archived baseline; max relative node
  difference (2.69\times10^{-16}\).

| Quantity | Result |
|---|---:|
| Calculated luminosity | (2.4396359574\times10^{52}\) erg/s |
| Fig. 7 reference | (1.2678147591\times10^{52}\) erg/s |
| Relative difference | (+92.4284\%\) |
| Global source-weighted escape probability | (3.25177\times10^{-4}\) |
| 8–15 km share of B.1 source | 79.6522% |
| 8–15 km share of escaped luminosity | 86.8551% |

The integrated luminosity closes against the archived high-order baseline at
(2.22\times10^{-16}\); the thin-source closure is zero and the escape
probability absolute residual is (5.42\times10^{-20}\). All regional
marginals and complete joint radius-energy-direction partitions pass.

The phase-space CSV contains 660 rows (508 all-radius plus 152 core-region
non-empty bins) and 13 columns. The SVG has 8 direction-resolved panels.
The heatmap display floor clips values below (10^{-8}) of the maximum only
for visualization; no rows are removed from the CSV or JSON.

## 3. PR52 scan archive extraction

The compressed archive remains the canonical Git object. The on-demand
extractor streams decompression, checks gzip CRC, verifies compressed and
uncompressed SHA-256/byte counts, and checks row/column consistency. The
80,770,035-byte expanded CSV is not committed because it duplicates the
20,156,701-byte gzip in every clone and in Git history. Use:

```bash
python extract_and_verify_scan_archive.py --output /path/to/original_uv_width_scan.csv
```

The default invocation verifies in a temporary directory and leaves no large
expanded file in the repository. The exact archive and extraction evidence is
recorded in `scan_archive_integrity_2026-11-17.json`.

## 4. Thermal-convergence CSV provenance

The shared eight-row CSV is byte-identical on the Original-UV and Two-VEV
branches. It is a legacy generic-kernel table, not two independent
model-specific convergence studies. Its order-sweep relative columns are
referenced to order 10, whereas the current driver uses the highest requested
order. The exact producer is unrecovered; direct attribution is withdrawn.
The Two-VEV order sweep couples (n_\phi=2n_{\rm GL}), so it cannot support
an independent azimuthal-convergence statement.

See
`docs/repository-management/THERMAL_CONVERGENCE_CSV_PROVENANCE_2026-11-17.md`.
No supernova luminosity, opacity, trapping or exclusion is inferred from this
homogeneous optically thin benchmark.

## 5. Remaining physical and source-level limitations

1. The pure-vector fixed-(\omega\) B.2 10 MeV prediction remains 92.43%
   above Fig. 7. The new decomposition diagnoses the current result; it does
   not explain the discrepancy.
2. The public Caputo/Bollig Fig. 3 muon-density label convention is not
   resolved by the plotted label alone. The single-(\mu^-\) B.17 source
   convention is retained; the net density is not substituted into the
   kernel.
3. The reconstructed profile is a public-figure reconstruction and composite
   input, not the raw same-snapshot Garching simulation arrays.
4. The local B.14 Compton polarization split is the no-recoil Thomson-limit
   approximation, not an exact recoil-resolved three-mode kernel.
5. The thermal-convergence CSV is a legacy homogeneous-cell benchmark; its
   exact historical producer is unknown and its Two-VEV azimuthal order is
   coupled to the Gauss-Legendre order.

No opacity rescale, arbitrary factor, boundary fit, or axial-vector curve
update is permitted on the basis of these results.

## 6. Repository state

The audit register is updated in the same closeout branch to reflect the
seven dispositions above and to fingerprint the current document versions.
The new provenance note and this review report are registered. The
maintenance branch has not been merged; no open pull request was present at
the time of this review. The next repository step is a final diff/PR review,
not a scientific promotion of the blocked vector benchmark.
