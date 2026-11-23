# LD-W-06 scalar-line, seagull, and three-W subset

This implements part of gates 3 and 5 in the [frozen common-$k$ assembly ledger](https://github.com/lm846802297-bit/axial-vector-review-response/blob/89cd043984012215f74ae331049a626badea9d57/research/rc001-vll-higgs-singlet-uv-eft/upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md). It assembles the two scalar lines, two seagulls and contracted three-W graph into a single weak/Dirac matrix in the archived relative convention. The new step is to combine the two negative scalar WTI endpoint pieces after translating **only** the A piece, exposing the precise heavy-line difference that a later Yukawa/LSZ completion would have to address. No original archive file, previous IndexError replay, or physical claim is changed.

## Exact group and routing conventions

Use $q$ incoming and $\kappa=k+q$. Label $u=k^2,\ v=\kappa^2,\ A=(r_A^Y)^2,\ A_W=(r_A^W)^2,\ B=(r_B^Y)^2,\ B_W=(r_B^W)^2$, and let $P(h)=\slashed h/(h^2-M_E^2)$, $h=k-p_1-p_2$. The actual three-W current vectors are $a=2p_2-k$, $b=-2p_3-\kappa$, and the scalar-line currents are $a-q$, $b+q$. All dots use $+---$. We retain the frozen $A\to B$ three-W factor $-ig_2\mathcal G_{AB}$. Below a shared $g_2$ and common external factors/projectors are suppressed; no relative phase is stripped.

The raw ordered weak tensors are $W_A=(\mathcal S_A+i\mathcal G_{AB})/2$ and $W_B=(\mathcal S_B+i\mathcal G_{AB})/2$. The direct route independently constructs them by Kronecker products on the four weak-index slots (with $-t^T$ for the conjugate field) rather than inserting these decompositions. The actual two seagulls use separate $\mathcal S_A,\mathcal S_B$.

## Unshifted and A-translated assembly

In the unshifted representation the raw scalar WTI signs give $-(\Delta_{AY}-\Delta_{AW})W_A$ and $+(\Delta_{BY}-\Delta_{BW})W_B$ multiplying their respective actual current contractions. Denote
$$
L_A=(a-q)\cdot b,\qquad L_B=a\cdot(b+q),\qquad
R=\frac{(a\cdot k)(b\cdot k)-(a\cdot\kappa)(b\cdot\kappa)}{uv}.
$$
The two **Y-pole** terms, both seagulls, and the full contracted three-W term combine to $X_0 P(h)$, where
$$
\begin{aligned}
X_0={}&
  \frac{-a\cdot b+3b\cdot q}{2vAB}\,\mathcal S_A
 +\frac{ a\cdot b+3a\cdot q}{2uAB}\,\mathcal S_B\\
&+\frac{i\mathcal G_{AB}}{AB}
 \left[
 -\frac12(a\cdot b)\Big(\frac1u-\frac1v\Big)
 +\frac12\Big(\frac{b\cdot q}{v}+\frac{a\cdot q}{u}\Big)-R
 \right].
\end{aligned}
$$
Here the $\mathcal S_{A,B}$ coefficients receive their own seagulls as well as the line-contact piece; specifically the seagull contributes $+b\cdot q/(vAB)$ and $+a\cdot q/(uAB)$. The $i\mathcal G$ contacts do not come from a seagull. The full unshifted subset is
$$
X_0 P(h)+\frac{L_A}{vA_WB}W_A P(h)-\frac{L_B}{uAB_W}W_B P(h).
$$
These identities use the raw contracted Yang–Mills numerator $(\kappa^2-k^2)(a\cdot b)+(a\cdot k)(b\cdot k)-(a\cdot\kappa)(b\cdot\kappa)$; the code obtains it by direct index contraction of the all-incoming $(q,k,-\kappa)$ vertex, not by assuming the displayed split.

Now only in the positive $W_A$ term change the dummy integration variable $k_{\rm new}=k_{\rm old}+q$, i.e. evaluate its old expression at $k-q$ after relabeling. Its other factors become $L_B/(uAB_W)$; its heavy argument becomes $h-q$, **not** $h$. With $H=h^2-M_E^2$, $H_-=(h-q)^2-M_E^2$, the exact finite difference is
$$
\delta P=P(h-q)-P(h)
  =\frac{(2h\cdot q-q^2)\slashed h-H\slashed q}{H_- H}.
$$
Thus in the translated representation the two $W$-pole terms together are
$$
\frac{L_B}{2uAB_W}
 \big[(\mathcal S_A-\mathcal S_B)P(h)
      +(\mathcal S_A+i\mathcal G_{AB})\delta P\big].
$$
The shared commutator multiplies the finite difference, but $\mathcal S_A-\mathcal S_B$ is independently retained. Neither two negative terms nor full subset integrands are compared pointwise at the same old/new $k$; explicitly translating A is essential. No integral-shift or regulator claim is made.

## Verification and boundary

Two exact rational points from the frozen ledger (including a generic off-shell $q^2=-4$) pass **1,536/1,536** raw-versus-factored Dirac/weak entry comparisons before translation and **1,536/1,536** after explicit translation of the A piece only. The denominator-cleared heavy finite difference passes 16/16 symbolic matrix entries. Flipping the commutator current-contact sign, dropping $R_{\rm FG}$, or using the unshifted heavy factor each changes 216 entries at the off-shell point. This validates a selected graph subset, not integrand-level closure of the entire LD-W-06 WTI, the complete ordinary-matter six-pair sum, reducible external-leg LSZ, BRST/ghost terms, a full STI or any Wilson coefficient. The next useful input is an explicit complete ordered Yukawa/external-leg numerator and denominators in the same normalization and same shifted routing, rather than a further zero test of the subset.

Run in this folder: `sha256sum -c SHA256SUMS`, then `python -B check.py > /tmp/ldw06-kernel-replay.json` and compare against `native.json`. Exact source fingerprints, diagnostic output, and task brief are included. No CI was run.
