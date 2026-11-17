# Individual review: six B.16 high-energy propagation and GR records

Review date: 2026-11-15. Baseline branch: `maintenance/repository-organization-audit-20261114`. Six B.16 records were read in full and cross-checked against their Python source, test modules, archived JSON, and historical GitHub Actions logs. The review now includes strict NumPy reproductions of all four high-energy V8 diagnostics; this is an implementation/provenance review, not a full new Fig. 7 parameter scan.

## 1. Document-by-document outcomes

| Document | Outcome | Findings and disposition |
|---|---|---|
| `B16_GR_ENERGY_AND_RAY_PROPAGATION_REQUIREMENTS_2026-11-09.md` | `PASS_WITH_NOTES` | The distinction between the paper's flat pseudo-Newtonian Euclidean-chord prescription and a full-GR extension is correct. The generic static-spherical ray kernel has seven passing tests, but is not applied to a fabricated SFHo metric. Clarified that the displayed Eq. (B.2) uses fixed \(\omega\); the path-redshift result is a separately labeled interpolation sensitivity. |
| `B16_HIGH_ENERGY_CHANNEL_KERNEL_AUDIT_2026-11-10.md` | `PASS_WITH_NOTES` | Corrected the Fermi-pair equation reference from B.25 to B.9 and fixed the reversed occupancy signs in the Python direct-angular helper. The full NumPy B.1+B.2 calculation now matches V8 luminosity to \(9.22\times10^{-13}\), escape probability to \(8.35\times10^{-13}\), and mean source-weighted \(\tau\) to \(1.75\times10^{-14}\). |
| `B16_HIGH_ENERGY_NU_CHORD_CONVERGENCE_2026-11-10.md` | `PASS_WITH_NOTES` | The Python implementation has now run all 108 combinations corresponding to the 36 rays and three opacity grids. Its five maximum-refinement metrics agree with V8 to a maximum relative difference of \(1.19\times10^{-9}\). |
| `B16_HIGH_ENERGY_OUTER_TEMPERATURE_SENSITIVITY_2026-11-10.md` | `PASS_WITH_NOTES` | Added the matching frozen-source \(210\text{--}510\) MeV NumPy calculation. All seven temperature scenarios reproduce the V8 escape and luminosity observables to better than \(2.5\times10^{-7}\) relative. The source is frozen; only B.2 opacity is recomputed. |
| `B16_HIGH_ENERGY_PATH_REDSHIFT_AUDIT_2026-11-10.md` | `PASS_WITH_NOTES` | Added the global energy-resolved NumPy reproduction using the archived V8 bilinear interpolation in radius and local energy. Its observables agree with V8 to better than \(3\times10^{-14}\). A separate direct-local-rate recomputation differs by \(+0.5021\%\) in escaped luminosity and is explicitly retained as an interpolation-method sensitivity, not silently mixed with the V8 prescription. |
| `B16_INDEPENDENT_ANALYTIC_PATH_INTEGRATION_AUDIT_2026-11-09.md` | `PASS_WITH_NOTES` | Full analytic B.2 path integration now reruns under pinned Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1 in Actions #43649694860. Same-grid reproduction is \(2.22\times10^{-16}\); Simpson-256 vs. QUADPACK angular escape averages agree to \(1.146\times10^{-6}\); final independent curve is within \(4.52\times10^{-5}\) of archived B.16. The +92.2493% Fig. 7 strong-endpoint residual remains. |

## 2. Source and test inspection

### Fermi-pair angular average

The paper's production kernel uses the two neutrino occupation factors \(f(E_1,\mu)f(E_2,-\mu)\); the blocking complements belong to the absorption integral. In `audit_b16_channel_resolved_energy.py`, the original `expit` arguments had the wrong signs. The corrected helper is
\[
\operatorname{expit}\!\left(\frac{\mu-E_1}{T}\right)
\operatorname{expit}\!\left(\frac{-\mu-E_2}{T}\right).
\]

The separate `audit_b16_neutrino_b7_b9_kernel.py` implementation uses a stable logistic function \(1/(1+e^x)\) with \(x=(E-\mu)/T\), which has the correct occupancy sign. Four pinned regression tests compare the direct angular implementations with the repository analytic average and published Eq. (B.9).

### Propagation and GR

- `audit_b16_high_energy_nu_chord_convergence.py` now has a strict NumPy output covering all 108 ray/grid cases.
- `audit_b16_high_energy_energy_resolved_numpy.py` computes the frozen-source outer-temperature sensitivity and the global fixed-\(\omega\)/path-redshift band comparison.
- The strict path-redshift reproduction implements the V8-documented bilinear interpolation in radius and local energy. The direct local-rate recomputation is retained separately to quantify interpolation-method sensitivity.
- `audit_b16_path_independent.py` is tied to the archived Python output by `run_commit_sha` and `code_sha256`. Its test module has five tests.
- `gr_ray_transport.py` is a generic geometry solver. Seven tests cover flat chords, redshift, toy Schwarzschild radial propagation, and finite-boundary/turning-point semantics. They do not supply the missing same-snapshot \(A(r)\) or \(M(r)\) profile.

## 3. Numerical evidence: NumPy versus V8

