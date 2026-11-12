# Bollig original-source thermodynamic profile audit: 15--22 km

Date: 2026-11-09
Source: Bollig et al., arXiv:2005.07141v7, Figs. 1 and 4.

## Scope

This extends the original-PDF vector-path comparison beyond the previously checked 5--15 km interval. It compares Caputo T(r) with Bollig Fig. 1 and Caputo mu_mu/T with Bollig Fig. 4. The combined mu_mu comparison is derived from T_Bollig times (mu_mu/T)_Bollig; it is not an independent third observable.

Only points inside the actual selected vector-path support and detected plot frame are compared. No extrapolation is performed. The original Garching simulation tables were not obtained in this audit.

## Source and curve support

- Bollig PDF SHA-256: 8267f8b1de184163308728c44000425ce58085c1d5bd799d0cbc1e4e8d740d61
- Caputo profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Fig. 1: page 1, drawing path 0, color [0.6999970078468323, 0.6999970078468323, 0.0].
- Fig. 4: page 2, drawing path 193, color [0.6999970078468323, 0.6999970078468323, 0.0].
- Fig. 1 usable radial support: [0.999973211957248, 19.99998543139328] km.
- Fig. 4 usable radial support: [0.9999994818700335, 20.000015543899178] km.
- Joint usable radial support: [0.9999994818700335, 19.99998543139328] km.

## Interval results

| Interval | Observable | Nodes | Mean abs. relative difference | Max abs. relative difference |
|---|---|---:|---:|---:|
| 15--20 km | T(r), Caputo vs Bollig Fig. 1 | 293 | 0.00429517% | 0.0162796% |
| 15--20 km | mu_mu/T, Caputo vs Bollig Fig. 4 | 294 | 0.00468416% | 0.0154741% |
| 15--20 km | mu_mu derived from T x mu_mu/T | 293 | 0.00511169% | 0.0212384% |
| 20--22 km | T(r), Caputo vs Bollig Fig. 1 | 0 | n/a | n/a |
| 20--22 km | mu_mu/T, Caputo vs Bollig Fig. 4 | 1 | 0.00233291% | 0.00233291% |
| 20--22 km | mu_mu derived from T x mu_mu/T | 0 | n/a | n/a |

## Selected radii

| target r (km) | profile node (km) | T_Bollig | T_Caputo | eta_Bollig | eta_Caputo | mu_mu,Bollig derived | mu_mu,Caputo |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | 15 | 13.23075 | 13.23142 | 4.707347 | 4.707185 | 62.28174 | 62.28272 |
| 16 | 16 | 9.538322 | 9.537411 | 4.941442 | 4.941567 | 47.13306 | 47.12976 |
| 17 | 17 | 7.405866 | 7.405305 | 4.449159 | 4.449351 | 32.94988 | 32.9488 |
| 18 | 18 | 5.919976 | 5.919927 | 3.953335 | 3.953468 | 23.40365 | 23.40424 |
| 19 | 19 | 4.881427 | 4.882019 | 3.646514 | 3.646417 | 17.80019 | 17.80188 |
| 20 | 20 | not covered | not covered | 3.513388 | 3.513306 | not covered | not covered |
| 20.5 | 20.5 | not covered | not covered | not covered | not covered | not covered | not covered |
| 21 | 21 | not covered | not covered | not covered | not covered | not covered | not covered |
| 21.5 | 21.5 | not covered | not covered | not covered | not covered | not covered | not covered |
| 22 | 22 | not covered | not covered | not covered | not covered | not covered | not covered |

## Interpretation

Zero supported nodes mean the original published vector curve does not cover that radial interval. This is not a failed numerical comparison: it is a lack of source coverage. Such a region must remain unvalidated by the published figure and must not be filled by extrapolation.

The 20--22 km interval must be classified separately from the 15--20 km interval. The reconstructed CSV can contain values there even when the original comparison curve does not.

No production rate, opacity, transport implementation, luminosity, vector benchmark, or axial-vector output is changed.

## Reproducibility

- Script: audit_bollig_outer_thermodynamic_profile.py
- Machine-readable output: outputs/bollig_outer_thermodynamic_profile_15_22km_2026-11-09.json
- PDF source: https://arxiv.org/pdf/2005.07141v7
