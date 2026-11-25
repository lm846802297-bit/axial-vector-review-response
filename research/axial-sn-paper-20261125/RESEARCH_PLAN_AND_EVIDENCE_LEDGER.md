# Axial U(1)_{L_mu-L_tau} supernova-cooling paper: research plan and evidence ledger

Date opened: 2026-11-25
Repository: lm846802297-bit/axial-vector-review-response
Branch: research/axial-sn-paper-20261125
Base: main at branch creation
Status: ACTIVE — local model/Ward, moving-muon thermal, neutrino, and low-mass limit checks are accepted; radial mode-resolved transport remains the current gate.

## Research question

Determine whether the nonconserved charged-muon axial current in the original single-VEV axial U(1)_{L_mu-L_tau} model produces quantitatively different SN1987A cooling and trapping limits from the conventional vector L_mu-L_tau model, after mode-resolved production, inverse processes, decays, and escape/transport are treated consistently.

The target is a standalone paper, not an expansion of the referee response. The first controlled numerical domain is 0.01 <= m_A' <= 200 MeV (below dimuon threshold), with the original one-VEV model and finite-mixing charged-muon current. The extension above 2 m_mu is a separate stage requiring the dimuon channel and is not silently included.

## Model definition to preserve

Original single-VEV model:
- m_A' = 2 g_X v_s.
- g_V^mu = g_X sin^2(theta_muR).
- g_A^mu = -g_X cos^2(theta_muR), in the repository convention A'_alpha mu_bar gamma^alpha (g_V + g_A gamma5) mu.
- g_nu_mu = +g_X and g_nu_tau = -g_X.
- Benchmark theta_muR = 1e-2; also report the pure-axial theta_muR -> 0 limit.
- No extra neutrino states, no second scalar VEV, and no physical-scalar cooling contribution are introduced in this first paper.

Goldstone matching:
- c_mu = |g_A^mu|/m_A'.
- The physical longitudinal A' mode already contains the Goldstone-equivalence contribution. Never add a separate Goldstone production rate on top of the physical longitudinal polarization.
- The high-energy Goldstone relation is a validation limit, not a replacement for exact finite-mass longitudinal matrix elements.

## Literature already identified

1. Bollig et al., arXiv:2005.07141 (muon-rich SN profiles and muon-coupled pseudoscalar production; include published erratum/corrected result).
2. Caputo, Raffelt & Vitagliano, arXiv:2109.03244v3 (muonic bosons, free-streaming/trapping and SN profiles).
3. Lai et al., Phys. Rev. D 110, 103023 (2024) (vector L_mu-L_tau supernova production/absorption).
4. Blinov et al., arXiv:2511.09619v2 (vector benchmark, ballistic/diffusive/other SN probes; Appendix B).
5. Gori et al., arXiv:2506.11191 (axial-vector supernova estimates and longitudinal mode; must distinguish its source assumptions).
6. Das, Ghosh & Puri, arXiv:2606.23769 (independent longitudinal/transverse transport for light vector bosons).
7. Wang & Zhang, arXiv:2610.35379 (updated vector dark-gauge-boson SN constraints).
8. Fang et al., arXiv:2608.27258 (the original axial U_A(1)_{L_mu-L_tau} UV model).

The novelty claim must be checked against items 5 and 6 in full text before manuscript drafting. Merely splitting vector polarizations or quoting the ALP limit is not a novelty.

## Existing repository work — reuse, do not rerun

A. Existing conditional pure-axial fixed-profile contour:
- Directory: research/stellar-cooling-constraints-20261105/
- Sources: rates.py, transport.py, run_scan.py, outputs/axial.json and VALIDATION_AND_REVIEW.md.
- Uses reconstructed SFHo-18.8, not raw Garching simulation data.
- The rates.py semi-Compton kernel uses an initial muon-at-rest/effective-density approximation, not the exact moving-muon thermal integral.
- The archived contour is explicitly conditional and is NOT an accepted final SN1987A exclusion.
- The package itself records an unresolved vector benchmark discrepancy and profile limitations. Do not relabel the old contour as validated.

B. Existing original-UV A0 mixed-current transport:
- File: research/stellar-cooling-constraints-20261105/blinov_reproduction/croon_a0_uv_axial_transport.py
- Report: CROON_A0_UV_AXIAL_TRANSPORT_2026-11-20.md
- Reuses the moving-muon B.13 kernel with amplitude-level vector/axial interference and the original finite-mixing current.
- Current accepted scope is a 10 MeV interior-profile diagnostic with adaptive radial integration; outer 25–100 km semi-Compton opacity is omitted.
- The full six-mass scan is pending; no local primary run is archived. Actions-based convergence is not a substitute for the required local primary computation.
- Current engine restricts m_A' < 2 m_mu and omits dimuon inverse decay.

C. Vector controls:
- PR #123 defines independent Croon/Lai vector comparison lanes; its description explicitly says it does not update an axial SN exclusion.
- Blinov Fig. 7 10 MeV high-coupling tail remains discrepant by +92.4284% in the strict phase-space result. This discrepancy must remain visible and must not be tuned away.
- The SFHo-18.8 reconstructed profile SHA-256 is 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. Profile provenance identifies it as a reconstruction from published figures, not raw simulation data.

