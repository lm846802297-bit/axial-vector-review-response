# Fifty-first review: B.16 P1-G/P1-H and P1-IIId composition/source records

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 5f0777ab01d9fd491b7b73ebe9c40740b941eecd  
Scope: six baseline documents, their linked scripts, outputs, source PDFs, and historical workflow evidence.

## 1. Executive result

Six documents were individually reviewed. Five are PASS_WITH_NOTES and one is HISTORICAL. The transport-only interpretation of P1-G/P1-H is internally consistent but must not be promoted to an energy-sphere calculation. The Caputo composition bookkeeping and Esseili-Kribs native-vector comparison are numerically supported within published-figure uncertainty. The initial Fig. 12 page-render report is superseded by the later native-vector extraction and is now explicitly marked HISTORICAL.

A provenance qualification was added to the Caputo composition report: the 18 km row is present in a separate extended key-radii CSV, while the currently linked 301-row extractor output and JSON stop at 15.2 km. The 18 km value remains archived evidence but is not claimed to be produced by the current extraction script.

No EOS table, density profile, collision kernel, B.2 opacity, coupling, luminosity curve, SN1987A limit, or axial-vector exclusion was modified.

## 2. Individual document outcomes

| Document | Outcome | Findings |
|---|---|---|
| B16_P1G_PUBLIC_DENSITY_NEUTRINO_TRANSPORT_ENVELOPE_2026-11-10.md | PASS_WITH_NOTES | The exponential density-tail integral is dimensionally consistent and the central \(\tau=2/3\) radii follow from the stated mean-free-path scaling. The result is a figure-level radial transport proxy, not an energy sphere. Current JS input schema differs from the archived JSON. |
| B16_P1H_GARCHING_ARCHIVE_ACCESS_AND_DATA_REQUIREMENTS_2026-11-10.md | PASS_WITH_NOTES | The official archive index and required data categories are clearly identified. HTTP 401 is a date-specific 2026-11-10 observation, not a claim about current availability or exact snapshot identity. No protected data or credentials were obtained. |
| B16_P1H_SMOOTH_DAUGHTER_REPROCESSING_B2_2026-11-10.md | PASS_WITH_NOTES | Smooth-tail band changes (-0.33%, -4.14%, -10.60%) are far smaller than the sharp 30 km extension (-70.94%). The output remains a band-only transport proxy. The direct V8 producer is not archived; the current Python driver is explicitly independent and schema-different. |
| B16_P1IIID_CAPUTO_COMPOSITION_CLOSURE_2026-11-11.md | PASS_WITH_NOTES | The 301-row composition CSV and JSON cross-figure closure reproduce to floating-point precision. The 18 km row is supported by a separate key-radii CSV, but that extended file has no current producer script; the current common-support extraction stops at 15.2 km. |
| B16_P1IIID_CROSS_PAPER_SOURCE_DEPENDENCE_AUDIT_2026-11-11.md | PASS_WITH_NOTES | Native PDF-vector extraction, source SHA, path indices, and numerical residuals were verified. Caputo and Esseili-Kribs are a shared-Garching model-lineage comparison, not independent hydrodynamic simulations. Residuals are below figure-level stroke uncertainty. |
| B16_P1IIID_FIG12_PDF_PAGE_RENDER_AUDIT_2026-11-11.md | HISTORICAL | Its qualitative-only status is superseded by the checksum-pinned native-vector extraction and numerical cross-check. The page render remains provenance, not current evidence. |

## 3. P1-G/P1-H transport interpretation

For the central public-density tail, the approximate radial \(\tau_{\nu N}=2/3\) radii are 22.37, 23.34, 24.62, and 26.23 km for daughter energies 100, 150, 255, and 500 MeV. The pair-mean daughter energy is \(\omega/2=105\)--255 MeV over the selected vector band. The central-tail pair-energy survival spans approximately 0.47--0.84 at 25 km, 0.90--0.98 at 27.5 km, and 0.986--0.997 at 30 km.

The radial 25--30 km reprocessing fraction is an unweighted diagnostic, not a source- and angle-weighted B.2 optical-depth integral. The smooth P1-H B.2 band integration gives:

- low tail: -0.33% band change, band-only total proxy +91.98% above Fig. 7;
- central tail: -4.14% band change, band-only total proxy +86.87%;
- high tail: -10.60% band change, band-only total proxy +78.21%.

The sharp P1-D 30 km extension gives -70.94% and a band-only proxy 2.79% below Fig. 7. The smooth transport model does not reproduce this near-match. It therefore cannot be used to select 30 km as a physical boundary. Keep the literal 25 km paper baseline.

These calculations still do not determine the heavy-flavor energy sphere. The density tail is read from a public figure, the mean-free-path model is approximate, and the treatment omits energy-changing pair kernels, angular transport, degeneracy, correlations, recoil, and weak magnetism.

## 4. Garching archive access

