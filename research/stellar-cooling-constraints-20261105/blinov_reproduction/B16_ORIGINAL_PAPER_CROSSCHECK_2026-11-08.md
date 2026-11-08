# B.16 original-paper cross-check: equations, transport convention, and profile provenance

**Date:** 2026-11-08  
**Status:** equation/transport cross-check completed; original raw-background identity remains unverified.  
**Benchmark:** \(m_V=10\) MeV, pure-vector \(L_\mu-L_\tau\), \(s18.8\)-SFHo-MUONS at \(t_{\rm pb}=1\) s.  
**Decision:** do not update or reinterpret the axial-vector curve.

## 1. Primary source and equation numbering

The primary source is Blinov, Fox, Kelly, Plestid and Zhou, *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, arXiv:2511.09619v2 (15 May 2026), Appendix B, especially pp. 21--25 of the PDF.

The correct Appendix-B mapping is:

| Blinov equation | Role in the calculation | Current reproduction |
|---|---|---|
| (B.1) | Ballistic luminosity/source integral; includes \(N(r)^2\), \(k=\sqrt{\omega^2-m_V^2}\), and \(\omega_{\min}=m_V/N(r)\) | Implemented by eq_b1_source_measure; source measure contains lapse squared and the local escape threshold |
| (B.2) | Direction-averaged escape probability with the path optical depth | Implemented with the full angular average and path integral |
| (B.3) | Chord distance \(s_{\max}(r,\cos\theta)\) to \(R_{\max}\) | Implemented and geometrically tested |
| (B.4) | Reduced absorption \(\Gamma^*_{\rm abs}=(1-e^{-\omega/T})\Gamma_{\rm abs}\) | Both equivalent reduced-rate forms checked |
| (B.5) | Vector speed \(v_V=\sqrt{1-m_V^2/\omega^2}\) | The \(1/v_V\) factor is retained in the optical depth |
| (B.6) | Neutrino inverse-decay production phase-space integral | Independently integrated over the two-body angular variable |
| (B.7)--(B.9) | Analytic neutrino production rate, vacuum width, and Fermi integral \(I\) | Direct phase-space integration agrees with the analytic result |
| (B.10) | Neutrino inverse-decay detailed balance, \(\Gamma_{\rm prod}=e^{-\omega/T}\Gamma_{\rm abs}\) | Independently checked against the inverse occupation-factor integral |
| (B.11)--(B.12) | Inverse muon decay and \(V\to\mu^+\mu^-\) width | Not open for \(m_V=10\) MeV |
| (B.13)--(B.18) | Compton production, approximate cross section, thermal factors, and forward/reverse cross-section relation | Separate Compton audit |
| (B.19) | Compton absorption detailed balance | Separate Compton occupation-factor audit |

**Important correction to the proposed equation grouping:** B.19 is the Compton absorption relation, not the neutrino inverse-decay relation. The neutrino inverse-decay chain is B.6 (production phase space), B.10 (detailed balance), and B.4 (reduced absorption). B.19 is retained as a separate Compton check and must not be used as the neutrino inverse-decay citation.

The Compton audit is independent of reference.py: it constructs the tree-level QED × vector-current amplitude, checks the B.18 phase-space/spin relation, the B.15/B.16 kinematic coefficient, and the B.19 occupation-factor detailed-balance identity. Its scope is an exact two-body vacuum/stationary-muon diagnostic; it does not replace the thermal supernova Compton rate.

## 2. Transport convention: fixed \(\omega\) along the B.2 path

