# RC-001 — all-six shifted Yukawa-singlet channel audit

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-g/03  
**Status:** the local Yukawa-singlet charge-factor check has been extended to all six LD-W-01…06 pair classes. Cross-vertex A endpoints share \(h-q\) after \(k'=k+q\); cross-vertex B endpoints share \(h+q\) after \(k'=k-q\); same-vertex LD-W-03/04 heavy spectators remain independent of the loop momentum. The physical left/right singlet charge sums vanish with these channel factors. This is not the full ordinary-matter Ward sum.

## 1. Cross-vertex A endpoint

Let \(P_L=p_1+p_2\) and \(h(k)=k-P_L\). The first common-\(k\) route uses \(k_{\rm old}=k+q\):
\[
h_A=k_{\rm old}-P_L-q=h(k).
\]
The secondary shift \(k'=k+q\) rewrites the same channel as
\[
\boxed{h_A=h(k')-q.}
\]
This applies whether the A endpoint is a fermion or a scalar: the physical fields at the left Yukawa singlet are \(\bar L,H\), and both variations share this same heavy factor.

## 2. Cross-vertex B endpoint

The B endpoint is already in the common \(k\) route, with \(h_B=h(k)\). Under the secondary shift \(k'=k-q\),
\[
\boxed{h_B=h(k')+q.}
\]
This applies whether the B endpoint is a fermion or a scalar: the fields at the right Yukawa singlet are \(H^\dagger,L\), and both variations share this same heavy factor.

## 3. Same-vertex pairs

For LD-W-03/04,
\[
h_E=p_F+p_S+q
\]
is independent of \(k\). Neither \(k\to k+q\) nor \(k\to k-q\) changes this heavy spectator. The F/S endpoint variations therefore continue to share \(h_E\).

## 4. Physical charge sums

The exact physical representation identities are
\[
(R_{\bar L}^a+R_H^a)T_0=0,\qquad
(R_{H^\dagger}^a+R_L^a)T_0=0.
\]
The standalone check multiplies these by independent heavy-channel factors \(S_E(h-q)\), \(S_E(h+q)\), and \(S_E(h_E)\). It verifies 192/192 weak-index components across all three channel types.

At the LD-W-06 rational point,
\[
H_0=-377,\qquad H_A=-389,\qquad H_B=-365.
\]
The channels are distinct, but the two field variations at each individual Yukawa vertex carry the same one. Hence the local charge-factor cancellation remains exact.

## 5. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_all_six_shifted_Yukawa_singlet_channel_audit.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.txt\`

The local exact checks include cross A/B shifted heavy channels, same-vertex spectator independence, and all left/right physical charge sums. This is a local endpoint-factor result, not a full Green-function Ward identity.

The ordinary-matter 1PI sum, the explicit four external-leg/LSZ contributions, and the BRST/ghost STI remain separate. No loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
