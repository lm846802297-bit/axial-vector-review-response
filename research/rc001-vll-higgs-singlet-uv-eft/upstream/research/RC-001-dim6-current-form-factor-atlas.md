# RC-001 — Dimension-six one-gauge-field form-factor atlas

**Status:** amplitude/topology registry established; no new finite current-form-factor coefficient is claimed. CI is explicitly skipped as an unavailable infrastructure check. The missing diagram-level calculation remains a physics evidence gap.

## 1. Scope and separation from the four-point gauge atlas

This note complements `research/RC-001-dim6-gauge-diagram-atlas.md` and `research/RC-001-dim6-uv-eft-subtraction-ledger.md`. It registers the amplitudes with one external gauge field,
\[
\bar L_\ell L_\ell V,\qquad \bar\ell_R\ell_R V,
\]
and the corresponding two-fermion/two-scalar form factors derived from the tree-level heavy-\(E_\ell\) exchange. It does not claim that the one-loop form factors have been integrated.

The already recorded bosonic field-strength/current-to-gauge coefficients in master §254 remain the existing bosonic module. They must be imported once for consistency checks, not recomputed or added to the new fermionic coefficients. A current-current graph connected by a single gauge propagator is reducible in that propagator and must not be called a direct local 1PI four-scalar or four-fermion coefficient.

## 2. External-current insertion classes

The external gauge field \(V_\mu\) is attached to every UV line on which its covariant kinetic term supplies a vertex. This is distinct from the internal virtual gauge boson in the one-loop correction: the latter is enumerated by the line-pair IDs in the four-point atlas.

