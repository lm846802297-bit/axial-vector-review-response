# 10 MeV B.2 channel-resolved opacity audit

Date: 2026-11-10  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`  
Input PR head before this audit: `dc46a5501769a9e4cf484c2183b0dad4ff2d4736`  
Result: [`b16_10mev_channel_resolved_opacity_2026-11-10.json`](outputs/b16_10mev_channel_resolved_opacity_2026-11-10.json)

## Scope and method

The literal B.2 reduced absorption kernel is split additively into neutrino inverse-decay and semi-Compton pieces:
[
\Gamma_{\rm red}=(e^{\omega/T}-1)\,\Gamma_{\rm prod}
=\Gamma_{\rm red,\nu}+\Gamma_{\rm red,C},
\qquad
\tau_i=g_X^2\int_{\rm chord}\frac{ds}{v}\,
\Gamma_{\rm red,i}(r(s),\omega).
]
The survival factor is evaluated with the sum, (P_{\rm esc}=\exp[-(\tau_\nu+\tau_C)]). The channel split is diagnostic only; it does not apply separate survival factors or modify the total opacity.

The direct V8 double-precision calculation uses the same reconstructed SFHo-18.8 profile, Fig. 7 digitization, coupling, and quadrature orders as the preceding phase-space cross-check: source radial 200, opacity radial 640, energy 200 plus lapse-threshold nodes, direction 32, path 64. The profile and Fig. 7 files are the same archived inputs. Node counts agree with the archived high-order baseline. V8-generated quadrature nodes are not bitwise-identical to NumPy's nodes, so this is not the strict NumPy runbook acceptance.

## Integrated optical-depth decomposition

| Quantity | Neutrino inverse decay | Semi-Compton | Total |
|---|---:|---:|---:|
| Global source-weighted mean \\(\tau\\) | 14.4807 | 1.6480 | 16.1287 |
| Global escape-weighted mean \\(\tau\\) | 4.5443 | 0.7501 | 5.2944 |
| 210--510 MeV source-weighted mean \\(\tau\\) | 5.9118 | 1.8076 | 7.7193 |
| 210--510 MeV escape-weighted mean \\(\tau\\) | 4.1072 | 0.8510 | 4.9581 |

In the 210--510 MeV band, the source-weighted optical depth is 0.7658 (76.58%) neutrino inverse decay and 0.2342 (23.42%) semi-Compton. Neutrino inverse decay is the larger opacity contribution, while semi-Compton remains substantial.

The 210--510 MeV band contains 9.670% of the total optically-thin source and 69.756% of the total escaping luminosity. Its mean escape probability is 2.3458e-3.

## Where the high-energy optical depth accumulates

The following entries are mean contributions to \\(\tau\\), averaged over B.1 source weights and all initial directions in the 210--510 MeV band. Path shells use the exact radial edges `0, 5, 8, 10, 12, 15, 18, 20, 22, 24, 25` km.

| Chord radius shell | \\(\langle\tau_\nu\rangle_{B.1}\\) | \\(\langle\tau_C\rangle_{B.1}\\) | Total |
|---|---:|---:|---:|
| 0-5 km | 0.1373 | 0.0090 | 0.1463 |
| 5-8 km | 0.5434 | 0.3187 | 0.8621 |
| 8-10 km | 0.7229 | 0.8563 | 1.5792 |
| 10-12 km | 0.6780 | 0.4778 | 1.1559 |
| 12-15 km | 0.9107 | 0.1449 | 1.0555 |
| 15-18 km | 0.8916 | 0.0009 | 0.8925 |
| 18-20 km | 0.5888 | 0.0000 | 0.5888 |
| 20-22 km | 0.5765 | 0.0000 | 0.5765 |
| 22-24 km | 0.5773 | 0.0000 | 0.5773 |
| 24-25 km | 0.2852 | 0.0000 | 0.2852 |

This separates the channels spatially:

- Semi-Compton opacity is concentrated in the inner region, principally 5--15 km. Its contribution becomes negligible outside 15--18 km.
- Neutrino inverse-decay opacity persists through the outer 15--25 km layers and supplies most of the high-energy optical depth.
- The targeted outer-layer neutrino inverse-decay kernel, radial interpolation, and path integration have now been checked in the P1 follow-up. No percent-level numerical propagation discrepancy is found; see B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md.

## Numerical checks

- The 512- and 1024-point Gauss-Legendre evaluations of (n_\mu F_{\rm deg}) agree at five sampled radii to relative differences below (2.4\times10^{-15}).
- Total luminosity: (2.4396359574\times10^{52}\,\mathrm{erg\,s^{-1}}), reproducing the previous V8 phase-space result at displayed precision.
- Relative optically-thin source closure versus the archived high-order baseline: `-8.7375e-14`.
- Relative escaped-luminosity closure versus the archived high-order baseline: `-9.2271e-13`.
- Absolute escape-probability residual versus the archived high-order baseline: `-2.7165e-16`.
- Path-shell labels in the JSON were audited against the exact radial edges; numerical values were unchanged by the label correction.

## Interpretation and next step

The 92.4% excess over the digitized Fig. 7 luminosity is not explained by a dominant semi-Compton opacity omission in the high-energy band: the computed \\(\tau_\nu\\) contribution is about 3.27 times the semi-Compton contribution. The P1 follow-up finds that direct path integration, angular integration, and profile-vertex-preserving opacity interpolation are numerically stable. The remaining high-energy path-redshift sensitivity is carried almost entirely by neutrino inverse-decay opacity and remains a separate physical diagnostic.

This does not yet identify the origin of the Fig. 7 discrepancy. In particular, it does not validate the reconstructed stellar profile against original simulation data, nor establish that fixed-`omega` path-energy treatment is the unique convention used in the paper. No opacity, source normalization, energy cutoff, vector baseline, or axial-vector curve is changed.


## P1 follow-up (2026-11-10)

The targeted high-energy B.2 path, angle, and opacity-interpolation checks are archived in [B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md](B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md). Direct path-coordinate integration agrees with the analytic radial primitive at the \(10^{-13}\) level; using all 1687 profile vertices instead of the 642-node opacity grid changes the sampled total optical depth by at most \(1.87\times10^{-5}\). A separate 36-ray channel-resolved path-redshift diagnostic finds that the redshift sensitivity is carried by neutrino inverse decay, while the semi-Compton opacity is nearly unchanged. These are targeted diagnostics, not a new global Fig. 7 calculation. The fixed-\(\omega\) B.2 baseline is retained.


## Source-weighted global path-redshift channel attribution (2026-11-10)

The P1 follow-up now includes a global Shapley decomposition over the full B.1 source measure in the 210--510 MeV band. The four fixed/redshift counterfactuals give \(L_{00}=1.70178483\times10^{52}\), \(L_{10}=1.22372442\times10^{52}\), \(L_{01}=1.70170496\times10^{52}\), and \(L_{11}=1.22367050\times10^{52}\) erg/s.

The Shapley attribution of the global luminosity change is 99.9860% from neutrino inverse decay and 0.0140% from semi-Compton absorption. This is source weighted and supersedes the 36-ray unweighted channel sample as the global attribution. The direct local-rate evaluation cross-check changes the redshifted band luminosity by about 0.50% relative to bilinear local-energy interpolation, but retains the same greater-than-99.98% neutrino attribution. The fixed-\(\omega\) B.2 baseline is unchanged.

See [B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md](B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md) and its machine-readable JSON result.


## P1-B.2 thermodynamic interpolation and input sensitivity (2026-11-10)

The follow-up audit is archived in [B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md](B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md), with machine-readable results in \`outputs/b16_p1b2_thermodynamic_interpolation_input_sensitivity_2026-11-10.json\` and the reproduction script \`audit_b16_p1b2_thermodynamic_input_sensitivity.py\`.

The 642-node precomputed-opacity interpolation and direct local-kernel recomputation from the 1687-vertex thermodynamic profile agree in total optical depth to \(9.07\times10^{-6}\) or better on the 36-ray high-energy sample. The larger Compton-only relative difference is at most \(1.43\times10^{-3}\), but is subdominant in total \(\tau\) on those rays.

A source-frozen global B.2 sensitivity calculation in the 210--510 MeV band finds:
- \(\pm10\%\) \(\mu_{\nu_\mu}\) changes the escaped luminosity by less than \(0.03\%\);
- \(\pm10\%\) \(T\) at fixed \(\mu_\mu\) changes it by \(+16.29\%/-15.33\%\);
- \(\pm10\%\) \(\mu_\mu\) at fixed \(T\) changes it by \(+19.95\%/-18.91\%\);
- correlated \(\pm10\%\) \(T,\mu_\mu\) variations at fixed \(\mu_\mu/T\) change it by \(+37.05\%/-32.36\%\).

These broad variations are stress tests, not inferred uncertainties. The actual baseline \(T\) and \(\mu_\mu/T\) match Bollig Figs. 1 and 4 over 5--15 km to maximum relative residuals \(9.90\times10^{-5}\) and \(2.127\times10^{-4}\), respectively. The remaining B.2 normalization issue is the relation between the polarization-summed production rate and the scalar absorption rate in the optical-depth exponent; it is not resolved by these thermodynamic tests.
