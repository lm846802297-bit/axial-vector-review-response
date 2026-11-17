# Fifty-third review: P1-IIIe C3 degeneracy validation, full radial EOS mapping, and P1-IIIa scalar response

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 0829716140fd04dd39069677a55e1dab4e08857d  
Scope: six pending documents, C1/C3 scripts and workflows, machine-readable outputs, and the P1-IIIa relativistic free-gas response implementation.

## 1. Executive result

Six documents were individually reviewed; all six are PASS_WITH_NOTES. The full 301-point Caputo-to-SFHo EOS mapping and the three C3 static-degeneracy validation stages have successful research-branch CI runs. The P1-IIIa relativistic free-gas response has strong internal numerical checks but remains a scalar response baseline, not a full weak collision kernel.

The main reproducibility qualifications are:
- C3-A compares distinct integral/derivative estimators but uses the same quadrature backend.
- C3-B's archived JSON includes cross_runtime_validation fields absent from the current Python driver; the archived record combines a direct JavaScript scan with Python-CI values, but the direct JavaScript producer is not archived.
- C3-C's CI reruns the same checked-in Python implementation in a clean environment; it is not a second independent algorithm.
- P1-IIIa has no dedicated test module or CI workflow, and its nonrelativistic helper returns zero at exactly \(q_0=0\) rather than the finite removable limit. The current archived comparisons use only nonzero stationary-recoil \(q_0\), so those numbers are unaffected.

No EOS table payload, mapped profile, C2 occupation, C3 static factor, dynamic weak tensor, B.2 opacity, Fig. 7 curve, luminosity, SN1987A limit, or axial-vector exclusion was modified.

## 2. Individual document outcomes

| Document | Outcome | Review finding |
|---|---|---|
| B16_P1IIIE_C3A_FULL_RADIAL_DEGENERACY_IDENTITY_2026-11-11.md | PASS_WITH_NOTES | The direct blocked integral and finite-difference density derivative agree over 301 radii. They are distinct estimators but share the same Gauss-Legendre phase_space_integrals backend; CI is a clean rerun, not an independent codebase. |
| B16_P1IIIE_C3B_FULL_RADIAL_DEGENERACY_STEP_SCAN_2026-11-11.md | PASS_WITH_NOTES | All 5,418 species-radius-step rows and nine \(h/T\) values pass. The selected \(3\times10^{-5}\) step is stable below \(10^{-8}\). Archived JSON has extra cross_runtime_validation metadata not emitted by the current Python driver; direct JavaScript producer source is absent. |
| B16_P1IIIE_C3C_FULL_RADIAL_DEGENERACY_DIAGNOSTICS_2026-11-11.md | PASS_WITH_NOTES | All 602 records pass, including relativistic C2 reproduction, NR fixed-density closure, and descriptive radial correlations. The CI is a clean rerun of the same Python implementation, not an independent algorithm. |
| B16_P1IIIE_C_CAPUTO_PROFILE_TO_SFHO_EOS_2026-11-11.md | PASS_WITH_NOTES | The ten-key-radius mapping is a valid predecessor and correctly uses \(Y_p^{\rm tot}\). The later full 301-point C1 mapping supersedes its pending full-profile/CI steps. |
| B16_P1IIIE_C_FULL_RADIAL_SFHO_EOS_MAPPING_2026-11-11.md | PASS_WITH_NOTES | The full-profile workflow run #42960145972 succeeds with checksum-pinned Caputo source and SFHo/FRDM tables, 301 radii, 308 physical density rows, and no interpolation extrapolation. Input remains a public-figure reconstruction, not raw Garching data. |
| B16_P1III_A_RELATIVISTIC_FERMI_GAS_RESPONSE_2026-11-10.md | PASS_WITH_NOTES | The spin-summed scalar response, angular reduction, support, detailed balance, and static sum rule are internally consistent. The benchmark is illustrative and vacuum-mass; no weak tensor, leptonic contraction, RPA, or correlations are included. No dedicated tests/CI are present; the NR helper lacks the exact \(q_0=0\) limit. |

## 3. Full radial EOS mapping

The successful workflow run #42960145972 completed the builder/interpolation tests, full 301-point mapping, and the domain/composition/filling-factor gates. It downloaded and checksum-verified the Caputo arXiv source archive and all three official SFHo/FRDM v1.03 tables. The map uses trilinear interpolation in \((\log_{10}T,Y_p^{\rm tot},\log_{10}n_B)\), only the 308 physical density rows, and bounds_error=True. All 301 points lie inside the table domains.

The profile uses Caputo Fig. 1/Fig. 4 native PDF paths and linear interpolation of \(T(r)\) onto the 0.05-km composition grid. It is a published-figure reconstruction at \(t_{\rm pb}=1\) s, not raw Garching hydro data or a time history. The full C1 mapping is therefore accepted as a local EOS snapshot input, not as a raw simulation profile.

