# B.16 unresolved mu_numu floor sensitivity in 20--22 km

Date: 2026-11-09
Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.

## Motivation

The Caputo reconstruction sets mu_numu=0 in 20--22 km because no resolved branch is present above the approximately 1 MeV figure floor. Bollig Figs. 1 and 4 do not cover this radial interval. The 20--22 km shell contributes about 12.7--12.8% of the source-weighted neutrino inverse-decay path optical depth for the dominant 8--15 km emission region.

## Controlled variation

- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Only mu_numu is varied, and only in 20--22 km; T, mu_mu, lapse, radial grid, and all other inputs are fixed.
- The assigned values +1 MeV and -1 MeV are figure-floor stress tests, not inferred profiles or statistical uncertainty intervals.
- Every scenario recomputes the complete B.1 source and B.2 opacity.
- Global quadrature: N_r=40, N_E=100, N_omega=32, N_s=32.

## Results

| mu_numu in 20--22 km | Weak L_escaped / baseline | Peak L_escaped / baseline | Strong L_escaped / baseline | Strong P_escape / baseline |
|---:|---:|---:|---:|---:|
| -1 MeV | 99.9998% | 100.005% | 100.009% | 100.009% |
| 0 MeV | 100% | 100% | 100% | 100% |
| +1 MeV | 99.9998% | 100.005% | 100.009% | 100.009% |

## Baseline diagnostics

- B.1 thin-source fraction emitted in 20--22 km: 0.0745279%.
- B.2 neutrino path-tau fraction in 20--22 km for 8--15 km emission: 12.719%.

## Sign symmetry and interpretation

The +1 MeV and -1 MeV cases are compared explicitly. A near-unity ratio is a numerical check of the expected charge-conjugation symmetry of the pair-production/absorption phase space under the symmetric angular integration; any residual is reported rather than assumed away.

The stress test quantifies only the unresolved chemical-potential floor. It does not establish the true mu_numu profile and is not used to tune the background or rescale the vector curve.

## Reproducibility

- Script: audit_b16_outer_numu_floor_sensitivity.py
- Machine-readable output: outputs/b16_outer_numu_floor_sensitivity_20_22km_10mev_2026-11-09.json
- Production axial-vector files and constraints remain unchanged.
