# Re-evaluation of the 10 MeV pure-vector Fig. 7 benchmark after profile and B.2 audits
> **Current input fingerprint:** the final B.16 rerun and paired JSON use profile B SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. The immediately preceding vertex-preserving snapshot A (`6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`) gave the same active thermodynamic inputs to floating-point precision; see `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`.


Date: 2026-11-09  
Status: **the pure-vector Fig. 7 curve is still not validated. The peak is reproduced at the few-percent level, the weak-end discrepancy is source-side, and the strong-end discrepancy is escape/opacity-side. The 12--15 km neutrino inverse-decay shell is important but is not the only relevant shell. No axial-vector curve is updated.**

## 1. Baseline held fixed

The comparison uses the existing 10 MeV pure-vector reference implementation with

\[
(N_r,N_E,N_\Omega,N_s)=(40,100,16,32),\qquad R_{\max}=25\ {\rm km}.
\]

The profile SHA-256 remains:

9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c

The new profile audit changes no production input file. It establishes that the Caputo \(T(r)\) and \(\mu_\mu/T\) curves agree with Bollig Figs. 1 and 4 on the dense radial grid at below 0.022% relative, and that Caputo's plotted \(n_\mu\) agrees with its own relativistic Fermi integral to below 0.54%. The absolute density in Bollig Fig. 3 remains lower by about 8.8% on average over 12--15 km. This unresolved figure-level discrepancy is recorded separately; it is not corrected by rescaling.

For the B.1 Compton source, the one-negative-muon convention in B.17 is verified. The implemented \(n_\mu F_{\rm deg}\) is the negative-muon susceptibility integral, and the direct B.16 source formula closes against the reference implementation to \(3.33\times10^{-16}\).

## 2. Full-curve comparison

The current baseline 10 MeV sensitivity output gives:

| Fig. 7 location | Calculated minus reference |
|---|---:|
| Weak-coupling endpoint | \(-8.89\%\) |
| Reference-luminosity peak | \(+2.57\%\) |
| Strong-coupling endpoint | \(+92.24\%\) |

Across the stored coupling grid, the mean absolute relative difference is 15.73%, and the maximum absolute relative difference is 92.24%.

The strong-endpoint calculated luminosity is therefore about 1.92 times the digitized Fig. 7 value. The peak agreement alone is not sufficient to claim that the vector benchmark is reproduced.

## 3. Separate source normalization from escape probability

Use

\[
L_{\rm calc}(g)=L_{\rm thin}^{\rm calc}(g)P_{\rm esc}^{\rm calc}(g),
\qquad
P_{\rm esc}^{\rm req}(g)=\frac{L_{\rm Fig.7}(g)}{L_{\rm thin}^{\rm calc}(g)}.
\]

The representative points are:

| Point | \(P_{\rm esc}^{\rm calc}\) | \(P_{\rm esc}^{\rm req}\) | Required / calculated |
|---|---:|---:|---:|
| Weak endpoint | 0.997869832 | 1.095179826 | 1.09751772 |
| Fig. 7 peak | 0.352473033 | 0.343645543 | 0.97495556 |
| Strong endpoint | \(3.23921\times10^{-4}\) | \(1.68498\times10^{-4}\) | 0.52018143 |

This separation fixes the interpretation:

1. **Weak endpoint:** \(P_{\rm esc}^{\rm req}>1\). No nonnegative absorption opacity can repair this point while the B.1 source is held fixed. The weak-end discrepancy is source normalization/profile-side.
2. **Peak:** the required escape probability differs from the calculated value by only 2.50% relative to the calculated value.
3. **Strong endpoint:** the required escape probability is 0.52019 times the calculated value. The corresponding effective extra optical depth is
   \[
   \Delta\tau_{\rm eff}
   =-\ln(0.52019)=0.6536.
   \]
   This is an averaged escape-probability statement, not a uniform shift to every ray.

## 4. What the 12--15 km B.2 audit establishes

For the dominant 8--15 km emission region, which contributes 79.61% of the total B.1 source, the strong-endpoint escape probability is

