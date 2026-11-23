# RC-001 — LD-W-03/04 exact common-\(k\) same-vertex endpoint bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-f/04  
**Status:** the two same-vertex classes are now expressed in their actual common-\(k\) current basis. The opposite LD-W-03/04 fermion WTIs, S-to-F scalar WTI, scalar-line/seagull shift, distinct Dirac-Hermitian loop orders, same-vertex weak tensors/phases, pair-dependent \(R_{\rm FG}\) projections, and external heavy spectators are checked independently. This is still a pairwise endpoint bridge, not the complete four-attachment Lorentz sum or the full five-point STI.

## 1. Frozen same-vertex routing

All external momenta are incoming:
\[
p_1+p_2+p_3+p_4+q=0,\qquad \kappa=k+q.
\]
For the two pairs,
\[
\begin{array}{c|cc|c}
 & F & S & h_E\\ \hline
{\rm LD\!-\!W\!-\!03} & \bar L(p_1) & H(p_2) & p_1+p_2+q\\
{\rm LD\!-\!W\!-\!04} & L(p_4) & H^\dagger(p_3) & p_3+p_4+q
\end{array}
\]
and the internal W flows \(S\to F\):
\[
k_S=k,\qquad k_F=\kappa.
\]
The common-\(k\) momenta are
\[
r_F^W=k+p_F,\qquad r_F^Y=k+p_F+q,
\]
\[
r_S^Y=p_S-k,\qquad r_S^W=p_S-k-q,
\qquad r_F^Y-r_F^W=q,\quad r_S^Y-r_S^W=q.
\]
The scalar currents are
\[
V_S^{\rm line}=2p_S-\kappa,\qquad
V_S^{3W}=2p_S-k,
\]
so
\[
\boxed{V_S^{\rm line}=V_S^{3W}-q.}
\tag{1.1}
\]

## 2. Opposite fermion-line WTIs

With \(S_F(r)=\slashed r/r^2\), the actual ordered contractions are
\[
\boxed{
S_F(r_F^W)\slashed qP_LS_F(r_F^Y)
=S_F(r_F^W)P_R-P_LS_F(r_F^Y)
\quad({\rm LD\!-\!W\!-\!03}),
}
\tag{2.1}
\]
\[
\boxed{
S_F(r_F^Y)\slashed qP_LS_F(r_F^W)
=P_LS_F(r_F^W)-S_F(r_F^Y)P_R
\quad({\rm LD\!-\!W\!-\!04}).
}
\tag{2.2}
\]
The two identities are checked in all 32 Dirac-matrix components. The \(P_L/P_R\) order and the two propagator orders are not interchanged.

## 3. S-to-F scalar WTI and the exact current rebase

Define
\[
\Delta_Y=\frac1{(r_S^Y)^2},\qquad
\Delta_W=\frac1{(r_S^W)^2},\qquad
\delta_S=\Delta_Y-\Delta_W.
\]
The S-to-F scalar orientation gives
\[
\boxed{
\frac{q\cdot(r_S^W+r_S^Y)}
{(r_S^W)^2(r_S^Y)^2}
=\Delta_W-\Delta_Y=-\delta_S.
}
\tag{3.1}
\]
The phase-weighted scalar-line plus seagull current from the six-pair endpoint construction is
\[
\boxed{
\mathcal C_S^\mu
=g_2\left[
\left(\frac12\delta_S V_S^{{\rm line},\mu}
+\Delta_Yq^\mu\right)\mathcal S_S^a
+\frac i2\delta_SV_S^{{\rm line},\mu}\mathcal G_{FS}^a
\right].
}
\tag{3.2}
\]
Here
\[
\mathcal S_S^a=\frac12R_F^aT_0,\qquad
\mathcal G_{FS}^a=\epsilon^{abc}R_F^bR_S^cT_0.
\]
Substituting (1.1) gives the exact three-W-basis expression
\[
\boxed{
\begin{aligned}
\mathcal C_S^\mu=g_2\Bigg[
&\frac12\delta_SV_S^{{\rm 3W},\mu}\mathcal S_S^a
+\frac12(\Delta_Y+\Delta_W)q^\mu\mathcal S_S^a\\
&+\frac i2\delta_SV_S^{{\rm 3W},\mu}\mathcal G_{FS}^a
-\frac i2\delta_Sq^\mu\mathcal G_{FS}^a
\Bigg].
\end{aligned}
}
\tag{3.3}
\]
The two contact structures are distinct:
\[
\boxed{
\mathcal C_{S,q}^{\mu}
=g_2\left[
\frac12(\Delta_Y+\Delta_W)q^\mu\mathcal S_S^a
-\frac i2\delta_Sq^\mu\mathcal G_{FS}^a
\right].
}
\tag{3.4}
\]
The first is symmetric in the scalar weak ordering; the second is the commutator contact. Neither is set to zero.