The published B.2 integrand is
\[
\tau(r,\omega,\cos\theta)
=\int_0^{s_{\max}} ds\,
\frac{\Gamma^*_{\rm abs}(r'(s),\omega)}{v_V(\omega)},
\qquad
r'(s)=\sqrt{r^2+s^2+2rs\cos\theta}.
\]

The energy argument shown in B.2 is the same \(\omega\) along the path. The local temperature and chemical potentials are evaluated at \(r'(s)\), but the published B.2 expression does not replace \(\omega\) by a lapse-redshifted local energy at each path point.

The gravitational factors enter B.1 through \(N(r)^2\) and the emission-radius lower bound \(\omega_{\min}=m_V/N(r)\). They are not an extra lapse factor in the fixed-\(\omega\) B.2 path integral.

Accordingly:
- the fixed-\(\omega\) prescription is the reproduction baseline;
- the path-redshift calculation is a separately labelled sensitivity diagnostic;
- the path-redshift diagnostic changes the local energy argument and local vector speed but keeps the Euclidean chord measure, so it is not a complete GR ray-tracing calculation;
- neither prescription is selected by fitting Fig. 7.

Blinov et al. explicitly state \(R_{\max}=R_\nu\simeq25\) km, motivate the full angular average, retain \(1/v_V\), and explain the reduced absorption factor as the effect of stimulated emission. The current fixed-\(\omega\) code follows these conventions.

## 3. Neutrino flavor and detailed balance

Blinov et al. state that the \(\nu_\mu\) and \(\nu_\tau\) chemical potentials can differ. The simulations do not provide \(\mu_{\nu_\tau}\), so they set \(\mu_{\nu_\tau}=0\). The current implementation uses the \(\nu_\mu\) chemical potential from the reconstructed profile and retains the zero-chemical-potential \(\nu_\tau\) channel.

The independent B.6/B.10/B.4 audit gives:

| Check | Maximum residual |
|---|---:|
| Direct B.6 angular integral vs analytic \(\nu_\mu\) integral | \(4.41\times10^{-14}\) |
| Direct B.6 angular integral vs analytic \(\nu_\tau\) integral | \(5.12\times10^{-14}\) |
| Direct B.6 flavor sum vs reference production kernel | \(4.76\times10^{-14}\) |
| B.10 detailed balance, \(\nu_\mu\) | \(3.55\times10^{-15}\) in log residual |
| B.10 detailed balance, \(\nu_\tau\) | \(3.55\times10^{-15}\) in log residual |
| B.10 absorption vs direct inverse phase-space integral | \(1.82\times10^{-15}\) |
| B.4 equivalent reduced-absorption forms | \(1.82\times10^{-15}\) |
| B.4 reduced neutrino rate vs reference kernel | \(4.77\times10^{-14}\) |

At sampled radii 22--25 km, where the reconstructed \(\mu_{\nu_\mu}=0\), the thermal neutrino inverse-decay absorption remains finite and agrees with the independent B.6/B.10/B.4 calculation. Zero chemical potential does not mean zero neutrino opacity.

## 4. Background provenance: what is and is not established

Blinov et al. identify the numerical benchmark as \(s18.8\)-SFHo-MUONS at 1 s post-bounce, generated with PROMETHEUS-VERTEX. The current public reconstruction uses:
- Caputo, Raffelt and Vitagliano, arXiv:2109.03244v3, Fig. 1, for \(T\), \(\mu_\mu\), and the plotted \(\mu_{\nu_\mu}\) branches;
- Ferreira, Marsh and Ravensburg, arXiv:2510.14469v1, Fig. 1, for the lapse curve;
- a matched Schwarzschild continuation from the last digitized lapse point near 24 km to 25 km.

The public Garching archive lists radial neutrino-moment and hydrodynamic profile collections associated with the Bollig/Hüdepohl PROMETHEUS-VERTEX simulations. The linked protected directories return HTTP 401 without authorization. The archive listing is a provenance lead, not proof that the exact \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1.000\) s snapshot is available in the linked collection. No protected raw file has been accessed.

The reconstructed profile has 0.05 km radial sampling, but some values beyond the visible plotting range are recovered from off-frame vector vertices in the public PDF. The lapse curve is visible only to approximately 24 km and is continued to 25 km. These choices are documented in data/profile_provenance.json.

A second warning concerns the plotted muon chemical potential. The Caputo and Ferreira figure reconstructions, despite carrying the same SFHo-18.8 model label, yield materially different \(\mu_\mu(r)\) curves in the core. The baseline retains Caputo's curve because its Fermi-integrated negative-muon density agrees with the independently plotted Caputo muon-density curve at the checked radii. Ferreira's \(\mu_\mu\) curve is retained as a diagnostic and is not silently mixed into the baseline. This figure-to-figure difference is unresolved at the raw-simulation level and must not be presented as a verified physical difference between two identical snapshots.

Consequently, the equation-level and transport-convention comparison is strong, but the background is not yet an exact raw-data reproduction of the authors' numerical input.

## 5. What the completed P1--P3 checks establish

1. **Outer profile/interpolation:** the 22--25 km temperature interpolation error is at most 0.122%, lapse error 0.0040%, and the large relative \(\mu_\mu\) interpolation error occurs where the muon density is negligible. Evaluating local neutrino opacity on the original 0.05 km nodes changes the 8--15 km source-weighted 22--25 km optical depth by \(1.23\times10^{-5}\); the strong-end outer-shell escape factor changes by \(7.18\times10^{-6}\).
2. **Lapse continuation:** freezing \(N(24\,{\rm km})\) changes the total B.1 source by only \(-1.16\times10^{-6}\); linear extrapolation changes it by \(+7.40\times10^{-8}\). The corresponding strong-end escape-factor changes are \(-2.45\times10^{-4}\) and \(+1.80\times10^{-5}\).
3. **Directional escape:** the 8--15 km region supplies 79.61% of the B.1 source. At the strong endpoint, source-weighted mean optical depths for this emission region are \(7.5711\times10^{15}g^2\) from the inner path and \(1.5634\times10^{15}g^2\) from the 22--25 km shell. Escaping directions are strongly biased outward: 75.82% of the selected region's escaping luminosity lies in \(0.5\leq\cos\theta\leq1\).

These results show that the outer shell matters, but neither the outer interpolation nor the tested lapse continuation explains the high-coupling Fig. 7 discrepancy. The inner path contributes more to the mean optical depth for the dominant emission region.

## 6. Source-versus-escape residual

At the weak endpoint, the escape probability required to match Fig. 7 while holding the current B.1 source fixed is greater than one. This cannot be repaired by changing an absorption rate; the source/profile normalization must be checked.

At the Fig. 7 peak, the required and calculated escape probabilities differ by approximately 2.5%.

At the strong endpoint:
\[
P_{\rm esc}^{\rm calc}=3.2392\times10^{-4},\qquad
P_{\rm esc}^{\rm req}=1.6850\times10^{-4}.
\]
The required-to-calculated ratio is 0.5202, or an effective escape-exponent difference of 0.6536. This is an averaged quantity, not a uniform additive shift to each ray's optical depth.

The tested quadrature, outer interpolation, lapse continuation, and inverse-decay algebra errors are all much smaller than the remaining strong-end discrepancy.

## 7. Status and next gate

- P1: outer inputs/interpolation checked on the reconstructed profile; no numerically significant interpolation error found.
- P2: neutrino inverse-decay phase space, B.10 detailed balance, and B.4 reduced absorption independently checked; no algebraic mismatch found. B.19 is correctly reserved for Compton.
- P3: direction-resolved optical depth and escape for 8--15 km sources checked.
- P4: published equations, fixed-\(\omega\) convention, angular geometry, \(R_{\max}\), flavor assumptions, and Fig. 7 digitization have been cross-checked. Exact raw-background identity remains unverified.
- P5: blocked. Do not recalculate or publish a new axial-vector constraint curve until the pure-vector benchmark has passed a source/profile-level reproduction gate.

No rate rescaling, fitted opacity correction, altered \(R_{\max}\), or production axial-output change is authorized by these checks.

## 8. Reproducibility pointers

- audit_b16_outer_profile_inputs.py
- audit_b16_outer_profile_interpolation.py
- audit_b16_lapse_boundary_sensitivity.py
- audit_b16_neutrino_inverse_decay.py
- audit_b16_directional_escape_8_15.py
- audit_b16_quadrature_convergence.py
- audit_b16_emission_radius_escape.py
- outputs/b16_outer_profile_inputs_10mev_2026-11-08.json
- outputs/b16_outer_profile_interpolation_10mev_2026-11-08.json
- outputs/b16_lapse_boundary_sensitivity_10mev_2026-11-08.json
- outputs/b16_neutrino_inverse_decay_10mev_2026-11-08.json
- outputs/b16_directional_escape_8_15km_10mev_2026-11-08.json
- outputs/b16_quadrature_convergence_10mev_2026-11-08.json
- outputs/b16_emission_radius_escape_10mev_2026-11-08.json

Primary literature:
- Blinov et al., https://arxiv.org/abs/2511.09619
- Caputo, Raffelt and Vitagliano, https://arxiv.org/abs/2109.03244
- Ferreira, Marsh and Ravensburg, https://arxiv.org/abs/2510.14469


### 4.1 Version-of-record and data-availability cross-check

The comparison above has now also been checked against the publisher's version of record, Blinov et al., JHEP 06 (2026) 155, DOI 10.1007/JHEP06(2026)155, published 15 June 2026. The relevant source is the publisher PDF, Appendix B (pp. 20--23), rather than an equation transcription from a secondary paper.

The publisher text confirms the following points directly:

- B.1 contains \(N(r)^2\) and the emission-point threshold \(\omega_{\min}=m_V/N(r)\).
- B.2 uses the full \(-1\leq\cos\theta\leq1\) angular average, the chord endpoint B.3, the local thermodynamic inputs at \(r'(s)\), and a fixed displayed energy argument \(\omega\) inside \(\Gamma_{\rm abs}^{*}(r'(s),\omega)\), with the explicit \(1/v_V\) factor.
- B.4 is the stimulated-emission-reduced absorption rate; B.5 defines \(v_V\).
- B.6 is the neutrino inverse-decay production phase-space integral; B.10 is its detailed-balance relation.
- B.13--B.18 describe Compton production and the forward/reverse cross-section relation; B.19 is specifically the Compton absorption detailed-balance equation.
- The authors explicitly identify \(R_{\max}=R_\nu\simeq25\) km.
- Figure 7 is the \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1\) s luminosity benchmark used in this audit.

