# RC-001 — Yukawa-singlet endpoint cancellation with common heavy-channel routing

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-b  
**Status:** the local gauge variation of each Yukawa singlet has been checked in the physical \(SU(2)_L\) field representations, and the common-\(k\) maps show that the two light-field endpoint variations at a given Yukawa vertex multiply the same heavy-channel spectator. Thus the local Yukawa-endpoint charge sum cancels before loop integration. This is the local endpoint sub-block only; it is not the complete external-leg/LSZ or Slavnov–Taylor identity.

## 1. Physical field representations

Use
\[
R_{\bar L}^a=-t^{aT},\qquad
R_H^a=+t^a,\qquad
R_{H^\dagger}^a=-t^{aT},\qquad
R_L^a=+t^a,\qquad t^a=\frac{\sigma^a}{2}.
\]
For the left Yukawa singlet \(\bar L H E_R\), \(E_R\) is an \(SU(2)_L\) singlet and
\[
\boxed{(R_{\bar L}^a+R_H^a)T_0=0.}
\tag{1.1}
\]
For the right conjugate Yukawa singlet \(\bar E_R H^\dagger L\),
\[
\boxed{(R_{H^\dagger}^a+R_L^a)T_0=0.}
\tag{1.2}
\]
These are checked directly with the physical field-representation matrices for every external weak-index component and all three generators.

## 2. Why the common heavy momentum matters

The WTI endpoint terms can be canceled by the local Yukawa-singlet charge sum only when the two field variations multiply the same heavy-channel factor. The previously fixed common-\(k\) maps give precisely this.

### Cross-vertex A-side insertion

Let \(P_L=p_1+p_2\) and \(k_{\rm old}=k+q\). The A-side external-W insertion has
\[
h_A=k_{\rm old}-P_L-q.
\]
After the validated shift,
\[
\boxed{h_A=k-P_L=h_{\rm ref}.}
\]
The two light-field variations \(\bar L,H\) at that left Yukawa vertex therefore share the same \(S_E(h_{\rm ref})\).

### Cross-vertex B-side insertion

The B-side route is already in the common \(k\) variable and has
\[
\boxed{h_B=k-P_L=h_{\rm ref}.}
\]
The two light-field variations \(H^\dagger,L\) at the right Yukawa vertex share this same heavy factor.

### Same-vertex triangles

For LD-W-03/04, the external W transfers \(q\) into the common Yukawa channel:
\[
\boxed{h_E=p_F+p_S+q.}
\]
The F-line insertion, S-line insertion, scalar seagull, and three-W route all use this same \(h_E\). It is independent of \(k\):
\[
\frac{\partial h_E}{\partial k^\mu}=0.
\]
Thus the F and S field variations at the same Yukawa vertex also multiply the same heavy spectator.

## 3. Local endpoint cancellation

Let \(X_{\rm rest}\) denote the remaining common Dirac, scalar, and propagator factors at the given Yukawa vertex. Since these factors are identical for the two field variations after the common-\(k\) shifts, the local endpoint sum factors as
\[
\delta_{\rm Yukawa}\mathcal M_{\rm endpoint}
\propto
\left(R_{\rm first}^a+R_{\rm second}^a\right)
T_0\,S_E(h_{\rm common})X_{\rm rest}=0.
\]
For the left vertex the pair is \((\bar L,H)\); for the right vertex it is \((H^\dagger,L)\). The same argument applies to the same-vertex F/S pair because its heavy channel is the common spectator \(h_E\).

This cancellation removes the **local Yukawa-vertex gauge variation** from the ordinary-matter endpoint ledger. It does not remove the external-leg emissions themselves from the amputated Green-function Ward identity: their reducible/LSZ organization must still be kept explicit.

## 3.1 LD-W-06 secondary shifts

