# RC-001 QLD8 derivative-placement Fierz and IBP ledger

**Date:** 2026-11-10  
**Scope:** exact covariant-IBP relation for the complete Higgs-source square, the derivative-placement map under spinor Fierz rearrangement, and the subsector-specific evanescent definitions. This is an operator-algebra ledger, not a loop renormalization or a final nonredundant SMEFT basis.

## 1. Fixed source definitions and flavor tensors

Use the original flavor-diagonal model source
\[
\begin{aligned}
J_d^k&=\bar d_{R\,r,a}(Y_d^\dagger)_{rp}Q_{L\,p,a}^k,\\
J_u^k&=\epsilon_{ik}\bar Q_{L\,p,a}^{\,i}(Y_u)_{pr}u_{R\,r,a},\\
J_e^k&=y_e^*\bar e_R L_e^k.
\end{aligned}
\]
Here \(p,q\) label left-handed quark generations, \(r,s\) label right-handed generations, and \(a,b\) are color indices. The dimension-five axial source \(J_H^{(5)}\) is outside the strict \(M_E^{-4}\) source-square truncation: its cross terms begin at \(M_E^{-5}\), and its square begins at \(M_E^{-6}\).

For clarity, the six independent Hermitian source-pair structures carry the following Yukawa tensors:
\[
\begin{array}{c|c}
\text{pair}&\text{Yukawa factor}\\ \hline
d^\dagger d&(Y_d)_{pr}(Y_d^\dagger)_{sq}\\
u^\dagger u&(Y_u^\dagger)_{rp}(Y_u)_{qs}\\
e^\dagger e&|y_e|^2\\
d^\dagger u&(Y_d)_{pr}(Y_u)_{qs}\\
d^\dagger e&y_e^*(Y_d)_{pr}\\
u^\dagger e&y_e^*(Y_u^\dagger)_{rp}
\end{array}
\]
The flavor tensors are spectators under spinor Fierz rearrangement; no diagonal-Yukawa or generation-degeneracy assumption is made for \(Y_u,Y_d\).

## 2. Exact covariant IBP relation

For any two Higgs-doublet sources \(J_A^k,J_B^k\), their product \(J_A^{k\dagger}D^\mu J_B^k\) is a gauge singlet. Hence
\[
\partial_\mu(J_A^{k\dagger}D^\mu J_B^k)
=(D_\mu J_A^k)^\dagger D^\mu J_B^k
+J_A^{k\dagger}D^2J_B^k.
\]
After dropping the total derivative in the action,
\[
\boxed{
(D_\mu J_A^k)^\dagger D^\mu J_B^k
\doteq -J_A^{k\dagger}D^2J_B^k .
}
\]
For a diagonal pair, hermitian conjugation gives the equivalent left-oriented form. A manifestly Hermitian representative is
\[
(D_\mu J_A)^\dagger D^\mu J_A
\doteq-\frac12\left[J_A^\dagger D^2J_A+(D^2J_A^\dagger)J_A\right].
\]
For a cross pair, retain \(-J_A^\dagger D^2J_B+\mathrm{h.c.}\).

This identity applies to the **complete sum** of the four product-rule placements. It does not say that each placement separately is equivalent to one another, and it does not eliminate the source-square operator.

## 3. Laplacian of each bilinear source

For a gauge-covariant scalar bilinear \(J=\bar f\,Y\,\chi\), with constant flavor matrix \(Y\),
\[
D^2J=(D^2\bar f)Y\chi
+2(D_\mu\bar f)Y D^\mu\chi
+\bar fY D^2\chi.
\]
Thus the four product-rule placements in \((D J_A^\dagger)(D J_B)\), after the one total-derivative relation above, are represented by three right-source Laplacian classes: a Laplacian on the barred fermion, a mixed one-derivative-on-each-fermion term, and a Laplacian on the unbarred fermion. Explicitly,
\[
\begin{aligned}
D^2J_d^k={}&
(D^2\bar d_{R\,r,a})(Y_d^\dagger)_{rp}Q_{L\,p,a}^k\\
&+2(D_\mu\bar d_{R\,r,a})(Y_d^\dagger)_{rp}D^\mu Q_{L\,p,a}^k\\
&+\bar d_{R\,r,a}(Y_d^\dagger)_{rp}D^2Q_{L\,p,a}^k,\\[1mm]
D^2J_u^k={}&\epsilon_{ik}\big[
(D^2\bar Q_{L\,p,a}^{\,i})(Y_u)_{pr}u_{R\,r,a}\\
&\qquad+2(D_\mu\bar Q_{L\,p,a}^{\,i})(Y_u)_{pr}D^\mu u_{R\,r,a}\\
&\qquad+\bar Q_{L\,p,a}^{\,i}(Y_u)_{pr}D^2u_{R\,r,a}\big],\\[1mm]
D^2J_e^k={}&y_e^*\big[
(D^2\bar e_R)L_e^k
+2(D_\mu\bar e_R)D^\mu L_e^k
+\bar e_R D^2L_e^k\big].
\end{aligned}
\]
All derivatives are covariant in the representation of the field on which they act. The weak \(\epsilon_{ik}\) and all generation/color labels are retained.

