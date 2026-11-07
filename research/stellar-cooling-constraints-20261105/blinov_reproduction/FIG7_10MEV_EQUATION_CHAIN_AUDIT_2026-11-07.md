# 10 MeV Fig. 7 equation-chain audit (2026-11-07)

## Scope

This audit targets the large high-coupling residual in the literal pure-vector comparison to Blinov et al., arXiv:2511.09619v2, Fig. 7. It checks the local semi-Compton kernel and degeneracy factor (Eqs. 31–33 in the current arXiv v2 numbering), reduced absorption (Eq. 20), chord optical depth (Eq. 18), and luminosity measure/redshift/radius treatment (Eq. 17).

The audit does not alter reference.py, does not apply a fitted normalization, does not replace the literal Blinov prescription, and does not change the axial scan, manuscript, or referee response.

Reproduce from the repository root:

~~~bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/diagnose_fig7_10mev_equation_chain.py
~~~

The machine-readable output is outputs/fig7_10mev_equation_chain_audit.json.

## Results

### Eqs. (31)–(33): semi-Compton kernel and muon degeneracy

- Reconstructing the implemented Eq. (31)–(32) semi-Compton coefficient from its displayed factors agrees with reference.py at zero floating-point residual on the sampled array.
- The optically thin source at 10 MeV is 67.95% neutrino coalescence and 32.05% semi-Compton; dimuon production is kinematically closed.
- The Eq. (33) degeneracy factor is independently checked through the thermodynamic identity T dn_mu/dmu_mu = n_mu F_deg, using a centered finite difference of the density integral at seven radii. The maximum relative residual is 1.61e-8.

This verifies the numerical implementation of the stated degeneracy integral. It does not independently validate the physical accuracy of the nonrelativistic/no-recoil semi-Compton approximation or the reconstructed stellar profile.

### Neutrino inverse decay: Eqs. (B6)–(B10)

Because neutrino coalescence dominates the 10 MeV opacity, the Fermi-pair kernel is also checked independently. At six radii, four energies, and both the \(\\nu_\\mu\) and \(\\nu_\\tau\) flavours (48 points), the analytic production kernel agrees with direct angular integration to a maximum relative residual of \(6.41\\times10^{-14}\). The independently integrated inverse process satisfies Eq. (B10), \(\\Gamma_{\\rm prod}=e^{-\\omega/T}\\Gamma_{\\rm abs}\), with maximum relative residual \(1.0\\times10^{-15}\).

The high-absorption point is neutrino-opacity dominated: the source-weighted mean optical depth at 25 km is 14.48 from inverse neutrino decay and 1.65 from semi-Compton absorption. The extra 24–25 km shell contributes \(\\Delta\\tau\\simeq0.928\), of which 0.928 is neutrino opacity and only \(3.72\\times10^{-4}\) is semi-Compton opacity. Thus the large high-coupling residual cannot be attributed primarily to the Compton opacity normalization.

### Eq. (20): reduced absorption

The stable evaluation

~~~text
(1-exp(-omega/T))*Gamma_abs
~~~

agrees with

~~~text
(exp(omega/T)-1)*Gamma_prod
~~~

to a maximum relative residual of 3.13e-16. This is an algebraic/detailed-balance consistency check using the same local production and absorption pair, not an independent inverse-process matrix-element calculation.

### Eq. (18): chord integration and angular average

At 88 radial, 180 energy, 24 angular, and 64 path quadrature orders, doubling the path and angular orders changes the luminosity by at most 4.2e-6 and 3.7e-5, respectively, at the weak-coupling, reference-peak, and high-absorption points. The corresponding maximum relative changes in the angle/path columns are about 1.6e-3 and 1.7e-3.

Thus the 10 MeV high-coupling tail is not explained by insufficient path- or angular-quadrature order in this setup.

### Eq. (17): phase-space measure, lapse and outer boundary

The energy-variable Jacobian is checked independently:

~~~text
k^2 dk * omega = k omega^2 d omega
~~~

with maximum relative residual 2.70e-16. The N(r)^2 factor is retained. Removing it is only a diagnostic and is not an allowed alternative to the luminosity-at-infinity prescription.

The 24–25 km shell is important for trapped particles. Holding the same source nodes and local source rates fixed, removing only the 24–25 km propagation segment increases the high-absorption luminosity by about 40.0%; the source-weighted mean additional optical depth from that shell is about 0.928 at the high-coupling point. At the peak the corresponding luminosity change is about 5.2%, while it is negligible in the optically thin limit.

**The 24 km result is not adopted.** Blinov Appendix B explicitly identifies R_max with the neutrinosphere radius R_nu ≈ 25 km (Eq. B3 discussion). The literal benchmark therefore keeps 25 km. The 24–25 km result documents sensitivity to the outermost reconstructed shell; it does not justify moving the physical boundary.

### Sensitivity to the reconstructed temperature profile

A uniform temperature rescaling is used only as a sensitivity diagnostic, with production and absorption recomputed together (not as a fitted correction). At the high-absorption point, changing the entire reconstructed T(r) profile by -5% moves the Fig. 7 residual from +92.2% to +30.7%; changing it by +5% moves the residual to +174.6%. The weak-coupling residual moves from -9.2% to -26.2% and +11.2%, respectively, while the peak moves from +2.3% to -19.8% and +29.2%.

