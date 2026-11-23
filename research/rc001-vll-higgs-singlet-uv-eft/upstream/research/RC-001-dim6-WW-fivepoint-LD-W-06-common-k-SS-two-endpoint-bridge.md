# RC-001 — LD-W-06 exact common-\(k\) S–S two-endpoint bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-f/05  
**Status:** the two LD-W-06 scalar endpoints have now been rebased independently into the actual three-W current basis. Their scalar-line/seagull kernels, seagull denominators, weak tensors, and the actual S–S \(R_{\rm FG}\) projection are checked at two nonsingular rational points. The A and B endpoints remain separate; no complete five-point Ward/ST cancellation is claimed.

## 1. Frozen LD-W-06 routing

Use
\[
p_4=-p_1-p_2-p_3-q,\qquad \kappa=k+q,\qquad
h=k-p_1-p_2.
\]
The pair is \(A=H(p_2)\), \(B=H^\dagger(p_3)\), with
\[
r_A^Y=k-p_2,\quad r_A^W=\kappa-p_2,
\]
\[
r_B^Y=\kappa+p_3,\quad r_B^W=k+p_3.
\]
The actual three-W endpoint currents are
\[
V_A^{3W}=2p_2-k,\qquad
V_B^{3W}=-2p_3-\kappa.
\]
The A-side scalar-line current is
\[
V_A^{\rm line}=2p_2-\kappa=V_A^{3W}-q,
\]
whereas the B-side scalar-line current is
\[
V_B^{\rm line}=-2p_3-k=V_B^{3W}+q.
\]
The two relations have opposite signs and must not be replaced by a single common scalar-current shift.

## 2. A-side scalar-line plus seagull

Define
\[
\Delta_{AY}=\frac1{(r_A^Y)^2},\qquad
\Delta_{AW}=\frac1{(r_A^W)^2},\qquad
\delta_A=\Delta_{AY}-\Delta_{AW}.
\]
The A-oriented scalar WTI is
\[
\frac{q\cdot(r_A^W+r_A^Y)}
{(r_A^W)^2(r_A^Y)^2}
=\Delta_{AY}-\Delta_{AW}=\delta_A.
\]
The phase-weighted A endpoint current is
\[
\mathcal C_A^\mu
=g_2\left[
\left(-\frac12\delta_AV_A^{{\rm line},\mu}
+\Delta_{AY}q^\mu\right)\mathcal S_A^a
-\frac i2\delta_AV_A^{{\rm line},\mu}\mathcal G_{AB}^a
\right].
\]
Rebasing \(V_A^{\rm line}=V_A^{3W}-q\) gives
\[
\boxed{
\begin{aligned}
\mathcal C_A^\mu=g_2\Big[
&-\frac12\delta_AV_A^{3W,\mu}\mathcal S_A^a
+\left(\Delta_{AY}+\frac12\delta_A\right)q^\mu\mathcal S_A^a\\
&-\frac i2\delta_AV_A^{3W,\mu}\mathcal G_{AB}^a
+\frac i2\delta_Aq^\mu\mathcal G_{AB}^a
\Big].
\end{aligned}
}
\tag{2.1}
\]
Its actual opposite-endpoint contraction is
\[
\boxed{
\mathcal K_{06,A}
=\frac{\slashed h\,(V_B^{3W}\cdot\mathcal C_A)}{\kappa^2}.
}
\tag{2.2}
\]
The symmetric and commutator \(q^\mu\) contacts in this kernel are weighted by \(V_B^{3W}\cdot q\), with distinct \(\mathcal S_A^a\) and \(\mathcal G_{AB}^a\).

## 3. B-side scalar-line plus seagull

Define
\[
\Delta_{BY}=\frac1{(r_B^Y)^2},\qquad
\Delta_{BW}=\frac1{(r_B^W)^2},\qquad
\delta_B=\Delta_{BY}-\Delta_{BW}.
\]
The B-oriented scalar WTI has the opposite sign:
\[
\frac{q\cdot(r_B^W+r_B^Y)}
{(r_B^W)^2(r_B^Y)^2}
=\Delta_{BW}-\Delta_{BY}=-\delta_B.
\]
The phase-weighted B endpoint current is
\[
\mathcal C_B^\mu
=g_2\left[
\left(\frac12\delta_BV_B^{{\rm line},\mu}
+\Delta_{BY}q^\mu\right)\mathcal S_B^a
+\frac i2\delta_BV_B^{{\rm line},\mu}\mathcal G_{AB}^a
\right].
\]
Since \(V_B^{\rm line}=V_B^{3W}+q\),
\[
\boxed{
\begin{aligned}
\mathcal C_B^\mu=g_2\Big[
&\frac12\delta_BV_B^{3W,\mu}\mathcal S_B^a
+\left(\Delta_{BY}+\frac12\delta_B\right)q^\mu\mathcal S_B^a\\
&+\frac i2\delta_BV_B^{3W,\mu}\mathcal G_{AB}^a
+\frac i2\delta_Bq^\mu\mathcal G_{AB}^a
\Big].
\end{aligned}
}
\tag{3.1}
\]
Its actual opposite-endpoint contraction is
\[
\boxed{
\mathcal K_{06,B}
=\frac{(V_A^{3W}\cdot\mathcal C_B)\slashed h}{k^2}.
}
\tag{3.2}
\]
Here the q contacts are weighted by \(V_A^{3W}\cdot q\). They are not the same graph as (2.2).

