# Global B.13 stage-A convergence audit: status (2026-11-09)

## Scope

This report records the numerical-convergence work for the 10 MeV pure-vector B.13 global transport benchmark. The physical collision kernels, fixed-\omega B.2 convention, SFHo-18.8 vertex-preserving profile, and interaction channels are held fixed. No empirical source/opacity/luminosity rescaling is applied. No production axial-vector curve or manuscript file is modified.

The profile fingerprint is:

\[
\texttt{SHA256}= \texttt{9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c}.
\]

The original B.13 reference grid is \(N_r=40\), \(N_E=100\), \(N_\Omega=16\), \(N_s=32\).

## 1. Radial and energy quadrature: completed

The successful GitHub Actions run [42536610504](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42536610504) generated the output file outputs/b13_global_grid_convergence_2026-11-09.json. Each refined B.13 run was paired with a B.16 baseline regenerated on the identical radial, energy, angular, and path grid. The B.16 closure residual was exactly zero for all three configurations.

For the like-for-like \(\mu^-\)-only B.13 variant (the species convention matching the single negative-muon distribution in Eq. (B.17)):

| \(N_r\) | \(N_E\) | Maximum absolute luminosity shift relative to \(40\times100\times16\times32\) |
|---:|---:|---:|
| 60 | 100 | \(0.10630\%\) |
| 40 | 140 | \(0.28410\%\) |
| 60 | 140 | \(0.27316\%\) |

The combined \(60\times140\) radial-energy grid therefore meets the project-level \(1\%\) luminosity-stability target. These are numerical acceptance targets, not physical uncertainty estimates.

At \(60\times140\times16\times32\), the B.13 luminosity differences relative to Fig. 7 are:

| Fig. 7 location | Relative difference |
|---|---:|
| Weak-coupling endpoint | \(-28.3054\%\) |
| Reference peak | \(-16.5636\%\) |
| Strong-coupling endpoint | \(+131.1176\%\) |

For comparison, the original \(40\times100\times16\times32\) summary gives \(-28.1090\%\), \(-16.3397\%\), and \(+131.5300\%\), respectively. The strong-endpoint discrepancy changes by only about \(0.41\) percentage points under the combined radial-energy refinement. Thus the large strong-coupling discrepancy is not explained by insufficient radial or energy quadrature at the tested resolutions.

The optically thin B.13/B.16 source ratio changes from \(0.7889823\) on the original grid to \(0.7888233\) on the \(60\times140\) grid. The strong-endpoint source-weighted escape fraction changes from \(4.94463\times10^{-4}\) to \(4.94935\times10^{-4}\). Both changes are small.

## 2. Separate the B.13 correction from the pre-existing B.16-to-Fig. 7 mismatch

The original-grid global summary allows the final luminosity ratio to be factorized exactly:

\[
\frac{L_{\mathrm{B13}}}{L_{\mathrm{B16}}}
=
\frac{L_{\mathrm{thin,B13}}}{L_{\mathrm{thin,B16}}}
\frac{f_{\mathrm{esc,B13}}}{f_{\mathrm{esc,B16}}}.
\]

The B.13/B.16 optically thin source ratio is coupling-independent and equals \(0.7889823\) for the \(\mu^-\)-only comparison. The endpoint decomposition is:

| Point | Thin-source ratio B.13/B.16 | Escape-fraction ratio B.13/B.16 | Final luminosity ratio B.13/B.16 |
|---|---:|---:|---:|
| Weak endpoint | 0.788982 | 1.000043 | 0.789016 |
| Fig. 7 reference peak | 0.788982 | 1.033801 | 0.815650 |
| Strong endpoint | 0.788982 | 1.526494 | 1.204376 |

Across all 25 stored coupling points, the optically thin ratio remains constant to the reported numerical precision, whereas the escape-fraction ratio rises monotonically from approximately 1 at weak coupling to 1.5265 at the strong endpoint. The B.13 luminosity therefore crosses the B.16 luminosity between the two stored points

\[
g=2.8754\times10^{-8}
\quad\text{and}\quad
g=3.4634\times10^{-8}.
\]

A log-linear interpolation of these two sampled luminosity ratios places the crossing near \(g\simeq2.95\times10^{-8}\). This is only a diagnostic interpolation between existing grid points, not a new physical boundary or a fit to Fig. 7. At the crossing, the escape-fraction ratio compensates the fixed source ratio, requiring approximately

