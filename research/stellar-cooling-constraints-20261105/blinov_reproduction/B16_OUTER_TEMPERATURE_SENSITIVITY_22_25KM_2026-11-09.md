# B.16 temperature sensitivity in the 22--25 km shell

Date: 2026-11-09
Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.

## Motivation

The 22--25 km shell is outside the original Bollig Fig. 1 and Fig. 4 frames. The current Caputo T(r) values in this interval are encoded off-frame PDF vector vertices, not visible plot data and not raw Garching simulation tables. The earlier direction-resolved B.16 synthesis assigns about 19.07% of the source-weighted neutrino inverse-decay path optical depth to this shell for dominant 8--15 km emission.

## Controlled variation

- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Off-frame baseline temperature range: [3.03377069226813, 3.55138904910432]
- Varied nodes: 222
- Only T_MeV is varied, and only for 22 <= r <= 25 km; mu_mu, mu_numu, lapse, radial grid, energy grid, angular quadrature, path quadrature, couplings, and Fig. 7 reference are fixed.
- Scales 0.9 and 1.1 are +/-10% stress tests; 0.7 and 1.3 are deliberately broad +/-30% stress tests. None is a statistical uncertainty interval.
- Every scenario recomputes the complete B.1 source and B.2 opacity.
- Global quadrature: N_r=40, N_E=100, N_omega=32, N_s=32.

## Results

| T scale in 22--25 km | Weak L_escaped / baseline | Peak L_escaped / baseline | Strong L_escaped / baseline | Strong P_escape / baseline |
|---:|---:|---:|---:|---:|
| 0.7 | 99.9369% | 99.6646% | 96.3809% | 96.4409% |
| 0.9 | 99.9701% | 99.8807% | 98.1867% | 98.2158% |
| 1.0 | 100% | 100% | 100% | 100% |
| 1.1 | 100.041% | 100.13% | 102.769% | 102.727% |
| 1.3 | 100.164% | 100.429% | 112.474% | 112.291% |

## Baseline diagnostics

| Quantity | Baseline value |
|---|---:|
| B.1 thin-source fraction emitted in 22--25 km | 0.0727628% |
| B.2 neutrino path-tau fraction in 22--25 km, all emission radii | 19.3314% |
| B.2 neutrino path-tau fraction in 22--25 km, 8--15 km emission | 19.1084% |

## Interpretation

The comparison separates the small B.1 emission contribution from the B.2 propagation effect. A change in escaped luminosity is primarily an outer-path opacity sensitivity if the thin-source ratio remains close to unity.

This is a stress test of the off-frame Caputo continuation, not a determination of the true uncertainty in the original SFHo-18.8 simulation. No result is used to tune the profile or rescale the vector curve.

## Reproducibility

- Script: audit_b16_outer_temperature_sensitivity_22_25km.py
- Machine-readable output: outputs/b16_outer_temperature_sensitivity_22_25km_10mev_2026-11-09.json
- Production axial-vector curve remains frozen.
