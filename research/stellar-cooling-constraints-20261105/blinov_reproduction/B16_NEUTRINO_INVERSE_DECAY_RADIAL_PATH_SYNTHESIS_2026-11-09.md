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

A finer grouping makes the radial distribution more transparent:

| Path segment | Source-weighted fraction | Escaped-population-weighted fraction |
|---|---:|---:|
| 0--8 km | 5.39% | 0.27% |
| 8--15 km | 31.93% | 33.81% |
| 15--22 km | 43.61% | 46.38% |
| 22--25 km | 19.07% | 19.54% |

Thus the largest *combined path segment* is 15--22 km, not 22--25 km. The 15--22 km segment alone contributes more than twice the source-weighted neutrino optical depth of the outer 22--25 km shell. This is the most direct reason to inspect the 15--22 km thermodynamic profile and path interpolation next.


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


## 8. Original-source support audit for the 15--22 km path

The independent Bollig original-PDF vector-path audit establishes that Caputo T(r) and mu_mu/T reproduce Bollig Figs. 1 and 4 throughout 15--20 km: mean absolute relative differences are 0.004295% and 0.004684%, with maxima 0.016280% and 0.015474%, respectively.

The original Bollig Fig. 1 and Fig. 4 plotting frames terminate at 20 km. Consequently, the 20--22 km portion of the current reconstructed profile has no direct Bollig-figure temperature support; only the single endpoint at 20 km is available for the degeneracy parameter. No extrapolation is used. The 20--22 km shell contributes 12.81% of the source-weighted neutrino inverse-decay path optical depth for the dominant 8--15 km emission region, so its reconstructed temperature cannot simply be ignored.

A self-consistent B.1+B.2 sensitivity test varies only T(r) in 20--22 km by +/-10% at N_r=40, N_E=100, N_omega=32, N_s=32. The baseline B.1 source fraction emitted in this shell is only 0.07453%. The separate full path-matrix calculation gives a 12.719% neutrino path-tau fraction for 8--15 km emission, compared with 12.81% in the earlier channel-shell-directional synthesis; this 0.09 percentage-point pipeline difference is retained rather than averaged. The +/-10% temperature stress changes the strong-endpoint escaped luminosity by -0.1493% / +0.1507% and its escape probability by -0.1208% / +0.1125%. The large Fig. 7 mismatch remains. This is a diagnostic stress test, not a statistical uncertainty band or a profile correction. The result is archived in B16_OUTER_TEMPERATURE_SENSITIVITY_20_22KM_2026-11-09.md.

Bollig et al. describe the high-muon-density region relevant to their axion production as approximately 5--15 km and report an axion sphere no farther out than about 18 km. These are statements about their axion-muon processes, not a direct proof that the vector neutrino inverse-decay opacity vanishes outside 18 km. The current vector B.2 path integral must therefore retain the independently computed 20--22 km contribution unless a model-specific calculation establishes otherwise.

No rate, source, opacity, coupling, luminosity, or axial-vector curve is rescaled.


The unresolved mu_numu figure-floor convention in 20--22 km was also tested by assigning +/-1 MeV throughout the shell and recomputing the complete B.1 source and B.2 opacity. Either sign changes the strong-endpoint escaped luminosity by only +0.00915% and the escape probability by +0.00936%; the two signs agree exactly at stored precision. Thus the unresolved 1 MeV floor in this shell is not a plausible explanation for the large Fig. 7 mismatch. This is a stress test, not a reconstructed measurement of mu_numu. See B16_OUTER_NUMU_FLOOR_SENSITIVITY_20_22KM_2026-11-09.md.


## 9. 22--25 km off-frame temperature and source-support audit

The Caputo source PDF contains 57 T(r) vector vertices in 22--25 km, with T=3.0363--3.5509 MeV. These are encoded off-frame vertices: the top-panel clip boundary ends at x_pdf=325, corresponding to the visible 20 km boundary. The mu_mu path has only six vertices between 22 and 22.1919 km and terminates at the 1 MeV plotting floor; the baseline profile sets mu_mu=0 beyond it. The original Bollig Figs. 1 and 4 do not validate any of these outer-shell values.

The 22--25 km shell contributes 19.1084% of the neutrino inverse-decay path optical depth for 8--15 km emission in the independent full B.1+B.2 path-matrix calculation, consistent with the earlier 19.07% direction-resolved synthesis. The B.1 source emitted in this shell is only 0.07276%.

A self-consistent temperature-only stress test of the 222 nodes, with N_r=40, N_E=100, N_omega=32, N_s=32, finds that at the strong endpoint +/-10% T changes escaped luminosity by -1.8133% / +2.7688%; a broad +/-30% stress changes it by -3.6191% / +12.4742%. The corresponding Fig. 7 discrepancy remains +85.29% to +116.23%, compared with +92.25% at baseline. The response is dominated by B.2 propagation rather than B.1 emission. These variations are stress tests, not statistical uncertainty estimates, and no profile or luminosity rescaling is applied. See B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md and CAPUTO_OFFFRAME_THERMODYNAMIC_VERTICES_20_22KM_2026-11-09.md.
