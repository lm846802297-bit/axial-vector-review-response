# LD-W-06: external conjugate-Higgs emission

The external field here is **$H^\dagger(p_3)$, not $H^\dagger(p_1)$**. The [frozen all-incoming ordering](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md) is $(\bar L(p_1),H(p_2),H^\dagger(p_3),L(p_4),W^a(q))$. This is the B-side reducible external scalar on the actual ordered LD-W-06 lower-point box. The [prior H(p2) result](https://github.com/lm846802297-bit/axial-vector-review-response/tree/60f2002e49028238d57453e765c63a1e3a0730bf/research/rc001-vll-higgs-singlet-uv-eft/validation/ldw06-external-higgs-leg) is context only and was not used as a numerical or derivational reference.

## Momentum and lower-point kernel

At the external gauge vertex the incoming legs are $(H^\dagger:p_3,\ W:q,\ H:-P)$, so $P=p_3+q$. The four-point arguments are $(p_1,p_2,P,p_4)$ and do sum to zero. Sewing toward the inner scalar/gauge endpoint and then toward the Yukawa endpoint gives $r_B=k+P,\ h=p_4+r_B=k-p_1-p_2,\ r_A=p_1+h=k-p_2$. This is the original internal-W loop coordinate $k$, with no dummy-variable shift. The heavy channel does not shift in that coordinate.

From the [frozen phase and four-point numerator rules](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md), the stripped shifted box is
$$
F_{06,B}(p_1,p_2,P,p_4;k)
=\frac{(2p_2-k)\cdot(-2P-k)\,\slashed h\,P_L}
{k^2\,(k-p_2)^2\,(k+P)^2\,(h^2-M_E^2)}.
$$
The actual B current is $-2p_3-k-2q$; the [internal B scalar-line graph](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md) instead has $-2p_3-k$. Comparable internal denominators do not make these currents equal.

## Weak and phase order

The bare external current from $p_H-p_{H^\dagger}$ is $-(2p_3+q)$. Sewing the conjugate slot pairs this sign with $t^T$, equivalently writing the **positive** vector $(2p_3+q)$ with $R_B=-t^T$. The minus is not counted again. If $T_{AB}=\sum_b R_A^bR_B^bT_0=-T_3/4$, the [frozen physical external-index convention](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md) gives
$$
Z_B^a=R_B^a T_{AB}=\sum_bR_A^bR_B^a R_B^b T_0.
$$
This is the **non-tilded B ordering** in that source: multiply from the outside of the B slot, not from the right of its seed generator. It differs from the order exposed by the previous A-leg appendix. Equality of the weak tensor with the internal B ordering does not identify the two graph amplitudes.

The extra scalar propagator and the external +i vertex give a relative $-g_2$, with the same $P_4=-g_2^2|y_\ell|^2$ and $P_L$ as the frozen box. In the Higgs-amputated graph the complete factor at this order is
$$
{\cal E}_{B,\mathrm{amp}}^{a,\alpha}
=-g_2P_4\,Z_B^a\frac{(2p_3+q)^\alpha}{(p_3+q)^2}\,F_{06,B},
\qquad
q_\alpha{\cal E}_{B,\mathrm{amp}}^{a,\alpha}
=-g_2P_4\,Z_B^a\left(1-\frac{p_3^2}{P^2}\right)F_{06,B}.
$$
Restoring just the original external scalar propagator $i/p_3^2$ gives $-ig_2P_4\,Z_B^a(1/p_3^2-1/P^2)F_{06,B}$ for the contracted source. The $p_3^2/P^2$ term must remain off shell, in line with the [frozen 1PI/1PR boundary](../../upstream/research/RC-001-dim6-WW-fivepoint-1PI-vs-1PR-LSZ-boundary.md). The factor tends to one only for the amputated scalar projection at $p_3^2=0$ and $P^2\ne0$. Before the loop integration the stripped $F_{06,B}$ has mass dimension $-5$; the uncontracted external emission adds dimension $-1$ and its contraction restores $-5$.

## Validation and boundaries

The [independent explicit sewing](check.py) compares bare component contractions with the shifted tensor formula. The [native record](native.json) gives all three exact rational points, including two off-shell points (one $q^2=-4$, one $q^2=0$) and an amputated $p_3^2=0$ case. The checks reproduce **9,216/9,216** uncontracted entries, **2,304/2,304** contracted entries and **1,536/1,536** entries with the external Higgs propagator restored. At the first point the right-current contraction changes from 36 (erroneously copying internal B) to 54 (correct shifted seed). The incorrect $p_3-q$ crossing, missing scalar pole term off shell, wrong transpose, reversed B order, wrong relative phase and copied internal current each fail at least one entry at every applicable point. The check isolates the transpose effect on the antisymmetric generator.

Replay with Python 3.12.14 and SymPy 1.14.0 in this folder:

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

The [task brief](../../task_briefs/20261123-ldw06-external-conjugate-higgs-leg.md) and [machine-readable standards application](../../../standards-provenance/tasks/20261123-ldw06-external-conjugate-higgs-leg.json) bind the current main lock and exact inputs; [inputs.json](inputs.json) records six frozen sources. The [RCRPS v1.0.1 run manifest](run_manifest.json) records a fresh local execution in a detached sparse checkout of exact main, with only the proposed script present as a dirty path. Its stdout is byte-identical to native.json. This is a local symbolic/rational diagnostic, not CI or a production run. It addresses one portion of [assembly gate 7](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates). It establishes neither cancellation with the internal graphs nor the complete external-leg, LSZ, Ward/STI, regulator/integrated matching or Wilson result.