### Comparison with the cross-vertex scalar endpoints

This is not the LD-W-02 or LD-W-05 formula copied with \(A/B\) relabelled:

| Endpoint | Current relation | Symmetric \(q^\mu\) coefficient | Commutator \(q^\mu\) coefficient |
|---|---|---|---|
| LD-W-02 B scalar | \(V_B^{\rm line}=V_B^{3W}+q\) | \(\Delta_Y+\delta_B/2\) | \(+i\delta_B/2\) |
| LD-W-05 A scalar | \(V_A^{\rm line}=V_A^{3W}-q\), with A-oriented WTI | \(\Delta_Y+\delta_A/2\) | \(+i\delta_A/2\) |
| LD-W-03/04 S scalar | \(V_S^{\rm line}=V_S^{3W}-q\), with S-to-F WTI | \(\Delta_Y-\delta_S/2=(\Delta_Y+\Delta_W)/2\) | \(-i\delta_S/2\) |

The distinct signs follow from the oriented scalar WTI and the actual \(WHH^\dagger\) current, not from a choice of notation.

## 4. Common-\(k\) shift and denominator bridge

Before the shift, the scalar-line graph has
\[
r_S^{S}=p_S-k_{\rm old},\quad
r_S^Y=p_S-k_{\rm old}+q,\quad
r_F^W=k_{\rm old}+p_F,\quad
k_S=k_{\rm old}.
\]
Set \(k_{\rm old}=k+q\). Then
\[
\begin{aligned}
r_S^{S}&\to r_S^W=p_S-k-q,\\
r_S^Y&\to r_S^Y=p_S-k,\\
r_F^W&\to r_F^Y=k+p_F+q,\\
k_S&\to\kappa,\qquad
V_S\to V_S^{\rm line}=2p_S-\kappa.
\end{aligned}
\tag{4.1}
\]
The seagull momentum \(r_S^{\rm sg}=p_S-k_{\rm old}+q\) maps to \(r_S^Y\), and its opposite fermion propagator maps to \(r_F^Y\).

Crucially, the two terms in \(\delta_S\) must not be treated as if they had the same denominator. They obey the exact shift identities
\[
\Delta_W(k)=\Delta_Y(k+q),
\]
\[
r_F^Y(k)=r_F^W(k+q),\qquad
V_S^{\rm line}(k)=V_S^{3W}(k+q),\qquad
D(\kappa(k))=D(k+q).
\tag{4.2}
\]
Thus the \(-\Delta_W\) part of the scalar-line WTI maps, after \(k\to k+q\), onto the corresponding fermion-side endpoint routing. The \(+\Delta_Y\) part is in the common routing of the seagull and the \(-D(\kappa)\) three-W term. This is the denominator/routing bridge; it is not yet a cancellation of the complete Dirac and weak-index weighted sum.

The relevant denominator families are
\[
D_{3W}=k^2\kappa^2(r_F^Y)^2(r_S^Y)^2(h_E^2-M_E^2),
\]
\[
D_{F{\rm line}}=k^2(r_F^W)^2(r_F^Y)^2(r_S^Y)^2(h_E^2-M_E^2),
\]
\[
D_{S{\rm line}}=\kappa^2(r_F^Y)^2(r_S^Y)^2(r_S^W)^2(h_E^2-M_E^2),
\]
\[
D_{\rm sg}=\kappa^2(r_F^Y)^2(r_S^Y)^2(h_E^2-M_E^2)
=\frac{D_{3W}}{k^2}.
\tag{4.3}
\]
The scalar-line graph retains both scalar propagators; the seagull retains one. The heavy denominator is a spectator and is independent of \(k\).

## 5. Actual Lorentz kernels and the retained \(R_{\rm FG}\) term

