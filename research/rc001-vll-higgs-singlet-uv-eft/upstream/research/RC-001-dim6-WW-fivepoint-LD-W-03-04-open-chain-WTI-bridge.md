# RC-001 — LD-W-03/04 actual same-vertex open-chain WTI bridge

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/04  
**Status:** both same-vertex fermion-line WTI orientations have now been inserted into their graph-specific open chains. The \(03\) and \(04\) Dirac orders are kept distinct, their heavy spectators use the corresponding \(h_E\), and the scalar current \(V_S(k)\) is contracted with the \(k\)-momentum Feynman-gauge W propagator. This is the fermion-line sub-block only.

## 1. Two oriented WTIs

For \(r_F^Y=r_F^W+q\),
\[
S_F^W\slashed qP_LS_F^Y=S_F^WP_R-P_LS_F^Y
\qquad (03),
\]
\[
S_F^Y\slashed qP_LS_F^W=P_LS_F^W-S_F^YP_R
\qquad (04).
\]
Both symbolic identities pass in all 32 Dirac components.

## 2. LD-W-03 left-open chain

Use
\[
p_F=p_1,\quad p_S=p_2,\quad
h_E^{03}=p_1+p_2+q,\quad V_S(k)=2p_2-k.
\]
The ordered chain is
\[
\mathcal O_{03}^{q,\mu}
=\gamma^\mu S_F^W\slashed qP_LS_F^Y
\frac{\slashed h_E^{03}P_L}{(h_E^{03})^2-M_E^2}
\frac{1}{(r_S^Y)^2}.
\]
Replacing the insertion by \(S_F^WP_R-P_LS_F^Y\) preserves the open chain. The open Lorentz-index comparison passes 64/64 matrix components; the \(D(k)V_S(k)\) contraction passes 16/16 entries.

## 3. LD-W-04 right-open chain

Use
\[
p_F=p_4,\quad p_S=p_3,\quad
h_E^{04}=p_3+p_4+q,\quad V_S(k)=2p_3-k.
\]
The opposite ordered chain is
\[
\mathcal O_{04}^{q,\nu}
=\frac{\slashed h_E^{04}P_L}{(h_E^{04})^2-M_E^2}
S_F^Y\slashed qP_LS_F^W\gamma^\nu
\frac{1}{(r_S^Y)^2}.
\]
The replacement \(S_F^Y\slashed qP_LS_F^W\to P_LS_F^W-S_F^YP_R\) preserves the chain. Its open-index comparison passes 64/64 matrix components; the \(V_S(k)D(k)\) contraction passes 16/16 entries.

The heavy spectator is independent of \(k\), with all 16 derivatives checked exactly. The two orientations are not merged into a single Dirac chain.

## 4. Exact rational diagnostic

At
\[
\begin{aligned}
k&=(3,1,1,0),&q&=(1,0,1,1),\\
p_1&=(1,0,0,1),&p_2&=(0,1,0,0),\\
p_3&=(1,1,0,1),&p_4&=-q-p_1-p_2-p_3,\\
M_E^2&=400,
\end{aligned}
\]
the \(03\) denominator factors are
\[
(k^2,\kappa^2,(r_F^W)^2,(r_F^Y)^2,
(r_S^Y)^2,(r_S^W)^2,(h_E^{03})^2-M_E^2)
=(7,10,13,16,8,11,-402),
\]
and the \(04\) factors are
\[
(7,10,-10,-5,2,5,-401).
\]
All factors are nonzero. Each contracted open-chain matrix has 16/16 nonzero entries.

## 5. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-03-04-open-chain-WTI-bridge.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_03_04_open_chain_WTI_bridge.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-03-04-open-chain-WTI-bridge.txt\`

The exact SymPy assertions for both oriented WTIs, the two open chains, the two Feynman-gauge contractions, the endpoint decompositions, and heavy-spectator independence were executed directly in the local calculation session. The standalone unittest module is included for reproducibility; no GitHub Actions result is claimed.

This does **not** complete the four-attachment same-vertex Ward sum. The scalar-line/seagull terms, their weak-index weights, and the reducible external-leg/LSZ plus BRST/ghost completion must still be combined. No loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
