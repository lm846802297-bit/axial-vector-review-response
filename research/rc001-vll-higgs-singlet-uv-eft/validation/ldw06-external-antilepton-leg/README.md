# LD-W-06: reducible W emission from the external barred lepton

This is the $\bar L(p_1)$ leg of the [ordered LD-W-06 S–S seed](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md). It is neither an internal scalar/fermion insertion nor one of the previously tested external scalars. The lower box is the actual fixed $H$–$H^\dagger$ cross-box, not a generic four-point vertex.

## Left fermion arrow and lower kernel

The all-incoming radiation vertex has $(\bar L:p_1,\, W:q,\,L:-P)$, with $P=p_1+q$. Its left open chain uses the physical numerator $+\slashed P$. In the [frozen oriented rules](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md), the left fermion-arrow convention is $-r_A$; at this vertex the fermion segment momentum incoming as $L$ is $-P$, so the physical numerator along the left chain is $-(-\slashed P)$. The gamma vertex precedes that propagator and both stand to the left of the ordered lower box. This is not a transpose of the right-fermion chain.

In the same loop coordinate $k$ the shifted four-point arguments are $(P,p_2,p_3,p_4)$ and sum to zero. The two scalar momenta are still $r_A=k-p_2$ and $r_B=k+p_3$; the heavy momentum changes to $h_A=p_4+r_B=k-P-p_2$. Neither scalar current changes. Define the stripped lower kernel
$$
F_A
=\frac{(2p_2-k)\cdot(-2p_3-k)\ \slashed h_A\,P_L}
{k^2(k-p_2)^2(k+p_3)^2(h_A^2-M_E^2)}.
$$
Then $P_RF_A=F_A$. At the first rational point the heavy denominator changes from $-398$ to $-408$; retaining the unshifted heavy factor is not valid.

## Weak basis, phase, and Ward contraction

Use the [frozen physical slot basis](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md), $T_{AB}=-T_3/4$, $t^a=\sigma^a/2$. The bare weak vertex on a fundamental arrow carries $t^a$. To compare the contracted bare indices to the archived barred-slot tensor, use the SU(2) intertwiner $J=i\sigma^2$. Express the input seed in fundamental coordinates via $J^{-1}$ on its barred slot and express the result back via $J$. The resulting matrix on that slot is $Jt^aJ^{-1}=-t^{aT}=R_{\bar L}^a$ for all three generators. Only this basis conversion accounts for the conjugate sign; it is not an extra Feynman phase. In frozen components the ordered weak tensor is $Z^a_{\bar L}=R_{\bar L}^a T_{AB}$, acting on index $i$ of $(i,j,k,l)$. The internal weak generators of this seed act on the two scalar slots, not on the barred slot.

With $S(v)=\slashed v/v^2$, $P_4=-g_2^2|y_\ell|^2$, the extra propagator $i S(P)$ and vertex $ig_2\gamma^\alpha P_L$ give the relative minus. With the original external barred leg amputated,
$$
\begin{aligned}
{\cal E}^{a,\alpha}_{\bar L,\mathrm{amp}}
&=-g_2P_4 Z^a_{\bar L}\,\gamma^\alpha P_L S(P)F_A,\\
q_\alpha{\cal E}^{a,\alpha}_{\bar L,\mathrm{amp}}
&=-g_2P_4 Z^a_{\bar L}\,[1-\slashed p_1\,S(P)]F_A .
\end{aligned}
$$
The contraction uses $\slashed q=\slashed P-\slashed p_1$ and $P_R F_A=F_A$; the inverse propagator $\slashed p_1$ stays at the far left. Restoring **only** the original barred propagator $i S(p_1)$ gives the [left connected Ward endpoint](../../upstream/research/RC-001-dim6-WW-fivepoint-1PI-vs-1PR-LSZ-boundary.md)
$$
q_\alpha{\cal E}_{\bar L,\mathrm{restored}}^{a,\alpha}
=-ig_2P_4 Z^a_{\bar L}\,[S(p_1)P_R-P_L S(P)]F_A .
$$
For an external row satisfying $\bar u_L(p_1)\slashed p_1=0$ at $p_1^2=0$ and $P^2\ne 0$, the inverse term vanishes **after** amputation and projection; it is nonzero before projection at both off-shell test points. The proof uses the existence of nonzero left-chiral external rows at the massless point, not insertion of $p_1^2=0$ into $S(p_1)$.

## Evidence and boundary

[check.py](check.py) solves the vertices, constructs the bare arrow/phase/weak tensors in components, and compares to the left Ward endpoint. Both denominator-cleared symbolic identities pass 16/16 matrix entries. Three exact rational points pass 9,216 uncontracted and 2,304 contracted amputated entries; the two off-shell points also pass 1,536 restored-propagator entries and the massless point 768 projected entries. At the first point removing the inverse term changes 288 entries; reversing the arrow, placing the box to the left, changing chirality, or incorrectly using $p_1-q$ also changes 288 entries. Incorrectly leaving the fundamental generator unconverted changes 192. The numerical [native output](native.json) is exact arithmetic, not a loop integral.

Replay from this folder: `sha256sum -c SHA256SUMS`, then `python -B check.py | cmp - native.json`. The [task brief](../../task_briefs/20261123-ldw06-external-antilepton-leg.md), [standards record](../../../standards-provenance/tasks/20261123-ldw06-external-antilepton-leg.json), [source pins](inputs.json), and [actual detached-checkout run manifest](run_manifest.json) record scope and provenance. No CI, PR, or integration decision is implied.

This is a third individual external-leg graph and only a partial contribution to [ordinary-matter gate 7](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates). The right $L$ graph, full field strength and external-leg assembly, gauge-sector terms, full Ward/LSZ/STI, the integrated UV/EFT difference and any Wilson coefficient remain outside the result.
