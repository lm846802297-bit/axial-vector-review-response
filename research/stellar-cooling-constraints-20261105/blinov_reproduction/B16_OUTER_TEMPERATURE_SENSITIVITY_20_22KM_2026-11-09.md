# B.16 temperature sensitivity in the 20--22 km shell

Date: 2026-11-09
Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.

## Motivation

The independent Bollig Fig. 1 and Fig. 4 vector-path audit validates Caputo T(r) and mu_mu/T through 20 km, but the original Bollig plotting frame ends at 20 km. The current 20--22 km profile is therefore not independently cross-checked against those original figures. The B.16 radial-path synthesis assigns 12.81% of the source-weighted neutrino inverse-decay path optical depth to this shell for the dominant 8--15 km emission region.

## Controlled variation

- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Only T_MeV is varied, and only for 20 <= r <= 22 km.
- mu_mu, mu_numu, lapse, radial grid, energy grid, angular quadrature, path quadrature, couplings, and Fig. 7 reference remain fixed.
- Scales 0.9 and 1.1 are stress tests, not statistical uncertainty intervals.
- Every scenario recomputes the complete B.1 source and B.2 opacity.

## Results

| T scale in 20--22 km | Weak L_escaped / baseline | Peak L_escaped / baseline | Strong L_escaped / baseline | Strong P_escape / baseline |
|---:|---:|---:|---:|---:|
| 0.9 | 99.9713% | 99.9133% | 99.8507% | 99.8792% |
| 1.0 | 100% | 100% | 100% | 100% |
| 1.1 | 100.038% | 100.091% | 100.151% | 100.112% |

## Baseline diagnostics

| Quantity | Baseline value |
|---|---:|
| B.1 thin-source fraction emitted in 20--22 km | 0.0745279% |
| B.2 path-tau fraction in 20--22 km, all emission radii | 12.8945% |
| B.2 path-tau fraction in 20--22 km, 8--15 km emission | 12.719% |

## Interpretation

The comparison separates a change in the B.1 thin source from a change in the B.2 escape probability. A small thin-source change with a larger escape-probability change identifies the 20--22 km shell as a propagation-input sensitivity, not an emission-normalization effect.

This is a sensitivity test of the current reconstructed profile, not a determination of the true uncertainty in the original SFHo-18.8 simulation. No result is used to tune the profile or rescale the vector curve.

## Reproducibility

- Script: audit_b16_outer_temperature_sensitivity.py
- Machine-readable output: outputs/b16_outer_temperature_sensitivity_20_22km_10mev_2026-11-09.json
- The production axial-vector curve remains frozen.
