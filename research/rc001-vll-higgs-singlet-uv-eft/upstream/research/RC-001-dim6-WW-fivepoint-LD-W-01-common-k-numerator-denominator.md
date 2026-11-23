# RC-001 — LD-W-01 exact common-\(k\) F–F numerator/denominator bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-f/01  
**Status:** the LD-W-01 F–F commutator/three-W sub-block has now been checked with its actual ordered Dirac chain, physical weak tensors, relative phases, oriented fermion WTIs, and complete spectator denominators. The common-\(k\) transverse inverse-kernel pieces cancel exactly, leaving the explicit nonzero \(R_{\rm FG}\) projection. This is not the complete LD-W-01 five-point amplitude or the full 24-graph Slavnov–Taylor identity.

## 1. Fixed momenta and actual chain

Use all incoming external momenta
\[
p_1+p_2+p_3+p_4+q=0,\qquad \kappa=k+q,
\]
and for LD-W-01 set \(p_A=p_1,\ p_B=p_4\):
\[
r_A=k-p_1,\qquad r_A^Y=k-p_1-q,
\]
\[
r_B=k+p_4,\qquad r_B^Y=k+p_4+q,
\qquad h=k-p_1-p_2.
\]
The actual three-W reference chain is
\[
\mathcal X_{01}=-\slashed r_A\slashed h\slashed r_B^Y P_L.
\]
No endpoint current is replaced by an arbitrary vector, and the open Dirac order is not changed.

The full three-W denominator is
\[
\boxed{
\mathscr D_{3W}^{01}
=k^2\kappa^2r_A^2(r_B^Y)^2(h^2-M_E^2).
}
\tag{1.1}
\]

## 2. Oriented fermion WTIs and common-\(k\) maps

The two off-shell fermion identities are
\[
S_F(-r_A)\slashed qP_LS_F(-r_A^Y)
=S_F(-r_A)P_R-P_LS_F(-r_A^Y),
\tag{2.1}
\]
\[
S_F(r_B^Y)\slashed qP_LS_F(r_B)
=P_LS_F(r_B)-S_F(r_B^Y)P_R.
\tag{2.2}
\]
The A-side Yukawa-endpoint term uses \(k_{\rm old}=k+q\), giving
\[
r_A^Y(k_{\rm old})=r_A,\quad
r_B(k_{\rm old})=r_B^Y,\quad
h_A(k_{\rm old})=h,\quad
k_{\rm old}=\kappa.
\tag{2.3}
\]
The B-side Yukawa-endpoint term is already in the common routing:
\[
r_A=r_A,\quad r_B^Y=r_B^Y,\quad h=h,\quad k_W=k.
\tag{2.4}
\]
All 32 vector components in these two maps are checked exactly.

The corresponding single-W endpoint denominators are
\[
\mathscr D_{A,Y}^{01}
=\kappa^2r_A^2(r_B^Y)^2(h^2-M_E^2),
\]
\[
\mathscr D_{B,Y}^{01}
=k^2r_A^2(r_B^Y)^2(h^2-M_E^2),
\]
and satisfy
\[
\boxed{
\mathscr D_{3W}^{01}=k^2\mathscr D_{A,Y}^{01}
=\kappa^2\mathscr D_{B,Y}^{01}.
}
\tag{2.5}
\]
These are exact denominator identities. The full external-field/Yukawa endpoint gauge variations are still kept outside the commutator/three-W sub-block.

## 3. Physical weak tensors and relative phase

For the cross-vertex \(A=\bar L,\ B=L\) pair, the explicit physical-representation bridge gives
\[
\mathcal W_A^a-\widetilde{\mathcal W}_A^a
=i\mathcal G_{AB}^a,\qquad
\mathcal W_B^a-\widetilde{\mathcal W}_B^a
=i\mathcal G_{AB}^a,
\]
with
\[
\mathcal G_{AB}^a=\epsilon^{abc}R_{\bar L}^bR_L^cT_0.
\]
The relative matter-line phase is \(-g_2\), so both endpoint commutators carry
\[
-g_2(\mathcal W-\widetilde{\mathcal W})
=-ig_2\mathcal G_{AB}^a,
\]
equal to the three-W relative phase-weighted weak tensor. The present script independently checks the A and B identities for all three external generators and all 16 weak-index components (48/48 each).

## 4. Actual Feynman-gauge kernel and Dirac-chain identity

