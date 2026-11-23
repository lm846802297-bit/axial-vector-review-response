# RC-001 — Common-\(k\) ordinary-matter longitudinal assembly ledger

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-g/02  
**Status:** the pairwise ingredients are indexed: cross-vertex and same-vertex fermion WTIs, six scalar-line/seagull endpoint kernels, six graph-specific \(R_{\rm FG}\) current projections, orientation-dependent three-W phases, the local Yukawa-singlet endpoint cancellation with common heavy-channel routing, the 1PI/1PR LSZ boundary, the exact longitudinal inverse-kernel completion target for \(R_{\rm FG}\), the IVn-e audit of momentum-dependent scalar-current routing, the exact three-W internal-leg exchange identity at the vertex/group-factor level, and seven exact scalar/fermion-line versus three-W denominator-factor relations. The IVh arbitrary-current identity was not sufficient by itself to establish graph-specific scalar-current cancellation. IVn-f/01–05 now insert the actual currents, ordered Dirac chains, shifted denominators, and scalar-line/seagull endpoint structures for all six pair classes; the full ordinary-matter longitudinal sum remains open. IVn-f/01 now closes the actual LD-W-01 F-F commutator/three-W sub-block with its explicit Dirac chain, physical weak tensor, relative phase, and complete spectator denominators; it leaves the explicit nonzero R_FG projection. IVn-f/02 now separates LD-W-02 into its A-side fermion/three-W sub-block and B-side scalar-line/seagull kernel, and derives the exact (V_B(k)=V_B(\kappa)+q) rebase with both symmetric and commutator (q^\mu) contacts retained. IVn-f/03 now adds the LD-W-05 A-side scalar split, with the symmetric and commutator q^mu contacts retained. IVn-f/04 completes the pair-specific LD-W-03/04 same-vertex endpoint bridge: V_S^line=V_S^3W-q, the symmetric and commutator q^mu contacts remain separate, and both Dirac-Hermitian R_FG chains and heavy spectators are checked. IVn-f/05 completes the pair-specific LD-W-06 S-S endpoint bridge: A and B currents are rebased separately, with (V_A^{\rm line}=V_A^{3W}-q) and (V_B^{\rm line}=V_B^{3W}+q); their two seagulls and weak tensors remain distinct. IVn-g/01 now audits the secondary shifts of the two LD-W-06 scalar-line \(-\Delta_W\) terms: the scalar/W/current factors align, but the heavy channel shifts to (h-q) on A and (h+q) on B. These terms cannot be identified pointwise with the unshifted (h)-channel three-W integrand. IVn-g/03 extends the shifted Yukawa-singlet channel check to all six pair classes: cross A variations share (h-q), cross B variations share (h+q), and same-vertex (h_E) is k-independent. The local left/right charge sums pass 192/192 weak components. IVn-h/01 now inserts both actual LD-W-01 fermion WTI contractions into their Feynman-gauge open chains. The A-side second endpoint maps to the κ-W denominator and the B-side second endpoint already uses the k-W denominator; both align with the corresponding three-W propagator factors. The first A/B endpoint terms remain explicit. IVn-h/02 now inserts the A-side LD-W-02 fermion WTI into the actual F-S open chain with the B scalar current (V_B(\kappa)), the κ-W propagator, and the heavy/scalar spectators. The open-index identity passes 64/64 matrix components and the contracted chain passes 16/16. IVn-h/03 now inserts the B-side LD-W-05 fermion WTI into the actual ordered S-F open chain with (V_A(k)), the k-W propagator, and the A-scalar/heavy spectators. The open-index identity passes 64/64 matrix components and the contracted chain passes 16/16. The separate (R_{\rm FG}) projector/order comparison remains open. This is not yet a summed Slavnov–Taylor identity. IVn-h/04 now inserts both same-vertex LD-W-03/04 fermion WTIs into their separate left-/right-open chains, with their graph-specific (h_E) spectators and (V_S(k)D(k)) contractions. Each open-index comparison passes 64/64 matrix components and each contracted chain passes 16/16; the two heavy spectators are independently checked to be k-independent. The scalar symmetric and commutator tensors remain distinct; reducible external-leg/LSZ terms and the gauge-fixing/ghost sector remain separate. IVn-h/05 reconciles the LD-W-05 B-oriented WTI projectors: both endpoint terms reduce to the same right-chiral open-chain orientation, with distinct r_B^W/r_B^Y momenta retained; the single-W endpoints remain distinct from the two-W R_FG numerator. IVn-h/06 similarly reconciles the LD-W-02 A-oriented F-S endpoint projectors: both terms share the rightmost P_L and ordered gamma_mu slash(r_A) slash(h_A) chain, retaining distinct r_A^W/r_A^Y momenta. Its single-W endpoints remain distinct from the two-W R_FG numerator. Both are projector-order checks, not cancellations.

## 1. Frozen common-\(k\) definitions

Write
\[
\kappa=k+q,\qquad p_4=-p_1-p_2-p_3-q.
\]
For cross-vertex \(A\to B\) pairs,
\[
r_A=k-p_A,\qquad r_B^Y=k+p_B+q,\qquad h=k-p_1-p_2.
\]
For same-vertex \(S\to F\) pairs,
\[
r_F^W=k+p_F,\qquad r_F^Y=k+p_F+q,\qquad
r_S^Y=p_S-k,\qquad h_E=p_F+p_S+q.
\]
The same-vertex \(h_E\) is independent of \(k\) and its heavy propagator remains a spectator.

The already validated shifts are:
- cross A-side Yukawa endpoint and A scalar seagull: \(k_{\rm old}=k+q\), with internal-W momentum \(\kappa\);
- cross B-side Yukawa endpoint and B scalar seagull: no shift, with internal-W momentum \(k\);
- same-vertex F-side Yukawa endpoint: no shift;
- same-vertex S-side Yukawa endpoint and S seagull: \(k_{\rm old}=k+q\), with internal-W momentum \(\kappa\).

