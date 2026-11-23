# RC-001 — LD-W-02 actual F-S open-chain WTI bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/02  
**Status:** the A-side fermion-line insertion has now been contracted inside the actual mixed F-S open chain. The calculation retains the B scalar propagator, the heavy-fermion spectator, the common-\(k\) B scalar current \(V_B(\kappa)\), and the corresponding \(\kappa\)-momentum Feynman-gauge W propagator. The oriented WTI is checked both before and after the full open-chain contraction.

## 1. A-side fermion WTI

With
\[
r_A^Y=r_A^W-q,\qquad
S_A^W=-\frac{\slashed r_A^W}{(r_A^W)^2},\qquad
S_A^Y=-\frac{\slashed r_A^Y}{(r_A^Y)^2},
\]
the oriented identity is
\[
\boxed{
S_A^W\slashed qP_LS_A^Y
=S_A^WP_R-P_LS_A^Y.
}
\]
The symbolic Dirac-matrix identity passes in all 16 components.

## 2. Actual mixed F-S open chain

In the common-\(k\) A-side sub-block, the B scalar current is
\[
V_B^\nu(\kappa)=-(2p_3+\kappa)^\nu,\qquad \kappa=k+q,
\]
and the heavy channel before the A-side endpoint shift is \(h_A=h-q\). The open chain is
\[
\mathcal O_{02}^{\alpha}
=\gamma^\alpha
S_A^W\slashed qP_LS_A^Y
\frac{\slashed h_A P_L}{h_A^2-M_E^2}
\frac{1}{(r_B^Y)^2}.
\]
Contracting its internal W index with the Feynman-gauge propagator and the actual B scalar current gives
\[
\mathcal A_{02}^{q}
=\gamma_\mu
S_A^W\slashed qP_LS_A^Y
\frac{\slashed h_A P_L}{h_A^2-M_E^2}
\frac{1}{(r_B^Y)^2}
D^{\mu\nu}(\kappa)V_{B,\nu}(\kappa),
\qquad
D^{\mu\nu}(\kappa)=\frac{g^{\mu\nu}}{\kappa^2}.
\]
The same expression with
\[
S_A^W\slashed qP_LS_A^Y
\longrightarrow S_A^WP_R-P_LS_A^Y
\]
is exactly equal. The open Lorentz-index comparison passes 64/64 Dirac components (four Lorentz components times 16 matrix entries); the contracted matrix comparison passes 16/16 entries. The two endpoint terms on the right-hand side are also retained separately and sum exactly to the contracted left-hand side.

## 3. Common-\(k\) endpoint route

The A-side Yukawa endpoint uses the old loop momentum \(k_{\rm old}=k+q\). The exact maps are
\[
\begin{aligned}
r_A^Y(k_{\rm old})&=r_A^W(k),\\
r_B^W(k_{\rm old})&=r_B^Y(k),\\
h_A(k_{\rm old})&=h(k),\\
k_{\rm old}&=\kappa.
\end{aligned}
\]
All 16 vector components are checked. Thus the shifted endpoint uses the same \(r_A^W,r_B^Y,h\) spectator factors as the common-\(k\) reference and the \(\kappa\)-momentum W propagator.

## 4. Exact rational diagnostic

At
\[
\begin{aligned}
k&=(5,1,2,0),&q&=(0,1,1,2),\\
p_1&=(1,1,0,1),&p_2&=(0,2,1,0),\\
p_3&=(2,0,1,1),&M_E^2&=400,
\end{aligned}
\]
the denominators used by the complete open chain are
\[
\begin{aligned}
(k^2,\kappa^2,(r_A^W)^2,(r_A^Y)^2,
(r_B^W)^2,(r_B^Y)^2,\\
h^2-M_E^2,(h-q)^2-M_E^2)
=(20,8,11,5,38,20,-390,-402).
\end{aligned}
\]
Every factor is nonzero. The contracted open-chain matrix has 16/16 nonzero entries at this point, so the test is not vacuous.

## 5. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-02-open-chain-WTI-bridge.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_02_open_chain_WTI_bridge.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-02-open-chain-WTI-bridge.txt\`

The exact SymPy assertions for the oriented WTI, open-index chain, Feynman-gauge scalar-current contraction, endpoint split, and common-\(k\) map were executed directly in the local calculation session. The standalone unittest module is included for reproducibility; no GitHub Actions result is claimed.

This does **not** cancel the B-side scalar-line/seagull q contacts against the fermion endpoint terms, external-leg/LSZ pieces, or the BRST/ghost sector. No complete 24-graph Ward identity, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
