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

### Separate GR redshift-along-ray diagnostic

A second path calculation conserves E_inf = N(r_source)*omega_source and evaluates the local energy along the ray as omega(r') = E_inf/N(r'), including the corresponding local vector speed. Relative to the fixed-local-energy path used in the literal reference implementation, the luminosity changes are:

| Point | Fixed-local-energy result | Conserved-E_inf diagnostic | Change |
|---|---:|---:|---:|
| Weak coupling | 9.895e51 erg/s | 9.894e51 erg/s | -0.012% |
| Reference peak | 1.955e54 erg/s | 1.851e54 erg/s | -5.28% |
| High absorption | 2.437e52 erg/s | 1.724e52 erg/s | -29.26% |

Compared with the digitized Fig. 7 reference, the conserved-E_inf diagnostic has residuals of approximately -9.17%, -3.12%, and +35.9%, respectively. It moves the high-coupling tail toward the published curve, but does not reproduce it.

This is recorded as a **separate GR-consistency diagnostic**, not as a correction to the literal Blinov reproduction. The printed Eq. (B2) writes the opacity as Gamma_abs^*(r'(s), omega) without displaying an explicit N(r_source)/N(r') argument. The precise energy convention intended inside that local rate along the ray must be resolved from the authors' convention/implementation before changing the reference lane. No redshift-aware result is silently substituted for the literal equation as printed.

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
