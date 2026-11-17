# Fiftieth review: B.16 P1-C, P1-D and P1-E/P1-F source records

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 50ccd18538a9e35fad9786ce16f360ac223794dc  
Scope: six baseline documents, their linked scripts/JSON/profile metadata, and later B.2/P1-G/P1-H follow-ups used to adjudicate the claims.

## 1. Executive result

Six documents were individually reviewed. All six are classified PASS_WITH_NOTES. One substantive wording correction was made: P1-C previously stated too strongly that the scalar opacity inserted in B.2 is unambiguously the polarization-summed rate. The later Boltzmann state-counting audit establishes the B.6/B.7/B.10 sum convention, but B.2 itself does not specify whether its scalar exponent uses the sum, the three-state average, or an assumed polarization closure.

The review also found several source/output schema mismatches. Archived JSON values remain inspectable and have numerical cross-checks, but the currently committed drivers are not always schema-identical to the files presented as their outputs. These are provenance/reproducibility qualifications, not evidence that the archived numbers are wrong. The reports now state the distinction explicitly.

No production source, opacity, coupling, profile, luminosity curve, transport output, SN1987A limit, or axial-vector exclusion was modified.

## 2. Individual document outcomes

| Document | Outcome | Review finding |
|---|---|---|
| B16_P1C_POLARIZATION_NORMALIZATION_AND_GLOBAL_MODE_TRANSPORT_2026-11-10.md | PASS_WITH_NOTES | The B.14 210--510 MeV mode-resolved result is a valid restricted-band diagnostic. Corrected the over-strong statement that B.2 unambiguously inserts the polarization-summed opacity. The B.6/B.7/B.10 sum convention is clear; B.2's incident-state closure is not. Added comparison with the later exact-B.13 recoil-resolved band result and identified the V8 JSON/Python-driver schema mismatch. |
| B16_P1D_RMAX_BOUNDARY_SENSITIVITY_2026-11-10.md | PASS_WITH_NOTES | The source-frozen band scan closes at path orders 64/128 to a maximum relative change of 8.61e-6. The selected-band source fraction outside 15 km is 9.69e-7. Inward and outward scans are conditional band diagnostics, not full Fig. 7 reruns. The outward extension is opacity-only; P1-G/P1-H show the sharp 30 km near-match is not reproduced by smooth transport. Archived JSON and current Python-driver schemas differ. |
| B16_P1E2_B1_NEUTRINO_CHEMICAL_POTENTIAL_SOURCE_SENSITIVITY_2026-11-10.md | PASS_WITH_NOTES | The archived source-only result gives +0.1985%/-0.2096% for ±10% \(\mu_{\nu_\mu}\), below 0.66% for ±30%, +1.1737% for \(\mu_{\nu_\mu}=0\), and -1.1737% for the diagnostic \(\mu_{\nu_\tau}=\mu_{\nu_\mu}\). The pair kernel is even under sign reversal. Current JS payload and archived JSON schemas differ; no dedicated unit-test module is present. |
| B16_P1E3_INTERIOR_LAPSE_B1_SOURCE_SENSITIVITY_2026-11-10.md | PASS_WITH_NOTES | Matching the weak-end source would require a +6.03% lapse shift over 8--15 km or +4.97% over 5--15 km. This is not supported by the independent public lapse visualization. The deformation is a source-only diagnostic, not a self-consistent metric variation. Current JS payload and archived JSON schemas differ; no dedicated unit-test module is present. |
| B16_P1E_NEUTRINOSPHERE_AND_PROFILE_PROVENANCE_AUDIT_2026-11-10.md | PASS_WITH_NOTES | The 1687-row profile fingerprint and PDF source hashes/path indices are internally consistent. The profile is a public-figure vector-path reconstruction, not raw Garching data. Off-frame Caputo paths and the 24--25 km Schwarzschild lapse continuation remain explicit model assumptions. The current review checked metadata and extractor logic, not a fresh PDF extraction. |
| B16_P1F_ENERGY_DEPENDENT_NEUTRINOSPHERE_AND_HIGH_ENERGY_DAUGHTERS_2026-11-10.md | PASS_WITH_NOTES | Daughter kinematics and energy weighting are correct. P1-G/P1-H refine the sharp-boundary diagnostic: the smooth transport-only model changes the high-energy band by -0.33% to -10.60%, not -70.94%. This does not compute the heavy-flavor energy sphere. P1-F/P1-G/P1-H archived JSON and current driver schemas are not uniformly identical. |

## 3. Polarization normalization: the corrected interpretation

The 2026-11-13 Boltzmann state-counting audit establishes:

1. B.7's factor of three converts the polarization-averaged vacuum decay width into the polarization-summed thermal production rate.
2. Under the B.6 spin-sum convention, B.10 is sum-to-sum detailed balance; it does not insert another factor of three.
3. For a fixed propagating polarization, the physical no-mixing attenuation exponent uses that mode's \(\Gamma_{{\rm abs},h}^{*}\).
4. An equal-occupation scalar closure uses the arithmetic-average opacity \(\sum_h\Gamma_{{\rm abs},h}^{*}/3\).
5. B.2 writes one scalar \(\Gamma_{\rm abs}^{*}\) in its ray exponent but does not explicitly identify it as the sum, average, or shorthand for a polarization closure.