The two secondary loop shifts required by the \(-\Delta_W\) pieces are
\[
k_A'=k+q,\qquad k_B'=k-q.
\]
They change the heavy channel, but they do not split the two light-field variations at either Yukawa singlet:
\[
h_{\bar L}(k_A')=h_H(k_A')=h(k_A')-q,
\]
\[
h_{H^\dagger}(k_B')=h_L(k_B')=h(k_B')+q.
\]
Consequently the local physical-representation identities remain
\[
(R_{\bar L}^a+R_H^a)T_0\,S_E(h-q)X_A=0,
\]
\[
(R_{H^\dagger}^a+R_L^a)T_0\,S_E(h+q)X_B=0.
\]
The three heavy denominators \(h^2-M_E^2\), \((h-q)^2-M_E^2\), and \((h+q)^2-M_E^2\) are generically distinct; the cancellation works because the two field variations at a given vertex share the same shifted heavy factor, not because the shifted propagators equal the unshifted one.

The exact calculation is recorded in:
- \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_shifted_Yukawa_singlet_charge_closure.py\`
- \`research/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.md\`
- \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.txt\`

The shifted heavy-channel maps pass 8/8 vector components on each side, and the shifted left/right singlet charge sums pass 96/96 weak components. This remains a local endpoint-factor cancellation only.

## 3.2 All-six pair-class extension

The same channel statement is not specific to LD-W-06:
- For every cross-vertex A endpoint (LD-W-01/02/05/06), the secondary shift \(k'=k+q\) gives the common left-singlet channel \(h-q\) for \(\bar L\) and \(H\).
- For every cross-vertex B endpoint (LD-W-01/02/05/06), the secondary shift \(k'=k-q\) gives the common right-singlet channel \(h+q\) for \(H^\dagger\) and \(L\).
- For same-vertex LD-W-03/04, \(h_E=p_F+p_S+q\) is independent of \(k\), so both loop shifts leave the common heavy spectator unchanged.

The exact physical charge sums, multiplied by independent \(S_E(h-q)\), \(S_E(h+q)\), and \(S_E(h_E)\) factors, pass 192/192 weak-index components. The routing maps pass 8/8 components for cross A, 4/4 for cross B, and 8/8 shift-vector plus 16/16 derivative checks for same-vertex spectators.

Reproduction:
- \`calculations/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.py\`
- \`calculations/test_RC001_dim6_WW_fivepoint_all_six_shifted_Yukawa_singlet_channel_audit.py\`
- \`research/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.md\`
- \`validation/RC-001-dim6-WW-fivepoint-all-six-shifted-Yukawa-singlet-channel-audit.txt\`

This closes the local Yukawa-singlet charge factor under the validated shifts for all six pair classes. It does not close the full 1PI longitudinal integrand or the reducible LSZ sector.

## 4. Exact reproduction

- Source: \`calculations/RC-001-dim6-WW-fivepoint-yukawa-singlet-endpoint-cancellation.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_yukawa_singlet_endpoint_cancellation.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-yukawa-singlet-endpoint-cancellation.txt\`

The local exact SymPy audit checks:
- left/right Yukawa-singlet charge sums: 96/96 weak components;
- cross-vertex A/B common heavy-channel maps: 8/8 vector components;
- same-vertex F/S/seagull/three-W common \(h_E\): 12/12 vector components;
- multiplication by the common heavy spectator preserves the zero weak charge sum: 96/96 component checks.

This is not a GitHub Actions result or a full Green-function calculation.

## 5. Boundary and next step

The local Yukawa endpoint charge sum is now closed. Still separate are:
1. the explicit reducible external-leg/LSZ emission terms and their shifted four-point amplitudes;
2. the ordinary-matter sum of fermion WTIs, scalar-line/seagull kernels, and three-W \(R_{\rm FG}\) terms;
3. the gauge-fixing/ghost Slavnov–Taylor completion;
4. \(W\)-field, gauge-coupling, \(L,H\) field, \(y_\ell,M_E\), \(C_{LD}\), and operator counterterms.

The next step is to combine the now-explicit local Yukawa endpoint cancellation with the ordinary-matter common-\(k\) integrand, while keeping the reducible external-leg terms in a separate ledger. No complete STI closure, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed here.
