# Fifty-fifth review: P1-I thermalization, B.2 propagation, gravity, and vector benchmark records

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 070f1b914ebde87ba4bd43fb784186b017dfed78  
Scope: six pending B.16/P1 records, their linked machine-readable outputs, the current profile identity, and later independent high-energy propagation checks.

## 1. Executive result

Six documents were reviewed individually. Five are PASS_WITH_NOTES and one is HISTORICAL.

The most important scientific correction is in P1-I: its proposed construction \(n_n=n_B-n_p\) would misidentify cluster-bound neutrons as free neutrons. The instruction is corrected to use the free-nucleon composition or the cross-checked Fig. 12 free-neutron/free-proton paths. The recoil pilot also now distinguishes the scattering opacity in Müller--Janka Eq. (A31) from the transport opacity in Keil--Raffelt--Janka Eq. (1); equating them is an isotropic-scattering closure, not a general identity.

The six-configuration quadrature study is classified HISTORICAL because its JSON records the earlier profile SHA 08d7afce..., not the current vertex-preserving profile B SHA 9fb14e79.... Its numerical results remain valid for that archived profile but cannot be quoted as the current profile-B convergence envelope.

No production source, opacity, coupling, Fig. 7 curve, SN1987A limit, or axial-vector constraint was changed.

## 2. Individual document outcomes

| Document | Outcome | Main finding |
|---|---|---|
| B16_P1I_LITERATURE_GUIDED_NEUTRINO_THERMALIZATION_2026-11-10.md | PASS_WITH_NOTES | Corrected free-neutron construction; distinguished \(\kappa_s\) from \(\kappa_T\); identified \(E/m_N=0.27\)--0.53 as an extrapolative range for the linear recoil approximation; no producer script/JSON exists for the recoil-only radius table. |
| B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md | PASS_WITH_NOTES | V8 output separates 108 direct-path, 60 vertex-grid, and 36 redshift-channel rays. The source-weighted Shapley result is not the unweighted 36-ray statistic. Exact V8 producer is not archived; later NumPy chord work is an independent neighboring check, not a regeneration of this JSON. |
| B16_PUBLISHED_GRAVITY_AND_ENERGY_PRESCRIPTION_RECONSTRUCTION_2026-11-09.md | PASS_WITH_NOTES | B.1 local-energy/\(E_\infty\) Jacobian is exact. B.2 is printed as a fixed-\(\omega\), Euclidean-chord integral. \(A(r)\) is needed only for an optional full-GR extension, not the published approximation. |
| B16_QUADRATURE_CONVERGENCE_2026-11-08.md | HISTORICAL | The JSON records profile SHA 08d7afce...; current profile B is 9fb14e79.... The 0.3% six-configuration convergence envelope is historical and must not be applied to profile B without a rerun. |
| B16_VECTOR_BENCHMARK_ACCEPTANCE_GATE_2026-11-09.md | PASS_WITH_NOTES | The numerical gate passes but the physical Fig. 7 reproduction remains failed at the 10 MeV strong endpoint. Clarified that missing \(A(r)\) does not block the published flat-spatial B.2 prescription; the outer thermodynamic profile remains the relevant background limitation. |
| B16_VERTEX_PRESERVING_GLOBAL_CHANNEL_DECOMPOSITION_2026-11-09.md | PASS_WITH_NOTES | The current-profile source/path decomposition is internally consistent. Corrected a NaN self-comparison display to zero relative shift; no physical number changed. |

## 3. P1-I recoil-only thermalization pilot

Keil, Raffelt and Janka define
\[
\tau_{\rm therm}(E,r)=\int_r^\infty dr'\,
\sqrt{\kappa_E(\kappa_T+\kappa_E)},\qquad
\tau_{\rm therm}(R_{\rm therm})=2/3,
\]
where \(\kappa_T\) is the transport opacity. Müller--Janka Eq. (A31), however, defines the recoil effective absorption opacity as
\[
\kappa_{a,\nu N}^{\rm recoil}
=\frac{|E_\nu-3T|}{m_N}\,\kappa_{s,\nu N},
\]
with \(\kappa_{s,\nu N}\) the scattering opacity. The identification \(\kappa_s\simeq\kappa_T\) is an isotropic-scattering closure; it is not exact for a general differential kernel. The pilot now labels this assumption.

