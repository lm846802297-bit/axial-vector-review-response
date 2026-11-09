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

The original Bollig Fig. 1 and Fig. 4 plotting frames both end at 20 km. The 20--22 km interval has no direct original-figure temperature support and only the endpoint at 20 km for mu_mu/T. No Bollig curve is extrapolated. A separate Caputo source-PDF audit identifies clip rectangles ending at x_pdf=325, while the underlying T and mu_mu drawing paths continue outside the visible frame. There are 45 T vertices and 48 mu_mu vertices in 20--22 km; the T path continues with 57 vertices through 22--25 km, while the mu_mu path reaches the 1 MeV plotting floor at 22.1919 km and has no further encoded continuation. The committed vertex CSVs reproduce these PDF vertices with maximum relative residuals below 10^-12. These are encoded off-frame PDF vectors, not visible plot data or raw Garching tables. Thus the Caputo continuation has a traceable PDF origin but no independent Bollig cross-check beyond 20 km.

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

## 7. 20--22 km muon-neutrino figure-floor sensitivity: completed

The baseline profile has mu_numu=0 at all 176 retained nodes in 20--22 km because no branch is resolved there above the approximately 1 MeV figure floor. A self-consistent B.1+B.2 rerun assigns mu_numu=+1 MeV and -1 MeV throughout this shell, keeping T, mu_mu, lapse, and all other inputs fixed. The global quadrature is N_r=40, N_E=100, N_omega=32, N_s=32.

At the strong endpoint, either sign changes the escaped luminosity by only +0.00915% and the escape probability by +0.00936% relative to the zero baseline. At the reference luminosity peak, the escaped luminosity changes by +0.00481%. The +1 MeV and -1 MeV results agree exactly at the stored precision, as expected from charge-conjugation symmetry of the pair phase-space integral under symmetric angular integration. Numerical closure residuals remain at floating-point precision.

The unresolved 1 MeV chemical-potential floor in 20--22 km is therefore not a plausible explanation for the order-one strong-coupling Fig. 7 mismatch. This is a figure-floor stress test, not a measurement of the true mu_numu profile. Full results are in [B16_OUTER_NUMU_FLOOR_SENSITIVITY_20_22KM_2026-11-09.md](B16_OUTER_NUMU_FLOOR_SENSITIVITY_20_22KM_2026-11-09.md) and [Actions run 42555233650](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42555233650).

## 8. 22--25 km temperature sensitivity: completed

The Caputo source-PDF audit confirms 57 encoded off-frame T(r) vertices in 22--25 km, spanning 3.0363--3.5509 MeV. The original Bollig Fig. 1 and Fig. 4 frames end at 20 km, so this interval has no independent Bollig-figure cross-check. The mu_mu path terminates at 22.1919 km at the 1 MeV plotting floor; the current profile sets mu_mu=0 beyond that point. The 22--25 km B.2 path is therefore dominated by neutrino inverse-decay opacity.

A self-consistent B.1+B.2 temperature stress test varies only T(r) across the 222 retained 22--25 km nodes, with N_r=40, N_E=100, N_omega=32, N_s=32. The baseline B.1 thin-source fraction emitted in this shell is 0.07276%, while the independent full path-matrix calculation assigns 19.1084% of the neutrino inverse-decay path optical depth for 8--15 km emission (19.3314% for all emission radii), consistent with the earlier direction-resolved 19.07% result.

At the strong endpoint:
- +/-10% T stress changes escaped luminosity by -1.8133% / +2.7688% and escape probability by -1.7842% / +2.7268%.
- Broad +/-30% T stress changes escaped luminosity by -3.6191% / +12.4742% and escape probability by -3.5591% / +12.2910%.
- The Fig. 7 discrepancy moves from +92.25% at baseline to +85.29% for T scaled by 0.7 and +116.23% for T scaled by 1.3; it remains order-one.

The B.1 source contribution remains below 0.24% even in the +30% case, so the response is primarily B.2 propagation. The +/-30% cases are deliberately broad stress tests, not statistical uncertainty intervals or proposed profile corrections. Full results are in [B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md](B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md) and [Actions run 42556526873](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42556526873).

## 9. Bollig Fig. 3 density comparison and plotting-floor treatment: completed

