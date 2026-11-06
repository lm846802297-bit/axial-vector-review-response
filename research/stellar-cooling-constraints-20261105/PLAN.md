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
