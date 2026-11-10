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
| Exact head commit | [f9e997311b6d5fc1eb79de501f49228994c02eb0](https://github.com/lm846802297-bit/high-energy-theory-research/commit/f9e997311b6d5fc1eb79de501f49228994c02eb0) |

Relevant upstream files at that pinned commit:

| Upstream artifact | Role in this interface |
|---|---|
| [research/RC-001-vll-higgs-singlet-uv-eft.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-vll-higgs-singlet-uv-eft.md) | Master record: UV model, EFT conventions, matching scope, and unresolved verification gates |
| [research/RC-001-QLD-UV-one-background-triangle.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-UV-one-background-triangle.md) | One-background hard form factors, off-shell amplitude projection, and IBP/EOM discussion |
| [research/RC-001-QLD-nonabelian-IBP-EOM-completion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-nonabelian-IBP-EOM-completion.md) | Restricted electroweak non-Abelian IBP/commutator/current representatives |
| [research/RC-001-QLD-total-current-expansion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-total-current-expansion.md) | Complete leading-renormalizable (J_Y), (J_2^a), and normalized axial (J_X) currents for the original one-VEV model |
| [calculations/RC-001-QLD-total-current-expansion-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/calculations/RC-001-QLD-total-current-expansion-audit.py) | Exact-rational charge/current bookkeeping audit |
| [validation/RC-001-QLD-total-current-expansion-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/validation/RC-001-QLD-total-current-expansion-audit.txt) | Recorded current-expansion checks |
| [research/RC-001-QLD-Higgs-source-EOM-model-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-Higgs-source-EOM-model-map.md) | Explicit axial-model Higgs EOM source, flavor-charge matrix, and leading fermion-EOM census |
| [calculations/RC-001-QLD-Higgs-source-EOM-model-map-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/calculations/RC-001-QLD-Higgs-source-EOM-model-map-audit.py) | Exact charge and inverse-heavy-mass-order audit |
| [validation/RC-001-QLD-Higgs-source-EOM-model-map-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/validation/RC-001-QLD-Higgs-source-EOM-model-map-audit.txt) | Recorded source/charge checks |
| [research/RC-001-QLD-source-square-Fierz-channel-census.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-source-square-Fierz-channel-census.md) | Nine ordered source-pair channels, chirality, color/weak contractions, and derivative-placement census before Fierz reduction |
| [calculations/RC-001-QLD-source-square-Fierz-channel-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/calculations/RC-001-QLD-source-square-Fierz-channel-audit.py) | Exact bookkeeping audit of the source-pair census |
| [validation/RC-001-QLD-source-square-Fierz-channel-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/validation/RC-001-QLD-source-square-Fierz-channel-audit.txt) | Recorded channel-census checks |
| [research/RC-001-portal-boundary-b1b3-reconciliation.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-portal-boundary-b1b3-reconciliation.md) | Tree-level (C_{5,ell}) Schur-complement sign and convention record |
| [calculations/RC-001-QLD-dim8-form-factor-projection.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/calculations/RC-001-QLD-dim8-form-factor-projection.py) | Exact polynomial projection implementation |
| [calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py) | Symbolic SU(2) matrix and algebra audit |
| [validation/RC-001-QLD-dim8-form-factor-projection.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/validation/RC-001-QLD-dim8-form-factor-projection.txt) | Recorded projection output |
| [validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt) | Recorded algebra-audit output |

**Validation status at the pinned revision:** the upstream validation text records exact symbolic/algebraic checks for the declared projection and restricted non-Abelian identities. These checks do not establish a complete nonredundant dimension-eight SMEFT basis, a complete matter-current reduction, full UV–EFT counterterm closure, or an independent FeynArts/FeynCalc diagram calculation. The current pinned upstream head f9e997311b6d5fc1eb79de501f49228994c02eb0 has no workflow run or combined status returned by the connector. The latest known Candidate schema validation run on the preceding source-map head, 42724054652, failed with an empty job-step list and no retrievable log; it cannot be attributed to the current-expansion or source-map calculations. The current, source-charge, and source-pair bookkeeping audits were independently executed in the local calculation environment and passed; no upstream CI pass is claimed. Accordingly, this interface does not describe the pinned upstream PR as CI-passing or fully validated.

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
| Gauge-current expansion into all leading-renormalizable light matter currents | [RC-001-QLD-total-current-expansion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-total-current-expansion.md) and exact-rational bookkeeping audit | Completed for the displayed restricted gauge-EOM representatives; fermion EOM/Fierz basis reduction remains open |
| Axial Higgs-source flavor/charge map | [RC-001-QLD-Higgs-source-EOM-model-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-Higgs-source-EOM-model-map.md) and exact charge audit | Source inventory and power counting established; no Fierz or final basis reduction |
| Higgs-source-square Fierz-channel census | [RC-001-QLD-source-square-Fierz-channel-census.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f9e997311b6d5fc1eb79de501f49228994c02eb0/research/RC-001-QLD-source-square-Fierz-channel-census.md) and exact bookkeeping audit | Nine ordered source-pair channels classified; explicit (d)-dimensional Fierz/IBP/evanescent reduction remains open |
| Fermion EOM/Fierz reduction and complete Green-basis map | Not completed | Open |
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

The leading-renormalizable gauge-EOM current expansion, model-specific Higgs-source/charge inventory, and source-square channel census are now complete for the displayed restricted representatives. The original flavor-diagonal assumption is explicit: the \(\bar L_\mu H\tau_R\) and \(\bar L_\tau H\mu_R\) entries are gauge-allowed but set to zero, whereas the diagonal \(\mu,\tau\) renormalizable Yukawas are gauge-forbidden. The next tasks are:

1. Perform explicit \(d\)-dimensional Fierz/IBP reduction of the six source-pair structures, retaining the gamma-traceless derivative components, crossed color contractions, weak-index identities, and evanescent operators.
2. Complete the remaining mixed-background hard amplitudes and same-order EFT soft/counterterm matching in the upstream calculation repository.
3. Assemble the final derivative-operator basis only after the preceding reductions and matching are complete.
4. Map the accepted derivative operators into the axial model and determine whether any contribute to the PR #69 \(hh,hs,ss\) two-point functions or remain independent current/three-point information.

Until a model-specific same-order diagram/counterterm map demonstrates a contribution to the scalar two-point functions, QLD8 remains a related UV–EFT derivative-matching sector and is not an additional numerical correction to the current PR #69 scalar self-energy or pole diagnostics.