\[
\frac{f_{\mathrm{esc,B13}}}{f_{\mathrm{esc,B16}}}
\simeq \frac{1}{0.7889823}=1.26746.
\]

Thus the weak-coupling B.13 reduction is almost entirely a source-normalization effect. At strong coupling, the lower B.13 thin source is more than compensated by the larger escape fraction. This is consistent with the lower exact B.13 Compton opacity relative to the B.16 approximate Compton opacity; it is not a universal multiplicative rescaling of the luminosity curve.

The B.16 fixed-\(\omega\) baseline itself differs from digitized Fig. 7 by \(-8.89\%\) at the weak endpoint, \(+2.57\%\) at the reference peak, and \(+92.24\%\) at the strong endpoint. The corresponding B.13 differences are \(-28.11\%\), \(-16.34\%\), and \(+131.53\%\). Consequently, the full B.13-to-Fig. 7 discrepancy must not be attributed to the B.13 collision-kernel replacement: the B.16 reference already contains a large strong-endpoint mismatch.

This establishes two separate validation questions for subsequent work: (i) why the fixed-\(\omega\) B.16 baseline departs from Fig. 7 in the strong-absorption tail, and (ii) what additional change the exact B.13 Compton source and opacity produce relative to that internally matched B.16 baseline. The first question remains distinct from the numerical quadrature convergence test and must not be hidden by tuning the B.13 result.

## 3. Angular and path quadrature: completed

The completed Actions run [42542328275](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42542328275) performed all four configurations: angular-only, path-only, joint angular/path, and combined radial-energy-angular-path refinement. The workflow's structural validation passed: all four labels and both B.13 variants are present, the fixed profile SHA256 matches, every same-grid B.16 closure residual is zero, and the production axial files remain unchanged.

The maximum B.13 luminosity shift on the combined grid is 0.2732%; the peak and strong-endpoint shifts are 0.2680% and 0.1842%, below the project targets of 1%, 1%, and 2%. The maximum escape-fraction shift is 0.0895%; no separate escape-fraction acceptance threshold was predeclared. The independent stage-A thin-source ratio changes from 0.7889822588 to 0.7888232697, a 0.0201% decrease.

The workflow conclusion is nevertheless failure because the final artifact upload hit the GitHub Actions artifact-storage quota. The full JSON was generated on the runner but was not uploaded, and no full JSON archive exists in the branch. A compact summary reconstructed from the job's printed per-scan JSON blocks is archived at [b13_global_convergence_vertex_preserving_10mev_2026-11-09_log_recovered_summary.json](outputs/b13_global_convergence_vertex_preserving_10mev_2026-11-09_log_recovered_summary.json). The audit report is [B13_GLOBAL_ANGULAR_PATH_CONVERGENCE_AUDIT_2026-11-09.md](B13_GLOBAL_ANGULAR_PATH_CONVERGENCE_AUDIT_2026-11-09.md). This recovered summary is explicitly not the original full JSON; its omitted arrays and detailed diagnostics require a fresh run or a later successful upload.

## 4. Positive muon-neutrino branch sensitivity: completed

The current-profile B.16 sensitivity run [42552214391](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42552214391) varies only the positive Caputo Fig. 1 mu_numu branch over 16.588180--18.4229996 km, containing 98 retained nodes. The B.1 source and B.2 opacity are recomputed consistently for branch scales 0, 0.9, 1.0, and 1.1. All channel, shell, direct-chord, mean-optical-depth, and angular-weight closure checks pass at floating-point precision.

Removing the entire positive branch changes the strong-endpoint escape probability by -0.01409% and escaped luminosity by -0.01286%. +/-10% variations change the strong-endpoint escape probability by less than 0.003%. The branch cannot explain the order-one strong-coupling Fig. 7 discrepancy. See [B16_NUMU_POSITIVE_BRANCH_SENSITIVITY_2026-11-09.md](B16_NUMU_POSITIVE_BRANCH_SENSITIVITY_2026-11-09.md). This does not certify the complete 15--22 km thermodynamic profile.

## 5. Bollig original-source thermodynamic profile audit: completed

The independent original-PDF comparison now extends through the full 15--20 km plotting interval. On the 1687-node Caputo reconstruction, the mean (maximum) absolute relative differences are:

