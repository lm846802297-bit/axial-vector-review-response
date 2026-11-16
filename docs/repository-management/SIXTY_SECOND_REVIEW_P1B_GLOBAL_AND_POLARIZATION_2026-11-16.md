# Sixty-second review — P1-B global 10 MeV and semi-Compton polarization

**Date:** 2026-11-16  
**Reviewed base:** \`9ed94d047ac1a7af4bbacca7ca44c5695f0bc732\`  
**Scope:** the next six \`PENDING\` entries in \`DOCUMENT_AUDIT_REGISTER.csv\`.  
**Disposition:** 3 \`PASS_WITH_NOTES\`, 2 \`REVISION_REQUIRED\`, 1 \`HISTORICAL\`.

This review compares the six documents with their machine-readable outputs, source snapshots, direct-projector code/tests, and the original GitHub Actions record. It does not modify a production collision kernel, opacity, transport table, luminosity, Fig. 7 reference, SN1987A limit, or axial-vector constraint.

## 1. Result summary

| Document | Result | Finding |
|---|---|---|
| \`WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md\` | \`REVISION_REQUIRED\` | The direct \(P_L\) follow-up strengthens the source-level discrepancy finding, but the header/earlier sections still say the origin is unidentified and the final symbolic recoil/Jacobian derivation remains open. |
| \`P1B_10MeV_ADAPTIVE01_LOCAL_PATCH_REPORT.md\` | \`PASS_WITH_NOTES\` | The stated local interpolation and selected pointwise quadrature criteria pass. The report correctly does not claim global kernel or transport acceptance. |
| \`P1B_10MeV_GLOBAL_02_REPORT.md\` | \`REVISION_REQUIRED\` | The 1687-knot scouting scan is complete, but selected interpolation and quadrature checks failed their thresholds. A later targeted hot-shell high-order result passes one point and is not incorporated in the report; the 1080/1140 midpoint-count discrepancy needs reconciliation. |
| \`P1B_10MeV_GLOBAL_PILOT_01.md\` | \`HISTORICAL\` | This is the sparse 8-radius × 5-energy scouting predecessor to Global 02 and Adaptive 01. Preserve as a dated pilot, not current acceptance evidence. |
| \`P1B_10MeV_RUN_43376779901.md\` | \`PASS_WITH_NOTES\` | The archival record correctly preserves a failed numerical acceptance and separately identifies the summary-publisher KeyError. |
| \`P1B_10MeV_RUN_43376779901_source_snapshot/README.md\` | \`PASS_WITH_NOTES\` | Seven copied source/input blobs were checked against the exact triggering commit. This is strong provenance, but byte identity is not a fresh clean-checkout numerical reproduction. |

## 2. Wang–Zhang polarization audit — REVISION_REQUIRED

The source-level analysis is substantially stronger than a mere comparison of integrated expressions.

### 2.1 Crossed amplitude and Ward identity

For the stated momentum routing and external indices, the crossed \(u\)-channel chain must reverse the vertex order relative to the \(s\)-channel:
\[
\gamma^\nu(\not P_u+m_\mu)\gamma^\mu.
\]
The literal same-order chain printed in Eq. (B.1b) does not cancel the \(s\)-channel Ward contraction. The independently evaluated 36-point grid gives:
- correct crossed amplitude: maximum normalized \(q_\mu\mathcal M^\mu\) residual \(1.33\times10^{-14}\);
- literal printed ordering: residual range \(1.74\times10^{-2}\) to \(1.06\);
- independent trace versus explicit spinor sum: \(8.37\times10^{-11}\).

This supports a source-level ordering inconsistency in the printed equation. It does **not** establish which ordering the authors used internally to generate Eqs. (B.2)–(B.4); the report must preserve that distinction.

### 2.2 Physical polarization and positivity

The direct rank-one longitudinal projection uses the exact vector-current Ward-equivalent representative
\[
\widetilde\epsilon_L^\mu
=\epsilon_L^\mu-\frac{q^\mu}{m_{Z'}}
=\frac{m_{Z'}}{\omega+|\mathbf q|}
(-1,\hat{\mathbf q}).
\]
This shift is valid only for the conserved pure-vector current. It must not be used for the axial current.

The direct \(P_L\) result is positive at all 36 tested points. The maximum physical-polarization versus Ward-representative difference is \(3.27\times10^{-7}\). The printed differential expressions have negative angular regions in each separately labelled physical channel, despite a positive polarization sum. A positive sum does not make negative mode-resolved rates admissible for production/absorption transport.

In the soft-muon/light-vector limit, the independent physical result is
\[
\frac{d\sigma_T}{dc}=C_0\beta(1+c^2)+O(r),\qquad
\frac{d\sigma_L}{dc}=C_0\beta x^2(1-c^2)+O(x^4,r),
\]
and therefore \(\sigma_L/\sigma_T\simeq x^2/2\). The paper's integrated unsuppressed term is assigned to \(L\), while the physical conserved-vector result assigns it to \(T\); the suppressed term also differs by a factor \(3/2\). This is not repaired by a simple \(T\leftrightarrow L\) relabeling.

### 2.3 B.3 subtraction is numerically ill-conditioned in the physics sense

The direct \(P_L\) follow-up finds that B.2 and B.4 individually remain close to their leading soft-limit values, while B.3, formed by subtracting them, systematically underestimates the direct longitudinal projection. An 80-digit scalar subtraction does not remove the residual.

The numerical asymptotic fits are
\[
\frac{B_2^{\rm paper}}{T_{\rm exact}}-1
\simeq\frac{2x^2r}{1+c^2},\qquad
\frac{B_3^{\rm paper}}{L_{\rm direct}}-1
\simeq-\frac{2r}{1-c^2}.
\]
At \(x=10^{-3}\) and \(E_\gamma\le0.1\) MeV, the maximum fit errors are 0.154% and 0.0921%, respectively. These are numerical asymptotic fits, not a complete symbolic finite-recoil derivation.

**Required document repair:** reconcile the status and Section 5/9 statements with Section 11. Distinguish (i) the printed B.1b ordering issue, (ii) the observed B.3 subtraction/recoil discrepancy, and (iii) the still-open question of whether the latter is a deliberate low-energy truncation or a printed-formula omission. Complete the symbolic leading-recoil expansion and the exact phase-space/Jacobian mapping before claiming a corrected finite-mass formula. No production kernel or paper limit is changed.

## 3. P1-B local and global calculations

All three P1-B reports use the same reconstructed SFHo-18.8 \(t_{\rm pb}=1\) s profile, 1687 rows, SHA-256 \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`, 10 MeV pure-vector endpoint, and exact-recoil moving-muon B.13 kernel.

