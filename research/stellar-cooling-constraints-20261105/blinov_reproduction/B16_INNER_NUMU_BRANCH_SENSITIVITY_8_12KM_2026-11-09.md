# B.16 negative mu_numu branch sensitivity in 8--12 km

Date: 2026-11-09
Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.

## Motivation

The Caputo profile contains a resolved negative mu_numu branch throughout 8--12 km. Its baseline range is -20.43 to -4.31 MeV, with mu_numu/T from -0.526 to -0.166. This interval lies in the main 8--15 km emission region and contributes appreciably to the neutrino inverse-decay path. The 12--15 km figure-floor test does not test this larger inner negative branch.

## Controlled variations

- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Only mu_numu is changed, only in 8--12 km. T, mu_mu, lapse, radial grid, energy grid, angular quadrature, path quadrature, couplings, and Fig. 7 reference are fixed.
- scale=0 removes the branch; scales 0.9 and 1.1 vary its magnitude by +/-10%; scale=-1 flips the sign solely as a symmetry diagnostic.
- Every scenario recomputes the complete B.1 source and B.2 opacity.
- Global quadrature: N_r=40, N_E=100, N_omega=32, N_s=32.

## Strong-endpoint results

| mu_numu treatment in 8--12 km | L_escaped / baseline | P_escape / baseline | Shift in L/L_Fig.7 - 1 |
|---|---:|---:|---:|
| sign-flipped branch | 100% | 100% | 0% |
| branch set to zero | 99.9777% | 99.6724% | -0.0428278% |
| magnitude reduced 10% | 99.9958% | 99.9382% | -0.00813379% |
| baseline negative branch | 100% | 100% | 0 |
| magnitude increased 10% | 100.005% | 100.068% | 0.00898796% |

## Baseline diagnostics

- B.1 thin-source fraction emitted in 8--12 km: 65.893%.
- B.2 neutrino path-tau fraction in 8--12 km for 8--15 km emission: 15.9324%.
- B.2 neutrino path-tau fraction in 8--12 km for all emission radii: 15.1246%.

## Charge-conjugation sign check

| Coupling point | L(sign-flipped)/L(baseline) | P_escape(sign-flipped)/P_escape(baseline) |
|---|---:|---:|
| weak_endpoint | 1 | 1 |
| reference_peak | 1 | 1 |
| strong_endpoint | 1 | 1 |

## Interpretation

The sign-flip test checks whether the integrated neutrino-antineutrino pair phase space is invariant under mu_numu -> -mu_numu after symmetric angular integration. The magnitude and zero-branch tests quantify the sensitivity to the negative branch itself.

The scale=0 case is an extreme counterfactual, not a proposed physical profile. The +/-10% cases are controlled stress tests, not statistical uncertainty intervals. No profile or luminosity rescaling is applied.

## Reproducibility

- Script: audit_b16_inner_numu_branch_sensitivity.py
- Machine-readable output: outputs/b16_inner_numu_branch_sensitivity_8_12km_10mev_2026-11-09.json
- Production axial-vector files and constraints remain unchanged.
