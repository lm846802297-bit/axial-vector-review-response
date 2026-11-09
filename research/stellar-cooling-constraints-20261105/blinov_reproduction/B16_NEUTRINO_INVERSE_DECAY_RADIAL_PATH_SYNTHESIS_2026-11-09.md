# B.2 neutrino inverse-decay radial-path synthesis (2026-11-09)

## Executive result

This post-processing synthesis uses the current-profile, channel-shell-direction resolved B.16 output at \(m_V=10\) MeV and the strong-coupling endpoint \(g=4.17168965\times10^{-8}\). It does not rerun the transport calculation or alter any rate.

For the dominant 8--15 km B.1 emission region:

- the source supplies 79.6114% of the total B.1 thin source;
- the source-weighted escape probability is \(3.53331\times10^{-4}\);
- the combined \(\nu_\mu\) and \(\nu_\tau\) inverse-decay optical depth is concentrated across the 8--22 km path shells, which account for 75.54% of its source-weighted path integral;
- the outer 22--25 km shell still contributes 19.07%, and is not negligible.

The important distinction is that the **outer shell is the largest single shell**, while the **inner 8--22 km group dominates collectively**.

## 1. Fixed benchmark and definitions

- Pure-vector B.14--B.19 reference baseline.
- \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\).
- Current vertex-preserving profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.
- \(R_{\max}=25\) km.
- Fixed \(\omega\) along each B.2 ray.
- Opacity channels: \(\nu_\mu\) inverse decay, \(\nu_\tau\) inverse decay, Compton, and dimuon. The dimuon channel is closed at this mediator mass.

For a path shell \(i\), the reported source-weighted mean is

\[
\left\langle\frac{\tau_{\nu,i}}{g^2}\right\rangle_{\rm src}
=
\frac{\int d\Pi_{\rm src}\,
(\tau_{\nu_\mu,i}+\tau_{\nu_\tau,i})/g^2}
{\int d\Pi_{\rm src}},
\]

where \(d\Pi_{\rm src}\) is the B.1 source measure over emission radius, energy, and direction. The escaped-population-weighted mean uses the same measure multiplied by the full survival factor \(e^{-\tau_{\rm tot}}\). These are different weightings and neither is a shell-by-shell additive decomposition of the final luminosity.

## 2. Source-weighted radial decomposition

The table shows the fraction of the total \(\nu_\mu+\nu_\tau\) path optical depth in each shell, for the dominant 8--15 km emission region at the strong endpoint.

| Path shell | Source-weighted fraction | Escaped-population-weighted fraction |
|---|---:|---:|
| 0--5 km | 1.20% | 0.06% |
| 5--8 km | 4.18% | 0.21% |
| 8--10 km | 6.83% | 4.00% |
| 10--12 km | 9.12% | 10.34% |
| 12--15 km | 15.97% | 19.46% |
| 15--16.5 km | 8.83% | 9.99% |
| 16.5--18.5 km | 12.42% | 13.31% |
| 18.5--20 km | 9.56% | 9.93% |
| 20--22 km | 12.81% | 13.15% |
| 22--25 km | 19.07% | 19.54% |

The total source-weighted \(\nu_\mu+\nu_\tau\) path optical depth is \(8.196\times10^{15}\) per \(g^2\); the escaped-population-weighted value is \(2.674\times10^{15}\) per \(g^2\).

Grouped by path region:

| Path group | Source-weighted fraction | Escaped-population-weighted fraction |
|---|---:|---:|
| Core, 0--8 km | 5.39% | 0.27% |
| Inner, 8--22 km | 75.54% | 80.19% |
| Outer, 22--25 km | 19.07% | 19.54% |

The same grouping for all emission radii gives source-weighted fractions 6.71%, 73.97%, and 19.32%, respectively. The conclusion is therefore not an artifact of restricting the source to 8--15 km.

## 3. Directional escape distribution

The direction cosine is measured relative to the local outward radial direction: negative values are initially inward-going rays and positive values are outward-going rays.

