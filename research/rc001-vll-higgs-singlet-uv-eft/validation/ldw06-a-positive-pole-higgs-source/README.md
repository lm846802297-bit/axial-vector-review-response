# LD-W-06: A positive scalar pole versus the external Higgs charge source

The previous [B-side charge check](../ldw06-b-positive-pole-conjugate-scalar-source/README.md) held a common loop argument without a change of variables. On the A side, the external source in its natural single-W coordinate must instead be evaluated at $\ell=k+q$ to share the internal pole factors. The sign and order below come from the actual A vertices, not from exchanging the B labels.

## Direct A pole and external routing

Take the [frozen common-$k$ S–S route](../../upstream/research/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.md). Write $\kappa=k+q$, $h=k-p_1-p_2$, $r_A^Y=k-p_2$, $r_A^W=\kappa-p_2$, $r_B^Y=\kappa+p_3$, $a=2p_2-k$, and $b=-2p_3-\kappa$. The original $H$ at the A ordinary W vertex supplies $p_2-r_A^W=a-q$. The B spectator current is $b$.

With common phase $g_2\mathcal P_4$ removed, $\mathcal P_4=-g_2^2|y_\ell|^2$, the extra scalar vertex and propagator give an overall minus in the direct A contraction. Its elementary factor is
$$
-[q\cdot(r_A^Y+r_A^W)]\,\Delta_{AY}\Delta_{AW}
=-\Delta_{AY}+\Delta_{AW}.
$$
This is the A sign in the [frozen scalar kernel](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md). In particular, “positive Y pole” names the $\Delta_{AY}$ term of the unsigned difference, not its final graph sign. Subtract the other pole contribution before comparing. With $D_A=\kappa^2(r_A^Y)^2(r_B^Y)^2$ and $\mathscr P(h)=\slashed hP_L/(h^2-M_E^2)$, the Y term is
$$
J_{AY}(k)=-W_A\,\frac{(a-q)\cdot b}{D_A}\mathscr P(h).
$$

For the [external lower box](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md), all-incoming $H(p_2)$ and W($q$) put $P_2=p_2+q$ into the H slot. With its ordinary W momentum $\ell$, the lower argument is $(p_1,P_2,p_3,p_4)$, the light momenta are $\ell-P_2,\ell+p_3$, and the heavy momentum is $p_4+\ell+p_3=\ell-p_1-P_2$. At $\ell=\kappa$, these are exactly $r_A^Y,r_B^Y,h$. The two external lower currents are $2P_2-\ell=a+q$ and $-2p_3-\ell=b$. Thus $F_2(\kappa)=(a+q)\cdot b\,\mathscr P(h)/D_A$. At unchanged $\ell=k$ the heavy momentum would instead be $h-q$, and the light/W factors would also differ. No assertion about shifting an integrated or regulated loop is used here.

## Charge order and resulting subtotal

In the [frozen raw index bridge](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md), the A internal line carries $W_A=\sum_b R_A^bR_A^aR_B^bT_0$. Applying the fundamental generator to the original exterior H slot of the weak seed $T_{AB}=-T_3/4$ gives $Z_2=R_H^aT_{AB}=\widetilde W_A$ in the opposite order. In particular, the external source does not have $W_A$. Using the [four-external source convention](../ldw06-four-external-ward-source/README.md), the bare charge piece contributes $-Z_2F_2(\kappa)$. Let $S_A=W_A+\widetilde W_A$ and $W_A-\widetilde W_A=i\mathcal G_{AB}$. The signed pair is
$$
J_{AY}(k)-Z_2F_2(\kappa)
=\frac{-S_A(a\cdot b)+i\mathcal G_{AB}(b\cdot q)}{D_A}\,\mathscr P(h).
$$
The symmetric coefficient **survives** on this side; simply copying the B-side $a\cdot b$ cancellation would be wrong. The q contact instead carries the pure commutator. This is only the one charge and one pole piece; neither A/B seagulls, external inverse terms, three-W/gauge-fixing/ghost/field contributions, nor possible common-regulator loop translations are inferred.

## Exact falsifiable checks

The checker constructs the full bare A-line contraction before splitting the two poles and separately solves the external lower box. Across three nonsingular cases it passes 4,608 entries for the two individual matrices and 2,304 factored signed comparisons, in addition to exact symbolic routing and sign identities.
- At the two generic points the symmetric part has 192 nonzero entries, the commutator part 288, and their sum 352. At $q^2=-4$ a representative entry is $-1/51876$ in the common phase normalization.
- In the control $q^2=-4$, $b\cdot q=0$ but $a\cdot b=45$; the commutator disappears and the symmetric part remains (192 entries).
- Wrong Y sign, reversed weak order, a false common loop label, or a mixed anchored denominator with the old heavy factor each changes 288 entries at every point. At the first point the correctly anchored heavy denominator is $-393$ rather than the unanchored $-405$. Copying the internal current is rejected in the generic cases; the orthogonal control intentionally cannot distinguish those two current contractions.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See [native output](native.json), [input pins](inputs.json), [task brief](../../task_briefs/20261123-ldw06-a-positive-pole-higgs-source.md), [standards provenance](../../../standards-provenance/tasks/20261123-ldw06-a-positive-pole-higgs-source.json), and [actual measured run](run_manifest.json). This is a selected pole/source interface within the [open assembly](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates), not a full Ward/LSZ/STI or a physical integrated noncancellation.