The extended original-PDF audit covers 15--20 km. Caputo T and mu_mu/T continue to reproduce Bollig Figs. 1 and 4 with mean absolute relative differences of 0.00431% and 0.00468%, respectively (294 profile nodes each). The maximum absolute differences are 0.01628% and 0.01547%.

The Fig. 3 absolute-density curve reaches its lower plotting floor of 10^-7 fm^-3 at r=16.646591 km. Of 294 nodes in 15--20 km, 90 remain above the floor (last at 16.603079 km) and 204 are censored. Only the 90 uncensored nodes are used for a density comparison. On those nodes, the Fermi density reconstructed from Caputo T,mu_mu is 10.402% higher on average than Bollig Fig. 3 (maximum 12.019%); using Bollig Fig. 1 T and Fig. 4 eta gives 10.385% mean and 12.108% maximum. The 17--20 km floor-clipped values are not treated as physical density measurements.

This confirms that the published-figure-level absolute-density tension persists through the last uncensored Fig. 3 segment, while T and mu_mu/T remain independently matched. It does not identify the origin of the discrepancy. No density normalization, B.1 source, B.2 opacity, luminosity, or axial-vector output is rescaled. Full details: [BOLLIG_15_20KM_THERMODYNAMIC_CROSSCHECK_2026-11-09.md](BOLLIG_15_20KM_THERMODYNAMIC_CROSSCHECK_2026-11-09.md); workflow [42557233565](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42557233565).

## 10. Inner 8--12 km negative muon-neutrino branch sensitivity: completed

The self-consistent B.1+B.2 sensitivity audit [42557144227](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42557144227) varies only the resolved negative Caputo mu_numu branch in 8--12 km. The branch spans -20.43 to -4.31 MeV over 270 profile nodes. It is tested at zero, +/-10% magnitude variations, and a sign flip. Every scenario recomputes the full source and opacity on the 40x100x32x32 grid.

At the strong endpoint:
- Removing the entire branch changes escaped luminosity by -0.02228% and escape probability by -0.32761%.
- A 10% reduction changes escaped luminosity by -0.00423% and escape probability by -0.06177%.
- A 10% increase changes escaped luminosity by +0.00468% and escape probability by +0.06801%.
- Sign reversal leaves the integrated result unchanged at the stored precision.

The 8--12 km shell contributes 65.893% of the B.1 thin source and 15.9324% of the neutrino path optical depth for 8--15 km emission. The resolved negative branch is therefore a real input in an important region, but even its complete removal changes the strong-endpoint escaped luminosity by only about 0.0223%. The sign-flip equality is a charge-conjugation/symmetric-integration diagnostic, not evidence that the physical sign is irrelevant to every differential observable.

Full results: [B16_INNER_NUMU_BRANCH_SENSITIVITY_8_12KM_2026-11-09.md](B16_INNER_NUMU_BRANCH_SENSITIVITY_8_12KM_2026-11-09.md); machine-readable output: [b16_inner_numu_branch_sensitivity_8_12km_10mev_2026-11-09.json](outputs/b16_inner_numu_branch_sensitivity_8_12km_10mev_2026-11-09.json).

## 11. Physical impact of the 15--20 km Fig. 3 density mismatch: current-profile assessment

The older 0.0873% outer-shell opacity estimate used profile SHA-256 08d7afce... and is superseded for the current calculation. The current vertex-preserving B.16 benchmark uses profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c and has a different B.2 channel decomposition.

In the current benchmark:
- The total B.2 optical-depth fraction accumulated in 15--20 km is 27.8619%.
- Of this, 27.8538 percentage points come from neutrino inverse decay.
- The muon-Compton opacity contribution from 15--20 km is only 0.0080846% of the total mean optical depth.
- The Compton contribution in the density-comparison interval 15--16.5 km is 0.0080023% of the total mean optical depth.

Therefore, the large 15--20 km total path contribution is not caused by the Fig. 3 density mismatch; it is almost entirely the neutrino inverse-decay channel. The density discrepancy can affect only the muon-Compton component. Moreover, at fixed T and mu_mu, the one-species B.17 product n_mu F_deg equals the susceptibility integral chi_mu(T,mu_mu), so a consistent change in n_mu normalization is compensated by F_deg. A hypothetical 10% change in all 15--16.5 km Compton opacity would shift the total source-weighted mean optical depth by only 0.0008002% (absolute mean-tau shift about 1.29e-4 at the strong endpoint). This is a conservative sensitivity scale, not a new transport run.

