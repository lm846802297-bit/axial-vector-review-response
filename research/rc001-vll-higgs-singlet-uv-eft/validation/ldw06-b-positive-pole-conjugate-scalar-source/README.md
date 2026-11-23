# LD-W-06: B positive scalar pole versus the external conjugate-Higgs source

This isolates **one** pair not treated by the [negative-pole fermion-source bridge](../ldw06-negative-pole-fermion-source-bridge/README.md): the B scalar line's positive $\Delta_{BY}$ pole and the charge part of the external $H^\dagger(p_3)$ Ward source. Both are compared at the **same** loop argument $k$. No loop shift, integration, other source, or external inverse term is used in this identity.

## Shared denominator, different current

In the [frozen S–S routing](../../upstream/research/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.md) use
$$
\kappa=k+q,\quad r_A^Y=k-p_2,\quad r_B^Y=k+p_3+q,\quad r_B^W=k+p_3,\quad
h=k-p_1-p_2,\quad a=2p_2-k,\quad b=-2p_3-\kappa .
$$
Normalize by the common $g_2\mathcal P_4$, with $\mathcal P_4=-g_2^2|y_\ell|^2$, and keep the right projector $\mathcal P(h)=\slashed hP_L/(h^2-M_E^2)$. The [B scalar Ward kernel](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md) has **positive** $\delta_B=\Delta_{BY}-\Delta_{BW}$ after the vertex/propagator phase is included. This sign can be read off from the direct B line factor
$$
- q\cdot(r_B^Y+r_B^W)\,\Delta_{BY}\Delta_{BW}
=\Delta_{BY}-\Delta_{BW}.
$$
Remove the negative $\Delta_{BW}$ term without translating either term. With $D_B=k^2(r_A^Y)^2(r_B^Y)^2$, the surviving B positive pole is
$$
J_{BY}=\frac{W_B\,a\cdot(b+q)\,\mathcal P(h)}{D_B}.
$$
The reason for $b+q=-2p_3-k$ is that the internal scalar–W endpoint attaches to the **original** external momentum $p_3$ on the external side of the extra W insertion.

For the external charge-source term, independently solve the four-point lower box with $(p_1,p_2,P_3,p_4)$, $P_3=p_3+q$ and $p_4=-p_1-p_2-p_3-q$. The right light momentum is $k+P_3=r_B^Y$, and the right Yukawa equation gives $h=p_4+r_B^Y=k-p_1-p_2$. The left current and light momentum remain $a,r_A^Y$. The [four-point scalar vertex](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md) at that charged argument is $-2P_3-k=b-q$, not the B internal current. Hence $F_3=a\cdot(b-q)\mathcal P(h)/D_B$.

## Exact charge identity

In the [physical weak-slot basis](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md), $R_B=R_{H^\dagger}=-t^T$. The direct B pole carries the non-tilded $W_B=\sum_b R_A^b R_B^a R_B^b T_0$. Independently acting with $R_B^a$ on the frozen $T_{AB}=-T_3/4$ gives its exact external charge tensor $Z_3=W_B$, not $\widetilde W_B$. The [four-leg source convention](../ldw06-four-external-ward-source/README.md) contributes $-Z_3F_3$ in this normalization. Thus
$$
J_{BY}-Z_3F_3
=\frac{2W_B (a\cdot q)\,\mathcal P(h)}{D_B}.
$$
The $a\cdot b$ coefficients cancel exactly; the shifted-current difference does not vanish generically. With $S_B=W_B+\widetilde W_B$ and $W_B-\widetilde W_B=i\mathcal G_{AB}$, this equals $(S_B+i\mathcal G_{AB})(a\cdot q)\mathcal P(h)/D_B$. The **separate** B seagull has a symmetric tensor $S_B$ and is not counted in this result. The $H^\dagger$ inverse-propagator piece and all other graphs are also excluded.

## Controlled exact check

The checker contracts the actual unsplit B numerator, separates its two scalar poles, and derives $F_3$ from the shifted lower-box vertices. At each of three points it passes 1,536 entries for the pole and source individually and 768 entries for their factored difference. At the two generic points $a\cdot q=-9$ and 288 residual entries are nonzero; one representative at $q^2=-4$ is $-1/288200$ in the common normalization. At the third, $q\ne0$, $q^2=-4$, $a\cdot q=0$, and $a\cdot b=13$: the individual charge and pole terms are nonzero but their difference is identically zero. Wrong charge sign, tilded weak order or substitution of the original B pole changes 288 entries even in the controlled-cancellation case. Copying the internal current into the source falsely gives zero at both generic points.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See [native values](native.json), [input pins](inputs.json), [task brief](../../task_briefs/20261123-ldw06-b-positive-pole-conjugate-scalar-source.md), [standards record](../../../standards-provenance/tasks/20261123-ldw06-b-positive-pole-conjugate-scalar-source.json), and [actual executed check](run_manifest.json). This is one fixed-route scalar charge/pole interface in the [open assembly](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates), not complete LSZ/Ward/STI closure or a physical integrated remainder.
