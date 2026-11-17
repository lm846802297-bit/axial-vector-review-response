# Sixty-third review — P1-B E1 energy support, rescaling audit, and original-UV validation

**Date:** 2026-11-16  
**Reviewed base:** `49af1dc579d57baa554bcb76324f395664b60049`  
**Scope:** the next six `PENDING` entries in `DOCUMENT_AUDIT_REGISTER.csv`.  
**Disposition:** 4 `PASS_WITH_NOTES`, 2 `REVISION_REQUIRED`.

This review checks each report against its machine-readable summaries, relevant source code, tests, manifests and available Git provenance. It does not change any collision kernel, production rate, opacity, luminosity, Fig. 7 reference, SN1987A limit or axial-vector constraint.

## 1. Result summary

| Document | Result | Finding |
|---|---|---|
| `P1B_E1_ENERGY_REFINEMENT_2026-11-14/REPORT.md` | `PASS_WITH_NOTES` | Seven radial anchors pass the stated interpolation screen and the peak-shell selected quadrature check passes. The report correctly leaves the 1687-knot global high-order gate open. |
| `P1B_E1_GLOBAL04_2026-11-14/REPORT.md` | `PASS_WITH_NOTES` | The 50 worst selected 2D cells and 16 stratified radial intervals pass their high-order checks. This is selected coverage, not exhaustive high-order acceptance; the referenced ZIP is not in the tracked Git tree. |
| `P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14/REPORT.md` | `PASS_WITH_NOTES` | Complete low-order midpoint/interpolation screening passes on the existing \(x\in[0.5,36]\) support. The appended low-\(x\) screen correctly identifies a missing full-band support region. |
| `P1B_E1_GLOBAL_FULL_2026-11-14/REPORT.md` | `REVISION_REQUIRED` | The prose says interval 1487 was not high-order verified, but the same directory contains a high-order recheck JSON and summary that explicitly pass it. The acceptance narrative is internally inconsistent. |
| `rescaling_audit/README.md` | `PASS_WITH_NOTES` | The post-processing-only scope, fixed-overlap fit and prohibition on adopting \(\kappa\) are correct. The pooled global objective is point-weighted, not mass-weighted equally; document this distinction. |
| `stellar-cooling-original-uv-model-20261105/validation-results-2026-11-05.md` | `REVISION_REQUIRED` | The archived thermal-convergence CSV does not match the reference convention/schema of the pinned convergence driver. Source-blob provenance for the decay-width module also needs a two-version clarification. |

## 2. P1-B E1 energy refinement and global interpolation

