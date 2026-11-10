# B5-2B3R — exact external-momentum routing for \(Q_{LD}\) pure-\(WW\) cross boxes

**Date:** 2026-11-11  
**Parent:** B5-2B, strict dimension-six EFT gauge matching.  
**Status:** the earlier common-numerator diagnostic is superseded. The four cross-vertex pairings are now reduced with their own external-momentum routing, propagator denominators, and \(O(P)\) numerator terms. The resulting coefficient is still only the hard four-cross-box subset; external-field terms, counterterms, EFT subtraction and the summed Ward identity remain open.

## 1. Fixed external Green function and routing

Use the ordered amplitude
\[
\bar L_i(p_1),\quad H_j(p_2),\quad H_k^\dagger(p_3),\quad L_l(p_4),
\]
with all momenta incoming and
\[
p_1=0,\qquad p_2=P,\qquad p_3=0,\qquad p_4=-P.
\]
The left Yukawa vertex contains \((\bar L,H)\), the right conjugate Yukawa vertex contains \((H^\dagger,L)\). Let the \(W\) momentum \(k\) flow from the left Yukawa vertex to the right. The heavy propagator momentum is
\[
q_E=k-P.
\]

For the four cross-vertex pairings, the momenta of the light internal lines are fixed by momentum conservation:
\[
q_{\bar L}=-k,\qquad q_{H^\dagger}=k,\qquad
q_H=P-k,\qquad q_L=k-P.
\]
The scalar-gauge vertices follow from
\[
\mathcal L\supset
ig_2W_\mu^a H^\dagger T^a
\overleftrightarrow{\partial^\mu}H.
\]
For the stated all-incoming convention, the \(H\) vertex at the left end contributes \(2P-k\), while the \(H^\dagger\) vertex at the right end contributes \(-k\).

The manual Wick-contraction census for this fixed external ordering has one \(W\)-exchange graph for each unordered pair of distinct external lines. The two same-Yukawa-vertex pairs are LD-W-03/04 and belong to the light-only UV/EFT subfamily; the four cross-vertex pairs below are the hard box subset. This is a fixed Green-function count, not an enumeration of other crossed external channels or a FeynArts-generated diagram list.

## 2. Exact per-pair numerator and denominator audit

The exact weak tensors from the SU(2) projection are
\[
\begin{array}{c|rrrr}
\text{pair}&\text{LD-W-01}&\text{LD-W-02}&\text{LD-W-05}&\text{LD-W-06}\\ \hline
T_3\text{ coefficient}&-\frac14&+\frac14&+\frac14&-\frac14
\end{array}
\]

Unlike the earlier common-routing diagnostic, the four Lorentz numerators are not identical. Their denominators and numerators are:

| Pair | Internal lines | Denominator | Numerator |
|---|---|---|---|
| LD-W-01: \(\bar L-L\) | \(q_{\bar L}=-k,\ q_L=q_E=k-P\) | \(k^4(k-P)^2[(k-P)^2-M_E^2]\) | \(\gamma^\mu(-\slashed k)\slashed{(k-P)}\slashed{(k-P)}\gamma_\mu\) |
| LD-W-02: \(\bar L-H^\dagger\) | \(q_{\bar L}=-k,\ q_{H^\dagger}=k\) | \(k^6[(k-P)^2-M_E^2]\) | \(\gamma^\mu(-\slashed k)\slashed{(k-P)}(-k_\mu)\) |
| LD-W-05: \(H-L\) | \(q_H=P-k,\ q_L=q_E=k-P\) | \(k^2(k-P)^4[(k-P)^2-M_E^2]\) | \((2P-k)_\mu\slashed{(k-P)}\slashed{(k-P)}\gamma^\mu\) |
| LD-W-06: \(H^\dagger-H\) | \(q_H=P-k,\ q_{H^\dagger}=k\) | \(k^4(k-P)^2[(k-P)^2-M_E^2]\) | \(-(2P-k)\cdot k\,\slashed{(k-P)}\) |

The numerator signs in this table include the internal momentum directions and the \(H/H^\dagger\) scalar-vertex momentum factors. The exact SU(2) tensor signs are listed separately in the preceding table, so they are not counted twice.

## 3. Hard scalar masters

Use
\[
J(M_E)=\int_k\frac{1}{(k^2)^2(k^2-M_E^2)},
\qquad
K(M_E)=\int_k\frac{1}{k^2(k^2-M_E^2)^2},
\]
with the same \(\overline{\mathrm{MS}}\) normalization and \(L=\ln(M_E^2/\mu_R^2)\) as B5-2B3. Their hard parts are
\[
\boxed{
J_{\rm hard}=\frac{\Delta_{\rm UV}+1-L}{M_E^2},
\qquad
K_{\rm hard}=-\frac{1}{M_E^2}.
}
\]

## 4. Pair-by-pair Lorentz reduction

Retain \(d=4-2\epsilon\) until after multiplying the UV pole.

### LD-W-01: fermion–fermion