The density mismatch remains an unresolved published-profile consistency issue, but it is not a plausible explanation for the order-one strong-coupling Fig. 7 mismatch in the current vertex-preserving B.16 benchmark. No empirical rescaling is applied. Full detail: [BOLLIG_15_20KM_THERMODYNAMIC_CROSSCHECK_2026-11-09.md](BOLLIG_15_20KM_THERMODYNAMIC_CROSSCHECK_2026-11-09.md).

## 12. Current vertex-preserving B.16 global channel decomposition: completed

The full current-profile B.16 result is [b16_global_fig7_vertex_preserving_10mev_2026-11-09.json](outputs/b16_global_fig7_vertex_preserving_10mev_2026-11-09.json), with profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. It must be distinguished from older B.16 audits using profile SHA-256 08d7afce....

Current B.1 thin-source channel fractions are 32.0050% Compton and 67.9950% neutrino inverse decay. Current B.2 source-weighted mean optical-depth fractions are 10.2218% Compton and 89.7782% neutrino inverse decay.

The 15--20 km shell contributes 27.8619% of the total B.2 mean optical depth, but 27.8538 percentage points are neutrino inverse decay. Its Compton contribution is only 0.0080846% of total mean optical depth. In the density-comparison shell 15--16.5 km, the Compton contribution is 0.0080023% of total mean optical depth. Thus the large outer-shell path contribution is not caused by the Fig. 3 muon-density residual. The older-profile estimate of 0.0873% for the full 15--20 km shell is superseded and must not be used for the current vertex-preserving benchmark.

At the strong endpoint, the fixed-omega B.2 baseline has \(L/L_{\rm Fig.7}-1=+92.2406\%\). The separately labeled path-redshift-only diagnostic shifts the luminosity by -28.8679% relative to fixed omega and leaves a +36.7448% discrepancy from Fig. 7. This alternative retains Euclidean straight chords and is not full GR ray tracing; Eq. (B.2) fixed omega remains the paper-faithful baseline. The redshift diagnostic therefore demonstrates sensitivity but does not solve the reproduction discrepancy.

Full channel and shell decomposition: [B16_VERTEX_PRESERVING_GLOBAL_CHANNEL_DECOMPOSITION_2026-11-09.md](B16_VERTEX_PRESERVING_GLOBAL_CHANNEL_DECOMPOSITION_2026-11-09.md).

## 13. Independent local absorption audit on current profile: completed

The B.6--B.10 and B.13--B.19 local audit was rerun on profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. It samples 16 radii and six energies (96 points), explicitly including the positive mu_numu branch at 16.75, 17.5, and 18.25 km and the 20--22 km shell at 20.5 and 21.5 km.

All independent local formula checks pass: maximum total production, absorption, and reduced-absorption closure residuals are 3.024e-14, 3.035e-14, and 3.048e-14. The separate maximum residuals for nu_mu/nu_tau B.6 production, B.10 detailed balance, neutrino B.4, Compton B.16 production, B.19, and Compton B.4 are all at or below 4.903e-14. The production axial-vector outputs remain unchanged.

This validates the current-profile local implementation of the printed Appendix-B reference formulae at the sampled points. It does not validate the physical accuracy of the B.14--B.16 no-recoil approximation, the global B.1/B.2 integration, or the Fig. 7 reproduction. Full report: [B16_LOCAL_ABSORPTION_VERTEX_PRESERVING_2026-11-09.md](B16_LOCAL_ABSORPTION_VERTEX_PRESERVING_2026-11-09.md); workflow [42558231626](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42558231626).

## 14. Exact moving-muon B.13 global alternative: completed

The current-profile global B.13 calculation consistently replaces both the Compton source and Compton reduced-absorption terms while retaining the published fixed-omega path prescription. It uses profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c and first reproduces the archived B.16 baseline on the same grids with zero residual.

For the like-for-like one-negative-muon case:
- B.16 reference implementation: weak -8.885%, peak +2.569%, strong +92.241% relative to Fig. 7.
- Consistent B.13 source-plus-opacity replacement: weak -28.109%, peak -16.340%, strong +131.530%.
- The optically thin source falls to 78.898% of B.16.
- At the strong endpoint, the escape probability rises from 3.23921e-4 to 4.94463e-4, but the source suppression dominates; the resulting luminosity is 131.53% above Fig. 7.

