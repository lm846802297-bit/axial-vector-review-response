# Pure-vector Fig. 7 benchmark: final acceptance gate (2026-11-09)

## Executive decision

**The numerical implementation checks pass, but the physical reproduction of the published Fig. 7 curve does not pass.** The 10 MeV fixed-\(\omega\), B.16 working benchmark on the current vertex-preserving profile B remains 92.2406% above the digitized strong-coupling endpoint. The path-redshift-only diagnostic reduces this to 36.7448%, but it is not the literal Appendix-B baseline and is not a full GR calculation.

No axial-vector curve is recalculated or updated. PR #57 remains Open / Draft.

## 1. Acceptance matrix

| Stage | Result | Evidence | Acceptance |
|---|---|---|---|
| B.1 independent optically-thin source | Independent radial/energy integration; source differs from the original implementation by -0.4430% | 400 radial nodes, 960 energy nodes per radius; energy lower limit (m_V/N(r)) | Numerical pass |
| B.2 independent propagation | Independent path-column integration and closure | Fixed-\(\omega\) Appendix-B prescription; independent path quadrature | Numerical pass |
| B.1+B.2 end-to-end | Independent source and path modules reproduce the stored B.16 calculation with mean absolute difference 0.3975% and maximum 0.4451% | 25 Fig. 7 coupling points; radial refinement changes the curve by at most 0.1987% | Internal reproduction pass |
| Local collision kernels | Full 64,000-point radius--energy grid checked | B.6, B.10, B.17 and B.16 residuals at or below the archived (10^{-13}) scale; angular-order and sign checks pass | Numerical pass |
| Fig. 7 physical comparison | Strong-endpoint residual remains +92.2406% for the fixed-\(\omega\) B.16 working benchmark | Current profile B; 25 coupling points | **Not passed** |
| Energy/GR convention | B.1 local-energy and E_infinity forms shown numerically equivalent; B.2 path-energy interpretation remains isolated | Independent local-vs-infinity B.1 quadrature and B.2 literal/path-redshift comparison | B.1 resolved; B.2 implementation convention remains a paper-level ambiguity |
| Stellar-background fidelity | Caputo (T(r)) and (mu_\mu/T) supported by direct Bollig figure comparisons; outer profile remains figure-derived | Original Bollig Figs. 1, 3 and 4 cross-checks; 20--25 km continuation not fully source-validated | Partial |

## 2. Current 10 MeV Fig. 7 residuals

The current profile is vertex-preserving profile B:

`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`

| Fig. 7 point | Fixed-\(\omega\), B.16 working benchmark | Path-redshift-only diagnostic |
|---|---:|---:|
| Weak endpoint | -8.8853% | -8.8991% |
| Reference peak | +2.5688% | -2.7704% |
| Strong endpoint | +92.2406% | +36.7448% |
| Mean absolute residual over 25 points | 15.7320% | 9.2163% |

The path-redshift-only calculation uses the conserved energy at infinity to update the local energy and local vector speed along the ray, but retains the Euclidean chord measure. It is a sensitivity diagnostic, not a full GR ray calculation and not a replacement for the literal fixed-\(\omega\) Appendix-B baseline.

Machine-readable current-profile output:
`outputs/b16_global_redshift_audit_2026-11-09.json`