This large response means the 10 MeV comparison is sensitive to the reconstructed thermal background. A uniform rescaling is not a physical uncertainty model and neither value is adopted. As a cross-check, the separately digitized Caputo and Ferreira temperature profiles agree to within 0.18% at sampled radii from 1 to 24 km, so the ±5% rescaling is deliberately a stress test, not an uncertainty inferred from those two sources. The mismatch cannot be resolved by choosing a temperature normalization to fit Fig. 7; the original simulation profile or a defensible profile uncertainty estimate would be needed to quantify this source of uncertainty.

### Separate GR redshift-along-ray diagnostic

A second path calculation conserves E_inf = N(r_source)*omega_source and evaluates the local energy along the ray as omega(r') = E_inf/N(r'), including the corresponding local vector speed. Relative to the fixed-local-energy path used in the literal reference implementation, the luminosity changes are:

| Point | Fixed-local-energy result | Conserved-E_inf diagnostic | Change |
|---|---:|---:|---:|
| Weak coupling | 9.895e51 erg/s | 9.894e51 erg/s | -0.012% |
| Reference peak | 1.955e54 erg/s | 1.851e54 erg/s | -5.28% |
| High absorption | 2.437e52 erg/s | 1.724e52 erg/s | -29.26% |

Compared with the digitized Fig. 7 reference, the conserved-E_inf diagnostic has residuals of approximately -9.17%, -3.12%, and +35.9%, respectively. It moves the high-coupling tail toward the published curve, but does not reproduce it.

This is recorded as a **separate alternative transport diagnostic**, not as a correction to the literal Blinov reproduction. Direct inspection of the published v2 Appendix B, Eq. (18), confirms that the printed opacity integrand is explicitly Gamma_abs^*(r'(s), omega), with the same omega carried along the chord; no N(r_source)/N(r') transformation appears in Eq. (18). The present reference.py therefore follows the literal printed Eq. (18) in holding the omega grid index fixed along the path. Eq. (17) separately includes N(r)^2 and the lower limit m_V/N(r), and the paper describes these as the luminosity redshift/time-dilation and escape-threshold effects. The conserved-E_inf calculation is a useful alternative physical prescription to compare, but it is **not** the literal Eq. (18) benchmark and must not be used to claim a correction to the authors' published result. The printed equation settles the implementation choice for a literal reproduction; it does not provide an independent derivation of the underlying GR transport convention.

### Fig. 7 digitization provenance check

The 10 MeV reference curve is extracted from the original arXiv v2 source archive member `luminosity_snapshot_t=1.pdf`, using the PDF vector drawing path rather than screenshot pixels. The archived audit identifies drawing index 43, 27 path segments, 28 raw vertices, and 25 vertices inside the plotting frame. It verifies the violet curve/legend assignment, axis calibration, and round-trip transformations from PDF coordinates to \\(\\alpha_V=g_{\\mu\\tau}^2/(4\\pi)\\) and luminosity. The x/y major-tick spacing residuals are \\(1.14\\times10^{-5}\\) and \\(5.09\\times10^{-6}\\) PDF points. The source PDF SHA-256 is `4d7d1d10bfe2b52992af94df98749fa3adac887c009cbf98515fa12e6c48fdb5`; the same source PDF is used in the comparison and was visually cross-checked against the version-of-record figure.

This rules out ordinary screenshot-based digitization error as an explanation for the 10 MeV tail mismatch. It does not recover author-side numerical samples or the authors' interpolation between plotted vertices. Full provenance is archived in `outputs/fig7_digitization_audit_2026-11-07.json` and `outputs/fig7_source_drawings_2026-11-07.json`.

### Existing source/opacity sensitivity results

The archived three-layer decomposition gives a weak-coupling residual of \\(-8.89\\%\\), a peak residual of \\(+2.57\\%\\), and a high-absorption residual of \\(+92.24\\%\\). At the high-absorption point, the source-weighted mean optical depths are 14.487 from neutrino inverse decay and 1.649 from semi-Compton absorption. The independent \\(\\mu_{\\nu_\\mu}\\) scaling scan from 0 to 1.5 changes the high-tail residual only from +92.14% to +92.35%; thus that particular chemical-potential profile is not the driver of the high-tail discrepancy in this test.

The one-factor opacity stress test shows that changing the neutrino opacity has a much larger effect on the high-coupling tail than changing the semi-Compton opacity. These are diagnostic sensitivities only; neither a rescaled opacity nor a fitted profile is adopted. The channel split itself passes internal sum checks at relative residuals below \\(7\\times10^{-16}\\), but the three-layer audit explicitly reuses the reference detailed-balance prescription and is not an independent microscopic derivation of the inverse rates.

## Current 10 MeV residuals

For the literal fixed-local-energy implementation and the digitized 25-point Fig. 7 curve:

| Point | Calculated / reference | Relative residual |
|---|---:|---:|
| Weak coupling | 0.9084 | -9.16% |
| Reference peak | 1.0229 | +2.29% |
| High absorption | 1.9222 | +92.22% |

The local algebraic checks and quadrature checks pass, but the full Fig. 7 curve does not. The source mismatch at weak coupling and the trapping mismatch at high coupling remain distinct problems.

## Decision

1. Do not insert a factor of two in Compton opacity. The earlier opacity-only factor-two test broke the matched production/absorption relation and is not a physical correction.
2. Keep R_max=25 km for the literal Blinov benchmark.
3. Keep the fixed-local-energy calculation as the literal reference lane until the paper's path-energy convention is unambiguously resolved.
4. Investigate the 10 MeV source/profile normalization and the high-coupling transport convention separately.
5. Do not promote the vector benchmark to passed, and do not use it to validate the axial cooling curve yet.

No production rate, transport routine, axial result, manuscript, or referee-response file is modified by this audit.