## 4. The two seagull tensors remain distinct

The raw physical weak-index products give
\[
\mathcal S_A^a
=\mathcal W_A^a+\widetilde{\mathcal W}_A^a
=\frac12R_B^aT_0,
\]
\[
\mathcal S_B^a
=\mathcal W_B^a+\widetilde{\mathcal W}_B^a
=\frac12R_A^aT_0,
\]
and
\[
\mathcal W_A^a-\widetilde{\mathcal W}_A^a
=\mathcal W_B^a-\widetilde{\mathcal W}_B^a
=i\mathcal G_{AB}^a.
\]
The A and B anticommutator tensors are checked separately for all three external generators and all 16 weak-index components. The same \(\mathcal G_{AB}\) appears in the two commutators, but this does not identify \(\mathcal S_A\) with \(\mathcal S_B\).

## 5. Denominators and the actual three-W \(R_{\rm FG}\) numerator

The three-W denominator is
\[
D_{3W}=k^2\kappa^2(r_A^Y)^2(r_B^Y)^2(h^2-M_E^2).
\]
The scalar-line and seagull denominators are
\[
D_{A,\rm line}
=\kappa^2(r_B^Y)^2(r_A^Y)^2(r_A^W)^2(h^2-M_E^2),
\]
\[
D_{A,\rm sg}
=\kappa^2(r_B^Y)^2(r_A^Y)^2(h^2-M_E^2)
=\frac{D_{3W}}{k^2},
\]
\[
D_{B,\rm line}
=k^2(r_A^Y)^2(r_B^Y)^2(r_B^W)^2(h^2-M_E^2),
\]
\[
D_{B,\rm sg}
=k^2(r_A^Y)^2(r_B^Y)^2(h^2-M_E^2)
=\frac{D_{3W}}{\kappa^2}.
\]
Each scalar-line graph retains both propagators on its own scalar line; each seagull retains only its one adjacent scalar propagator. The two endpoint denominators are not interchanged.

The actual S–S Feynman-gauge remainder is
\[
\boxed{
\mathcal N_{06}
=(V_A^{3W}\cdot k)\slashed h(V_B^{3W}\cdot k)
-(V_A^{3W}\cdot\kappa)\slashed h(V_B^{3W}\cdot\kappa).
}
\tag{5.1}
\]
It is divided by \(k^2\kappa^2\), with the remaining factors \((r_A^Y)^2(r_B^Y)^2(h^2-M_E^2)\). The heavy numerator \(\slashed h\) remains inside the loop-side chain; unlike LD-W-03/04, it is not an external spectator.

## 6. Exact rational diagnostics

Two nonsingular rational five-point points are used, with \(M_E^2=400\) only as an algebraic diagnostic:

| Point | \((k^2,\kappa^2,(r_A^Y)^2,(r_B^Y)^2,h^2-M_E^2)\) | \(\delta_A\) | \(\delta_B\) |
|---|---|---:|---:|
| 1 | \((10,8,11,15,-393)\) | \(6/187\) | \(4/285\) |
| 2 | \((34,44,35,75,-377)\) | \(2/245\) | \(-14/4575\) |

All five three-W denominator factors and all A/B line/seagull denominator factors are nonzero at both points. The direct Lorentz-index contraction agrees with (5.1) in 32/32 matrix components. The A and B scalar endpoint kernels each agree before and after rebasing in all 64/64 matrix components. All four q-contact projections (A/B times symmetric/commutator) are nonzero at both points.

The exact source and six local tests are:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_common_k_SS_two_endpoint_bridge.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.txt\`

These are local exact SymPy checks, not a GitHub Actions result.

## 7. Boundary and next step

This completes the **pair-specific endpoint-current rebase** for all six LD-W-01…06 classes. It does not yet assemble the LD-W-06 A/B scalar-line terms with the two seagulls, the matter-line endpoint terms, and the three-W \(D(k)-D(\kappa)+R_{\rm FG}\) term into one Lorentz- and weak-index-weighted integrand. The A/B seagull tensors remain separate, and no contact term or \(R_{\rm FG}\) is discarded.

The next step is the full ordinary-matter common-\(k\) longitudinal integrand assembly across all six pair classes. That assembly must include the four fermion-line WTI endpoint pieces, all six scalar-line/seagull kernels, all six three-W kernels, the correct weak-index order and relative phases, and the local Yukawa-singlet charge cancellation. The four reducible external-leg/LSZ contributions and the BRST/ghost STI remain separate. No loop integration, UV–EFT subtraction, or Wilson coefficient should be attempted until this integrand-level Ward identity is closed.
