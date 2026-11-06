# Axial EFT cooling calculation and referee response

Date: 2026-11-06. Authorized scope: finish a reproducible cooling calculation, make a constraint figure, write the scientific response, submit a PR. No manuscript edits.

## Design and scientific scope
Use the axial-vector EFT benchmark with the pure axial muon current and the two specified active-flavor neutrino currents. Compute a fixed-profile SN1987A ballistic cooling benchmark including three polarization modes, neutrino inverse decay/decay, exact-recoil muon-rest inverse Compton with an effective Pauli-blocked muon density, and dimuon inverse decay/decay above threshold. Use detailed balance and angle-averaged reduced opacity. The calculation is a stationary-profile transport approximation, not a hydrodynamic SN simulation or a LESN/high-energy-neutrino recast.

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
- [x] Independent code/formula audit in the integration pass. The spin-degeneracy factor 2 is already included in the effective target density: the (dp=p_{\max}dx/2) quadrature Jacobian supplies the compensating factor (1/2). An independent quadrature regression test is added to lock this normalization; the existing scan outputs remain unchanged.
- [x] Commit and push the research branch; PR #56 is open as a Draft for author review. Final merge remains pending exact-head numerical validation, LaTeX/PDF checks and review.

## Review focus
Mode degeneracy belongs outside the escape exponent. Opacity includes1/v and reduced absorption. Muon chemical potentials include rest energy. Strong-coupling surface layers need resolved quadrature. Source-figure digitization is not raw simulation data. Excluded area is specific to listed channels/approximations; unshaded area is not a globally allowed region. Omitted processes and backreaction are scientific scope limits, not internal task status.

## Preservation audit baseline
Existing Major4.4: relevance; vector reference scales including LESN; Kahn citation; unchanged active neutrino current; vector benchmark coalescence dominance; axial Ward identity/Goldstone scale; threshold widths; kinetic-mixing scaling and its vacuum limitation. Preserve every independent argument and qualify vector-only dominance. New calculation supersedes only the statement that no axial-specific contour is used; record the replacement.