## 4. C3-A: local degeneracy identity

At fixed \(T,m_N^*,U_N,\xi_{\rm SPP}\),
\[
F_{NN}^{\rm deg}
=\frac{\int dp\,p^2f_N(1-f_N)}{\int dp\,p^2f_N}
=\frac{T}{n_N'}\left.\frac{\partial n_N'}{\partial\nu_N}\right|_{T,m_N^*}.
\]
The archived residuals are \(7.82\times10^{-11}\) RMS / \(3.20\times10^{-10}\) maximum for neutrons and \(8.80\times10^{-11}\) RMS / \(1.98\times10^{-10}\) maximum for protons. The direct C2 reproduction is at floating-point scale. Workflow #42970450802 passes tests, recomputes all 301 radii, and checks the archived CSV/JSON.

Qualification: the direct integral and derivative use different integrands/estimators but the same phase_space_integrals quadrature routine. The clean CI run validates reproducibility of the checked-in implementation, not independent quadrature code.

## 5. C3-B: finite-difference step scan

The 5,418-row scan covers 301 radii, two species, and nine \(h/T\) values. Reducing \(h/T\) from \(10^{-2}\) to \(10^{-3}\) reduces maximum residuals by approximately 100, confirming \(O(h^2)\) truncation. The shared \(h/T=3\times10^{-5}\) step gives a maximum direct-scan residual \(3.19345\times10^{-10}\), comfortably below the \(10^{-8}\) gate. The exact roundoff floor varies by backend.

Workflow #42971175588 passes the tests, recomputes all 5,418 rows, and checks the selected-step and reference invariants.

The archived JSON has an additional cross_runtime_validation object absent from the checked-in Python driver. Its species values record the direct JavaScript scan, while the cross-runtime field stores Python-CI values. The direct JavaScript producer source/invocation is not archived; the workflow's Python rerun checks numerical invariants rather than byte-for-byte JSON schema equality. Preserve this source/provenance distinction.

## 6. C3-C: radial static-factor diagnostics

The dimensionless reduction
\[
F_{NN}^{\rm deg}=\mathcal F(\eta_N,\theta_N),\qquad
\eta_N=\nu_N/T,\quad \theta_N=T/m_N^*
\]
is exact for the stated local relativistic quasiparticle prescription. Across the profile, \(T/m_N^*\) is 0.0138--0.0555. The maximum nonrelativistic fixed-\(\nu\) shifts are 8.88% (n) and 3.67% (p); the fixed-density shifts are larger, 18.99% and 8.87%, because the NR chemical potential must be refitted to preserve density.

Workflow #42998186301 passes five tests, recomputes all 602 species-radius records, and checks the committed JSON/CSV invariants. This is a clean rerun of the same Python implementation, not a second independent codebase. The radial correlations/regressions are descriptive along one snapshot and not causal or universal EOS relations.

## 7. P1-IIIa scalar relativistic free-gas response

The response
\[
S_N(q_0,q)=2\int\frac{d^3p}{(2\pi)^3}\,2\pi
\delta(q_0+E_p-E_{p+q})f_p(1-f_{p+q})
\]
has the correct spin factor and, after angular integration, the \(1/(\pi q)\) prefactor and \(|q_0|<q\) support. The JSON records maximum residuals \(6.42\times10^{-12}\) for the density equation, \(7.83\times10^{-11}\) for detailed balance, \(4.80\times10^{-13}\) for the static sum rule, and \(4.29\times10^{-14}\) for 300/900-node convergence.

The benchmark uses \(T=3.03\) MeV, \(Y_p=0.10\), \(n_0=0.16\ {\rm fm}^{-3}\), and vacuum nucleon masses. It is deliberately not the C1/C2 SFHo profile. The implementation does not yet include the vector/axial single-nucleon tensor, weak magnetism, form factors, leptonic contraction, neutrino final-state blocking, mean fields, RPA, or NN correlations.

A small helper limitation is noted: S_nr returns zero at exactly \(q_0=0\), although its analytic expression has a finite removable limit. The archived NR comparison only evaluates nonzero stationary-target recoil \(q_0\), so no stored result is affected. Implement the limit before using S_nr in a full \(q_0\)-spectrum integration. There is no dedicated P1-IIIa test module or CI workflow.

## 8. Disposition

All six documents are PASS_WITH_NOTES. C1 and C3 are accepted within their local static, figure-derived snapshot scope. P1-IIIa remains a scalar free-gas baseline only. The C3B archived JSON/source schema distinction and P1-IIIa zero-transfer helper limit are explicitly recorded. No dynamic weak response, B.2 opacity, Fig. 7 curve, luminosity, SN1987A limit, or axial-vector constraint is modified.