Successful workflow:
[Run #42568420651](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42568420651).

## 3. What the background audit has established

### 3.1 Muon chemical potential

The direct original Bollig Fig. 4 comparison selects the Caputo \\(\mu_\mu/T\\) profile over the Ferreira digitization:

- Caputo: mean relative difference 0.00518%, maximum 0.01434%;
- Ferreira: mean relative difference 12.74%, maximum 17.18% in the directly compared 12--15 km interval.

The Ferreira substitution is retained only as an off-baseline sensitivity diagnostic. It is not an admissible correction to the current SFHo-18.8, 1 s benchmark.

### 3.2 Absolute muon density

Caputo's (n_\mu) is internally consistent with its relativistic Fermi integral. Bollig Fig. 3 is lower by about 5% on average over 5--15 km and about 8.8% over 12--15 km.

This difference is not a license to rescale the Compton rate: the B.17 combination (n_\mu F_{\rm deg}) is the susceptibility determined by the same (T,\mu_\mu) distribution. A density-only rescaling would break that relation.

### 3.3 Outer thermodynamic profile

The original Bollig figure paths do not fully resolve the 20--25 km continuation. Existing stress tests show:

- a ±10% temperature change over 20--22 km changes the strong-endpoint luminosity by only about ±0.15%;
- a ±30% temperature change over 22--25 km changes it by approximately -3.6% to +12.5%;
- the tested outer muon-neutrino chemical-potential floor changes are negligible.

These tests quantify sensitivity; they do not establish the true outer profile. No profile is adjusted to improve Fig. 7 agreement.

### 3.4 Lapse and spatial geometry

The lapse (N(r)) has an independent visual cross-check over 0--20 km against the SFHo-18.8 profile slide in Zuowei Liu's 2026-10-31 presentation (slide 65). This is not a machine-precision metric table.

The important distinction is that Blinov's published Appendix-B baseline uses N(r) in B.1 but uses Euclidean straight chords in B.2; it does not require A(r) or M(r). The absence of A(r) limits a full-GR extension, not reproduction of the published approximation. See [B16_PUBLISHED_GRAVITY_AND_ENERGY_PRESCRIPTION_RECONSTRUCTION_2026-11-09.md](B16_PUBLISHED_GRAVITY_AND_ENERGY_PRESCRIPTION_RECONSTRUCTION_2026-11-09.md).

## 4. Published-prescription boundary

The version-of-record paper, Blinov et al., JHEP 06 (2026) 155, presents:

- a main-text description of \(\omega\) as energy at spatial infinity;
- an Appendix-B.1 source integral whose lower limit (m_V/N(r)) and (N(r)^2) factor imply a local source-energy variable;
- a literal Appendix-B.2 optical-depth expression with the same \(\omega\) along the chord;
- a formal Compton phase-space rate B.13 and the reduced expressions B.14--B.16.

The article does not deposit its numerical code or associated data, and the Fig. 7 discussion does not unambiguously identify which Compton implementation was used in the unpublished numerical code. The current project retains B.16 as the operational working benchmark and B.13 as a separate alternative; it does not claim to know the authors' exact implementation.

The source-level convention and implementation ambiguity is documented in:
`B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md`.

## 5. What remains, and what does not

### Completed; do not repeat

1. Independent B.1 source integration.
2. Independent B.2 path integration and end-to-end B.1+B.2 closure.
3. Dense local collision-kernel checks on the full integration grid.
4. Caputo-versus-Ferreira \(\mu_\mu/T\) adjudication against Bollig Fig. 4.
5. Current-profile redshift-only diagnostic and archival.
6. Source-weighted muon-velocity diagnostic for the B.14 non-relativistic approximation.
7. Inner and outer \(\mu_{\nu_\mu}\) branch/plot-floor sensitivity tests.
8. B.1 source/background audit to the limit of public figure data: B.17's one-\(\mu^-\)-species \(n_\mu F_{\rm deg}\) product is independently checked; the Fig. 3 density discrepancy is not explained by the \(\mu^+\) fraction and is not a permitted standalone normalization; the density-only source-weighted estimate is about 1% over 5--15 km.
9. Strong-endpoint emission-radius decomposition: 8--15 km supplies 79.61% of the thin source and 86.84% of the escaped luminosity; 22--25 km emission supplies 0.073% and 3.36%, respectively. Fig. 7 itself contains no radius-resolved reference distribution.
10. The 10 MeV global B.13 source-plus-opacity alternative and its radial/energy/angular/path convergence scans. The combined \(60\times140\times24\times48\) grid changes the B.13 luminosity curve by at most 0.2732% relative to \(40\times100\times16\times32\); the strong-endpoint residual changes from \(+131.53\%\) to approximately \(+131.12\%\). The full artifact upload hit the Actions storage quota, so the compact recovered scan summary is the archived numerical record. B.13 is a separate moving-muon alternative, not the operational Fig. 7 benchmark. The 0.1 and 1 MeV global outputs remain baseline-grid comparisons and are not described here as independently grid-converged.
11. P1 high-energy B.2 propagation audit: direct \(s\)-coordinate integration agrees with the analytic radial primitive at \(\leq8.3\times10^{-14}\) for four-point path quadrature across 108 rays; Simpson/Gauss angular averages agree below \(6\times10^{-7}\); using all 1687 retained profile vertices rather than the 642-node opacity grid changes sampled total optical depths by at most \(1.87\times10^{-5}\). A separate 36-ray fixed-\(\omega\)/path-redshift comparison shows that the redshift sensitivity is carried by neutrino inverse-decay opacity, with negligible semi-Compton change. See [B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md](B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md).
12. Source-weighted global Shapley attribution of the 210--510 MeV path-redshift sensitivity: 99.9860% of the global luminosity change is due to neutrino inverse-decay opacity and 0.0140% to semi-Compton opacity. The four counterfactual luminosities reproduce the archived fixed-\(\omega\) and bilinear-redshift band results at \(2.84\times10^{-6}\) and \(4.09\times10^{-7}\) relative residuals, respectively. A direct local-rate evaluation differs from the bilinear redshift result by 0.50% but preserves the channel attribution.
13. P1-B.2 thermodynamic interpolation and source-frozen input sensitivity: direct local-kernel evaluation from the 1687-vertex profile versus the 642-node opacity table changes sampled total optical depths by at most \(9.07\times10^{-6}\). In the source-frozen 210--510 MeV band, \(\pm10\%\) variations of \(\mu_{\nu_\mu}\) change the escaped luminosity by less than \(0.03\%\), while \(\pm10\%\) \(T\) or \(\mu_\mu\) stress tests produce larger changes through semi-Compton opacity. The baseline \(T\) and \(\mu_\mu/T\) profiles independently match Bollig Figs. 1 and 4 at the \(10^{-4}\) relative scale. See [B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md](B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md).


### Still unresolved

1. The exact same-snapshot Garching thermodynamic profile remains unavailable. The public-figure reconstruction is internally consistent for the validated \(T\) and \(\mu_\mu/T\) ranges, but the Bollig Fig. 3 absolute-density tension remains unresolved at the raw-profile level. The 20--25 km continuation is also not directly validated by the original Bollig Fig. 1/Fig. 4 frames.
2. The unpublished Fig. 7 numerical code is unavailable. The text supports B.14 in the low-mass Compton regime, but does not identify the Compton implementation for every plotted mass point. B.16 remains the adopted equation-level reproduction benchmark; B.13 remains a separately completed alternative.
3. The displayed B.2 equation uses fixed \(\omega\), which remains the literal reproduction baseline. The path-redshift alternative is a separately quantified physical sensitivity; the unpublished numerical code is unavailable, so its exact implementation cannot be independently inferred.
4. The B.16 physical reproduction still fails at the 10 MeV strong endpoint: \(+92.2406\%\) for fixed \(\omega\). The path-redshift-only diagnostic gives \(+36.7448\%\), but is not the literal published baseline.
5. The scalar versus polarization-resolved interpretation of the B.2 absorption rate remains a separate transport-prescription question; the mode-resolved result is not silently substituted for the published scalar baseline.
6. A same-snapshot spatial metric \(A(r)\) or enclosed mass \(M(r)\) is needed only for an optional full-GR extension, not for the published Euclidean-chord B.2 approximation.

The protected Garching endpoint limits raw-profile precision. This does not prevent the method-level B.1--B.5 checks using the current public-profile reconstruction, but it prevents claiming exact reproduction of the original simulation background.


## 6. Final gate decision

- **Numerical modules:** pass.
- **Current public-profile reconstruction:** internally consistent for the validated (T) and (mu_\mu/T) ranges, but incomplete in the outer profile and metric.
- **Pure-vector Fig. 7 reproduction:** not passed.
- **Axial-vector recalculation:** frozen.
- **PR #57:** keep Open / Draft; do not merge as a validated reproduction.

The P1-B.2 thermodynamic interpolation audit and the subsequent P1-C polarization-normalization audit are complete. The scalar Appendix-B normalization is retained as the literal baseline; the mode-resolved diagnostic is not substituted and no factor-of-three rescaling is authorized. P1-D has quantified the source-frozen 25--30 km boundary sensitivity. P1-E1--E3 have completed the outer-lapse, neutrino-chemical-potential, and interior-lapse source tests. P1-F has derived the high-energy daughter-neutrino spectrum and identified the energy-dependent heavy-flavor energy sphere as the relevant missing physics. P1-G has used the same-snapshot public Caputo Fig. 1 density curve through 20 km to estimate a transport-only outer-tail envelope: the central radial \(\tau_{\nu N}=2/3\) radius is about 24.6 km at 255 MeV and 26.2 km at 500 MeV. The smooth central-tail 25--30 km reprocessing fraction is only 8.91% on an unweighted radial/node average, so the full P1-D 30 km vacuum-opacity extension remains an extreme upper bound.

Do not repeat generic radial/path interpolation, broad profile stress tests, or full-opacity boundary scans. The actual heavy-flavor energy sphere cannot be computed without same-snapshot energy-changing neutrino collision kernels and moments. Retain the literal \(R_{\max}=25\) km, fixed-\(\omega\), scalar B.2 baseline; keep all axial-vector outputs unchanged.


## 7. Official data and metric-source availability

The official Garching archive index lists the relevant Bollig/Hüdepohl radial hydro and neutrino profiles and separately lists Robert Bollig's Python TOV solver (2020). Direct checks of the radial-profile and TOV-solver endpoints return HTTP 401 Unauthorized; the archive index states that some collections are password protected. A recent independent SFHo-18.8 analysis, arXiv:2610.35379, also points to this same archive for its full simulation profiles rather than providing an independent raw-data mirror.

Consequently, the exact same-snapshot hydro table remains unavailable through the checked unauthenticated endpoints. The spatial metric A(r) or M(r) is also unavailable, but this is a limitation only for a full-GR extension: the published B.1--B.2 reproduction prescription uses the lapse in the source term and Euclidean chords in the path integral. Do not infer A(r) from the lapse alone, use a generic TOV solver as a substitute for the time-dependent snapshot, or splice another progenitor/time profile.

Detailed endpoint and source audit:
[B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md](B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md).


Three-mass B.13 source/opacity and local convergence audit: [B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md](B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md).


## 7. Source-language qualification: what the published text does and does not prove (2026-11-10)

A cross-check against the version-of-record wording requires a narrower statement than the earlier categorical wording in the separate method note.

The paragraph following Fig. 7 explicitly invokes Eq. (B.14) for the **low-mass Compton absorption regime** and its mass-independent (m_V\to0) behavior. This is direct evidence that the authors use the B.14 approximation to interpret that low-mass regime. It does not, by itself, explicitly state that every Fig. 7 mass point is evaluated with B.14--B.19, nor does it expose the unpublished numerical implementation line by line.

For (m_V=10\,\mathrm{MeV}), the paper states that inverse neutrino decay dominates trapping above the MeV scale. This makes the B.14--B.19 implementation the natural operational benchmark for the published calculation, while the exact B.13 kernel is a controlled relativistic correction study. Nevertheless, because the code is unavailable and the text does not explicitly label the Compton implementation for each Fig. 7 mass, the strongest defensible provenance statement is:

- B.14--B.19 is the adopted equation-level reproduction prescription for the published Appendix-B approximation and the operational Fig. 7 benchmark;
- B.13 is the general phase-space expression and its global replacement is an alternative calculation, not a required Fig. 7 convergence target;
- the article does not let us prove the exact code path used at every plotted mass point.

This qualification does not change any numerical result. The current B.16 fixed-ω benchmark remains the correct working branch to compare with Fig. 7 under the adopted reading. Its +92.24% strong-endpoint residual remains a failed physical reproduction against the digitized curve, despite sub-percent internal numerical closure. It must not be presented as an accepted reproduction.

The B.13 convergence scans are complete as a separate alternative-kernel study. Their residuals (+131.53% at the 10 MeV strong endpoint) are not evidence that the published Fig. 7 baseline itself fails because B.13 is not the operational benchmark adopted here.

No source, opacity, profile, coupling, luminosity, or axial-vector production result is changed by this wording adjudication.


## 8. P1 high-energy B.2 propagation audit (2026-11-10)

The direct calculation is archived in [B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md](B16_P1_B2_HIGH_ENERGY_PROPAGATION_AUDIT_2026-11-10.md), with its machine-readable output in \`outputs/b16_p1_b2_high_energy_propagation_audit_2026-11-10.json\`.

The key results are:
- Direct \(s\)-coordinate integration and the analytic radial primitive agree to \(8.3\times10^{-14}\) or better with four Gauss points per profile segment, including central, near-central, tangent, inward, and outward rays.
- The 642-node opacity interpolation grid agrees with an opacity table evaluated at all 1687 retained profile vertices: the maximum sampled change in total optical depth is \(1.87\times10^{-5}\), and the maximum sampled angular escape-average change is \(2.18\times10^{-5}\).
- In a separate 36-ray path-redshift diagnostic, the neutrino inverse-decay optical depth changes by a mean \(+4.98\%\) over the selected rays, while the semi-Compton optical depth changes by a mean \(+2.56\times10^{-6}\). These are unweighted ray diagnostics, not global source-weighted averages.

The P1 numerical propagation checks do not explain the \(+92.2406\%\) fixed-\(\omega\) strong-endpoint mismatch. The path-redshift branch remains a physical sensitivity and is not substituted for the displayed Eq. (B.2) baseline. No source, opacity, or axial-vector result is modified.


### Global channel attribution addendum

The source-weighted 210--510 MeV Shapley decomposition is archived in the P1 report and JSON output. It confirms that the path-redshift effect is a neutrino inverse-decay opacity effect, not a Compton opacity effect. This is a separate physical sensitivity and does not alter the fixed-\(\omega\) Fig. 7 baseline.


## 9. P1-C through P1-G closure update (2026-11-10)

The follow-up sequence is now complete at the scope supported by public information:

- **P1-C:** polarization-summed production/absorption normalization reconciled with the scalar Appendix-B prescription. No manual factor-of-three correction is allowed.
- **P1-D:** \(R_{\max}\) sensitivity evaluated at 15, 18.5, 20, 22, 24, 25, 26, 27.5, and 30 km, with source frozen at the literal 25 km baseline.
- **P1-E1--E3:** outer lapse, \(\mu_{\nu_\mu}\)/\(\mu_{\nu_\tau}=0\), and interior lapse source sensitivities completed.
- **P1-F:** boosted vector-decay daughter energies and energy-/flavor-dependent heavy-flavor decoupling reviewed.
- **P1-G:** the same SFHo-18.8, 1 s public baryon-density figure used to estimate a transport-only neutrino optical-depth envelope. This suggests a central 255 MeV transport radius near 24.6 km and 500 MeV near 26.2 km, but does not determine the energy sphere.

The P1-D 30 km sharp-boundary luminosity proxy nearly matches the Fig. 7 strong point only when the entire 210--510 MeV band is assigned full extra vacuum opacity. P1-G instead finds a central smooth radial 25--30 km reprocessing fraction of about 8.91% across the ten vector-energy nodes. The P1-D extension is therefore an extreme conditional upper bound, not a physical correction.

The exact heavy-flavor energy sphere remains uncomputed because the raw same-snapshot composition, energy-changing collision kernels, and neutrino moments are unavailable. The current public figure provides \(n_B(r)\) only through 20 km; the 20--25 km tail in P1-G is extrapolated. Do not select a new boundary, fit Fig. 7, or update the axial-vector curve.

**Final decision remains unchanged:** the literal fixed-\(\omega\), scalar B.2 benchmark is not a successful Fig. 7 reproduction at 10 MeV; PR #57 stays Draft/Open, and axial-vector recalculation remains frozen.


## 10. P1-H smooth daughter-reprocessing B.2 integration (2026-11-10)

P1-H has now inserted the P1-G energy-weighted daughter survival proxy into the full B.2 ray integral for the 210--510 MeV band. The B.1 source and scalar opacity inside 25 km are frozen; only the outer \(V\to\nu\bar\nu\) opacity is multiplied by \(1-P_{\rm pair}^{E}(\omega,r)\).

The central equal-mode density tail changes the band by \(-4.14\%\), the high-density tail by \(-10.60\%\), and the low-density tail by \(-0.33\%\). The band-only total proxies remain \(+86.87\%\), \(+78.21\%\), and \(+91.98\%\) above Fig. 7. By contrast, the sharp full-opacity \(R_{\max}=30\) km extension suppresses the band by \(70.94\%\) and gives a spurious near-match.

The B.1 source, literal \(R_{\max}=25\) band, and sharp \(R_{\max}=30\) band close to the P1-C/P1-D archived results at \(1.9\times10^{-11}\), \(5.0\times10^{-12}\), and \(5.5\times10^{-12}\). The direct V8 computation is archived; the Python implementation is added for repository reproduction but has not yet been independently rerun.

**Updated decision:** the smooth public-density transport model does not explain the strong-endpoint discrepancy. The exact energy sphere remains unavailable without same-snapshot energy-changing neutrino collision kernels and moments. Retain the literal 25 km baseline, keep PR #57 Draft/Open, and do not update the axial-vector constraint curve.
