# B.2 path-energy and radial convergence status (2026-11-09)

## Executive summary

The three-mass B.2 path-energy audit completed successfully on the vertex-preserving reconstructed SFHo-18.8 profile (SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`). It compares the literal fixed-`omega` Eq. (B.2) implementation with a separate redshift-only diagnostic,
`omega_local(s)=omega_source N(r_source)/N(r(s))`, while keeping the Euclidean chord and path measure unchanged.

The energy-convention effect is coupling dependent and grows toward strong absorption. On the highest tested grid (80 radial, 200 energy, 32 angular, 64 path nodes), the redshift-only luminosity at the strong-coupling endpoint shifts relative to fixed-`omega` by approximately:
- 0.1 MeV: -5.64%;
- 1 MeV: -11.55%;
- 10 MeV: -28.85%.

These are sensitivity results, not evidence that the authors' unpublished code used the redshifted prescription. They are not full-GR ray tracing.

## 1. Fixed-omega versus path-redshift comparison

| mV | Fixed-omega strong-end residual vs Fig. 7 | Redshift-only strong-end residual vs Fig. 7 | Redshift-only shift vs fixed-omega |
|---:|---:|---:|---:|
| 0.1 MeV | -20.25% | -24.75% | -5.64% |
| 1 MeV | -5.34% | -16.17% | -11.55% |
| 10 MeV | +92.46% | +36.93% | -28.85% |

The 0.1 and 1 MeV absolute luminosity curves do not yet pass the full radial-grid convergence gate below, so their residuals are provisional. The relative path-redshift shift is much more stable across the tested grids: at the strong endpoint it changes from -5.06% to -5.29% at 0.1 MeV, from -11.43% to -11.55% at 1 MeV, and from -28.87% to -28.85% at 10 MeV when comparing the original 40x100x16x32 grid with the 80x200x32x64 grid.

The 10 MeV global quadrature scan passes all tested one-factor and combined-grid criteria. It is retained as a transport stress test, not as the primary low-mass Compton benchmark.

## 2. What has converged and what has not

The B.2 path-energy scan varies radial, energy, angular, and path orders independently, and also tests a combined fine grid. Energy refinement 150 to 200, angular refinement 24 to 32, and path refinement 48 to 64 each change the luminosity by less than 1% for all three masses.

The radial 60 to 80 comparison is the limiting dimension:
| mV | Maximum luminosity change, radial 60 to 80 |
|---:|---:|
| 0.1 MeV | 7.63% |
| 1 MeV | 1.87% |
| 10 MeV | 0.36% |

The combined 80x200x32x64 grid therefore fails the 1% global criterion at 0.1 and 1 MeV, while passing at 10 MeV. This is why the low-mass path-energy curves must not yet be treated as converged.

## 3. Opacity interpolation is a separate numerical dimension

An independent audit fixes the B.1 source quadrature and varies only the radial grid used to tabulate/interpolate the B.2 absorption rate.

For 0.1 MeV, the maximum luminosity change falls from 1.74% (160 to 240 opacity nodes) to 0.436% (240 to 320), 0.403% (320 to 480), and 0.158% (480 to 640). For 1 MeV, 80 to 120 nodes already gives 0.765%, with subsequent changes below 0.55%. For 10 MeV, all tested transitions pass the 1% threshold.

This opacity-grid convergence does not remove the separate source-radial quadrature sensitivity. The two must not be conflated.

## 4. Follow-up radial-source convergence

A dedicated follow-up audit now varies the B.1 source radial quadrature over orders 80, 100, 120, 160, and 200 while holding the B.2 opacity interpolation grid fixed at 640 nodes, and holding energy/angular/path quadratures at 100/16/32. This decouples source radial integration from opacity interpolation and is running for 0.1 and 1 MeV.

The audit is designed to identify the minimum radial order at which both the fixed-`omega` and redshift-only luminosity curves stabilize to the project 1% numerical target. This target is a numerical screening criterion, not a physical uncertainty estimate.

## 5. Interpretation and guardrails

1. Keep literal fixed-`omega` B.2 as the paper-faithful baseline.
2. Keep the path-redshift-only branch as a distinct sensitivity test.
3. Do not call the redshift-only result a full-GR transport calculation: the spatial metric factor and corresponding ray geometry are not included.
4. Do not apply an empirical opacity or luminosity rescaling.
5. Do not update the axial-vector constraint curve until the pure-vector reference benchmark and the relevant global numerical convergence checks pass.

## 6. Reproducibility

- Three-mass path-energy scan: [Run #42579746452](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42579746452)
- Isolated opacity interpolation scan: [Run #42581429474](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42581429474)
- High-order source radial scan (0.1 and 1 MeV): initial CI attempts exposed and fixed a metadata-key issue and then a literal line-break syntax issue. The current decoupled run [#42583529538](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42583529538) holds the opacity interpolation grid at 640 nodes while refining the B.1 source radial order from 80 to 200; at the time of this report update, its two mass jobs are running.
- Machine-readable path-energy results: `outputs/b2_path_energy_convergence_2026-11-09.json`
- Machine-readable opacity-grid results: `outputs/b2_opacity_interpolation_convergence_2026-11-09.json`

The failed initial radial workflow attempts are retained as transparent debugging records. They failed before producing scientific results (first a metadata-key mismatch, then a syntax issue); the current run uses the corrected script and decoupled opacity grid.


## 7. Method correction and replacement run (2026-11-09)

The first high-order source-radial attempt, Run #42583529538, is **not accepted as a convergence result**.

Two independent issues were identified:

1. The output writer appended a literal backslash-n sequence to the JSON payload. The numerical calculation step completed, but the validation step failed with `JSONDecodeError: Extra data`. This is a serialization failure, not a physics or quadrature failure.
2. The first implementation formed the interpolation grid as `unique([0, source_r, opacity_r, R])`. Consequently, changing the B.1 source-radial order also changed the B.2 opacity interpolation grid. Because the energy grid additionally included `m_A'/N(r_i)` at every point of that combined grid, it changed the energy nodes as well. That implementation did not isolate the B.1 radial quadrature and its output is not used as scientific evidence.

The corrected implementation separates the grids explicitly:

- The B.1 source radii and weights are generated from the variable source order (80, 100, 120, 160, 200). Source-local rates are evaluated directly at these nodes.
- The B.2 opacity profile and rates are evaluated on the fixed opacity grid generated with order 640, including only the fixed grid and the two radial endpoints. Source nodes are not inserted into this interpolation grid.
- The energy grid is constructed from the fixed opacity-grid lapse values and the base energy order 100. Its actual node count and SHA-256 are recorded; both must remain identical across the five source-radial orders.
- The path integrals are evaluated for each source radius against the same fixed opacity grid. The path-redshift diagnostic receives the source lapse evaluated at the source node, rather than assuming that the source node belongs to the opacity grid.
- The workflow checks that the source-grid hashes vary, while the opacity-grid and energy-grid hashes remain identical. It also retains the fixed profile SHA-256 and verifies that the production axial-vector files are unchanged.

The JSON serialization is corrected. The replacement run is [Run #42585236139](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42585236139), currently running on commit `799de095c74e344cb77ffc41fd722738d1343dad`.

Until that run passes its numerical and isolation checks, no B.1 source-radial convergence conclusion is drawn. The earlier 0.1 and 1 MeV outputs are excluded. No axial-vector production result or constraint curve is modified.


## 8. First accepted independent source-radial result and filename correction (2026-11-09)

Run #42585236139 produced the first accepted independent-grid result for 0.1 MeV. The 0.1 MeV job completed the calculation, passed all grid-isolation and production-file checks, and archived its JSON output:

`outputs/b2_radial_source_convergence_0.1mev_2026-11-09.json`.

The recorded grid identities are:
- Source radial nodes: 80, 100, 120, 160, and 200; all five source-grid hashes differ.
- Fixed B.2 opacity grid: 642 nodes, identical SHA-256 across all five source orders.
- Fixed energy grid: 742 nodes, identical SHA-256 across all five source orders. The configured energy order is 100, with the fixed opacity-grid lapse-threshold nodes added to that base grid.
- Profile SHA-256 remains `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

The maximum absolute luminosity changes between adjacent source-radial orders are:

| Source order transition | Fixed-omega | Path-redshift diagnostic |
|---|---:|---:|
| 80 to 100 | 0.7466% | 0.7465% |
| 100 to 120 | 0.1978% | 0.1976% |
| 120 to 160 | 0.1556% | 0.1550% |
| 160 to 200 | 0.1437% | 0.1437% |

Thus the 0.1 MeV B.1 source-radial integral passes the project's 1% adjacent-grid screening criterion on the fixed opacity and energy grids. This is a source-radial convergence result only: energy/angular/path orders remain 100/16/32 in this isolation scan, so its Fig. 7 residuals are not substituted for the separate higher-order global B.2 result.

The 1 MeV numerical calculation in Run #42585236139 also completed and printed the same grid-isolation metadata, but its validation step looked for `..._1.0mev_...` while the run step had written `..._1mev_...`. This is a workflow filename-normalization error; it is not a numerical or physics failure. The 1 MeV JSON was therefore not archived or accepted.

The validation now uses the same matrix mass string as the calculation and archive steps. The corrected replacement workflow is [Run #42586195530](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42586195530), currently running both mass points so each receives the same end-to-end validation.