The archive index identifies collections for neutrino signals, radial neutrino moments/spectral data/hydro profiles, hydro profiles, trajectories, and progenitor data. The two relevant Bollig2016 endpoints returned HTTP 401 in the 2026-11-10 check. This is a dated access observation only. It does not prove that the exact s18.8-SFHo-MUONS, \(t_{\rm pb}=1\) s snapshot is present in every linked collection or that access remains unchanged today.

A defensible energy-sphere calculation still needs the same-snapshot hydrodynamic background, heavy-flavor neutrino distributions or sufficient moments/closure, energy- and flavor-dependent scattering/absorption/emission/pair kernels, and metadata for model, time, coordinate, frame, species, and units.

## 5. Caputo composition closure

The current extraction script reads checksum-pinned Caputo PDF vector paths and outputs a 301-point common-support profile over 0.2--15.2 km. Recomputing the metrics from that CSV gives:

- \(Y_p^{\rm Fig4}\) versus \(n_p^{\rm Fig1}/n_B^{\rm Fig1}\): 0.0320205% RMS relative, 0.084956% maximum absolute;
- \(Y_e+Y_\mu\) versus \((n_e+n_\mu)/n_B\): 0.107404% RMS relative, 0.264299% maximum absolute;
- cluster-charge absolute difference: \(1.61510\times10^{-4}\) RMS and \(4.12567\times10^{-4}\) maximum per baryon.

The 18 km table row is present in caputo_composition_key_radii_2026-11-11.csv, together with 16 and 20 km rows. However, the currently linked extractor writes only the 0.2--15.2 km common-support profile, and its JSON explicitly records that range. No current checked-in script writes the extended key-radii CSV. The 18 km row is retained as a separate archived vector-derived datum, not as output of the current 301-row run. The document now states this boundary; exact producer/invocation provenance should be added before claiming reproducibility beyond 15.2 km.

The physical bookkeeping remains:
\[
X_{\rm cl}=1-Y_n-Y_p,\qquad
Y_Q^{\rm cl}=Y_e+Y_\mu-Y_p,
\]
\[
n_n^{\rm free}=Y_n n_B,\qquad n_p^{\rm free}=Y_p n_B.
\]
Do not infer \(n_n^{\rm free}=n_B-n_p^{\rm free}\).

## 6. Esseili-Kribs Fig. 12 cross-publication check

The checksum-pinned SCOAP3 APS PDF has SHA-256 c3b92fe6cf2a8bd3fec84925e2baababfe0c707327a68135013f953ed3d87d43 (2,749,668 bytes). Native paths 25, 181, and 182 identify SFHo-18.8 temperature, neutron, and proton; the workflow verifies the PDF checksum before extraction. Historical run #42955259591 succeeded on the research branch at SHA 014e80889095e846357dc5e02e5c4070b7c45faf.

The numerical summary gives 0.0707% RMS for E-K temperature versus Caputo over 55 radii, 0.0953% RMS versus Bollig over 391 radii, and 0.580%/0.586% RMS for E-K neutron/proton versus Caputo reconstructed free nucleons over ten radii. Their sum agrees with Caputo free baryons at 0.574% RMS. The corrected log-density-axis calibration is selected by equal tick spacing and same-model composition consistency; the literal alternative is about ten times too high. The upper glyphs remain visually ambiguous, so no definite typesetting error is asserted.

These are published-figure vector comparisons within the same Garching model lineage. They are not independent simulation validation, and their sub-percent residuals are smaller than the estimated line-stroke uncertainty (about 4.9% in density).

## 7. Reproducibility qualifications

- P1-G's current JavaScript driver uses figure_read_off_central / figure_read_off_stress_envelope input fields, while the archived JSON uses nB20_over_n0_central / H_km_central / stress_envelope. The current driver is not schema-identical to the archived producer.
- P1-H's archived result is a direct V8 calculation. The checked-in Python implementation returns configuration/closures/baseline fields, while the archived JSON uses method/numerical_closure/conclusions. The document already states that the Python rerun is not claimed.
- The extended Caputo composition key-radii CSV contains 16/18/20 km values but has no current producer script; the 301-row common-support extraction is only 0.2--15.2 km.
- The native Fig. 12 vector extraction and cross-check scripts are present and the associated workflow verifies the exact PDF SHA. Its successful run is historical research-branch evidence, not CI on maintenance PR #115.

## 8. Disposition

Five documents are PASS_WITH_NOTES and the initial PDF-page render report is HISTORICAL. The P1-G/P1-H results remain conditional transport proxies; the 25 km baseline remains unchanged; Caputo cluster bookkeeping is retained with the extended-radius provenance caveat; and the E-K comparison is described as cross-publication consistency within a shared Garching model lineage.

No production profile, EOS input, collision kernel, B.2 opacity, coupling, luminosity curve, SN1987A limit, or axial-vector constraint is modified.
