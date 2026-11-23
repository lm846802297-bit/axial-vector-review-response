# RC-001 — Raw weak-index bridge for same-vertex \(WW\) five-point graphs

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVe  
**Status:** the raw weak-index ordering for LD-W-03/04 is now derived separately using their actual internal-W orientation \(S\to F\). The two seed tensors, the F- and S-line ordered products, the scalar seagull anticommutator, and the reversed three-W group tensor are checked explicitly. Together with the cross-vertex bridge, this accounts for the weak-index ordering of all 24 direct attachments. The Lorentz-weighted Ward sum remains open.

## 1. Why LD-W-03/04 cannot inherit the cross-vertex three-W sign

The same-vertex seed pairs are
\[
\begin{array}{c|cc}
\text{pair}&F&S\\ \hline
\text{LD-W-03}&\bar L\ (0)&H\ (1)\\
\text{LD-W-04}&L\ (3)&H^\dagger\ (2)
\end{array}
\]
where \(F\) denotes the fermion endpoint and \(S\) the scalar endpoint. The internal W is oriented from the scalar endpoint to the fermion endpoint:
\[
k_S=k,\qquad k_F=k+q,\qquad q+k_S-k_F=0.
\]
This is the opposite orientation from the cross-vertex A-to-B routing. In particular, the three-W weak tensor must not be copied with the same endpoint ordering.

Use the physical field generators
\[
R_{\bar L}^a=-t^{aT},\quad R_H^a=t^a,\quad
R_{H^\dagger}^a=-t^{aT},\quad R_L^a=t^a,
\qquad t^a=\frac{\sigma^a}{2}.
\]
The seed exchange tensor is
\[
\mathcal T_{FS}=\sum_bR_F^bR_S^bT_0
=-\frac34T_0
\]
for both LD-W-03 and LD-W-04.

## 2. Raw F- and S-line matrix order

The B1 momentum routes place the external-W insertion between the Yukawa vertex and the internal-W endpoint on both matter propagators. The fermion arrow and complex-scalar index orientation give different matrix orderings. In the physical field-representation basis, the raw ordered tensors are
\[
\mathcal W_F^a
=\sum_bR_F^bR_F^aR_S^bT_0,
\qquad
\widetilde{\mathcal W}_F^a
=\sum_bR_F^aR_F^bR_S^bT_0,
\]
\[
\mathcal W_S^a
=\sum_bR_F^bR_S^aR_S^bT_0,
\qquad
\widetilde{\mathcal W}_S^a
=\sum_bR_F^bR_S^bR_S^aT_0.
\]
The exact physical-representation algebra gives
\[
\boxed{
\mathcal W_F^a-\widetilde{\mathcal W}_F^a
=+i\mathcal G_{FS}^a,
\qquad
\mathcal W_S^a-\widetilde{\mathcal W}_S^a
=+i\mathcal G_{FS}^a,
}
\]
where
\[
\mathcal G_{FS}^a
=\epsilon^{abc}R_F^bR_S^cT_0.
\]
The two commutator identities are checked for both same-vertex pairs, all three external-W generators and all 16 weak-index components.

## 3. Three-W tensor with the actual \(S\to F\) orientation

At the three-W vertex the internal index \(b\) is attached to the S-side line and \(c\) to the F-side line. The raw group factor is therefore
\[
\mathcal G_{3W,\,S\to F}^a
=\epsilon^{abc}R_S^bR_F^cT_0.
\]
Because the two endpoint actions act on different tensor slots, they commute. Interchanging the dummy labels \(b\leftrightarrow c\) then gives
\[
\boxed{
\mathcal G_{3W,\,S\to F}^a
=-\epsilon^{abc}R_F^bR_S^cT_0
=-\mathcal G_{FS}^a.
}
\tag{3.1}
\]
This is the sign reversal absent from the cross-vertex A-to-B orientation.

