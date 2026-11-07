# Axial EFT cooling calculation and referee response

Date: 2026-11-06. Authorized scope: finish a reproducible cooling calculation, make a constraint figure, write the scientific response, submit a PR. No manuscript edits.

## Design and scientific scope
Use the axial-vector EFT benchmark with the pure axial muon current and the two specified active-flavor neutrino currents. Compute a fixed-profile SN1987A ballistic cooling benchmark including three polarization modes, neutrino inverse decay/decay, exact-recoil muon-rest inverse Compton with an effective Pauli-blocked muon density, and dimuon inverse decay/decay above threshold. Use mode-by-mode detailed balance and reduced opacity; propagate each polarization separately and sum escaped luminosities only after attenuation. Keep scalar summed-opacity runs as diagnostics, not as the physical mode-resolved solver. The calculation is a stationary-profile transport approximation, not a hydrodynamic SN simulation or a LESN/high-energy-neutrino recast.

Primary inputs: Liu–Miller1705.01633 vacuum matrix element; Blinov2511.09619 App B transport; published SFHo18.8 t=1s profiles, digitized from public vector figures when original tables are access controlled. Record digitization and all reconstructed tails. Threshold4.4e52 erg/s; compare3e52. Source redshift N² and Emin=M/N follow Blinov; fixed local energy along straight chords is an approximation.

## Implementation plan
- [x] Read latest main, instructions, existing response and prior kernel work; isolated worktree based on0f3816e.
- [x] Preserve published profile curves and reproducible extraction/provenance.
- [x] Independently test mode-resolved kernels, detailed balance, widths, crossing, Thomson and longitudinal limits.
- [x] Implement angular escape and luminosity; test analytic uniform-sphere escape, zero opacity and g² scaling.
- [x] Scan mass/coupling; quantify quadrature, cutoff and profile/approximation sensitivity; plot axial, vector-current comparison and original Fig2 window.
- [x] Extend Major4.4 without removing independent old arguments; update Major2 cross-reference and manuscript synchronization checklist.
- [x] Compile current response, inspect figures and relevant PDF pages; verify quotations/citations and actual numerical outputs.
- [x] Audit the actual scientific/layout diff and record preservation/deletion ledger in VALIDATION_AND_REVIEW.md.
- [x] Second-pass internal code/formula audit in the integration pass (not a separate independent reviewer). The spin-degeneracy factor 2 is already included in the effective target density: under `p=p_max(1+x)/2`, the Jacobian `dp=p_max dx/2` supplies the compensating factor `1/2`. An independent adaptive-quadrature regression test locks this normalization; the existing scan outputs remain unchanged.
- [x] Commit and push the research branch; PR #56 remains Open / Draft. The numerical checks and a 65-page LaTeX/PDF build with source-preservation audit and visual review have passed on the unchanged scientific source. The PDF-publication refspec fix has passed a fresh Actions run (42165491749); the current 65-page PDF and audit fingerprint are committed. No merge has been performed.

## Review focus
Mode degeneracy belongs outside the escape exponent. Opacity includes1/v and reduced absorption. Muon chemical potentials include rest energy. Strong-coupling surface layers need resolved quadrature. Source-figure digitization is not raw simulation data. Excluded area is specific to listed channels/approximations; unshaded area is not a globally allowed region. Omitted processes and backreaction are scientific scope limits, not internal task status.

## Preservation audit baseline
Existing Major4.4: relevance; vector reference scales including LESN; Kahn citation; unchanged active neutrino current; vector benchmark coalescence dominance; axial Ward identity/Goldstone scale; threshold widths; kinetic-mixing scaling and its vacuum limitation. Preserve every independent argument and qualify vector-only dominance. New calculation supersedes only the statement that no axial-specific contour is used; record the replacement.


## Stage 1: Blinov polarization-resolved rate audit (2026-11-07)

**Status: derivation and source/code audit recorded; production code unchanged.**

See [POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md](POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md), cross-linked from [VECTOR_BENCHMARK_AUDIT_2026-11-07.md](VECTOR_BENCHMARK_AUDIT_2026-11-07.md).

