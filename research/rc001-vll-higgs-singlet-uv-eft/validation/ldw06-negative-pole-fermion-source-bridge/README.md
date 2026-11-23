# LD-W-06: negative scalar poles and their fermion source interface

The [secondary-shift audit](../../upstream/research/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.md) fixes both momentum maps. The [previous ordered appendix](https://github.com/lm846802297-bit/axial-vector-review-response/tree/a8a43434ec7bf48371033f5e371baa0af41cd133/research/rc001-vll-higgs-singlet-uv-eft/validation/ldw06-ordered-kernel) assembled the A translation. Here the B translation is assembled with its signed weak tensor, the two representations are related without conflating their loop arguments, and the pair is joined to just the two **fermion charge-source** terms from the [external Ward source](../ldw06-four-external-ward-source/README.md). The scalar-source and external inverse terms are not included in that subtotal.

## B translation and distinct anchors

All expressions have the archived overall phase $g_2\mathcal P_4$ removed. Use $\kappa=k+q$, $h=k-p_1-p_2$, $a=2p_2-k$, $b=-2p_3-\kappa$. From the [frozen scalar Ward kernels](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md), the negative-propagator pieces are $+C_A W_A \mathcal P(h)$ and $-C_B W_B\mathcal P(h)$, where
$$
\begin{aligned}
C_A(k)&=\frac{(a-q)\cdot b}{\kappa^2(r_A^W)^2(r_B^Y)^2},&
C_B(k)&=\frac{a\cdot(b+q)}{k^2(r_A^Y)^2(r_B^W)^2},&
\mathcal P(h)&=\frac{\slashed h P_L}{h^2-M_E^2}.
\end{aligned}
$$
The distinct weak orders are $W_A=\sum_bR_A^bR_A^aR_B^bT_0$ and $W_B=\sum_bR_A^bR_B^aR_B^bT_0$. Tildes reverse the two generators on the emitting slot. They satisfy $W_A-\widetilde W_A=W_B-\widetilde W_B=i\mathcal G_{AB}$ with the [frozen physical weak slots](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md).

The B translation means $k_{\rm old}=k_{\rm new}+q$. It maps all three light/W momenta and both scalar currents in $C_B(k+q)$ to those in $C_A(k)$, while $\mathcal P(h)\mapsto\mathcal P(h+q)$. The A-anchored pair (B alone translated) and B-anchored pair (A alone translated) are
$$
\begin{aligned}
J_A(k)&=C_A(k)\,[W_A\mathcal P(h)-W_B\mathcal P(h+q)],\\
J_B(k)&=C_B(k)\,[W_A\mathcal P(h-q)-W_B\mathcal P(h)].
\end{aligned}
$$
In particular $J_A(k-q)=J_B(k)$ by exact substitution. The same-argument $J_A(k)=J_B(k)$ is **not** true generically. This is a distinction between routing representations, not an assertion about permitted translations of a regulated loop integral.

The commutator part of $J_A$ equals $-i\mathcal G_{AB} C_A[\mathcal P(h+q)-\mathcal P(h)]/2$. It therefore isolates precisely a finite heavy difference; with $H=h^2-M_E^2$ and $H_+=(h+q)^2-M_E^2$,
$$
\mathcal P(h+q)-\mathcal P(h)
=\frac{H\slashed q-(2h\cdot q+q^2)\slashed h}{H H_+}P_L .
$$
The complementary symmetric part is $C_A[(W_A+\widetilde W_A)\mathcal P(h)-(W_B+\widetilde W_B)\mathcal P(h+q)]/2$.

## Interface to the actual fermion charge-source terms

In the single-W fixed-$k$ convention of the four external legs, solve the lower vertices after shifting only $\bar L(p_1)$ or $L(p_4)$. Neither change affects either scalar current or scalar propagator. Their shifted boxes are exactly $F_1=C_B\mathcal P(h-q)$ and $F_4=C_B\mathcal P(h)$, not proportional approximations. Therefore $J_B=W_A F_1-W_B F_4$.

The local Yukawa singlet acts on the **seed** $T_0$. Commuting the original $\bar L$ or $L$ slot past the two internal scalar generators **before** using the singlet relation gives
$$
Z_1=R_{\bar L}^a T_{AB}=-W_A,\qquad Z_4=R_L^a T_{AB}=-\widetilde W_B,\qquad
T_{AB}=\sum_b R_A^bR_B^bT_0.
$$
The resulting B-side weak order is tilded. Replacing it by $-W_B$ would suppress an exact commutator term from the subtotal. With the relative signs fixed by the frozen kernels, adding **only** the two external fermionic charge-source pieces yields
$$
J_B-Z_1F_1-Z_4F_4=2W_A F_1-i\mathcal G_{AB}F_4 .
$$
This is not zero at the tested points. It identifies a defined internal–external **charge subtotal** in the stated B-anchor. It is not the partial matrix with all four external terms and all five known internal graphs reported previously, and is not physical noncancellation. The other scalar-pole pieces, scalar charge and inverse terms, regular seagulls and three-W, Yukawa/field/ghost completion, allowed regulator shifts, and integrated matching are not settled by this calculation.

## Exact checks and provenance

The checker verifies both five-vector maps plus the two heavy maps, 16 denominator-cleared heavy-difference entries, and 1,536 entries each for the signed B translation, paired routing identity, commutator isolation, and fermion-source interface. At the first nonsingular point $q^2=-4$, $(H_-,H,H_+)=(-405,-393,-389)$; the charge subtotal has 336 nonzero entries (first: $-3/273790$). At the second point $q$ is nonzero lightlike and $(H_-,H,H_+)=(-389,-377,-365)$; the subtotal has 352 nonzero entries. The same-$k$ anchor difference has 352 at both points; dropping the heavy shift or replacing $W_B$ by $\widetilde W_B$ changes 288 at both.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See [native output](native.json), [input pins](inputs.json), [task brief](../../task_briefs/20261123-ldw06-negative-pole-fermion-source-bridge.md), [standards record](../../../standards-provenance/tasks/20261123-ldw06-negative-pole-fermion-source-bridge.json), and [actual local execution](run_manifest.json). This advances [assembly gates 5–7](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md#6-remaining-assembly-gates) for this selected subtotal only. No full Ward/LSZ/STI or Wilson coefficient is inferred.
