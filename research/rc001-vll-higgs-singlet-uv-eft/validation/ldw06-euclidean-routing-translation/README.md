# LD-W-06: no UV surface term for the selected Euclidean loop translations

The [negative-pole interface](../ldw06-negative-pole-fermion-source-bridge/README.md) mapped the integrands but left regulated loop translations open. For the exact full-theory LD-W-06 boxes specified below, each term is absolutely integrable at the [archived nonexceptional Euclidean point](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md#7-nonexceptional-five-point-kinematics). A finite change of loop origin consequently gives the same integral. More specifically, a translated radius-$R$ cutoff ball produces a boundary difference of order $R^{-2}$, so it leaves no UV surface term when the cutoff is removed.

## Terms and allowable translations

Use the [archived negative-pole route](../../upstream/research/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.md) and the [four external source routes](../ldw06-four-external-ward-source/README.md). In this note all scalar products and squares are positive-signature Euclidean; $p_1,p_2,p_3,q=\mu(e_1,e_2,e_3,e_4)$, $p_4=-p_1-p_2-p_3-q$, and $M_E^2>0$. The continuation convention is the standard Minkowski $+i0$ prescription; the claim here is about their Euclidean representatives with massless factors $\ell_E^2$ and a heavy factor $h_E^2+M_E^2$. Common Wick phases are suppressed and no direct real-Minkowski change of contour is inferred.

Set $h=k-p_1-p_2$, $\kappa=k+q$, $A=2p_2-k$, $B=-2p_3-k$ and $P(H)=\slashed H P_L/(H^2+M_E^2)$. Every row gives the same function template
$$
F(k)=
\frac{(u\cdot v)P(H)}
     {\ell_W^2\ell_A^2\ell_B^2}.
$$

| Term | $\ell_W$ | $\ell_A$ | $\ell_B$ | $u$ | $v$ | $H$ |
| --- | --- | --- | --- | --- | --- | --- |
| A negative pole | $\kappa$ | $\kappa-p_2$ | $\kappa+p_3$ | $A-q$ | $B-q$ | $h$ |
| B negative pole | $k$ | $k-p_2$ | $k+p_3$ | $A$ | $B$ | $h$ |
| $F_1$ (external barred lepton) | $k$ | $k-p_2$ | $k+p_3$ | $A$ | $B$ | $h-q$ |
| $F_2$ (external Higgs) | $k$ | $k-p_2-q$ | $k+p_3$ | $A+2q$ | $B$ | $h-q$ |
| $F_3$ (external conjugate Higgs) | $k$ | $k-p_2$ | $k+p_3+q$ | $A$ | $B-2q$ | $h$ |
| $F_4$ (external lepton) | $k$ | $k-p_2$ | $k+p_3$ | $A$ | $B$ | $h$ |

The table strips the known ordered weak and other common phases: the A negative pole carries $+W_A$ and B $-W_B$ in the normalization of the previous negative-pole audit. Translating the *entire* A kernel by $k_{\rm old}=k_{\rm new}-q$ gives the $F_1$ routed scalar and Dirac factors. Translating the entire B kernel by $k_{\rm old}=k_{\rm new}+q$ gives $F_4(k_{\rm new}+q)$, with heavy argument $h+q$ at $k_{\rm new}$. These do not identify the heavy line with its unshifted argument at the same loop point. In particular a change of heavy argument **at fixed light route** is a different integrand operation, not a translation.

## Absolute bounds and their domain

For fixed external data and positive $M_E^2$, choose $R_0$ so that beyond it every shifted Euclidean line momentum obeys $|k+c|\ge|k|/2$. The two linear currents and chiral linear numerator then give $\|N\|\le C|k|^3$. Four full quadratic denominators have absolute product bounded below by $c|k|^8$. Therefore
$$
\|F(k)\|\le C'|k|^{-5},\qquad
\int_{|k|>R}\|F(k)\|\,d^4k=O(R^{-1}).
$$
For a fixed shift $s$, the symmetric difference of the two cutoff balls is contained in $R-|s|\le |k|\le R+|s|$. Its volume is $O(R^3)$ and the integrand is uniformly $O(R^{-5})$ there, giving the stated $O(R^{-2})$ bound without relying on angular or Dirac cancellations.

In the interior, the three light pole centers in each row are translates of $(0,p_2,-p_3)$, $(0,p_2+q,-p_3)$ or $(0,p_2,-p_3-q)$. At the archived orthogonal point they are always distinct, so near each center the only possible singularity is bounded by $C/|k-k_*|^2$, integrable in four dimensions. This also holds for generic Euclidean points keeping those centers distinct; the heavy denominator is bounded below by $M_E^2$. Setting $p_2=0$ in the nonshifted light chart makes the W and A centers coincide: the simple-pole proof then no longer applies. That control does not assert divergence, which would require checking the numerator. Where external inverse terms merely multiply these boxes by bounded matrices depending on the fixed external momenta, they do not change the loop degree; they are not set to zero here.

For the fixed-light-route change, write $H_0=h^2+M_E^2$ and $\delta_\pm=\pm2h\cdot q+q^2$. Its separately improved bound is explicit:
$$
P(h\pm q)-P(h)
=\frac{H_0(\pm\slashed q)-\delta_\pm\slashed h}
       {H_0(H_0+\delta_\pm)}P_L
=O(|k|^{-2}).
$$
Multiplying by the fixed light factor gives $O(|k|^{-6})$. Likewise $F_j-F_4=O(|k|^{-6})$, since the degree-3 numerator and degree-8 denominator leading forms are the same for every $F_j$ (the common-denominator numerator difference has degree at most 10, over degree 16). Neither improvement is required to shift the individual terms.

## Exact checks and boundary

The checker independently solves the two lower-point vertex routings, then checks 64 components of translated line/current/denominator/numerator identities. It checks the heavy difference symbolically and all eight routed rows along three exact rational large-$R$ rays, with and without projection on $q$; each has the same nonzero chiral $R^{-5}$ leading matrix per ray. Along each ray the anchored heavy difference has a nonzero $R^{-6}$ coefficient, and all three $F_j-F_4$ are bounded by that order. It also checks the Euclidean Clifford algebra, distinct centers and the exceptional collision. The symbolic uniform estimate, not the three rays, proves translation legitimacy. No numerical loop integration was run.

This does not show that separate hard or soft terms from a mass expansion may be shifted or that their UV/IR poles cancel. The archived [LD-W-03/04 light triangles](../../upstream/research/RC-001-dim6-WW-same-vertex-soft-matching.md#3-uv-numerator-and-the-common-light-loop-pole) have a $k$-independent heavy channel and leading $|k|^{-4}$, so the same absolute $L^1$ proof does not cover them; this does not rule out their consistent treatment in a specified translation-invariant regulator. This note is not a statement about exceptional or on-shell IR limits, Minkowski threshold continuation, the missing BRST source, the complete Ward/LSZ/STI, UV–EFT subtraction, or a Wilson coefficient.

    sha256sum -c SHA256SUMS
    python -B check.py | cmp - native.json

See the [native checks](native.json), [exact inputs](inputs.json), [task brief](../../task_briefs/20261123-ldw06-euclidean-routing-translation.md), [standards record](../../../standards-provenance/tasks/20261123-ldw06-euclidean-routing-translation.json), and [measured replay](run_manifest.json).
