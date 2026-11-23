# RC-001 — LD-W-02 projector/order reconciliation

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/06  
**Status:** the \(P_L/P_R\) placements in the actual A-oriented LD-W-02 F-S open chain have been reduced exactly. Both WTI endpoints share the rightmost \(P_L\) and the ordered \(\gamma_\mu\slashed r_A\slashed h_A\) chain, while retaining the distinct \(r_A^W\) and \(r_A^Y\) momenta. The two-W \(R_{\rm FG}\) numerator remains a separate object.

## 1. Chiral reduction

The oriented A-side WTI is
\[
S_A^W\slashed qP_LS_A^Y=S_A^WP_R-P_LS_A^Y,
\]
with
\[
S_A^W=-\frac{\slashed r_A^W}{(r_A^W)^2},\qquad
S_A^Y=-\frac{\slashed r_A^Y}{(r_A^Y)^2}.
\]
The open chain has the heavy spectator \(\slashed h_A P_L\) to the right. Its two endpoint terms reduce as
\[
\gamma_\mu S_A^WP_R\slashed h_AP_L
=-\frac{\gamma_\mu\slashed r_A^W\slashed h_AP_L}{(r_A^W)^2},
\]
\[
-\gamma_\mu P_LS_A^Y\slashed h_AP_L
=+\frac{\gamma_\mu\slashed r_A^Y\slashed h_AP_L}{(r_A^Y)^2}.
\]
The scalar spectator and the common-\(k\) current \(V_B(\kappa)\) are not absorbed into these projector manipulations. The four open Lorentz components pass 128/128 matrix-entry comparisons.

## 2. Keep the two-W remainder distinct

The graph-specific two-W projection follows the explicit cross-pair current ordering:
\[
\mathcal N_{02}^{\rm FG}
=\left[(V_B(\kappa)\cdot k)\slashed k(-\slashed r_A^W)\slashed h
-(V_B(\kappa)\cdot\kappa)\slashed\kappa(-\slashed r_A^W)\slashed h\right]P_L.
\]
The contracted single-W WTI endpoints have a different ordered structure and opposite endpoint signs:
\[
\mathcal E_W=-\slashed V_B(\kappa)\slashed r_A^W\slashed h_A P_L,\qquad
\mathcal E_Y=+\slashed V_B(\kappa)\slashed r_A^Y\slashed h_A P_L,
\]
with their respective fermion propagator denominators \((r_A^W)^2\) and \((r_A^Y)^2\).
These objects have different W-kernel and Dirac structures. The audit verifies that both are nonzero at the rational point, but does not identify them or infer a cancellation before the full longitudinal assembly.

At the common rational point,
\[
V_B(\kappa)\cdot k=-33,\qquad
V_B(\kappa)\cdot\kappa=-18.
\]
All W, fermion, scalar, and heavy denominators used in the local check are nonzero.

## 3. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-02-projector-order-reconciliation.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_02_projector_order_reconciliation.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-02-projector-order-reconciliation.txt\`

The exact SymPy assertions cover ten chiral intertwining identities and 128 endpoint matrix-entry reductions. Local execution against source commit `ddf9d41d408b4ee94ccb0c313befcb97423f4b81` used Python 3.13.5 and SymPy 1.14.0; the combined LD-W-02/LD-W-05 regression suite passed 9/9 tests (5/5 for LD-W-02 and 4/4 for LD-W-05). GitHub Actions are not claimed as passed; the latest candidate-schema, QLD8 counterterm-basis, and QLD chiral-Fierz runs concluded failure, with causes not established from the available job metadata.

No complete LD-W-02 scalar-line/seagull cancellation, 24-graph Ward identity, LSZ/ST closure, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