Thus the exact moving-muon B.13 replacement does not repair the Fig. 7 mismatch at 10 MeV; it worsens the strong-endpoint discrepancy. It remains a separate alternative physical calculation outside the regime where the paper motivates the B.14--B.16 no-recoil approximation. It is not substituted for the paper-faithful B.16 reference curve.

Full report: [B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md](B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md).

## 15. Independent SFHo-18.8 lapse-profile cross-check: completed qualitatively

A separate public visualization is identified in Zuowei Liu's 31 October 2026 presentation, slide 65, which plots the lapse factor versus radius for the SFHo-18.8 core and explicitly cites Bollig et al. (arXiv:2005.07141) and the Garching core-collapse supernova archive. The black lapse curve visually agrees with the current profile values over 0--20 km. Representative read-offs at 0, 5, 10, 15, and 20 km are approximately 0.735, 0.760, 0.810, 0.865, and 0.900; the current profile gives 0.73633, 0.75868, 0.81136, 0.86350, and 0.89889. The differences are within a few 10^-3, comparable to the rasterized slide read-off resolution.

This is qualitative visual corroboration, not precision digitization or access to the original Garching lapse table. It validates the radial trend and normalization of the lapse profile through 20 km; the 20--22 km continuation remains outside the plotted range. No lapse values are modified. Full report: [BOLLIG_LAPSE_PROFILE_VISUAL_CROSSCHECK_2026-11-09.md](BOLLIG_LAPSE_PROFILE_VISUAL_CROSSCHECK_2026-11-09.md).

## 16. B.1 local-energy / B.2 path-redshift convention audit: completed

The B.1 lower integration limit m_V/N(r) and N(r)^2 luminosity prefactor imply that the energy integrated at the production point is local. The literal B.2 exponent then uses the same omega at every path point, which holds the local-energy argument fixed along the chord. The main-text description of omega as energy at spatial infinity is not transparently consistent with that Appendix-B notation.

The repository keeps the literal Appendix-B fixed-omega prescription as the Fig. 7 reproduction baseline. A separate path-redshift-only diagnostic uses omega_loc(s)=omega_source*N_source/N(r(s)) while retaining Euclidean straight chords. At the strong endpoint it shifts the luminosity by -28.8679% relative to fixed omega, reducing the Fig. 7 residual from +92.2406% to +36.7448%; the weak and peak residuals become -8.8991% and -2.7704%. It does not close the discrepancy and is not a full GR ray trace.

A complete GR path calculation would also require a consistent spatial metric/path element, not just the lapse. The public profile has no independently tabulated A(r) or enclosed-mass profile for the full path. No baseline is changed. Full report: [B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md](B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md).

## 17. Independent analytic B.2 propagation implementation: completed

A second B.2 implementation now computes the chord integral analytically for the piecewise-linear radial opacity table. It uses z=s+r cos(theta), b=r sqrt(1-cos^2(theta)), splits each ray at all radial interpolation knots and the inward-ray turning point, and integrates A+B sqrt(b^2+z^2) exactly on each segment. The direction average is checked independently with Gauss-Legendre, composite Simpson, and adaptive QUADPACK. It shares only the local collision kernel, B.1 source measure, profile, and Fig. 7 reference with the baseline; it does not use the existing B.2 path integrator to generate its optical-depth columns.

Workflow [42562585233](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42562585233) passes, including the analytic-path unit tests, full 10 MeV calculation, baseline closure, and unchanged-production-output check.

The reconstructed original B.16 calculation reproduces the archived result to a maximum relative difference of 1.11e-16. At path order 128, the existing path quadrature differs from the analytic integral by at most 0.07193% pointwise, 0.01152% at the 99th percentile, and 0.001329% in source-weighted RMS; its maximum luminosity shift against the analytic 16-angle result is 0.0001396%. The Simpson-256 angular average differs from 27 adaptive QUADPACK checks by at most 1.146e-6 relative.

The final analytic-path/Simpson-256 luminosity curve differs from archived B.16 by at most 4.521e-5 relative (0.00452%). Its Fig. 7 residuals are -8.8853% at the weak endpoint, +2.5694% at the reference peak, and +92.2493% at the strong endpoint. Therefore the fixed-profile B.2 numerical path and angular integration is independently validated and cannot explain the order-one strong-endpoint discrepancy. This conclusion is conditional on the shared profile, local opacity, B.1 source measure, and literal fixed-omega Euclidean-chord prescription; it does not validate those physical inputs or resolve the energy-convention issue.