### 3.1 Adaptive 01 local patch — PASS_WITH_NOTES

The patch covers a limited high-energy/radial region and passes its stated local criteria:
- sequential PCHIP radial/energy interpolation: maximum direct-midpoint discrepancy \(0.5883848\%\), below 1%;
- both interpolation orders give the same recorded maximum;
- maximum detailed-balance residual \(4.97\times10^{-14}\);
- maximum final-muon shell residual \(1.30\times10^{-13}\);
- 12 selected worst midpoints: order \((28,16,16,16)\) to \((32,18,18,18)\) maximum change \(9.3747\times10^{-5}\), below 0.1%.

Two additional local checks are useful:
- hot-shell endpoint at \(r=8.4821412\) km, \(\omega=1500\) MeV: order ladder ends with \(9.4393\times10^{-4}\), just below the \(10^{-3}\) criterion;
- narrow \(\mu_\mu\) support transition spans \(10^{-6}\) km (1 mm); five direct samples change by at most \(7.14\times10^{-8}\) between the stated quadrature orders. The profile was not smoothed.

The report explicitly says that the 12-point check is not all 151 patch points, the patch is not the full radial-energy domain, and no full-star emissivity or optical depth was recomputed. Retain those limitations. A local patch-weighted integral is not a GR luminosity.

### 3.2 Global 02 — REVISION_REQUIRED

G1 evaluated all 1687 radial knots at five thermal coordinates, for 8435 direct B.13 points and 36 checkpointed chunks. All rates are finite/nonnegative; maximum detailed-balance residual is \(1.0934\times10^{-14}\), and maximum final-muon shell residual is \(6.2145\times10^{-13}\).