This confirms the equation mapping, fixed-\(\omega\) path prescription, full angular geometry, and 25 km boundary used in the code. It also confirms that B.19 must not be used as the neutrino inverse-decay detailed-balance equation.

The same publisher PDF states that the article has no associated data deposited with it. Its acknowledgements thank Thomas Janka and Daniel Kresse for providing the supernova profiles. The Garching archive page lists relevant radial neutrino-moment and hydro-profile collections, but explicitly warns that some archives are password protected; the linked PROMETHEUS-VERTEX profile directories relevant to this reconstruction return HTTP 401 without authorization. Consequently, the exact \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1\) s numerical snapshot used by the authors is not independently recoverable from the public article or those archive links in the present workflow. We do not substitute another progenitor, EOS, or post-bounce time and call it the same model.

### 4.2 Independent figure-source consistency checks

The public figure reconstructions provide a useful but not exact substitute:

- The Caputo and Ferreira temperature curves agree to a maximum relative difference of \(5.29\times10^{-4}\) over the overlapping 22--24 km outer interval (RMS \(1.99\times10^{-4}\)). Thus the 22--25 km temperature input is independently cross-checked at the figure level.
- The two curves labeled as the muon chemical potential disagree substantially in the core, even though the model label is SFHo-18.8. In the 22--24 km interval, the baseline Caputo \(\mu_\mu\) reaches at most 5.52 MeV; the corresponding muon density is already exponentially suppressed at \(T\simeq3.0\)--3.6 MeV. The large fractional interpolation difference near the low-value cutoff therefore does not produce a relevant 10 MeV Compton opacity correction.
- The Caputo \(\mu_{\nu_\mu}\) branches do not resolve the 22--25 km interval above the plot's approximately 1 MeV floor. The baseline zero continuation is explicitly a figure-resolution prescription, not a claim that the raw simulation chemical potential is known to vanish exactly. Setting \(|\mu_{\nu_\mu}|=1\) MeV throughout the outer shell changes the strong-end outer-shell escape factor by only \(4.94\times10^{-4}\) relative.
- The lapse curve is independently digitized from Ferreira only to approximately 24 km and then continued with a matched Schwarzschild form. Since the published fixed-\(\omega\) B.2 path opacity contains no lapse factor, this uncertainty affects B.1 source weighting, not the local outer-shell inverse-decay opacity. The separate lapse-boundary test finds a negligible B.1/escape impact for the two tested continuations.

