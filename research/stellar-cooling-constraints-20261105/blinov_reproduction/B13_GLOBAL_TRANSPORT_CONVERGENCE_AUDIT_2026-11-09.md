# Global B.13 exact-Compton transport convergence audit

Date: 2026-11-09  
Status: **all finest-step criteria passed**

## 1. Scope and fixed physics

This is Phase A only: global radial, energy, direction, and path quadrature convergence at the 10 MeV pure-vector benchmark. The B.13 local collision-kernel quadrature remains fixed at (12, 8, 8, 8), with the existing pointwise refinement check at (16, 10, 10, 10). No collision model, stellar profile, B.2 propagation convention, coupling normalization, or axial-vector calculation is changed.

- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Profile: 1687-row vertex-preserving reconstruction from public figures; not the original Garching raw simulation table.
- Transport: scalar, polarization-summed, fixed-omega Eq. (B.2).
- B.13 Compton source and reduced opacity are replaced together.
- Primary charge convention: mu-minus only, matching Eq. (B.17).
- Every scan point regenerates the B.16 reference on the identical grid and checks its closure before the B.13 replacement.

## 2. Grid configurations

| Case | Radial order | Energy order | Direction order | Path order |
|---|---:|---:|---:|---:|
| baseline | 40 | 100 | 16 | 32 |
| radial60 | 60 | 100 | 16 | 32 |
| radial80 | 80 | 100 | 16 | 32 |
| energy150 | 40 | 150 | 16 | 32 |
| energy200 | 40 | 200 | 16 | 32 |
| angle24 | 40 | 100 | 24 | 32 |
| angle32 | 40 | 100 | 32 | 32 |
| path48 | 40 | 100 | 16 | 48 |
| path64 | 40 | 100 | 16 | 64 |

The radial rule is composite over fixed interfaces at 0, 5, 8, 10, 12, 15, 18, 20, 22, 24, and 25 km. The final energy grid also includes radius-dependent emission-threshold nodes, so its node count exceeds the input energy order.

## 3. Pairwise convergence shifts

Each row changes only the named quadrature dimension. Shifts are fine grid relative to the immediately coarser grid. The table shows the B.13 mu-minus consistent source-plus-opacity result.

| Refinement | max all-coupling |ΔLthin| | max all-coupling |ΔPesc| | |ΔLtotal| at Fig. 7 peak | |ΔLtotal| at strong endpoint |
|---|---:|---:|---:|---:|
| radial 40 to 60 | 0.0107% | 0.0956% | 0.0159% | 0.1063% |
| radial 60 to 80 | 0.0970% | 0.2414% | 0.1273% | 0.3386% |
| energy 100 to 150 | 0.3218% | 0.0005% | 0.3212% | 0.3220% |
| energy 150 to 200 | 0.1120% | 0.0002% | 0.1118% | 0.1121% |
| angle 16 to 24 | 0.0000% | 0.0017% | 0.0008% | 0.0017% |
| angle 24 to 32 | 0.0000% | 0.0006% | 0.0001% | 0.0001% |
| path 32 to 48 | 0.0000% | 0.0016% | 0.0001% | 0.0016% |
| path 48 to 64 | 0.0000% | 0.0010% | 0.0007% | 0.0005% |

The machine-readable result also reports the same shifts for the B.16 reference implementation, separating convergence of the published approximate kernel from convergence of the exact B.13 replacement.

## 4. Finest-step acceptance

Provisional audit criteria: maximum all-coupling change in optically thin luminosity below 1%; change in luminosity at the digitized Fig. 7 peak below 1%; and change at the strong-coupling endpoint below 2%. These are numerical tolerances, not physical bounds.

| Dimension | Finest comparison | Lthin < 1% | Peak Ltotal < 1% | Strong-end Ltotal < 2% | Result |
|---|---|---:|---:|---:|---|
| radial | radial 60 to 80 | PASS | PASS | PASS | **PASS** |
| energy | energy 150 to 200 | PASS | PASS | PASS | **PASS** |
| angular | angle 24 to 32 | PASS | PASS | PASS | **PASS** |
| path | path 48 to 64 | PASS | PASS | PASS | **PASS** |

## 5. Escape and radial-source diagnostics

Pesc is reported separately because source and escape changes can cancel in Ltotal. The aggregate JSON records the 5–10 km and 10–15 km fractions of the B.1 source and escaped strong-endpoint luminosity for B.16 and B.13.

| Case | B.13 source, 5–10 km | B.13 escaped L, 5–10 km | B.13 source, 10–15 km | B.13 escaped L, 10–15 km |
|---|---:|---:|---:|---:|
| angle24 | 52.9459% | 67.0387% | 43.4290% | 30.0552% |
| angle32 | 52.9459% | 67.0385% | 43.4290% | 30.0550% |
| baseline | 52.9459% | 67.0381% | 43.4290% | 30.0558% |
| energy150 | 52.9461% | 67.0386% | 43.4290% | 30.0561% |
| energy200 | 52.9462% | 67.0388% | 43.4291% | 30.0562% |
| path48 | 52.9459% | 67.0389% | 43.4290% | 30.0551% |
| path64 | 52.9459% | 67.0392% | 43.4290% | 30.0548% |
| radial60 | 52.9510% | 66.9941% | 43.4257% | 30.0375% |
| radial80 | 53.0023% | 67.0979% | 43.3768% | 29.9286% |

## 6. Closure and decision

Every grid point must reproduce its own same-grid B.16 baseline with maximum relative residual below 2e-10. B.13 detailed-balance, absorption/production, and final muon-shell residuals must remain below 1e-10. Each job commits its compact numerical summary directly to the research branch. Full local-rate arrays and matching B.16 files are generated in the job workspace but are not persisted; the exact configurations and scripts allow them to be regenerated.

No empirical source, opacity, coupling, or luminosity rescaling is applied. No axial-vector curve is regenerated or modified. If a finest-step criterion fails, Phase A remains open and only the failed quadrature dimension is refined.

## 7. Reproducibility

- Aggregate JSON: outputs/b13_global_convergence_summary_2026-11-09.json
- Per-grid summaries: outputs/b13_global_convergence_2026-11-09/summary_*.json
- Full local-rate arrays and matched B.16 files: associated GitHub Actions workflow artifacts.
- Scripts: audit_b16_global_redshift.py, audit_b13_global_transport.py, summarize_b13_global_transport.py, summarize_b13_convergence.py.

## Companion 0.1 MeV scan: not converged

The companion 0.1 MeV vertex-preserving scan is archived separately in `outputs/b13_global_convergence_vertex_preserving_0p1mev_2026-11-09.json`. It records `overall_passed=false` and `overall_grid_passed=false`. The angular (24 to 32), energy (150 to 200), and path (48 to 64) refinements pass their stated criteria, but the radial 60 to 80 refinement does not:

- Maximum relative change in the optically thin source: 0.3173% (passes the 1% criterion).
- Maximum relative change in total luminosity: 5.2749% (fails the 2% strong-endpoint criterion).
- Maximum relative change in escape probability: 4.9419% (fails the 1% criterion).

Accordingly, the 0.1 MeV result is retained as an unresolved convergence diagnostic and must not be described as converged. The 10 MeV convergence result above applies only to its own fixed-\(\omega\) vector benchmark; it does not establish agreement with Fig. 7 or validate the complete supernova transport model.