## 4. Derivative placement under Fierz rearrangement

For a generic source pair
\[
(\bar\psi\chi)(\bar\eta\xi),
\]
let \(r=0\) mean that the derivative in the first source bilinear acts on \(\bar\psi\), and \(r=1\) that it acts on \(\chi\). Let \(s=0\) mean that the derivative in the second source bilinear acts on \(\bar\eta\), and \(s=1\) that it acts on \(\xi\). The spinor Fierz rearrangement pairs \((\bar\psi,\xi)\) and \((\bar\eta,\chi)\); it does **not** move a derivative from one field to another.

The exact derivative assignment after Fierz is:

| Original placement \((r,s)\) | First Fierz bilinear \((\bar\psi\,\Gamma\,\xi)\) | Second Fierz bilinear \((\bar\eta\,\Gamma'\,\chi)\) |
|---|---|---|
| \((0,0)\) | \(D_\mu\bar\psi\) | \(D^\mu\bar\eta\) |
| \((0,1)\) | \(D_\mu\bar\psi\) and \(D^\mu\xi\) | no derivative |
| \((1,0)\) | no derivative | \(D_\mu\bar\eta\) and \(D^\mu\chi\) |
| \((1,1)\) | \(D^\mu\xi\) | \(D_\mu\chi\) |

The table is just a relabeling of the four differentiated fermion fields. In particular, placements \((0,1)\) and \((1,0)\) put both derivatives inside one Fierz-rearranged bilinear. They must not be silently replaced by the \((0,0)\) or \((1,1)\) patterns.

## 5. Channel-to-evanescent map

The four-dimensional Fierz projections and the working \(D=4-2\epsilon\) Fierz-difference definitions are:

| Ordered source pair | Chiral projectors in original scalar pair | Four-dimensional physical projection | Evanescent difference |
|---|---|---|---|
| \(d^\dagger d\) | \(R\otimes L\) | vector \(\times\) vector | \(E_{RL}^{(rs)}\) |
| \(u^\dagger u\) | \(L\otimes R\) | vector \(\times\) vector | \(E_{LR}^{(rs)}\) |
| \(e^\dagger e\) | \(R\otimes L\) | vector \(\times\) vector | \(E_{RL}^{(rs)}\) |
| \(d^\dagger e\) | \(R\otimes L\) | quark-lepton vector \(\times\) vector | \(E_{RL}^{(rs)}\) |
| \(d^\dagger u\) | \(R\otimes R\) | scalar plus tensor | \(E_{RR}^{(rs)}\) |
| \(u^\dagger e\) | \(L\otimes L\) | scalar plus tensor | \(E_{LL}^{(rs)}\) |

For every derivative placement, \(E_{RL}^{(rs)}\) is defined as the original differentiated scalar product plus one half of the differentiated crossed vector-current product; \(E_{LR}^{(rs)}\) is its \(L\leftrightarrow R\) counterpart. Likewise \(E_{RR}^{(rs)}\) and \(E_{LL}^{(rs)}\) are the original differentiated same-projector scalar products plus one half of the crossed scalar product plus one eighth of the crossed tensor product. The derivative acts on the same original fermion field before and after the spinor-index rearrangement, as tabulated in §4.

These are definitions of evanescent differences: they vanish in exactly four dimensions by the checked Fierz identities, but are not set to zero in \(D=4-2\epsilon\). The no-\(O(\epsilon)\)-physical-admixture convention and open-line NDR prescription are fixed in [RC-001-QLD-chiral-Fierz-identities.md](RC-001-QLD-chiral-Fierz-identities.md). This does not close the one-loop evanescent counterterm basis; higher antisymmetrized gamma strings must be added if generated.

## 6. What this reduction does and does not establish

Established:
1. The full source-square has nine ordered pairs, equivalently three diagonal pairs and three cross pairs plus their Hermitian conjugates.
2. Each ordered pair has four product-rule placements, giving 36 placements across the full ordered sum.
3. The complete pair admits the exact covariant-IBP representation \(-J_A^\dagger D^2J_B\).
4. The Laplacian of each source has exactly three Leibniz classes.
5. The derivative labels are preserved under the spinor Fierz rearrangement, with the nontrivial \((0,1)\) and \((1,0)\) assignments shown explicitly.
6. Each channel has a specified chiral Fierz class and corresponding Fierz-difference evanescent definition.

Not established:
- reduction of the Laplacian and mixed-derivative classes to a minimal operator basis using the full fermion EOM;
- the complete one-loop evanescent mixing/counterterm matrix;
- the same-order EFT soft graphs and finite UV-minus-EFT Wilson coefficients;
- a contribution to the PR #69 \(hh,hs,ss\) scalar two-point functions.

No source-square coefficient is promoted into the scalar two-point matching by this ledger.
