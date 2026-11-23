# RC-001 — Physical SU(2) representation bridge for the five-point weak tensors

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVa  
**Status:** the signed WTI actions used in the pair-projection audit are now explicitly related to the physical field-representation generators. The two-generator seed tensors are unchanged, while three-generator products acquire the expected overall sign. The physical-representation commutator and seagull identities are checked algebraically for all six pair labels. However, the raw open-chain mapping is established in two separate records: B2c-IVd for the four cross-vertex pairs LD-W-01/02/05/06, and B2c-IVe for same-vertex LD-W-03/04 with their distinct S-to-F internal-W orientation. This file remains the common field-representation algebra bridge, not the complete Lorentz-weighted 24-graph sum.

## 1. Physical field generators versus signed WTI actions

The exact \(SU(2)_L\) projection note uses the physical representations
\[
R_{\bar L}^a=-t^{aT},\qquad
R_H^a=+t^a,\qquad
R_{H^\dagger}^a=-t^{aT},\qquad
R_L^a=+t^a,
\qquad t^a=\frac{\sigma^a}{2}.
\]
The earlier Stage-B2b signed actions were
\[
\mathscr T_{\bar L}^a=+t^{aT},\quad
\mathscr T_H^a=-t^a,\quad
\mathscr T_{H^\dagger}^a=+t^{aT},\quad
\mathscr T_L^a=-t^a.
\]
Therefore
\[
\boxed{R_r^a=-\mathscr T_r^a}
\]
for every external slot. The physical generators satisfy the standard algebra
\[
[R_r^a,R_r^b]=+i\epsilon^{abc}R_r^c.
\]

This distinction matters:
- the seed pair tensor contains two generators, so \(R_A^bR_B^b=\mathscr T_A^b\mathscr T_B^b\);
- a five-point matter-line tensor contains three generators, so \(R_A^bR_A^aR_B^b=-\mathscr T_A^b\mathscr T_A^a\mathscr T_B^b\).

Thus the pair-projection table cannot be used to infer the sign of a three-generator graph tensor without this conversion.

## 2. Seed pair projections are unchanged

Define
\[
\mathcal T_{AB}=\sum_bR_A^bR_B^bT_0,
\qquad T_0=\delta_{ij}\delta_{kl}.
\]
The six exact projections remain
\[
\begin{array}{c|rrrrrr}
\text{pair}&01&02&03&04&05&06\\ \hline
\mathcal T_{AB}
&-\frac14T_3&+\frac14T_3&
-\frac34T_0&-\frac34T_0&
+\frac14T_3&-\frac14T_3
\end{array}
\]
with \(T_3=\sigma^I_{ij}\sigma^I_{kl}\). All 96 weak-index components reproduce the existing SU(2) attachment-projection note.

## 3. Candidate ordered physical-representation tensors

For the four cross-vertex pairs LD-W-01/02/05/06, the B1 propagator/vertex routes give the following open-chain order:

- A-side line: the internal-W endpoint precedes the external-W insertion in the open line chain;
- B-side line: the external-W insertion precedes the internal-W endpoint.

In the physical field-representation basis, the corresponding ordered tensors are
\[
\mathcal W_A^a
=\sum_bR_A^bR_A^aR_B^bT_0,
\qquad
\mathcal W_B^a
=\sum_bR_A^bR_B^aR_B^bT_0.
\]
The reversed Yukawa-endpoint orderings are
\[
\widetilde{\mathcal W}_A^a
=\sum_bR_A^aR_A^bR_B^bT_0,
\qquad
\widetilde{\mathcal W}_B^a
=\sum_bR_A^bR_B^bR_B^aT_0.
\]
With the physical algebra,
\[
\boxed{
\mathcal W_A^a-\widetilde{\mathcal W}_A^a
=+i\mathcal G_{AB}^a,
}
\]
\[
\boxed{
\mathcal W_B^a-\widetilde{\mathcal W}_B^a
=+i\mathcal G_{AB}^a,
}
\]
where
\[
\mathcal G_{AB}^a
=\epsilon^{abc}R_A^bR_B^cT_0
=\epsilon^{abc}\mathscr T_A^b\mathscr T_B^cT_0.
\]
The A- and B-side physical commutator signs are therefore both \(+i\mathcal G_{AB}^a\). This differs from the signed-action commutator labels in B2c-III exactly by the three-generator sign conversion.