D. UV/analytic controls:
- research/stellar-cooling-original-uv-model-20261105/ contains the original-model axial semi-Compton matrix element, decay widths, single-VEV map, and Goldstone Ward-identity tests.
- low_mass_axial/ contains an existing low-mass derivation and exploratory numerical study; inspect its assumptions before reuse.

## Work packages and acceptance gates

### WP0 — Freeze inputs and literature map
Acceptance:
- Pin exact main/base commit, all reused source blob SHAs, profile SHA-256, paper versions/DOIs.
- Full-text audit of the axial SN literature, especially Gori et al. and Das et al.; write a novelty matrix.
- Explicitly distinguish paper-reported values from our independent calculations.
Status: PARTIAL (the relevant literature set and reusable methods are identified; the full-text novelty matrix for Gori et al. and Das et al. remains open before manuscript drafting).

### WP1 — Exact local collision kernels
Acceptance:
- Exact moving-muon thermal semi-Compton production and inverse absorption for mu- and mu+ targets.
- L,+,- mode resolution; finite-mixing V/A interference retained.
- Gauge Ward identities, positivity, threshold support, and mode-by-mode detailed balance pass.
- Goldstone/ALP limit reproduced in its domain, with no double counting of the longitudinal mode.
- Independent implementation/check of selected phase-space points.
Status: PASS_WITH_NOTES (exact moving-muon local thermal rates, explicit-v-spinor charge map, mode-by-mode detailed balance, Goldstone-equivalent longitudinal limit, and conserved-vector limit have independent archived checks; a standalone pseudoscalar thermal integral is not claimed).

### WP2 — Complete radial inputs and transport
Acceptance:
- Establish the source and meaning of T, mu_mu, mu_nu_mu, lapse, muon susceptibility, and outer 25–100 km medium inputs.
- Do not splice incompatible profiles without a quantified matching/provenance audit.
- Include angular escape, decay, absorption, redshift/lapse consistently, or state and validate a controlled approximation.
- Demonstrate path, radial, energy, angular and coupling-grid convergence.
Status: PARTIAL (B.1/B.2 energy convention and polarization state counting are resolved; the exact moving-muon mode-resolved rates are not yet connected to the radial transport kernel, and the profile remains reconstructed rather than raw Garching data).

### WP3 — Axial SN luminosity and boundaries
Acceptance:
- Scan 0.01–200 MeV and coupling with separate L,+,- and neutrino/muon contributions.
- Extract free-streaming and trapping boundaries with uncertainty bands from profile and transport variations.
- Reproduce vector control limits under the same numerical conventions before interpreting axial/vector differences.
- Preserve the unresolved Blinov 10 MeV discrepancy as a systematic until resolved.
Status: NOT STARTED (no new axial parameter scan has been launched).

### WP4 — Independent physical validation
Acceptance:
- Compare the low-mass longitudinal limit to the corrected Bollig/Caputo muonic-pseudoscalar calculation using identical coupling normalization and medium inputs.
- Compare neutrino-only sector to the flavour-matched vector L_mu-L_tau control.
- Check energy conservation/detailed balance and independent luminosity integration.
- Quantify uncertainty and show that conclusions are stable under accepted profile variants.
Status: PARTIAL (local kernels and limiting cases pass; full radial transport and luminosity-level independent validation remain open).

### WP5 — Manuscript and archive
Acceptance:
- Reproducible manuscript, figures, native CSV/JSON, plotting source, environment and hardware record, source/data hashes.
- Independent review of equations, units, references and figure provenance.
- PR review before merge to main.
Status: NOT STARTED.

## Non-goals for this first paper

- No full hydrodynamic supernova simulation.
- No broad survey of ordinary stars, white dwarfs, red giants or cosmology.
- No neutrino-mass/PMNS model extension.
- No claim that a short A' decay length alone eliminates neutrino-transport or energy-deposition effects.
- No use of the conditional old contour as a final exclusion.
- No change to the existing referee response or its SN paragraph unless a verified result requires it.

## Immediate next actions

1. Build exact moving-muon mode-resolved radial-energy tables for the three physical modes using the pinned reconstructed SFHo-18.8 profile.
2. Combine those rates with the already validated \\(\nu_\\mu,\\nu_\\tau\\) inverse-decay production and absorption kernels.
3. Feed each mode separately into the existing transport kernel, retaining the accepted B.1 local-source-energy and literal B.2 fixed-\\(\\omega\\) Euclidean-chord conventions.
4. Complete source-weighted radial/energy interpolation, quadrature and angular-escape convergence; retain the scalar B.2 reproduction lane separately from physical mode-resolved transport.
5. Only after WP2/WP4 pass, launch the 0.01--200 MeV axial parameter scan. Do not reuse the old stationary-muon fixed-profile contour as a final exclusion.
6. In parallel before manuscript drafting, complete the full-text novelty matrix for Gori et al. (arXiv:2506.11191) and Das et al. (arXiv:2606.23769).
