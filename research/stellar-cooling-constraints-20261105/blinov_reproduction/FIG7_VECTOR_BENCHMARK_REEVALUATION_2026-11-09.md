# Re-evaluation of the 10 MeV pure-vector Fig. 7 benchmark after profile and B.2 audits

Date: 2026-11-09  
Status: **the pure-vector Fig. 7 curve is still not validated. The peak is reproduced at the few-percent level, the weak-end discrepancy is source-side, and the strong-end discrepancy is escape/opacity-side. The 12--15 km neutrino inverse-decay shell is important but is not the only relevant shell. No axial-vector curve is updated.**

## 1. Baseline held fixed

The comparison uses the existing 10 MeV pure-vector reference implementation with

\[
(N_r,N_E,N_\Omega,N_s)=(40,100,16,32),\qquad R_{\max}=25\ {\rm km}.
\]

The profile SHA-256 remains:

08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9

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
| Weak endpoint | 0.997870 | 1.095184 | 1.09752 |
| Fig. 7 peak | 0.352473 | 0.343647 | 0.97496 |
| Strong endpoint | \(3.23918\times10^{-4}\) | \(1.68498\times10^{-4}\) | 0.52019 |

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
P_{\rm esc}^{8-15\,{\rm km}}=3.53332\times10^{-4}.
\]

The analytic radial path decomposition finds that the 12--15 km shell contributes approximately 16% of the source-weighted \(\nu_\mu\) and \(\nu_\tau\) path optical depth and about 19.5% of the corresponding escaped-population-weighted optical depth.

The channel-specific leave-one-shell-out tests give:

| Removed 12--15 km absorption component | Increase in escaping luminosity |
|---|---:|
| \(\nu_\mu\) inverse decay | 59.31% |
| \(\nu_\tau\) inverse decay | 59.32% |
| Compton | 15.04% |

These are nonlinear sensitivity tests and are not additive. They establish that the 12--15 km neutrino inverse-decay opacity is important in the high-coupling tail.

The local B.2 inverse-decay rates also close against direct angular phase-space integration and B.10 detailed balance at the \(10^{-15}\) level. The full B.2 path integral agrees with an independent 256-point full-path integration to a maximum relative residual of \(1.19225\times10^{-4}\), with a dominant-source-weighted L1 difference of \(2.09389\times10^{-6}\).

## 5. Why the 12--15 km shell is not the whole explanation

The full shell attribution shows that the outer 22--25 km shell has the largest individual all-channel leave-one-shell-out sensitivity at the strong endpoint: removing that shell raises the luminosity by a factor 4.056. Removing all opacity in 12--15 km raises it by a factor 2.943.

Thus, the 12--15 km shell is a major contributor, but the outer neutrino inverse-decay path remains at least as important to the final escape probability. The literature-defined \(R_{\max}=25\) km remains fixed; the boundary is not extended or tuned to improve agreement.

A separate physical-approximation issue also remains: the full moving-muon/recoil Compton kernel B.13 is not the same approximation as B.14--B.16. The B.14--B.16 implementation closes algebraically, but its physical accuracy at \(m_V=10\) MeV remains unresolved. No B.13 substitution is made in the reference baseline.

## 6. Final decision

- Keep the current Caputo \(T,\mu_\mu\) working baseline and derive the B.1 one-species \(n_\mu F_{\rm deg}\) from the relativistic Fermi integral.
- Keep the Bollig Fig. 3 absolute-density discrepancy explicit. Do not rescale the density, source, opacity, or luminosity.
- Keep the B.2 \(\nu_\mu\) and \(\nu_\tau\) inverse-decay implementation unchanged; its local and global numerical checks pass.
- Do not alter \(R_{\max}=25\) km.
- Do not update or regenerate the axial-vector cooling curve.
- Do not declare the pure-vector Fig. 7 benchmark validated.

The next narrow transport priority is a source-weighted comparison of the 12--15 km and 22--25 km neutrino inverse-decay shells, including the reconstructed \(T,\mu_{\nu_\mu}\), lapse, and direction-resolved path weights in the outer shell. In parallel, retain the B.13 versus B.14--B.16 Compton comparison as a distinct physical-approximation question. No empirical fit to Fig. 7 is permitted.

## 7. Reproducibility

- Source/escape separation: B16_FIG7_SOURCE_VS_ESCAPE_DIAGNOSTIC_2026-11-08.md
- Channel/shell/direction audit: B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_2026-11-09.md
- Dedicated 12--15 km B.2 shell audit: B16_12_15KM_NEUTRINO_INVERSE_DECAY_SHELL_AUDIT_2026-11-09.md
- Density and B.1 source audit: BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md
- Current opacity sensitivity data: outputs/fig7_10mev_opacity_sensitivity.json
- Successful profile/B.1 audit: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42527477573
- Successful B.2 path audit: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42504612491

No production rates, transport routines, luminosity outputs, or axial-vector plots are modified by this re-evaluation.