With the already-fixed relative phases
\[
P_{\rm line}/P_4=-g_2,\qquad
P_{3W}/P_4=-ig_2,
\]
the phase-weighted group factors are
\[
-g_2(\mathcal W_F^a-\widetilde{\mathcal W}_F^a)
=-ig_2\mathcal G_{FS}^a,
\]
\[
-g_2(\mathcal W_S^a-\widetilde{\mathcal W}_S^a)
=-ig_2\mathcal G_{FS}^a,
\]
whereas
\[
\frac{P_{3W}}{P_4}\mathcal G_{3W,\,S\to F}^a
=(-ig_2)(-\mathcal G_{FS}^a)
=+ig_2\mathcal G_{FS}^a.
\]
Thus the same-vertex line commutator and three-W group-phase factors are opposite:
\[
\boxed{
-g_2(\mathcal W_{F,S}^a-\widetilde{\mathcal W}_{F,S}^a)
+\frac{P_{3W}}{P_4}\mathcal G_{3W,\,S\to F}^a=0.
}
\]
This is a group-phase identity only. The Lorentz kernels must still be compared with the exact shifted momenta before it can be called a diagrammatic cancellation.

## 4. Scalar seagull at the S endpoint

There is one scalar seagull per same-vertex pair. Its raw weak tensor is
\[
\mathcal S_S^a
=\sum_bR_F^b\{R_S^a,R_S^b\}T_0
=\mathcal W_S^a+\widetilde{\mathcal W}_S^a
=\frac12R_F^aT_0.
\]
The anticommutator and its equality to the sum of the two S-line orderings are checked for both pairs, all external-W generators and all weak-index components (96/96). Its Lorentz contact factor \(q^\mu\) remains separate from the scalar-line propagator difference.

## 5. Attachment census and relation to the cross-vertex subset

Each same-vertex pair contains:
1. one F-line external-W insertion;
2. one S-line external-W insertion;
3. one S-endpoint scalar seagull;
4. one insertion on the internal W through the three-W vertex.

Thus LD-W-03 and LD-W-04 contribute eight attachments. The cross-vertex raw-index bridge covers the other 16:
\[
16_{\rm cross}+8_{\rm same}=24_{\rm direct}.
\]
The B1 routing source already verifies the same-vertex shifted heavy momentum
\[
P_E=P_{FS}+q
\]
for the F-line, S-line, seagull and three-W attachments. No momentum-routing gap remains here; the outstanding task is the Lorentz-weighted sum.

## 6. Reproduction and evidence boundary

- Exact source: calculations/RC-001-dim6-WW-same-vertex-raw-weak-index-bridge.py
- Captured output: validation/RC-001-dim6-WW-same-vertex-raw-weak-index-bridge.txt
- Cross-vertex counterpart: research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md

The local exact checks establish:
- physical representation algebra: 144/144 matrix components;
- two seed tensors: 32/32 weak components;
- F- and S-line ordered commutators: 96/96 each;
- phase-weighted F/S commutator plus \(S\to F\) three-W group factor: 96/96 each;
- S-endpoint scalar seagull anticommutator: 96/96.

Combining the two raw-index bridges now fixes the weak-index ordering and relative group phases for all 24 direct attachments. It does **not** establish:
1. cancellation of the Lorentz kernels multiplying the same-vertex group-phase identity;
2. the complete cross-vertex matter-line/three-W Lorentz sum;
3. the scalar-line/seagull Lorentz sum with distinct weak tensors;
4. the Feynman-gauge \(R_{\rm FG}\) gauge-fixing/ghost completion;
5. external-leg/LSZ, parameter and operator counterterms;
6. any integrated UV five-point form factor or Wilson coefficient.

The next step is the common-\(k\) Lorentz-weighted sum, not another weak-index census. Use the already-validated B1 routes, the cross-vertex and same-vertex raw tensors, and the distinct scalar seagull factors. Keep the \(R_{\rm FG}\) remainder explicit. Only after the longitudinal integrand closes should the UV/EFT hard-soft subtraction and transverse form-factor comparison be attempted.
