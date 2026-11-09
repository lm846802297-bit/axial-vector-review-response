# Current vertex-preserving B.16 global channel and radial decomposition (2026-11-09)

## Executive summary

This report uses the current vertex-preserving profile, SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`, and the archived full 10 MeV B.16 benchmark. It supersedes any channel or shell fraction inferred from the older profile SHA-256 08d7afce... for this benchmark.

The current B.2 source-weighted mean optical depth is dominated by neutrino inverse decay (89.7782%), with Compton contributing 10.2218%. The 15--20 km region contributes 27.8619% of the total optical depth, but 27.8538 percentage points are neutrino inverse decay. The muon-Compton contribution in the entire 15--20 km region is only 0.0080846% of the total. Therefore the approximately 10% Fig. 3 muon-density mismatch cannot be used to explain the large outer-shell path optical depth.

The fixed-\(\omega\) B.2 benchmark gives a strong-endpoint luminosity 92.2406% above the digitized Fig. 7 reference. A separately labeled path-redshift-only diagnostic reduces the discrepancy to +36.7448%, but does not remove it. This redshift-only variant is not the published Eq. (B.2) prescription and is not a full GR ray trace.

## 1. Frozen benchmark

- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`
- Fig. 7 reference SHA-256: `6a9f68add5dde4b41373702d0e10538985bc513db20a7152ebf2e143130aeac4`
- Mass: 10 MeV.
- Global quadrature: \(N_r=40, N_E=100, N_\Omega=16, N_s=32\).
- Fixed-\(\omega\) B.2 is the baseline.
- No production axial-vector output is modified.

## 2. B.1 source decomposition

| Channel | Fraction of optically thin source |
|---|---:|
| Compton | 32.0050% |
| Neutrino inverse decay | 67.9950% |
| Dimuon | 0% |

The radial source fractions (all channels) are:
| Shell | Fraction |
|---|---:|
| 12--15 km | 13.7184% |
| 15--18 km | 1.6462% |
| 18--20 km | 0.1772% |
| 20--22 km | 0.0745% |
| 22--25 km | 0.0728% |

The combined 15--20 km thin-source fraction is 1.8234%. This is not a per-channel decomposition; the exact channel-specific radial split is not inferred from the total-shell fractions.

## 3. B.2 source-weighted optical-depth decomposition

| Absorption channel | Fraction of total mean optical depth |
|---|---:|
| Compton | 10.2218% |
| Neutrino inverse decay | 89.7782% |
| Dimuon | 0% |

| Absorption shell | Total | Neutrino inverse decay | Compton |
|---|---:|---:|---:|
| 15-16.5 km | 7.9737% | 7.9657% | 0.008002% |
| 16.5-18.5 km | 11.0533% | 11.0532% | 0.000082% |
| 18.5-20 km | 8.8349% | 8.8349% | 0.000000% |
| 20-22 km | 11.5748% | 11.5748% | 0.000000% |
| 22-25 km | 17.3206% | 17.3206% | 0.000000% |

In 15--20 km, the total optical-depth fraction is 27.8619%, almost all of which is the neutrino inverse-decay channel (27.8538%). The Compton contribution is only 0.008085% of the total optical depth.

In the density-comparison interval 15--16.5 km, the Compton contribution is 0.008002% of the total. The Fig. 3 density residual affects the muon-Compton component, not the neutrino inverse-decay channel. The latter dominates the shell's path opacity.

## 4. Fixed-omega versus path-redshift-only diagnostic

| Quantity | Fixed-\(\omega\) Eq. (B.2) baseline | Path-redshift-only diagnostic |
|---|---:|---:|
| Weak endpoint relative difference vs Fig. 7 | -8.8853% | -8.8991% |
| Reference peak relative difference vs Fig. 7 | 2.5688% | -2.7704% |
| Strong endpoint relative difference vs Fig. 7 | 92.2406% | 36.7448% |
| Strong-endpoint luminosity shift vs fixed baseline | 0 | NaN% |

The path-redshift-only diagnostic uses \(\omega_{\rm loc}(s)=\omega_{\rm source}N_{\rm source}/N(s)\) in the local absorption kernel while retaining the same Euclidean path length and straight chord. It is a redshift-only sensitivity test, not full GR propagation. Appendix B, Eq. (B.2), explicitly evaluates the absorption rate at one fixed \(\omega\) along the chord, so fixed-\(\omega\) remains the paper-faithful baseline. The alternative demonstrates sensitivity to the energy prescription but cannot be substituted into the benchmark without a justified change of transport model.

## 5. Interpretation and next step

1. The current profile's outer-shell total opacity is large because of neutrino inverse decay, not because of the muon-density-dependent Compton channel.
2. The Fig. 3 density residual therefore does not explain the 15--20 km neutrino path contribution.
3. The path-redshift-only diagnostic substantially reduces, but does not eliminate, the strong-endpoint discrepancy; it is not the Eq. (B.2) baseline.
4. The remaining strong-endpoint mismatch must be investigated in the fixed-\(\omega\) implementation, its local neutrino inverse-decay kernel, and the source-weighted escape integral, rather than by adjusting the outer muon density.

## 6. Reproducibility

- Current B.16 machine-readable result: `outputs/b16_global_fig7_vertex_preserving_10mev_2026-11-09.json`
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`
- This report does not change the production axial-vector curve, the fixed-\(\omega\) baseline, or any source/opacity normalization.