Full report: [B16_INDEPENDENT_ANALYTIC_PATH_INTEGRATION_AUDIT_2026-11-09.md](B16_INDEPENDENT_ANALYTIC_PATH_INTEGRATION_AUDIT_2026-11-09.md); machine-readable result: [b16_path_independent_analytic_10mev_2026-11-09.json](outputs/b16_path_independent_analytic_10mev_2026-11-09.json).

## 18. Independent B.1 optically-thin source integration: completed

The B.1 source integral with the escape factor set to one has now been independently evaluated using equal-width composite radial Gauss--Legendre quadrature and logarithmic-energy Gauss--Legendre quadrature in x=log(omega-m_V). The exact radius-dependent lower limit omega_min=m_V/N(r) is inserted at every radial node. The implementation evaluates the local production kernels directly at its new energy nodes and does not call eq_b1_source_measure, energy_weights, radial_rule, load_profile, or any B.2 path integrator.

Workflow [42563868176](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42563868176) passes, including four quadrature unit tests, the full 10 MeV source integration, channel closure, finite-JSON validation, and the unchanged-production-axial-output check.

The final 400-radial-node, 960-energy-node-per-radius source is 4.30436817e70 erg/s per g^2: 67.9313% neutrino inverse decay and 32.0687% muon-Compton; dimuon inverse decay is kinematically closed. The archived B.16 source is 4.32352241e70 erg/s per g^2, so the independent result is lower by 0.4430%.

The radial integral changes by only 0.002141% between 200 and 400 radial nodes. At 200 radial nodes, energy results are stable to the displayed precision from 80 to 240 logarithmic panels. Increasing the energy upper offset from 1000 to 4000 MeV changes the source by only 2.575e-9 relative.

A matched comparison reconstructs the archived 40 radial nodes and weights, but replaces the old energy grid/energy_weights with direct logarithmic-energy integration. At fixed 40 radial nodes, the independent energy integral is lower by 0.5755%. Refining the radial integral from 40 to 400 nodes then raises the source by 0.1332%, leaving the net -0.4430% difference against the archived B.1 source. Thus the discrepancy is sub-percent and is not large enough to explain the order-one strong-coupling Fig. 7 mismatch.

This validates only the optically-thin source integral with O=1. The full B.1 luminosity, including the escape factor O(r,omega), remains to be evaluated with the independent B.2 implementation on matched radial and energy nodes. Full report: [B16_INDEPENDENT_B1_THIN_SOURCE_AUDIT_2026-11-09.md](B16_INDEPENDENT_B1_THIN_SOURCE_AUDIT_2026-11-09.md); machine-readable result: [b16_b1_independent_thin_source_10mev_2026-11-09.json](outputs/b16_b1_independent_thin_source_10mev_2026-11-09.json).

## 19. Full independent B.1+B.2 luminosity integration: completed

The independently integrated optically-thin B.1 source and the analytic B.2 chord propagation have now been combined into a full 10 MeV vector luminosity calculation. For each source radius, the exact lower energy limit m_V/N(r) is inserted; local production and reduced absorption are evaluated at the new energy nodes; the optical depth is integrated analytically on a 202-node radial opacity grid; and the angular escape average is evaluated at 16 Gauss-Legendre directions for all 25 Fig. 7 couplings.

Workflow [42564417076](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42564417076) passes, including unit tests, full integration, source closure, radial stability, finite-JSON validation, and unchanged-production-output checks.

The final 200-source-node result has a 4.30427601e70 erg/s per g^2 optically-thin source, agreeing with the independent 400-node B.1 source audit to -0.002141%. Doubling the source radial nodes from 100 to 200 changes the full luminosity curve by at most 0.19867% over the 25 coupling points.

The full independent curve agrees with archived B.16 to a maximum absolute relative difference of 0.4451% and a mean absolute relative difference of 0.3975%. Against Fig. 7, it remains -9.2908% at the weak endpoint, +2.1522% at the reference peak, and +92.0542% at the strong endpoint. Thus the independent end-to-end implementation reproduces the archived calculation to sub-percent accuracy but does not remove the order-one strong-coupling mismatch with Fig. 7.

