# Fifty-eighth review: 10 MeV Fig. 7 local rates, three-layer transport, Compton method, digitization, and redshift records

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: f643113e973c79ed383f9713d16d6110d3a92e63  
Scope: six pending Fig. 7 documents, linked source/tests/JSON/workflows, current profile fingerprint, and the 56th/57th review qualifications.

## 1. Executive result

Six documents were reviewed individually: three PASS_WITH_NOTES, one REVISION_REQUIRED, and two HISTORICAL.

The most important correction is that the scalar attenuation rate in Eq. (B.2) is not unambiguously specified as a polarization sum. B.6/B.7/B.10 establish the local summed-rate convention, but B.2 itself inserts one scalar \(\Gamma_{\rm abs}^{*}\) without identifying it as a sum, three-state average, or polarization closure. The local-rate and vector-benchmark reports now reflect this.

The local-rate/polarization report remains REVISION_REQUIRED because it claims a self-contained addendum (script, CSV, JSON, plot, pinned inputs, helper source and tests) but none of those artifacts is present in the reviewed repository tree. Its numerical results cannot be independently regenerated from the checked-in repository.

The three-layer and flavor-resolved fixed-\(\omega\)/redshift records are HISTORICAL because their archived outputs use the older profile-A SHA 08d7afce..., whereas current profile B is 9fb14e79.... The digitization geometry audit and the 256-angle path-integral audit provide stronger current reference checks, but neither is a new profile-B three-layer or full flavor-resolved rerun.

No production source, opacity, coupling, profile, Fig. 7 reference vertices, luminosity curve, SN1987A limit, or axial-vector constraint was changed.

## 2. Individual document outcomes

| Document | Outcome | Findings |
|---|---|---|
| FIG7_10MEV_LOCAL_RATE_POLARIZATION_ESCAPE_AUDIT_2026-11-13.md | REVISION_REQUIRED | Corrected the over-strong claim that B.2 necessarily exponentiates the polarization-summed opacity. The reported high-order local calculation is not independently reproducible from the current repository: the claimed addendum script, selected-node CSV, JSON, plot, pinned-input manifest, and helper source are absent. Its 32-direction result is 0.0932% above the later 256-angle path-integral value; preserve the grid distinction. |
| FIG7_10MEV_THREE_LAYER_AUDIT_2026-11-07.md | HISTORICAL | The committed JSON is internally consistent with the report and has four regression tests plus successful workflow run #42310090478. However, its JSON uses profile SHA 08d7afce... (profile A), not current profile B 9fb14e79...; retain as profile-A channel-decomposition evidence only. |
| FIG7_COMPTON_BASELINE_METHOD_AUDIT_2026-11-09.md | PASS_WITH_NOTES | B.14--B.19 are correctly identified as the published no-recoil/nonrelativistic-muon Fig. 7 approximation, while B.13 is the general moving-muon expression and a separate correction study. This does not prove the approximation's physical accuracy at 10 MeV; the consistent global B.13 replacement increases the strong-endpoint residual. |
| FIG7_DIGITIZATION_AUDIT_2026-11-08.md | PASS_WITH_NOTES | The PDF hash, native path, axis calibration, and visible 25-point 10 MeV curve are corroborated by the later six-curve geometry audit. The high-\(g\) drop is present in the original vector path; the figure still does not expose author-side numerical samples. |
| FIG7_VECTOR_BENCHMARK_REEVALUATION_2026-11-09.md | PASS_WITH_NOTES | The current profile-B source/escape analysis remains useful and the benchmark remains unvalidated. Corrected the claim that B.2 uniquely mandates a polarization-summed scalar exponent; clarified grid-specific luminosity values and the restricted 210--510 MeV B.13 scope. |
| FLAVOUR_RESOLVED_FIXED_OMEGA_VS_REDSHIFT_2026-11-08.md | HISTORICAL | Driver, four tests, workflow and JSON exist, but the JSON is pinned to old profile A (08d7afce...). Its Euclidean-chord path-redshift comparison is a historical sensitivity diagnostic, not a full GR ray trace or current profile-B result. |

