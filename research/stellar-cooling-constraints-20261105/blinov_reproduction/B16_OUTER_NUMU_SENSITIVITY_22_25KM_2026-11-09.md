# B.16 unresolved mu_numu continuation sensitivity in 22--25 km

Date: 2026-11-09
Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.

## Motivation

The original Bollig Figs. 1 and 4 stop at 20 km. The current profile sets mu_numu=0 in 22--25 km because no resolved chemical-potential branch is available there. This shell contributes about 19.1% of the source-weighted neutrino inverse-decay path optical depth for dominant 8--15 km emission. Its chemical-potential continuation therefore deserves a direct stress test, independently of the temperature-only variation.

## Controlled variation

- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
- Only mu_numu is varied, and only in 22--25 km; T, mu_mu, lapse, radial grid, and all other inputs are fixed.
- The assigned values +/-1 and +/-3 MeV are stress tests, not inferred profiles or statistical uncertainty intervals.
- Every scenario recomputes the complete B.1 source and B.2 opacity.
- Global quadrature: N_r=40, N_E=100, N_omega=32, N_s=32.

## Results

| mu_numu in 22--25 km | Weak L_escaped / baseline | Peak L_escaped / baseline | Strong L_escaped / baseline | Strong P_escape / baseline |
|---:|---:|---:|---:|---:|
| -3 MeV | 99.9981% | 100.072% | 100.15% | 100.153% |
| -1 MeV | 99.9998% | 100.008% | 100.017% | 100.017% |
| 0 MeV | 100% | 100% | 100% | 100% |
| +1 MeV | 99.9998% | 100.008% | 100.017% | 100.017% |
| +3 MeV | 99.9981% | 100.072% | 100.15% | 100.153% |

## Baseline diagnostics

- B.1 thin-source fraction emitted in 22--25 km: 0.0727628%.
- B.2 neutrino path-tau fraction in 22--25 km for 8--15 km emission: 19.1084%.

## Sign symmetry

The +1/-1 MeV and +3/-3 MeV pairs are compared explicitly. The pair-production phase space is expected to be invariant under mu_numu -> -mu_numu after exchanging neutrino and antineutrino. The numerical ratios are reported rather than assumed.

## Interpretation limits

This test addresses only the unresolved muon-neutrino chemical-potential continuation. It does not establish the true outer profile. The temperature-only 22--25 km stress test is a separate result. The scenarios are not combined into a statistical error band and are not used to tune the background or rescale the vector curve.

## Reproducibility

- Script: audit_b16_outer_numu_sensitivity_22_25km.py
- Machine-readable output: outputs/b16_outer_numu_sensitivity_22_25km_10mev_2026-11-09.json
- Production axial-vector files and constraints remain unchanged.


## Quantitative conclusion

For the strong endpoint, assigning a constant +1 or -1 MeV muon-neutrino chemical potential throughout 22--25 km changes the escaped luminosity by only +0.0172%. Assigning +3 or -3 MeV changes it by only +0.1505%. The peak changes are +0.0082% and +0.0719%, respectively. The sign-paired results agree exactly at stored precision.

Thus, although the 22--25 km shell contributes 19.1084% of the source-weighted neutrino path optical depth for 8--15 km emission, the tested uncertainty in its muon-neutrino chemical potential has a negligible effect on the strong-endpoint luminosity. This is a useful distinction: the shell's temperature/path contribution matters, but the unmeasured mu_numu continuation is not a plausible explanation for the +92% Fig. 7 mismatch within the tested ±3 MeV envelope.

## Reproducibility

- Script: `audit_b16_outer_numu_sensitivity_22_25km.py`
- Workflow: [Run #42572982267](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42572982267)
- Machine-readable output: `outputs/b16_outer_numu_sensitivity_22_25km_10mev_2026-11-09.json`
- The full B.1 source and B.2 opacity were recomputed for all five scenarios; profile identity, shell fractions, and ±mu_numu sign symmetry passed.
