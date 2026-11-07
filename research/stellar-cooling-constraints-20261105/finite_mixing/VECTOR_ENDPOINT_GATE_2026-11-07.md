# Pure-vector endpoint validation gate

**Decision: BLOCKED (2026-11-07).** Do not accept a finite-mixing stellar-cooling curve until the pure-vector endpoint is reconciled with the published Blinov et al. result.

## Reference

Use the published version of record: N. Blinov et al., *L_mu-L_tau gauge bosons in beam dumps and supernovae*, JHEP 2026, 155, DOI [10.1007/JHEP06(2026)155](https://doi.org/10.1007/JHEP06(2026)155), arXiv:2511.09619.

The published paper defines the ballistic luminosity and angular optical-depth prescription in Appendix B, Eqs. (B.1)--(B.5), and the neutrino, dimuon, and semi-Compton rates in Eqs. (B.6)--(B.19). Its Fig. 7 shows the full luminosity-versus-coupling curves at 1 s post-bounce; Fig. 4 gives the cooling contour. The published PDF is the primary figure source for the next digitization pass.

## Existing evidence on the PR #56 branch

| Test | Existing result | Assessment |
|---|---:|---|
| Independent scalar Appendix-B path: Fig. 4 boundaries at 1, 10, 100, 200 MeV | maximum boundary difference 2.60% | Partial pass only |
| Independent scalar path: Fig. 7, 1 MeV | 5.54% max / 1.60% mean | Within provisional target |
| Independent scalar path: Fig. 7, 10 MeV | 91.35% max / 15.64% mean | Fail |
| Independent scalar path: Fig. 7, 200 MeV | 1.59% max / 0.71% mean | Within provisional target |
| Existing mode-resolved vector scan: mass endpoint | 259.08--259.14 MeV | Fail against archived Fig. 4 endpoint near 210.98 MeV |
| Literal scalar Appendix-B scan: mass endpoint | 214.06--214.14 MeV | Close to archived Fig. 4 endpoint, but does not pass the 10 MeV Fig. 7 test |

The scalar and mode-resolved scans are not a one-factor comparison: they change both the semi-Compton prescription and the polarization/opacity treatment. The mismatch cannot be assigned to a single factor of three, recoil correction, or profile effect without a controlled comparison.

The existing coupling-axis rescaling audit is diagnostic only. Its mass-specific 10 MeV fit improves Fig. 7 but worsens the already-close Fig. 4 boundary; the global fit does not reconcile all masses. No fitted kappa is applied to production scans or constraint curves.

## Required sequence

1. **Published-source digitization.** Extract Fig. 4 and Fig. 7 from the published version-of-record PDF, not only the arXiv source-archive PDF. Record PDF SHA-256, drawing/path identifiers, axis calibration, vertices, and digitization uncertainty.
2. **Matched local rates.** Compare neutrino inverse decay, dimuon inverse decay, and semi-Compton production/absorption separately at fixed (r, omega, m_V), with identical profile values and coupling conventions. Record the exact approximation used for each channel.
3. **Opacity convention.** Reconcile the scalar Gamma_abs used in Eq. (B.2) with the polarization-summed production rates in Eqs. (B.6) and (B.13). Compare scalar-summed, polarization-averaged, and mode-resolved transport without silently inserting a factor of three. Preserve mode-by-mode detailed balance in the physical solver.
4. **Full Fig. 7 comparison.** Compare luminosity at every digitized coupling, not only the contour crossing. Vary one ingredient at a time; do not fit a correction to the target curve.
5. **Contour and endpoint comparison.** Compare both Fig. 4 boundaries over the available mass points and the maximum-mass closure.
6. **Convergence and provenance.** Increase radial, energy, angular, and path quadrature independently; archive the exact profile and input hashes.

## Provisional numerical acceptance targets

These are engineering acceptance targets for the reproduction check, not claims about the astrophysical systematic uncertainty:

- Fig. 4 lower and upper boundaries: relative deviation no larger than 3% at the four representative masses (1, 10, 100, 200 MeV).
- Fig. 7 full luminosity curves: mean absolute relative deviation no larger than 5% and maximum no larger than 10% at each digitized mass, including the 10 MeV trapping tail.
- Maximum-mass closure: agree within the digitization resolution of the published contour.
- All per-channel detailed-balance tests pass; all reported results are reproducible from archived inputs and code.

If the original stellar profile is unavailable, the result must be labelled a reconstructed-profile comparison. It must not be described as an exact reproduction of the authors' original numerical calculation.

## Disposition

No mixed-current scan starts until the published-source vector endpoint passes this gate. No rescale factor, opacity multiplier, or post-hoc contour adjustment is allowed. PR #56 remains Open / Draft.


## Published version-of-record visual cross-check (2026-11-07)

The published JHEP PDF and arXiv v2 PDF have now been compared visually:

- Published-version Fig. 4 (PDF p. 16) and arXiv v2 Fig. 4 (PDF p. 17) show the same plotted cooling contour, shaded regions, axes, and line styles.
- Published-version Fig. 7 (PDF p. 24) and arXiv v2 Fig. 7 (PDF p. 26) show the same six luminosity curves, axes, and legend.

No visible figure revision is found. This is a visual cross-check only: the archived numerical vertices remain those extracted from the arXiv source PDF, and exact path-level re-digitization from the version-of-record PDF is still pending. The 10 MeV residual therefore remains a genuine unresolved numerical mismatch, not something explained away by a visibly revised figure.

Two statements in the published paper are relevant to interpreting that mismatch:

1. The text below Fig. 7 states that above the MeV scale, neutrino decay dominates trapping, while Compton absorption is mainly relevant at lower masses.
2. Appendix B below Eq. (B.14) says the nonrelativistic-muon/no-recoil semi-Compton approximation is typically relevant for \(m_V\lesssim\mathrm{MeV}\).

Our 10 MeV audit finds a source-weighted opacity split of about 89.8% neutrino inverse decay and 10.2% inverse Compton. A 10% opacity component can still have a large effect after exponentiation in the strong-trapping tail. This does not justify changing its normalization; it identifies the 10 MeV Compton approximation/profile input as a targeted controlled-comparison priority.

The paper's Section 4.5 also explicitly notes order-one differences from earlier literature due to its updated treatment and says previous results are recovered when their methods are replicated. Therefore the acceptance target here is the Blinov version-of-record result itself, not an unspecified older vector curve.


## One-factor muon-chemical-potential profile sensitivity (2026-11-07)

A controlled diagnostic changes only \(\mu_\mu(r)\), replacing the baseline Caputo digitization with the separate Ferreira digitization while keeping \(T(r)\), \(\mu_{\nu_\mu}(r)\), lapse, rates, transport, mass, and coupling grid fixed. The full output is archived at [muon_profile_sensitivity_10mev.json](../blinov_reproduction/outputs/muon_profile_sensitivity_10mev.json).

| Metric, 10 MeV | Baseline Caputo \(\mu_\mu\) | Ferreira \(\mu_\mu\) only |
|---|---:|---:|
| Mean absolute relative Fig. 7 residual | 15.73% | 42.13% |
| Maximum absolute relative Fig. 7 residual | 92.24% | 65.04% |
| \(4.4\times10^{52}\) lower crossing \(g_X\) | \(1.014\times10^{-9}\) | \(8.055\times10^{-10}\) |
| \(4.4\times10^{52}\) upper crossing \(g_X\) | \(3.862\times10^{-8}\) | \(3.807\times10^{-8}\) |

The alternative curve improves the far-trapping tail but worsens the weak-coupling and peak regions and substantially worsens the full-curve residual. It does not solve the 10 MeV mismatch and is not adopted. The baseline Caputo central \(\mu_\mu\) is independently consistent with the digitized muon number density: the Fermi integral gives \(9.581\times10^{-5}\,\mathrm{fm}^{-3}\), compared with the plotted \(9.628\times10^{-5}\,\mathrm{fm}^{-3}\) (about 0.5%). Adding \(m_\mu\) to this chemical potential would overpredict the central density by about a factor of 88 and is therefore incorrect under this profile convention.

The exact s18.8-SFHo-MUONS source profile is not available in the public material currently accessible to this audit: the Garching archive entry for the radial profiles returns HTTP 401, and the published paper's data-availability statement does not provide associated simulation data/code. Consequently, a full point-by-point Fig. 7 reproduction cannot be claimed from the reconstructed profile alone. The Fig. 4 contour-level agreement remains a useful independent cross-check, but it is not equivalent to reproducing the full luminosity curve.

**Disposition:** retain the Caputo profile as the better independently density-anchored reconstruction; retain Ferreira only as a systematic diagnostic. The 10 MeV full-curve gate remains blocked.

## Published-version equation-level audit (2026-11-07)

The Springer version-of-record PDF was opened and checked directly (JHEP06(2026)155, published 15 June 2026; DOI 10.1007/JHEP06(2026)155). The relevant source locations are Appendix B, pp. 20--23, Eqs. (B.1)--(B.19), and Fig. 7 on p. 24.

This confirms the following details that the vector gate must reproduce:

1. **Ballistic luminosity and opacity:** Eq. (B.1) integrates the production rate over the local phase space with the lapse/redshift factors and escape-energy threshold. Eq. (B.2) direction-averages the survival probability over the full emission angle; Eq. (B.4) defines the reduced absorption rate as \((1-e^{-\omega/T})\Gamma_{\rm abs}\); Eq. (B.5) includes \(v_V=\sqrt{1-m_V^2/\omega^2}\) in the optical depth.
2. **Neutrino inverse decay:** Eq. (B.6) explicitly sums over the three initial vector polarizations. Eq. (B.7) therefore contains an explicit factor of 3 because the vacuum width in Eq. (B.8) is averaged over initial vector polarizations. Eq. (B.10) imposes detailed balance. The two active flavors are evaluated separately, with \(\mu_{\nu_\tau}=0\) in their profiles.
3. **Dimuon inverse decay:** Eqs. (B.11)--(B.12) use the total spin-averaged vacuum width to both muon chiralities and the corresponding threshold factor.
4. **Semi-Compton:** Eq. (B.13) sums over all external polarizations in the thermal rate. Eqs. (B.14)--(B.18) use the nonrelativistic-muon/no-recoil approximation, include the massive-vector phase-space velocity factors and the two photon spin states, and define the degeneracy factor \(F_{\rm deg}\). Eq. (B.19) fixes absorption by detailed balance.
5. **Full-curve criterion:** Fig. 7 is the luminosity versus \(\alpha_V\) at fixed masses, not merely the cooling-boundary crossing. The text below Fig. 7 states that neutrino inverse decay dominates trapping above the MeV scale, while semi-Compton absorption is mainly relevant at lower masses.

### Required two-lane validation (do not conflate the lanes)

The published calculation is written in polarization-summed rates and a scalar escape probability. The physical mixed-current extension, by contrast, must preserve mode-resolved production and absorption and propagate each mode with its own opacity. These are distinct implementations unless one proves their equivalence for the observable under the adopted approximations.

Accordingly, the vector gate now has two separate requirements:

- **Lane A — literal paper reproduction:** implement the published Appendix-B summed-rate prescription literally, with the same reconstructed profile and the exact published equations, and reproduce the full Fig. 7 luminosity curves plus Fig. 4 boundaries. This is the external benchmark and must pass the numerical tolerances above. No fitted coupling rescale is allowed.
- **Lane B — mode-resolved physical transport:** independently verify the per-polarization rates, vacuum widths, detailed balance, and escaped luminosity. Explain quantitatively any difference from Lane A. A Lane-B result is not required to equal a polarization-summed Lane-A result by assumption; any equivalence or discrepancy must be derived.

Only after Lane A reproduces the published pure-vector result and Lane B has a documented, physically consistent transport prescription may the finite-mixing UV benchmark curve be promoted as a validated result. For the mixed case, the same prescription must be used consistently in all three endpoints (pure vector, pure axial, and \(\theta_{\mu R}=10^{-2}\)); the vector endpoint must reduce to the published Lane-A benchmark in the literal-reproduction implementation.

**Current disposition remains BLOCKED.** This source audit does not resolve the 10 MeV Fig. 7 mismatch, does not validate the 259 MeV mode-resolved endpoint, and does not authorize a mixed-current luminosity scan or exclusion curve.

## Priority reset: microscopic forward/reverse rates first (2026-11-07)

The 10 MeV three-layer diagnostic reports a source-weighted mean reduced-opacity split of 89.78% neutrino inverse decay and 10.22% inverse Compton. This is specific to the 10 MeV benchmark and its source weighting; it is not assumed to hold at other masses or for every local ray.

The immediate P0 work is therefore:

1. **Neutrino inverse decay:** independently integrate production \(f_1f_2\) and absorption \((1-f_1)(1-f_2)\), using adaptive quadrature separate from the production solver's Gauss--Legendre implementation. Resolve \(\nu_\mu\), \(\nu_\tau\), and each polarization. Compare both rates and verify \(\Gamma_{h,\rm abs}/\Gamma_{h,\rm prod}=e^{\omega/T}\).
2. **Semi-Compton:** independently integrate forward \(f_\gamma\) and inverse \(1+f_\gamma\) factors in the B.14--B.19 no-recoil approximation, and compare the summed normalization with B.14/B.16. Keep this audit distinct from the full moving-muon B.13 thermal integral. The existing exact-recoil fixed-target collision-integrand test remains a separate pointwise B.19 check.
3. **P1 local diagnostics:** after both rate audits pass, compare channel-resolved local rates and optical depths at three representative \((r,\omega,m_V)\) points; inspect their radial and energy support.
4. **P1 transport:** compare the direction-averaged escape probability and the full Fig. 7 high-coupling tail, without reducing the average of exponentials to the exponential of an average optical depth.
5. **P2 current switch:** only after the pure-vector full-curve benchmark passes, run the pure-axial and finite-mixing cases with the same validated transport prescription.

The adaptive reference and acceptance criteria are recorded in [DIRECT_COLLISION_INTEGRAL_AUDIT_2026-11-07.md](../DIRECT_COLLISION_INTEGRAL_AUDIT_2026-11-07.md). The new tests and workflow are internal validation assets; they do not authorize any production-rate rescaling or mixed-current scan. In particular, the existing neutrino code already evaluates both Fermi products and Pauli-blocking factors separately; the independent adaptive calculation is intended to test that implementation, not to imply that its absorption rate was previously inferred from its production rate.

**Gate remains BLOCKED** until the published pure-vector full Fig. 7 comparison passes. A successful local detailed-balance test is necessary, but not sufficient, for the literature benchmark.

