# RC-001 — Consolidated raw weak-index and relative-phase ledger for all 24 \(WW\) five-point attachments

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVf  
**Status:** the raw weak-index ordering and relative Feynman-rule phase factors are now accounted for across all six seed pairs and all 24 direct external-W attachments. The cross-vertex and same-vertex subsets are kept distinct because their internal-W orientations differ. This closes the **weak-index/phase census**, not the Lorentz-weighted Ward sum.

## 1. Complete six-pair attachment census

| Pair | Internal-W orientation | Matter-line insertions | Scalar seagulls | Three-W | Total |
|---|---|---:|---:|---:|---:|
| LD-W-01 | A \(\to\) B | 2 | 0 | 1 | 3 |
| LD-W-02 | A \(\to\) B | 2 | 1 (B) | 1 | 4 |
| LD-W-03 | S \(\to\) F | 2 | 1 (S) | 1 | 4 |
| LD-W-04 | S \(\to\) F | 2 | 1 (S) | 1 | 4 |
| LD-W-05 | A \(\to\) B | 2 | 1 (A) | 1 | 4 |
| LD-W-06 | A \(\to\) B | 2 | 2 (A and B) | 1 | 5 |
| **Total** |  | **12** | **6** | **6** | **24** |

The two same-vertex pairs are not treated as ordinary cross-vertex pairs: their internal W flows from the scalar endpoint S to the fermion endpoint F.

## 2. Raw three-W weak tensors and phase comparison

Use
\[
\frac{P_{\rm line}}{P_4}=-g_2,\qquad
\frac{P_{\rm seagull}}{P_4}=+g_2,\qquad
\frac{P_{3W}}{P_4}=-ig_2.
\]

### Cross-vertex subset: internal W \(A\to B\)

Define
\[
\mathcal G_{AB}^a=\epsilon^{abc}R_A^bR_B^cT_0.
\]
The raw ordered matter-line commutators obey
\[
\mathcal W_A^a-\widetilde{\mathcal W}_A^a
=\mathcal W_B^a-\widetilde{\mathcal W}_B^a
=+i\mathcal G_{AB}^a.
\]
The three-W graph has group tensor \(+\mathcal G_{AB}^a\). Therefore
\[
\left(\frac{P_{\rm line}}{P_4}\right)
(\mathcal W-\widetilde{\mathcal W})
=-ig_2\mathcal G_{AB}^a,
\qquad
\left(\frac{P_{3W}}{P_4}\right)\mathcal G_{3W}^a
=-ig_2\mathcal G_{AB}^a.
\]
The phase-weighted group factors have the **same** sign. The Lorentz kernels determine how these terms combine.

### Same-vertex subset: internal W \(S\to F\)

Define
\[
\mathcal G_{FS}^a=\epsilon^{abc}R_F^bR_S^cT_0.
\]
The F- and S-line ordered commutators both give \(+i\mathcal G_{FS}^a\). But the three-W vertex attaches its internal indices in the order S,F, so
\[
\mathcal G_{3W,S\to F}^a
=\epsilon^{abc}R_S^bR_F^cT_0
=-\mathcal G_{FS}^a.
\]
Consequently,
\[
\left(\frac{P_{\rm line}}{P_4}\right)
(\mathcal W_{F,S}-\widetilde{\mathcal W}_{F,S})
=-ig_2\mathcal G_{FS}^a,
\]
whereas
\[
\left(\frac{P_{3W}}{P_4}\right)\mathcal G_{3W,S\to F}^a
=+ig_2\mathcal G_{FS}^a.
\]
The phase-weighted group factors have **opposite** signs. Again, this is not yet a Lorentz cancellation statement.

The difference between these two rows is essential. Applying the cross-vertex three-W sign to LD-W-03/04 would reverse their relative group phase.

## 3. Scalar seagull weak tensors