These are algebraic/kinematic closure checks at scouting quadrature order \((10,6,6,6)\), not quadrature convergence.

G2 selected 60 high-variation radial intervals. The summary JSON reports 1080 direct midpoint evaluations, while the Markdown report says 1140 after adding energy midpoints. This may be a difference between original-\(x\) and refined-energy subsets, but the report should give an explicit count breakdown and reconcile the totals.

The selected checks show:
- at original thermal nodes, radial midpoint discrepancy below 0.09%;
- after energy refinement/PCHIP, worst checked midpoint discrepancy \(1.0720\%\), slightly above the 1% target, near \(r=14.55\)–\(14.60\) km, \(x=10.3923\), \(\mu^+\) production, longitudinal component;
- a representative hot-shell point initially changes by \(1.4371\%\) from order \((10,6,6,6)\) to \((14,8,8,8)\), above the 0.1% criterion.

A later targeted hot-shell order ladder in the summary JSON reaches a final change \(3.8318\times10^{-4}\) from \((22,12,12,12)\) to \((26,14,14,14)\). This passes that one point, but it does not erase the original low-order failure or validate all selected/global points. The Markdown report should incorporate this follow-up with the exact result-file provenance and retain the global-open status.

**Global 02 disposition:** radial-knot coverage complete; selected interpolation and initial quadrature acceptance not passed; one later hot-shell point passes after targeted refinement; global kernel, full-star emissivity, GR optical depth, luminosity and SN1987A constraint remain uncomputed.

### 3.3 Pilot 01 — HISTORICAL

Pilot 01 is an 8-radius × 5-energy sparse scouting mesh: 40 direct points at order \((16,10,10,10)\). Its detailed-balance and mass-shell checks pass, but the report correctly says it is not a converged radial-energy table, interpolation acceptance, emissivity, optical depth or luminosity.

It is superseded as the current progress snapshot by Global 02 and Adaptive 01. Preserve it as a pilot and do not count its local closure as global acceptance.

## 4. Original run #43376779901 and source snapshot

### 4.1 Numerical result — PASS_WITH_NOTES as an archival record

