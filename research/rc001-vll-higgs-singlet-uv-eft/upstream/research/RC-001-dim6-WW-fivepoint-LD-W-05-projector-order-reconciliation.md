# RC-001 — LD-W-05 projector/order reconciliation

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/05  
**Status:** the \(P_L/P_R\) placements in the actual B-oriented LD-W-05 WTI endpoints have been reduced using the physical Dirac algebra. Both endpoints have the same right-chiral open-chain orientation, but retain distinct \(r_B^W\) and \(r_B^Y\) momenta. The separately defined two-W \(R_{\rm FG}\) numerator remains a different kinematic object; no equality is imposed.

## 1. Exact chiral identities

For the chosen four-dimensional Dirac convention,
\[
P_L\gamma^\mu=\gamma^\mu P_R,\qquad
P_R\gamma^\mu=\gamma^\mu P_L,
\]
\[
P_L\slashed r=\slashed rP_R,\qquad
P_R\slashed r=\slashed rP_L.
\]
All ten matrix identities pass exactly.

## 2. Actual B-oriented WTI endpoint order

The oriented WTI is
\[
S_B^Y\slashed qP_LS_B^W=P_LS_B^W-S_B^YP_R.
\]
After inserting the heavy spectator on the left and the W vertex on the right, the two terms are
\[
\slashed hP_L\slashed r_B^W\gamma_\nu P_L,\qquad
-\slashed h\slashed r_B^YP_R\gamma_\nu P_L.
\]
The projector identities reduce them to
\[
\boxed{
\slashed h\slashed r_B^W\gamma_\nu P_L,\qquad
-\slashed h\slashed r_B^Y\gamma_\nu P_L.
}
\]
The rightmost \(P_L\) and the Dirac order are common; the two fermion momenta remain distinct. The four open Lorentz components pass 128/128 matrix-entry comparisons.

## 3. Keep the \(R_{\rm FG}\) numerator separate

The graph-specific cross-vertex LD-W-05 two-W projection has the order
\[
\mathcal N_{05}^{\rm FG}
=\left[(V_A\cdot k)\slashed h\slashed r_B^Y\slashed k
-(V_A\cdot\kappa)\slashed h\slashed r_B^Y\slashed\kappa\right]P_L.
\]
After contracting the single-W propagator with the scalar current, the two WTI endpoint numerators are instead
\[
\mathcal E_W=\slashed h\slashed r_B^W\slashed V_A P_L,\qquad
\mathcal E_Y=-\slashed h\slashed r_B^Y\slashed V_A P_L.
\]
The former contains the two-W inverse-kernel difference; the latter is the WTI endpoint after the single Feynman-gauge propagator is contracted with the scalar current. Their distinct matrix order and propagator structure must be preserved until the full longitudinal sum is assembled. The audit explicitly verifies that both structures are nonzero at the rational point and does not assert they are equal.

At the LD-W-05 rational point,
\[
V_A\cdot k= -28,\qquad V_A\cdot\kappa=-31.
\]
Both the \(R_{\rm FG}\) numerator and the single-W endpoint numerator have 16/16 nonzero matrix entries.

## 4. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-05-projector-order-reconciliation.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_05_projector_order_reconciliation.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-05-projector-order-reconciliation.txt\`

Local execution against source commit `ddf9d41d408b4ee94ccb0c313befcb97423f4b81` used Python 3.13.5 and SymPy 1.14.0. The calculation entry point passed, and the combined LD-W-05/LD-W-02 regression suite passed 9/9 tests (4/4 for LD-W-05 and 5/5 for LD-W-02). GitHub Actions are not claimed as passed; the latest candidate-schema, QLD8 counterterm-basis, and QLD chiral-Fierz runs concluded failure, with causes not established from the available job metadata. It does not close the scalar-line/seagull q contacts, the other pair classes, the four external-leg/LSZ terms, the ghost/ST sector, or the full ordinary-matter longitudinal integrand. No loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
