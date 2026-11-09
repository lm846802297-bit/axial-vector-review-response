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

The 210--510 MeV band contains NaN% of the total optically-thin source and NaN% of the total escaping luminosity. Its mean escape probability is 2.3458e-3.

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
- The next targeted audit should therefore prioritize the outer-layer neutrino inverse-decay kernel and its radial interpolation/path integration, rather than rescaling the Compton opacity.

## Numerical checks

- The 512- and 1024-point Gauss-Legendre evaluations of (n_\mu F_{\rm deg}) agree at five sampled radii to relative differences below (2.4\times10^{-15}).
- Total luminosity: (2.4396359574\times10^{52}\,\mathrm{erg\,s^{-1}}), reproducing the previous V8 phase-space result at displayed precision.
- Relative optically-thin source closure versus the archived high-order baseline: `-8.7375e-14`.
- Relative escaped-luminosity closure versus the archived high-order baseline: `-9.2271e-13`.
- Absolute escape-probability residual versus the archived high-order baseline: `-2.7165e-16`.
- Path-shell labels in the JSON were audited against the exact radial edges; numerical values were unchanged by the label correction.

## Interpretation and next step

The 92.4% excess over the digitized Fig. 7 luminosity is not explained by a dominant semi-Compton opacity omission in the high-energy band: the computed \\(\tau_\nu\\) contribution is about 3.27 times the semi-Compton contribution. Outer-layer neutrino inverse-decay opacity is the priority for an independent formula and interpolation audit.

This does not yet identify the origin of the Fig. 7 discrepancy. In particular, it does not validate the reconstructed stellar profile against original simulation data, nor establish that fixed-`omega` path-energy treatment is the unique convention used in the paper. No opacity, source normalization, energy cutoff, vector baseline, or axial-vector curve is changed.
