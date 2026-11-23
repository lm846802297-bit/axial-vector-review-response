# RC-001 — Dimension-six gauge-correction diagram atlas

**Status:** exhaustive charge-compatible attachment-class census for the tree-level heavy-lepton exchange amplitudes has been recorded and locally checked. It is not yet a FeynArts-generated list of individual diagrams. The heavy-line self-energy/master-integral and FF/FS Yukawa-vertex hard sub-blocks are recorded separately; the complete gauge integrals, pole tables, finite matching coefficients, and diagram-package validation remain open unless explicitly marked otherwise below. PR #4 was merged as a provisional integration checkpoint; this does not close the physics gates.

## 1. Fixed model and matching target

The UV theory contains the heavy vector-like charged leptons \(E_\ell\), light lepton doublets \(L_\ell\), right-handed charged leptons \(\ell_R\), the SM Higgs doublet \(H\), and the complex singlet \(S\). The EFT retains \(H,S,A'\) and all light leptons. We integrate out \(E_\ell\) in the unbroken phase and match at the common scale \(\mu_R\).

Use \(\eta_\mu=+1\), \(\eta_\tau=-1\), and normalize \(X\)-charges in units of \(Q_\ell\). The charge assignments relevant to the tree-level derivative operators are:

| Line / field | \(SU(2)_L\) | \(Y\) | \(x\equiv Q_X/Q_\ell\) |
|---|---:|---:|---:|
| \(E_\ell\) | singlet | \(-1\) | \(\eta_\ell\) |
| \(L_\ell\) | doublet | \(-1/2\) | \(\eta_\ell\) |
| \(\bar L_\ell\) | conjugate doublet | \(+1/2\) | \(-\eta_\ell\) |
| \(H\) | doublet | \(+1/2\) | \(0\) |
| \(H^\dagger\) | conjugate doublet | \(-1/2\) | \(0\) |
| \(\ell_R\) | singlet | \(-1\) | \(-\eta_\ell\) |
| \(\bar\ell_R\) | singlet | \(+1\) | \(+\eta_\ell\) |
| \(S_\ell\) | singlet | \(0\) | \(+2\eta_\ell\) |
| \(S_\ell^\ast\) | singlet | \(0\) | \(-2\eta_\ell\) |

The tree-level operators and coefficients are
\[
Q_{LD,\ell}=(\bar L_\ell H)i\slashed D(H^\dagger L_\ell),
\quad C_{LD,\ell}=\frac{|y_\ell|^2}{M_{E_\ell}^2},
\]
\[
Q_{RD,\ell}=S_\ell^\ast\bar\ell_R i\slashed D(S_\ell\ell_R),
\quad C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_{E_\ell}^2}.
\]
The matching targets in this note are the \(O(g^2/M_E^2)\) corrections to the amputated \(\bar L L H^\dagger H\) and \(\bar\ell_R\ell_R S_\ell^\ast S_\ell\) amplitudes, their one-gauge-field form factors, and the induced current/source operators. The already-recorded bosonic field-strength/current-to-gauge coefficients in master §254 are a separate module and must not be added a second time.

## 2. How the attachment census is defined

For each tree-level heavy-exchange graph, label the internal heavy line \(E\) and the four external lines \(f,\bar f,\phi,\phi^\ast\). A one-gauge-boson correction is classified by the unordered pair of lines receiving the two gauge endpoints. The 10 distinct pairs among the five line types are enumerated below. Repeated insertions on the heavy line, the two charge-conjugate tree routings, both Yukawa vertices, and both orientations of a complex scalar must be generated separately by a diagram generator; the pair table is an attachment-class census, not a claim that every pair corresponds to exactly one graph.

