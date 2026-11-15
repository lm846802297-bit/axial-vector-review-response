# Fifty-second review: P1-IIId vector/NSE provenance and P1-IIIe-A/B/C2 EOS occupation

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 66d2e68f8417ee1da56c392037c8c14f7c311503  
Scope: six pending documents, the linked extraction/occupation code, test modules, machine-readable outputs, and the official Hempel/Fiorillo conventions.

## 1. Executive result

Six documents were individually reviewed; all six are PASS_WITH_NOTES. The P1-IIId public-figure chain is now materially more complete than the original source-audit notes indicate: the native Fig. 12 extraction and Caputo cross-check are complete, and the E--K neutron/proton curves are consistent with Caputo free-nucleon densities at the sub-percent figure level. This is not raw Garching validation.

The P1-IIIe EOS occupation mapping is algebraically consistent with Hempel Eqs. (91)--(99) and (107), and the official SFHo/FRDM tables have been checksum-verified and decoded. The 301-point C2 occupation output passes its recorded local density and quadrature criteria. The published global mass-time averages remain unreproduced because the Garching time-dependent profiles and \(\Delta M\,\Delta t\) weights are not available.

One small code consistency correction was made: the generic filling-factor inference default now uses the exact HS excluded-volume reference density \(n_B^0=0.15824150805\ {\rm fm}^{-3}\), matching the raw-table audit. The public SFHo manual reports the rounded value 0.1583. A regression test was added. The full unit-test suite was **not rerun after this correction**, so no new test pass is claimed. Existing raw-table/CI acceptance remains historical evidence for the pre-correction tree.

No EOS table payload, C1/C2 profile, static degeneracy output, dynamic response, B.2 opacity, Fig. 7 curve, SN1987A limit, or axial-vector exclusion was changed.

## 2. Individual document outcomes

| Document | Outcome | Review finding |
|---|---|---|
| B16_P1IIID_FIG12_VECTOR_EXTRACTION_CROSSCHECK_2026-11-11.md | PASS_WITH_NOTES | The archived source PDF hash, page, path indices, and numerical summary agree. The workflow pins the published APS PDF hash; the standalone extractor accepts one additional hash, which must be separately provenance-labelled. Figure-level residuals are below the line-stroke uncertainty; this is not raw-profile precision. |
| B16_P1IIID_NSE_CLUSTER_CHARGE_CLOSURE_2026-11-11.md | PASS_WITH_NOTES | The conditional NSE bookkeeping is sound. E--K/Caputo comparison supports the free-nucleon interpretation at figure level. The 8 km charge residual is digitization closure noise because the Fig. 4 cluster fraction is zero there; nonzero cluster fractions are supported from 9--15 km. Raw archive variable definitions and nuclear response remain open. |
| B16_P1IIID_PUBLIC_SNAPSHOT_COMPOSITION_PROVENANCE_2026-11-10.md | PASS_WITH_NOTES | The old execution order is updated: Caputo extraction and E--K figure-level cross-check are complete. The public figure reconstruction is not raw Garching data; the historical HTTP 401 is date-specific. SFHoY remains a separate EOS scenario. |
| B16_P1IIIE_A_EOS_OCCUPATION_IMPLEMENTATION_2026-11-11.md | PASS_WITH_NOTES | The Hempel-to-Fiorillo mapping, free-volume density, spin factor, static degeneracy factor, derivative identity, and \(\xi\) volume normalization are consistent. The old statement that the binary tables could not be acquired is historical. The software field scalar_potential_mev actually stores the full \(U_N\), not only \(\Sigma_S\). |
| B16_P1IIIE_B_SFHO_REALDATA_CLOSURE_2026-11-11.md | PASS_WITH_NOTES | Official table hashes, layouts, physical-density mask, whole-table identities, and the 224-cell sampled closure are documented. The 35/35 local suite and no-skip CI acceptance are recorded in §13; the earlier pending-execution statements in §10/§12 are superseded. Global Fiorillo Table 1 averages are still not reproduced. |
| B16_P1IIIE_C2_FULL_RADIAL_EOS_FERMI_DISTRIBUTIONS_2026-11-11.md | PASS_WITH_NOTES | The 301-point C1 input fingerprint, Hempel convention, local density closure, and all-radius quadrature maxima agree with the archived JSON. The unit tests sample selected radii; the full radial maxima come from the standalone run/JSON. This is a Caputo public-figure snapshot, not a raw Garching time history. |

## 3. P1-IIId native-vector and NSE cross-check

The archived E--K extraction uses the published APS PDF SHA-256 c3b92fe6cf2a8bd3fec84925e2baababfe0c707327a68135013f953ed3d87d43, page index 14 / printed page 15, and paths 25/181/182. The workflow downloads and pins that exact source. The standalone extractor also accepts d660eb390271b41c5c0c20ccd52cc57df891a78d30067a78f84bb6c228225a92; current archived outputs identify the c3b92... source. Any use of the alternate hash must preserve its own provenance.

The numerical cross-check gives:
- E--K temperature versus Caputo: 0.0707% RMS over 55 common radii;
- E--K temperature versus Bollig Fig. 1: 0.0953% RMS over 391 radii;
- E--K neutron/proton versus Caputo free n,p: 0.580%/0.586% RMS over ten radii;
- E--K n+p versus Caputo free baryons: 0.574% RMS;
- E--K n+p versus total Caputo nB: 5.325% RMS.

The corrected density calibration is selected by equal log-tick spacing and the same-model free-nucleon comparison. The upper tick glyphs remain visually ambiguous; this is not proof of a typesetting error. The line-stroke uncertainty is about 4.9% in density, so sub-percent residuals are not raw-profile precision.