\[
P_{\rm esc}^{8-15\,{\rm km}}=3.5333093\times10^{-4}.
\]

The analytic radial path decomposition finds that the 12--15 km shell contributes approximately 16% of the source-weighted \(\nu_\mu\) and \(\nu_\tau\) path optical depth and about 19.5% of the corresponding escaped-population-weighted optical depth.

The channel-specific leave-one-shell-out tests give:

| Removed 12--15 km absorption component | Increase in escaping luminosity |
|---|---:|
| \(\nu_\mu\) inverse decay | 59.31% |
| \(\nu_\tau\) inverse decay | 59.32% |
| Compton | 15.04% |

These are nonlinear sensitivity tests and are not additive. They establish that the 12--15 km neutrino inverse-decay opacity is important in the high-coupling tail.

The local B.2 inverse-decay rates also close against direct angular phase-space integration and B.10 detailed balance at the \(10^{-15}\) level. The full B.2 path integral agrees with an independent 256-point full-path integration to a maximum relative residual of \(1.19179\times10^{-4}\), with a dominant-source-weighted L1 difference of \(2.09403\times10^{-6}\).

## 5. Why the 12--15 km shell is not the whole explanation

The current vertex-preserving full-path audit gives, for all emission radii, a luminosity factor 4.07286 when all 22--25 km absorption is removed and 2.92624 when all 12--15 km absorption is removed. Restricting the source to the dominant 8--15 km emission region changes these factors to 2.62660 and 3.04695, respectively. These source-region definitions must not be mixed.

Thus, the 12--15 km shell is a major contributor, but the outer neutrino inverse-decay path remains at least as important to the final escape probability. The literature-defined \(R_{\max}=25\) km remains fixed; the boundary is not extended or tuned to improve agreement.

A separate physical-approximation issue is now quantified. The exact moving-muon/recoil kernel B.13 differs substantially from B.14--B.16 at \(m_V=10\) MeV, where the paper says the non-relativistic/no-recoil approximation is normally used only for \(m_V\lesssim\) MeV. A global B.13 source-and-opacity replacement has now been completed; it is reported in Section 7 and does not resolve the B.16--Fig. 7 discrepancy. The published B.16 implementation remains unchanged as the Fig. 7 reproduction baseline.

## 6. Current-profile outer-shell polarization diagnostic

The 22--25 km shell is now evaluated with the same vertex-preserving profile (SHA-256 `9fb14e79...`) using direct mode-resolved inverse-decay rates. For the dominant 8--15 km source region, the shell-only escape factors are:

| Coupling point | Literal scalar B.2 | Mode-resolved diagnostic |
|---|---:|---:|
| Fig. 7 peak | 0.82617 | 0.93630 |
| Strong endpoint | 0.15039 | 0.46785 |

At the strong endpoint, the ratio is 3.1109. The mode-resolved result agrees with the three-state average-opacity diagnostic to about \(3\times10^{-5}\) relative; the longitudinal/transverse rate splitting itself is typically 8--10% in the sampled outer-shell energy range.

The paper's scalar prescription is unambiguous for reproducing Fig. 7: Eq. (B.6) sums over polarization states, Eq. (B.7) supplies the factor of three relative to the polarization-averaged vacuum decay width, and Eq. (B.10) fixes detailed balance. The scalar \(\Gamma_{\rm abs}\) in Eq. (B.2) is therefore evaluated with the polarization-summed rate in the published baseline. Propagating each polarization with its own opacity is a separate, more differential transport extension; it is not a correction to the literal published scalar prescription. The repository retains the polarization-summed scalar result for the Fig. 7 reproduction baseline.

The outer-shell mode audit uses a 48-point mode integral and 512-point direct phase-space checks, four direction bins with 32-point angular quadrature, and the current 222-node vertex-preserving outer profile. Its output is `outputs/b16_outer_shell_polarization_resolved_10mev_2026-11-09.json`. No production axial curve is changed.

The fixed-\(\omega\) result remains the published Eq. (B.2) baseline. A separate path-redshift-only diagnostic changes the full-curve mean absolute relative difference to 9.22% and its maximum to 36.74%; it is not a full GR ray trace and is not substituted for the fixed-\(\omega\) baseline.