| Form-factor ID | External amplitude | Lines that can emit the external field at the matter vertex | Restrictions |
|---|---|---|---|
| LD-B-FF | \(\bar L_\ell L_\ell H^\dagger H\,B_\mu\) | \(E_\ell,\bar L_\ell,L_\ell,H^\dagger,H\) | Use the hypercharges in the gauge atlas; include external-field and input renormalization |
| LD-W-FF | \(\bar L_\ell L_\ell H^\dagger H\,W_\mu^I\) | \(\bar L_\ell,L_\ell,H^\dagger,H\) | \(E_\ell\) is an \(SU(2)_L\) singlet; retain the weak generator/tensor until projection |
| LD-X-FF | \(\bar L_\ell L_\ell H^\dagger H\,A'_\mu\) | \(E_\ell,\bar L_\ell,L_\ell\) | \(H,H^\dagger\) have zero \(X\)-charge |
| RD-B-FF | \(\bar\ell_R\ell_R S_\ell^\ast S_\ell\,B_\mu\) | \(E_\ell,\bar\ell_R,\ell_R\) | \(S_\ell\) is hypercharge neutral |
| RD-X-FF | \(\bar\ell_R\ell_R S_\ell^\ast S_\ell\,A'_\mu\) | \(E_\ell,\bar\ell_R,\ell_R,S_\ell^\ast,S_\ell\) | Keep the signed \(\eta_\ell\) factors on fermion and scalar lines |
| LD/RD-BX-FF | Same external states with the mixed \(B-A'\) propagator/field basis | The applicable \(B\) and \(A'\) insertions above | Conditional on the declared kinetic-mixing matrix, its boundary condition and threshold prescription |

For each row, generate the complete one-loop set, not only a vertex correction on the light-fermion line:

1. External \(V_\mu\) insertion on each allowed light-fermion, heavy-fermion, and scalar propagator segment, including both segments adjacent to the two conjugate Yukawa vertices where distinct.
2. All internal virtual-gauge attachments from the four-point atlas, with the external-current insertion placed on every compatible line/vertex of the resulting one-loop topology.
3. External-leg self-energies and LSZ/amputation terms in the same convention as the four-point amplitude.
4. Scalar seagull contributions and the corresponding scalar/gauge-field counterterms where allowed by the covariant kinetic terms.
5. Gauge-field wavefunction renormalization, \(B-A'\) field/kinetic mixing, and parameter counterterms. For non-Abelian external \(W^I\), include the gauge-sector and ghost contributions required by the chosen gauge fixing and Ward/Slavnov-Taylor identities.
6. EFT insertions of \(Q_{LD}\) or \(Q_{RD}\), including the one-gauge contact term from the covariant derivative, virtual-gauge attachments to external lines, EFT counterterms, and the same external-field convention.

This list is a topology-generation prescription. It is not a claim that every bullet corresponds to one individual Feynman graph; exact multiplicities and signs must be fixed by explicit graph generation or a documented manual enumeration.

## 3. EFT covariant-derivative contact terms

For both operators the differentiated composite is an \(SU(2)_L\) singlet:
\[
\Psi_L=H^\dagger L_\ell,\qquad \Psi_R=S_\ell\ell_R,\qquad
Y(\Psi_L)=Y(\Psi_R)=-1,\quad x(\Psi_L)=x(\Psi_R)=\eta_\ell.
\]
Consequently the single-external-gauge contact from the derivative insertion has \(B_\mu\) and \(A'_\mu\) components but no direct \(W_\mu^I\) component. This absence does not remove \(W\)-loop corrections to \(Q_{LD}\): the external \(L,H\) lines still couple to \(W\).

For the mixed \(B-A'\) sector, retain the full gauge kinetic/propagator matrix until the external-field basis and the renormalized mixing boundary are specified. Do not replace a signed mixed charge factor by a Boolean “allowed” flag.

### 3.1 Tree-level \(W\) Ward identity and the partial loop check

For the \(SU(2)_L\) sector define
\[
\Psi_L=H^\dagger L_\ell,\qquad \bar\Psi_L=\bar L_\ell H.
\]
Both composites are weak singlets, so
\[
D_\mu^{SU(2)}\Psi_L=\partial_\mu\Psi_L,\qquad
D_\mu^{SU(2)}\bar\Psi_L=\partial_\mu\bar\Psi_L.
\]
With \(D_\mu H=\partial_\mu H-i g_2T^IW_\mu^I H\) and \(D_\mu L=\partial_\mu L-i g_2T^IW_\mu^I L\),
\[
(D_\mu H)^\dagger L+H^\dagger D_\mu L
=\partial_\mu(H^\dagger L)
+i g_2H^\dagger T^IW_\mu^IL-i g_2H^\dagger T^IW_\mu^IL
=\partial_\mu(H^\dagger L).
\]
The cancellation holds generator by generator for \(I=1,2,3\), not only after summing over weak indices. Thus the tree-level EFT insertion \(Q_{LD}=\bar\Psi_L i\slashed D\Psi_L\) has no direct \(W_\mu^I\) contact vertex. This explicit expansion is independently checked in calculations/RC-001-dim6-WW-wick-multiplicity.py (five local regression tests; captured output in validation/RC-001-dim6-WW-wick-multiplicity.txt). The longitudinal external-\(W\) Ward contraction of the emissions from the two composite pairs is proportional to
\[
(t_{\bar L}^I+t_H^I)T_0,\qquad
(t_{H^\dagger}^I+t_L^I)T_0,
\]
and both vanish by the singlet identities in research/RC-001-dim6-SU2-attachment-projection.md. The same explicit Wick audit shows that the two endpoint assignments for each unordered pair cancel the \(1/2!\) in the second-order interaction, giving unit multiplicity; this is a manual combinatoric check, not a generated graph/sign census. Thus the tree-level operator insertion satisfies the \(W\)-current Ward identity without a derivative-contact term.

A separate partial one-loop check is now available for the internal-\(W\) four-point cross-box sub-block. Contracting the four cross-box numerators with the longitudinal propagator projector gives the kernels
\[
\left(A_{01}^{(L)},A_{02}^{(L)},A_{05}^{(L)},A_{06}^{(L)}\right)
=\left(-\frac{2K}{d},-\!J+\frac{2K}{d},
-\frac{2K}{d},-\!J+\frac{2K}{d}\right),
\]
whose \(T_3\) projection vanishes. This establishes gauge-parameter independence of that fixed-routing cross-box subset. It does **not** evaluate the one-loop external-\(W\) form factor, nor the complete Slavnov–Taylor identity including external-leg, gauge-sector, and counterterm contributions. Accordingly, LD-W-FF remains **NOT EVALUATED**.

### 3.2 EFT one-\(W\) contact associated with the \(T_3\) derivative tensor

The tree-level singlet operator \(Q_{LD}\) has no direct \(W\) contact. The \(T_3\) tensor generated by the cross-box sub-block is a different weak contraction and must be covariantized in the triplet representation. Define
\[
X^I=\bar L\sigma^I H,\qquad
Y^I=H^\dagger\sigma^I L,\qquad
Q_{LD}^{(3)}=X^I i\gamma^\mu(D_\mu^{\rm adj}Y)^I.
\]
The Pauli identity
\[
\sum_I\sigma^I_{ij}\sigma^I_{kl}
=2\delta_{il}\delta_{kj}-\delta_{ij}\delta_{kl}
=(T_3)_{ij,kl}
\]
shows that this operator has precisely the \(T_3\) four-point tensor, with no extra normalization factor in the Pauli-matrix convention.

For \(D_\mu=\partial_\mu-i g_2 W_\mu^I\sigma^I/2\) on doublets, the triplet derivative is
\[
(D_\mu^{\rm adj}Y)^I
=\partial_\mu Y^I+g_2\epsilon^{IJK}W_\mu^JY^K.
\]
Consequently, if a local coefficient \(C_3\) multiplies \(Q_{LD}^{(3)}\), its EFT one-\(W\) contact is
\[
\boxed{
\mathcal L_{\rm contact}
=i g_2 C_3\epsilon^{IJK}
(\bar L\sigma^I H)\gamma^\mu W_\mu^J
(H^\dagger\sigma^K L).
}
\]
The Pauli completeness and adjoint-commutator identities are checked in calculations/RC-001-dim6-WW-triplet-current-contact.py (four local tests; captured output in validation/RC-001-dim6-WW-triplet-current-contact.txt). In the fixed all-incoming Fourier convention \(e^{-ipx}\) of the WW cross-box note, the raw amplitude coefficient \(C_3^{WW,\rm box}\) multiplies \(+\slashed P T_3\), while the matrix element of the displayed \(Q_{LD}^{(3)}\) carries \(p_3+p_4=-P\). Thus \(C_{Q_{LD}^{(3)}}^{WW,\rm box}=-C_3^{WW,\rm box}\); the contact sign must follow the operator coefficient, not the raw \(+\slashed P\) amplitude label.

The nonexceptional cross-box hard polynomial has now been decomposed into the independent off-shell momentum vectors
\[
v_D=p_3+p_4=-(p_1+p_2),\qquad
v_-=p_2-p_3,\qquad v_+=p_2+p_3.
\]
Its \(v_D\) coefficient is
\[
a(L)=-\frac12+\frac L2,\qquad L=\ln\frac{M_E^2}{\mu_R^2},
\]
while the other coefficients are \(b(L)=-1/32+7L/16\) and \(c(L)=7/32-5L/16\). Since the raw \(+\slashed P\) amplitude coefficient is \(-a\), the \(Q_{LD}^{(3)}\) operator coefficient is \(a\) in the stated Fourier convention. Restoring the common loop factor,
\[
C_{Q_{LD}^{(3)}}^{WW,\rm cross}
=\frac{g_2^2|y_\ell|^2}{16\pi^2M_E^2}
\left(-\frac12+\frac L2\right)
\]
for this fixed cross-box sub-block. At \(\mu_R=M_E\), this is \(-g_2^2|y_\ell|^2/(32\pi^2M_E^2)\). The corresponding EFT contact is obtained by inserting this coefficient into the boxed adjoint-derivative contact above. The \(v_-\) and \(v_+\) directions are retained as off-shell form factors and are not yet assigned to Warsaw-basis operators. The decomposition is checked in calculations/RC-001-dim6-WW-offshell-formfactor-decomposition.py and the contact coefficient in calculations/RC-001-dim6-WW-triplet-contact-from-hard-polynomial.py, with validation outputs under validation/.

For the purpose of constructing the **EFT local one-\(W\) contact** before EOM/IBP reduction, the two remaining directions can be represented by the gauge-covariant redundant off-shell operators
\[
\mathcal O_-^{(3)}
=T_{ij,kl}(\bar L_i\gamma^\mu L_l)\,
i\!\left[H_k^\dagger D_\mu H_j-(D_\mu H_k^\dagger)H_j\right],
\]
\[
\mathcal O_+^{(3)}
=T_{ij,kl}(\bar L_i\gamma^\mu L_l)\,
i\!\left[H_k^\dagger D_\mu H_j+(D_\mu H_k^\dagger)H_j\right],
\qquad T_{ij,kl}=\sum_A\sigma^A_{ij}\sigma^A_{kl}.
\]
Their four-point form factors are \(v_-=p_2-p_3\) and \(v_+=p_2+p_3\). Expanding the doublet covariant derivatives gives
\[
\mathcal L_{\mathcal O_-}^{W}
=2g_2 b\,T_{ij,kl}(\bar L_i\gamma^\mu L_l)
H_k^\dagger\frac{\sigma^J_{jm}}2H_m\,W_\mu^J,
\qquad
\mathcal L_{\mathcal O_+}^{W}=0.
\]
The latter cancellation follows because the gauge connections in \(H^\dagger D_\mu H+(D_\mu H^\dagger)H\) cancel. The Pauli contraction in the first contact is checked componentwise:
\[
T_{ij,kl}\frac{\sigma^J_{jm}}2
=\delta_{il}\sigma^J_{km}-\frac12\sigma^J_{im}\delta_{kl}.
\]
Thus, in this redundant off-shell basis, the full local contact implied by the hard polynomial is the sum of the \(Q_{LD}^{(3)}\) adjoint contact with coefficient \(a(L)\) and the \(\mathcal O_-^{(3)}\) contact with coefficient \(b(L)\); the \(v_+\) term has no direct \(W\) contact. The common factor \(g_2^2|y_\ell|^2/(16\pi^2M_E^2)\) multiplies \(a,b,c\). At \(\mu_R=M_E\), \(a=-1/2\) and \(b=-1/32\). The exact momentum/Pauli checks are in calculations/RC-001-dim6-WW-covariant-contact-completion.py and validation/RC-001-dim6-WW-covariant-contact-completion.txt.

This constructs the **EFT local contact in a redundant gauge-covariant basis**. It is still not the UV one-loop five-point form factor, and it is not yet a Warsaw-basis coefficient: the Hermitian completion, EOM/IBP reduction, and external-leg emissions remain to be included.

This is the **EFT contact implied by the local triplet derivative operator**, not the UV one-loop five-point form factor. It does not close LD-W-FF or determine the final \(C_{H\ell}^{(3)}\) coefficient. The UV current amplitude, its common off-shell EFT subtraction, the other derivative tensors, and the EOM/IBP projection remain required.

### 3.3 Exact Pauli-Fierz map before applying equations of motion

The four-point \(T_3\) derivative structure must not be identified directly with the Warsaw-basis \(O_{H\ell}^{(3)}\). Applying the Pauli completeness relation to the *entire covariant derivative*, including its adjoint connection, gives the exact off-shell identity
\[
\begin{aligned}
Q_{LD}^{(3)}
={}&2i\big[(D_\mu H)^\dagger H\big]
       (\bar L\gamma^\mu L)
+2(H^\dagger H)(\bar L i\slashed D L)\\
&-Q_{LD}.
\end{aligned}
\]
Here \(Q_{LD}=(\bar L H)i\slashed D(H^\dagger L)\) uses the same field ordering and covariant-derivative convention as above. Equivalently, since
\[
2i(D_\mu H)^\dagger H
=i\partial_\mu(H^\dagger H)
-H^\dagger i\overleftrightarrow D_\mu H,
\]
one has
\[
\boxed{
Q_{LD}^{(3)}+Q_{LD}
=
\big[i\partial_\mu(H^\dagger H)
-H^\dagger i\overleftrightarrow D_\mu H\big]
(\bar L\gamma^\mu L)
+2(H^\dagger H)(\bar L i\slashed D L).
}
\]
This identity is off shell: the last term must **not** be discarded before the light-lepton equation of motion is applied. With the SM Yukawa convention
\[
\mathcal L_Y=-\bar L Y_e H e_R+\mathrm{h.c.},
\qquad i\slashed D L=Y_e H e_R,
\]
the last term maps into the corresponding Higgs-dressed Yukawa/source operator. The total derivative term can be integrated by parts only together with the divergence of the lepton current; that divergence is also controlled by the Yukawa EOM. Therefore the triplet box projection feeds a correlated set of \(O_{H\ell}^{(1)}\)-type current, \(Q_{LD}\), and Yukawa-source representatives before basis reduction. It is not a stand-alone \(O_{H\ell}^{(3)}\) coefficient.

For completeness, with the SM lepton equations of motion in the convention above,
\[
i\slashed D L=Y_e H e_R,\qquad
i(D_\mu\bar L)\gamma^\mu=-\bar e_RY_e^\dagger H^\dagger,
\]
the current divergence is
\[
\partial_\mu(\bar L\gamma^\mu L)
=i\big(\bar e_RY_e^\dagger H^\dagger L
-\bar L Y_e H e_R\big).
\]
After integration by parts and use of these EOM, the preceding off-shell identity becomes
\[
\boxed{
Q_{LD}^{(3)}+Q_{LD}
\doteq
-\,O_{H\ell}^{(1)}
+(H^\dagger H)
\big(\bar e_RY_e^\dagger H^\dagger L
+\bar L Y_e H e_R\big),
}
\]
where
\[
O_{H\ell}^{(1)}
=(H^\dagger i\overleftrightarrow D_\mu H)
(\bar L\gamma^\mu L),
\]
and \(\doteq\) denotes equality modulo a total derivative and the light-field EOM. The Yukawa-source term is the Hermitian pair required by the EOM reduction; it is not optional. This gives the operator-level destination of the \(T_3\) derivative tensor in the stated convention. It does not by itself determine its Wilson coefficient, because the full UV/EFT one-\(W\) amplitude and all other matching sub-blocks must still be summed.

The identity follows directly by expanding
\[
(\bar L_i\sigma^I_{ij}H_j)i\gamma^\mu
\big[(D_\mu H^\dagger)_k\sigma^I_{kl}L_l
+H^\dagger_k\sigma^I_{kl}D_\mu L_l\big]
\]
and using \(\sigma^I_{ij}\sigma^I_{kl}
=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}\). No on-shell condition, gauge choice, or loop integral is used. The operator-basis projection must preserve the same convention for \(Q_{LD}\), the SM Yukawa sign, and the total-derivative/EOM source terms.

### 3.4 Exact EFT one-\(W\) contact and local gauge-covariance check

The local contact vertices implied by the fixed internal-\(W\) hard polynomial are now recorded in research/RC-001-dim6-WW-fivepoint-EFT-ward.md. In the redundant off-shell basis \(F(aQ_D^{(3)}+bO_-^{(3)}+cO_+^{(3)})\), with \(F=g_2^2|y_\ell|^2/(16\pi^2M_E^2)\), the direct one-\(W\) contacts are
\[
F g_2 W_\mu^J\left[
ia\,\epsilon^{IJK}(\bar L\sigma^I H)\gamma^\mu(H^\dagger\sigma^K L)
+2b\,T_{3(ij,kl)}(\bar L_i\gamma^\mu L_l)
H_k^\dagger\left(\frac{\sigma^J}{2}\right)_{jm}H_m
\right],
\]
while \(O_+^{(3)}\) has zero direct contact. At \(\mu_R=M_E\), \(a=-1/2\), \(b=-1/32\), giving coefficients \(-ig_2F/2\) and \(-g_2F/16\).

The accompanying exact SymPy audit verifies the adjoint commutator and local-gauge cancellation in \(D_\mu^{\rm adj}Y\), invariance of the \(T_3\) tensor under all four doublet transformations, and the Pauli-generator contact contraction for all three \(W^I\). Five local regression tests pass. The explicit-log slopes are \(\mathrm d(a,b,c)/\mathrm d\ln\mu_R=(-1,-7/8,5/8)\); these are not the complete anomalous dimensions.

This closes only the **EFT local-contact/covariance** part for the stated hard sub-block. The UV one-loop external-\(W\) five-point form factor, its transverse part, the full external-leg/gauge-sector/counterterm set, and the complete Slavnov–Taylor sum remain unevaluated. Sources: calculations/RC-001-dim6-WW-fivepoint-EFT-ward.py, calculations/test_RC001_dim6_WW_fivepoint_EFT_ward.py, validation/RC-001-dim6-WW-fivepoint-EFT-ward.txt.

## 4. Form-factor decomposition and matching record

Use common nonexceptional off-shell external momenta (or one common infrared regulator) and the same gauge-fixing, \(\overline{\mathrm{MS}}\), and external-field conventions on both sides. For each amplitude, record separately:

- the tree-level form factor;
- the one-loop UV vertex/form-factor contribution;
- UV and IR poles before subtraction;
- the EFT soft contribution, including the derivative-contact graphs;
- external-field and parameter counterterms;
- the finite local polynomial after UV–EFT subtraction;
- the projection onto the chosen nonredundant current/operator basis;
- the gauge-EOM image, if used, and all induced current-current/source companions.

For a fermion current, retain a complete off-shell transverse/longitudinal tensor basis until the Ward identity is checked; do not infer a local Wilson coefficient from a single on-shell form factor. For a scalar current, keep the independent \((p+p')^\mu\) and \(q^\mu\) structures until the same projection is performed. The tensor basis and normalization must be identical in UV and EFT. The already-derived diagonal-gauge (y,\lambda,M_E) parameter-counterterm pieces are tabulated in `research/RC-001-dim6-gauge-parameter-counterterms.md`; the (Q_{LD}) internal-(W) weak-index contractions are tabulated in `research/RC-001-dim6-SU2-attachment-projection.md`. Neither record supplies the missing current-form-factor loop integrals.

The Ward-Takahashi/Slavnov-Taylor check is applied to the summed amplitude including external-leg pieces and contact vertices. A stripped vertex graph alone is insufficient. After the UV–EFT difference, separate local 1PI coefficients from gauge-reducible current exchange and apply gauge-field EOM only once.

## 5. Evidence ledger

| ID | UV graph/form-factor data | EFT subtraction | Counterterms and consistency tests | Status |
|---|---|---|---|---|
| LD-B-FF | External \(B\) on \(E,L,H\) lines plus all compatible one-loop gauge families | \(Q_{LD}\) insertion, \(B\)-contact, external-line and mixed-propagator graphs if retained | \(B\) field/input renormalization, Ward identity, local/reducible separation | NOT EVALUATED |
| LD-W-FF | External \(W^I\) on doublet fermion/scalar lines plus required gauge-sector graphs | Tree \(Q_{LD}\) insertion and external-line \(W\) graphs; include the triplet redundant-basis contacts in §3.4 | Weak tensor, UV five-point amplitude, Slavnov-Taylor identity, gauge/ghost and external-field terms | PARTIAL: EFT local contact/covariance checked; UV five-point NOT EVALUATED |
| LD-X-FF | External \(A'\) on \(E,L\) lines; include kinetic-mixing effects where applicable | \(Q_{LD}\) insertion and \(A'\)-contact graphs | Signed flavor charges, mixing boundary, current/EOM bookkeeping | NOT EVALUATED |
| RD-B-FF | External \(B\) on \(E,\ell_R\) lines | \(Q_{RD}\) insertion and \(B\)-contact graphs | Hypercharge/input counterterms, Ward identity | NOT EVALUATED |
| RD-X-FF | External \(A'\) on \(E,\ell_R,S\) lines | \(Q_{RD}\) insertion and \(A'\)-contact graphs | Signed flavor/scalar charges, mixing boundary, Ward identity | NOT EVALUATED |
| MIX-FF | External-field rotations and mixed \(B-A'\) propagator contributions | Same full kinetic matrix and renormalization boundary on EFT side | No implicit \(\chi(\mu_R)=0\); state it as an input if chosen | CONDITIONAL / NOT EVALUATED |
| BASIS-FF | Sum all UV form-factor tensors at the same coupling order | Subtract matching EFT tensors before reduction | Apply Ward identities, EOM/IBP and current-source mapping once; keep reducible exchange separate | OPEN |

## 6. Explicit non-claims and closure

No finite \(O(g^2/M_E^2)\) fermionic current-form-factor coefficient is claimed in this file. The existing master §254 bosonic coefficients remain separate. The current environment lacks FeynArts/FeynCalc and equivalent diagram-level tools; independent graph-level signs, multiplicities and loop numerators remain unverified. CI is skipped by explicit project decision and is not a closure gate, but this does not waive the missing physics evidence.

Close these rows only after the individual UV and EFT form factors have been calculated, their UV/IR poles and counterterms documented, Ward identities verified on the summed amplitudes, and local/reducible contributions projected into the common operator basis. PR #4 remains Draft/Open until those physics requirements are met.