- Fig. 1 temperature: 0.004295% (0.016280%).
- Fig. 4 mu_mu/T: 0.004684% (0.015474%).
- Derived mu_mu from T times mu_mu/T: 0.005112% (0.021238%); this is a combined cross-check, not an independent third observable.

The original Bollig Fig. 1 and Fig. 4 plotting frames both end at 20 km. The 20--22 km interval has no direct original-figure temperature support and only the endpoint at 20 km for mu_mu/T. No extrapolation is used. The 20--22 km Caputo temperature input therefore remains a public-figure reconstruction without an independent Bollig-figure cross-check.

This unsupported interval is not negligible in the B.16 path integral: the 20--22 km shell contributes 12.81% of the source-weighted nu_mu+nu_tau inverse-decay path optical depth for the dominant 8--15 km emission region. The self-consistent 20--22 km temperature stress test is complete; see Section 6 and [Actions run 42554811330](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42554811330). Its +/-10% variations are diagnostic stress tests, not statistical uncertainty intervals.

The full source-curve coverage and pointwise comparisons are recorded in [BOLLIG_OUTER_THERMODYNAMIC_PROFILE_15_22KM_2026-11-09.md](BOLLIG_OUTER_THERMODYNAMIC_PROFILE_15_22KM_2026-11-09.md). The machine-readable result is [bollig_outer_thermodynamic_profile_15_22km_2026-11-09.json](outputs/bollig_outer_thermodynamic_profile_15_22km_2026-11-09.json).

## 6. 20--22 km temperature sensitivity: completed

The self-consistent B.1+B.2 stress test varies only T(r) in the 20--22 km shell, using the same 10 MeV pure-vector reference and the N_r=40, N_E=100, N_omega=32, N_s=32 grid. The 176 affected profile nodes have baseline temperatures from 3.5514 to 4.2044 MeV. All other profile fields, including mu_mu, mu_numu, and lapse, remain unchanged.

At baseline, the B.1 thin-source fraction emitted in 20--22 km is only 0.07453%. The independent full B.1+B.2 path-matrix recomputation gives a 12.719% share of the neutrino inverse-decay path optical depth for 8--15 km emission (12.8945% for all emission radii). The earlier channel-shell-directional synthesis gives 12.81% for the 8--15 km subset; the 0.09 percentage-point difference is retained as a small cross-pipeline diagnostic difference, not averaged away.

For a +/-10% temperature stress:
- Strong-endpoint escaped luminosity changes by -0.1493% / +0.1507%.
- Strong-endpoint escape probability changes by -0.1208% / +0.1125%.
- The strong-endpoint Fig. 7 discrepancy remains approximately +91.96% to +92.54%, compared with +92.25% at baseline.

The same-grid channel, shell, direct-chord, and source-weighted mean-optical-depth closure checks pass at floating-point precision. The 20--22 km temperature variation is therefore not a plausible explanation for the order-one strong-coupling mismatch at the tested +/-10% level. This is not a statistical uncertainty estimate and does not certify the true Garching background. Full details are in [B16_OUTER_TEMPERATURE_SENSITIVITY_20_22KM_2026-11-09.md](B16_OUTER_TEMPERATURE_SENSITIVITY_20_22KM_2026-11-09.md).

## 7. Current decision

- Radial, energy, angular, and path global quadrature: passed the stated project-level luminosity-stability targets at the tested resolutions.
- Same-grid B.16 closure: passed for all four global B.13 configurations with zero residual.
- Global convergence artifact archival: partial only; the original full JSON upload failed because the Actions storage quota was exhausted. The compact log-recovered summary is explicitly labelled and archived.
- Local B.13 collision-kernel quadrature: sampled-point high-order validation passes at the three representative points, with a maximum 20-to-24 order change of 0.03016% against the audit-specific 0.1% screening target. The full continuous r-omega domain is not certified.
- B.16 neutrino inverse-decay radial path: current-profile shell, angle, and leave-one-out synthesis is documented in B16_NEUTRINO_INVERSE_DECAY_RADIAL_PATH_SYNTHESIS_2026-11-09.md. The 8-22 km path group dominates collectively, while 22-25 km remains individually important.
- Fig. 7 mismatch: persists after numerical convergence and must be investigated as a separate physical/reproduction issue.
- Axial-vector production curve: remains frozen.