At \(E=255\) and \(500\) MeV, \(E/m_N\simeq0.27\) and \(0.53\). Applying the linear recoil fraction at these energies is an extrapolation of the small-recoil effective opacity. The radii 23.95 km and 26.09 km for the central tail remain scale estimates, not controlled energy-sphere predictions.

The composition input also matters. The validated Caputo/E--K composition work shows a nonzero cluster baryon fraction in the 9--15 km region. Therefore \(n_B-n_p^{\rm free}\) is not the free-neutron density. Use \(n_n^{\rm free}=Y_n n_B\) and \(n_p^{\rm free}=Y_p n_B\), or the cross-checked E--K free-nucleon curves. A nuclear scattering response is still not included by simply relabeling the total baryon density.

The P1-I recoil-only table has no committed producer script or JSON. It remains a transparent but not script-reproducible literature pilot. Existing P1-I-B/C and P1-IIIb/P1-IIIe-C4 local kernels should be reused; the radial energy-redistribution problem remains separate and unfinished. In particular, \(e^{-\tau_{\rm therm}}\) is not an exact daughter escape probability.

## 4. High-energy B.2 path audit

The P1-B.2 JSON records three different ray samples:
- 108 rays for direct path-coordinate versus analytic radial primitive;
- 60 rays for 642 opacity nodes versus all 1687 profile vertices;
- 36 rays for fixed-\(\omega\) versus path-redshift channel attribution.

The direct path result reaches \(8.3\times10^{-14}\) agreement with the analytic primitive at four Gauss points per split segment. The 642-to-1687 comparison changes total optical depth by at most \(1.87\times10^{-5}\) and the selected angle-averaged escape probability by at most \(2.18\times10^{-5}\). The 36-ray channel means are unweighted; the separate Shapley decomposition is source weighted and assigns 99.9860% of the global 210--510 MeV luminosity change to neutrino inverse decay and 0.0140% to semi-Compton.

The direct V8 producer for this exact JSON is not archived. The later pinned NumPy high-energy chord study provides an independent neighboring cross-check (36 rays across three opacity grids, 108 combinations, maximum V8/NumPy metric difference \(1.19\times10^{-9}\)); it does not recreate the distinct 108/60/36 ray sets or the global Shapley payload in this P1 JSON. Keep the evidence and provenance statements separate.

## 5. Gravity and energy prescription

The B.1 local source energy and energy-at-infinity forms are exactly related by \(E_\infty=N(r)\omega_{\rm loc}\) and the Jacobian stated in the report. The B.2 expression as printed uses one fixed \(\omega\) along a Euclidean straight chord. No \(A(r)\), proper-distance factor, or geodesic bending appears. The path-redshift branch is a sensitivity calculation, not the printed baseline and not a full-GR ray trace.

Thus missing \(A(r)\) or \(M(r)\) is not a blocker for reproducing the published pseudo-Newtonian approximation. It blocks only an optional full-GR extension.

## 6. Quadrature provenance and current vector gate

The six-configuration quadrature JSON has profile SHA 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9, whereas the current vertex-preserving profile B is 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. The old scan is retained as historical; the 42nd review's later high-energy path checks on profile B do not amount to a rerun of the complete six-configuration 25-point luminosity grid.

The acceptance gate remains: numerical modules pass, but the fixed-\(\omega\) 10 MeV strong endpoint is \(+92.2406\%\) above the digitized Fig. 7 point. The path-redshift-only diagnostic gives \(+36.7448\%\), but does not become the published baseline. Axial-vector recalculation remains frozen.

The vertex-preserving channel decomposition uses the current profile SHA. Its reported source-weighted mean optical-depth split (89.7782% neutrino inverse decay, 10.2218% Compton) and 15--20 km shell attribution are kept as diagnostics for that benchmark. The NaN self-comparison was a presentation artifact and is now shown as a zero shift.

## 7. Disposition

Five records are PASS_WITH_NOTES; the old-profile quadrature report is HISTORICAL. No source, opacity, coupling, profile, luminosity curve, Fig. 7 reference, SN1987A limit, or axial-vector constraint changed. The next P1-I step, if pursued, is not another recoil-only opacity multiplier: it is a species-resolved radial energy-exchange calculation using the already reviewed local kernels and explicit nuclear/cluster limitations.
