# Fifty-seventh review: Bollig Fig. 4, outer profile, B.2 path integral, and Fig. 7 records

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: ff7da4a626f746b237209e3222a4d47143f0b65a  
Scope: six B.2/Bollig/Fig. 7 documents, their vector extraction outputs, current-profile fingerprints, and pinned numerical JSON.

## 1. Executive result

Six documents were reviewed individually: five PASS_WITH_NOTES and one HISTORICAL.

A numerical transcription error was found and corrected in the independent B.2 path-integral report. Its pinned JSON gives the 256-angle high-coupling luminosity \(2.43736510986799\times10^{52}\) erg/s and residual \(+92.24931\%\), not the older \(2.4373347089\times10^{52}\) erg/s and \(+92.24691\%\) quoted in the Markdown table. The JSON also gives a maximum difference \(1.2477\times10^{-5}\) against the archived three-layer baseline, not the \(2.22\times10^{-16}\) figure previously stated. The report now matches the pinned output.

The Ferreira/Caputo 5--15 km numerical comparison is marked HISTORICAL because its archived input profile SHA is older than the current profile B. The direct Bollig Fig. 4 vector check still selects Caputo as the \(\mu_\mu/T\) baseline, but its 97-node comparison statistics lack a separate comparison script/JSON and explicit profile fingerprint.

No source, opacity, profile, coupling, Fig. 7 reference, SN1987A limit, or axial-vector constraint was changed.

## 2. Individual document outcomes

| Document | Outcome | Main finding |
|---|---|---|
| BOLLIG_ORIGINAL_FIG4_MUON_DEGENERACY_CROSSCHECK_2026-11-09.md | PASS_WITH_NOTES | Bollig Fig. 4 vector extraction is checksum-pinned (222 points, path 193). The reported 97-node Caputo comparison is useful but has no separate comparison script/JSON or profile SHA. |
| BOLLIG_OUTER_THERMODYNAMIC_PROFILE_15_22KM_2026-11-09.md | PASS_WITH_NOTES | Current profile B and Bollig PDF are checksum-pinned. \(T\) and \(\mu_\mu/T\) agree over 15--20 km; 20--22 km has zero temperature support and only one endpoint degeneracy point, so no extrapolation is allowed. |
| EQ_B2_INDEPENDENT_PATH_INTEGRAL_AUDIT_2026-11-08.md | PASS_WITH_NOTES | Current profile B analytic path integration is independently converged against the reference path. Corrected the 256-angle luminosity/residual and the archived three-layer comparison metric to match the JSON. |
| FERREIRA_CAPUTO_MUON_PROFILE_PROVENANCE_AUDIT_2026-11-10.md | HISTORICAL | Its 5--15 km statistics use input SHA e41df78c..., whereas current profile B is 9fb14e79.... Preserve the old comparison as provenance only; direct Bollig Fig. 4 selects Caputo. |
| FIG7_10MEV_EQUATION_CHAIN_AUDIT_2026-11-07.md | PASS_WITH_NOTES | Local B.1/B.2 algebra, degeneracy identity, detailed balance and quadrature checks are consistent. These tests do not validate the physical nonrelativistic/no-recoil semi-Compton approximation; scalar B.2 polarization closure remains under-specified. |
| FIG7_10MEV_FOLLOWUP_DIAGNOSTIC_2026-11-08.md | PASS_WITH_NOTES | The joint source-radius/absorber-radius matrix is tied to current profile B. Its \(+35.97\%\) path-redshift result is grid-specific and must not be equated to the later \(+36.7448\%\) high-order diagnostic. |

## 3. Bollig Fig. 4 and outer profile provenance

The Bollig Fig. 4 source extraction is pinned to PDF SHA-256 8267f8b1de184163308728c44000425ce58085c1d5bd799d0cbc1e4e8d740d61, page index 2, path 193, with 222 extracted vector rows. The reported Caputo/Ferreira comparison over 97 profile nodes is not accompanied by a dedicated comparison script/JSON or an explicit input-profile SHA. It remains a documented comparison, not a fully reproducible numerical artifact.

The outer 15--22 km profile audit is stronger on provenance: it pins current profile B SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c and the same Bollig PDF SHA. It supports the \(T\) and \(\mu_\mu/T\) comparison through 15--20 km. There are no Fig. 1 temperature points in 20--22 km and only one endpoint Fig. 4 degeneracy point. This is a support boundary, not a reason to extrapolate.

The separate Ferreira/Caputo audit JSON records input SHA-256 e41df78c8035540760fbcb7ef592cd830171822e, which differs from current profile B. Its 77.26% radius-weighted and 82.98% node-mean profile differences remain valid only for that older input. The qualitative choice of Caputo is supported by the direct Bollig Fig. 4 check, but the old numerical averages are not current profile-B statistics.

## 4. Independent B.2 path-integral numerical correction

The pinned JSON records current profile B SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c and code SHA-256 84b1960eae74d15d6c1ad9a0bb23feb51ff26b28eb031134e839a6b4986e5a1e. The analytic path integral is exact for the same piecewise-linear radial opacity interpolant. It independently checks path-coordinate quadrature, not the local opacity model or its physical completeness.

The corrected angular table is:

| Angular order | Mean absolute Fig. 7 residual | 10 MeV strong-endpoint residual |
|---:|---:|---:|
| 16 | 15.7332% | 92.2489% |
| 64 | 15.7326% | 92.2493% |
| 128 | 15.7327% | 92.2493% |
| 256 | 15.7327% | 92.2493% |

The archived three-layer baseline comparison has maximum relative difference \(1.2477\times10^{-5}\) and mean \(5.0990\times10^{-6}\). The previous \(2.22\times10^{-16}\) Markdown value was not supported by the pinned JSON. The corrected 256-angle result remains a numerical diagnostic; it does not replace the fixed-\(\omega\) B.2 baseline or resolve the \(+92\%\) physical mismatch.

## 5. Fig. 7 equation-chain and follow-up scope

The equation-chain audit checks the B.1 phase-space Jacobian, \(n_\mu F_{\rm deg}=T\,\partial n_\mu/\partial\mu_\mu\), reduced absorption detailed balance, and path/angular quadrature. It does not establish the physical accuracy of the nonrelativistic/no-recoil semi-Compton kernel. The later P1-C result also clarifies that B.6/B.7/B.10 establish sum-to-sum local rates, while the scalar \(\Gamma_{\rm abs}^{*}\) in the B.2 exponent is not explicitly identified as a polarization sum, three-state average, or separate closure.

The follow-up matrix distinguishes optically thin source weights, source-weighted optical depths, and escaped-luminosity shell fractions. Its \(+35.97\%\) conserved-\(E_\infty\) residual is tied to its 88-radial/180-energy/24-angle/64-path configuration. The later \(+36.7448\%\) value is a separate higher-order diagnostic, not a same-grid disagreement. Neither path-redshift value is selected as a correction to the published fixed-\(\omega\) prescription.

The full-band low-x prerequisite remains open; the later exact-B.13 calculation covers 210--510 MeV only. No full-band Fig. 7 or axial-vector result follows from these documents.

## 6. Disposition

Five documents are PASS_WITH_NOTES and one older-profile comparison is HISTORICAL. The direct Bollig Fig. 4 source favors Caputo; the 15--20 km thermodynamic profile is cross-checked; the 20--22 km interval remains unsupported; the B.2 path-integral report now matches its JSON; and the full-band low-x/physical Fig. 7 gates remain open.

No production profile, source, opacity, coupling, Fig. 7 reference, SN1987A limit, or axial-vector constraint is modified.
