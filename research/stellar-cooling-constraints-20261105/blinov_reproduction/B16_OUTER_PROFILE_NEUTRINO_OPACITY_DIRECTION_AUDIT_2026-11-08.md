# B.16 22--25 km profile, neutrino inverse-decay, and direction-resolved escape audit

> **Historical profile version:** the paired numerical output for this report uses the 501-node uniform profile, SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`. The current working input is the 1687-row vertex-preserving profile, SHA-256 `6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`. The current-profile rerun and quantitative old/new comparison are documented in `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`; see also `outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json`. Keep this report as a historical record and do not combine its numerical output with current-profile results.


**Status:** the first three stages of the 2026-11-08 investigation are complete. The independent literature comparison is partially complete; the original raw Garching profile has not been accessed. No axial-vector constraint curve is updated.

**Benchmark:** pure-vector \(m_V=10\) MeV, fixed-\(\omega\) Appendix-B prescription, \(R_{\max}=R_\nu=25\) km, reconstructed SFHo-18.8 profile at \(t_{\rm pb}=1\) s.

## 1. Outer profile inputs and interpolation

### 1.1 Provenance and sampled inputs

The current profile contains 502 digitized rows at 0.05 km spacing from 0 to 25 km. In the 22--25 km shell, the 61 original nodes give:

| Input | Range |
|---|---:|
| \(T\) | 3.03377--3.55139 MeV |
| \(\mu_\mu\) | 0--5.51998 MeV |
| \(\mu_{\nu_\mu}\) | 0 MeV in the adopted digitization |
| \(N(r)\) | 0.908502--0.919912 |

The zero \(\mu_{\nu_\mu}\) continuation is a figure-resolution convention: the published logarithmic plot does not resolve \(|\mu_{\nu_\mu}|<1\) MeV in this outer region. A separate \(|\mu_{\nu_\mu}|=1\) MeV sensitivity test is included below. The tau-neutrino chemical potential is set to zero as explicitly stated by Blinov et al., because the simulations do not provide it and tau leptons are not populated in the PNS.

The profile is a public-figure reconstruction, not the raw Garching simulation table. The temperature is digitized from Caputo et al. (arXiv:2109.03244v3), while the lapse is digitized from Ferreira et al. (arXiv:2510.14469v1) through 24 km and matched to a Schwarzschild exterior through 25 km. The two published temperature curves agree over their overlap to a maximum relative difference of 0.267%. The two published \(\mu_\mu\) curves differ more visibly; the Caputo curve is retained as the baseline and the Ferreira curve remains a diagnostic alternative. No restricted raw simulation table was accessed or redistributed.

### 1.2 Primitive-field and local-rate interpolation

The existing B.2 path grid has only nine nodes in the outer shell, with a maximum spacing of 0.680 km. We compared the current two-stage interpolation (evaluate rates on the composite radial grid, then interpolate rates along the chord) against direct interpolation of the archived 0.05 km primitive profile followed by local nonlinear rate evaluation.

| Quantity | Result |
|---|---:|
| Maximum temperature interpolation error | 0.00426 MeV |
| Maximum lapse interpolation error | \(3.61\times10^{-5}\) |
| Maximum neutrino reduced-absorption local-rate interpolation error | 0.0837% |
| RMS neutrino reduced-absorption interpolation error | 0.0252% |
| Source-weighted 22--25 km neutrino optical-depth change | 0.00123% |
| Strong-endpoint outer-shell escape-factor change | 0.000718% |

The \(\mu_\mu\) interpolation has a larger absolute discrepancy at isolated digitized nodes, but at \(m_V=10\) MeV the local Compton reduced opacity is only \(1.35\times10^{-15}\) of the neutrino reduced-opacity peak in this shell. Thus it cannot explain the 10 MeV tail discrepancy.

Refining the path-opacity grid while holding the B.1 source quadrature and source values fixed gives the same conclusion. At the strong endpoint, changing from the 40-node source grid to a uniform 0.05 km path grid changes the luminosity by 0.176%; a 0.025 km grid changes it by 0.178%. At the Fig. 7 peak the change is approximately 0.010%. These are small numerical corrections, not an explanation of the roughly 92% high-coupling luminosity mismatch.

Setting \(|\mu_{\nu_\mu}|=1\) MeV throughout 22--25 km, with all other inputs fixed, changes the strong-endpoint outer-shell escape factor by 0.0494%. The figure-floor convention is therefore not a significant 10 MeV opacity uncertainty.

### 1.3 Correct role of the lapse

In the fixed-\(\omega\) B.2 prescription, the path opacity depends on local \(T(r')\) and chemical potentials at the path radius, but the lapse does not enter the path integral directly. The lapse enters B.1 through the \(N(r)^2\) source factor and the local escape-energy threshold \(\omega_{\min}=m_V/N(r)\).

Only 0.0728% of the reconstructed 10 MeV optically thin source lies at \(r\ge22\) km, and 0.0205% lies at \(r\ge24\) km. Therefore the outer-shell lapse continuation is not a plausible explanation of the strong-coupling propagation discrepancy, although it remains part of the source-side audit.

## 2. Direct neutrino inverse-decay phase-space audit

### 2.1 Equation-number clarification

The equation labels are kept process-specific:

- B.4 defines the reduced absorption rate,
  \[
  \Gamma_{\rm abs}^{*}=(1-e^{-\omega/T})\Gamma_{\rm abs}.
  \]
- B.6--B.10 describe mode-resolved neutrino inverse decay, its production/absorption integrals, and detailed balance.
- B.19 belongs to semi-Compton forward/inverse detailed balance. It is **not** the neutrino inverse-decay equation and is not used as such here.

For neutrino inverse decay, the detailed-balance identity tested here is the B.10 relation
\[
\Gamma_{\rm prod}=e^{-\omega/T}\Gamma_{\rm abs}.
\]

The B.19 semi-Compton collision-integrand test remains a separate regression in 'test_stage1_detailed_balance.py'. That test uses the actual mode-resolved Compton matrix elements at fixed-muon kinematics; it is not a full moving-muon thermal phase-space integration.

### 2.2 Independent direct integration

A new implementation directly integrates the Fermi occupation and blocking factors over the two-body decay angle using 512-point Gauss-Legendre quadrature. It separately evaluates \(\nu_\mu\), \(\nu_\tau\), and the \(L,+,-\) vector modes, then compares with the existing 48-point mode-resolved implementation and with the closed-form Fermi-pair antiderivative.

The audit covers \(r=8,10,12,15,18.5,20,22,23,24,25\) km and \(\omega=12,15,20,30,50,100,300\) MeV.

| Check | Maximum relative residual |
|---|---:|
| Mode production, 48-point code vs direct integral | \(4.01\times10^{-12}\) |
| Mode absorption, 48-point code vs direct integral | \(4.01\times10^{-12}\) |
| B.4 reduced-absorption identity | \(6.81\times10^{-15}\) |
| Neutrino B.10 detailed balance | \(6.82\times10^{-15}\) |
| Closed-form Fermi integral vs direct angular integral | \(4.19\times10^{-15}\) |
| Polarization sum vs scalar Fermi-pair expression | \(2.90\times10^{-12}\) |
| 256-point vs 512-point direct quadrature | \(5.55\times10^{-15}\) |
| \(\mu_{\nu_\mu}\to-\mu_{\nu_\mu}\) plus helicity-label swap | \(2.33\times10^{-15}\) |

Thus the neutrino inverse-decay Fermi integral, Pauli blocking, B.4 reduced opacity, and B.6--B.10 mode decomposition are numerically consistent in the tested domain. No missing factor or numerical integration error at the \(10^{-12}\) level is indicated.

This does not test the provenance of the reconstructed stellar profile, the validity of the fixed-\(\omega\) propagation prescription, or the scalar-versus-mode-resolved ambiguity in how B.2 combines polarization opacities.

## 3. Strong-coupling escape probability by emission radius and direction

The 8--15 km region accounts for 79.23% of the global B.1 source at 10 MeV. The corresponding impact parameters span 0.303--14.787 km. A ray through the 22--25 km shell travels 3.000--3.869 km in that shell, depending on impact parameter.

### 3.1 Peak and strong endpoint

| Quantity, sources at 8--15 km | Fig. 7 peak \(g=1.1341\times10^{-8}\) | Strong endpoint \(g=4.1717\times10^{-8}\) |
|---|---:|---:|
| Full-path escape probability | 0.3543 | \(3.5026\times10^{-4}\) |
| Outer-shell-only escape probability | 0.8258 | 0.1500 |
| Unattenuated-source-weighted mean outer-shell \(\tau\) | 0.2015 | 2.7267 |
| 90th percentile outer-shell \(\tau\) | 0.3711 | 5.0210 |

At the strong endpoint, the outer shell is optically important. However, it is not the only source of trapping: the full-path escape probability is much smaller than the outer-shell-only escape probability because rays also cross the dense inner PNS.

### 3.2 Direction dependence at the strong endpoint

The direction bins are defined by the cosine \(c_\theta\) relative to the outward radial direction.

| Direction bin | \(c_\theta\) | Full-path escape probability |
|---|---|---:|
| Inward radial | \([-1,-0.8]\) | \(8.74\times10^{-6}\) |
| Inward oblique | \([-0.8,-0.2]\) | \(1.40\times10^{-5}\) |
| Tangential | \([-0.2,0.2]\) | \(1.10\times10^{-4}\) |
| Outward oblique | \([0.2,0.8]\) | \(5.89\times10^{-4}\) |
| Outward radial | \([0.8,1]\) | \(1.45\times10^{-3}\) |

Outward radial trajectories are the most transparent, while inward trajectories are strongly suppressed because they cross the inner core before reaching the outer boundary. The full angular average is therefore essential; a radial-only estimate would substantially overestimate the escaping luminosity.

The outer-shell-only escape probabilities are much closer across the inward/outward sign pairs because the 22--25 km path length depends on the impact parameter \(b=r\sqrt{1-c_\theta^2}\), not on the sign of \(c_\theta\). The large inward/outward difference in the full path is generated mainly by the interior trajectory.

### 3.3 Emission-shell comparison

At the strong endpoint, the outer-shell-only escape probabilities are approximately:

| Emission shell | Outer-shell-only escape probability |
|---|---:|
| 8--10 km | 0.1908 |
| 10--12 km | 0.1331 |
| 12--15 km | 0.0625 |

The outer shell attenuates the more outward-emitted source more strongly when the source is nearer 15 km, because the impact-parameter distribution and the path geometry change with emission radius. Nevertheless, the full-path escape probability is still dominated by the accumulated opacity through the inner and intermediate shells.

## 4. Comparison with the published literature and remaining limitations

Blinov et al., arXiv:2511.09619v2, explicitly use the SFHo-18.8 muonic supernova model at 1 s post-bounce, set \(R_{\max}=R_\nu\simeq25\) km, perform the full angular average, include the \(1/v_V\) factor in the optical depth, use the stimulated-emission reduced opacity, and include gravitational effects in the B.1 luminosity and escape-energy threshold. The present literal reference implementation follows these displayed choices.

Blinov et al. also state that \(\nu_\mu\) and \(\nu_\tau\) have different chemical potentials; the \(\nu_\tau\) chemical potential is set to zero because the simulation does not provide it. This matches the flavor convention used here. The paper further states that the 25 km boundary is the neutrinosphere radius, not an arbitrary numerical cutoff.

The current reconstructed profile combines public figure information from Caputo et al. (arXiv:2109.03244v3) and Ferreira et al. (arXiv:2510.14469v1). Its temperature curves agree over their overlap to 0.267%, and the outer lapse is matched to the exterior Schwarzschild form. However, the reconstructed \(\mu_\mu\) curves differ between the two publications, and \(\mu_{\nu_\mu}\) is unresolved below the plotted 1 MeV floor. These limitations are not removed by the direct rate audit.

The B.2 equation in the paper is written with a scalar opacity, whereas B.6 and B.13 explicitly sum over the three vector polarizations in their production rates. The printed B.2 does not uniquely state whether the scalar absorption rate is a sum, an average, or a production-weighted effective rate when the mode opacities differ. The mode-resolved and literal scalar reference calculations must therefore remain separately identified; agreement of the local neutrino inverse-decay rates does not settle this prescription ambiguity.

The 10 MeV Fig. 7 high-coupling discrepancy remains open. The tests above show that it is not explained by the 22--25 km rate interpolation, by the neutrino inverse-decay angular integral, or by a coarse path quadrature. The strong endpoint is sensitive to the outer shell and to the full interior direction-dependent path. The next comparison must therefore isolate (i) the digitized background/profile reconstruction, (ii) the scalar versus mode-resolved interpretation of B.2, and (iii) the exact numerical opacity along the entire chord. No rate or luminosity rescaling is justified.

## 5. Reproducibility and outputs

- Outer input audit: 'audit_b16_outer_profile_inputs.py'
- Outer path-grid refinement: 'audit_b16_outer_profile_interpolation.py'
- Direct neutrino inverse-decay integral: 'audit_b16_neutrino_inverse_decay_direct.py'
- Direction-resolved escape: 'audit_b16_outer_escape_angular_distribution.py'
- Machine-readable results:
  - 'outputs/b16_outer_profile_inputs_10mev_2026-11-08.json'
  - 'outputs/b16_outer_profile_interpolation_10mev_2026-11-08.json'
  - 'outputs/b16_neutrino_inverse_decay_direct_10mev_2026-11-08.json'
  - 'outputs/b16_outer_escape_angular_distribution_10mev_2026-11-08.json'
- The corresponding GitHub Actions runs are archived on the research branch. All final runs for the above four audits completed successfully.

## 6. Decision gate before any axial-vector update

Do not update the axial-vector constraint curve at this stage. First complete an independent comparison of the literal scalar B.2 implementation with the mode-resolved attenuation prescription, and compare the reconstructed background against all available published profile information. The raw Garching profile remains unavailable in this audit; no claim of exact original-profile reproduction is made. Only after the pure-vector Fig. 7 baseline is understood should the axial-vector rates be substituted.
