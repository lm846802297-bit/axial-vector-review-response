# LD-W-06: reducible W emission from the right lepton

This isolates $L(p_4)$ in the [all-incoming ordered seed](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md), $(\bar L(p_1),H(p_2),H^\dagger(p_3),L(p_4),W^a(q))$. It does not alter the three prior external-leg checks or any of the internal graphs.

## Right arrow and lower box

The additional external vertex takes $(L:p_4,W:q,\bar L:-P)$, with $P=p_4+q$. In the [frozen right-arrow convention](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md) the physical intervening fermion numerator is $+\slashed P$, not $-\slashed P$. The propagator is between the lower box and the right vertex: $F_B S(P)\gamma^\alpha P_L$, in that order.

The lower box arguments are $(p_1,p_2,p_3,P)$. At fixed internal W loop coordinate $k$, the exact vertex equations give $r_A=k-p_2$, $h=r_A-p_1=k-p_1-p_2$, and $r_B=h-P=k+p_3$. Thus shifting the right external lepton does **not** shift the heavy channel. With $S(x)=\slashed x/x^2$ the reduced ordered kernel is
$$
F_B=\frac{(2p_2-k)\cdot(-2p_3-k)\ \slashed h\,P_L}
{k^2(k-p_2)^2(k+p_3)^2(h^2-M_E^2)}.
$$
At the first diagnostic point the heavy denominator is $-398$; inserting the unrelated barred-leg shift would give $-408$.

## Weak action and chiral contraction

Use the [frozen physical external slots](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md) $(i,j,k_{\rm w},l)$, and $T_{AB}=\sum_bR_H^bR_{H^\dagger}^bT_0=-T_3/4$. The right external weak field is fundamental, $R_L^a=t^a=\sigma^a/2$. The [checker](check.py) evaluates the bare physical-slot matrix element $\langle L_l|t^a|L_n\rangle$ together with both actual scalar generators, i.e.
$$
Z_L^a{}_{i j k_{\rm w} l}
=\sum_{b,n}t^b_{ji}(-t^{bT})_{k_{\rm w}n}t^a_{ln}
=(R_L^a T_{AB})_{i j k_{\rm w} l}.
$$
The action is on slot $l$, not a third internal generator on the conjugate scalar slot. There is no conjugate weak conversion on $L$ in this physical-slot convention. Reversing the fundamental weak indices in that same convention is not an automatic consequence of the right gamma-chain order.

The additional bare $iS(P)$ followed by $ig_2\gamma^\alpha P_L$ gives a relative $-g_2$ against the frozen $P_4=-g_2^2|y_\ell|^2$. With the original right propagator amputated,
$$
\begin{aligned}
{\cal E}_{L,\mathrm{amp}}^{a,\alpha}&=-g_2P_4 Z_L^a F_B S(P)\gamma^\alpha P_L,\\
q_\alpha{\cal E}_{L,\mathrm{amp}}^{a,\alpha}
&=-g_2P_4 Z_L^a F_B[1-S(P)\slashed p_4].
\end{aligned}
$$
To see the latter identity, use $S(P)\slashed qP_L=[1-S(P)\slashed p_4]P_L$, and commute the even Dirac product $S(P)\slashed p_4$ through $P_L$ before using $F_BP_L=F_B$. The inverse-propagator factor remains at the **right** end. If only the original right propagator $iS(p_4)$ is restored, the contraction is
$$
q_\alpha{\cal E}_{L,\mathrm{restored}}^{a,\alpha}
=-ig_2P_4 Z_L^a F_B[P_L S(p_4)-S(P)P_R] .
$$
This is the right-chain order of the [frozen elementary chiral endpoint](../../upstream/research/RC-001-dim6-WW-fivepoint-1PI-vs-1PR-LSZ-boundary.md) as applied to this actual box. With $p_4^2=0$ and $P^2\ne0$, it is the **amputated** expression that can then act on a right chiral column satisfying $\slashed p_4u_L(p_4)=0$; only then may the inverse-propagator term be dropped. The test explicitly uses nonzero columns with a nonzero lower-box action.

## Exact checks

The [native output](native.json) contains two off-shell points and one massless original-leg point, with 9,216 uncontracted, 2,304 contracted, 1,536 original-propagator-restored, and 768 projected matrix entries agreeing exactly. Both denominator-cleared chiral identities pass 16/16 symbolic entries. Wrong crossing, arrow, extra heavy shift, chirality, or relative phase changes 288 entries at each off-shell point. Transposing the weak matrix in the same slot basis changes 96; instead acting on the conjugate Higgs changes 192. Dropping the right inverse term changes 288 entries at each off-shell point, and zero only after the massless-column projection.

Replay from this directory:

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

The [task brief](../../task_briefs/20261123-ldw06-external-lepton-leg.md), [standards provenance](../../../standards-provenance/tasks/20261123-ldw06-external-lepton-leg.json), [frozen inputs](inputs.json), and [measured local execution](run_manifest.json) are pinned. This is only the single bare reducible right $L$ graph in [gate 7](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates). No four-leg sum, field renormalization, complete LSZ/Ward/STI, loop integration or Wilson matching is implied.
