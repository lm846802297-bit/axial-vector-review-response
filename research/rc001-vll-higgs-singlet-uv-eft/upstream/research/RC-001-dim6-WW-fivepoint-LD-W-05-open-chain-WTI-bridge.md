# RC-001 — LD-W-05 actual S-F open-chain WTI bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/03  
**Status:** the B-side fermion-line insertion has now been contracted inside the actual ordered S-F open chain. The calculation retains the A scalar propagator, the heavy-fermion spectator, the common-\(k\) A scalar current \(V_A(k)\), and the \(k\)-momentum Feynman-gauge W propagator. The B-oriented WTI is checked with its actual right-open Lorentz index and after contraction.

## 1. B-side fermion WTI

With
\[
r_B^Y=r_B^W+q,\qquad
S_B^W=\frac{\slashed r_B^W}{(r_B^W)^2},\qquad
S_B^Y=\frac{\slashed r_B^Y}{(r_B^Y)^2},
\]
the oriented identity is
\[
\boxed{
S_B^Y\slashed qP_LS_B^W
=P_LS_B^W-S_B^YP_R.
}
\]
The symbolic Dirac-matrix identity passes in all 16 components.

## 2. Actual ordered S-F open chain

The common-\(k\) B-side sub-block uses
\[
V_A^\mu(k)=(2p_2-k)^\mu,\qquad
D^{\mu\nu}(k)=\frac{g^{\mu\nu}}{k^2},
\]
and the heavy and A-scalar spectators. The ordered fermion chain is
\[
\mathcal O_{05}^{q,\nu}
=
\frac{1}{(r_A^Y)^2}
\frac{\slashed h}{h^2-M_E^2}
S_B^Y\slashed qP_LS_B^W\gamma^\nu.
\]
Contracting its left scalar current and internal W index gives
\[
\mathcal A_{05}^{q}
=
V_{A,\mu}(k)\frac{1}{(r_A^Y)^2}
\frac{\slashed h}{h^2-M_E^2}
S_B^Y\slashed qP_LS_B^W
D^{\mu\nu}(k)\gamma_\nu.
\]
The replacement
\[
S_B^Y\slashed qP_LS_B^W
\longrightarrow
P_LS_B^W-S_B^YP_R
\]
leaves the full open chain unchanged. The open Lorentz-index comparison passes 64/64 Dirac components; the Feynman-gauge contracted matrix comparison passes 16/16 entries. The two endpoint terms are kept separately and sum exactly to the left-hand side.

The \(P_L/P_R\) order is preserved exactly as given by the B-oriented WTI. It is not silently identified with the separately tabulated \(R_{\rm FG}\) numerator; that projector/order comparison remains an explicit follow-up check.

## 3. Common-\(k\) endpoint route

The B-side Yukawa endpoint is already in the common-\(k\) routing:
\[
r_A^Y=k-p_2,\quad
r_B^Y=k+p_4+q,\quad
h=k-p_1-p_2,\quad
V_A=2p_2-k,
\]
with internal W momentum \(k\). The the unshifted B-line relation and the equality of the two expressions for the heavy channel pass 8/8 vector components.

## 4. Exact rational diagnostic

At
\[
\begin{aligned}
k&=(5,1,2,0),&q&=(0,1,1,2),\\
p_1&=(1,1,0,1),&p_2&=(0,2,1,0),\\
p_3&=(2,0,1,1),&p_4&=-p_1-p_2-p_3-q,\\
M_E^2&=400,
\end{aligned}
\]
the denominator factors are
\[
(k^2,\kappa^2,(r_A^Y)^2,(r_A^W)^2,
(r_B^W)^2,(r_B^Y)^2,h^2-M_E^2)
=(20,8,17,23,-22,-4,-390).
\]
Every factor is nonzero. The contracted open-chain matrix has 16/16 nonzero entries at this point.

## 5. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-05-open-chain-WTI-bridge.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_05_open_chain_WTI_bridge.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-05-open-chain-WTI-bridge.txt\`

The exact SymPy assertions for the oriented WTI, open-index chain, Feynman-gauge scalar-current contraction, endpoint split, and common-\(k\) route were executed directly in the local calculation session. The standalone unittest module is included for reproducibility; no GitHub Actions result is claimed.

This does **not** cancel the A-side scalar-line/seagull q contacts against the fermion endpoint terms, external-leg/LSZ pieces, or the BRST/ghost sector. The separate \(R_{\rm FG}\) projector/order comparison remains open. No complete 24-graph Ward identity, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