These checks make a large *outer-shell interpolation* explanation implausible. They do not establish identity with the exact profile supplied privately to Blinov et al. The remaining raw-background uncertainty is therefore still open.

### 4.3 What can be concluded about the discrepancy

The current evidence supports the following hierarchy:

1. **Equation/algebra error in neutrino inverse decay:** not supported. Independent direct B.6 and inverse-occupation integrals reproduce the analytic production rate, B.10, and B.4 at relative residuals of order \(10^{-14}\)--\(10^{-15}\).
2. **22--25 km interpolation or chemical-potential floor:** not supported as the origin. Dense-profile evaluation changes the strong-end outer-shell escape factor by \(7.18\times10^{-6}\); the conservative \(|\mu_{\nu_\mu}|=1\) MeV floor test changes it by \(4.94\times10^{-4}\).
3. **Angular/path geometry convention:** the implementation follows the published B.2/B.3 full angular chord integral, and independent geometry tests pass. The direction-resolved audit shows that the dominant inward/outward selection is accumulated in the inner path, not generated by an incorrect 22--25 km path length.
4. **Exact stellar background:** remains unresolved because the original raw snapshot is not deposited with the article and the relevant archive endpoints are protected. This is the main remaining literature-reproduction limitation.
5. **Axial-vector constraint:** remains blocked until the pure-vector Fig. 7 benchmark is reproduced or its residual is traced to a documented difference in the source background or model assumptions.