| Diagnostic | Strict NumPy result | Maximum difference from V8 |
|---|---|---:|
| Full channel-resolved B.1+B.2 luminosity | \(2.439635957361032\times10^{52}\,\mathrm{erg\,s^{-1}}\) | \(9.22\times10^{-13}\) relative |
| Full channel escape probability | \(3.2517740193528985\times10^{-4}\) | \(8.35\times10^{-13}\) relative |
| Source-weighted total mean \(\tau\) | \(16.128716668935596\) | \(1.75\times10^{-14}\) relative |
| 36-ray chord convergence | 108 cases; five maximum-refinement metrics | \(1.19\times10^{-9}\) relative |
| Outer-temperature sensitivity | Seven frozen-source scenarios | \(2.5\times10^{-7}\) relative for main observables |
| High-energy path-redshift | \(210\text{--}510\) MeV escaped luminosity shift \(-28.09487548\%\) | \(3\times10^{-14}\) relative |
| Independent analytic B.2 path | 25-point Simpson-256 curve; strong-endpoint residual \(+92.24931\%\) | \(4.52\times10^{-5}\) maximum relative difference vs. archived B.16 |

The path-redshift result is not an ambiguity in the printed equation. The published B.2 integrand uses fixed \(\omega\) along the chord. The \(-28.09\%\) result is the separate conserved-\(E_\infty\) sensitivity, retaining a Euclidean chord. The direct-local-rate alternative differs from the V8 bilinear interpolation by \(+0.5021\%\); both methods are archived and labeled separately.

The global all-energy redshift-only result, which moves the 10 MeV strong-endpoint Fig. 7 residual from about \(+92.24\%\) to \(+36.74\%\), remains a separate output and is not averaged with the high-energy-band \(-28.09\%\) result.

## 4. Pinned Python workflows and executed tests

All workflows pin Python 3.12.14, NumPy 2.5.4, and SciPy 1.18.1.

### Kernel regression

Run [#43646106550](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43646106550) passed 20/20 tests:
- Fermi-pair channel helper: 4/4;
- B.6/B.10/B.4 neutrino kernel: 4/4;
- independent analytic B.2 path helper: 5/5;
- generic GR ray kernel: 7/7.

### Full channel and chord reproductions

Run [#43647616434](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43647616434) completed:
- full channel-resolved B.1+B.2 calculation;
- 36-ray high-energy neutrino chord convergence;
- provenance checks;
- archived strict NumPy JSON outputs on the reviewed branch.

### Outer-temperature and path-redshift reproductions

Run [#43648694518](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43648694518) completed:
- seven frozen-source outer-temperature scenarios;
- global high-energy fixed-\(\omega\)/path-redshift comparison;
- five automated V8-versus-NumPy reproduction tests;
- strict NumPy JSON outputs archived on the reviewed branch.

### Full independent analytic B.2 path integration

Run [#43649694860](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43649694860) completed successfully on the pinned runtime. It passes five analytic-path unit tests, recomputes the complete 40-radius-node / 142-energy-node / 25-coupling calculation, validates output provenance and numerical closure, and archives the JSON output. The workflow now guards write-back to the reviewed maintenance branch.

These are independent reproducibility runs. They do not modify production source arrays, coupling values, the Fig. 7 digitization, or axial-vector constraints.

## 5. Remaining reproducibility and physical gates

1. The pinned end-to-end B.1+B.2 luminosity calculation is now complete (Actions #43651020195), using the separately pinned B.1 and B.2 outputs. It reproduces archived B.16 to 0.445059% maximum relative difference over all 25 couplings, with source closure at 2.14115e-5 relative. The Fig. 7 residual remains -9.2908% at weak coupling and +92.0542% at the strong endpoint. The next investigation is therefore the shared physical inputs and conventions—not another quadrature refinement: reconstructed public-figure profile versus the original Garching snapshot, shared local production/absorption kernels and muon-species convention, and fixed-local-energy versus energy-at-infinity interpretation. Do not rescale the source or opacity.
2. Keep the generic GR kernel separate from a physical full-GR SN result until same-snapshot \(N(r)\) and \(A(r)\) or \(M(r)\) data are available.
3. The public-figure reconstructed thermodynamic profile is not the original Garching raw snapshot; its provenance uncertainty remains.
4. The \(+92\%\) Fig. 7 strong-endpoint discrepancy remains unresolved. No opacity rescaling, source normalization adjustment, or fitted correction is authorized.

## 6. Physical disposition

The printed Eq. (B.2) uses fixed \(\omega\) along the Euclidean chord. The path-redshift branch is a separate counterfactual sensitivity and is not full GR. The missing \(A(r)\) or \(M(r)\) profile blocks a full-GR extension, not reproduction of the paper's stated flat-spatial-coordinate approximation.

No source, opacity, coupling, energy cutoff, production axial-vector output, or constraint curve is modified. The high-energy local kernel and path quadrature are now independently reproduced across NumPy and V8, but the physical Fig. 7 strong-endpoint mismatch remains open.

## 7. Baseline register

The 462-document baseline register now records **282 individually reviewed** and **180 pending**. Outcome totals: 2 PASS, 183 PASS_WITH_NOTES, 88 HISTORICAL, 9 REVISION_REQUIRED, and 180 PENDING.


## Current-tree and workflow reconciliation (2026-11-16)

All six source documents in §1 remain present. Their current Git blob IDs match the live tree and the baseline register's `current_blob_sha`; all six remain `PASS_WITH_NOTES` with `MATCH_CURRENT` fingerprints. The five cited pinned workflow runs (#43646106550, #43647616434, #43648694518, #43649694860 and #43651020195) were independently fetched and are completed successfully. This confirms the recorded implementation/test scope, including the corrected Fermi-pair occupancy signs and high-energy fixed-source/path-redshift reproductions.

The physical boundary remains unchanged: the path-redshift branch is not full GR without same-snapshot metric data; the fixed-(\omega) Euclidean chord is the printed B.2 baseline; and the Fig. 7 strong-endpoint mismatch remains approximately +92%. No rescaling, profile substitution, source/opacity adjustment, or axial-vector update is justified by these successful workflows.