The numerator contains
\[
\gamma^\mu(-\slashed k)\slashed{(k-P)}\slashed{(k-P)}\gamma_\mu
= (d-2)(k-P)^2\slashed k.
\]
The \((k-P)^2\) cancels the corresponding light-fermion denominator. Expanding the remaining heavy denominator to first order in \(P\) gives
\[
\boxed{
A_{01}=\frac{2(d-2)}{d}K.
}
\]

### LD-W-02: fermion–scalar

The scalar vertex contributes \(-k_\mu\). Contracting the Lorentz numerator gives
\[
\gamma^\mu(-\slashed k)\slashed{(k-P)}(-k_\mu)
=k^2\slashed{(k-P)}.
\]
After canceling \(k^2\), the direct \(-\slashed P\) term gives \(-J\), and expanding the heavy propagator gives \(+2K/d\):
\[
\boxed{
A_{02}=-J+\frac{2}{d}K.
}
\]

### LD-W-05: scalar–fermion

The scalar vertex contributes \(2P-k\), while the two adjacent fermion/heavy momenta are both \(k-P\):
\[
(2P-k)_\mu\slashed{(k-P)}\slashed{(k-P)}\gamma^\mu
=(k-P)^2(2\slashed P-\slashed k).
\]
After canceling the light denominator, shift \(q=k-P\) and expand \(1/(q+P)^2\). The direct \(\slashed P\) term gives \(J\), and the tensor term gives \(+2J/d\):
\[
\boxed{
A_{05}=\left(1+\frac{2}{d}\right)J.
}
\]

### LD-W-06: scalar–scalar

The two scalar vertices give
\[
-(2P-k)\cdot k
=(k-P)^2+O(P^2).
\]
This cancels the corresponding light-scalar denominator. Shifting \(q=k-P\) and expanding \(1/(q+P)^4\) gives
\[
\boxed{
A_{06}=-\frac{4}{d}J.
}
\]

## 5. Weak-tensor sum and the \(O(\epsilon)\) finite term

The four-box tensor-weighted coefficient is
\[
\begin{aligned}
A_{WW}^{\rm box}
&=\frac14(-A_{01}+A_{02}+A_{05}-A_{06})\\
&=\boxed{
\frac14\left[
\frac{6}{d}J-\frac{2(d-3)}{d}K
\right].
}
\end{aligned}
\]

At \(d=4-2\epsilon\),
\[
\frac{6}{d}=\frac32+\frac34\epsilon+O(\epsilon^2),
\qquad
-\frac{2(d-3)}{d}
=-\frac12+\frac34\epsilon+O(\epsilon^2).
\]
The \(O(\epsilon)\) term multiplying the UV pole in \(J\) contributes \(+3/16\) to the finite coefficient. Substituting the hard masters gives
\[
\boxed{
A_{WW,\rm hard}^{\rm box}
=\frac{1}{M_E^2}
\left(
\frac38\Delta_{\rm UV}
-\frac38L
+\frac{11}{16}
\right).
}
\]

If one sets \(d=4\) before multiplying the UV pole, the finite constant is incorrectly \(1/2\), rather than \(11/16\). The difference \(3/16\) is precisely the retained \(O(\epsilon)\times1/\epsilon\) contribution.

With the same common amplitude convention as the tree-level \(Q_{LD}\) exchange, the raw four-box tensor is proportional to
\[
\Gamma_{\rm box}^{WW,\rm hard}
\propto
-i\frac{|y_\ell|^2g_2^2}{16\pi^2}
\frac{1}{M_E^2}
\left(
\frac38\Delta_{\rm UV}
-\frac38L+\frac{11}{16}
\right)T_3\slashed P.
\]
The UV pole and matching logarithm do **not** cancel inside the four-box subset. They must be combined with the EFT operator counterterm and the remaining UV/EFT amplitude organization.

## 6. Superseded diagnostic and remaining boundary

The earlier file b5_2b3_qld_ww_crossbox_tensor_kernels.py used a common numerator/denominator family for all four pairs. That simplification omitted the distinct external-momentum shifts in LD-W-01, LD-W-05 and LD-W-06. Its \(+3/(4M_E^2)\) result is therefore a historical algebraic diagnostic and is **superseded** by this exact-routing calculation. It must not be used as the \(WW\) matching coefficient.

The new companion b5_2b3_qld_ww_exact_routing.py and its regression tests check the four distinct numerator reductions, the weak-tensor-weighted sum, and the \(O(\epsilon)\) finite term. The symbolic checks are local algebra checks, not a FeynArts/FeynCalc reproduction.

Still required for the complete \(WW\) matching:
1. UV/EFT subtraction of the full set with a shared nonexceptional IR prescription.
2. External \(L,H\) LSZ/self-energy terms and the \(C_{LD}\) parameter/operator counterterms exactly once.
3. The EFT operator-counterterm matrix in the common Pauli-current/EOM basis.
4. The one-\(W\) form-factor/contact comparison and the summed Ward/Slavnov–Taylor identity.
5. Independent diagram-level validation of the fixed-routing graph count and signs.

No complete \(C_{HL}^{(1,3)}\) Wilson coefficient or anomalous dimension is claimed.