The appropriate next step is therefore a source/profile-level comparison, not another adjustment to the local inverse-decay formula or the outer-shell interpolation. No opacity rescaling, fit to Fig. 7, or change to the production axial result is justified by the present evidence.


### 4.4 Cross-check of the muon chemical-potential reconstruction against the original Bollig figures

A more discriminating check is available than simply comparing two later figure reconstructions. The original Bollig et al. paper, arXiv:2005.07141v7, directly plots both the SFHo-18.8 muon number density (Fig. 3) and the degeneracy parameter \(\mu_\mu/T\) (Fig. 4). Its text states that the latter remains a small \(O(1)\) quantity in the high-muon-density region \(5\lesssim r\lesssim15\) km. The same paper defines the Fermi occupation as \(f_\mu(E)=[\exp((E-\mu_\mu)/T)+1]^{-1}\).

Using the common temperature curve and the two independently digitized \(\mu_\mu(r)\) curves gives:

| \(r\) [km] | \((\mu_\mu/T)_{\rm Caputo}\) | \((\mu_\mu/T)_{\rm Ferreira}\) |
|---:|---:|---:|
| 0 | 2.42 | 13.23 |
| 5 | 2.21 | 9.20 |
| 8 | 2.36 | 4.31 |
| 10 | 3.03 | 3.87 |
| 12 | 3.61 | 4.23 |
| 15 | 4.71 | 5.19 |
| 18 | 3.95 | 4.47 |
| 20 | 3.51 | 2.95 |

The Caputo reconstruction tracks the original Bollig Fig. 4 SFHo-18.8 curve: it is approximately \(2\)--\(3\) in the inner core and rises to a few near 15 km. The Ferreira reconstruction instead gives \(\mu_\mu/T\simeq13.2\) at the center and \(\simeq9.2\) at 5 km, which is incompatible with the original Fig. 4 curve and with the paper's stated mild-degeneracy description.

As a further diagnostic, inserting both digitized curves into the same relativistic Fermi integral
\[
n_\mu=\frac{1}{\pi^2}\int_0^\infty dp\,p^2
\left[\exp\!\left(\frac{\sqrt{p^2+m_\mu^2}-\mu_\mu}{T}\right)+1\right]^{-1}
\]
gives the following implied densities:

| \(r\) [km] | \(n_\mu^{\rm Caputo}\) [fm\(^{-3}\)] | \(n_\mu^{\rm Ferreira}\) [fm\(^{-3}\)] | Ratio |
|---:|---:|---:|---:|
| 0 | \(9.58\times10^{-5}\) | \(5.90\times10^{-2}\) | 616 |
| 5 | \(4.67\times10^{-4}\) | \(4.61\times10^{-2}\) | 98.8 |
| 8 | \(4.66\times10^{-3}\) | \(2.08\times10^{-2}\) | 4.46 |
| 10 | \(4.49\times10^{-3}\) | \(8.73\times10^{-3}\) | 1.94 |
| 12 | \(1.94\times10^{-3}\) | \(3.27\times10^{-3}\) | 1.68 |
| 15 | \(4.01\times10^{-5}\) | \(6.45\times10^{-5}\) | 1.61 |

The Caputo-derived density has the same qualitative radial behavior and scale as the original Bollig Fig. 3 SFHo-18.8 curve: it peaks around 8--10 km at a few \(10^{-3}\,\mathrm{fm}^{-3}\) and is strongly suppressed toward the center and beyond 15 km. The Ferreira-derived density is far above the plotted original profile in the inner core. The density comparison is a diagnostic based on the same ideal relativistic Fermi integral; it is not a replacement for the unavailable raw simulation table.

**Decision:** for the present Blinov reproduction, retain the Caputo \(\mu_\mu(r)\) reconstruction. Do not substitute the Ferreira curve merely because its figure also labels the model SFHo-18.8. The Ferreira figure-level \(\mu_\mu\) curve is not consistent with the original Bollig Fig. 3--4 diagnostics under the common Fermi-distribution convention. The reason for this inter-publication discrepancy is not established; it may involve a different profile version or chemical-potential convention and must remain explicitly unresolved. This finding makes the Caputo baseline substantially better supported than the Ferreira alternative, but still does not turn the digitized profile into the exact raw snapshot used by Blinov et al.
