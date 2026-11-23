# LD-W-06: A seagull on the Higgs charge subtotal

Add one A contact to the [already checked A positive-pole and Higgs charge subtotal](../ldw06-a-positive-pole-higgs-source/README.md). The B contact does not fix this sign or routing. No prior pole pair was recomputed.

## From the kinetic term to the common A route

In the [frozen kinetic convention](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md), the quadratic W term of $(D_\mu H)^\dagger D^\mu H$ is $+g_2^2 W^a_\mu W^{b\mu}t^at^b$. Differentiation with respect to two labelled gauge legs yields $+ig_2^2g_{\alpha\mu}\{t^a,t^b\}$. The extra derivative supplies both orders, also when the group labels coincide. The quartic vertex **replaces** the ordinary $+ig_2$ vertex with no extra scalar propagator. The [frozen phase ratio](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md) is therefore $+g_2$ relative to $\mathcal P_4=-g_2^2|y_\ell|^2$, not the minus from successive cubic vertices with an intervening $i$ propagator.

In the [A chart of the archived S–S route](../../upstream/research/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.md), $p_2$ and $q$ enter the contact and the ordinary W leaves with $\kappa=k+q$. Conservation gives its sole A propagator $r_A=\kappa-p_2-q=k-p_2=r_A^Y$. The left Yukawa vertex gives $h=r_A-p_1$, and the right one gives $r_B=h-p_4=\kappa+p_3$, with $p_4=-p_1-p_2-p_3-q$. Thus
$$
D_A=\kappa^2(r_A^Y)^2(r_B^Y)^2,\qquad
a=2p_2-k,\quad b=-2p_3-\kappa,\quad
\mathscr P(h)=\frac{\slashed hP_L}{h^2-M_E^2}.
$$
Neither the original ordinary-W frame $k$, the pre-emission scalar $(r_A^W)^2=(\kappa-p_2)^2$, nor a separate extra A scalar propagator belongs to this contact.

In the [frozen physical weak slots](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md), the weak weight of the quartic is
$$
S_A=\sum_b\{R_A^a,R_A^b\} R_B^bT_0=\tfrac12R_B^aT_0,\qquad R_A=t,\quad R_B=-t^T.
$$
Here $S_A=W_A+\widetilde W_A$ and $W_A-\widetilde W_A=i\mathcal G_{AB}$. Crucially the remaining reduced generator is on the **B spectator**, unlike the reduced B-contact tensor.

## Only the symmetric coefficient changes

Contract the open quartic metric with $q$ and the B spectator current $b$. Removing the common $g_2\mathcal P_4$, the result is
$$
J_{A,\rm sg}=S_A(b\cdot q)\mathscr P(h)/D_A.
$$
The previously established A pole and reanchored exterior Higgs charge had coefficient $-S_A(a\cdot b)+i\mathcal G_{AB}(b\cdot q)$ in this same chart. The selected sum is consequently
$$
R_{A,{+{\rm chg}},\,{\rm sg}}
=\big[S_A(b\cdot q-a\cdot b)+i\mathcal G_{AB}(b\cdot q)\big]\mathscr P(h)/D_A .
$$
This modifies the symmetric coefficient without touching the commutator. It does not generally cancel the symmetric part. The calculation makes no additional integration-frame transformation.

## Exact checks

All nine labelled quartic pairs (36 matrix entries), 2,304 contact and 2,304 increment entries pass. At both generic points the contact has 192 nonzero entries and the updated subtotal 352. At the first, a representative normalized contact entry is $+1/415008$ while the updated subtotal there is $-7/415008$. A wrong phase, A scalar pole or extra propagator, ordinary-W argument, or spurious heavy shift changes 192 entries at each generic point; a single generator order changes 288.

At nonzero $q$ with $q^2=-4$, $b\cdot q=0$ and $a\cdot b=45$, the contracted contact vanishes but the symmetric subtotal survives in 192 entries. The open-vector contact still has 768 nonzero entries, detecting wrong phase and single-order replacements. This separates a kinematic zero from removing the vertex.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See [native output](native.json), [inputs](inputs.json), [task brief](../../task_briefs/20261123-ldw06-a-seagull-charge-subtotal.md), [standards](../../../standards-provenance/tasks/20261123-ldw06-a-seagull-charge-subtotal.json), and [measured run](run_manifest.json). This is one increment in the [open assembly](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates); the combined three-W, inverse, ghost/field, and complete regulator-defined Ward/LSZ/STI or Wilson matching are not asserted.