## 7. Global B.13 exact Compton replacement

The full global comparison now replaces the Compton source and reduced absorption together, while keeping the published scalar, polarization-summed Eq. (B.2) prescription and the neutrino inverse-decay channel unchanged.

| Point | B.16 baseline | B.13 \(\mu^-\), consistent source + opacity |
|---|---:|---:|
| Weak endpoint | \(-8.89\%\) | \(-28.11\%\) |
| Fig. 7 peak | \(+2.57\%\) | \(-16.34\%\) |
| Strong endpoint | \(+92.24\%\) | \(+131.53\%\) |

The optically thin source decreases to \(0.78898\) of the B.16 value, while the strong-endpoint escape probability increases by a factor \(1.5265\). The latter effect dominates, so the consistent B.13 result is about \(20.4\%\) above the B.16 luminosity at the strong endpoint. The B.13 \(\mu^-+\mu^+\) extension is nearly identical; the positive-muon contribution is only \(0.672\%\) of the B.13 Compton source.

The radial decomposition identifies 5--10 km as the main region of Compton-source suppression and escape enhancement. The global B.13 replacement does not fix the independent B.16--Fig. 7 discrepancy; it increases the strong-endpoint excess. Source-only and opacity-only substitutions are diagnostic counterfactuals and are not treated as physical predictions.

The full report and machine-readable outputs are:

- B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md
- outputs/b13_global_transport_vertex_preserving_10mev_2026-11-09.json
- outputs/b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json

The B.16 baseline closes exactly against its archived output before the B.13 replacement. This closure is a code-to-archive check, not a validation of agreement with Fig. 7.

## 8. Final decision

- Keep the current Caputo \(T,\mu_\mu\) working baseline and derive the B.1 one-species \(n_\mu F_{\rm deg}\) from the relativistic Fermi integral.
- Keep the Bollig Fig. 3 absolute-density discrepancy explicit. Do not rescale the density, source, opacity, or luminosity.
- Keep the B.2 \(\nu_\mu\) and \(\nu_\tau\) inverse-decay implementation unchanged; its local and global numerical checks pass.
- Do not alter \(R_{\max}=25\) km.
- Do not update or regenerate the axial-vector cooling curve.
- Do not declare the pure-vector Fig. 7 benchmark validated.

The 12--15 km and 22--25 km inverse-decay shells are now compared with source weighting and direction-resolved paths on the same latest vertex-preserving profile. The B.13 versus B.14--B.16 question is also now tested globally with consistent source and opacity replacement. The next task is a dedicated radial- and energy-grid convergence scan of that B.13 global calculation, followed by a focused comparison of the remaining B.16--Fig. 7 difference in the source-weighted neutrino inverse-decay path contributions and reconstructed background inputs. No empirical fit to Fig. 7 is permitted.

## 9. Reproducibility

- Source/escape separation: B16_FIG7_SOURCE_VS_ESCAPE_DIAGNOSTIC_2026-11-08.md
- Channel/shell/direction audit on current profile: outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json
- Profile version reconciliation: PROFILE_VERSION_RECONCILIATION_2026-11-09.md
- Outer-shell polarization audit: outputs/b16_outer_shell_polarization_resolved_10mev_2026-11-09.json
- Dedicated 12--15 km B.2 shell audit: B16_12_15KM_NEUTRINO_INVERSE_DECAY_SHELL_AUDIT_2026-11-09.md
- Density and B.1 source audit: BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md
- Global B.13 exact Compton source-and-opacity audit: B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md
- Global B.13 full machine-readable output: outputs/b13_global_transport_vertex_preserving_10mev_2026-11-09.json
- Global B.13 compact summary: outputs/b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json
- Current opacity sensitivity data: outputs/fig7_10mev_opacity_sensitivity.json
- Successful profile/B.1 audit: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42527477573
- Successful B.2 path audit: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42504612491

No production rates, transport routines, luminosity outputs, or axial-vector plots are modified by this re-evaluation.