These are the group-theory factors for the ordered products shown for the cross-vertex subset. The separate explicit-index bridge checks their mapping to the raw cross-vertex matrix chains. Do not apply this A/B graph-order assignment automatically to LD-W-03/04: their internal W is oriented from the scalar endpoint S to the fermion endpoint F, and their raw matrix order must be derived from that routing. The relative Lorentz signs from the two oriented line WTIs still have to be included before combining the cross-vertex A/B terms with the three-W graph.

## 4. Physical scalar-seagull tensors

The physical scalar generators obey
\[
\{R_{\rm scalar}^a,R_{\rm scalar}^b\}
=\frac12\delta^{ab}\mathbf1.
\]
Hence
\[
\boxed{
\mathcal S_A^a
=\sum_b\{R_A^a,R_A^b\}R_B^bT_0
=\frac12R_B^aT_0,
}
\]
\[
\boxed{
\mathcal S_B^a
=\sum_bR_A^b\{R_B^a,R_B^b\}T_0
=\frac12R_A^aT_0.
}
\]
The physical-representation seagull identities are checked algebraically for all scalar slots, three external-W generators and 16 weak-index components (288/288). For the cross-vertex scalar endpoints, the explicit raw-index bridge confirms that the seagull tensor is the sum of the two ordered matter-line tensors. For LD-W-03/04, the anticommutator identity alone does not determine which ordered product belongs to the graph because the internal W is oriented from S to F; the separate B2c-IVe raw-index bridge now derives that ordering.

The Lorentz coefficient \(q^\mu\) from the seagull vertex is not included in this group-only identity. It must be combined with the scalar-line WTI while retaining the distinct weak tensors.

## 5. Relative phase and what remains undetermined

The Feynman-rule phase ratios fixed in Stage B2c-I/II are
\[
P_{\rm line}/P_4=-g_2,\qquad
P_{\rm seagull}/P_4=+g_2,\qquad
P_{3W}/P_4=-ig_2.
\]
For the four cross-vertex pairs, the physical matter-line commutator tensor \(+i\mathcal G_{AB}^a\) carries the phase-weighted group factor \(-ig_2\mathcal G_{AB}^a\). The three-W graph has the same group-phase factor, multiplying its own contracted Lorentz kernel. Do not extend this graph-order statement to LD-W-03/04 before deriving their raw S-to-F chains.

This equality of phase-weighted group factors is **not** a cancellation proof. The A/B line WTI endpoint signs, the two terms in the three-W inverse-kernel difference, the scalar seagull Lorentz terms, and the Feynman-gauge remainder must be assembled in one common numerator expression. In particular, do not infer the sign of the final sum from the group tensor alone.

## 6. Reproduction and evidence boundary

The exact SymPy calculation is in
calculations/RC-001-dim6-WW-fivepoint-physical-representation-bridge.py
with output in
validation/RC-001-dim6-WW-fivepoint-physical-representation-bridge.txt.

It checks:
- the physical generator algebra \([R^a,R^b]=+i\epsilon^{abc}R^c\) for all four field slots;
- all six pair projections (96/96);
- candidate A-line ordered commutator relation in the physical-representation algebra (288/288);
- candidate B-line ordered commutator relation in the physical-representation algebra (288/288);
- physical scalar-seagull tensors (288/288).

This does not establish:
1. the complete Lorentz-weighted cross-vertex A/B matter-line plus three-W cancellation;
2. the Lorentz-weighted same-vertex LD-W-03/04 line/three-W sum;
3. the scalar-line/seagull endpoint sum with distinct weak tensors;
4. the ghost/gauge-fixing Slavnov–Taylor completion;
5. external-leg/LSZ and counterterm terms;
6. any integrated five-point hard coefficient or transverse form factor.

The next task is to combine the cross-vertex raw-index tensors with the B1 momentum routes and the graph-specific Lorentz numerators, then perform the \(q_\alpha\) contraction and common-loop-momentum shift algebra before integration. The same-vertex LD-W-03/04 raw chains must be derived separately rather than imported from the cross-vertex A/B template.