| \(\cos\theta\) bin | Mean escape probability | Fraction of escaping luminosity |
|---|---:|---:|
| -1 to -0.5 | \(7.862\times10^{-6}\) | 0.556% |
| -0.5 to 0 | \(3.938\times10^{-5}\) | 2.786% |
| 0 to 0.5 | \(2.824\times10^{-4}\) | 19.979% |
| 0.5 to 1 | \(1.084\times10^{-3}\) | 76.679% |

Thus, only 3.342% of the escaping luminosity in this source region comes from initially inward-going directions; 96.658% comes from outward-going directions. This is a transport-geometry effect: inward-going rays cross additional inner radial layers before turning and escaping. The direction bins are integrated separately with their own mapped Gauss rules.

## 4. Nonlinear leave-one-out sensitivity

The following tests remove the indicated neutrino inverse-decay opacity and recompute the full escaped-luminosity integral. They are nonlinear counterfactual sensitivities, not additive contributions and not proposed physical corrections.

| Removed neutrino opacity | Dominant 8--15 km source: luminosity factor | All emission radii: luminosity factor |
|---|---:|---:|
| Both \(\nu_\mu+\nu_\tau\) in 8--22 km | 114.15 | 108.36 |
| Both \(\nu_\mu+\nu_\tau\) in 22--25 km | 2.627 | 4.073 |
| Both flavors in all 8--25 km shells | 901.92 | 876.17 |

The 12--15 km and 22--25 km shells are individually sensitive. For the dominant 8--15 km source, removing only the \(\nu_\mu\) inverse-decay opacity in 12--15 km increases the luminosity by 59.31%; removing only the \(\nu_\tau\) there gives 59.32%. The corresponding individual changes in 22--25 km are 59.63% for either flavor.

These individual shell effects must not be summed. The group-level counterfactuals show why the complete inner 8--22 km path is more consequential than the outer shell alone.

## 5. Numerical closure

The current-profile calculation reports:

| Check | Residual |
|---|---:|
| B.1 production-channel sum | \(4.01\times10^{-16}\) |
| B.2 reduced-absorption channel sum | \(5.94\times10^{-16}\) |
| Angular-weight normalization | 0 |
| Analytic radial path vs independent 256-point full-path quadrature, maximum relative residual | \(1.192\times10^{-4}\) |
| Same path comparison, source-weighted L1 relative residual for 8--15 km emission | \(2.094\times10^{-6}\) |

At the strong endpoint, increasing the global angular order from 16 to 64 changes the dominant-region source-weighted escape probability by only \(5.73\times10^{-6}\) at order 16 and \(1.30\times10^{-6}\) at order 32 relative to order 64. The direction-bin quadrature scan is also stable at the reported precision.

## 6. Physical interpretation and limitations

1. The outer 22--25 km neutrino shell is important: it contributes about 19% of the source-weighted neutrino path optical depth and has a large individual leave-out response.
2. It is not correct to describe that shell as the sole or dominant total attenuation region. The 8--22 km path group carries about 76% of the source-weighted neutrino optical depth and produces a much larger combined leave-out response.
3. The strong angular asymmetry of escaping luminosity shows that the path geometry matters: most escaping particles are initially outward-going, while inward-going rays are strongly suppressed.
4. Leave-one-out factors are nonlinear diagnostics. They do not establish that any shell opacity is erroneous, and they must not be converted into multiplicative corrections.
5. This is the pure-vector B.16 reference baseline. It does not substitute the exact moving-muon B.13 Compton kernel into the B.1 source and B.2 opacity. The separate B.13 local-kernel convergence audit therefore does not change these B.16 numbers.
6. The reconstructed public-figure stellar profile is not the raw Garching simulation table used by the original calculation. Numerical convergence of the path integral does not remove this background-input limitation or establish agreement with Fig. 7.

No source, coupling, opacity, luminosity, production rate, or axial-vector curve is rescaled or modified.

## 7. Reproducibility

- Current-profile machine-readable input: outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json
- Path and direction implementation: audit_b16_inner_path_channel_directional.py
- Related current-profile reports: B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_VERTEX_PRESERVING_2026-11-09.md and B16_COMBINED_CHANNEL_SHELL_SENSITIVITY_2026-11-09.md.
