# RC-001 upstream interface — Higgs/VLL UV–EFT matching

**Record type:** cross-repository integration and provenance record.  
**Created:** 2026-11-10.  
**Owning workstream:** axial-vector PR #69, Higgs–radial-scalar mixing and complex poles.  
**Status:** structural model correspondence established; derivative-sector results are linked but not yet imported into the scalar two-point prediction.

## 1. Purpose and repository boundary

This document connects the RC-001 calculations in **high-energy-theory-research** to the original axial \(U_A(1)_{L_\mu-L_\tau}\) model studied in this repository.

The repositories have deliberately different responsibilities:

- **Calculation source of truth:** [lm846802297-bit/high-energy-theory-research](https://github.com/lm846802297-bit/high-energy-theory-research). It owns the general UV–EFT derivations, loop scripts, symbolic algebra, numerical outputs, validation logs, and the complete operator-matching ledger.
- **Model-application source of truth:** [lm846802297-bit/axial-vector-review-response](https://github.com/lm846802297-bit/axial-vector-review-response). It owns the original model's field/charge map, benchmark assumptions, model-specific interpretation, and any conclusion eventually used in the manuscript or referee response.

Do not copy the upstream loop scripts or generated validation files into this repository. This interface stores the exact upstream revision, the model map, the physical relationship between workstreams, and the conditions for transferring a result. The upstream repository remains authoritative for the calculation itself.

This is an internal research document. It does not modify the manuscript, the formal referee-response letter, or the approved model scope.

## 2. Pinned upstream source and provenance

The upstream source is pinned to the exact PR head inspected for this interface:

| Item | Pinned value |
|---|---|
| Repository | lm846802297-bit/high-energy-theory-research |
| Pull request | [PR #11 — RC-001 UV–EFT matching](https://github.com/lm846802297-bit/high-energy-theory-research/pull/11) |
| PR state at inspection | Open / Draft; not merged |
| Branch | research/rc001-dim8-full-matching-20261109 |
| Exact head commit | [877cff6e17da933ac3212e803348ab422e920c96](https://github.com/lm846802297-bit/high-energy-theory-research/commit/877cff6e17da933ac3212e803348ab422e920c96) |

Relevant upstream files at that pinned commit:

| Upstream artifact | Role in this interface |
|---|---|
| [research/RC-001-vll-higgs-singlet-uv-eft.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-vll-higgs-singlet-uv-eft.md) | Master record: UV model, EFT conventions, matching scope, and unresolved verification gates |
| [research/RC-001-QLD-UV-one-background-triangle.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-UV-one-background-triangle.md) | One-background hard form factors, off-shell amplitude projection, and IBP/EOM discussion |
| [research/RC-001-QLD-nonabelian-IBP-EOM-completion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-nonabelian-IBP-EOM-completion.md) | Restricted electroweak non-Abelian IBP/commutator/current representatives |
| [research/RC-001-QLD-total-current-expansion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-total-current-expansion.md) | Complete leading-renormalizable (J_Y), (J_2^a), and normalized axial (J_X) currents for the original one-VEV model |
| [calculations/RC-001-QLD-total-current-expansion-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-total-current-expansion-audit.py) | Exact-rational charge/current bookkeeping audit |
| [validation/RC-001-QLD-total-current-expansion-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-total-current-expansion-audit.txt) | Recorded current-expansion checks |
| [research/RC-001-QLD-Higgs-source-EOM-model-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-Higgs-source-EOM-model-map.md) | Explicit axial-model Higgs EOM source, flavor-charge matrix, and leading fermion-EOM census |
| [calculations/RC-001-QLD-Higgs-source-EOM-model-map-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-Higgs-source-EOM-model-map-audit.py) | Exact charge and inverse-heavy-mass-order audit |
| [validation/RC-001-QLD-Higgs-source-EOM-model-map-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-Higgs-source-EOM-model-map-audit.txt) | Recorded source/charge checks |
| [research/RC-001-QLD-source-square-Fierz-channel-census.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-source-square-Fierz-channel-census.md) | Nine ordered source-pair channels, chirality, color/weak contractions, and derivative-placement census before Fierz reduction |
| [calculations/RC-001-QLD-source-square-Fierz-channel-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-source-square-Fierz-channel-audit.py) | Exact bookkeeping audit of the source-pair census |
| [validation/RC-001-QLD-source-square-Fierz-channel-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-source-square-Fierz-channel-audit.txt) | Recorded channel-census checks |
| [research/RC-001-QLD-chiral-Fierz-identities.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-chiral-Fierz-identities.md) | Exact 4D chiral Fierz identities and candidate evanescent definitions |
| [calculations/RC-001-QLD-chiral-Fierz-identities.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-chiral-Fierz-identities.py) | Exact SymPy component-by-component Fierz audit |
| [validation/RC-001-QLD-chiral-Fierz-identities.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-chiral-Fierz-identities.txt) | Recorded 1024-component validation output |
| [research/RC-001-QLD8-derivative-Fierz-IBP-ledger.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-derivative-Fierz-IBP-ledger.md) | Exact source-square covariant IBP identity and derivative-aware Fierz placement map |
| [calculations/RC-001-QLD8-derivative-Fierz-placement-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-derivative-Fierz-placement-audit.py) | Exact bookkeeping audit of nine ordered pairs and 36 derivative placements |
| [validation/RC-001-QLD8-derivative-Fierz-placement-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-derivative-Fierz-placement-audit.txt) | Recorded derivative-label transport checks |
| [research/RC-001-QLD8-second-order-fermion-EOM-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-second-order-fermion-EOM-map.md) | Second-order EOMs for Q_L, u_R, d_R, L_e, e_R and the resulting Higgs-derivative/field-strength operator classes |
| [calculations/RC-001-QLD8-second-order-fermion-EOM-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-second-order-fermion-EOM-audit.py) | Exact Minkowski Clifford, Dirac-square sign, and source-charge audit |
| [validation/RC-001-QLD8-second-order-fermion-EOM-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-second-order-fermion-EOM-audit.txt) | Recorded second-order EOM convention checks |
| [research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) | Exact 4D Fierz projections for EOM-generated scalar-vector and scalar-tensor structures, including Levi-Civita/self-dual terms |
| [calculations/RC-001-QLD-EOM-generated-chiral-Fierz-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-EOM-generated-chiral-Fierz-audit.py) | Exact SymPy component audit of 34 chiral identities |
| [validation/RC-001-QLD-EOM-generated-chiral-Fierz-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-EOM-generated-chiral-Fierz-audit.txt) | Recorded 8704-component validation output |
| [research/RC-001-QLD8-one-loop-counterterm-basis.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-one-loop-counterterm-basis.md) | P1.0 off-shell Green-basis map, source-pair/color/weak/flavor labels, and rank-3/rank-4 evanescent seeds |
| [calculations/RC-001-QLD8-counterterm-basis-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-counterterm-basis-audit.py) | Exact gamma-duality, color-completeness, source-representation, and derivative-census audit |
| [validation/RC-001-QLD8-counterterm-basis-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-counterterm-basis-audit.txt) | Recorded P1.0 exact-arithmetic validation output |
| [.github/workflows/rc001-qld8-counterterm-basis-audit.yml](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/.github/workflows/rc001-qld8-counterterm-basis-audit.yml) | PR-triggered independent CI for the P1.0 basis-seed audit |
| [research/RC-001-QLD8-QCD-color-factor-block.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-color-factor-block.md) | Exact six pairwise SU(3) exchange-color matrices for the (d^\dagger d) QCD pilot |
| [calculations/RC-001-QLD8-QCD-color-factor-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-QCD-color-factor-audit.py) | Exact Gell-Mann-matrix evaluation and color-conservation check |
| [validation/RC-001-QLD8-QCD-color-factor-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-QCD-color-factor-audit.txt) | Recorded color-matrix validation output |
| [research/RC-001-QLD8-QCD-one-loop-momentum-routing.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-one-loop-momentum-routing.md) | Exact (d^\dagger d) source insertion momentum and six QCD exchange-topology routings |
| [calculations/RC-001-QLD8-QCD-momentum-routing-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-QCD-momentum-routing-audit.py) | Exact symbolic check of four derivative placements and all six loop-momentum shifts |
| [validation/RC-001-QLD8-QCD-momentum-routing-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-QCD-momentum-routing-audit.txt) | Recorded momentum-routing validation output |
| [research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md) | Formal crossed odd-rank projection coefficients (f_n(D)), including rank-five Gram degeneracy |
| [calculations/RC-001-QLD8-ddim-Fierz-projection-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-ddim-Fierz-projection-audit.py) | Symbolic (f_1,f_3,f_5) and explicit 4D (sigmaGamma^{(n)}sigma) audit |
| [validation/RC-001-QLD8-ddim-Fierz-projection-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-ddim-Fierz-projection-audit.txt) | Recorded d-dimensional projection and Gram-degeneracy checks |
| [research/RC-001-QLD8-QCD-direct-pairing-color-basis.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-direct-pairing-color-basis.md) | Direct-pairing singlet/octet color basis and exact transformation to crossed-current basis |
| [calculations/RC-001-QLD8-QCD-direct-color-basis-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-QCD-direct-color-basis-audit.py) | Exact direct/crossed SU(3) color-matrix and similarity-transform audit |
| [validation/RC-001-QLD8-QCD-direct-color-basis-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-QCD-direct-color-basis-audit.txt) | Recorded direct-pairing color audit output |
| [research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md) | Six Feynman-gauge direct-pairing open-line numerator chains and gamma-rank analysis |
| [calculations/RC-001-QLD8-QCD-open-line-numerator-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD8-QCD-open-line-numerator-audit.py) | Exact 4D cross-chain and same-bilinear gamma-chain checks |
| [validation/RC-001-QLD8-QCD-open-line-numerator-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD8-QCD-open-line-numerator-audit.txt) | Recorded direct-pairing numerator gamma audit |
| [research/RC-001-QLD8-RL-tensor-evanescent-seed.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-RL-tensor-evanescent-seed.md) | Direct-pairing (RL) tensor evanescent from the two-gamma open-line chain; relation to crossed-basis evanescents remains to be determined |
| [.github/workflows/rc001-qld-chiral-fierz-identities.yml](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/.github/workflows/rc001-qld-chiral-fierz-identities.yml) | PR-triggered exact-Fierz CI workflow (run not yet observed) |
| [research/RC-001-portal-boundary-b1b3-reconciliation.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-portal-boundary-b1b3-reconciliation.md) | Tree-level (C_{5,ell}) Schur-complement sign and convention record |
| [calculations/RC-001-QLD-dim8-form-factor-projection.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-dim8-form-factor-projection.py) | Exact polynomial projection implementation |
| [calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py) | Symbolic SU(2) matrix and algebra audit |
| [validation/RC-001-QLD-dim8-form-factor-projection.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-dim8-form-factor-projection.txt) | Recorded projection output |
| [validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt) | Recorded algebra-audit output |

**Validation status at the pinned revision:** the exact 4D chiral Fierz audit, derivative-placement bookkeeping audit, second-order Dirac-square/source-charge audit, and EOM-generated scalar–vector/scalar–tensor Fierz audit were independently executed locally and passed. The latest EOM-generated Fierz audit verifies 34 matrix identities (8704/8704 components) plus six chiral tensor self-duality relations. Explicit minimal Fierz-difference definitions are now written for all four scalar–vector chiral channels and all opposite-/same-chirality scalar–tensor channels, with the Grassmann sign and derivative/field-strength labels retained. The source-square covariant-IBP identity applies to the complete product-rule sum; the derivative ledger records all 36 placements. Upstream PR-triggered runs 42735130364 (Fierz workflow) and 42735130363 (Candidate schema validation) both failed with empty job-step lists; the log endpoint has repeatedly returned 404, so the cause remains unknown. No CI pass is claimed. The four-dimensional projections and tree-level evanescent definitions are established, but the one-loop evanescent mixing/counterterm matrix and closure under UV-generated higher gamma strings remain open. The P1.2 symbolic audit also derives the crossed odd-rank projection coefficients \(f_n(D)\): \(f_1=-3\epsilon/4+O(\epsilon^2)\), \(f_3=-5\epsilon/24+O(\epsilon^2)\), and \(f_5=-1/(3\epsilon)+O(1)\). The \(f_5\) pole is a Gram-projection singularity, not a loop UV pole. The scalar–vector \(E_{RL;V}\) and direct tensor–tensor sector are distinct, and the direct-pairing \(E_{3;RL}^{\rm dir}\) is not the crossed \(X_3^{RL}\). The new P1.0 QLD8 basis-seed audit additionally checks rank-3 duality in 64/64 assignments, rank-4 duality in 256/256 assignments, contracted rank-3/rank-4 projections for RR/RL/LR/LL, the SU(3) completeness identity in 81/81 color-index assignments, the SU(2) epsilon invariant, the source hypercharges, and the 9-pair/36-placement count. Its local exact checks pass. The new P1.0 workflow has been added, but no run is yet returned for the latest head; no CI pass is claimed. This remains a basis/evanescent-seed audit only: no one-loop integral, UV pole, Z matrix, anomalous dimension, or finite Wilson coefficient has been calculated. The P1.1a \(d^\dagger d\) QCD color block then checks the crossed tensor \(C_X=C_1/3+2C_8\), all six pairwise \(\mathbf T_a\cdot\mathbf T_b\) matrices in the singlet/octet basis, and the exact sum \(\sum_{a<b}\mathbf T_a\cdot\mathbf T_b=-(8/3)\mathbf1\). These local exact checks pass. The updated QLD8 workflow now runs both the P1.0 gamma/source audit and the P1.1a color audit. The latest run on the pinned head, #42744441420, completed with failure but exposed an empty job-step list; the job-log endpoint returned 404. The cause is unknown, so this is not evidence of an algebra assertion failure. No CI pass is claimed. The color matrices are group-theory factors only: no loop kernel, Feynman-rule sign, UV pole, \(Z\) matrix, or anomalous dimension is yet calculated. The P1.1b \(d^\dagger d\) QCD routing audit then checks that the four source derivative placements sum to \(q_A^2\), that all six exchange topologies have the correct \(q_A\) shift, and that \(q_A^{(ab)}+q_B^{(ab)}=0\) with insertion factor \([q_A^{(ab)}]^2\). These exact symbolic checks pass. The current QLD8 workflow run on the latest pinned source still terminates with an empty job-step list; log retrieval returns 404, so the cause is unknown and no CI pass is claimed. The QCD pilot now has its source momentum factor, corrected topology routing, direct-pairing color matrices, and six open-line numerator skeletons fixed. The direct-pairing one-gluon Feynman-gauge chains generate gamma rank at most two on each bilinear. Overall graph signs, D-dimensional tensor integrals, UV poles, and counterterms remain uncalculated. The P1.1c direct-pairing \(RL\) tensor check further verifies that \((\bar Q\sigma^{\mu\nu}P_Rd)(\bar d\sigma_{\mu\nu}P_LQ)\) vanishes in four dimensions and that the corresponding two-gamma chain decomposes into \(D\,P_R\otimes P_L\) plus this tensor structure. Its \(O(\epsilon)\) scalar coefficient must be retained when multiplied by a UV pole. The direct tensor seed is not counted independently of the crossed \(E_{RL;V}\)/rank-three seeds until their \(d\)-dimensional Fierz map is known. No graph coefficient or UV pole is inferred.

The commit pin is immutable provenance, not an assertion that PR #11 has been merged. If the upstream head changes, update this interface only after inspecting the new diff, source files, and validation evidence.

## 3. Model correspondence with the original axial \(U_A(1)_{L_\mu-L_\tau}\) theory

The UV interaction structure in RC-001 is structurally the same charged-lepton/VLL/Higgs/singlet sector as the original model in the archived v6 manuscript, Eq. (Lagrangian) and the charge table:

\[
\begin{aligned}
\mathcal L_{\rm UV}\supset-\sum_{\ell=\mu,\tau}\big[
&y_\ell\bar L_\ell H E_{\ell R}
+\lambda_\ell S_\ell\bar E_{\ell L}\ell_R\\
&+M_{E_\ell}\bar E_{\ell L}E_{\ell R}
\big]+\mathrm{h.c.},
\qquad S_\mu=S,\quad S_\tau=S^* .
\end{aligned}
\]

The field/charge correspondence is:

| Field or parameter | Original axial model | RC-001 correspondence |
|---|---|---|
| \(H\) | SM doublet, \(Y_H=+1/2\), \(Q_X(H)=0\) | Same Higgs doublet and neutral axial charge |
| \(S\) | Complex singlet, \(Q_S=+2Q_\ell\), one VEV \(v_s\) | Same complex singlet; \(S_\mu=S\), \(S_\tau=S^*\) |
| \(L_\mu,\mu_R\) | \(+Q_\ell,-Q_\ell\) | Same muon chiral charges |
| \(L_\tau,\tau_R\) | \(-Q_\ell,+Q_\ell\) | Same tau chiral charges |
| \(E_\mu,E_\tau\) | Vector-like under the SM; axial charges \(+Q_\ell,-Q_\ell\) | Same flavor-resolved VLL sector |
| \(y_\ell,\lambda_\ell,M_{E_\ell}\) | Original universal-seesaw Yukawas and heavy masses | Same interaction parameters, subject to explicit normalization and phase conventions |
| \(A'\) | Gauge boson of \(U_A(1)_{L_\mu-L_\tau}\), \(m_{A'}=2g_Xv_s\) | Corresponds to the upstream \(U(1)_X\) gauge factor; \(H\) itself is neutral |

Thus the structural UV field content relevant to the charged-lepton/VLL/Higgs/singlet matching agrees. This is not permission to transfer every coefficient without checking conventions, perturbative order, external states, and the full diagram set.

The model identity is the **original one-VEV \(S+\mathrm{VLL}\) model**. No additional singlet VEV, \(\sigma\), right-handed-neutrino completion, or other extension is imported. The separate optional neutrino completion discussed for Major Points 3/4.1 is outside this interface.

## 4. What the RC-001 QLD8 calculation actually contributes

The QLD8 work is a derivative-operator matching sector of the same UV theory. It is related to the Higgs/VLL loop programme, but it is not the same Green function as the \(h\)-\(s\) two-point calculation in PR #69.

The upstream one-background calculation establishes, for its stated off-shell amplitude representatives, three polynomial amplitude columns. The transverse pair obeys the action-level relation

\[
\mathcal O_P+\frac12\mathcal O_Q
\doteq \mathcal O_{E,H},
\]

so a coefficient pair is reparameterized as

\[
a\,\mathcal O_P+b\,\mathcal O_Q
\doteq
a\,\mathcal O_{E,H}
+\left(b-\frac a2\right)\mathcal O_Q.
\]

Here \(\doteq\) denotes equality in the action up to a total derivative. The EOM representative must not be discarded before its Higgs-source, gauge-commutator, and current companions are included. The upstream non-Abelian note extends this algebra only for the stated Higgs-current representatives; the complete current basis and complete off-shell matching remain open.

Three objects must be kept distinct:

1. **Fermionic QLD8 Green-basis operator:** the dimension-eight derivative operator with two light-fermion fields, whose one-background form factors are being projected and reduced.
2. **Bosonic Higgs higher-derivative source:** \(\mathcal O_S=H^\dagger(-D^2)^3H\), associated with the \(p^6/M_E^4\) term in a Higgs two-point function. It is a separate bosonic amplitude direction, not the QLD8 fermionic operator.
3. **PR #69 scalar-potential operator:**
   \[
   O_8^{\rm pot}=(H^\dagger H)^2(S^\dagger S)^2.
   \]
   This is the non-derivative scalar-potential operator generated in the leading EFT5 light-fermion determinant and matched in the restricted heavy-VLL scalar-potential calculation. It is **not** the QLD8 fermionic derivative operator.

Consequently, the QLD8 coefficient map must not be added to the PR #69 \(O_8^{\rm pot}\) coefficient, nor interpreted as an immediate numerical correction to \(\Pi_{hs}\), the scalar pole positions, or the local \(h\)-\(s\) curvature.

## 5. Relationship to axial-vector PR #69

PR #69 ([Higgs–radial-scalar mixing and complex poles](https://github.com/lm846802297-bit/axial-vector-review-response/pull/69)) already contains the original-model fermion-sector self-energy matrix, VLL scalar-potential matching, the leading EFT5 bubble/contact and \(O_8^{\rm pot}\) pole analysis, and a cross-reconciliation with the earlier RC-001 scalar-potential record.

The QLD8 one-background calculation is relevant to PR #69's remaining task of completing derivative-operator matching and consistently treating field redefinitions/EOM. Its immediate role is to supply a pinned upstream operator-algebra result and an explicit list of unresolved matching dependencies.

It does **not** currently:
- add a new diagram to the already reported \(hh\), \(hs\), or \(ss\) mass-eigenstate two-point functions;
- change the quoted finite heavy-VLL coefficient of \(O_8^{\rm pot}\);
- close the complete same-order EFT soft/counterterm set;
- provide a complete gauge-independent \(2\times2\) scalar propagator;
- determine physical complex poles, residues, a coherent two-pole line shape, or an experimental exclusion.

A contribution may be transferred into the scalar two-point prediction only after a model-specific amplitude/counterterm map demonstrates that it contributes to that Green function at the same declared perturbative order. An operator-basis identity by itself is not an additional self-energy diagram.

## 6. Convention checks required before coefficient-level transfer

### 6.1 Covariant-derivative and gauge-field signs — explicit map

The archived axial manuscript uses
\[
D_\mu^-=\partial_\mu-i g_Y Y B_\mu^-
-i g_W T^aW_\mu^{a,-}-i g_{A'}Q_{A'}A_\mu^{\prime-},
\]
whereas the upstream non-Abelian note uses
\[
D_\mu^+=\partial_\mu+i g'Y B_\mu^+
+i g_2T^aW_\mu^{a,+}.
\]
Choose
\[
g'=g_Y,\qquad g_2=g_W,\qquad
B_\mu^+=-B_\mu^-,
\quad W_\mu^{a,+}=-W_\mu^{a,-},
\quad A_\mu^{\prime+}=-A_\mu^{\prime-}.
\]
Keep the generators and charges unchanged. Then
\[
\boxed{D_\mu^+=D_\mu^-}
\]
on all fields. In the axial model \(g_X=g_{A'}Q_\ell\); with the upstream normalized charge \(x=Q_{A'}/Q_\ell\), the physical product \(g_Xx\) is unchanged.

For raw component field strengths, with the non-Abelian commutator term defined consistently with each derivative convention,
\[
F_{\mu\nu}^{a,+}=-F_{\mu\nu}^{a,-},
\qquad B_{\mu\nu}^+=-B_{\mu\nu}^-,
\qquad F_{\mu\nu}^{\prime+}=-F_{\mu\nu}^{\prime-}.
\]
But the matrix curvature defined by \([D_\mu,D_\nu]=i\mathscr F_{\mu\nu}\) is invariant:
\[
\mathscr F_{\mu\nu}^+=\mathscr F_{\mu\nu}^-.
\]
The Higgs and fermion currents built from \(D_\mu\) are also unchanged.

The operator-level translation is therefore basis dependent:

| Object | Translation |
|---|---|
| \(D_\mu\), \(D^2\), Higgs/fermion currents | unchanged |
| Raw component \(F_{\mu\nu}\) | changes sign |
| Commutator curvature \(\mathscr F=[D,D]/i\) | unchanged |
| \(D\)-only operators, including \(Q_{LD}^{(8)}\), \(Q_{RD}^{(8)}\), and \(\mathcal O_S=H^\dagger(-D^2)^3H\) | unchanged, including their Wilson coefficients |
| One-background vertex obtained by expanding a \(D\)-only operator | changes sign with the external gauge-field variable |
| Operators with one explicit raw \(F_A\), including \(\mathcal O_P,\mathcal O_Q,\mathcal O_{E,H}\) | change sign; their coefficients change sign when translated between raw-\(F\) bases |
| Products of two raw component field strengths \(F_AF_B\) | even under the simultaneous field sign flip |
| Terms written as raw external \(F_A\) times invariant \(\mathscr F\) | translate both definitions explicitly; do not treat \(\mathscr F\) as a raw field strength |

The raw-field gauge equations of motion have opposite signs:
\[
\partial_\rho F_+^{\rho\mu}=+gJ^\mu,
\qquad
\partial_\rho F_-^{\rho\mu}=-gJ^\mu,
\]
with the same current \(J^\mu\). Thus coefficients of gauge-EOM current representatives must be translated consistently. The fact that \(Q_X(H)=0\) removes an internal \(U(1)_X\) curvature acting directly on \(H\); it does not remove mixed external-\(F_X\)/internal-\(B\) or \(F_X/W\) structures generated by the full SM covariant derivative.

The complete algebraic sign derivation and reproducible audit are in [C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md](C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md).

### 6.2 Signed dimension-five coefficient — algebraic discrepancy identified

The common operator orientation is
\[
\mathcal O_{5,\ell}=S_\ell\bar L_\ell H\ell_R,
\qquad
\mathcal L_{\rm EFT}^{(5)}\supset
-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.}
\]
The original mass matrix gives
\[
\mathcal M_\ell=
\begin{pmatrix}
0&y_\ell v_h/\sqrt2\\
\lambda_\ell v_s/\sqrt2&M_{E_\ell}
\end{pmatrix},
\qquad
m_{\ell,\mathrm{Schur}}
=-\frac{y_\ell\lambda_\ell v_hv_s}{2M_{E_\ell}}.
\]
Since the EFT VEV insertion gives \(m_{\ell,\mathrm{EFT}}=C_{5,\ell}v_hv_s/2\), the unique coefficient in this displayed convention is
\[
\boxed{C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.}
\]

The archived v6 manuscript Eq. (5-d), under the same displayed operator orientation and Lagrangian sign, instead writes \(c_\ell/\Lambda=+y_\ell\lambda_\ell/M_{E_\ell}\). Its signed EFT mass is therefore the negative of the UV Schur result. This is an algebraic sign discrepancy in the printed relation, not a different value of the positive physical singular mass. The manuscript's bi-orthogonal matrices are both proper rotations; for positive real \(y_\ell\lambda_\ell M_{E_\ell}\), \(\det\mathcal M_\ell<0\), so the signed diagonal masses must have a negative product. The quoted \(m_\ell^2\) relation is unaffected.

A right-handed light-field rephasing changes \(\lambda_\ell\) and \(\mathcal O_{5,\ell}\) together; it preserves \(C_{5,\ell}=-y_\ell\lambda_\ell/M_{E_\ell}\) and does not turn it into the positive relation while keeping the same transformed UV parameters and operator orientation.

**Internal convention decision:** PR #69 and RC-001 retain the Schur-complement result. The v6 Eq. (5-d) discrepancy is recorded but no manuscript or formal referee-response edit is made in this research PR. Existing PR #69 results based on \(|C_5|^2\) or \(|C_5|^4\) are unchanged; sign-sensitive interference must use the corrected convention consistently. See the reproducible [C5 and gauge-convention audit](C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md).

### 6.3 Portal boundary and renormalization scheme

The PR #69 reference condition
\[
\lambda_{HS}^{\rm EFT}(M_E)=0,\qquad
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{E}
\]
is a conditional matching benchmark, not a symmetry prediction and not a portal boundary fixed by the original paper. Any imported derivative-operator result must preserve the stated portal input or show its dependence.

Before combining coefficients, also align:
- the definition of the 1PI insertion and inverse-propagator sign;
- Minkowski metric and \(D=4-2\epsilon\) conventions;
- \(A_0/B_0\) normalization and subtraction scheme;
- matching scale and heavy-mass normalization;
- the hard/soft split and the EFT counterterm basis;
- whether coefficients refer to a Green basis, an IBP-reduced basis, or a fully EOM-reduced basis.

A matching coefficient in one of these conventions is not transferred by copying its numerical value alone.

## 7. Evidence and completion status

| Item | Current evidence | Status for axial-vector use |
|---|---|---|
| Charged-lepton/VLL/Higgs/singlet UV interaction structure | Original v6 Lagrangian/charge table and RC-001 master record | Structural correspondence established |
| \(O_8^{\rm pot}=(H^\dagger H)^2(S^\dagger S)^2\) | PR #69 benchmark reconstruction and RC-001 cross-reconciliation | Already tracked in PR #69; restricted scalar-potential result only |
| Three-column off-shell QLD8 amplitude projection | Pinned RC-001 §5J and exact polynomial projection record | Upstream algebraic result; not a complete operator basis |
| \(\mathcal O_P,\mathcal O_Q\) IBP relation | Pinned RC-001 §5K | Action-level identity for the declared representatives |
| Electroweak non-Abelian commutator/current map | Pinned RC-001 §5M and exact-rational audit | Restricted Higgs-current commutator map plus complete leading-renormalizable light-field currents; fermion EOM/Fierz reduction remains open |
| Gauge-current expansion into all leading-renormalizable light matter currents | [RC-001-QLD-total-current-expansion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-total-current-expansion.md) and exact-rational bookkeeping audit | Completed for the displayed restricted gauge-EOM representatives; fermion EOM/Fierz basis reduction remains open |
| Axial Higgs-source flavor/charge map | [RC-001-QLD-Higgs-source-EOM-model-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-Higgs-source-EOM-model-map.md) and exact charge audit | Source inventory and power counting established; no Fierz or final basis reduction |
| Higgs-source-square Fierz-channel census | [RC-001-QLD-source-square-Fierz-channel-census.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-source-square-Fierz-channel-census.md) and exact bookkeeping audit | Nine ordered source-pair channels classified; explicit (d)-dimensional Fierz/IBP/evanescent reduction remains open |
| Four-dimensional chiral Fierz algebra and working scheme | [RC-001-QLD-chiral-Fierz-identities.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-chiral-Fierz-identities.md) and exact SymPy audit | Four 4D identities checked in 1024/1024 components; NDR/anticommuting-γ5 and minimal Fierz evanescents fixed for the open-line QLD8 sector; full d-dimensional counterterm basis remains open |
| Derivative-aware source-square Fierz/IBP map | [RC-001-QLD8-derivative-Fierz-IBP-ledger.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-derivative-Fierz-IBP-ledger.md) and exact bookkeeping audit | Exact covariant IBP for the complete pair sum; 9 ordered pairs/36 placements and derivative transport checked; final basis remains open |
| Second-order fermion EOM map | [RC-001-QLD8-second-order-fermion-EOM-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-second-order-fermion-EOM-map.md) and exact convention audit | Dirac-square sign and source charges checked; endpoint Laplacians expose Higgs-derivative and field-strength four-fermion classes; enlarged evanescent basis remains open |
| Four-dimensional Fierz projection and explicit tree-level evanescents after second-order EOM | [RC-001-QLD-EOM-generated-chiral-Fierz-identities.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) and 8704-component exact audit | Displayed scalar-vector/tensor projections checked; minimal (E_{XY;V}) and (E_{XY;T}) differences defined; one-loop evanescent mixing and full Green-basis reduction remain open |
| QLD8 P1.0 off-shell Green-basis and gamma-string seed map | [RC-001-QLD8-one-loop-counterterm-basis.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-one-loop-counterterm-basis.md) plus exact gamma/color/source audit | Source-pair labels and rank-3/rank-4 4D projection seeds checked; one-loop closure and Z matrix not calculated |
| QLD8 P1.1a \(d^\dagger d\) QCD color-factor block | [RC-001-QLD8-QCD-color-factor-block.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-color-factor-block.md) and exact SU(3) audit | Six pairwise color matrices and color-singlet sum checked; no loop kernels or UV poles |
| QLD8 P1.1b \(d^\dagger d\) QCD momentum routing | [RC-001-QLD8-QCD-one-loop-momentum-routing.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-one-loop-momentum-routing.md) and exact symbolic audit | Four derivative placements and six topology momentum shifts checked; no loop kernels or UV poles |
| QLD8 P1.1c direct \(RL\) tensor evanescent | [RC-001-QLD8-RL-tensor-evanescent-seed.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-RL-tensor-evanescent-seed.md) and exact gamma-matrix audit | 4D vanishing, d-dimensional chain, and crossed odd-rank projections checked; rank-five Gram degeneracy exposes why finite rank-1/rank-3 elimination is invalid |
| QLD8 P1.2 direct-tensor d-dimensional Fierz projections | [RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md) and exact symbolic audit | \(f_1,f_3,f_5\) derived; rank-five Gram inverse is singular at \(D=4\); full finite closure remains open |
| QLD8 P1.3a direct-pairing QCD color basis | [RC-001-QLD8-QCD-direct-pairing-color-basis.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-direct-pairing-color-basis.md) and exact SU(3) audit | Direct/crossed basis map, six matrices, and color-singlet sum checked |
| QLD8 P1.3b six direct-pairing QCD numerator chains | [RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/877cff6e17da933ac3212e803348ab422e920c96/research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md) and exact 4D gamma audit | Six numerator skeletons and direct rank-2 ceiling checked; full graph signs/integrals open |
| Fermion EOM/Fierz reduction and complete Green-basis map | Partially reduced as recorded above | Open |
| Mixed-background hard amplitudes and same-order EFT soft graphs | Not completed | Open |
| Full counterterm closure and finite renormalized dimension-eight Wilson vector | Not completed | Open |
| C5 Schur-complement and (D/F/curvature) convention audit | [C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md](C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md), exact-rational test suite | Algebraic sign and field-variable map established; no loop calculation |
| Independent FeynArts/FeynCalc diagram validation | Not completed in the pinned record | Open |
| Physical \(h\)-\(s\) poles and observables | Requires the full PR #69 propagator programme | Open; not implied by QLD8 algebra |

## 8. Synchronization protocol

1. **Upstream changes first.** Derivations, scripts, and validation artifacts are changed only in high-energy-theory-research.
2. **Pin exact revisions.** When the upstream head advances, inspect the commit diff and update the SHA and file links here. Do not link a moving main branch as the sole provenance for a result.
3. **Map before importing.** Compare fields, charges, operator orientation, covariant-derivative signs, mass-matrix conventions, renormalization scheme, perturbative order, and hard/soft subtraction.
4. **Keep calculation and application separate.** Do not duplicate upstream scripts or claim that an upstream algebra check is an axial-model numerical validation.
5. **Transfer only demonstrated contributions.** A QLD8 result enters PR #69's scalar two-point ledger only if a model-specific diagram and counterterm derivation shows that it contributes to \(hh\), \(hs\), or \(ss\) at the same order.
6. **Update the manuscript last.** A result enters the formal reply or manuscript only after its model-specific derivation and validation are accepted and the author explicitly selects it for that purpose.

## 9. Immediate follow-up

The leading-renormalizable gauge-EOM current expansion, model-specific Higgs-source/charge inventory, source-square channel census, exact four-dimensional scalar-pair Fierz algebra, derivative-aware covariant-IBP map, second-order fermion-EOM map, and four-dimensional Fierz projections plus explicit tree-level Fierz-difference definitions for the EOM-generated scalar-vector/tensor structures are now recorded.

Next tasks:

1. Fix the complete relative Feynman-rule signs and fermion-flow conventions for all six direct-pairing QCD exchange graphs.
2. Generate the complete \(D=4-2\epsilon\) tensor numerators, including mixed rank-two\(\otimes\)scalar structures, with the direct color matrices and source factors kept correlated.
3. Add all four external-leg self-energy/wavefunction counterterms.
4. Perform the nonexceptional off-shell tensor integrals (or a consistent \(R^*\) implementation), separate power-like terms from the degree-two logarithmic local UV polynomial, and extract the \(1/\epsilon\) poles.
5. Verify the complete pole in the direct color/Dirac basis, then choose the finite direct-pairing physical/evanescent/EOM basis and calculate the QCD counterterm block.
6. Move to the same-chirality \(d^\dagger u\) QCD sector to test scalar/tensor and rank-four mixing.
7. Extend to \(SU(2)_L\), hypercharge, Yukawa, and background-gauge blocks.
8. Match the resulting operator set against all same-order EFT soft insertions and counterterms in the same NDR scheme.
9. Complete the finite UV-minus-EFT Wilson vector before testing any contribution to PR #69 \(hh,hs,ss\).