Full report: [B16_FULL_INDEPENDENT_B1B2_LUMINOSITY_AUDIT_2026-11-09.md](B16_FULL_INDEPENDENT_B1B2_LUMINOSITY_AUDIT_2026-11-09.md); machine-readable result: [b16_full_b1b2_independent_10mev_2026-11-09.json](outputs/b16_full_b1b2_independent_10mev_2026-11-09.json).

## 20. Dense local B.6--B.10 and B.14--B.19 audit: completed

The local production and absorption kernels used by the full independent B.1+B.2 calculation have now been independently checked on the exact global quadrature grid: 200 source radii times 320 exact-threshold energy nodes per radius, or 64,000 (r,omega) points.

At each radial node, neutrino B.6 production and inverse-occupation absorption are reconstructed from direct two-body angular phase-space integrals for nu_mu and nu_tau separately. The one-species B.17 negative-muon density and susceptibility are independently evaluated with the transformed momentum integral. Compton B.14--B.19 production, absorption, and reduced opacity are reconstructed from that susceptibility.

Workflow [42565336032](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42565336032) passes, including unit tests, the full 64,000-point audit, finite-output validation, and the unchanged-production-axial-output check.

Maximum residuals over the full grid:
- neutrino B.6 production: 6.31e-14;
- neutrino B.10 absorption: 6.00e-14;
- B.17 muon susceptibility: 2.65e-13;
- Compton B.16 production: 2.66e-13;
- total production/absorption/reduced absorption: 2.30e-13.

The 256-to-512 direct neutrino angular quadrature change is at most 1.20e-14. The nu_mu pair-production rate is invariant under mu_nu_mu -> -mu_nu_mu to 3.96e-15, as expected from exchanging the two initial-state energies in the symmetric angular integral.

This closes the local algebraic/numerical coverage gap for the B.16 vector baseline on the actual B.1+B.2 integration grid. It does not validate the physical no-recoil B.14--B.16 approximation against exact moving-muon B.13, nor the reconstructed stellar profile or the energy/GR propagation convention.

Full report: [B16_DENSE_LOCAL_KERNEL_AUDIT_2026-11-09.md](B16_DENSE_LOCAL_KERNEL_AUDIT_2026-11-09.md); machine-readable result: [b16_dense_local_kernel_audit_10mev_2026-11-09.json](outputs/b16_dense_local_kernel_audit_10mev_2026-11-09.json).

## 21. Current decision

- Radial, energy, angular, and path global quadrature: passed the stated project-level luminosity-stability targets at the tested resolutions.
- Same-grid B.16 closure: passed for all four global B.13 configurations with zero residual.
- Global convergence artifact archival: partial only; the original full JSON upload failed because the Actions storage quota was exhausted. The compact log-recovered summary is explicitly labelled and archived.
- Local B.13 collision-kernel quadrature: sampled-point high-order validation passes at the three representative points, with a maximum 20-to-24 order change of 0.03016% against the audit-specific 0.1% screening target. The full continuous r-omega domain is not certified.
- B.16 neutrino inverse-decay radial path: current-profile shell, angle, and leave-one-out synthesis is documented in B16_NEUTRINO_INVERSE_DECAY_RADIAL_PATH_SYNTHESIS_2026-11-09.md. The 8-22 km path group dominates collectively, while 22-25 km remains individually important.
- Independent B.2 propagation: analytic path integration, path-order convergence, and three independent angular-integration methods pass; the fixed-profile B.2 numerical implementation is not the source of the order-one Fig. 7 mismatch.
- Independent B.1 thin source: radial and logarithmic-energy quadratures pass; the optically-thin source differs from the archived source by -0.4430%, with energy and radial effects separated by the matched-40-node test.
- Full independent B.1+B.2: the 25-point luminosity curve reproduces archived B.16 to 0.4451% maximum relative difference; the Fig. 7 strong-endpoint residual remains +92.0542%. The end-to-end numerical integration is therefore validated at the sub-percent level for the adopted inputs.
- Dense local B.6--B.10 and B.14--B.19 audit: 64,000 actual global (r,omega) nodes pass independent phase-space/susceptibility checks with maximum residuals below 2.7e-13. The local B.16 formula implementation is validated over the full integration grid; the physical no-recoil approximation remains a separate issue.
- Fig. 7 mismatch: persists after numerical convergence and must be investigated as a separate physical/reproduction issue.
- Axial-vector production curve: remains frozen.
