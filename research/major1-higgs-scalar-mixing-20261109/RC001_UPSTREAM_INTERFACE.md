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
| Exact head commit | [df9c007e8d4bd1716beae3b14591e12b6a551a8d](https://github.com/lm846802297-bit/high-energy-theory-research/commit/df9c007e8d4bd1716beae3b14591e12b6a551a8d) |

Relevant upstream files at that pinned commit:

| Upstream artifact | Role in this interface |
|---|---|
| [research/RC-001-vll-higgs-singlet-uv-eft.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/research/RC-001-vll-higgs-singlet-uv-eft.md) | Master record: UV model, EFT conventions, matching scope, and unresolved verification gates |
| [research/RC-001-QLD-UV-one-background-triangle.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/research/RC-001-QLD-UV-one-background-triangle.md) | One-background hard form factors, off-shell amplitude projection, and IBP/EOM discussion |
| [research/RC-001-QLD-nonabelian-IBP-EOM-completion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/research/RC-001-QLD-nonabelian-IBP-EOM-completion.md) | Restricted electroweak non-Abelian IBP/commutator/current representatives |
| [research/RC-001-portal-boundary-b1b3-reconciliation.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/research/RC-001-portal-boundary-b1b3-reconciliation.md) | Tree-level (C_{5,ell}) Schur-complement sign and convention record |
| [calculations/RC-001-QLD-dim8-form-factor-projection.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/calculations/RC-001-QLD-dim8-form-factor-projection.py) | Exact polynomial projection implementation |
| [calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py) | Symbolic SU(2) matrix and algebra audit |
| [validation/RC-001-QLD-dim8-form-factor-projection.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/validation/RC-001-QLD-dim8-form-factor-projection.txt) | Recorded projection output |
| [validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt](https://github.com/lm846802297-bit/high-energy-theory-research/blob/df9c007e8d4bd1716beae3b14591e12b6a551a8d/validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt) | Recorded algebra-audit output |

**Validation status at the pinned revision:** the upstream validation text records exact symbolic/algebraic checks for the declared projection and restricted non-Abelian identities. These checks do not establish a complete nonredundant dimension-eight SMEFT basis, a complete matter-current reduction, full UV–EFT counterterm closure, or an independent FeynArts/FeynCalc diagram calculation. The latest workflow run associated with the pinned head was reported as failed, but its job-step details and logs were not retrievable; the commit has no successful combined status to cite. Accordingly, this interface does not describe the pinned upstream PR as CI-passing or fully validated.

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

### 6.1 Covariant-derivative and gauge-field signs

The archived axial manuscript writes the covariant derivative with the convention
\[
D_\mu=\partial_\mu-i g_Y Y B_\mu-i g_W T^aW_\mu^a
-i g_{A'}Q_{A'}A'_\mu,
\]
whereas the pinned upstream non-Abelian note writes its electroweak Higgs derivative as
\[
D_\mu H=(\partial_\mu+i g'Y_HB_\mu+i g_2W_\mu^aT^a)H.
\]
The two conventions can be related by a consistent gauge-field/coupling sign redefinition, but the map must be written explicitly before comparing one-background form factors or signs of field-strength operators. In particular, \(g_X=g_{A'}Q_\ell\) in the axial paper is not to be confused with a bare gauge coupling stripped of its charge normalization.

The upstream observation \(Q_X(H)=0\) removes an internal \(U(1)_X\) curvature acting directly on \(H\). It does not remove mixed external-\(F_X\) / internal-\(B_{\mu\nu}\) or \(F_X\) / \(W_{\mu\nu}^a\) structures generated by the full SM covariant derivative. Those mixed-background terms still require matching if the complete background-field amplitude is claimed.

### 6.2 Signed dimension-five coefficient

The common operator orientation is
\[
\mathcal O_{5,\ell}=S_\ell\bar L_\ell H\ell_R.
\]
The upstream tree-level Schur-complement convention is
\[
\mathcal L_{\rm EFT}^{(5)}\supset
-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.},
\qquad
C_{5,\ell}^{(0)}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
This gives the signed light mass implied by the original mass matrix
\[
\mathcal M_\ell=
\begin{pmatrix}
0&y_\ell v_h/\sqrt2\\
\lambda_\ell v_s/\sqrt2&M_{E_\ell}
\end{pmatrix},
\qquad
m_{\ell,\mathrm{signed}}^{\rm Schur}
=-\frac{y_\ell\lambda_\ell v_hv_s}{2M_{E_\ell}}
\]
at leading order.

The archived manuscript [Eq. (5-d)](../../overleaf-source/axial-vector-model-building-v6/main-v6.tex), under the same displayed operator orientation, writes
\[
\mathcal L_{\rm 5-d}
=-\frac{c_\ell}{\Lambda}\mathcal O_{5,\ell}+\mathrm{h.c.},
\qquad
\frac{c_\ell}{\Lambda}\simeq+\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
The displayed signs therefore require an explicit reconciliation against the mass-matrix Schur complement and the precise phase/sign conventions for \(y_\ell,\lambda_\ell,M_{E_\ell}\). PR #69 currently uses the signed RC-001 convention; this interface records the comparison with the printed manuscript equation as an open audit item. No manuscript or referee-response edit is made here.

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
| Electroweak non-Abelian commutator/current map | Pinned RC-001 §5M and SymPy audit text | Restricted Higgs-current algebra; full current basis open |
| Gauge-current expansion into all light matter currents | Not completed in the pinned record | Open |
| Fermion EOM/Fierz reduction and complete Green-basis map | Not completed | Open |
| Mixed-background hard amplitudes and same-order EFT soft graphs | Not completed | Open |
| Full counterterm closure and finite renormalized dimension-eight Wilson vector | Not completed | Open |
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

The next coordination tasks are:

1. Resolve the signed \(C_{5,\ell}\) comparison between the mass-matrix Schur complement, the RC-001 convention, and the printed v6 Eq. (5-d).
2. Write one common covariant-derivative/gauge-field convention map for the original axial model and the upstream background-field calculation.
3. Complete the upstream total-current expansion, fermion-EOM/Fierz reduction, mixed-background amplitudes, and same-order soft/counterterm matching.
4. Only then determine whether any of the derivative-operator coefficients contribute to the PR #69 scalar two-point functions or remain separate three-point/current-sector information.

Until those steps are completed, the QLD8 work is an important related UV–EFT matching result, but it is not an additional numerical correction to the current PR #69 scalar self-energy or pole diagnostics.