The bare vertex contraction is checked componentwise:
\[
q^\alpha\Gamma_{\alpha\mu\nu}(q,k,-k-q)
=\mathcal K_{\mu\nu}(\kappa)-\mathcal K_{\mu\nu}(k),
\]
where \(\mathcal K_{\mu\nu}(p)=p^2g_{\mu\nu}-p_\mu p_\nu\).

With \(D^{\mu\nu}(p)=g^{\mu\nu}/p^2\),
\[
D(\kappa)[\mathcal K(\kappa)-\mathcal K(k)]D(k)
=D(k)-D(\kappa)+R_{\rm FG},
\]
\[
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-\kappa^\mu\kappa^\nu}{k^2\kappa^2}.
\tag{4.1}
\]
The actual LD-W-01 chain is inserted on both sides of this identity. Define
\[
\mathcal N_{01}
=\slashed k\mathcal X_{01}\slashed k
-\slashed\kappa\mathcal X_{01}\slashed\kappa.
\]
The exact rational-point Dirac-matrix check confirms
\[
\gamma_\mu\mathcal X_{01}\gamma_\nu
\left[(D(\kappa)[\mathcal K(\kappa)-\mathcal K(k)]D(k))^{\mu\nu}
+(D(\kappa)-D(k))^{\mu\nu}\right]
=\frac{\mathcal N_{01}}{k^2\kappa^2}.
\tag{4.2}
\]
Thus the transverse \(D(k)-D(\kappa)\) pieces cancel in this isolated commutator/three-W sub-block, while the \(R_{\rm FG}\) term remains.

Restoring the common spectator denominator and phase-weighted weak tensor,
\[
\boxed{
\mathcal M_{01,\mathrm{comm}+3W}
=
\frac{-ig_2\mathcal G_{AB}^a}
{r_A^2(r_B^Y)^2(h^2-M_E^2)}
\frac{\mathcal N_{01}}{k^2\kappa^2}.
}
\tag{4.3}
\]
Equation (4.3) is the residual \(R_{\rm FG}\) projection, not an independently physical local interaction or a Wilson coefficient.

## 5. Exact checks and rational diagnostic

The standalone SymPy source checks:
- A/B oriented fermion WTIs: 32/32 Dirac components;
- A-shift and B-unshift common-\(k\) maps: 32/32 vector components;
- three-W versus single-W denominator factors: 2/2 exact identities;
- \(q^\alpha\Gamma_{\alpha\mu\nu}=\Delta\mathcal K_{\mu\nu}\): 16/16 Lorentz components;
- Feynman-gauge propagator-chain decomposition: 16/16 tensor components;
- physical A/B weak commutators and phase alignment: 48/48 components each;
- actual LD-W-01 Dirac-chain reduction to \(R_{\rm FG}\): 32/32 matrix components at an exact nonsingular rational point.

For
\[
\begin{aligned}
k&=(4,1,2,1),&q&=(1,2,0,1),\\
p_1&=(1,0,1,0),&p_2&=(0,1,0,2),\\
p_3&=(2,0,1,1),&p_4&=(-4,-3,-2,-4),
\end{aligned}
\]
with \(M_E^2=400\), the denominator factors are
\[
(k^2,\kappa^2,r_A^2,(r_B^Y)^2,h^2-M_E^2)
=(10,8,6,-3,-393).
\]
All are nonzero and all 16 entries of \(\mathcal N_{01}\) are nonzero. This is a nonsingular algebraic diagnostic, not a physical benchmark.

Reproduction:
- source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-01-common-k-numerator-denominator.py\`
- tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_01_common_k_numerator_denominator.py\`
- output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-01-common-k-numerator-denominator.txt\`

Six local regression tests pass. This is not a GitHub Actions result.

## 6. Boundary and next step

This calculation does **not** include the complete Yukawa-endpoint gauge variations, external-leg/LSZ terms, gauge-fixing/ghost Slavnov–Taylor completion, counterterms, other five-point pairs, loop integration, UV–EFT subtraction, or a Wilson coefficient. It does not set \(R_{\rm FG}\) to zero.

The next graph is LD-W-02 (F–S). Its B-side scalar current is momentum dependent, so its scalar-line commutator, seagull anticommutator and three-W current must be assembled together. The A-side fermion current remains the fixed-\(\gamma^\mu\) control endpoint. In particular, the \(V_B(k)\) versus \(V_B(k+q)\) difference must not be removed by inspection.
