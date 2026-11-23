# LD-W-06: add the B seagull to the B charge subtotal

Take the [established B positive-pole plus external H† charge subtotal](../ldw06-b-positive-pole-conjugate-scalar-source/README.md) as the starting relation. This check adds **only** the B seagull, at the same archived common-$k$ argument. It does not recompute either previous positive-pole pair.

## Derive the quartic vertex and its route

In the [archived scalar kinetic convention](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md), $D_\mu=\partial_\mu-i g_2 R W_\mu$, and the quadratic-in-$W$ term of $(D_\mu H)^\dagger D^\mu H$ carries $+g_2^2 W^a_\mu W^{b\mu}R^aR^b$. Differentiating with respect to the two labelled W legs gives **both** orders in the vertex:
$$
V^{\alpha\mu,ab}_B=+i g_2^2g^{\alpha\mu}\{R_B^a,R_B^b\},\qquad
R_B=-t^T,\quad t=\sigma/2.
$$
There is no divided-out factor of two when $a=b$; the two derivatives are on independently labelled legs. Replacing the ordinary $+ig_2$ vertex by the quartic one gives $+g_2$ relative to the four-point phase $\mathcal P_4=-g_2^2|y_\ell|^2$. It does **not** give the minus from an extra vertex *and* extra scalar propagator in an ordinary-line diagram. This is the phase comparison in the [oriented vertex ledger](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md).

At the B contact the original incoming Higgs momentum $p_3$ and both gauge momenta $k,q$ enter the same vertex, so the only B propagator has $r_B^Y=k+p_3+q$. There is no separate segment with $r_B^W=k+p_3$. With $p_4=-p_1-p_2-p_3-q$, the right Yukawa equation gives $h=p_4+r_B^Y=k-p_1-p_2$ and the left scalar line has $r_A^Y=p_1+h=k-p_2$. These reproduce the [archived B seagull route](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md). Define
$$
D_B=k^2(r_A^Y)^2(r_B^Y)^2,\qquad
a=2p_2-k,\qquad
\mathscr P(h)=\frac{\slashed hP_L}{h^2-M_E^2}.
$$
The internal W carries $k$, not $\kappa=k+q$; the latter appears only inside $r_B^Y$ here.

The normalized weak factor follows directly by differentiation in the physical-index basis:
$$
S_B=\sum_bR_A^b\{R_B^a,R_B^b\}T_0=\tfrac12 R_A^a T_0,\qquad R_A=t .
$$
The code differentiates all 9 pairs of labelled generators (36 matrix entries), and checks both $S_B=W_B+\widetilde W_B$ and $W_B-\widetilde W_B=i\mathcal G_{AB}$ in the [frozen weak order](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md). The anti-doublet minus occurs twice in the anticommutator, not as an extra phase.

## Which part changes?

Removing the common $g_2\mathcal P_4$, contraction at the contact gives $a^\mu q^\alpha g_{\alpha\mu}=a\cdot q$. Thus the increment is
$$
J_{B,\rm sg}=S_B\,(a\cdot q)\frac{\mathscr P(h)}{D_B}.
$$
The known pole/charge relation was $2W_B(a\cdot q)\mathscr P(h)/D_B=(S_B+i\mathcal G_{AB})(a\cdot q)\mathscr P(h)/D_B$. Adding the contact at the identical loop argument gives
$$
R_{B,+{\rm chg},\,{\rm sg}}
=(2S_B+i\mathcal G_{AB})(a\cdot q)\frac{\mathscr P(h)}{D_B}.
$$
The symmetric coefficient doubles, while the commutator coefficient is unchanged. Neither reintroduces an $a\cdot b$ term. This selected subtotal is generically nonzero. Its properties do not imply the behavior of the other seagull, three-W graphs, inverse external terms, or any full regulated Ward sum.

## Exact checks and boundaries

At all three nonsingular points the checker passes 2,304 total contact entries and 2,304 total increment entries. At the two generic points $a\cdot q=-9$, each contact has 192 nonzero entries and each updated subtotal has 352. In the first trace, a contact entry is $+1/288200$ at generator 0, weak indices (0,1,0,0) and Dirac indices (0,0), zero based, with common phase removed. Wrong phase, old/extra B pole or wrong internal W virtuality are each detected in 192 entries at both points; retaining only one quartic weak order is detected in 288.

The third point has $q^2=-4$ and $a\cdot q=0$. The selected longitudinal subtotal vanishes, but the uncontracted contact has 768 nonzero entries; its independent wrong-phase and single-order controls still fail. Thus the longitudinal zero does not mean the seagull itself is absent.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See [native data](native.json), [input pins](inputs.json), [task brief](../../task_briefs/20261123-ldw06-b-seagull-charge-subtotal.md), [standards record](../../../standards-provenance/tasks/20261123-ldw06-b-seagull-charge-subtotal.json), and [measured local run](run_manifest.json). This is a bare one-contact increment within the [open assembly](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates), not an integrated nonzero claim, complete Ward/LSZ/STI result, or Wilson match.
