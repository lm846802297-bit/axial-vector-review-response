# RC-001 — Explicit raw-index weak bridge for cross-vertex \(WW\) five-point graphs

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVd  
**Status:** the four cross-vertex seed pairs LD-W-01/02/05/06 now have an explicit weak-index contraction using the physical field-representation matrices. The ordered A/B matter-line tensors, their commutators, the scalar seagull anticommutators, and the relative phase factors are checked component by component. This covers 16 of the 24 direct five-point attachments. The same-vertex pairs LD-W-03/04 are deliberately excluded from the ordering claim because their internal W is oriented from the scalar endpoint to the fermion endpoint; their raw chains require a separate derivation.

## 1. Scope and fixed field representations

Use the all-incoming four-point tensor ordering
\[
(\bar L_i,H_j,H^\dagger_k,L_l),\qquad
T_0{}_{ijkl}=\delta_{ij}\delta_{kl}.
\]
The physical field-representation generators are
\[
R_{\bar L}^a=-t^{aT},\qquad
R_H^a=+t^a,\qquad
R_{H^\dagger}^a=-t^{aT},\qquad
R_L^a=+t^a,
\qquad t^a=\frac{\sigma^a}{2}.
\]
They obey
\[
[R_r^a,R_r^b]=i\epsilon^{abc}R_r^c.
\]
The script implements these matrices directly and contracts the internal weak indices explicitly. It does not call the earlier signed-action helper, so the three-generator sign conversion is not hidden in an action-basis convention.

For the cross-vertex classes, A is the line attached to the left Yukawa vertex and B is the line attached to the right conjugate Yukawa vertex. The fixed assignments are
\[
\begin{array}{c|cc}
\text{pair}&A&B\\ \hline
\text{LD-W-01}&\bar L&L\\
\text{LD-W-02}&\bar L&H^\dagger\\
\text{LD-W-05}&H&L\\
\text{LD-W-06}&H&H^\dagger
\end{array}
\]
and reproduce the four seed projections
\[
\mathcal T_{AB}=\sum_bR_A^bR_B^bT_0
=\left(-\frac14,+\frac14,+\frac14,-\frac14\right)T_3.
\]

## 2. Ordered raw-index products from the open chains

For the cross-vertex momentum routing in the B1 record, the internal-W endpoint and external-W insertion occur in opposite matrix order on the two sides of the open exchange chain. The raw physical-representation tensors are
\[
\mathcal W_A^a
=\sum_bR_A^bR_A^aR_B^bT_0,
\qquad
\widetilde{\mathcal W}_A^a
=\sum_bR_A^aR_A^bR_B^bT_0,
\]
\[
\mathcal W_B^a
=\sum_bR_A^bR_B^aR_B^bT_0,
\qquad
\widetilde{\mathcal W}_B^a
=\sum_bR_A^bR_B^bR_B^aT_0.
\]
Here the tilded tensors are the reversed endpoint orderings used to isolate the commutator. They are not extra Feynman graphs.

Define the three-W weak tensor
\[
\mathcal G_{AB}^a
=\epsilon^{abc}R_A^bR_B^cT_0.
\]
The exact raw-matrix contractions give
\[
\boxed{
\mathcal W_A^a-\widetilde{\mathcal W}_A^a
=+i\mathcal G_{AB}^a,
\qquad
\mathcal W_B^a-\widetilde{\mathcal W}_B^a
=+i\mathcal G_{AB}^a.
}
\tag{2.1}
\]
These identities are checked for every one of the four cross-vertex pairs, all three external-W generators and all 16 weak-index components.

## 3. Relative Feynman-rule phases

Relative to the corresponding four-point seed graph, the already-audited phase ratios are
\[
\frac{P_{\rm line}}{P_4}=-g_2,\qquad
\frac{P_{\rm seagull}}{P_4}=+g_2,\qquad
\frac{P_{3W}}{P_4}=-ig_2.
\]
Combining the first relation with (2.1),
\[
\boxed{
-g_2(\mathcal W_A^a-\widetilde{\mathcal W}_A^a)
=-ig_2\mathcal G_{AB}^a,
}
\]
\[
\boxed{
-g_2(\mathcal W_B^a-\widetilde{\mathcal W}_B^a)
=-ig_2\mathcal G_{AB}^a.
}
\]
The right-hand side is the same weak tensor and relative phase as the three-W insertion. This is the required group-phase alignment for the matter-line/three-W Ward sum. It is **not yet a cancellation**: the Lorentz kernels, their shifted loop momenta, and the Feynman-gauge remainder must still be combined before a sign or cancellation can be claimed.