All four P1-B records use the reconstructed SFHo-18.8 \(t_{\rm pb}=1\) s profile, 1687 radial rows, profile SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`, exact-recoil moving-muon B.13, \(m_{A'}=10\) MeV, pure-vector coupling, both muon charges and \(L,+,-\) modes.

### 2.1 Seven-anchor energy refinement — PASS_WITH_NOTES

The interpolation coordinate is
\[
x=(\omega_{\rm local}-m_{A'})/T(r).
\]
The five original nodes \(\{0.5,2,6,18,36\}\) are bisected in \(\sqrt{x}\), giving nine interpolation knots. The prescription is PCHIP in \(\sqrt{x}\) for \(\log\Gamma_{\rm abs}\); production and reduced absorption are reconstructed using detailed balance at the local thermodynamic point.

The seven selected radii have maximum interpolation errors:
- center: 0.6828%;
- peak-temperature shell at 8.48214 km: 0.4311%;
- previous G2 energy-worst radius at 14.575 km: 0.7351%;
- 21.63469 km: 0.3381%;
- 22.1 km: 0.3289%;
- muon-support edge at 22.191894 km: 0.3273%;
- 24.5 km: 0.2891%.

The peak-shell selected 17-point quadrature ladder ends with a maximum successive-order change \(8.8413\times10^{-4}\), below \(10^{-3}\). The other radii have targeted high-order checks only; the report does not claim every channel/energy point at every radius has been quadrature-validated.

The JSON also explicitly disclaims full 1687-knot acceptance and full-star transport. It records that an earlier stated 30,357-point global scan is not present in the retrievable report/artifact and is therefore not used as validated evidence. This is an appropriate provenance correction.

### 2.2 Global-02 full radial-node screen — PASS_WITH_NOTES, with a linked report inconsistency

The Global-Full summary records 1687 radial nodes × 17 energy coordinates = 28,679 low-order direct B.13 evaluations. The five-knot grid has a maximum interpolation error of 3.0794% and fails at all 1687 radial nodes. One bisection gives a nine-knot PCHIP grid with maximum error 0.7362% and zero radial nodes above 1%.

The top-60 radial-neighbor intervals receive 540 direct midpoint evaluations; maximum radial interpolation error is 0.0828%. The selected high-order energy-worst point changes by \(7.4685\times10^{-4}\), below \(10^{-3}\). These checks support the nine-knot interpolation screen, but not a full high-order scan.

**Required correction:** the report's Section 3/acceptance text is inconsistent for radial interval 1487:
- `REPORT.md` says the 22.191894 km support-edge interval had only a low-order midpoint check and was not counted as high-order verified;
- `RADIAL_INTERVAL_1487_HIGH_ORDER.json` gives direct high-order results at the left endpoint, midpoint and right endpoint, all ending at order \((20,12,12,12)\);
- the maximum successive-order change is \(3.3585\times10^{-7}\), and the high-order midpoint interpolation error is \(3.0783\times10^{-9}\);
- `TARGETED_HIGH_ORDER_SUMMARY.json` records `high_order_recheck: true` and `all_three_selected_radial_midpoint_intervals_high_order_pass: true`.

The report should add the interval-1487 result and explicitly list all three high-order radial intervals. Do not change the underlying JSON or upgrade the global result to a full high-order pass.

### 2.3 Global-03 full 2D midpoint screen — PASS_WITH_NOTES

The 1686 adjacent radial intervals are all covered. The 28,662 direct B.13 midpoint evaluations are reused for:
- 28,662 radial-midpoint comparisons: maximum 0.08284%;
- 13,488 energy-PCHIP midpoint comparisons: maximum 0.73617%;
- 13,488 2D cell-center comparisons.

Sequential PCHIP in \(\sqrt{x}\), followed by log-linear radial interpolation, has maximum 2D midpoint discrepancy 0.80678%, with zero of 13,488 cells above 1%. The local bilinear-log diagnostic has maximum error 5.47244%, with 11,509 cells above 1%; it must not be used as the production interpolant.

The four selected high-order cells subsequently pass their stated \(10^{-3}\) quadrature criterion; the maximum final successive-order change is 0.09327%. The interval-702 \(x=36\) endpoint extension is included in the recomputed high-order PCHIP error of 0.41892%.

These are low-order full-profile interpolation screens plus selected high-order checks, not an exhaustive high-order quadrature scan.

### 2.4 Global-04 selected high-order extension — PASS_WITH_NOTES

The top 50 PCHIP-error cells span 13.85–16.10 km and \(x_{\rm mid}=0.78125\). Their 900 endpoint nodes plus 50 cell centers give 950 direct high-order nodes. All pass the 0.1% successive-order criterion:
- maximum endpoint change: 0.09556%;
- maximum cell-center change: 0.004173%;
- maximum selected high-order PCHIP discrepancy: 0.806843%;
- cells above 1%: 0/50.

Sixteen stratified radial intervals contribute 240 additional direct nodes. All pass 0.1%; the maximum successive-order change is 0.099067%, and maximum radial midpoint interpolation discrepancy is 0.082851%.

The report correctly says that this is not an exhaustive high-order evaluation of every radius-energy node or every 2D cell center. It also correctly does not claim a full-star B.1 source integral, exact-B.13 B.2 optical depth, luminosity or updated SN1987A limit.

**Archive note:** `MANIFEST.sha256` records the digest of `P1B_E1_GLOBAL04_HIGH_ORDER_2026-11-14.zip`, but the ZIP itself is absent from the tracked Git tree. The compact summary and report are present; the raw 950-node bundle cannot be inspected from this checkout alone. Preserve the manifest digest and make the archive retrievable before describing the bundle as an available reproducibility artifact.

### 2.5 Low-\(x\) support gap — material limitation, correctly disclosed

The Global-03 report's Global-05 addendum records 80 direct evaluations at 16 stratified radii and \(x=\{0.05,0.1,0.2,0.35,0.5\}\), at screening order \((10,6,6,6)\). All rates are finite/nonnegative; maximum detailed-balance residual is \(4.6060\times10^{-15}\), and maximum final-muon shell residual is \(1.6261\times10^{-13}\).

For \(\mu^-\), the \(x=0.05\) to \(x=0.5\) absorption ratios at 9.95 km are 7.079 longitudinal and 1.817 for each transverse mode; at 15.5 km they are 2.468 and 1.244. Therefore setting the B.13 Compton absorption to zero below the existing \(x=0.5\) table support is not justified by the current data.

This is a low-order, 16-radius support screen, not a full radial scan or integrated luminosity correction. It establishes that the current full-band B.1/B.2 extrapolation is not accepted; it does not quantify the luminosity impact. The 210–510 MeV restricted-band result remains distinct from a full-band transport result.

**Combined P1-B disposition:** the nine-knot sequential PCHIP interpolation prescription passes the complete low-order midpoint screen on its existing support, and selected high-order checks pass. Global high-order quadrature is not complete, low-\(x\) support is missing, and no full-star emissivity, GR optical depth, luminosity or SN1987A limit is established.

## 3. Coupling-axis rescaling audit — PASS_WITH_NOTES

The README correctly isolates the audit from production modules. The script reads archived luminosity/reference JSONs and interpolates in \(\log L\)-\(\log g\); it does not rerun B.13, matrix elements, opacity or stellar transport. The fit uses \(\kappa\in[0.90,1.10]\), 801 grid points, no extrapolation, and a fixed point set across every trial \(\kappa\).

The literal scalar comparison gives:
- fixed fit points: 32 at 1 MeV, 25 at 10 MeV, 12 at 200 MeV;
- pooled global best fit \(\kappa=1.03\), RMS log residual 9.3098%, maximum ordinary relative residual 47.53%;
- 10 MeV mass-specific \(\kappa=1.06675\) improves its Fig. 7 pointwise fit, but the Fig. 4 lower/upper boundary deviations become \(-5.95\%\) and \(-5.35\%\), from an unscaled match within about 1%;
- the 1 MeV and 200 MeV mass-specific fits are close to unity.

The README's warning not to apply fitted \(\kappa\) to production scans or constraint figures is correct. The mode-resolved `exact_modes` control is explicitly not a like-for-like scalar-opacity implementation and must not be treated as standalone evidence of a production-code error.

**Documentation note:** the global objective concatenates all 69 fixed points with equal point weights, not equal mass weights. Consequently the 1, 10 and 200 MeV datasets contribute 32/69, 25/69 and 12/69 of the pooled residuals. Add this to the README so \(\kappa=1.03\) is not misread as an equal-mass global fit. This does not change the conclusion that one common rescaling fails.

The dedicated workflow is branch-restricted to `codex/major44-axial-cooling-constraints-20261105`; no fresh run on this maintenance PR is claimed.

## 4. Original single-VEV UV-model validation — REVISION_REQUIRED

The physical scope is appropriately constrained to the original one-VEV model:
\[
S=(v_s+s+i a_s)/\sqrt2,\quad Q_X(S)=2,\quad
m_{A'}=2|g_X|v_s,\quad G=a_s.
\]
The six mapping tests check the implemented mass relation, Goldstone projection, mass-proportional benchmark identity, inverse map, lepton-mass scaling and invalid-input handling. They are unit tests of the implemented algebra; they are not a replacement for a full UV Lagrangian/VLL-mass-matrix derivation.

The matrix-element module is a vacuum tree-level \(\gamma\mu\to\mu A'\) calculation. Its checks include on-shell kinematics, polarization orthonormality, electromagnetic Ward contraction, lab/CM total-cross-section agreement, Klein–Nishina agreement, the conserved-vector Thomson limit and axial longitudinal \(1/m_{A'}^2\) scaling. The quoted \(|\mathcal W_{V,A}|_{\max}\) values are absolute amplitude residuals at one benchmark, not dimensionless normalized residuals; label them as benchmark-specific or add a normalized residual.

The thermal module is explicitly homogeneous, optically thin and polarization-summed. It does not provide medium-rest-frame T/L-separated emissivities/opacities, inverse-process trapping, radial transport or an SN exclusion. The two-channel neutrino fractions omit kinetic-mixing-induced \(e^+e^-\) and other open channels; the report correctly does not call them complete physical branching fractions.

### 4.1 Convergence CSV does not match the pinned driver

The source table pins `stellar_semi_compton_thermal_convergence.py` to blob `e36ab13ae32216ae4d3c9a2323099485f880a1b0`. That driver:
- uses the last/highest requested quadrature order as the reference (`order_values[-1]`);
- writes `relative_rate_to_reference` and `relative_emissivity_to_reference`.

The committed `thermal-convergence-2026-11-05.csv` instead has columns `relative_rate_percent` and `relative_emissivity_percent`, with order 10 set to zero. Its order-12 row is \(-0.010803\%\) in event rate and \(+0.020199\%\) in emissivity, i.e. relative to order 10. Under the pinned driver with orders 6, 8, 10, 12, the order-12 row would be zero and the order-10 row would be approximately \(+0.0108\%\) and \(+0.0202\%\) relative to order 12.

The order-10-to-12 difference quoted in prose is numerically recoverable from the raw rate/emissivity columns. However, the CSV is not the direct output/schema of the pinned driver under its current reference convention. Resolve this by either regenerating the CSV with the pinned driver and documenting the highest-order reference, or pinning the exact legacy producer and explicitly stating its order-10 reference convention. Do not claim exact producer-level reproducibility until reconciled.

### 4.2 Source-blob reconciliation

The report lists `axial_decay_widths.py` blob `8f2d320858bd16173f16bed72af3d1cf1d8a8625`; the migrated original-model branch currently contains blob `32cc52210464d7e7618ca5b6e84be84ba616434e`. The old blob is retrievable and its width formula bodies match the current file; the differences are documentation/output labels for the two-channel neutrino fraction. Record both as “validated source snapshot” and “current archived file” rather than presenting the old hash as the current branch blob.

**UV-model disposition:** the model mapping and local matrix-element/thermal checks are useful and their scope limitations are mostly stated correctly. The validation record remains `REVISION_REQUIRED` until the convergence CSV producer/reference mismatch and dual source-blob provenance are explicitly reconciled. No thermal or stellar physics output is changed in this review.

## 5. Register reconciliation

Before this review: 372 reviewed, 90 pending:
- 249 PASS_WITH_NOTES
- 2 PASS
- 19 REVISION_REQUIRED
- 102 HISTORICAL
- 90 PENDING

After this review: 378 reviewed, 84 pending:
- 253 PASS_WITH_NOTES
- 2 PASS
- 21 REVISION_REQUIRED
- 102 HISTORICAL
- 84 PENDING

## 6. Required next work

1. Correct the Global-Full report's interval-1487 narrative using the already committed high-order JSON; keep the global high-order gate open.
2. Make the Global-04 ZIP retrievable or explicitly label it as an external archive not included in the repository.
3. Extend the B.13 table below \(x=0.5\) over the full radial profile, then perform high-order checks and quantify its integrated B.1/B.2 impact.
4. Do not proceed to full-star emissivity/GR optical-depth acceptance until the full energy support and global quadrature gates pass.
5. Add the point-weighting convention to the rescaling README; never adopt fitted \(\kappa\) as a production coupling redefinition.
6. Reconcile the UV validation CSV with its exact producer and record both the historical and current decay-width source hashes.

**Scientific disposition:** this review validates substantial interpolation progress and the limited rescaling/UV-model scopes, but it does not establish a full-band P1-B kernel, exact-B.13 B.2 transport, a reproduced vector Fig. 7 curve, or a model-specific SN1987A exclusion. No production physics outputs or axial-vector constraints changed.


## 7. Post-review current-tree reconciliation (2026-11-16)

Two of the reviewed findings have since been corrected without changing numerical outputs:

1. **Global-Full interval 1487:** `REPORT.md` now lists the three high-order radial-midpoint intervals individually. The support-edge interval 1487 is included with its direct high-order JSON provenance (blob `d0143b8070b0bcac571042e9b33c1a7412fa73ee`): all three nodes pass through order ((20,12,12,12)), maximum successive-order change (3.3585\times10^{-7}), midpoint interpolation error (3.0783\times10^{-9}). The report no longer says this interval was only low-order checked. This resolves the internal narrative inconsistency; global high-order quadrature and full-star transport remain unaccepted.

2. **Rescaling README:** the point-weighting convention is now explicit. The pooled literal fit has 69 equally weighted points: 32 at 1 MeV, 25 at 10 MeV and 12 at 200 MeV. The fit is point-weighted, not equal-mass weighted; this is documentation only and does not change (kappa=1.03) or the no-rescaling conclusion.

The Global-04 raw ZIP remains absent from the tracked tree; only its manifest digest, compact summary and report are available here. The low-(x) B.13 support gap remains material: the existing (x\ge0.5) table cannot be used as a full-band Compton opacity without the missing low-(x) extension and full radial/high-order validation.

The original single-VEV UV validation record remains `REVISION_REQUIRED`. The committed thermal-convergence CSV is not the direct output/schema of the pinned highest-order-reference driver, and the historical/current decay-width source blobs still need to be labelled as separate snapshots. Do not infer a model-specific UV–EFT closure or supernova limit from this local validation.

With the two post-review corrections recorded, this 63rd review report is `PASS_WITH_NOTES`; the remaining two underlying research records retain their own separate statuses. No production kernel, coupling, opacity, luminosity, Fig. 7 reference, SN1987A limit or axial-vector constraint was changed.