Therefore the literal B.2 implementation is retained for equation-level reproduction, while no-mixing and equal-occupation propagation remain separate physical lanes. The evidence does not establish a definite factor-of-three error by the paper's authors.

## 4. Exact-B.13 comparison and restricted-band scope

The archived P1-C B.14 result is \(6.615829\times10^{53}\) erg/s for the 210--510 MeV band, compared with the literal B.16 scalar band \(1.701785\times10^{52}\) erg/s (ratio 38.8758).

The later exact-B.13 moving-muon calculation independently closes the B.16 scalar band to \(1.01\times10^{-7}\). With both muon charges, it obtains:

- B.13 scalar-sum opacity: \(2.1001262\times10^{52}\) erg/s;
- B.13 independent mode-resolved transport: \(6.05812455\times10^{53}\) erg/s;
- mode-resolved/B.16 scalar band ratio: 35.5987;
- mode-resolved/B.13 scalar-sum ratio: 28.8465.

The exact-B.13 and B.14 mode weights applied to the same B.13 scalar Compton source differ by only 0.0024% in mode-resolved luminosity. The approximately 8.4% difference from the archived P1-C B.14 result is mainly the overall recoil-resolved Compton source/opacity, not the mode split.

The exact-B.13 result passes 42 local points at the 0.1% successive-order criterion, with maximum detailed-balance residual 1.10e-14. It remains restricted to 210--510 MeV. The full-band low-x extension is incomplete (seven of 24 planned pilot points); no full-band Fig. 7 or axial-vector result is accepted.

## 5. Boundary and daughter-neutrino interpretation

The P1-D boundary scan is numerically converged, but its outward rows add only vacuum-limit neutrino opacity outside 25 km while freezing the source and omitting outer Compton opacity. They are not self-consistent alternative supernova models.

P1-F correctly identifies the 105--255 MeV pair-mean daughter-energy range and the broad daughter spectrum. P1-G's figure-level exponential density tail estimates central radial transport radii of 22.37, 23.34, 24.62, and 26.23 km at 100, 150, 255, and 500 MeV. This is a transport-sphere proxy, not an energy-sphere calculation.

P1-H inserts the smooth pair-energy survival proxy into the 210--510 MeV B.2 ray integral. Its band changes are -0.33% (low tail), -4.14% (central tail), and -10.60% (high tail), compared with -70.94% for the sharp 30 km extension. Band-only total proxies remain +91.98%, +86.87%, and +78.21% above Fig. 7. The sharp-boundary near-match is therefore not a physical prediction within the tested smooth transport model.

Retain \(R_{\max}=25\) km as the literal paper baseline. A true energy-sphere treatment still requires same-snapshot heavy-flavor energy-changing collision kernels and neutrino moments.

## 6. Profile provenance

The active profile has 1687 rows and SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. profile_provenance.json records the Caputo SNProfile.pdf hash 19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e and Ferreira SNModelComparison.pdf hash 5cc8b07dad824b65391fae6229bb9eca138c1cf5ff0348c8aaf712779a2566f2, together with the vector path indices.

The extractor checks those hashes and reads the PDF vector paths, but the PDFs are external public arXiv archive members rather than committed raw data. The profile remains a public-figure reconstruction. The Caputo 20--25 km paths include off-frame vector data; the lapse from 24--25 km is a matched Schwarzschild continuation. The raw same-snapshot Garching hydro/neutrino arrays remain unavailable in this repository.

## 7. Artifact reproducibility qualifications

The following archived JSON/source pairs are not schema-identical in the current tree:

| Record | Current driver versus archived output |
|---|---|
| P1-C | Python driver defaults to a different output filename and emits profile/metrics_vs_fig7 fields, while the archived V8 JSON contains calculation/equation_normalization/source_closure/results. |
| P1-D | Python driver emits interpretation; archived JSON contains conclusions and outward_extension_consistency_note. |
| P1-E2 | JS driver emits resolution_checks/conclusion; archived JSON contains lower_resolution/higher_resolution/conclusions. |
| P1-E3 | JS driver uses a resolution_checks/conclusion payload; archived JSON uses lower_resolution/higher_resolution/conclusions. |
| P1-F | JS driver uses polarization_weights and high_energy_band_source_fraction fields; archived JSON uses mode_weights, polarization_sum and band_source_fraction. |
| P1-G | Current JS source input-field names differ from the archived JSON's inputs schema. |
| P1-H | The document already states that the Python driver is an independent implementation and was not the direct V8 producer; the V8 producer source is not archived. |

These mismatches do not invalidate the numerical records by themselves, but the exact producer version/invocation is not fully established. Do not describe the current scripts as exact producers of the archived JSONs. Future closure should either archive the producing source revision and invocation or regenerate separately named outputs from the current drivers and compare all numerical fields.

## 8. Final disposition

All six documents are PASS_WITH_NOTES. The P1-C B.2 wording was corrected; source/output provenance caveats were added; later exact-B.13 and P1-G/P1-H results were incorporated without changing the published scalar baseline.

No production physics output, B.2 baseline, \(R_{\max}=25\) km choice, coupling, Fig. 7 reference, SN1987A limit, or axial-vector constraint was modified. Continue the next batch from the next PENDING row in DOCUMENT_AUDIT_REGISTER.csv.
