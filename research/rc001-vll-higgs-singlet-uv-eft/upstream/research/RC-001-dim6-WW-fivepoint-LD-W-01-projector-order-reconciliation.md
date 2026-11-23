# RC-001 — LD-W-01 F–F WTI projector/order reconciliation

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/07  
**Status:** completed local algebraic/projector audit for the LD-W-01 F–F pair. Both oriented fermion-WTI endpoint chains have been reduced with their actual Dirac ordering; the shifted A-side and unshifted B-side second endpoints agree in common-\(k\) routing; and the final \(P_L\) placement in the pair-specific two-W \(R_{\rm FG}\) numerator is checked. This does not close the complete six-pair longitudinal identity.

## 1. Conventions and fixed routing

Use
\[
\eta_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1),\qquad
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad
P_{L,R}=\frac{1\mp\gamma_5}{2},
\]
\[
p_1+p_2+p_3+p_4+q=0,\qquad \kappa=k+q.
\]
For LD-W-01, \(p_A=p_1\) and \(p_B=p_4\):
\[
r_A^W=k-p_1,\quad r_A^Y=k-p_1-q,\qquad
r_B^W=k+p_4,\quad r_B^Y=k+p_4+q,
\]
\[
h=k-p_1-p_2,\qquad h_A=h-q.
\]
The propagator numerators and signs are
\[
S_A^{W,Y}=-\frac{\slashed r_A^{W,Y}}{(r_A^{W,Y})^2},\qquad
S_B^{W,Y}=+\frac{\slashed r_B^{W,Y}}{(r_B^{W,Y})^2}.
\]
The exact diagnostic uses \(M_E^2=400\); this is a nonsingular algebraic point, not a physical benchmark.

## 2. Both oriented WTI endpoint reductions

The two fermion identities are
\[
S_A^W\slashed qP_LS_A^Y=S_A^WP_R-P_LS_A^Y,
\]
\[
S_B^Y\slashed qP_LS_B^W=P_LS_B^W-S_B^YP_R.
\]
With the actual F–F open-chain ordering, the four endpoint reductions are
\[
\begin{aligned}
\gamma_\mu S_A^WP_R\slashed h_A S_B^W\gamma_\nu P_L
&=\gamma_\mu S_A^W\slashed h_A S_B^W\gamma_\nu P_L,\\
-\gamma_\mu P_LS_A^Y\slashed h_A S_B^W\gamma_\nu P_L
&=-\gamma_\mu S_A^Y\slashed h_A S_B^W\gamma_\nu P_L,\\
\gamma_\mu S_A^W\slashed hP_LS_B^W\gamma_\nu P_L
&=\gamma_\mu S_A^W\slashed hS_B^W\gamma_\nu P_L,\\
-\gamma_\mu S_A^W\slashed hS_B^YP_R\gamma_\nu P_L
&=-\gamma_\mu S_A^W\slashed hS_B^Y\gamma_\nu P_L.
\end{aligned}
\]
These follow from \(P_L\gamma^\mu=\gamma^\mu P_R\), \(P_R\gamma^\mu=\gamma^\mu P_L\), and the corresponding slash-momentum identities. The exact matrix comparison covers all four Lorentz-index pairs \((\mu,\nu)\) and all 16 Dirac entries for each endpoint: \(1024/1024\) entries pass.

## 3. Common-\(k\) equality of the second endpoints

For the A-side second endpoint set \(k_{\rm old}=k+q\). Then
\[
r_A^Y(k_{\rm old})=r_A^W(k),\quad
h_A(k_{\rm old})=h(k),\quad
r_B^W(k_{\rm old})=r_B^Y(k),\quad
k_{\rm old}=\kappa.
\]
After this shift, the A-side second endpoint is
\[
-\gamma_\mu P_LS_A^W\slashed hS_B^Y\gamma_\nu P_L.
\]
The B-side second endpoint is already in the common routing:
\[
-\gamma_\mu S_A^W\slashed hS_B^YP_R\gamma_\nu P_L.
\]
Both reduce to the same ordered chain,
\[
\boxed{-\gamma_\mu S_A^W\slashed hS_B^Y\gamma_\nu P_L.}
\]
The equality is checked in \(256/256\) matrix entries. The A-side shift map passes \(16/16\) vector components.

The W propagator momenta are not identified: the shifted A-side term carries the \(\kappa\)-momentum W propagator, whereas the B-side term carries the \(k\)-momentum W propagator. With
\[
D_{3W}=k^2\kappa^2(r_A^W)^2(r_B^Y)^2(h^2-M_E^2),
\]
their single-W denominators satisfy
\[
D_{A,Y}^{\rm shifted}=\frac{D_{3W}}{k^2},\qquad
D_{B,Y}^{\rm common}=\frac{D_{3W}}{\kappa^2}.
\]
Both identities pass exactly. The first A/B endpoints retain their separate \(h-q\) versus \(h\), and \(r_B^W\) spectator routing.

## 4. Pair-specific two-W \(R_{\rm FG}\) ordering

The stripped common matter chain is
\[
X_{01}=-\slashed r_A^W\slashed h\slashed r_B^Y.
\]
The pair-specific Feynman-gauge remainder is
\[
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-\kappa^\mu\kappa^\nu}{k^2\kappa^2},
\]
and its numerator is
\[
\boxed{
N_{01}=\slashed kX_{01}\slashed kP_L
-\slashed\kappa X_{01}\slashed\kappa P_L.
}
\]
The direct Lorentz-index contraction and this factorized expression agree in all \(16/16\) matrix entries. The final \(P_L\) acts after the right W current. The former placement with \(P_L\) inserted before the right \(\slashed k\) or \(\slashed\kappa\) is rejected in \(16/16\) entries.

At the rational point, \(N_{01}\) is nonzero in all 16 entries and remains distinct from the common one-W endpoint chain and from all four Feynman-gauge endpoint contractions (\(64/64\) matrix-entry differences). Thus this audit does not set \(R_{\rm FG}\) to zero or identify it with a single-W endpoint.

## 5. Exact rational diagnostic and checks

Use
\[
\begin{aligned}
k&=(4,1,2,1),&q&=(1,2,0,1),\\
p_1&=(1,0,1,0),&p_2&=(0,1,0,2),\\
p_3&=(2,0,1,1),&p_4&=(-4,-3,-2,-4).
\end{aligned}
\]
The denominator factors are
\[
(k^2,\kappa^2,(r_A^W)^2,(r_A^Y)^2,
(r_B^W)^2,(r_B^Y)^2,h^2-M_E^2,h_A^2-M_E^2)
=(10,8,6,2,-13,-3,-393,-405).
\]
All are nonzero.

Local execution used Python 3.13.5, SymPy 1.14.0, Linux x86_64 / glibc 2.41. The calculation entry point passed, and the standalone unittest suite passed \(6/6\) tests. Exact source and test files:
- calculations/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation.py
- calculations/test_RC001_dim6_WW_fivepoint_LD_W_01_projector_order_reconciliation.py

Captured output and provenance:
- validation/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation.txt
- validation/RC-001-dim6-WW-fivepoint-LD-W-01-projector-order-reconciliation-run-manifest.json

## 6. Boundary

This closes only the LD-W-01 F–F projector/order sub-block. It does not assemble the complete 24-attachment sum, the other five pair classes, all local Yukawa variations, reducible external-leg/LSZ terms, gauge-fixing/ghost Slavnov–Taylor completion, or counterterms. No loop integration, UV–EFT subtraction, transverse form factor, Wilson coefficient, or physical matching claim is made.