## 2. Pair-by-pair ingredient map

| Pair | Fermion-line WTI | Scalar line + seagull | Three-W orientation and phase-weighted group tensor | Explicit RFG chain |
|---|---|---|---|---|
| LD-W-01 (F–F) | A-oriented and B-oriented WTIs | none | \(A\to B:\ -ig_2\mathcal G_{AB}\) | \(\mathcal N_{01}\), with \(-\slashed r_A\,\slashed h\,\slashed r_B^Y\) |
| LD-W-02 (F–S) | A-oriented WTI | B scalar: \(\mathcal C_B\), one seagull | \(A\to B:\ -ig_2\mathcal G_{AB}\) | \(\mathcal N_{02}\), with \(-\slashed r_A\,\slashed h\,V_B\) |
| LD-W-03 (F–S) | same-vertex LD-W-03 WTI | S scalar: \(\mathcal C_S\), one seagull | \(S\to F:\ +ig_2\mathcal G_{FS}\) | \(\mathcal N_{03}\), order \(\slashed k\slashed r_F^Y\) |
| LD-W-04 (S–F) | same-vertex LD-W-04 conjugate WTI | S scalar: \(\mathcal C_S\), one seagull | \(S\to F:\ +ig_2\mathcal G_{FS}\) | \(\mathcal N_{04}\), order \(\slashed r_F^Y\slashed k\) |
| LD-W-05 (S–F) | B-oriented WTI | A scalar: \(\mathcal C_A\), one seagull | \(A\to B:\ -ig_2\mathcal G_{AB}\) | \(\mathcal N_{05}\), with \(V_A\,\slashed h\,\slashed r_B^Y\) |
| LD-W-06 (S–S) | none | A scalar \(\mathcal C_A\) and B scalar \(\mathcal C_B\), two separate seagulls | \(A\to B:\ -ig_2\mathcal G_{AB}\) | \(\mathcal N_{06}\), with \(V_A\,\slashed h\,V_B\) |

