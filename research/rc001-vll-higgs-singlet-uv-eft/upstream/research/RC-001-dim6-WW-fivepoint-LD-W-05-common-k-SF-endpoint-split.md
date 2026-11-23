# RC-001 — LD-W-05 exact common-\(k\) S–F endpoint split

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-f/03  
**Status:** the B-side fermion-WTI/Yukawa-endpoint map is now explicitly aligned with the three-W graph using the actual A-scalar current \(V_A(k)\). Separately, the A-side scalar-line/seagull current \(V_A(k+q)\) is re-expressed in the three-W basis. The exact rebase retains both symmetric and commutator \(q^\mu\) contacts. No physical non-cancellation is claimed.

## 1. Fixed LD-W-05 momenta

Set \(p_A=p_2,\ p_B=p_4\), and
\[
\kappa=k+q,\qquad
r_A^Y=k-p_2,\qquad r_A^W=\kappa-p_2,
\]
\[
r_B^Y=\kappa+p_4,\qquad h=k-p_1-p_2,
\]
\[
V_A^{\rm line}=2p_2-\kappa,\qquad
V_A^{3W}=2p_2-k.
\]
The three-W denominator is
\[
\boxed{
\mathscr D_{3W}^{05}
=k^2\kappa^2(r_A^Y)^2(r_B^Y)^2(h^2-M_E^2).
}
\tag{1.1}
\]

## 2. B-side fermion WTI: exact match to the three-W A endpoint

The B-oriented fermion WTI is
\[
S_F(r_B^Y)\slashed qP_LS_F(r_B^W)
=P_LS_F(r_B^W)-S_F(r_B^Y)P_R.
\]
The B-side Yukawa-endpoint term is already in the common \(k\) routing. It retains
\[
r_A^Y=k-p_2,\qquad r_B^Y=\kappa+p_4,\qquad
h=k-p_1-p_2,\qquad V_A=2p_2-k.
\tag{2.1}
\]
Thus the scalar current in this sub-block is exactly the three-W A-endpoint current \(V_A^{3W}\). Its single-W denominator is
\[
\mathscr D_{B,Y}^{05}
=k^2(r_A^Y)^2(r_B^Y)^2(h^2-M_E^2)
=\frac{\mathscr D_{3W}^{05}}{\kappa^2}.
\tag{2.2}
\]

## 3. A-side scalar-line plus seagull: exact current rebase

Define
\[
\Delta_Y=\frac1{(r_A^Y)^2},\qquad
\Delta_W=\frac1{(r_A^W)^2},\qquad
\delta_A=\Delta_Y-\Delta_W.
\]
The A-oriented scalar WTI is
\[
\frac{q\cdot(r_A^W+r_A^Y)}
{(r_A^W)^2(r_A^Y)^2}
=\Delta_Y-\Delta_W=\delta_A.
\tag{3.1}
\]
The phase-weighted A-side scalar-line plus seagull current is
\[
\boxed{
\mathcal C_A^\mu
=g_2\left[
\left(-\frac12\delta_AV_A^{{\rm line},\mu}
+\Delta_Yq^\mu\right)\mathcal S_A^a
-\frac i2\delta_AV_A^{{\rm line},\mu}\mathcal G_{AB}^a
\right].
}
\tag{3.2}
\]
The actual currents obey
\[
V_A^{3W}-V_A^{\rm line}=q,
\qquad V_A^{\rm line}=V_A^{3W}-q.
\]
Therefore
\[
\boxed{
\begin{aligned}
\mathcal C_A^\mu=g_2\Big[
&-\frac12\delta_AV_A^{3W,\mu}\mathcal S_A^a
+\left(\frac12\delta_A+\Delta_Y\right)q^\mu\mathcal S_A^a\\
&-\frac i2\delta_AV_A^{3W,\mu}\mathcal G_{AB}^a
+\frac i2\delta_Aq^\mu\mathcal G_{AB}^a
\Big].
\end{aligned}
}
\tag{3.3}
\]
The symmetric \(q^\mu\) coefficient is
\[
\frac12\delta_A+\Delta_Y
=\frac32\Delta_Y-\frac12\Delta_W.
\]
The commutator contact is
\[
\boxed{
\Delta\mathcal C_{A,\mathrm{comm}}^\mu
=\frac{i g_2}{2}\delta_Aq^\mu\mathcal G_{AB}^a.
}
\tag{3.4}
\]
It remains distinct from the symmetric seagull tensor.