With \(\slashed{\mathcal C}_S=\gamma_\mu\mathcal C_S^\mu\), the two scalar-line/seagull kernels retain their seed orders:
\[
\boxed{
\mathcal K_{03,S}
=\frac{\slashed{\mathcal C}_S\slashed r_F^Y}{\kappa^2},
\qquad
\mathcal K_{04,S}
=\frac{\slashed r_F^Y\slashed{\mathcal C}_S}{\kappa^2}.
}
\tag{5.1}
\]
The \(R_{\rm FG}\) contractions of the three-W graph use \(V_S^{3W}=2p_S-k\):
\[
\boxed{
\mathcal N_{03}
=(V_S^{3W}\!\cdot k)\slashed k\slashed r_F^Y
-(V_S^{3W}\!\cdot\kappa)\slashed\kappa\slashed r_F^Y,
}
\tag{5.2}
\]
\[
\boxed{
\mathcal N_{04}
=(V_S^{3W}\!\cdot k)\slashed r_F^Y\slashed k
-(V_S^{3W}\!\cdot\kappa)\slashed r_F^Y\slashed\kappa.
}
\tag{5.3}
\]
The loop-side \(R_{\rm FG}\) factor is \(\mathcal N_{03,04}/(k^2\kappa^2)\), with remaining denominator \((r_F^Y)^2(r_S^Y)^2(h_E^2-M_E^2)\). Equations (5.2) and (5.3) are Dirac-Hermitian conjugate orders for a common \(r_F^Y,V_S^{3W}\); they are not replaced by one another inside either graph.

The chiral heavy propagator remains external to the loop-side kernel:
\[
P_R\frac{\slashed h_E+M_E}{h_E^2-M_E^2}P_L
=\frac{\slashed h_EP_L}{h_E^2-M_E^2}.
\]
It is attached in the original LD-W-03 or conjugate LD-W-04 seed order and is not commuted through \(\mathcal K\) or \(\mathcal N\).

## 6. Same-vertex weak phases

For both pairs, the explicit physical-representation tensors satisfy
\[
\mathcal W_F^a-\widetilde{\mathcal W}_F^a
=i\mathcal G_{FS}^a,\qquad
\mathcal W_S^a-\widetilde{\mathcal W}_S^a
=i\mathcal G_{FS}^a,
\]
\[
\mathcal G_{3W,S\to F}^a=-\mathcal G_{FS}^a,\qquad
\mathcal S_S^a=\mathcal W_S^a+\widetilde{\mathcal W}_S^a
=\frac12R_F^aT_0.
\]
With relative phases \(-g_2\) for matter-line insertions and \(-ig_2\) for the three-W insertion, the phase-weighted commutator and three-W group factors cancel algebraically. This is the already-checked weak-index identity, not the Lorentz-weighted diagram cancellation. The symmetric \(\mathcal S_S^a\) contact and the \(R_{\rm FG}\) projection remain separate.

## 7. Exact rational diagnostics and reproduction

Two nonsingular rational five-point diagnostic points are used. All momenta are in a common arbitrary unit and satisfy \(p_4=-p_1-p_2-p_3-q\). \(M_E^2=400\) is only a nonsingular algebraic diagnostic, not a physical benchmark.

| Point | Pair | \((k^2,\kappa^2,(r_F^Y)^2,(r_F^W)^2,(r_S^Y)^2,(r_S^W)^2,h_E^2-M_E^2)\) | \(\delta_S\) | \((\Delta_Y+\Delta_W)/2\) |
|---|---|---|---:|---:|
| 1 | 03 | \((7,10,16,13,8,11,-402)\) | \(3/88\) | \(19/176\) |
| 1 | 04 | \((7,10,-5,-10,2,5,-401)\) | \(3/10\) | \(7/20\) |
| 2 | 03 | \((34,44,58,46,35,49,-407)\) | \(2/245\) | \(6/245\) |
| 2 | 04 | \((34,44,4,-4,13,19,-405)\) | \(6/247\) | \(16/247\) |

At both points, all denominator factors are nonzero, all four \(R_{\rm FG}\) numerators have 16/16 nonzero entries, and the raw/rebased scalar endpoint kernels agree in all 64 matrix components across the four pair-point combinations. The two \(q^\mu\) contact matrices are nonzero at every point; the second point's LD-W-04 contacts each have 8/16 nonzero entries, while the other cases have 16/16.

The exact source and seven local regression tests are:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_03_04_common_k_same_vertex_endpoint_split.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-03-04-common-k-same-vertex-endpoint-split.txt\`

These are local exact SymPy checks; no GitHub Actions result is claimed.

## 8. Boundary and next step

This result does **not** establish the complete LD-W-03/04 four-attachment Ward sum. The fermion-line WTI endpoint terms, scalar-line terms, seagull, and three-W \(D(k)-D(\kappa)+R_{\rm FG}\) terms still have to be combined with their full ordered weak tensors, the local Yukawa-singlet charge variations, and the external-leg/LSZ sector. The \(\mathcal S_S^a\) and \(\mathcal G_{FS}^a\) terms are not identified, and neither \(R_{\rm FG}\) nor the \(q^\mu\) contacts are discarded.

No complete five-point STI, loop integration, UV–EFT subtraction, transverse form factor, or Wilson coefficient is claimed.
