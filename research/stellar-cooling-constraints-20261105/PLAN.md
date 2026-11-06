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