- B.6–B.10: resolved the chiral-neutrino inverse-decay rate into (L,+,-); each mode obeys detailed balance, and the sum reproduces the factor 3 in B.7. The current code assigns the neutrino rather than antineutrino to daughter 1, which swaps the two circular labels but leaves the longitudinal mode and total unchanged.
- B.11–B.12: resolved the vector dimuon channel into longitudinal and transverse weights; the width, total sum, and per-mode balance agree with the current implementation.
- B.13–B.19: resolved the inverse semi-Compton kernel by incident vector polarization. The per-mode Thomson limit and summed photon/velocity normalization are checked. The existing thermal kernel is a stationary-muon/effective-density approximation, not the full moving-muon integral.
- **Comparison control:** the existing `exact_modes` and `blinov_literal` scans also change the semi-Compton prescription (finite-recoil stationary-muon kernel versus the analytic no-recoil B.14–B.16 kernel). Their contour difference is therefore not a pure polarization-normalization test. If Stage 2 is authorized, separate the two comparisons by changing one ingredient at a time.
- B.2/B.4: the printed scalar opacity has no explicit polarization prescription. A summed production rate must be paired with a production-weighted escape factor; it is not generally consistent to exponentiate a polarization-summed absorption rate.
- B.17: the printed susceptibility integral does not explicitly state whether the charge-conjugate muon species is included; the current effective density includes both charges. Keep this convention open rather than changing it silently.

**Supplemental regression work:** added `test_stage1_detailed_balance.py` with (i) a pointwise B.19 test using the actual inverse-Compton matrix elements for L,+,- and both muon charges, (ii) a three-mode opacity-shape test, and (iii) an independent adaptive-quadrature check of the two-charge susceptibility. Added `audit_muon_susceptibility.py` plus the saved `outputs/vector_audit/muon_susceptibility_charge_audit.json`, which quantify the B.17 charge-conjugate convention on the selected profile. The inner-core $\mu^+$ fraction is 0.3–1.3%; it is negligible at larger radii in absolute density. The printed B.17 convention remains unresolved.

