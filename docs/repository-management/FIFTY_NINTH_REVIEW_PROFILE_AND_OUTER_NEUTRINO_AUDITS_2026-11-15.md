# Fifty-ninth review — profile provenance and outer-neutrino audits

**Date:** 2026-11-15  
**Reviewed base:** \`c7ba00a611e7afa388046d29a84129f19d93e6e2\`  
**Scope:** the first six \`PENDING\` entries in \`docs/repository-management/DOCUMENT_AUDIT_REGISTER.csv\` at the reviewed base.  
**Disposition:** 2 \`PASS_WITH_NOTES\`, 2 \`REVISION_REQUIRED\`, 2 \`HISTORICAL\`.

No production rate, opacity, B.2 transport, coupling, luminosity, Fig. 7 reference, SN1987A limit, or axial-vector output was changed in this review.

## 1. Result summary

| Document | Result | Main reason |
|---|---|---|
| \`MUON_CHEMICAL_POTENTIAL_SOURCE_AUDIT_2026-11-07.md\` | \`REVISION_REQUIRED\` | The plotted muon density is a net-muon quantity, while the claimed Fermi-density closure uses \(n_{\mu^-}\) only; the current comparison therefore mixes definitions. |
| \`OUTER_NEUTRINO_ABSORPTION_INTERPRETATION_2026-11-08.md\` | \`HISTORICAL\` | Numerical transport results use the superseded 501-node uniform profile A, SHA-256 \`08d7afce...\`; one optical-depth table also omits its per-\(g^2\) normalization. |
| \`OUTER_NEUTRINO_PROFILE_CONVENTION_AUDIT_2026-11-08.md\` | \`HISTORICAL\` | The flavor-stress and path-quadrature results are from profile A, not the current vertex-preserving profile B. The archived note also has over-escaped TeX delimiters. |
| \`PROFILE_INPUT_AUDIT_12_15KM_2026-11-09.md\` | \`REVISION_REQUIRED\` | The density test has the same one-species/net-density mismatch; the generated JSON omits the profile CSV hash and is absent from this maintenance-branch tree; generated interpretation text is stale. |
| \`PROFILE_RADIAL_CONVERGENCE_8_15KM_2026-11-09.md\` | \`PASS_WITH_NOTES\` | The current JSON is pinned to profile B SHA-256 \`9fb14e79...\`; the radial scan is useful and convergent at 80-to-120 order, but energy and angular orders are fixed. |
| \`PROFILE_TRANSPORT_SENSITIVITY_12_15KM_2026-11-09.md\` | \`PASS_WITH_NOTES\` | The current JSON is pinned to profile B; the controlled 8--15 km substitution is diagnostic only and is not a physically adopted profile. |

## 2. Profile-version reconciliation

The checked artifacts contain three distinct fingerprints that must not be conflated:

| Profile generation | SHA-256 | Grid | Interpretation |
|---|---|---:|---|
| Uniform profile A | \`08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9\` | 501 nodes | Superseded uniform grid; it smears sharp digitized support boundaries. |
| Vertex-preserving predecessor | \`6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc\` | 1687 nodes | Earlier fingerprint of the current vertex-preserving construction. |
| Latest profile B | \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\` | 1687 nodes | Current reconstructed profile fingerprint in the maintenance PR. |

The existing profile-version reconciliation records that the 6c47-to-9fb14 refresh changed only last-digit serialization in the active thermodynamic columns. This is distinct from the material profile-A-to-profile-B change at support boundaries. Outputs are not to be relabelled with a hash they did not actually use.

The outer-neutrino absorption JSON is pinned to profile A (08d7). The earlier 1687-node outer-profile-input artifact is pinned to 6c47. The current maintenance-branch radial-convergence and transport-sensitivity JSONs are pinned to 9fb14.

## 3. Individual findings

### 3.1 Muon chemical-potential source audit — REVISION_REQUIRED

The upstream public-figure cross-check is valuable:

- Caputo \(\mu_\mu/T\) versus Bollig Fig. 4: maximum relative difference 0.0161%, mean absolute relative difference 0.00551% over the stated comparison interval.
- Caputo \(n_\mu\) versus Bollig Fig. 3: mean absolute relative difference 3.73%, maximum 10.45% over the common resolved interval.
- The current provenance JSON records the latest profile SHA-256 \`9fb14e79...\` and the Caputo density-curve SHA-256. The vector inventory records the Bollig PDF source hash.

These are figure-path comparisons, not a claim that the underlying Garching simulation data have sub-percent precision. The public figures support retaining Caputo as the baseline; the origin of the Ferreira-versus-Caputo discrepancy remains unresolved.

**Definition mismatch requiring correction.** The provenance script's density integral computes only
\[
n_{\mu^-}=\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f_{\mu^-}(E).
\]
It then compares that quantity with the plotted \(n_\mu\) curve. The supernova muonization literature defines the net muon number as an excess of \(\mu^-\) over \(\mu^+\); see Croon et al., *Supernova Muons: New Constraints on \(Z'\) Bosons, Axions and ALPs*, JHEP 01 (2021) 107, Sec. 2, DOI: https://doi.org/10.1007/JHEP01(2021)107, arXiv:2006.13942. Thus the like-for-like density is
\[
n_\mu^{\rm net}=n_{\mu^-}-n_{\mu^+},
\]
not \(n_{\mu^-}\) alone.

The separate \`audit_muon_chemical_potential.py\` implements this net density, but its archived JSON uses the old profile-A hash 08d7. Its six-point net-density reconstruction has a maximum absolute residual of 1.7557%, rather than the 0.5--1.1% quoted by the one-species comparison. The antimuon-to-muon ratio in that audit is about 1.24% at 5 km, 1.03% at 8 km, 0.28% at 10 km, and much smaller farther out. The numerical difference is modest, but the definitions must not be mixed when quoting precision.

Required repair:
1. Add \(n_{\mu^+}\) and \(n_\mu^{\rm net}\) to the provenance output and explicitly label the existing one-species result \(n_{\mu^-}\).
2. Re-run the net-density comparison on the latest profile B, preserving the old profile-A output as historical.
3. Add hashes for the Bollig Fig. 3 and Fig. 4 digitized CSV inputs to the provenance JSON.
4. Add a regression test for the net-density comparison.

This does not overturn the Caputo baseline choice supported by the Fig. 4 degeneracy-parameter cross-check. It does mean the current “internal density consistency” wording and quoted 0.5--1.1% precision cannot be accepted as a net-density validation.

### 3.2 Outer neutrino absorption interpretation — HISTORICAL

The numerical shell-removal and flavor-resolved results belong to the profile-A output, SHA-256 08d7, not the current vertex-preserving profile B. The document is retained as a historical calculation record; its radial-attribution factors and flavor decomposition must not be cited as current-profile-B outputs.

A separate units/normalization correction is also required before reuse. The channel table labels \(8.3245\times10^{15}\) and \(9.4779\times10^{14}\) as mean optical depths. These are coefficients per \(g^2\), not dimensionless optical depths. At the stated benchmark \(g=4.1717\times10^{-8}\), multiplying the neutrino coefficient by \(g^2\) gives approximately 14.49, consistent with the dimensionless neutrino optical-depth total in the companion profile-convention note. The table should be labelled \(\langle\tau/g^2\rangle_Q\) (or otherwise state the coupling normalization).

The flavor statement that the \(\nu_\tau\bar\nu_\tau\) contribution remains when \(\mu_{\nu_\mu}\) is set to zero is physically correct. The historical classification applies to the profile-dependent numerical results, not to that general channel-counting argument.

### 3.3 Outer neutrino profile convention audit — HISTORICAL

The outer chemical-potential stress tests, source-weighted shell optical depths, and 40/80 radial-order comparison are associated with the old profile-A transport output. They are not current profile-B numerical results. The assumption \(\mu_{\nu_\tau}=0\) is explicitly a modeling baseline because the public Caputo figure does not provide a separate \(\nu_\tau\) profile; it is not a direct extraction.

The physical interpretation remains useful: the \(\nu_\tau\bar\nu_\tau\) term does not vanish when the \(\nu_\mu\) chemical potential is set to zero, and detailed balance allows the reduced absorption to approach the time-dilated vacuum-decay scale in cold outer layers.

The Markdown source contains over-escaped math delimiters (for example, double-escaped inline delimiters and display-math brackets), which can render as literal backslashes rather than equations. Keep the historical scientific content, but repair the TeX escaping before reusing or citing the note.

### 3.4 Profile input audit, 12--15 km — REVISION_REQUIRED

The source-PDF identity work is useful. The associated profile workflow run #43197376758 completed successfully, including the profile extraction, nine focused tests, source-path audit, B.1+B.2 sensitivity calculation, radial scan, and production-output guard.

However, three items prevent acceptance of the current document/output pair:

1. The generated \`profile_12_15km_audit_2026-11-09.json\` is present on the research branch but is absent from the reviewed maintenance-PR tree.
2. The generated JSON records the two source-PDF hashes but does not record the profile CSV SHA-256. The workflow log shows that this run used the 6c47 vertex-preserving predecessor; the current profile is 9fb14.
3. The generator imports \`negative_muon_density_and_degeneracy\`, and the tests compare that one-species \(n_{\mu^-}\) with the plotted \(n_\mu\) curve. The test tolerance of 2% allows the mismatch to pass, but it does not make the definitions identical.

The generated \`manual_review_status\` and interpretation strings also still say that the numerical \(\mu_\mu\) discrepancy is unresolved without distinguishing two separate questions: the origin of the Ferreira-versus-Caputo discrepancy remains unresolved, while the baseline choice is supported by the later Bollig Fig. 4 comparison.

Required repair: add the profile hash to the JSON, distinguish \(n_{\mu^-}\) from \(n_\mu^{\rm net}\), update the generator's interpretation text, and archive the regenerated JSON on the maintenance branch. Preserve the old run and its actual 6c47 fingerprint.

### 3.5 Profile radial convergence, 8--15 km — PASS_WITH_NOTES

The current maintenance-branch JSON is pinned to profile B SHA-256 9fb14. It varies radial order 40, 80, and 120 at fixed \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\), energy order 100, angular order 32, and fixed-\(\omega\) B.2 paths.

Relative to order 120:
- order 80 differs by 0.0326% in baseline \(P_{\rm esc}\), 0.1141% in the fixed-source escape ratio, and 0.0670% in the B.1 source ratio;
- order 40 differs by 0.3169%, 0.6589%, and 0.1567%, respectively.

The ray-shell path integral is analytic for the piecewise-linear opacity interpolation; the varied radial order changes the emission-radius quadrature and radial opacity sampling grid. It is not a scan of the angular or energy quadrature orders. Order 120 is the highest tested reference, not an extrapolated exact limit.

Workflow #43197376758 ran the immediately preceding 6c47 profile fingerprint. The current JSON uses 9fb14; the profile-version reconciliation documents the last-digit-only refresh between these two vertex-preserving fingerprints. Result: accept the radial study with these scope limitations, not as a full multidimensional global-convergence proof.

### 3.6 Profile transport sensitivity, 12--15 km — PASS_WITH_NOTES

The current JSON is pinned to profile B SHA-256 9fb14 and uses radial order 40, energy order 100, angular order 32, \(m_V=10\) MeV, and fixed \(\omega\) along B.2 paths.

For the diagnostic-only Ferreira-\(\mu_\mu\) substitution over 8--15 km:
- B.1 source ratio: 1.2709188;
- own-source escape-probability ratio: 0.6608578;
- fixed-baseline-source escape-probability ratio: 0.6197762;
- escaped B.1 integral ratio: 0.8398966.

Thus the substitution increases the B.1 source by about 27.1%, lowers the own-source escape probability by about 33.9%, lowers the fixed-source escape probability by about 38.0%, and lowers the net escaped source integral by about 16.0%. It does not reproduce the required change and is not evidence that the Ferreira curve is the correct physical profile.

The 12--15 km-only variant changes the B.1 source by about +0.65% and the fixed-source escape probability by about -6.70%. The \(\mu_{\nu_\mu}=0\) 12--15 km stress changes the B.1 source by about +0.0055% and the fixed-source escape probability by about -0.0066%. These remain controlled sensitivity diagnostics, not adopted profile changes.

As with the radial scan, the successful workflow run used 6c47; the current archived JSON uses 9fb14. The study is accepted as a fixed-grid 10 MeV sensitivity result, not a global energy/angle convergence or Fig. 7 acceptance result.

## 4. Workflow and provenance evidence

- Workflow run #43197376758, “SFHo-18.8 profile and shell-resolved B.1+B.2 sensitivity (8--15 km)”: success. It regenerated the public-figure profile, passed nine focused profile tests, generated the profile-input audit, ran the 8--15 km transport sensitivity and 40/80/120 radial scan, and checked that production axial outputs remained unchanged. Its input fingerprint was 6c47.
- Workflow run #43197376818, “B.16 muon-neutrino profile sensitivity”: success. This is adjacent evidence for the \(\mu_{\nu_\mu}\) stress lane; it does not upgrade the old profile-A outer-neutrino absorption results to profile B.
- No full Fig. 7 benchmark, luminosity curve, or axial-vector constraint was accepted or changed by these six document reviews.

## 5. Register reconciliation

Before this review, the register contained 348 reviewed and 114 pending documents:
- 238 PASS_WITH_NOTES
- 2 PASS
- 10 REVISION_REQUIRED
- 98 HISTORICAL
- 114 PENDING

After reviewing the six next pending entries, the register contains 354 reviewed and 108 pending:
- 240 PASS_WITH_NOTES
- 2 PASS
- 12 REVISION_REQUIRED
- 100 HISTORICAL
- 108 PENDING

## 6. Required next work

1. Correct both muon-density audits to report \(n_{\mu^-}\), \(n_{\mu^+}\), and \(n_\mu^{\rm net}\) separately; rerun the net-density comparison on profile B and add tests.
2. Add the profile SHA-256 to the 12--15 km audit JSON, refresh its interpretation strings, and archive the output in the maintenance branch.
3. Keep the old profile-A outer-neutrino results historical. If they are needed for current conclusions, rerun the flavor-resolved and path-redshift lanes on profile B without rescaling any rate or fitting Fig. 7.
4. Correct the per-\(g^2\) optical-depth label and TeX escaping in the historical outer-neutrino notes before reusing them.
5. Keep the radial-convergence result limited to the tested radial dimension; do not infer full energy-angle convergence from it.

**Scientific disposition:** no profile substitution is adopted, no opacity or source rescaling is permitted, and the pure-vector Fig. 7 discrepancy remains unresolved.

## 7. Erratum added during the sixtieth review (2026-11-15)

The earlier statement in §3.1 that the plotted Caputo muon-density curve is a net-muon quantity was too strong. The public Fig. 3 convention is not established by the available source metadata. The independent B.1 source audit reports both \(n_{\mu^-}\) and \(n_{\mu^-}-n_{\mu^+}\) comparisons: the \(n_{\mu^-}\)-to-plot residual over the 12--15 km digitized vertices has 0.472% mean and 0.538% maximum absolute relative difference, while the net-density comparison over 5--15 km has 0.990% mean and 1.863% maximum. The latter interval includes inner radii with a larger positive-muon fraction; in the outer 12--15 km shell that fraction is below about 0.086% at 12 km and negligible by 15 km.

Accordingly, the audit finding is retained as \`REVISION_REQUIRED\`, but its reason is now stated precisely: the plotted-density convention must not be assumed, both density definitions must be reported, and the same-vertex 12--15 km net comparison should be recorded if the convention is resolved. This does not alter the B.17 source definition, which uses one negative-muon species with two spin states.


## 8. Post-review tree refresh erratum (2026-11-16)

A current-tree check after the reviewed-base snapshot found that the 12--15 km audit JSON is now present on the maintenance branch at `research/stellar-cooling-constraints-20261105/data/profile_12_15km_audit_2026-11-09.json` (blob SHA `9ae2d16dccae0f34489cae792f6e7c71403b3fa0`). This resolves the earlier *missing-file* part of §3.4. It does not resolve the scientific/provenance findings: the JSON records the two source-PDF hashes but still has no SHA-256 for the exact profile CSV, and its density comparison reports the one-species negative-muon Fermi integral against the plotted (n_\mu) curve without establishing the plotted curve's charge convention. The profile-input audit therefore remains `REVISION_REQUIRED` until the profile fingerprint and both density conventions are explicitly recorded and checked on common vertices.

The §3.1 erratum remains in force: the plotted Caputo Fig. 3 density convention is not established by the available public source. Report (n_{\mu^-}) and (n_{\mu^-}-n_{\mu^+}) separately; do not call either one the uniquely correct interpretation of the plotted curve without source evidence.

The 8--15 km radial-convergence and transport-sensitivity outputs remain pinned to profile B SHA `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. Workflow #43197376758 succeeded on head `3d227183aef41d2cc7671440e994bdd07a255ff5`; its radial-convergence log explicitly prints the earlier `6c47...` baseline for the sensitivity variants. Keep the workflow's per-variant fingerprint and the checked-in profile-B output fingerprint distinct. This review does not promote the diagnostic substitutions to physical profile changes.