The Caputo Fig. 4 composition gives \(X_{\rm cluster}=0\) at 8 km, despite a 0.037% \(n_Q^{\rm cl}/n_B\) residual from the Fig. 1 density paths. That residual is treated as figure-digitization closure error. From 9 to 15 km, the reconstructed cluster baryon fraction rises from about 0.45% to 8.85%, the cluster charge fraction from about 0.19% to 3.43%, and the effective \(\langle Z/A\rangle_{\rm cl}\) varies from about 0.42 to 0.387. These are public-figure composition estimates. They support keeping free nucleons and clusters separate but do not calculate nuclear neutrino opacity.

## 4. Hempel-to-Fiorillo convention audit

Hempel (2015) Eqs. (91)--(93) define \(n_N'=n_N/\xi\) and the HS filling factor. Eqs. (94)--(99) show that the nucleus interaction \(W_N\) enters both the total vector self-energy and total chemical potential and cancels in the Fermi occupation. The resulting mapping is
\[
U_N=m_N^*-m_N+\Sigma_{V,N}^{\rm tot},\qquad
\mu_{N,F}^*=\mu_N^{\rm nonrel},
\]
\[
\nu_N=\mu_N^{\rm nonrel}-U_N,\qquad
K_N(p)=\sqrt{p^2+m_N^{*2}}-m_N^*.
\]
Hempel Eq. (107) multiplies a response per available nucleon volume by \(\xi\) to obtain the total-volume rate. The code's density and static-factor formulas follow these conventions.

The code attribute scalar_potential_mev is semantically broader than its name: it stores the complete \(U_N\), including the effective-mass shift and total vector self-energy. The report now makes this explicit; a future API cleanup may rename it, but no interface-wide refactor was attempted here.

## 5. Official SFHo/FRDM data and local closure

The B report records exact archive and extracted-table hashes, the (81,61,326,18), (81,60,326,7), and (81,61,326,8) layouts, and the physical 308-row density mask. Its full-table checks validate binary parsing, grid alignment, thermodynamic identities, composition free-n,p layers, and the filling-factor identity. The sampled phase-space closure covers 224 states, with 208 inside the stated validity domain; it is not a continuous-domain theorem.

The exact HS excluded-volume reference density used by the raw-table identity is 0.15824150805 fm^-3. The public manual rounds the SFHo saturation density to 0.1583 fm^-3. The generic kernel fallback had used the rounded value while the real-table audit supplied the unrounded value explicitly. The fallback default and unit-test expectations are now aligned to the exact table-module constant. This affects only the generic composition-inferred-\(\xi\) path; the raw-table audit and C1/C2 production outputs are unchanged because they use the SPP \(\xi\) or pass the exact constant.

The recorded 35/35 local P1-IIIe-A/B suite and run #42953524476 are accepted as historical pre-correction evidence. The new default-constant patch and added regression test have not been run through the full suite in this review.

## 6. C2 full-radial occupation

The C2 JSON records the input CSV SHA-256 97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59, the 301-point 0.20--15.20 km grid, and the official EOS-table hashes. Across all 301 radii:
- maximum relative density residual: 0.2154% neutron, 0.7630% proton;
- maximum |Delta nu_N|: 0.1166 MeV neutron, 0.1832 MeV proton;
- maximum |Delta F_NN_deg|: 4.06e-4 neutron, 4.45e-4 proton;
- 2048-versus-512 relative density changes: 6.11e-15 neutron, 5.33e-15 proton;
- 2048-versus-512 absolute F_deg changes: 6.55e-15 neutron, 5.00e-15 proton.

The primary occupation retains the tabulated Hempel/Fiorillo chemical potentials. Density-matched states are sensitivity diagnostics only. The unit-test module checks selected core/outer points; the full radial maxima are reported by the standalone analysis JSON. This is local snapshot-level closure, not the Fiorillo mass-time averages and not a dynamic response or cooling result.

## 7. Remaining physical boundaries

1. The Garching raw same-snapshot profile and its field dictionary have not been obtained; the Caputo profile is a published-figure reconstruction.
2. The Fiorillo Table 1 averages require the mass-time profile and \(\Delta M\,\Delta t\) weights and remain unreproduced.
3. The P1-IIIb kernel covers free neutrons/protons; nuclear coherent/inelastic response is not yet included.
4. The E--K density comparison is restricted to the common 1--15 km Caputo composition support; do not extrapolate the composition closure to 16--20 km from the separate key-radii artifact.
5. No dynamic weak tensor, B.2 opacity, Fig. 7 luminosity, SN1987A limit, or axial-vector exclusion is changed by these documents.

## 8. Final disposition

All six documents are PASS_WITH_NOTES. The P1-IIId figure-level comparison and composition interpretation are updated; the P1-IIIe EOS data/occupation chain is accepted within its documented sampled-grid and snapshot scope. The generic filling-factor default is aligned to the exact HS reference density, but the new regression test has not yet been executed. Continue with the next PENDING row in DOCUMENT_AUDIT_REGISTER.csv.

## 9. Post-review artifact-integrity repair (2026-11-15)

The committed file \`outputs/p1iii_eos_kernel_self_test_2026-11-11.json\` was found to contain three literal backslash-n sequences between object properties. A strict JSON parser failed at line 78, column 48. Only those three separators were replaced with ordinary line breaks; the file now parses successfully and all numerical check values are unchanged.

This is an archived-output formatting defect, not a generator defect: the Python self-test writer uses json.dumps, and the successful EOS workflow generates a fresh temporary JSON and parses it before asserting the checks. No code or test was changed in this repair. It does not supersede the existing qualification that the separate default-filling-factor code patch and its new regression test have not yet been run through the full suite.

**Disposition of this addendum:** formatting-only repair verified by JSON.parse; no new physics or CI acceptance claim.