**Disposition:** keep the production solver mode-resolved. Do not change the opacity normalization, introduce a factor of 3, or modify scan outputs in Stage 1. The complete 30-test suite, saved scan validation, figure regeneration, and numerical audit reproducibility pass in [GitHub Actions run #49](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42284283285). Stage 2 starts only after the B.2 opacity convention and B.17 charge convention are explicitly addressed. PR #56 remains Draft; manuscript and referee response remain untouched.


## Stage 2 reset: independent Blinov scalar reproduction (2026-11-07)

**Purpose:** separate literal reproduction of the reference paper from validation of the existing mode-resolved production solver. No existing scans, audit records, figures, manuscript source, or referee-response files are deleted or overwritten.

**New independent module:** [blinov_reproduction/README.md](blinov_reproduction/README.md).

- [x] Create an isolated implementation that imports neither production rates.py nor transport.py.
- [x] Transcribe the summed neutrino/dimuon rates, nonrelativistic no-recoil semi-Compton rate, single-species Eq. (33) degeneracy factor, scalar reduced opacity, full chord/direction average, and luminosity integral.
- [x] Add regression tests for the Fermi-integral rest limit, archived independent decay-rate formula, Compton Thomson limit, Eq. (35) detailed balance, and constant-opacity chord integration.
- [x] Add a comparison script for digitized Fig. 4 cooling contours and Fig. 7 luminosity curves.
- [x] Add CI execution and archival of the generated four-mass scan and comparison JSON.
- [x] Inspect the new run's actual Fig. 4 and Fig. 7 residuals; do not label reproduction successful from unit tests alone.
- [ ] Compare the independent scalar reference against the existing mode-resolved solver under matched microphysics and transport inputs, varying one ingredient at a time.
- [ ] Only after the vector benchmark is understood, resume axial-vector result validation.

**First-run result:** the 40/100/16/32 quadrature scan matches the digitized Fig. 4 lower/upper boundaries at 1, 10, 100, and 200 MeV to within 2.60%. The Fig. 7 pointwise residuals are 5.54% max / 1.60% mean at 1 MeV, 91.35% max / 15.64% mean at 10 MeV, and 1.59% max / 0.71% mean at 200 MeV. Thus the boundary match does not establish complete luminosity-curve reproduction; 10 MeV remains a clear mismatch. Numerical outputs are saved in blinov_reproduction/outputs/ and include code/profile/input hashes and the run commit SHA.

**Interpretation boundary:** this module implements the scalar Appendix-B prescription literally, including the scalar opacity. It is a reference-reproduction path, not a declaration that scalar summed opacity is the physically correct per-particle attenuation law when the three polarization opacities differ. The original authors' private numerical choices are not inferred. The profile remains the archived reconstructed SFHo-18.8, t=1 s profile; it is not original simulation data.

**Scope freeze:** do not change production rates.py, transport.py, existing vector/axial scans, constraint plots, manuscript source, or referee-response TeX/PDF in this stage. PR #56 remains Open / Draft.


## Stage 3: finite-mixing vector–axial extension (2026-11-07)

**Status: UV coupling map plus amplitude-level mixed Compton/dimuon kernels and endpoint tests are added; no mixed-current luminosity scan or constraint curve is yet claimed.**

The dedicated module is [finite_mixing/README.md](finite_mixing/README.md). The UV coupling map is implemented in [finite_mixing/model.py](finite_mixing/model.py), with endpoint and chiral-coupling tests.

The required muon-current convention is
\[
\mathcal L_{\mu A'} =
A'_\mu\bar\mu\gamma^\mu
(g_V^\mu+g_A^\mu\gamma^5)\mu,
\quad
g_V^\mu=g_X\sin^2\theta_{\mu R},
\quad
g_A^\mu=-g_X\cos^2\theta_{\mu R}.
\]
The rates module's axial basis is \(\gamma^\mu(-\gamma^5)\), so its coefficient is \(-g_A^\mu\), not \(g_A^\mu\). The active-neutrino couplings remain \(g_{\nu_\mu}=+g_X\) and \(g_{\nu_\tau}=-g_X\), independent of \(\theta_{\mu R}\).

### P0 prerequisite: pure-vector endpoint

Before any mixed-current cooling curve is accepted, the pure-vector endpoint must reproduce the **published version-of-record** Blinov et al. result. The current audit is not yet a pass:

- The independent scalar Appendix-B path matches the currently archived digitized Fig. 4 boundaries at four masses within 2.60%, but its Fig. 7 pointwise comparison has a 91.35% maximum and 15.64% mean absolute relative residual at 10 MeV.
- The existing mode-resolved vector solver closes at 259.08–259.14 MeV, whereas the currently archived Fig. 4 digitization reaches about 210.98 MeV.
- These two paths differ in both the opacity prescription and the semi-Compton treatment; neither a fitted coupling-axis rescaling nor a posteriori factor-of-two opacity change is allowed.

The current Fig. 4/Fig. 7 digitizations originate from the arXiv source archive. The published JHEP version-of-record figures must be independently checked and digitized before final acceptance. The full gate and acceptance targets are recorded in [VECTOR_ENDPOINT_GATE_2026-11-07.md](finite_mixing/VECTOR_ENDPOINT_GATE_2026-11-07.md).

### Execution order

1. Re-extract the published version-of-record Fig. 4 and Fig. 7 reference curves, recording source PDF hashes and digitization provenance.
2. Resolve the pure-vector local-rate, polarization/opacity, and transport comparison one ingredient at a time. Preserve detailed balance and do not insert fitted rescaling factors.
3. Require both contour-boundary and full-luminosity-curve agreement before declaring the vector benchmark passed.
4. The local amplitude-level vector–axial kernels are implemented and endpoint-tested; only after the vector gate passes, integrate them into the transport scan and run the three endpoints: pure axial, pure vector, and the UV benchmark \(\theta_{\mu R}=10^{-2}\).
5. Keep the existing axial scan and all referee-response/manuscript files unchanged until the mixed result passes its own convergence and endpoint tests.

**Disposition:** PR #56 remains Open / Draft. The mixed-current module is deliberately blocked at the vector-validation gate; no mixed constraint curve is presented as a result.


### Version-of-record figure check

A visual side-by-side check of the published JHEP PDF and arXiv v2 finds no visible changes to Fig. 4 or Fig. 7 (published PDF pp. 16 and 24; arXiv v2 pp. 17 and 26). This does not replace exact path-level re-digitization; the archived vertices remain the arXiv-source extraction. The published text also states that the no-recoil semi-Compton approximation is typically relevant for m_V below the MeV scale, making the 10 MeV tail a priority for controlled Compton/profile comparisons. See [finite_mixing/VECTOR_ENDPOINT_GATE_2026-11-07.md](finite_mixing/VECTOR_ENDPOINT_GATE_2026-11-07.md).


### 10 MeV profile-sensitivity result

A one-factor test replacing only the Caputo \(\mu_\mu(r)\) curve with the separate Ferreira curve gives a worse full Fig. 7 residual (mean 42.13%, maximum 65.04%, versus 15.73% and 92.24% for the baseline) and does not resolve the high-coupling tail. The Caputo central \(\mu_\mu\) independently reproduces the plotted muon density to about 0.5%; adding \(m_\mu\) to it is incorrect. The exact s18.8-SFHo-MUONS simulation profile is not publicly accessible from the current Garching archive endpoint (HTTP 401), and the paper does not deposit its simulation data/code. Thus exact point-by-point Fig. 7 reproduction is not currently supportable from the reconstructed profile. See [VECTOR_ENDPOINT_GATE_2026-11-07.md](finite_mixing/VECTOR_ENDPOINT_GATE_2026-11-07.md) and the archived [profile-sensitivity output](../blinov_reproduction/outputs/muon_profile_sensitivity_10mev.json).

## Final agreed validation order (2026-11-07)

**Decision:** use Selection 1 as the main project structure and retain only the necessary independent-integral checks from Selection 2 as lower-level validation tools. Do not expand the project into a general-purpose full supernova transport calculation.

### Ordered execution and current evidence

1. **P0-A — independent forward/reverse rate tests: PASS within the stated approximations.**
   - Run the new adaptive-quadrature neutrino and direct B.14 Compton tests and archive the actual JSON/CI result.
   - Neutrino production and absorption are already evaluated separately in the production implementation; the adaptive reference is an independent numerical cross-check.
   - Keep the B.14 no-recoil Compton test distinct from the full moving-muon B.13 thermal integral.
   - **Status: PASS for the scoped local-rate audit.** GitHub Actions run [#6](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42318485267) completed successfully: all 82 repository physics tests passed, and the independent adaptive audit evaluated 60 neutrino points and 60 B.14 Compton points. Maximum relative errors were: neutrino production vs. production solver `3.91e-15`; neutrino absorption `3.96e-15`; neutrino mode balance `1.07e-15`; Compton mode balance `2.38e-16`; B.14 spin-summed normalization `3.94e-16`. The two-charge susceptibility also passed an independent density-derivative regression. Machine-readable results are committed at `outputs/direct_collision_integrals_2026-11-07.json` (audit run SHA `4ee2375`, archival commit `608b4af`). This closes only the local integral checks; it does not validate the full moving-muon B.13 Compton integral, the 10 MeV Fig. 7 tail, or stellar transport.

2. **P0-B — complete the literal Blinov Fig. 7 comparison.**
   - The source-PDF audit has now identified all six vector paths in the pinned arXiv v2 source member `luminosity_snapshot_t=1.pdf`: 10^{-6} MeV (drawing 39, 83 segments), 10^{-5} MeV (40, 83), 0.1 MeV (41, 45), 1 MeV (42, 34), 10 MeV (43, 27), and 200 MeV (44, 14). The source PDF SHA-256 is `4d7d1d10bfe2b52992af94df98749fa3adac887c009cbf98515fa12e6c48fdb5`; the source archive SHA-256 is `ea5bf58438c6442f24b3b781842fdb4ccbec80383c53d605a44ddf224ade8729`. Drawing metadata is archived in `outputs/fig7_source_drawings_2026-11-07.json`.
   - `compare_vector_luminosity.py` now extracts all six source-PDF paths and checks their drawing index, colour, segment count, and pinned PDF SHA-256. The full six-mass scan and comparison completed successfully in [Actions run #42319703283](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42319703283). Outputs are archived in `outputs/vector_audit/luminosity_comparison.json`, `blinov_reproduction/outputs/blinov_fig7_six_mass_scan.json`, and `blinov_reproduction/outputs/fig7_six_mass_comparison.json`.
   - Full-curve residuals (mean/max absolute relative difference): 10^{-6} MeV 24.56%/82.28%; 10^{-5} MeV 24.21%/82.45%; 0.1 MeV 7.15%/36.13%; 1 MeV 1.51%/5.39%; 10 MeV 15.70%/92.15%; 200 MeV 0.82%/1.72%. Only 1 and 200 MeV meet the provisional mean <=5%, max <=10% criterion. **P0-B is not passed.**
   - Residuals are small in the weak-coupling portions of the light-mass curves but grow in the high-coupling/trapping tails. For example, the 10^{-6} and 10^{-5} MeV calculations are within about 2% at weak coupling but underpredict the high-coupling tail by roughly 35--50%; the 10 MeV high-coupling tail is overpredicted by about 92%. This points to a transport/opacity or profile-sensitive discrepancy, but does not yet identify its cause.
   - A controlled high-resolution scan (88/180/24/64 versus 40/100/16/32) is now running to test quadrature convergence and compare the independent scalar implementation with the separate vector-audit implementation. No coupling rescale or opacity multiplier is permitted.
   - The exact s18.8-SFHo-MUONS source profile is not available in the current public source archive; current results use a reconstructed SFHo-18.8 profile. Label all such results as reconstructed-profile comparisons, not exact reproduction of the authors' private run.

3. **P0-C — Fig. 4 ballistic-cooling boundary comparison.**
   - The seven-mass scalar scan rechecked the four Fig. 4 points (1, 10, 100, 200 MeV). Lower/upper crossing deviations are +0.80%/-0.78%, +0.33%/+1.03%, -0.90%/+1.09%, and -1.44%/+2.91%, respectively.
   - The current four-point comparison is within the provisional 3% tolerance, but the 200 MeV upper boundary is close to the threshold. Treat P0-C as **provisionally passing**, pending the high-resolution convergence run. This is a digitized-contour comparison using a reconstructed profile, not exact recovery of the authors' simulation.
   - Do not infer that the Fig. 7 luminosity curves have passed from the Fig. 4 contour crossings.

4. **P1 — compare mode-resolved transport with the published polarization-summed prescription.**
   - Hold all microphysics and profile inputs fixed; change only the opacity/transport prescription.
   - Compare scalar summed, production-weighted, and per-mode survival probabilities. Do not assume \(\sum_h e^{-\tau_h}=e^{-\sum_h\tau_h}\).
   - Record differences in escaped luminosity, not merely local opacity.

5. **P2 — finite-mixing/axial extension.**
   - Start only after the pure-vector Lane-A full Fig. 7 gate passes and the Lane-B mode-resolved transport prescription is documented.
   - Run pure vector, pure axial, and the UV finite-mixing benchmark using the same profile, phase-space conventions, and transport implementation.
   - No mixed-current exclusion curve is promoted before endpoint, convergence, and literature checks pass.

### Scope control

- Keep the existing production rates, transport outputs, axial figures, manuscript, and referee-response files unchanged during this validation stage.
- No arbitrary rescaling of \(g_X\), production, absorption, or opacity.
- No broad stellar-model scan is required. Use the published benchmark profile and a small number of controlled diagnostics to isolate the mismatch.
- A failed or unavailable source-data comparison is reported as such; it is not repaired by tuning.
- PR #56 remains Open / Draft until the pure-vector literature gate is resolved.

## Latest execution update: full Fig. 7 and polarization transport (2026-11-07)

This section supersedes the earlier pending status statements above. It records actual completed runs; it does not authorize a mixed-current scan.

### P0-A — independent local collision integrals: PASS

The direct adaptive-quadrature audit and its repository-wide regression suite passed in [Actions run #42318485267](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42318485267). All 82 physics tests passed. The audit separately integrated neutrino production and absorption and the B.14 no-recoil Compton forward/reverse factors. Maximum relative errors are at the 10^-15 level. The output is archived in \`outputs/direct_collision_integrals_2026-11-07.json\`. This is a local-rate pass only; it is not a full B.13 moving-muon calculation or a transport validation.

### P0-B — six-mass Fig. 7 reproduction: NOT PASSED

All six PDF paths are now digitized and pinned. The published Fig. 7 source states that neutrino inverse decay dominates trapping above the MeV scale, while Compton absorption dominates at lower masses; the B.14 no-recoil approximation is specifically relevant for m_V ≲ MeV. The high-coupling region is also explicitly flagged by the paper as subject to significant fixed-profile/backreaction uncertainties.

The independent scalar Appendix-B scan has been repeated at several resolutions:

| m_V (MeV) | 88/180/24/64 mean/max residual | 132/280/40/96 mean/max residual |
|---:|---:|---:|
| 10^-6 | 9.47% / 28.54% | 4.62% / 12.90% |
| 10^-5 | 9.22% / 29.51% | 4.63% / 13.49% |
| 0.1 | 3.36% / 18.66% | 2.68% / 15.08% |
| 1 | 1.32% / 2.13% | 1.47% / 2.34% |
| 10 | 15.82% / 92.13% | 15.84% / 92.09% |
| 200 | 0.57% / 1.49% | 0.56% / 1.47% |

The ultralight 10^-6 and 10^-5 MeV scans are not yet converged: the 88/180/24/64 to 132/280/40/96 change on the published Fig. 7 vertices is about 6% mean and 24% maximum. A further 176/360/64/128 scan is running for these two masses. The 0.1 MeV curve is more stable but its maximum residual remains above the provisional 10% criterion. The 10 MeV mismatch is stable under quadrature refinement and remains about 16% mean / 92% maximum. Only 1 and 200 MeV currently meet the full-curve target.

The 10 MeV mismatch is not plausibly fixed by changing the B.14 Compton kernel alone: the paper identifies neutrino inverse decay as the dominant trapping channel above MeV, and the B.14 approximation is primarily relevant below MeV. A fixed-target exact-recoil diagnostic was also run; it worsens the 10 MeV literature residual and is not a substitute for the full moving-muon B.13 integral. Do not launch B.13 merely to fit the curve.

The 10 MeV high-coupling tail is in the regime where the paper itself warns that new-vector backreaction can invalidate a fixed SM stellar profile. The exact s18.8-SFHo-MUONS source profile has not yet been obtained. A matching provenance lead is now identified in the Garching archive's protected Bollig/Hüdepohl 1D PROMETHEUS-VERTEX collections (radial neutrino moments/spectral data/hydro profiles and hydro radial profiles), but the archive listing alone does not prove that the exact model and t_pb=1 s snapshot are included. The linked directories return HTTP 401 without credentials. An access request and exact model/time confirmation are now P0; see ORIGINAL_SFHO188_PROFILE_ACCESS_2026-11-07.md. Current comparisons remain reconstructed-profile comparisons, not exact reproduction.

### P0-C — Fig. 4 boundaries: PASS at the current resolution

The 88/180/24/64 scan rechecks the 1, 10, 100, and 200 MeV crossings within 2.82%, below the provisional 3% tolerance. The 200 MeV upper crossing is the limiting point. This is a digitized-contour check using the reconstructed profile, not a validation of all Fig. 7 luminosity curves.

### P1 — polarization transport comparison: quantified, not equivalent

A controlled four-lane comparison uses the same B.14 local Compton kernels and changes the treatment of polarization/opacity:

- \`blinov_literal\`: scalar summed opacity, matching the printed polarization-summed Appendix-B prescription;
- \`thomson_modes\`: identical B.14 local rates, but propagate each polarization with its own opacity;
- \`blinov_average\`: arithmetic mean opacity (sum divided by three), retained only as a diagnostic hypothesis;
- \`exact_recoil_scalar\` and \`exact_modes\`: fixed-target exact-recoil controls, not the full moving-muon B.13 calculation.

The signed comparison is archived in \`outputs/vector_audit/transport_prescription_comparison.json\`. The mode-resolved luminosity is higher than the scalar-summed luminosity at every digitized point. Its mean increase over the scalar-summed prescription is 111%, 157%, 677%, 447%, 558%, and 244% at 10^-6, 10^-5, 0.1, 1, 10, and 200 MeV, respectively; the maximum pointwise increase reaches factors above 100 in some tails. This is the nonlinear distinction between \`sum_h Q_h exp(-tau_h)\` and applying a polarization-summed opacity to every mode. The local mode rates sum to the scalar rates and pass the independent detailed-balance tests; the difference arises in transport, not from a missing local factor.

The arithmetic-average-opacity diagnostic does not reproduce the published curves and is not adopted. No factor of 1/3 or 3 is inserted into the production solver. The literal scalar-summed lane is retained only as the literature-reproduction benchmark; the mode-resolved lane is retained as the physically distinct polarization-resolved result. These lanes must not be conflated.

### Current decision and next actions

1. Finish the ultrafine light-mass convergence run.
2. Preserve the 10 MeV result as unresolved under the reconstructed profile; investigate only source-supported neutrino-profile and high-coupling transport sensitivities, not arbitrary opacity factors.
3. Do not run the finite-mixing or axial constraint scan yet. The pure-vector full Fig. 7 gate has not passed, and the two transport prescriptions are demonstrably inequivalent.
4. If a mixed-current result is eventually requested, report the Blinov-compatible scalar-summed lane and the mode-resolved lane separately, with the same current endpoints and profile in each lane. Do not claim the two are interchangeable.

PR #56 remains Open / Draft. The manuscript and referee-response files remain unchanged.



## Latest execution update: independent Eq. (B.2) path/angular integration (2026-11-08)

This update records the next transport-only validation. It does not change the local collision kernels, profile, chemical potentials, opacity normalization, production source, manuscript, or referee response.

### P0-D — independent path and angular integration: PASS

A separate implementation evaluates Eq. (B.2) in impact-parameter/longitudinal coordinates,
\[
b=r\sqrt{1-\mu^2},\quad z_0=r\mu,\quad
r'(z)=\sqrt{b^2+z^2},\quad
z_{\rm exit}=\sqrt{R_{\max}^2-b^2}.
\]
For the frozen piecewise-linear radial opacity interpolant, the line integral is evaluated analytically on each radial cell. The angular average is independently recomputed at 16, 64, 128, and 256 Gauss-Legendre nodes and checked at selected points by adaptive angular quadrature.

- Six new ray-geometry/path/angular regression tests pass.
- The full Major 4.4 numerical-validation workflow passes, including repository-wide tests and saved-scan reproducibility.
- At identical 16 angular nodes, replacing the existing 32-node path quadrature with the analytic path integral changes the integrated luminosity by at most \(4.31\times10^{-5}\) over the 25 Fig. 7 points.
- The angular luminosity sequence is converged: the maximum 128-to-256 change is \(1.10\times10^{-7}\) over the curve and \(8.20\times10^{-9}\) at the high-coupling endpoint.
- The high-coupling 10 MeV residual remains \(+92.24691\%\); the mean absolute residual remains \(15.7326\%\).

**Decision:** the approximately 92% high-coupling discrepancy is not caused by the numerical path integral or angular quadrature of the current scalar reference implementation. Do not retune chemical potentials, local rates, or opacity, and do not spend further effort increasing the Eq. (B.2) quadrature order.

### Independent outer-shell result

The exact-boundary path decomposition gives
\[
\frac{\langle\tau_{\nu,15-25}\rangle}
{\langle\tau_{\nu,\mathrm{total}}\rangle}=0.6311733,
\]
consistent with the earlier 63.17% estimate. The two flavor contributions remain nearly equal. This is a fraction of the source-weighted mean neutrino optical depth, not a fraction of the luminosity absorbed.

By production-radius bin, the outer 15–25 km shell contributes 59.42%, 58.04%, 65.91%, 87.53%, and 95.58% of the neutrino optical depth for the 0–5, 5–10, 10–15, 15–20, and 20–25 km source bins, respectively. At the high-coupling point, the escaped luminosity is dominated by sources at 5–15 km.

### Archived records

- Detailed report: research/stellar-cooling-constraints-20261105/blinov_reproduction/EQ_B2_INDEPENDENT_PATH_INTEGRAL_AUDIT_2026-11-08.md
- Independent implementation: research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_eq_b2_path_integral.py
- Regression tests: research/stellar-cooling-constraints-20261105/blinov_reproduction/test_eq_b2_path_integral.py
- Machine-readable output: research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/eq_b2_independent_path_integral_2026-11-08.json

### Next action

Keep the validated local rates and Eq. (B.2) path/angular integral frozen. Move to the remaining non-transport possibilities in the established order: verify the paper's energy convention along a ray, independently recheck the digitized 10 MeV Fig. 7 tail, and then assess the reconstructed-profile/fixed-background limitation. PR #56 remains Open / Draft; the manuscript and referee-response files remain unchanged.


## 2026-11-08 follow-up: energy-frame ambiguity, Fig. 7 vector digitization, and spatial weights

The four requested checks are separated and documented in blinov_reproduction/FIG7_10MEV_FOLLOWUP_DIAGNOSTIC_2026-11-08.md.

### 1. Energy convention — ambiguity identified, two lanes retained

- Appendix-B Eq. (B.2) literally uses the same numerical \(\omega\) along the path.
- The main-text Eq. (4.2) describes \(\omega\) as energy at spatial infinity.
- Appendix-B Eq. (B.1), through the lower limit \(m_V/N(r)\), the \(N(r)^2\) prefactor, and the local \(k\), \(T(r)\), and \(v_V\) dependence in Eqs. (B.5)–(B.19), instead uses a local production-frame energy.
- The published JHEP 06 (2026) 155 version retains the same convention wording and equations. Its Data Availability and Code Availability Statements say no associated data or code will be deposited, so the authors' internal numerical implementation cannot be inspected.

**Decision:** the fixed-numerical-\(\omega\) path remains the literal Appendix-B equation lane. The conserved-\(E_\infty\) remapping remains a separate partial-GR diagnostic on the same Euclidean chord geometry. It is not a full GR ray-tracing result and cannot be asserted to reproduce the authors' unpublished code.

At the high-absorption point, the conserved-\(E_\infty\) diagnostic lowers the luminosity by 29.2634%, but still leaves a +35.9708% residual relative to the digitized Fig. 7 point. No fit or opacity adjustment is adopted.

### 2. Fig. 7 digitization — native vector path verified

The 10 MeV curve is reconstructed from the native vector drawing in the pinned arXiv v2 PDF, not from screenshot pixels. The audit records 27 line segments, 28 raw vertices, and 25 visible vertices; coordinate round-trip residuals are at floating-point precision. This rules out ordinary raster digitization as a plausible source of the 92% tail discrepancy, while not recovering the authors' original unplotted numerical samples.

### 3. Spatial weights — joint production/absorber matrix completed

The new matrix independently separates production-radius bins from absorber-radius bins using frozen local rates and the validated analytic Eq. (B.2) path integral.

- 97.12% of the optically thin source is produced at 5–15 km.
- At high coupling, 59.13% and 37.43% of the escaped luminosity originate at 5–10 km and 10–15 km, respectively.
- The neutrino optical-depth fraction accumulated at 15–25 km is 59.42%, 58.04%, 65.91%, 87.53%, and 95.58% for production radii 0–5, 5–10, 10–15, 15–20, and 20–25 km.
- Semi-Compton opacity is concentrated at 5–15 km; the extended outer opacity is neutrino inverse decay.
- The local channel sum closes at \(5.94\times10^{-16}\); exact absorber-shell additivity is below \(1.54\times10^{-14}\).

The outer-shell optical-depth share is not an absorbed-luminosity fraction. No local rate or profile input is altered.

### 4. Fixed-background caveat — physical interpretation only

Blinov et al. explicitly warn that above the \(\lambda_{\rm mfp}(T_{\max})=R_\nu\) line, the vector can modify supernova energy transport and fixed-SM-profile constraints become uncertain. Using their rough Eq. (4.3), \(m_V=10\) MeV and the reconstructed \(T_{\max}=33.92\) MeV gives \(g_{\rm line}\sim1.01\times10^{-8}\), while the high-absorption endpoint is \(4.17\times10^{-8}\). The endpoint is therefore in the paper's fixed-background-caveat region.

This limits the physical interpretation of the high-coupling curve; it does not explain a numerical mismatch between our evaluation and Fig. 7, since Fig. 7 itself is calculated on the prescribed fixed profile.

### Reproducibility

- Report: blinov_reproduction/FIG7_10MEV_FOLLOWUP_DIAGNOSTIC_2026-11-08.md
- Spatial audit: blinov_reproduction/audit_fig7_spatial_weight_matrix.py
- Tests: blinov_reproduction/test_fig7_spatial_weight_matrix.py
- Machine-readable matrix: blinov_reproduction/outputs/fig7_spatial_weight_matrix_2026-11-08.json
- CI: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42409199703 (success)

PR #56 remains Open / Draft. No manuscript or referee-response source/PDF is modified.
