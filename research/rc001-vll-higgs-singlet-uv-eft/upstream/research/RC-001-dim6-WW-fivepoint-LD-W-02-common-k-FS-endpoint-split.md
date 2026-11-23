# RC-001 — LD-W-02 exact common-\(k\) F–S endpoint split

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-f/02  
**Status:** the A-side fermion-WTI/Yukawa-endpoint map is now explicitly aligned with the three-W graph using the actual B-scalar current \(V_B(\kappa)\). Separately, the complete B-side scalar-line plus seagull current is re-expressed in the \(V_B(\kappa),q^\mu\) basis. This produces explicit symmetric and commutator \(q^\mu\) contacts, which are retained for the external-endpoint/LSZ/STI assembly. No physical non-cancellation is claimed.

## 1. Fixed LD-W-02 momenta

Set \(p_A=p_1,\ p_B=p_3\), and
\[
\kappa=k+q,\qquad
r_A=k-p_1,\qquad
r_B^W=k+p_3,\qquad
r_B^Y=k+p_3+q,
\]
\[
h=k-p_1-p_2,\qquad
V_B(k)=-2p_3-k,\qquad
V_B(\kappa)=-2p_3-\kappa.
\]
The three-W denominator is
\[
\boxed{
\mathscr D_{3W}^{02}
=k^2\kappa^2r_A^2(r_B^Y)^2(h^2-M_E^2).
}
\tag{1.1}
\]

## 2. A-side fermion WTI: exact match to the three-W B endpoint

The A-side fermion WTI remains
\[
S_F(-r_A^W)\slashed qP_LS_F(-r_A^Y)
=S_F(-r_A^W)P_R-P_LS_F(-r_A^Y).
\]
For its Yukawa-endpoint term, use \(k_{\rm old}=k+q\). Then
\[
\begin{aligned}
r_A^Y(k_{\rm old})&=r_A,\\
r_B^W(k_{\rm old})&=r_B^Y,\\
h_A(k_{\rm old})&=h,\\
V_B(k_{\rm old})&=V_B(\kappa),\\
k_{\rm old}&=\kappa.
\end{aligned}
\tag{2.1}
\]
All 20 vector components are checked exactly. The single-W denominator after this shift is
\[
\mathscr D_{A,Y}^{02}
=\kappa^2r_A^2(r_B^Y)^2(h^2-M_E^2)
=\frac{\mathscr D_{3W}^{02}}{k^2}.
\tag{2.2}
\]
Thus this A-side fermion endpoint uses exactly the scalar current and scalar propagator appearing at the B endpoint of the three-W graph. It is not the B-side scalar-line insertion.

## 3. B-side scalar-line plus seagull: exact current rebase

Define
\[
\Delta_Y=\frac1{(r_B^Y)^2},\qquad
\Delta_W=\frac1{(r_B^W)^2},\qquad
\delta_B=\Delta_Y-\Delta_W.
\]
The B-oriented scalar WTI is
\[
\frac{q\cdot(r_B^W+r_B^Y)}
{(r_B^W)^2(r_B^Y)^2}
=\Delta_W-\Delta_Y=-\delta_B.
\tag{3.1}
\]
The common-\(k\) scalar-line plus seagull current from IVm is
\[
\boxed{
\mathcal C_B^\mu
=g_2\left[
\left(\frac12\delta_BV_B^\mu(k)+\Delta_Yq^\mu\right)\mathcal S_B^a
+\frac{i}{2}\delta_BV_B^\mu(k)\mathcal G_{AB}^a
\right].
}
\tag{3.2}
\]
Since
\[
V_B(k)-V_B(\kappa)=q,
\]
substitution gives the exact identity
\[
\boxed{
\begin{aligned}
\mathcal C_B^\mu=g_2\Bigg[
&\frac12\delta_BV_B^\mu(\kappa)\mathcal S_B^a
+\left(\frac12\delta_B+\Delta_Y\right)q^\mu\mathcal S_B^a\\
&+\frac{i}{2}\delta_BV_B^\mu(\kappa)\mathcal G_{AB}^a
+\frac{i}{2}\delta_Bq^\mu\mathcal G_{AB}^a
\Bigg].
\end{aligned}
}
\tag{3.3}
\]
Equivalently, the symmetric \(q^\mu\) coefficient is
\[
\frac12\delta_B+\Delta_Y
=\frac32\Delta_Y-\frac12\Delta_W.
\]
The final term in (3.3),
\[
\boxed{
\Delta\mathcal C_{B,\mathrm{comm}}^\mu
=\frac{i g_2}{2}\delta_Bq^\mu\mathcal G_{AB}^a,
}
\tag{3.4}
\]
is a distinct commutator contact. It cannot be merged into the symmetric seagull tensor \(\mathcal S_B^a\).

