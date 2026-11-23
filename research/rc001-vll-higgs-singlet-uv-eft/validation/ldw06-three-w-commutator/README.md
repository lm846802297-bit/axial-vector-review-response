# LD-W-06: when the three-W graph absorbs a selected commutator

Take only the commutator projections of the already checked [A](../ldw06-a-seagull-charge-subtotal/README.md) and [B](../ldw06-b-seagull-charge-subtotal/README.md) positive-pole, external-charge and seagull subtotals. The symmetric weak tensors are outside this calculation. The new comparison is to the actual internal three-W graph, not its metric propagator difference alone.

## Fixed routing and sign

In the [frozen S–S map](../../upstream/research/RC-001-dim6-WW-fivepoint-LD-W-06-common-k-SS-two-endpoint-bridge.md), let $\kappa=k+q$, $a=2p_2-k$, $b=-2p_3-\kappa$, $r_A=k-p_2$, $r_B=\kappa+p_3$, $h=k-p_1-p_2=r_B+p_4$. The two existing projected commutators have denominators $D_{3W}/k^2$ and $D_{3W}/\kappa^2$, respectively, where
$$
D_{3W}=k^2\kappa^2 r_A^2r_B^2(h^2-M_E^2).
$$
All three graphs sit at the same $k$ and carry the same heavy numerator; no integration variable is changed.

The [frozen field-strength and Fourier conventions](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md) give $-g_2 f^{abc}(\partial_\mu W^a_\nu)W^{b\mu}W^{c\nu}$ in the cubic action. The checker assigns the three labelled legs in all six orders before contracting with $(q,a,b)$ at incoming momenta $(q,k,-\kappa)$. This yields
$$
Y=(\kappa^2-k^2)(a\cdot b)-(a\cdot k)(b\cdot q)-(b\cdot\kappa)(a\cdot q).
$$
An extra W propagator contributes $-i$ relative to the seed. Direct fundamental/conjugate matrix multiplication with the [frozen opposite A/B orderings](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md) gives $W_A-\widetilde W_A=W_B-\widetilde W_B=i\mathcal G_{AB}$. Thus after taking out $g_2P_4,i\mathcal G_{AB}\slashed hP_L/D_{3W}$, the three-W numerator is $-Y$, and the selected sum is
$$
\begin{aligned}
N&=k^2(b\cdot q)+\kappa^2(a\cdot q)-Y\\
 &=2(p_2\cdot k)(b\cdot q)-2(p_3\cdot\kappa)(a\cdot q)
      -(\kappa^2-k^2)(a\cdot b).
\end{aligned}
$$
The last term is kept at general kinematics. The first two terms expose exactly the coefficients left after combining each endpoint commutator with the corresponding longitudinal piece of the sewn vertex. There is no general same-route cancellation of this projected sum.

## Controls: exact absorption and failure one parameter away

Take spacelike $q$ with $q^2=-4$ and $k^2=\kappa^2=14$. This removes the metric piece without setting the three-W contraction to zero. For the A comparison set $a\cdot q=0$ and keep $b\cdot q=10$: the B commutator is then absent, and A cancels against the full three-W numerator precisely at $p_2\cdot k=0$. Vary only a transverse component of $p_2$ while keeping these projections fixed; $p_2\cdot k=1$ leaves a nonzero numerator. For B, set $b\cdot q=0$, $a\cdot q=-10$ and vary $p_3\cdot\kappa$ in the same way, with independent momenta.

| Control | A numerator | B numerator | Three-W numerator | Sum |
| --- | ---: | ---: | ---: | ---: |
| A, orthogonal | 140 | 0 | −140 | 0 |
| A, detuned | 140 | 0 | −120 | 20 |
| B, orthogonal | 0 | −140 | 140 | 0 |
| B, detuned | 0 | −140 | 160 | 20 |
| Unequal W virtualities | 180 | 22 | −90 | 112 |

All propagator factors and external virtualities are nonzero. The four equal-virtuality controls reject a flipped three-W phase and replacing the three-W chain by its metric part. The unequal-virtuality control detects swapped single-W weighting. The replay checks four symbolic identities and 96 raw weak entries; no loop shifts, external on-shell limit, negative scalar poles, inverse external terms, ghost/gauge-fixing completion, full Ward/LSZ/STI, integral, or Wilson coefficient are tested. The zeros are kinematic controls, not a generic symmetry or a statement about other projections.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See the [exact output](native.json), [pinned inputs](inputs.json), [task brief](../../task_briefs/20261123-ldw06-three-w-commutator.md), [standards record](../../../standards-provenance/tasks/20261123-ldw06-three-w-commutator.json), and [run manifest](run_manifest.json).