## 3. Polarization and B.2 interpretation

The 2026-11-13 Boltzmann state-counting audit and the 56th/57th review reports establish the correct separation:

1. B.7 converts the polarization-averaged vacuum decay width into the thermal production sum.
2. Under the B.6 spin-sum convention, B.10 is sum-to-sum detailed balance; it adds no further factor of three.
3. A no-mixing mode calculation propagates each mode with its own \(\Gamma_{{\rm abs},h}^{*}\).
4. An equal-occupation closure uses the arithmetic-average opacity \(\sum_h\Gamma_{{\rm abs},h}^{*}/3\).
5. B.2 writes one scalar \(\Gamma_{\rm abs}^{*}\) in its ray exponent but does not specify which of these closures it denotes.

Therefore, retain the literal scalar B.2 code as the equation-level reproduction lane, but do not claim that the paper unambiguously mandates a polarization-summed exponent or that a factor-of-three error has been demonstrated.

## 4. Local-rate report: numerical and provenance boundary

The local-rate report quotes \(L_{\rm calc}=2.439635957\times10^{52}\) erg/s for a 32-direction/64-path configuration. The later independent 256-angle path-integral result is \(2.43736510986799\times10^{52}\) erg/s; the difference is \(+0.09317\%\). The values are close but configuration-specific.

More importantly, the current Git tree contains no artifact corresponding to the report's claimed localization addendum. The missing source/output bundle prevents independent reproduction of its local-rate residuals, source fractions, optical-depth statistics, mode-resolved luminosity, and escape fraction. These numbers are not promoted to verified current repository outputs until the exact producer, inputs, invocation and tests are committed.

## 5. Historical profile-A calculations

The three-layer JSON records profile SHA 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9, Fig. 7 comparison JSON SHA 6ec153f4bc0acbc1fdcdcc6b7855cfc980a61e440e858ea571d06923823de0a2, and (40,100,16,32) quadrature. Its 92.2382% strong-endpoint residual is a historical profile-A result, not a profile-B result. The four regression tests and successful workflow #42310090478 validate the software bookkeeping for that run, not its applicability to the current profile.

The flavor-resolved fixed-\(\omega\)/redshift JSON also records profile SHA 08d7afce.... Its shell ratios and luminosity-removal factors remain useful historical diagnostics, but a current-profile replacement would require rerunning the same full flavor-resolved decomposition against profile B. The path-redshift calculation retains Euclidean \(ds\), so it is not a full GR ray trace.

## 6. Compton approximation and Fig. 7 digitization

The B.14--B.19 implementation is the correct literal published-approximation lane for reproducing the paper's stated Fig. 7 calculation. The general B.13 expression is retained as a separate moving-muon/recoil correction study. The consistent global B.13 source-plus-opacity replacement gives a larger strong-endpoint residual (about +131.53%), so it does not validate or replace B.16.

The source-PDF digitization is well supported. The geometry audit pins the arXiv v2 PDF SHA 4d7d1d10..., checks all six native vector paths and axis tick coordinates, and reconstructs the archived 25-point 10 MeV curve. The high-\(g\) tail is not explained by a curve-swap, sorting, duplicate-\(x\), or visible-frame clipping error. This still does not provide the authors' unplotted simulation samples.

## 7. Current disposition

- Keep the B.14--B.19 literal approximation as the Fig. 7 reference implementation; keep B.13 as a separate correction study.
- Keep fixed-\(\omega\) Eq. (B.2) as the literal equation-level path lane; keep path-redshift as a separate diagnostic.
- Keep the 25-point Fig. 7 reference vertices and \(R_{\max}=25\) km unchanged.
- Do not claim that the scalar B.2 exponent is unambiguously polarization-summed.
- Do not treat profile-A three-layer or flavor-resolved outputs as current profile-B evidence.
- Do not declare the pure-vector Fig. 7 benchmark validated or update the axial-vector cooling curve.
- Require the missing local-rate addendum before closing that document's reproducibility review.

No production profile, source, opacity, coupling, luminosity curve, manuscript, referee response, SN1987A limit, or axial-vector constraint is changed.