For diagonal gauge propagators, the nonzero pair tests are \(Y_iY_j\), \(x_ix_j\), and the existence of two \(SU(2)\)-doublet generators. Stable pair IDs are assigned in the order listed in the census output: LD or RD, gauge label, and a two-digit index. Thus the sets are LD-B-01…10, LD-W-01…06, LD-X-01…03, LD-BX-01…09, RD-B-01…03, RD-X-01…10, and RD-BX-01…07. The same structural ID applies to both flavors; the signed coefficient is evaluated separately at \(\eta_\mu=+1\) and \(\eta_\tau=-1\). Self-energy/contact IDs use the line and gauge labels (for example LD-SE-E-B, RD-SE-S-X, LD-CT-B and RD-CT-X). For an off-diagonal \(B\)-\(A'\) propagator induced by kinetic mixing, the charge factor is proportional to
\[
Y_i x_j+x_iY_j
\]
up to the declared sign convention for the kinetic-mixing term. This factor can vanish even when both lines carry hypercharge and \(X\)-charge; those cancellations are kept explicitly.

## 3. \(Q_{LD}\): \(\bar L_\ell L_\ell H^\dagger H\)

The five line types are \(E,\bar L,L,H^\dagger,H\). The exhaustive nonzero pair classes are:

| Gauge propagator | Nonzero line-pair classes | Number of classes | Interpretation |
|---|---|---:|---|
| \(B B\) | all 10 pairs among \(E,\bar L,L,H^\dagger,H\) | 10 | Hypercharge exchange: same-vertex vertex corrections and cross-vertex boxes, plus heavy-line attachments |
| \(W^I W^I\) | all 6 pairs among \(\bar L,L,H^\dagger,H\) | 6 | \(E\) is an \(SU(2)\) singlet; no \(W E E\) endpoint exists |
| \(A'A'\) | \(E\!-\!\bar L,\ E\!-\!L,\ \bar L\!-\!L\) | 3 | \(H,H^\dagger\) carry no \(X\)-charge |
| \(B A'\) mixed propagator | all pairs except \(H^\dagger\!-\!H\) | 9 | Conditional on the kinetic-mixing propagator/boundary; retain the signed charge factor, not just a Boolean charge test |

The pair labels expand as follows. The hypercharge set is
\(E\!-\!\bar L,E\!-\!L,E\!-\!H^\dagger,E\!-\!H,\bar L\!-\!L,\bar L\!-\!H^\dagger,\bar L\!-\!H,L\!-\!H^\dagger,L\!-\!H,H^\dagger\!-\!H\).
The weak set is
\(\bar L\!-\!L,\bar L\!-\!H^\dagger,\bar L\!-\!H,L\!-\!H^\dagger,L\!-\!H,H^\dagger\!-\!H\).
The \(X\)-set is \(E\!-\!\bar L,E\!-\!L,\bar L\!-\!L\).
The mixed set is the hypercharge set with \(H^\dagger\!-\!H\) removed. For the mixed propagator, the exact coefficient \(Y_i x_j+x_iY_j\) must still be inserted; its sign and magnitude are not replaced by the count above.

### 3.1 Self-energy, mass, and vertex subfamilies

These are mandatory subfamilies in addition to the distinct-line exchange pairs:

- Heavy \(E_\ell\) self-energy insertions from \(B\), \(A'\), and the mixed \(B\)-\(A'\) propagator, including mass and field counterterms.
- \(L_\ell\) external-leg self-energies from \(B,W,A'\), plus the mixed propagator when retained.
- \(H\) external-leg self-energies from \(B,W\), including the scalar-gauge seagull contribution to the scalar two-point function and the corresponding parameter counterterms.
- Yukawa-vertex corrections at each conjugate \(y_\ell\) vertex: the \(L-H\) pair admits \(B,W\); the \(E-L\) pair admits \(B,A'\) and conditional mixed exchange; the \(E-H\) pair admits \(B\) and conditional mixed exchange. The mixed term must be checked with the signed charges and not inferred solely from field content.
- Cross-vertex boxes for all allowed pairs joining lines attached to opposite Yukawa vertices; keep the external momentum routing and weak-index tensor for each crossed routing.
- External-field and parameter counterterms for \(y_\ell,M_{E_\ell},g_Y,g_2,g_X\), and the kinetic-mixing input if it is part of the chosen scheme.

**Evaluated sub-blocks (not full LD matching):** the Feynman-gauge heavy-\(E_\ell\) self-energy kernel and zero-momentum Yukawa-vertex/crossed-box scalar masters are recorded in research/RC-001-dim6-heavy-line-vertex-box-integrals.md. The heavy-containing FF/FS vertex hard sub-block is recorded in research/RC-001-dim6-heavy-vertex-hard-pieces.md. The four \(WW\) cross-vertex classes LD-W-01/02/05/06 now have explicit per-pair numerator reductions, a hard/soft scalar-master split, a direct gamma-function check, and a vanishing longitudinal-projector triplet sum for one fixed ordered amplitude in research/RC-001-dim6-WW-crossbox-exact-routing.md. The charge-conjugate operator orientation maps to the same integrated action operator modulo a total derivative, so it is not an additional factor of two. Exact diagram-generator multiplicities, same-vertex and external-field Ward bookkeeping, and the complete LD UV–EFT vertex/contact sum remain open.

## 4. \(Q_{RD}\): \(\bar\ell_R\ell_R S_\ell^\ast S_\ell\)

The five line types are \(E,\bar\ell_R,\ell_R,S_\ell^\ast,S_\ell\). The exhaustive nonzero pair classes are:

| Gauge propagator | Nonzero line-pair classes | Number of classes | Interpretation |
|---|---|---:|---|
| \(B B\) | \(E\!-\!\bar\ell_R,E\!-\!\ell_R,\bar\ell_R\!-\!\ell_R\) | 3 | \(S_\ell\) is hypercharge neutral |
| \(W^I W^I\) | none | 0 | All fields in this tree-level \(Q_{RD}\) exchange are weak singlets |
| \(A'A'\) | all 10 pairs among \(E,\bar\ell_R,\ell_R,S_\ell^\ast,S_\ell\) | 10 | Every line is \(X\)-charged |
| \(B A'\) mixed propagator | \(E\!-\!S_\ell^\ast,E\!-\!S_\ell,\bar\ell_R\!-\!\ell_R,\bar\ell_R\!-\!S_\ell^\ast,\bar\ell_R\!-\!S_\ell,\ell_R\!-\!S_\ell^\ast,\ell_R\!-\!S_\ell\) | 7 | The mixed charge factor vanishes for \(E-\bar\ell_R\), \(E-\ell_R\), and \(S_\ell^\ast-S_\ell\) |

### 4.1 Self-energy, mass, and vertex subfamilies

- Heavy \(E_\ell\) self-energy from \(B,A'\), and conditional mixed propagation.
- \(\ell_R\) external-leg self-energy from \(B,A'\), and conditional mixed propagation.
- \(S_\ell\) external-leg self-energy from \(A'\), including the scalar-gauge seagull; there is no direct \(B S_\ell S_\ell^\ast\) or \(W S_\ell S_\ell^\ast\) vertex in the unbroken representation.
- \(\lambda_\ell\)-vertex corrections at both conjugate vertices: \(E-\ell_R\) admits \(B,A'\); \(E-S_\ell\) and \(\ell_R-S_\ell\) admit \(A'\) and conditional mixed exchange where the signed mixed factor is nonzero.
- Cross-vertex boxes and all crossed momentum routings for the nonzero pairs in §4, together with external-field and parameter counterterms for \(\lambda_\ell,M_{E_\ell},g_Y,g_X\) and the kinetic-mixing input.

**Evaluated sub-block (not full RD matching):** the same heavy-\(E_\ell\) self-energy and scalar master kernels apply to the \(Q_{RD}\) exchange because the heavy Dirac representation is the same. The heavy-containing FF/FS vertex hard sub-block is now evaluated in research/RC-001-dim6-heavy-vertex-hard-pieces.md; the complete RD UV–EFT vertex/contact sum, external light-fermion/scalar contributions, and crossed routings remain open. The additive \(B-A'\) two-point threshold is derived in `research/RC-001-dim6-mixed-kinetic-threshold.md`; it does not determine the conditional mixed-propagator four-point coefficients.

## 5. EFT-side diagrams and covariant-derivative contact vertices

The composite fields differentiated in the chosen operators have
\[
Y(H^\dagger L_\ell)=Y(S_\ell\ell_R)=-1,\qquad
x(H^\dagger L_\ell)=x(S_\ell\ell_R)=\eta_\ell.
\]
Both composites are \(SU(2)_L\) singlets. In the convention
\(D_\mu=\partial_\mu-i g_Y Y B_\mu-i g_X Q_X A'_\mu\),
\[
i\slashed D\Psi
=i\slashed\partial\Psi-g_Y\slashed B\Psi
+g_X\eta_\ell Q_\ell\slashed A'\Psi
\]
for either composite \(\Psi=H^\dagger L_\ell\) or \(\Psi=S_\ell\ell_R\). Thus the single-gauge contact vertex from the derivative operator has \(B\) and \(A'\) components but no direct \(W\) component. The \(W\)-correction graphs on the \(Q_{LD}\) side still exist through the external doublet lines and their gauge interactions.

For each operator insertion, the EFT set must include:

1. The insertion with a gauge boson exchanged between every allowed pair of external lines, with the same infrared regulator and momentum routing as the UV set.
2. The insertion's one-gauge contact vertex joined by a gauge propagator to each compatible external line/current. Include the conjugate operator/contact vertex consistently.
3. External-leg self-energies and the same LSZ/amputated-field convention used on the UV side.
4. EFT operator counterterms and renormalization of the tree-level \(C_{LD}\) or \(C_{RD}\) insertion.
5. The tree-level \(C_5\) sector only in the coupling monomials where it contributes at the same loop order. Do not add a gauge exchange to an already one-loop \(C_5C_5^\ast\) bubble and call it a one-loop graph; that is a two-loop correction.

## 6. Related current and source amplitudes

The two-fermion/two-scalar matching cannot be used as a proxy for all current coefficients. Track the following amplitudes separately:

- Fermion-current form factors: \(\bar L_\ell L_\ell B\), \(\bar L_\ell L_\ell W^I\), \(\bar L_\ell L_\ell A'\), and \(\bar\ell_R\ell_R B,A'\).
- Scalar-current form factors: \(H^\dagger H B\), \(H^\dagger H W^I\) in the appropriate derivative/current structures, and \(S^\dagger S A'\).
- Connected current-exchange amplitudes generated by joining the fermion and scalar form factors with \(B,W,A'\), or the mixed \(B-A'\) propagator. These are reducible in the exchanged gauge line and must not be reported as direct local 1PI four-scalar coefficients.
- EFT contact contributions induced by the covariant derivative in \(Q_{LD},Q_{RD}\), plus the gauge-field-EOM images in the selected basis.
- The kinetic-mixing boundary and running. If \(\chi(\mu_R)=0\) is adopted as an input, record it as an explicit boundary condition and verify the threshold prescription; otherwise retain the mixed-propagator terms with the full gauge kinetic matrix.

The bosonic field-strength and current-to-gauge matching already recorded in master §254 is retained as existing evidence. This atlas adds no duplicate contribution to that table.

## 7. Diagram-generation boundary

The atlas is complete at the level of charge-compatible one-gauge-boson attachment classes to the stated tree exchange, including external-leg subfamilies, mixed-propagator charge cancellations, and EFT derivative-contact classes. It is **not** yet an exact count of individual Feynman diagrams: diagram multiplicities, orientations, signs, weak-index tensors, gauge-fixing contributions, and symmetry factors must be generated and checked by FeynArts or an equivalent tool.

The current execution environment has no Mathematica/Wolfram executable, FeynCalc, FeynArts, pyfeyn, or QGRAF executable/module available. Therefore no external diagram generator or independent diagram-level amplitude calculation has been run. The local Python census only checks the charge-compatible attachment inventory; it cannot certify loop numerators or coefficients.

## 8. Reproducible companion files

- Structural generator: calculations/RC-001-dim6-gauge-atlas-census.py
- Captured output: validation/RC-001-dim6-gauge-atlas-census.txt
- UV–EFT subtraction matrix: research/RC-001-dim6-uv-eft-subtraction-ledger.md
- Primary analytic soft kernels: research/RC-001-dim6-soft-loop-integrals-and-checks.md

The diagram-level, integral-level, and model-level statuses must remain distinct. CI is explicitly skipped as an unavailable infrastructure check and is not a closure gate; no CI pass is claimed. PR #4 stays Draft/Open until the missing amplitudes, counterterms, common-basis reduction, and independent diagram-level evidence are closed.