For the physical \((H,L)\) slots, the weak factors obey
\[
\mathcal W_A^a-\widetilde{\mathcal W}_A^a
=i\mathcal G_{AB}^a,\qquad
\mathcal W_A^a+\widetilde{\mathcal W}_A^a
=\mathcal S_A^a=\frac12R_L^aT_0.
\]
The A-line commutator and three-W phase-weighted group factors are both \(-ig_2\mathcal G_{AB}^a\).

The actual contracted scalar endpoint kernel is
\[
\mathcal K_{05,A}
=\frac{\slashed h\slashed r_B^Y\slashed{\mathcal C}_A}{\kappa^2},
\]
with remaining spectator denominator \((r_B^Y)^2(h^2-M_E^2)\). The scalar propagators \(\Delta_Y,\Delta_W\) are already contained in \(\mathcal C_A\).

## 4. Three-W \(R_{\rm FG}\) projection with the actual A scalar current

Use
\[
\mathcal X_{05}=\slashed h\slashed r_B^YP_L
\]
and \(V_A^{3W}=2p_2-k\). The explicit remainder numerator is
\[
\boxed{
\mathcal N_{05}
=[V_A^{3W}\cdot k]\mathcal X_{05}\slashed k
-[V_A^{3W}\cdot\kappa]\mathcal X_{05}\slashed\kappa.
}
\tag{4.1}
\]
Its denominator is (1.1). The exact rational-point matrix check verifies the actual \(V_A^{3W},\gamma^\nu\) endpoint contraction against \(R_{\rm FG}\), and the \(D(\kappa)-D(k)\) transverse-kernel cancellation in this isolated current sub-block.

This is not a cancellation of the additional A-side scalar-line/seagull kernel (3.2); its symmetric and commutator \(q^\mu\) contacts (3.3) remain for the endpoint/LSZ/STI assembly.

## 5. Exact rational diagnostic

Use
\[
\begin{aligned}
k&=(5,1,2,0),&q&=(0,1,1,2),\\
p_1&=(1,1,0,1),&p_2&=(0,2,1,0),\\
p_3&=(2,0,1,1),&p_4&=(-3,-4,-3,-4).
\end{aligned}
\]
With \(M_E^2=400\),
\[
(k^2,\kappa^2,(r_A^Y)^2,(r_A^W)^2,(r_B^Y)^2,h^2-M_E^2)
=(20,8,23,17,-4,-390),
\]
and
\[
\delta_A=\frac1{23}-\frac1{17}=-\frac6{391}\ne0.
\]
All denominators are nonzero. The three-W \(\mathcal N_{05}\) has 16/16 nonzero matrix entries. The A-side commutator \(q^\mu\) contact, after contraction with the B fermion chain and internal W propagator, also has 16/16 nonzero matrix entries.

These are exact rational diagnostics, not physical benchmark points or evidence of a nonzero uncanceled physical amplitude.

## 6. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-05-common-k-SF-endpoint-split.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_05_common_k_SF_endpoint_split.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-05-common-k-SF-endpoint-split.txt\`

Six local regression tests pass. Exact checks include the B-side fermion WTI, A-side scalar WTI/current rebase, 20-component common-\(k\) map, three denominator-factor identities, A-side weak commutator/seagull tensors, and actual rational-point \(R_{\rm FG}\)/\(q^\mu\)-contact matrices.

**Not established:** cancellation of (3.4) against external-field/Yukawa endpoint variations, external-leg/LSZ terms, the ghost/gauge-fixing STI, or counterterms. No physical non-cancellation is claimed. No full five-point STI, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
