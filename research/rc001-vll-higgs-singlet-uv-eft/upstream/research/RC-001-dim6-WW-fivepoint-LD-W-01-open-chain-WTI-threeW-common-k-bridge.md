# RC-001 — LD-W-01 actual open-chain WTI and three-W common-\(k\) bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/01  
**Status:** the two actual LD-W-01 fermion-line insertions have now been contracted with \(q_\alpha\) inside their complete Feynman-gauge open chains. Their oriented WTIs, the A-side Yukawa-endpoint loop shift, the two single-W denominator alignments to the three-W reference, and the actual \(R_{\rm FG}\) numerator are checked. The first endpoint terms remain explicit; this is not the complete 24-graph sum.

## 1. Fixed LD-W-01 routing

Use all incoming external momenta and
\[
p_1+p_2+p_3+p_4+q=0,\qquad \kappa=k+q,
\]
\[
r_A^W=k-p_1,\quad r_A^Y=k-p_1-q,\qquad
r_B^W=k+p_4,\quad r_B^Y=k+p_4+q,
\]
\[
h=k-p_1-p_2,\qquad h_A=h-q.
\]
The physical fermion propagators are
\[
S_A^W=-\frac{\slashed r_A^W}{(r_A^W)^2},\quad
S_A^Y=-\frac{\slashed r_A^Y}{(r_A^Y)^2},\quad
S_B^W=\frac{\slashed r_B^W}{(r_B^W)^2},\quad
S_B^Y=\frac{\slashed r_B^Y}{(r_B^Y)^2}.
\]

## 2. Actual A/B fermion-line WTI insertions

The A-side insertion is
\[
\boxed{
S_A^W\slashed qP_LS_A^Y
=S_A^WP_R-P_LS_A^Y.
}
\tag{2.1}
\]
The B-side insertion has the opposite orientation:
\[
\boxed{
S_B^Y\slashed qP_LS_B^W
=P_LS_B^W-S_B^YP_R.
}
\tag{2.2}
\]
These identities are inserted into the actual open chains:
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
The Feynman-gauge Lorentz contraction is performed explicitly. The two open-chain equalities pass independently in all 16 Dirac-matrix components each.

## 3. A-side Yukawa endpoint and the common-\(k\) map

The A-side second WTI term uses the original loop variable \(k_{\rm old}\). Set
\[
k_{\rm old}=k+q.
\]
Then
\[
\begin{aligned}
r_A^Y(k_{\rm old})&=r_A^W(k),\\
h_A(k_{\rm old})&=h(k),\\
r_B^W(k_{\rm old})&=r_B^Y(k),\\
k_{\rm old}&=\kappa.
\end{aligned}
\tag{3.1}
\]
All 16 vector components are checked exactly. Thus the A-side second endpoint term uses the \(\kappa\)-momentum W propagator and the same \(r_A,h,r_B^Y\) spectator factors as the three-W reference.

The B-side second WTI term is already in the common-\(k\) routing and uses the \(k\)-momentum W propagator.

## 4. Denominator alignment

The three-W denominator is
\[
D_{3W}=k^2\kappa^2(r_A^W)^2(r_B^Y)^2(h^2-M_E^2).
\]
After the A-side shift, its second WTI endpoint denominator is
\[
D_{A,Y}^{\rm shifted}
=\kappa^2(r_A^W)^2(r_B^Y)^2(h^2-M_E^2)
=\frac{D_{3W}}{k^2}.
\]
The B-side second WTI endpoint denominator is
\[
D_{B,Y}^{\rm common}
=k^2(r_A^W)^2(r_B^Y)^2(h^2-M_E^2)
=\frac{D_{3W}}{\kappa^2}.
\]
These are the two single-W denominator factors appearing in the three-W inverse-kernel difference. The first A/B WTI endpoint terms are not silently identified with them: they retain their own \(h-q,r_B^W\) or \(h,r_B^W\) Yukawa-channel denominators.

## 5. Actual \(R_{\rm FG}\) remainder

The actual ordered chain is
\[
\mathcal X_{01}=-\slashed r_A^W\slashed h\slashed r_B^YP_L.
\]
The direct contraction of this chain with
\[
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-\kappa^\mu\kappa^\nu}{k^2\kappa^2}
\]
is checked against
\[
\mathcal N_{01}
=\slashed k\mathcal X_{01}\slashed k
-\slashed\kappa\mathcal X_{01}\slashed\kappa.
\]
All 16 numerator entries are nonzero at the chosen nonsingular rational point, and the direct Lorentz contraction agrees with the factorized expression in all 16 matrix components.

The weak-index commutator phases and the local Yukawa-singlet charge factors are recorded in the earlier cross-vertex and all-six shifted-charge audits. They are not reinterpreted here as a complete cancellation.

## 6. Exact rational point

Use
\[
\begin{aligned}
k&=(4,1,2,1),&q&=(1,2,0,1),\\
p_1&=(1,0,1,0),&p_2&=(0,1,0,2),\\
p_3&=(2,1,1,1),&p_4&=(-4,-4,-2,-4).
\end{aligned}
\]
With \(M_E^2=400\), the denominator factors are
\[
(k^2,\kappa^2,(r_A^W)^2,(r_A^Y)^2,
(r_B^W)^2,(r_B^Y)^2,h^2-M_E^2,(h-q)^2-M_E^2)
\]
\[
=(10,8,6,2,-18,-4,-393,-405).
\]
All are nonzero. The A-shifted and B-common endpoint denominators are
\[
(8,6,-4,-393),\qquad (10,6,-4,-393),
\]
matching \(D_{3W}/k^2\) and \(D_{3W}/\kappa^2\), respectively.

## 7. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-01-open-chain-WTI-threeW-common-k-bridge.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_01_open_chain_WTI_threeW_common_k_bridge.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-01-open-chain-WTI-threeW-common-k-bridge.txt\`

The local exact checks include 32/32 open-chain WTI Dirac components, 16/16 A-side shift-vector components, two exact denominator alignments, and the actual \(R_{\rm FG}\) contraction. No GitHub Actions result is claimed.

This does **not** combine the first A/B endpoint terms with all local Yukawa variations, the three-W propagator difference, or the reducible external-leg/LSZ terms. No complete 24-graph Ward identity, ghost/ST closure, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
