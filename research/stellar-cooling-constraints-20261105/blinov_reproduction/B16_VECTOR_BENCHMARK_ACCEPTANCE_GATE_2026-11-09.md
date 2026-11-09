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
| Energy/GR convention | Published lapse-only source prescription and Euclidean-chord path reconstructed; full-GR extension remains unavailable | B.1--B.5 plus Caputo et al. arXiv:2201.09890 Supplemental C | Published-method prescription understood; Sec. 4.1/B.1 notation ambiguity remains |
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
2. Independent B.2 path integration.
3. B.1+B.2 end-to-end numerical closure.
4. Dense local collision-kernel checks on the full integration grid.
5. Caputo-versus-Ferreira \\(\mu_\mu/T\\) adjudication against Bollig Fig. 4.
6. Current-profile redshift-only diagnostic and archival.
7. Source-weighted muon-velocity diagnostic for the B.14 non-relativistic approximation; workflow #42572394290 passes and the JSON is archived.
8. 22--25 km muon-neutrino chemical-potential stress test at ±1 and ±3 MeV; workflow #42572982267 passes. The strong-endpoint luminosity changes by only +0.0172% and +0.1505%, respectively.

### Still unresolved

1. The true same-snapshot thermodynamic continuation over 20--25 km.
2. The exact unpublished numerical choice between the formal Compton integral B.13 and its reduced B.14--B.16 prescription; the 0.1 and 1 MeV global comparison is now running on the current profile.
3. The control of the non-relativistic/no-recoil muon approximation in B.14. The source-weighted B.17 susceptibility diagnostic gives mean muon speed 0.761 and 93.2% of the susceptibility weight at v_mu>0.5 in the low-mass Compton source region; this motivates, but does not replace, the full B.13 rate comparison.
4. A same-snapshot spatial metric A(r) or enclosed mass M(r) only if a separate full-GR extension is pursued.

The Garching radial-profile endpoint remains access-protected. This limits raw-profile precision and any optional full-GR extension, but it does not prevent the method-level checks of the published B.1--B.5 prescription using the reconstructed profile.

## 6. Final gate decision

- **Numerical modules:** pass.
- **Current public-profile reconstruction:** internally consistent for the validated (T) and (mu_\mu/T) ranges, but incomplete in the outer profile and metric.
- **Pure-vector Fig. 7 reproduction:** not passed.
- **Axial-vector recalculation:** frozen.
- **PR #57:** keep Open / Draft; do not merge as a validated reproduction.

The next action is not another integration-code patch. It is either to obtain genuinely new, independently sourced physical input or to record the present result as a non-reproduction with quantified limitations. No empirical rescaling, profile swapping, or opacity tuning is permitted.


## 7. Official data and metric-source availability

The official Garching archive index lists the relevant Bollig/Hüdepohl radial hydro and neutrino profiles and separately lists Robert Bollig's Python TOV solver (2020). Direct checks of the radial-profile and TOV-solver endpoints return HTTP 401 Unauthorized; the archive index states that some collections are password protected. A recent independent SFHo-18.8 analysis, arXiv:2610.35379, also points to this same archive for its full simulation profiles rather than providing an independent raw-data mirror.

Consequently, the exact same-snapshot hydro table and spatial metric remain unavailable through the checked unauthenticated endpoints. The current lapse comparison is visual only; it does not supply (A(r)) or (M(r)). Do not infer (A(r)) from the lapse alone, use a generic TOV solver as a substitute for the time-dependent snapshot, or splice another progenitor/time profile.

Detailed endpoint and source audit:
[B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md](B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md).
