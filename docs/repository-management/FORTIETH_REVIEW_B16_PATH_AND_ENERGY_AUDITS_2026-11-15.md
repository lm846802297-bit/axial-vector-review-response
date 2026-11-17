# Individual review: B.16 path, shell, and energy-convention records

Review date: 2026-11-15. Baseline branch: `maintenance/repository-organization-audit-20261114`. Six B.16 documents were reviewed. Their evidence is kept separate from the published Fig. 7 discrepancy and from the unavailable same-snapshot raw supernova profile.

| Document | Outcome | Findings and disposition |
|---|---|---|
| `B16_10MEV_OUTER_INPUT_PHASESPACE_DIRECTION_AUDIT_2026-11-08.md` | `HISTORICAL` | The 22–25 km interpolation/lapse continuation, neutrino inverse-decay phase space, and direction-resolved escape tests pass their stated internal checks. The note concludes that these cannot explain the approximately 92% strong-endpoint Fig. 7 excess; outer-shell opacity is material but inner-path opacity dominates for 8–15 km sources. Its next-step wording is a dated snapshot and is superseded by later whole-path and independent B.1/B.2 audits. It correctly forbids rate rescaling and axial-curve updates. |
| `B16_12_15KM_NEUTRINO_INVERSE_DECAY_SHELL_AUDIT_2026-11-09.md` | `HISTORICAL` | The document itself labels its 501-node profile (SHA-256 08d7af...) historical and warns not to combine its numerical values with the current 1687-row vertex-preserving profile. Its channel-resolved 12–15 km inverse-decay result remains useful as provenance, but current-profile quantitative conclusions must come from the paired rerun/profile reconciliation record. |
| `B16_COMBINED_CHANNEL_SHELL_SENSITIVITY_2026-11-09.md` | `PASS_WITH_NOTES` | The combined nonlinear leave-out diagnostics correctly recompute luminosity after removing whole shells, whole channels, and inner/outer path groups. They identify neutrino inverse decay as the dominant attenuation channel and 12–15 km/22–25 km as sensitive shells. These are counterfactual sensitivity diagnostics, not alternative physical models; their nonlinear shifts must not be added. The interpretation correctly points to background/profile inputs rather than an established opacity algebra error. |
| `B16_CROSS_MASS_OPACITY_AND_ENERGY_CONVENTION_DIAGNOSTIC_2026-11-09.md` | `PASS_WITH_NOTES` | The 0.1/1/10 MeV source and opacity decomposition and fixed-\(\omega\) versus path-redshift-only comparison preserve the distinction between a diagnostic and full GR. The redshift-only variant improves the 10 MeV strong endpoint but worsens the 0.1/1 MeV endpoints, so it cannot be used as a universal correction. The exact B.16 reduced-Compton opacity cancellation is separately derived. Repaired a malformed path-redshift display equation whose omega and fraction commands were broken across lines. |
| `B16_DENSE_LOCAL_KERNEL_AUDIT_2026-11-09.md` | `PASS_WITH_NOTES` | Independent formula reconstructions cover all 64,000 actual \((r,\omega)\) nodes used in the end-to-end vector calculation, with maximum residuals at or below \(2.65\times10^{-13}\) and a 256→512 neutrino angular quadrature change at or below \(1.20\times10^{-14}\). This validates the local B.6–B.10 and B.14–B.19 implementations over that integration grid. It does not validate the physical no-recoil approximation against B.13, the stellar profile, GR energy/path convention, or agreement with Fig. 7. |
| `B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md` | `PASS_WITH_NOTES` | The B.1 integration variable is established as local production-point energy, with \(N(r)^2\) converting to luminosity at infinity; the B.1 energy-variable issue is resolved by an exact variable transformation. The literal B.2 expression retains fixed \(\omega\) along the chord as the reproduction baseline. The path-redshift-only variant retains Euclidean chords and is explicitly not full GR. The note correctly states that the article does not independently prove which unpublished Compton implementation generated Fig. 7, and that no fit-to-Fig. 7 choice is made. |

## Interpretation and limitations

- The outer-profile/direction audit and old 12–15 km shell audit are preserved as dated provenance, not live numerical authority.
- Leave-out tests are nonlinear sensitivities, not corrections.
- The redshift-only path calculation is not full GR; it lacks the spatial metric/ray geometry.
- Dense local-kernel closure validates the implemented local formulas on the chosen grid, not the physical model inputs.
- B.1's local-energy variable is resolved; the literal B.2 fixed-energy interpretation remains the adopted reproduction baseline pending any authoritative clarification.
- No opacity/source/luminosity rescaling or axial-vector constraint update is authorized by these records.

## Documentation repair

The cross-mass diagnostic contained a malformed display equation in which `\omega`, `\rm`, and `\frac` were split/corrupted. Replaced it with the intended
\[
\omega_{\rm loc}(r')=\omega_s\frac{N(r_s)}{N(r')}.
\]
No numerical result or physical convention was changed.

## Updated baseline register

The 462-row baseline register now records 252 individually reviewed and 210 pending documents after this batch. Exact outcome counts are maintained in `DOCUMENT_AUDIT_REGISTER.csv`.

No physics script was modified or rerun. This batch is a document/evidence review and equation-rendering repair only.


## Follow-up documentation corrections (2026-11-15)

- Added a historical-profile banner and corrected a literal escaped-newline break in the 10-MeV outer-input audit; its old 501-node values remain separate from the 1687-row profile.
- Added a scope boundary to the combined channel-shell sensitivity note, explicitly preventing leave-out shifts from being treated as additive corrections or global convergence.
- Linked the completed three-mass B.13 comparison from the cross-mass diagnostic and retained the fixed-omega versus path-redshift question as a separate unresolved B.2 issue.
- Repaired inline-code formatting in the dense local-kernel audit.
- Normalized malformed doubled TeX escapes and a stray parenthesis in the energy-variable audit. The exact B.1 local-energy versus E-infinity transformation remains established, but a separate comparison with the older archived B.1 source shows small residuals: -0.443% total, -0.536% neutrino inverse decay, and -0.245% muon-Compton. These are not caused by the variable transformation and remain visible as a distinct source-integration/profile/interpolation residual.
- No production calculation was rerun.


## Current-tree reconciliation (2026-11-16)

All six reviewed document paths remain present in the current tree. Their live Git blob IDs and baseline-register outcomes match the six entries in §1 exactly: two HISTORICAL profile-specific audits and four PASS_WITH_NOTES records. The 501-node historical profile SHA remains explicitly separated from the current 1687-row profile. The later B.13 three-mass comparison and the current fixed-(\omega) B.2 baseline remain separate from the redshift-only sensitivity diagnostic. No rate rescaling, profile replacement, luminosity update, SN1987A limit change or axial-vector curve update is supported by this review.
