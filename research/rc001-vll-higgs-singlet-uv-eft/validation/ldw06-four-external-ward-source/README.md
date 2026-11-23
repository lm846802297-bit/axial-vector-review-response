# LD-W-06: four external emissions and the shifted Ward source

This combines four original external emissions on one ordered LD-W-06 S–S lower box. The direct bare contraction is compared with an independently constructed four-point source variation and its external inverse-propagator terms. No field, ghost, gauge-fixing, or counterterm completion is assumed.

## One lower-box convention

Use the [frozen all-incoming order](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md) $(\bar L(p_1),H(p_2),H^\dagger(p_3),L(p_4),W^a(q))$. Put $P_j=p_j+q$ in the emitting slot of the lower four-point box. Keep the same single internal W loop momentum $k$ in every external term. For $h=k-p_1-p_2$, $A=2p_2-k$, and $B=-2p_3-k$:

| Emitting leg | Left scalar current and momentum | Right scalar current and momentum | Heavy momentum |
|---|---|---|---|
| $\bar L(p_1)$ | $A,\ k-p_2$ | $B,\ k+p_3$ | $h-q$ |
| $H(p_2)$ | $A+2q,\ k-p_2-q$ | $B,\ k+p_3$ | $h-q$ |
| $H^\dagger(p_3)$ | $A,\ k-p_2$ | $B-2q,\ k+p_3+q$ | $h$ |
| $L(p_4)$ | $A,\ k-p_2$ | $B,\ k+p_3$ | $h$ |

For each row $F_j$ is the [ordered stripped box](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md), the scalar current dot product times $\slashed h_jP_L$ over the two listed scalar virtualities, $k^2$, and $h_j^2-M_E^2$. The two fermion arrows use $+\slashed P_j$ on opposite sides of $F_j$. Each physical-slot scalar current is $p_j+P_j$; the conjugate sign is already in its weak generator. The extra vertex and intermediate propagator give a factor $-g_2$ relative to the four-point phase $\mathcal P_4=-g_2^2|y_\ell|^2$ in all four diagrams.

## Bare sum and independent source variation

In the [physical weak basis](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md) the slot generators are $R_j=(-t^T,t,-t^T,t)$ and $T_{AB}=\sum_bR_H^bR_{H^\dagger}^bT_0=-T_3/4$. Write $Z_j^a=R_j^aT_{AB}$. The direct calculation sews physical weak indices and contracts the four explicit bare radiation vertices.

Independently vary the lower four-point source with a local weak rotation proportional to $e^{-iqx}$ on each field in turn. The Fourier insertion shifts only that field's argument to $p_j+q$. The coefficient of the common infinitesimal parameter is
$$
\mathcal W^a=\sum_{j=1}^4 Z_j^aF_j=\sum_{j=1}^4 Z_j^a(F_j-F_4).
$$
The second equality follows from $\sum_jR_j^aT_{AB}=0$, checked against the independent Fierz form for all 48 weak components. It is not an assertion that each left or right pair separately annihilates the dressed box.

Apply the [frozen chiral endpoint identities](../../upstream/research/RC-001-dim6-WW-fivepoint-1PI-vs-1PR-LSZ-boundary.md). With $S(v)=\slashed v/v^2$, the result after amputation of all four original legs is
$$
\begin{aligned}
\mathcal I^a &= Z_1^a\,\slashed p_1 S(P_1)F_1
+Z_2^a\,\frac{p_2^2}{P_2^2}F_2
+Z_3^a\,\frac{p_3^2}{P_3^2}F_3
+Z_4^a\,F_4 S(P_4)\slashed p_4, \\
q_\alpha\mathcal E_{\rm ext,amp}^{a,\alpha}
&=-g_2\mathcal P_4(\mathcal W^a-\mathcal I^a).
\end{aligned}
$$
The fermion inverse terms occupy opposite ends of their Dirac chains. Restoring all original propagators multiplies this composite endpoint by $iS(p_1)$ on the left, $iS(p_4)$ on the right, and $(i/p_2^2)(i/p_3^2)$. This matches four explicit connected diagrams with original propagators restored at their proper positions.

At generic nonzero $q$, projecting the amputated original fermions onto nonzero massless rows and columns and putting both original scalars on shell removes $\mathcal I^a$ but not $\mathcal W^a$. At the separate $q=0$ test all original virtualities are instead nonzero and both the source and the contraction are zero. These two operations are not interchanged.

## Known-subset comparison

At the two nonzero-$q$ off-shell points alone, add just the [two scalar lines and two seagulls](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md) and the contracted three-W graph of the [previous ordered subset](https://github.com/lm846802297-bit/axial-vector-review-response/tree/a8a43434ec7bf48371033f5e371baa0af41cd133/research/rc001-vll-higgs-singlet-uv-eft/validation/ldw06-ordered-kernel). Use normalization $g_2\mathcal P_4$ for both internal and external pieces, as well as the same final $P_L$. This fixes the archived common-$k$ representation before any further secondary shift, with $\kappa=k+q$ on the second half of the three-W graph. **352 entries of the partial sum remain nonzero at each point.** The [native output](native.json) gives an exact representative entry. This does not establish any nonzero physical or integrated remainder. Different loop representations need not agree pointwise, and the full internal/ghost/field sector is not included.

## Validation and replay

[check.py](check.py) passes 3,072 amputated entries over four points, 2,304 connected entries at the three nonsingular off-shell points including $q=0$, and 768 projected entries at the separate massless point. Reversing fermion order, removing the heavy shift or omitting a leg are detected at generic $q$. Dropping the inverse terms changes 352 entries at each nonzero-$q$ off-shell point and none after massless projection.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See [task brief](../../task_briefs/20261123-ldw06-four-external-ward-source.md), [standards application](../../../standards-provenance/tasks/20261123-ldw06-four-external-ward-source.json), [source pins](inputs.json), and [measured run](run_manifest.json). This addresses the bare external assembly step of [gate 7](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates). No full Ward/LSZ/STI, integrated subtraction or Wilson coefficient is claimed.