## 4. Scalar seagulls: the weak tensor cannot be factored out as if it were the line tensor

For a scalar endpoint A, the raw two-gauge vertex gives
\[
\mathcal S_A^a
=\sum_b\{R_A^a,R_A^b\}R_B^bT_0
=\mathcal W_A^a+\widetilde{\mathcal W}_A^a
=\frac12R_B^aT_0.
\]
For a scalar endpoint B,
\[
\mathcal S_B^a
=\sum_bR_A^b\{R_B^a,R_B^b\}T_0
=\mathcal W_B^a+\widetilde{\mathcal W}_B^a
=\frac12R_A^aT_0.
\]
The exact component checks are 96/96 for each scalar-endpoint family in this four-pair subset.

This has an important consequence for the Lorentz bookkeeping. The ordinary scalar-line graph carries one ordered tensor, \(\mathcal W_A\) or \(\mathcal W_B\), whereas the seagull carries the **sum** of the two orderings. For example, the A-side scalar contribution has the schematic phase-weighted structure
\[
-g_2\,(\Delta_Y-\Delta_W)V_A^\mu\,
\mathcal W_A^a
+g_2\,\Delta_Yq^\mu\,\mathcal S_A^a,
\]
with the common spectator, heavy, internal-W and loop factors understood. The B-side expression has its own reversed scalar-line Ward sign and \(\mathcal S_B^a\). Therefore one must not combine scalar-line and seagull terms into a single stripped Lorentz vector while silently assigning them the same weak tensor.

Equivalently,
\[
\mathcal W_A^a=\frac12\mathcal S_A^a+\frac{i}{2}\mathcal G_{AB}^a,
\qquad
\mathcal W_B^a=\frac12\mathcal S_B^a+\frac{i}{2}\mathcal G_{AB}^a.
\]
This decomposition separates the symmetric scalar/seagull tensor from the antisymmetric commutator tensor that is paired with the three-W graph.

**Correction to the preceding Lorentz-only audit:** its stripped scalar numerator identity checks the kinematic factors only. It does not establish a complete weak-index-weighted scalar-line-plus-seagull identity. The weak factors must be kept separately as above. No scalar-endpoint Ward cancellation is claimed until both factors are inserted into the common routed integrand.

## 5. Which 16 attachments are covered

| Pair | A-line | B-line | Scalar seagull(s) | Three-W | Total |
|---|---:|---:|---:|---:|---:|
| LD-W-01 | 1 | 1 | 0 | 1 | 3 |
| LD-W-02 | 1 | 1 | 1 (B) | 1 | 4 |
| LD-W-05 | 1 | 1 | 1 (A) | 1 | 4 |
| LD-W-06 | 1 | 1 | 2 (A and B) | 1 | 5 |
| **Total** | **4** | **4** | **4** | **4** | **16** |

The remaining eight direct attachments are LD-W-03/04 (four each). Their four-point seed routings and all five-point momentum-conservation equations, including
\[
P_E=P_{FS}+q,
\]
are already checked in calculations/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.py. They are not missing momentum routes. What remains open for those two pairs is the raw weak-index matrix order and its combination with their distinct \(S\to F\) internal-W orientation.

## 6. Reproduction and evidence boundary

- Exact explicit-index source: calculations/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.py
- Captured output: validation/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.txt

The local exact SymPy checks establish:
- physical representation algebra: 144/144 matrix components;
- four seed pair tensors: 64/64 weak components;
- A- and B-line ordered commutators: 192/192 each;
- phase-weighted A/B commutators matching the three-W group-phase factor: 192/192 each;
- A- and B-side raw scalar seagull tensors: 96/96 each;
- scalar line/seagull group decomposition: 96/96 for each scalar-endpoint family.

This is an explicit weak-index bridge for the cross-vertex subset. It does not establish:
1. the Lorentz-weighted matter-line plus three-W cancellation;
2. the full scalar-line/seagull Lorentz/group sum;
3. the raw weak-index order for same-vertex LD-W-03/04;
4. the Feynman-gauge \(R_{\rm FG}\) completion by gauge-fixing/ghost terms;
5. external-leg/LSZ, parameter and operator counterterms;
6. an integrated UV five-point form factor or a Wilson coefficient.

The next calculation is to insert these tensors into the exact B1 momentum routes, contract each of the 16 cross-vertex graphs with \(q_\alpha\), and perform the common-\(k\) shift algebra. The matter-line commutator terms and the three-W inverse-kernel difference must be compared at the integrand level, while the scalar seagull terms retain their distinct weak tensors. Only after this closes should the two same-vertex raw chains be added and the full 24-graph sum attempted.
