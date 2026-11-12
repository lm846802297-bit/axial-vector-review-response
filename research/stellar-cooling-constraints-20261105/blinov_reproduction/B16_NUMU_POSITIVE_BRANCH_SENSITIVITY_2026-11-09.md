# B.16 sensitivity to the positive muon-neutrino chemical-potential branch (2026-11-09)

## Executive result

The isolated positive \(\mu_{\nu_\mu}\) branch in the Caputo Fig. 1 reconstruction has a negligible effect on the 10 MeV B.16 vector benchmark. Setting the entire positive branch to zero changes the strong-endpoint escape probability by -0.01409% and escaped luminosity by -0.01286% relative to baseline. A +/-10% variation changes the strong-endpoint escape probability by less than 0.003%.

The branch is therefore not a plausible explanation for the order-one strong-coupling Fig. 7 mismatch. This targeted sensitivity result does not certify the complete 15--22 km thermodynamic background.

## 1. Fixed inputs and isolated variation

- Mediator mass: 10 MeV; pure-vector B.14--B.19 reference implementation.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Fig. 7 reference SHA-256: `6a9f68add5dde4b41373702d0e10538985bc513db20a7152ebf2e143130aeac4`.
- Positive-branch support: 16.5881801203445--18.4229995917391 km; 98 retained nodes.
- Digitized branch range: 0.999999834--1.797062102 MeV.
- Only \(\mu_{\nu_\mu}\) within this positive branch is scaled. \(T\), \(\mu_\mu\), lapse, negative branch, radial grid, and all other inputs are unchanged.
- Each scenario recomputes the complete B.1 source and B.2 opacity consistently.
- Fixed-\(\omega\) B.2 convention and 40x100x16x32 global grid are retained.
- Scale 0 and +/-10% are stress tests, not statistical uncertainty intervals.

## 2. Strong-endpoint results

At \(g=4.1716896502\times10^{-8}\):

| Positive-branch scale | \(P_{\rm esc}/P_{\rm esc}^{\rm base}\) | \(L_{\rm esc}/L_{\rm esc}^{\rm base}\) | Shift in \(L/L_{\rm Fig.7}-1\) |
|---:|---:|---:|---:|
| 0 | 99.985907% | 99.987143% | -0.024716% |
| 0.9 | 99.997328% | 99.997562% | -0.004687% |
| 1.0 | 100% | 100% | 0 |
| 1.1 | 100.002951% | 100.002692% | +0.005176% |

Baseline strong-endpoint values:
- \(P_{\rm esc}=3.23921117\times10^{-4}\);
- \(L_{\rm esc}=2.43725494\times10^{52}\,\mathrm{erg\,s^{-1}}\);
- relative difference from Fig. 7: +92.240619%.

Setting the positive branch to zero changes the optically thin source by only +0.001236% relative to baseline. The response is therefore almost entirely a small B.2 escape-probability change, not a B.1 source-normalization change.

## 3. Weak endpoint and reference peak

| Positive-branch scale | Weak-endpoint escaped-luminosity ratio | Peak escaped-luminosity ratio |
|---:|---:|---:|
| 0 | 100.001203% | 99.993446% |
| 0.9 | 100.000228% | 99.998757% |
| 1.0 | 100% | 100% |
| 1.1 | 99.999749% | 100.001372% |

The largest response among the three reference points occurs at the strong endpoint and remains below 0.013% even when the entire branch is removed.

## 4. Numerical closure

For all four scenarios:
- Source-channel sum maximum relative residual: 4.37e-16.
- Shell-column sum residual: 0.
- Shell columns vs direct chord maximum relative residual: 6.54e-16.
- Source-weighted mean optical-depth matrix residual: at most 2.22e-16.
- Angular-weight normalization residual: 0.
- Production axial-vector files and constraints are unchanged.

## 5. Interpretation and next step

The positive \(\mu_{\nu_\mu}\) branch is not responsible for the large 15--22 km contribution to the total neutrino inverse-decay path optical depth. The large path contribution reflects the baseline two-flavor inverse-decay opacity integrated over a broad radial interval, not the small positive-branch chemical-potential correction.

This test does not certify the full 15--22 km background. The remaining input audit should focus on \(T(r)\), \(\mu_\mu(r)\), and lapse/source weighting, together with the reconstruction of the 15--22 km profile from the public figure. The original Garching simulation table remains unavailable; the current profile is a public-figure reconstruction.

No source, opacity, coupling, luminosity, or axial-vector constraint is rescaled. The pure-vector reference and production axial-vector curves remain frozen.

## 6. Reproducibility

- Workflow: [Run 42552214391](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42552214391)
- Machine-readable result: `outputs/b16_numu_positive_branch_sensitivity_10mev_2026-11-09.json`
- Script: `audit_b16_numu_positive_branch_sensitivity.py`
- Workflow: `.github/workflows/b16-numu-positive-branch-sensitivity.yml`