The physical weak tensors are checked directly for the \((\bar L,H^\dagger)\) slots:
\[
\mathcal W_B^a-\widetilde{\mathcal W}_B^a
=i\mathcal G_{AB}^a,\qquad
\mathcal W_B^a+\widetilde{\mathcal W}_B^a
=\mathcal S_B^a=\frac12R_{\bar L}^aT_0.
\]
The A/B fermion/three-W commutator phase is \(-ig_2\mathcal G_{AB}^a\), while the scalar-line and seagull pieces retain their separate phase-weighted tensors in (3.2).

The actual contracted scalar endpoint kernel is
\[
\mathcal K_{02,B}
=\frac{\slashed{\mathcal C}_B(-\slashed r_A)\slashed h}{k^2},
\]
with remaining spectator denominator \(r_A^2(h^2-M_E^2)\). The scalar propagators \(\Delta_Y,\Delta_W\) are already contained in \(\mathcal C_B\).

## 4. Three-W \(R_{\rm FG}\) projection with the actual B scalar current

For the three-W graph use
\[
\mathcal X_{02}=-\slashed r_A\slashed hP_L
\]
and the actual endpoint current \(V_B(\kappa)\). Its explicit remainder numerator is
\[
\boxed{
\mathcal N_{02}
=\slashed k\,\mathcal X_{02}\,[V_B(\kappa)\cdot k]
-\slashed\kappa\,\mathcal X_{02}\,[V_B(\kappa)\cdot\kappa].
}
\tag{4.1}
\]
The full \(R_{\rm FG}\) contribution has denominator (1.1). The exact rational-point matrix check verifies the contraction of the actual \(\gamma^\mu\) and \(V_B^\nu(\kappa)\) endpoint currents against \(R_{\rm FG}^{\mu\nu}\), as well as the \(D(\kappa)-D(k)\) transverse-kernel cancellation in this isolated current sub-block.

This is not a cancellation of the additional B-side scalar-line/seagull kernel (3.2). That kernel has its own two scalar propagators and its \(q^\mu\) contacts (3.3).

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
(k^2,\kappa^2,r_A^2,(r_B^W)^2,(r_B^Y)^2,h^2-M_E^2)
=(20,8,11,38,20,-390),
\]
and
\[
\delta_B=\frac9{380}\ne0.
\]
All denominators are nonzero. The three-W \(\mathcal N_{02}\) has 16/16 nonzero matrix entries. The commutator contact (3.4), after contraction with the opposite fermion chain and the internal W propagator, also has 16/16 nonzero matrix entries.

These are exact rational diagnostics, not physical benchmark points or evidence of a nonzero uncanceled physical amplitude.

## 6. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-02-common-k-FS-endpoint-split.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_02_common_k_FS_endpoint_split.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-02-common-k-FS-endpoint-split.txt\`

Six local regression tests pass. The exact checks include the A-side fermion WTI, B-side scalar WTI, four-component current rebase, 20-component A-side common-\(k\) map, two denominator identities, B-side weak commutator/seagull tensors, and the actual rational-point \(R_{\rm FG}\) and \(q^\mu\)-contact matrices.

**Not established:** cancellation of (3.4) against external-field/Yukawa endpoint variations, external-leg/LSZ terms, the ghost/gauge-fixing STI, or counterterms. No physical non-cancellation is claimed. No full five-point STI, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
