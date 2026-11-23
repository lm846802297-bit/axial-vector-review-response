# RC-001 — LD-W-06 shifted Yukawa-singlet charge closure

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-g/02  
**Status:** the secondary LD-W-06 shifts \(k_A'=k+q\) and \(k_B'=k-q\) have been applied to the two Yukawa vertices. At the left vertex, the \(\bar L\) and \(H\) variations share \(h-q\); at the right vertex, the \(H^\dagger\) and \(L\) variations share \(h+q\). The physical SU(2) singlet charge sums therefore still vanish when multiplied by the corresponding shifted heavy propagator. This closes the local charge-factor check, not the full five-point Ward/LSZ sum.

## 1. Shifted heavy channels

Let \(P_L=p_1+p_2\) and \(h(k)=k-P_L\).

For the A-side secondary shift
\[
k_A'=k+q,
\]
the two light-field variations at the left Yukawa singlet have
\[
h_{\bar L}(k_A')=k_A'-P_L-q=h(k_A')-q,
\]
\[
h_H(k_A')=k_A'-P_L-q=h(k_A')-q.
\]
They therefore multiply the same shifted heavy factor
\[
S_E(h-q)=\frac{\slashed{(h-q)}P_L}{(h-q)^2-M_E^2}
\]
(up to the common Feynman-rule factors and the unchanged rest of the endpoint chain).

For the B-side secondary shift
\[
k_B'=k-q,
\]
the two light-field variations at the right Yukawa singlet have
\[
h_{H^\dagger}(k_B')=k_B'-P_L+q=h(k_B')+q,
\]
\[
h_L(k_B')=k_B'-P_L+q=h(k_B')+q.
\]
They multiply the same
\[
S_E(h+q)=\frac{\slashed{(h+q)}P_L}{(h+q)^2-M_E^2}.
\]

## 2. Physical singlet charge sums

The physical field representations remain
\[
R_{\bar L}^a=-t^{aT},\quad R_H^a=t^a,\quad
R_{H^\dagger}^a=-t^{aT},\quad R_L^a=t^a.
\]
Thus
\[
(R_{\bar L}^a+R_H^a)T_0=0,\qquad
(R_{H^\dagger}^a+R_L^a)T_0=0.
\]
Because the two variations at each vertex multiply the same shifted heavy propagator, the local charge sum still factors:
\[
(R_{\bar L}^a+R_H^a)T_0\,S_E(h-q)X_A=0,
\]
\[
(R_{H^\dagger}^a+R_L^a)T_0\,S_E(h+q)X_B=0.
\]
The exact physical-representation check covers all three generators and all 16 external weak-index components for each singlet.

## 3. Rational heavy-channel check

At the LD-W-06 rational diagnostic point,
\[
h=(5,-1,-1,0),\quad q=(1,1,0,0),\quad M_E^2=400,
\]
the denominators are
\[
h^2-M_E^2=-377,\qquad
(h-q)^2-M_E^2=-389,\qquad
(h+q)^2-M_E^2=-365.
\]
The shifted heavy factors are distinct, but the two field variations at each individual Yukawa vertex share the same one. Hence the local singlet charge cancellation survives both secondary shifts.

## 4. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_shifted_Yukawa_singlet_charge_closure.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-shifted-Yukawa-singlet-charge-closure.txt\`

The local exact checks cover both secondary heavy-channel maps (8/8 vector components each), 96/96 weak-index charge-sum components, and the rational \(H_0,H_A,H_B\) values. These are local SymPy checks, not a GitHub Actions result.

This does **not** show that the full LD-W-06 scalar-line terms cancel the three-W graph. The ordered Lorentz kernels, symmetric/commutator q contacts, \(R_{\rm FG}\), and reducible external-leg/LSZ terms remain in the ordinary-matter Ward assembly.