For any scalar endpoint X with opposite endpoint Y,
\[
\mathcal S_X^a
=\sum_b\{R_X^a,R_X^b\}R_Y^bT_0
=\mathcal W_X^a+\widetilde{\mathcal W}_X^a
=\frac12R_Y^aT_0.
\]
For an endpoint on the B side, the corresponding order is
\[
\mathcal S_B^a
=\sum_bR_A^b\{R_B^a,R_B^b\}T_0
=\mathcal W_B^a+\widetilde{\mathcal W}_B^a
=\frac12R_A^aT_0.
\]
Thus the seagull tensor is the sum of the two ordered line tensors, not either one separately. The scalar-line and seagull Lorentz numerators must remain attached to their own weak tensors in the integrand.

## 4. Reproduction records

The full raw-index result is split into two independently checkable pieces:
- Cross-vertex LD-W-01/02/05/06: research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md
- Same-vertex LD-W-03/04: research/RC-001-dim6-WW-same-vertex-raw-weak-index-bridge.md

The exact local SymPy audits establish:
- six seed pair projections: 96 weak-index components;
- ordered A/B/F/S commutators: 576 weak-index components;
- phase-weighted matter-line/three-W group-factor relations: 576 weak-index components;
- all scalar seagull anticommutators and their decomposition into ordered tensors: 288 weak-index components;
- direct attachment count: \(12+6+6=24\).

The source and output files are listed in the two companion notes. These are local exact symbolic checks, not a FeynArts/QGRAF run or a GitHub Actions result.

## 5. What is now closed and what remains open

**Closed:**
- the raw weak-index matrix ordering, the endpoint orientation of the three-W group tensor, the relative phase factors, and the scalar seagull anticommutators for all 24 direct attachments;
- the abstract fixed-current common-\(k\) transverse-kernel identity between matter-line commutator kernels and the three-W inverse-kernel difference, with the \(A\to B\) and \(S\to F\) signs kept distinct. Its graph-specific use for momentum-dependent scalar currents remains subject to the IVn-e routing bridge;
- exact common-\(k\) maps for all 12 Yukawa-endpoint terms and all six scalar-seagull routings, including the shifted heavy-channel momenta.

The ordinary-Feynman-gauge remainder \(R_{\rm FG}\) is nonzero and is retained. The new kernel identity does not close its ghost/gauge-fixing Slavnov–Taylor completion.

**Still open:**
1. insert the explicit pair-dependent fermion/scalar currents and heavy propagator numerators into the common-\(k\) identities;
2. combine the scalar-line and seagull Lorentz factors with their distinct weak tensors and the Yukawa/external endpoint terms;
3. complete external-leg/LSZ, parameter/operator counterterms and the gauge-fixing/ghost Slavnov–Taylor sector;
4. perform the common UV–EFT soft subtraction for the five-point amplitude;
5. compare the remaining local longitudinal contact with the already fixed EFT one-\(W\) contact.

The universal-kernel and route-map records are:
- \`research/RC-001-dim6-WW-fivepoint-common-k-lorentz-kernel.md\`
- \`research/RC-001-dim6-WW-fivepoint-common-k-shift-maps.md\`

These results do not yet constitute an integrated UV five-point form factor or a Wilson coefficient.

## 6. 2026-11-11 qualification: abstract kernel versus actual scalar-current routing

The weak-index and relative-phase census in this file remains closed. The separate IVh Lorentz-kernel calculation also remains a valid tensor identity for fixed arbitrary endpoint-current values. However, IVn-e finds that the actual scalar derivative currents used by IVl and IVm differ by \(q\) after their respective common-\(k\) routings. Therefore the abstract \(D(k)-D(k+q)\) cancellation must not yet be described as a completed graph-specific Lorentz-weighted cancellation for LD-W-02/03/04/05/06.

The exact audit and the six nonzero rational-point substitution checks are recorded in
\`research/RC-001-dim6-WW-fivepoint-momentum-dependent-scalar-current-audit.md\`.
The remaining task is to derive a common routing or an explicit change-of-variable identity with the complete scalar, light-fermion, heavy and W denominators, including the exchanged three-W Lorentz indices, weak tensor, phase and Dirac ordering. No physical non-cancellation is claimed; no graph is removed and \(R_{\rm FG}\) remains explicit.