The original Actions run used source commit \`0f61bfc3e381402cbea9740958b9a2744f006040\`, profile B, 19 radial × 27 energy grid nodes and 468 cell midpoints. Its machine-readable manifest records:
- local emissivity energy-order change \(5.3263\times10^{-6}\): pass;
- maximum grid-node refinement change \(3.3678\times10^{-3}\): fail against \(10^{-3}\);
- maximum cell-midpoint refinement change \(2.4404\times10^{-3}\): fail against \(10^{-3}\);
- direct midpoint versus sequential log interpolation error \(0.571297\): fail against 1%;
- detailed balance \(4.2660\times10^{-14}\) and mass shell \(7.0487\times10^{-13}\): pass.

Thus the overall P1-B numerical acceptance correctly remains **NOT PASSED**.

The workflow's failure has two independent components:
1. the numerical acceptance genuinely fails quadrature and interpolation thresholds;
2. the later summary-publisher step throws \`KeyError: 'energy_coverage_pass'\`.

The regression tests (8/8), dense numerical audit and artifact upload succeeded. The KeyError is a reporting-code defect, not the reason the numerical acceptance failed. Conversely, fixing the KeyError would not turn the numerical result into a pass.

### 4.2 Source snapshot — PASS_WITH_NOTES

The source snapshot preserves the calculation driver, exact-recoil kernel, rate/profile helpers, test and fixed digitized profile. The recorded source commit is pinned, and the review's prior blob comparison confirms all seven copied files match their original source-commit blob IDs exactly.

This establishes byte-level provenance of the copied inputs and source. It does not establish a fresh clean-checkout rerun of the 10.9 MB numerical JSON. The README correctly points to the exact original checkout/package layout and original Actions artifact. Keep the original artifact digest and source SHA as the authoritative archive identity.

## 5. Register reconciliation

Before this review: 366 reviewed, 96 pending:
- 246 PASS_WITH_NOTES
- 2 PASS
- 17 REVISION_REQUIRED
- 101 HISTORICAL
- 96 PENDING

After this review: 372 reviewed, 90 pending:
- 249 PASS_WITH_NOTES
- 2 PASS
- 19 REVISION_REQUIRED
- 102 HISTORICAL
- 90 PENDING

## 6. Required next work

1. Repair the Wang–Zhang audit's stale status and reconcile its source-level B.1b finding with the B.3 direct-projector follow-up; derive the finite-recoil expansion and exact phase-space/Jacobian mapping symbolically.
2. Reconcile Global 02's 1080 versus 1140 midpoint count and update the report with the later one-point high-order hot-shell convergence result.
3. Extend direct midpoint checks beyond the selected 60 intervals and complete adaptive energy refinement across all 1686 radial intervals.
4. Complete pointwise quadrature refinement for every charge and polarization component, including the \(\mu^+\) high-energy and \(x\simeq10\) regions.
5. Only after global kernel acceptance, construct the full radial-energy table and independently integrate volume-weighted emissivity and GR optical depth.
6. Keep the pure-vector Fig. 7 gate blocked; do not rescale source, opacity, coupling, profile, luminosity, or any axial-vector constraint.

**Scientific disposition:** this round establishes a substantial local polarization finding and progress in 10 MeV B.13 sampling, but no globally accepted P1-B kernel or transport result. No updated SN1987A or axial-vector exclusion is authorized.


## 7. Post-review current-tree reconciliation (2026-11-16)

The Wang–Zhang audit has since been updated. Its current header and §12 now identify the direct (P_L) and explicit-spinor follow-up, distinguish the printed crossed-chain ordering inconsistency from the recoil-order bias in the B.3 subtraction, and state precisely that the complete symbolic finite-recoil expansion and exact phase-space/Jacobian mapping remain open. This resolves the stale “origin unidentified” status language, but not the underlying analytic derivation. The pure-vector Fig. 7 gate remains not passed.

The Global 02 count discrepancy remains unresolved at the source-record level: the machine-readable summary field `G2.direct_midpoint_evaluations` is 1080, while §G2 of the Markdown report says 1140. The available summary does not provide a subset decomposition proving that the extra 60 are separate energy-midpoint evaluations. Do not silently choose one total or infer a breakdown. A report addendum now records the exact field-level discrepancy and the later one-point hot-shell result.

A subsequent, distinct Global-03 full-profile screen is now archived at `P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14/GLOBAL_2D_SUMMARY.json` (blob `650496bd63bccff038bed9bcdff468e8287df376`). It directly evaluates 28,662 B.13 radial midpoints over all 1,686 intervals, plus 13,488 energy-PCHIP and 13,488 two-dimensional sequential-PCHIP cell centers. All sequential interpolation checks pass the 1% screening threshold. However, the same summary explicitly sets `global_high_order_quadrature_acceptance=false`; it does not compute full-star emissivity, GR optical depth, luminosity or Fig. 7, and does not update SN1987A. This is later evidence, not a retroactive repair of the Global 02 count or its original scouting-order acceptance.

The targeted hot-shell JSON (blob `3b11d334e62ce0adf0520587c3e370598ebf53bd`) confirms the single (r=8.4821412) km, (omega=417.895) MeV point converges from order ((22,12,12,12)) to ((26,14,14,14)) by (3.8318\times10^{-4}), below the 0.1% criterion. It remains a one-point check, not a global high-order acceptance.

The seven-file source snapshot was rechecked against its pinned source manifest and the repository tree: every copied file's blob ID matches the recorded source-commit blob ID. The archived run #43376779901 still has a genuine numerical acceptance failure (grid refinement (3.3678\times10^{-3}), midpoint refinement (2.4404\times10^{-3}), interpolation error (57.13\%)); the separate publisher `KeyError: 'energy_coverage_pass'` is a reporting defect, not the cause of the physical acceptance failure.

With these current-tree qualifications, the 62nd review report itself is `PASS_WITH_NOTES`: its remaining Global 02 count discrepancy and symbolic Wang–Zhang derivation are accurately preserved as open issues. No kernel, opacity, transport table, luminosity, Fig. 7 reference, SN1987A limit or axial-vector constraint is modified.