The exact \(R_{\rm FG}\) numerators and denominators are recorded in
\`research/RC-001-dim6-WW-fivepoint-explicit-RFG-six-pair-currents.md\`.
The actual scalar-line/seagull kernels and their \(\mathcal S_X/\mathcal G_{\rm orient}\) tensors are recorded in
\`research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md\`.
The same-vertex fermion WTI orientations are recorded in
\`research/RC-001-dim6-WW-fivepoint-same-vertex-fermion-WTI.md\`.

## 3. Fermion-line Ward identities

The cross-vertex identities remain the B2c-I/II conventions:
\[
S_F(-r_A^W)\slashed qP_LS_F(-r_A^Y)
=S_F(-r_A^W)P_R-P_LS_F(-r_A^Y),
\]
\[
S_F(r_B^Y)\slashed qP_LS_F(r_B^W)
=P_LS_F(r_B^W)-S_F(r_B^Y)P_R.
\]
For the same-vertex pairs, the explicit newly derived identities are
\[
\boxed{
S_F(r_F^W)\slashed qP_LS_F(r_F^Y)
=S_F(r_F^W)P_R-P_LS_F(r_F^Y)
\quad(\mathrm{LD\!-\!W\!-\!03}),
}
\]
\[
\boxed{
S_F(r_F^Y)\slashed qP_LS_F(r_F^W)
=P_LS_F(r_F^W)-S_F(r_F^Y)P_R
\quad(\mathrm{LD\!-\!W\!-\!04}).
}
\]
The two same-vertex identities are related by Dirac-Hermitian conjugation but retain opposite open-line order. The heavy channel \(S_E(h_E)\) is a spectator and is not differentiated with respect to \(k\).

## 4. What the common-\(k\) kernel cancellation does establish

For the cross-vertex group phase \(-ig_2\mathcal G_{AB}\), and the same-vertex phase \(+ig_2\mathcal G_{FS}\), the universal matter-line commutator kernel and the contracted three-W transverse inverse-kernel difference have already been aligned at common \(k\). Their \(D(k)-D(\kappa)\) pieces cancel in the universal arbitrary-current sub-block, leaving
\[
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-\kappa^\mu\kappa^\nu}{k^2\kappa^2}.
\]
The IVl source inserts the six graph-specific currents into the residual tensor. However, IVn-e finds that the scalar derivative currents used in IVl and IVm are evaluated at different shifted momenta: \(V_A(k)-V_A(\kappa)=q\), \(V_B(k)-V_B(\kappa)=q\), and \(V_S(k)-V_S(\kappa)=q\). The IVh arbitrary-current test uses independent momentum-independent symbols for its endpoint currents, so it proves the tensor identity but does not yet prove the graph-specific cancellation after these scalar-current shifts. The exact six-endpoint diagnostic is recorded in `research/RC-001-dim6-WW-fivepoint-momentum-dependent-scalar-current-audit.md`. IVn-e also checks seven exact denominator-factor relations. In the cross A/B and same-vertex F/S line insertions, an adjacent matter propagator replaces the second W propagator in the corresponding three-W denominator; the seagull denominators are the three-W denominator divided by the relevant W virtuality. These relations are recorded in the IVn-e audit. No physical non-cancellation is claimed; the loop-variable/routing bridge remains to be derived. IVn-d separately identifies \(R_{\rm FG}\) as the negative of the propagator-sandwiched longitudinal inverse-kernel difference: with \(L_{\mu\nu}(p)=p_\mu p_\nu\), \(D(\kappa)[L(\kappa)-L(k)]D(k)=-R_{\rm FG}\). Thus \(K+L=p^2g\) closes the inverse-kernel algebra. This is the tensor target for the BRST/ghost STI, not proof that a ghost graph by itself cancels the matter-chain remainder.

### 4.1 LD-W-01 graph-specific control result (IVn-f/01)

For \(A=\bar L,\ B=L\), the actual chain
\[
\mathcal X_{01}=-\slashed r_A\slashed h\slashed r_B^Y P_L
\]
has been inserted into the Feynman-gauge inverse-kernel identity. The A-side Yukawa-endpoint shift \(k_{\rm old}=k+q\) and the unshifted B-side map align the two single-W denominator terms with the three-W reference. The physical A/B commutator tensors both give \(-ig_2\mathcal G_{AB}^a\), and the actual matrix contraction gives
\[
\mathcal M_{01,\mathrm{comm}+3W}
=\frac{-ig_2\mathcal G_{AB}^a}
{r_A^2(r_B^Y)^2(h^2-M_E^2)}
\frac{\mathcal N_{01}}{k^2\kappa^2}.
\]
This is precisely the retained \(R_{\rm FG}\) projection in the isolated commutator/three-W sub-block. It is not the full LD-W-01 five-point Ward identity: Yukawa-endpoint gauge variations, external legs, ghosts, counterterms, and UV–EFT subtraction remain outside this calculation.

The exact source and six local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-01-common-k-numerator-denominator.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_01_common_k_numerator_denominator.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-01-common-k-numerator-denominator.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-01-common-k-numerator-denominator.txt\`

### 4.2 LD-W-02 graph-specific endpoint split (IVn-f/02)

For \(A=\bar L,\ B=H^\dagger\), the A-side fermion Yukawa-endpoint shift \(k_{\rm old}=k+q\) maps the B scalar current to \(V_B(\kappa)\), exactly the current in the three-W graph. Its single-W denominator is \(\mathscr D_{3W}^{02}/k^2\).

The B-side scalar-line/seagull kernel is a distinct sub-block. It contains \(V_B(k)\), \(\delta_B=\Delta_Y-\Delta_W\), and the seagull contact \(\Delta_Yq^\mu\). Re-expressing it in the three-W current basis gives
\[
\begin{aligned}
\mathcal C_B^\mu=g_2\Big[
&\tfrac12\delta_BV_B^\mu(\kappa)\mathcal S_B^a
+(\tfrac12\delta_B+\Delta_Y)q^\mu\mathcal S_B^a\\
&+\tfrac i2\delta_BV_B^\mu(\kappa)\mathcal G_{AB}^a
+\tfrac i2\delta_Bq^\mu\mathcal G_{AB}^a
\Big].
\end{aligned}
\]
The last two \(q^\mu\) terms are kept separately in the symmetric and commutator weak tensors. At the exact rational diagnostic point \(\delta_B=9/380\), and the commutator \(q^\mu\) contact produces a nonzero 16/16 Dirac matrix. This is not evidence of a physical non-cancellation; its combination with external-field/Yukawa endpoint variations and LSZ terms remains open.

The exact source and six local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-02-common-k-FS-endpoint-split.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_02_common_k_FS_endpoint_split.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-02-common-k-FS-endpoint-split.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-02-common-k-FS-endpoint-split.txt\`

### 4.3 LD-W-05 graph-specific endpoint split (IVn-f/03)

For \(A=H,\ B=L\), the unshifted B-side fermion Yukawa-endpoint term carries \(V_A(k)\), exactly the A-scalar current in the three-W graph. Its denominator is \(\mathscr D_{3W}^{05}/\kappa^2\).

The A-side scalar-line/seagull kernel instead contains \(V_A^{\rm line}=2p_2-\kappa\), while the three-W current is \(V_A^{3W}=2p_2-k\). Since \(V_A^{\rm line}=V_A^{3W}-q\), the exact rebased current is
\[
\begin{aligned}
\mathcal C_A^\mu=g_2\Big[
&-\tfrac12\delta_AV_A^{3W,\mu}\mathcal S_A^a
+(\tfrac12\delta_A+\Delta_Y)q^\mu\mathcal S_A^a\\
&-\tfrac i2\delta_AV_A^{3W,\mu}\mathcal G_{AB}^a
+\tfrac i2\delta_Aq^\mu\mathcal G_{AB}^a
\Big].
\end{aligned}
\]
At the exact rational diagnostic point \(\delta_A=-6/391\); the commutator \(q^\mu\) contact produces a nonzero 16/16 Dirac matrix. It is retained and is not interpreted as a physical non-cancellation.

The exact source and six local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-05-common-k-SF-endpoint-split.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_05_common_k_SF_endpoint_split.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-05-common-k-SF-endpoint-split.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-05-common-k-SF-endpoint-split.txt\`

The scalar-line/seagull sub-block is now also explicit. Its weak tensors remain
\[
\mathcal S_X^a
\quad\text{and}\quad
\mathcal G_{AB}^a\ \text{or}\ \mathcal G_{FS}^a
\]
as separate structures. The local Yukawa-singlet endpoint variation is now checked separately: \( (R_{\bar L}^a+R_H^a)T_0=0 \) and \( (R_{H^\dagger}^a+R_L^a)T_0=0 \), and the common-​\(k\) shifts show that the two fields at each Yukawa vertex multiply the same heavy-channel spectator. This closes the local charge-sum sub-block. It does not yet provide the complete reducible external-leg/LSZ contribution or the full gauge variation of the amputated Green function. Do not infer a complete scalar-endpoint cancellation merely from the universal arbitrary-current kernel identity.

### 4.4 LD-W-03/04 same-vertex S-to-F endpoint bridge (IVn-f/04)

The same-vertex scalar endpoint has a different current rebase from both cross-vertex scalar cases. With
\[
r_S^Y=p_S-k,\quad r_S^W=p_S-\kappa,\quad
\Delta_{Y,W}=1/(r_S^{Y,W})^2,\quad \delta_S=\Delta_Y-\Delta_W,
\]
the S-to-F scalar WTI gives
\[
q\cdot(r_S^W+r_S^Y)\Delta_W\Delta_Y
=\Delta_W-\Delta_Y=-\delta_S.
\]
The scalar-line current is \(V_S^{\rm line}=2p_S-\kappa\), while the three-W current is \(V_S^{3W}=2p_S-k\), so \(V_S^{\rm line}=V_S^{3W}-q\). The exact rebased scalar-line/seagull current is
\[
\begin{aligned}
\mathcal C_S^\mu=g_2\Big[
&\tfrac12\delta_S V_S^{3W,\mu}\mathcal S_S^a
+\tfrac12(\Delta_Y+\Delta_W)q^\mu\mathcal S_S^a\\
&+\tfrac i2\delta_S V_S^{3W,\mu}\mathcal G_{FS}^a
-\tfrac i2\delta_Sq^\mu\mathcal G_{FS}^a
\Big].
\end{aligned}
\]
Thus the symmetric and commutator contacts have coefficients \((\Delta_Y+\Delta_W)/2\) and \(-i\delta_S/2\), respectively. This is not the LD-W-02 B-side or LD-W-05 A-side formula with a relabelled endpoint.

The common shift \(k_{\rm old}=k+q\) maps the original scalar-line momenta to
\[
r_S^S\to r_S^W,\quad r_S^Y\to r_S^Y,\quad
r_F^W\to r_F^Y,\quad k_S\to\kappa,\quad
V_S\to V_S^{\rm line}.
\]
Moreover,
\[
\Delta_W(k)=\Delta_Y(k+q),\quad
r_F^Y(k)=r_F^W(k+q),\quad
V_S^{\rm line}(k)=V_S^{3W}(k+q).
\]
Therefore the \(-\Delta_W\) part of the scalar WTI maps, after \(k\to k+q\), to the corresponding F-side endpoint routing. The seagull denominator is exactly \(D_{3W}/k^2\); the scalar-line graph retains both scalar propagators and must not be assigned the seagull denominator.

The actual ordered kernels are
\[
\mathcal K_{03,S}=\slashed{\mathcal C}_S\slashed r_F^Y/\kappa^2,\qquad
\mathcal K_{04,S}=\slashed r_F^Y\slashed{\mathcal C}_S/\kappa^2,
\]
and the corresponding three-W remainders retain
\[
\begin{aligned}
\mathcal N_{03}&=(V_S^{3W}\cdot k)\slashed k\slashed r_F^Y
-(V_S^{3W}\cdot\kappa)\slashed\kappa\slashed r_F^Y,\\
\mathcal N_{04}&=(V_S^{3W}\cdot k)\slashed r_F^Y\slashed k
-(V_S^{3W}\cdot\kappa)\slashed r_F^Y\slashed\kappa.
\end{aligned}
\]
The chiral heavy propagator \(P_R(\slashed h_E+M_E)P_L/(h_E^2-M_E^2)\) remains a \(k\)-independent spectator in the original seed order.

The exact source and seven regression tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_03_04_common_k_same_vertex_endpoint_split.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.txt\`

The exact rational checks use two nonsingular points for both pair orientations. They confirm 64/64 direct-versus-factorized \(R_{\rm FG}\) matrix components and 64/64 raw-versus-rebased scalar-kernel components. The two q-contact matrices remain nonzero. The weak-index checks reproduce the S-to-F group-phase identity, but do not claim the Lorentz-weighted four-attachment cancellation.

### 4.5 LD-W-06 two scalar endpoints (IVn-f/05)

LD-W-06 has two independent scalar-line/seagull sub-blocks. For the A endpoint,
\[
V_A^{\rm line}=V_A^{3W}-q,\qquad
\mathcal C_A^\mu=g_2\left[
-\tfrac12\delta_AV_A^{3W,\mu}\mathcal S_A^a
+(\Delta_{AY}+\tfrac12\delta_A)q^\mu\mathcal S_A^a
-\tfrac i2\delta_AV_A^{3W,\mu}\mathcal G_{AB}^a
+\tfrac i2\delta_Aq^\mu\mathcal G_{AB}^a
\right].
\]
For the B endpoint,
\[
V_B^{\rm line}=V_B^{3W}+q,\qquad
\mathcal C_B^\mu=g_2\left[
\tfrac12\delta_BV_B^{3W,\mu}\mathcal S_B^a
+(\Delta_{BY}+\tfrac12\delta_B)q^\mu\mathcal S_B^a
+\tfrac i2\delta_BV_B^{3W,\mu}\mathcal G_{AB}^a
+\tfrac i2\delta_Bq^\mu\mathcal G_{AB}^a
\right].
\]
The actual contracted kernels are
\[
\mathcal K_{06,A}=\slashed h(V_B^{3W}\cdot\mathcal C_A)/\kappa^2,\qquad
\mathcal K_{06,B}=(V_A^{3W}\cdot\mathcal C_B)\slashed h/k^2.
\]
The A/B seagull tensors remain
\[
\mathcal S_A^a=\tfrac12R_B^aT_0,\qquad
\mathcal S_B^a=\tfrac12R_A^aT_0.
\]
They are not identified, even though both commutators use \(\mathcal G_{AB}^a\).

The seagull denominators satisfy \(D_{A,\rm sg}=D_{3W}/k^2\) and \(D_{B,\rm sg}=D_{3W}/\kappa^2\). The scalar-line denominators retain both propagators on their respective scalar lines. The actual S-S \(R_{\rm FG}\) numerator is
\[
\mathcal N_{06}
=(V_A^{3W}\cdot k)\slashed h(V_B^{3W}\cdot k)
-(V_A^{3W}\cdot\kappa)\slashed h(V_B^{3W}\cdot\kappa).
\]
Two nonsingular rational points verify the direct Lorentz contraction (32/32 matrix components) and the A/B raw-to-rebased endpoint kernels (64/64 matrix components). All four A/B symmetric/commutator \(q^\mu\) contacts remain nonzero.

The exact source and six local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_common_k_SS_two_endpoint_bridge.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.txt\`

This closes the pair-specific endpoint-current rebase for LD-W-06, not the complete S-S four-attachment Ward sum.

### 4.6 LD-W-06 secondary scalar shifts change the heavy channel (IVn-g/01)

The second loop shifts needed to align the \(-\Delta_W\) terms are not innocuous. For the A-side term, set \(k_A'=k+q\). The scalar and current factors map as
\[
\kappa(k)\to k_A',\quad
r_A^W(k)\to r_A^Y(k_A'),\quad
r_B^Y(k)\to r_B^W(k_A'),
\]
\[
V_A^{\rm line}(k)\to V_A^{3W}(k_A'),\quad
V_B^{3W}(k)\to V_B^{\rm line}(k_A').
\]
But
\[
\boxed{h(k)=h(k_A')-q.}
\]
The shifted heavy denominator is \((h(k_A')-q)^2-M_E^2\), not the original \(h(k_A')^2-M_E^2\).

For the B-side term, set \(k_B'=k-q\). Then
\[
k\to\kappa(k_B'),\quad
r_A^Y(k)\to r_A^W(k_B'),\quad
r_B^W(k)\to r_B^Y(k_B'),
\]
\[
V_A^{3W}(k)\to V_A^{\rm line}(k_B'),\quad
V_B^{\rm line}(k)\to V_B^{3W}(k_B'),
\]
whereas
\[
\boxed{h(k)=h(k_B')+q.}
\]
Its heavy denominator is \((h(k_B')+q)^2-M_E^2\).

The generic identities are
\[
(h-q)^2-M_E^2=(h^2-M_E^2)+q^2-2h\cdot q,
\]
\[
(h+q)^2-M_E^2=(h^2-M_E^2)+q^2+2h\cdot q.
\]
At the exact rational point used in IVn-g/01,
\[
H_0=-377,\qquad H_A=-389,\qquad H_B=-365.
\]
The scalar/W/current factors align under each secondary shift, but the heavy denominators remain distinct. This is not a physical non-cancellation: the shifted terms must be compared with the corresponding Yukawa-endpoint and reducible LSZ contributions. The previous local Yukawa-singlet charge check was performed at the first common-\(k\) routing; its extension to these \(h\pm q\) channels is an explicit remaining check.

The exact source and six local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_secondary_shift_heavy_channel_audit.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.txt\`

IVn-g/02 extends the local Yukawa-singlet charge check to these shifted channels: the two left-vertex variations share (h-q), and the two right-vertex variations share (h+q), so both local charge sums still vanish. This is a precise routing/denominator result, not a completed Ward identity.

### 4.7 Shifted LD-W-06 Yukawa-singlet charge factors (IVn-g/02)

The secondary shifts change the heavy channel but do not split the two field variations at either Yukawa singlet:
\[
k_A'=k+q:\quad h_{\bar L}=h_H=h(k_A')-q,
\]
\[
k_B'=k-q:\quad h_{H^\dagger}=h_L=h(k_B')+q.
\]
The physical charge sums therefore remain
\[
(R_{\bar L}^a+R_H^a)T_0\,S_E(h-q)X_A=0,\qquad
(R_{H^\dagger}^a+R_L^a)T_0\,S_E(h+q)X_B=0.
\]
The exact check passes 8/8 vector components for each heavy-channel map and 96/96 weak-index components for the shifted singlet charge sums. This is a local endpoint-factor cancellation; it does not sum the scalar-line/three-W Lorentz kernels or the reducible LSZ terms.

The exact source and five local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_shifted_Yukawa_singlet_charge_closure.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.txt\`

### 4.8 Shifted Yukawa-singlet channels for all six pairs (IVn-g/03)

The local charge-factor check now covers every pair class:
\[
\begin{array}{c|c|c}
\text{endpoint class}&\text{secondary shift}&\text{common heavy channel}\\ \hline
\text{cross A: LD-W-01/02/05/06}&k'=k+q&h(k')-q\\
\text{cross B: LD-W-01/02/05/06}&k'=k-q&h(k')+q\\
\text{same vertex: LD-W-03/04}&k'\!=k\pm q&h_E=p_F+p_S+q
\end{array}
\]
At each left Yukawa singlet the two field variations \(\bar L,H\) carry the same \(S_E(h-q)\); at each right singlet \(H^\dagger,L\) carry the same \(S_E(h+q)\). For LD-W-03/04 the heavy spectator \(S_E(h_E)\) is independent of the loop shift. The physical charge sums remain
\[
(R_{\bar L}^a+R_H^a)T_0=0,\qquad
(R_{H^\dagger}^a+R_L^a)T_0=0.
\]
The all-six audit passes 8/8 cross-A vector components, 4/4 cross-B components, 8/8 same-vertex shift components plus 16/16 derivative checks, and 192/192 weak-index charge-sum components.

The exact source and six tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_all_six_shifted_Yukawa_singlet_channel_audit.py\`
- \`research/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.md\`
- \`validation/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.txt\`

This closes the local Yukawa-singlet charge factor for the validated shifts. It does not close the full ordinary-matter 1PI longitudinal integrand or the reducible LSZ sector.

### 4.9 LD-W-01 actual open-chain WTI/three-W bridge (IVn-h/01)

The two fermion-line insertions are now contracted with \(q_\alpha\) inside their complete Feynman-gauge open chains:
\[
\mathcal F_A^q
=\gamma^\mu S_A^W\slashed qP_LS_A^Y
\slashed{(h-q)}S_B^W\gamma_\mu,
\]
\[
\mathcal F_B^q
=\gamma^\mu S_A^W\slashed hS_B^Y
\slashed qP_LS_B^W\gamma_\mu.
\]
The oriented WTI identities are
\[
S_A^W\slashed qP_LS_A^Y=S_A^WP_R-P_LS_A^Y,
\]
\[
S_B^Y\slashed qP_LS_B^W=P_LS_B^W-S_B^YP_R.
\]
Both actual open-chain equalities pass independently in 16/16 Dirac components.

For the A-side second endpoint, \(k_{\rm old}=k+q\) maps
\[
r_A^Y(k_{\rm old})\to r_A^W(k),\quad
h_A(k_{\rm old})\to h(k),\quad
r_B^W(k_{\rm old})\to r_B^Y(k),\quad
k_{\rm old}\to\kappa.
\]
Its denominator is \(D_{3W}/k^2\). The B-side second endpoint is already in the common routing and has denominator \(D_{3W}/\kappa^2\). These are precisely the two single-W factors in the three-W inverse-kernel difference.

The first A/B endpoint terms are not folded into these aligned terms: they retain their own \(h-q,r_B^W\) or \(h,r_B^W\) Yukawa-channel denominators. The actual LD-W-01 \(R_{\rm FG}\) numerator is also checked by direct Lorentz contraction (16/16 matrix components).

The exact source and six local tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-01-open-chain-WTI-threeW-common-k-bridge.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_01_open_chain_WTI_threeW_common_k_bridge.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-01-open-chain-WTI-threeW-common-k-bridge.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-01-open-chain-WTI-threeW-common-k-bridge.txt\`

This closes the actual LD-W-01 open-chain WTI and denominator bridge, not the complete LD-W-01 weak-index/Yukawa/LSZ sum.

### 4.10 LD-W-02 actual F-S open-chain WTI bridge (IVn-h/02)

The A-side WTI is now inserted into the actual mixed F-S chain:
\[
\mathcal O_{02}^{\alpha}
=\gamma^\alpha S_A^W\slashed qP_LS_A^Y
\frac{\slashed{(h-q)}P_L}{(h-q)^2-M_E^2}
\frac{1}{(r_B^Y)^2}.
\]
The common-\(k\) A-side sub-block carries \(V_B(\kappa)\) and \(D^{\mu\nu}(\kappa)=g^{\mu\nu}/\kappa^2\). Replacing the fermion-line insertion by
\[
S_A^WP_R-P_LS_A^Y
\]
leaves the complete open chain unchanged. The exact comparison passes 64/64 open Lorentz-index matrix components and 16/16 contracted matrix entries; both endpoint terms are retained explicitly.

The A-side endpoint map \(k_{\rm old}=k+q\) also passes 16/16 vector components:
\[
r_A^Y(k_{\rm old})\to r_A^W(k),\quad
r_B^W(k_{\rm old})\to r_B^Y(k),\quad
h_A(k_{\rm old})\to h(k),\quad
k_{\rm old}\to\kappa.
\]
At the rational point, all eight W/fermion/scalar/heavy denominator factors are nonzero:
\[
(20,8,11,5,38,20,-390,-402).
\]

The exact source, six regression tests, and validation output are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-02-open-chain-WTI-bridge.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_02_open_chain_WTI_bridge.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-02-open-chain-WTI-bridge.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-02-open-chain-WTI-bridge.txt\`

The B-side scalar-line/seagull q contacts remain separate; this closes the actual fermion-line WTI sub-block only.

### 4.11 LD-W-05 actual S-F open-chain WTI bridge (IVn-h/03)

The B-oriented insertion
\[
S_B^Y\slashed qP_LS_B^W=P_LS_B^W-S_B^YP_R
\]
has now been inserted into the actual ordered S-F chain:
\[
\mathcal O_{05}^{q,\nu}
=\frac{1}{(r_A^Y)^2}
\frac{\slashed h}{h^2-M_E^2}
S_B^Y\slashed qP_LS_B^W\gamma^\nu.
\]
The common-\(k\) contraction uses \(V_A^\mu(k)=2p_2^\mu-k^\mu\) and \(D^{\mu\nu}(k)=g^{\mu\nu}/k^2\). The WTI replacement preserves the complete open chain. The open-index identity passes 64/64 matrix components; the Feynman-gauge contracted chain passes 16/16 matrix entries. The two endpoint terms remain explicit.

The B-side Yukawa endpoint is already in the common-\(k\) routing, with five vector maps passing 20/20 components. The rational denominator factors are
\[
(20,8,17,23,-22,-4,-390),
\]
all nonzero.

The source, six regression tests, and validation output are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-05-open-chain-WTI-bridge.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_05_open_chain_WTI_bridge.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-05-open-chain-WTI-bridge.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-05-open-chain-WTI-bridge.txt\`

IVn-h/05 now reconciles the LD-W-05 B-oriented WTI projector placement: both endpoints reduce to the same right-chiral open-chain order, while retaining distinct (r_B^W) and (r_B^Y) momenta. The single-W WTI endpoint numerators are explicitly kept distinct from the two-W (R_{\rm FG}) projection; this closes the projector-order audit, not their full cancellation.

### 4.12 LD-W-03/04 actual same-vertex open-chain WTIs (IVn-h/04)

The two orientations are now inserted into their distinct actual open chains:
\[
\mathcal O_{03}^{q,\mu}
=\gamma^\mu S_F^W\slashed qP_LS_F^Y
\frac{\slashed h_E^{03}P_L}{(h_E^{03})^2-M_E^2}
\frac{1}{(r_S^Y)^2},
\]
\[
\mathcal O_{04}^{q,\nu}
=\frac{\slashed h_E^{04}P_L}{(h_E^{04})^2-M_E^2}
S_F^Y\slashed qP_LS_F^W\gamma^\nu
\frac{1}{(r_S^Y)^2}.
\]
For 03 the replacement is \(S_F^W P_R-P_LS_F^Y\); for 04 it is \(P_LS_F^W-S_F^YP_R\). The open-index identities pass 64/64 components separately, and the \(V_S(k)D(k)\) contractions pass 16/16 entries separately. The two \(h_E\) spectators are k-independent (16/16 derivative checks).

At the shared rational point the denominator tuples are
\[
03:\ (7,10,13,16,8,11,-402),\qquad
04:\ (7,10,-10,-5,2,5,-401),
\]
with all factors nonzero. The two Dirac orders remain separate.

The exact source, six regression tests, and validation output are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-03-04-open-chain-WTI-bridge.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_03_04_open_chain_WTI_bridge.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-03-04-open-chain-WTI-bridge.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-03-04-open-chain-WTI-bridge.txt\`

This closes the two same-vertex fermion-line WTI sub-blocks, not their four-attachment sum.

### 4.13 LD-W-05 projector/order reconciliation (IVn-h/05)

The B-oriented WTI gives
\[
S_B^Y\slashed qP_LS_B^W=P_LS_B^W-S_B^YP_R.
\]
After insertion into the actual ordered S-F chain, the two endpoint terms contain
\[
\slashed hP_L\slashed r_B^W\gamma_\nu P_L,\qquad
-\slashed h\slashed r_B^YP_R\gamma_\nu P_L.
\]
Using \(P_L\slashed r=\slashed rP_R\) and \(P_R\gamma_\nu=\gamma_\nu P_L\), these become
\[
\slashed h\slashed r_B^W\gamma_\nu P_L,\qquad
-\slashed h\slashed r_B^Y\gamma_\nu P_L.
\]
Thus the rightmost chiral orientation agrees, but the two fermion momenta remain distinct. The four open Lorentz components pass 128/128 matrix-entry comparisons.

The two-W remainder has the separate order
\[
\mathcal N_{05}^{\rm FG}
=\left[(V_A\cdot k)\slashed h\slashed r_B^Y\slashed k
-(V_A\cdot\kappa)\slashed h\slashed r_B^Y\slashed\kappa\right]P_L.
\]
After the single-W propagator is contracted with the scalar current, the signed WTI endpoint numerators are
\[
\mathcal E_W=\slashed h\slashed r_B^W\slashed V_A P_L,\qquad
\mathcal E_Y=-\slashed h\slashed r_B^Y\slashed V_A P_L.
\]
The exact rational-point check finds all three matrices nonzero (16/16 entries each) and distinct. The complete longitudinal sum must determine how these pieces combine. The local combined regression suite passes 9/9 tests (LD-W-05: 4/4; LD-W-02: 5/5), using Python 3.13.5 and SymPy 1.14.0 at source commit \`ddf9d41d408b4ee94ccb0c313befcb97423f4b81\`. The latest PR-head GitHub Actions runs for candidate-schema validation, QLD8 counterterm-basis, and QLD chiral-Fierz checks are failures, not passes.

The exact source and four regression tests are recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-05-projector-order-reconciliation.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_05_projector_order_reconciliation.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-05-projector-order-reconciliation.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-05-projector-order-reconciliation.txt\`

### 4.14 LD-W-02 projector/order reconciliation (IVn-h/06)

The A-oriented WTI gives
\[
S_A^W\slashed qP_LS_A^Y=S_A^WP_R-P_LS_A^Y.
\]
With the heavy spectator \(\slashed h_AP_L\) to its right, the two terms reduce to
\[
\gamma_\mu S_A^WP_R\slashed h_AP_L
=-\frac{\gamma_\mu\slashed r_A^W\slashed h_AP_L}{(r_A^W)^2},
\]
\[
-\gamma_\mu P_LS_A^Y\slashed h_AP_L
=+\frac{\gamma_\mu\slashed r_A^Y\slashed h_AP_L}{(r_A^Y)^2}.
\]
The common rightmost \(P_L\) and Dirac order are established, while the distinct fermion momenta are retained. The open Lorentz comparison passes 128/128 matrix entries.

The two-W \(R_{\rm FG}\) projection follows the explicit cross-pair current ordering,
\[
\mathcal N_{02}^{\rm FG}
=\left[(V_B(\kappa)\cdot k)\slashed k(-\slashed r_A^W)\slashed h
-(V_B(\kappa)\cdot\kappa)\slashed\kappa(-\slashed r_A^W)\slashed h\right]P_L.
\]
The contracted single-W WTI endpoints have the distinct signed order
\[
\mathcal E_W=-\slashed V_B(\kappa)\slashed r_A^W\slashed h_A P_L,\qquad
\mathcal E_Y=+\slashed V_B(\kappa)\slashed r_A^Y\slashed h_A P_L,
\]
with the corresponding \((r_A^W)^2\) and \((r_A^Y)^2\) propagator denominators. The exact rational-point check finds all three matrices nonzero (16/16 entries each) and distinct. At the rational point,
\[
V_B(\kappa)\cdot k=-33,\qquad
V_B(\kappa)\cdot\kappa=-18,
\]
and all seven local denominator factors are nonzero. The local combined regression suite passes 9/9 tests (LD-W-05: 4/4; LD-W-02: 5/5), using Python 3.13.5 and SymPy 1.14.0 at source commit \`ddf9d41d408b4ee94ccb0c313befcb97423f4b81\`. The exact source and tests are:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-02-projector-order-reconciliation.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_02_projector_order_reconciliation.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-02-projector-order-reconciliation.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-02-projector-order-reconciliation.txt\`

### 4.15 LD-W-01 F-F projector/order reconciliation (IVn-h/07)

Both oriented F-F fermion WTIs are now reduced in the actual ordered open chains. The four endpoint reductions retain the graph-specific \(h-q\), \(h\), \(r_B^W\), and \(r_B^Y\) routing, with the common rightmost \(P_L\). Exact comparison passes \(1024/1024\) Dirac-matrix entries.

After the A-side shift \(k_{\rm old}=k+q\), its second endpoint and the unshifted B-side second endpoint reduce to the same common-\(k\) chain
\[
-\gamma_\mu S_A^W\slashed hS_B^Y\gamma_\nu P_L,
\]
passing \(256/256\) matrix entries. The A-side shift map passes \(16/16\) vector components; the two single-W denominator alignments to the three-W reference pass \(2/2\) identities. The W propagator momenta remain distinct (\(\kappa\) on the shifted A endpoint and \(k\) on the B endpoint).

The pair-specific \(R_{\rm FG}\) direct Lorentz contraction agrees with its factorized five-slash numerator in \(16/16\) entries. The final \(P_L\) must act after the right W current; the earlier pre-\(\slashed k\) placement is rejected in \(16/16\) entries. The \(R_{\rm FG}\) matrix remains nonzero and distinct from the one-W endpoint contractions. The local unittest suite passes \(6/6\) tests.

Sources and run evidence:
- calculations/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation.py
- calculations/test_RC001_dim6_WW_fivepoint_LD_W_01_projector_order_reconciliation.py
- research/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation.md
- validation/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation.txt
- validation/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation-run-manifest.json

This closes the LD-W-01 projector/order sub-block only. It does not close the six-pair longitudinal sum, the complete STI, loop integration, UV-EFT subtraction, or a Wilson coefficient.

### 4.16 LD-W-03/04 same-vertex endpoint/\(R_{\rm FG}\) order (IVn-h/08)

The two same-vertex fermion-line WTI endpoint pairs have now been reduced after the actual internal-W Lorentz contraction with the scalar current \(V_S=2p_S-\kappa\). For LD-W-03,
\[
\mathcal E_{03,W}=\slashed V_S\slashed r_F^W P_R,\qquad
\mathcal E_{03,Y}=-\slashed V_S\slashed r_F^Y P_R.
\]
For the Dirac-Hermitian-conjugate LD-W-04 orientation,
\[
\mathcal E_{04,W}=\slashed r_F^W\slashed V_S P_L,\qquad
\mathcal E_{04,Y}=-\slashed r_F^Y\slashed V_S P_L.
\]
The two pairs obey the expected Dirac-bar relations. The projector placement and reversed gamma order are retained; the two orientations are not collapsed into one chain. The pair-specific two-W remainders remain
\[
\mathcal N_{03}^{\rm FG}=(V_S\!\cdot k)\slashed k\slashed r_F^Y
-(V_S\!\cdot\kappa)\slashed\kappa\slashed r_F^Y,
\]
\[
\mathcal N_{04}^{\rm FG}=(V_S\!\cdot k)\slashed r_F^Y\slashed k
-(V_S\!\cdot\kappa)\slashed r_F^Y\slashed\kappa.
\]
At the recorded nonsingular rational point, all endpoint matrices and \(R_{\rm FG}\) numerators are nonzero and pairwise distinct; the \(h_E\) spectator is \(k\)-independent. This is an endpoint-order reconciliation, not a cancellation.

Execution boundary: the six identities, rational-point entries, denominator values, and spectator derivatives were independently reconstructed and evaluated in the current Python 3.13.5/SymPy 1.14.0 analysis runtime. The committed source entry point and unittest have not yet been executed from repository paths; no CI or independent diagram-package pass is claimed. See the LD-W-03/04 endpoint-order research note and companion source/validation files.
## 5. Direct-attachment census

The ordinary internal attachments remain
\[
12\ {\rm matter\!-\!line}
+6\ {\rm scalar\ seagull}
+6\ {\rm three\!-\!W}
=24.
\]
By pair:
\[
(3,4,4,4,4,5)
\]
for LD-W-01…06. No new topology is introduced in IVl/IVm/IVn-a…IVn-e.

## 6. Remaining assembly gates

1. **LD-W-01 projector/order reconciliation — completed as a local algebraic sub-block (IVn-h/07).** Both oriented endpoint chains, the A-shift/B-common second-endpoint equality, and the pair-specific two-W \(R_{\rm FG}\) projector order are checked. The complete six-pair sum remains open.
2. **LD-W-03/04 same-vertex order reconciliation — completed as an endpoint-order sub-block (IVn-h/08).** Both oriented WTI endpoint pairs are reduced with their actual scalar-current contraction and compared with their own (R_{\rm FG}) chains; the Dirac-bar relations and (h_E) spectator are checked. No cancellation is inferred.
3. **LD-W-06 scalar endpoint completion.** No fermion-line WTI exists for S-S. Assemble its two scalar-line kernels and two seagulls with the exact shifted heavy denominators and compare to the two-W remainder.
4. **Assemble the ordinary-matter longitudinal integrand for all six pairs.** Insert the fermion-line WTIs, scalar-line kernels, seagulls, and three-W kernels using exact weak tensors and phases.
5. **Perform every secondary loop-variable shift on the complete numerator and denominator.** Keep the two terms in each \(\delta_X=\Delta_Y-\Delta_W\) separate. For LD-W-06, the A and B negative-propagator terms shift \(h\) to \(h-q\) and \(h+q\), respectively.
6. **Combine the local Yukawa-singlet factors with the actual ordered 1PI terms.** Local charge sums pass for all six pairs, but this alone does not establish cancellation of the Lorentz- and weak-index-weighted integrand.
7. **Write the four reducible external-leg/LSZ factors and their lower-point amplitudes explicitly.** Keep them outside the 1PI five-point vertex until the full Ward identity is assembled.
8. **Derive the BRST/ghost Slavnov–Taylor completion** and test the longitudinal inverse-kernel target \(D(\kappa)[L(\kappa)-L(k)]D(k)=-R_{\rm FG}\) in the assembled matter-current chains.
9. **Add counterterms:** \(W\)-field, gauge-coupling, matter-field, Yukawa, heavy-mass, and operator counterterms. Only after the complete off-shell identity closes should the common-regulator UV–EFT subtraction and comparison with the EFT one-\(W\) vertex be performed.

No loop integration, complete STI closure, transverse form factor, UV–EFT matching coefficient, or Wilson coefficient is claimed at this stage.
