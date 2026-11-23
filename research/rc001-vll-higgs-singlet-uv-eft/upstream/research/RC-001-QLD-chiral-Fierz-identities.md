# RC-001 chiral Fierz identities for the QLD8 source-square channels

**Date:** 2026-11-10  
**Scope:** exact four-dimensional chiral Fierz identities needed by the source-pair census, plus candidate evanescent definitions for a later \(d=4-2\epsilon\) reduction. This is not yet a one-loop anomalous-dimension or finite-matching calculation.

## 1. Spinor identities

Use
\[
P_{R,L}=\frac{1\pm\gamma_5}{2},\qquad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu],
\qquad g_{\mu\nu}=\operatorname{diag}(+,-,-,-).
\]
The exact four-dimensional c-number tensor identities are
\[
\begin{aligned}
(P_R)_{\alpha\beta}(P_R)_{\gamma\delta}
={}&\frac12(P_R)_{\alpha\delta}(P_R)_{\gamma\beta}\\
&+\frac18(\sigma^{\mu\nu}P_R)_{\alpha\delta}
(\sigma_{\mu\nu}P_R)_{\gamma\beta},\\
(P_L)_{\alpha\beta}(P_L)_{\gamma\delta}
={}&\frac12(P_L)_{\alpha\delta}(P_L)_{\gamma\beta}\\
&+\frac18(\sigma^{\mu\nu}P_L)_{\alpha\delta}
(\sigma_{\mu\nu}P_L)_{\gamma\beta},\\
(P_R)_{\alpha\beta}(P_L)_{\gamma\delta}
={}&\frac12(\gamma^\mu P_L)_{\alpha\delta}
(\gamma_\mu P_R)_{\gamma\beta},\\
(P_L)_{\alpha\beta}(P_R)_{\gamma\delta}
={}&\frac12(\gamma^\mu P_R)_{\alpha\delta}
(\gamma_\mu P_L)_{\gamma\beta}.
\end{aligned}
\]
For anticommuting fermion fields, exchanging the middle two fields contributes an additional minus sign. The operator Fierz identities are therefore
\[
\boxed{\begin{aligned}
(\bar\psi P_R\chi)(\bar\eta P_R\xi)
={}&-\frac12(\bar\psi P_R\xi)(\bar\eta P_R\chi)\\
&-\frac18(\bar\psi\sigma^{\mu\nu}P_R\xi)
(\bar\eta\sigma_{\mu\nu}P_R\chi),\\
(\bar\psi P_L\chi)(\bar\eta P_L\xi)
={}&-\frac12(\bar\psi P_L\xi)(\bar\eta P_L\chi)\\
&-\frac18(\bar\psi\sigma^{\mu\nu}P_L\xi)
(\bar\eta\sigma_{\mu\nu}P_L\chi),\\
(\bar\psi P_R\chi)(\bar\eta P_L\xi)
={}&-\frac12(\bar\psi\gamma^\mu P_L\xi)
(\bar\eta\gamma_\mu P_R\chi),\\
(\bar\psi P_L\chi)(\bar\eta P_R\xi)
={}&-\frac12(\bar\psi\gamma^\mu P_R\xi)
(\bar\eta\gamma_\mu P_L\chi).
\end{aligned}}
\]
These identities act only on spinor indices. Color, weak-isospin, flavor, and derivative labels must be carried through the rearrangement.

## 2. Application to the source-pair census

The chirality classification in [RC-001-QLD-source-square-Fierz-channel-census.md](RC-001-QLD-source-square-Fierz-channel-census.md) now has explicit four-dimensional projections:

- \(d^\dagger d\), \(u^\dagger u\), and \(e^\dagger e\) are opposite-projector scalar pairs and project to vector-current structures.
- \(d^\dagger e\) is also an opposite-projector pair and projects to a quark-lepton vector-current structure.
- \(d^\dagger u\) and \(u^\dagger e\) are same-projector pairs and require both scalar and tensor structures.

For example, suppressing the derivative placement but retaining the weak/color labels,
\[
\begin{aligned}
(\bar Q_{L,a}^k d_{R,a})(\bar e_R L_e^k)
&=-\frac12(\bar Q_{L,a}^k\gamma^\mu L_e^k)
(\bar e_R\gamma_\mu d_{R,a}),\\
\epsilon_{ik}(\bar Q_{L,a}^k d_{R,a})(\bar Q_{L,b}^i u_{R,b})
&=-\frac12\epsilon_{ik}
(\bar Q_{L,a}^k u_{R,b})(\bar Q_{L,b}^i d_{R,a})\\
&\quad-\frac18\epsilon_{ik}
(\bar Q_{L,a}^k\sigma^{\mu\nu}u_{R,b})
(\bar Q_{L,b}^i\sigma_{\mu\nu}d_{R,a}).
\end{aligned}
\]
The second example retains the crossed color labels \(a,b\) and the antisymmetric weak contraction. It must not be replaced by a color-singlet current product without a separate \(SU(3)_c\) completeness step.

The identities apply separately to each of the four product-rule derivative placements in \((D_\mu J_A)^\dagger D^\mu J_B\), with the relevant fermion field replaced by its covariant derivative. They do not identify those derivative placements with one another; IBP and EOM relations must be handled afterwards.

## 3. Candidate evanescent definitions

For a later \(d=4-2\epsilon\) calculation, one possible minimal Fierz-difference definition is
\[
\begin{aligned}
E_{RR}^{(0)}={}&
(\bar\psi P_R\chi)(\bar\eta P_R\xi)
+\frac12(\bar\psi P_R\xi)(\bar\eta P_R\chi)\\
&+\frac18(\bar\psi\sigma^{\mu\nu}P_R\xi)
(\bar\eta\sigma_{\mu\nu}P_R\chi),\\
E_{RL}^{(0)}={}&
(\bar\psi P_R\chi)(\bar\eta P_L\xi)
+\frac12(\bar\psi\gamma^\mu P_L\xi)
(\bar\eta\gamma_\mu P_R\chi),
\end{aligned}
\]
with \(E_{LL}^{(0)}\) and \(E_{LR}^{(0)}\) obtained by \(L\leftrightarrow R\). These vanish by the four-dimensional identities above. The superscript \((0)\) means no \(O(\epsilon)\) physical-operator admixture has been added to the definition.

This is a **minimal Fierz-difference evanescent convention**, not yet a complete one-loop evanescent basis. A working scheme is now fixed for the QLD8 open-fermion-line sector:
- dimensional continuation \(D=4-2\epsilon\) and \(\overline{\mathrm{MS}}\), consistent with the RC-001 master;
- naive dimensional regularization with anticommuting \(\gamma_5\) on the open fermion lines;
- the \(E_{RR}^{(0)},E_{LL}^{(0)},E_{RL}^{(0)},E_{LR}^{(0)}\) definitions above, with no \(O(\epsilon)\) physical-operator admixture at the definition stage.

This is a **subsector-specific working prescription**, not a blanket prescription for every RC-001 diagram. The QLD8 Green functions under discussion have open external-fermion lines; if a closed \(\gamma_5\) trace or anomaly-sensitive subgraph enters a later completion, stop and treat that subgraph with a consistent anomaly-preserving prescription (for example BMHV plus the required finite symmetry-restoring counterterms), rather than applying anticommuting \(\gamma_5\) blindly.

Higher antisymmetrized gamma strings generated by one-loop renormalization may require additional evanescent operators. The four Fierz-difference operators above are not asserted to close the full counterterm basis. A redefinition \(E_i\to E_i+\epsilon r_{ij}Q_j\) changes finite renormalized Wilson coefficients and must be recorded if made. The UV and EFT sides must use exactly the same prescription and evanescent definitions.

## 4. Exact validation and boundary

The companion SymPy script constructs the Dirac gamma matrices and verifies all four c-number tensor identities component by component (256 components per identity). The operator-level minus signs are then supplied by the Grassmann field interchange, not by the matrix identity itself.

This closes the four-dimensional spinor Fierz algebra used to classify the source pairs. It does not establish the \(d\)-dimensional evanescent mixing matrix, the finite one-loop scheme conversion, the full color/weak basis, the derivative IBP reduction, or the final dimension-eight Wilson vector.


## 5. Explicit representative Fierz map for all six source-pair channels

The following expressions suppress the four derivative placements but keep weak and color indices. They are the spinor Fierz projection to apply separately to each derivative placement.

### 5.1 Opposite-projector channels

\[
\begin{aligned}
d^\dagger d:\quad
&(\bar Q_{L,a}^k d_{R,a})(\bar d_{R,b}Q_{L,b}^k)\\
&\quad=-\frac12
(\bar Q_{L,a}^k\gamma^\mu Q_{L,b}^k)
(\bar d_{R,b}\gamma_\mu d_{R,a}),\\[2mm]
u^\dagger u:\quad
&(\bar u_{R,a}Q_{L,a}^i)(\bar Q_{L,b}^i u_{R,b})\\
&\quad=-\frac12
(\bar u_{R,a}\gamma^\mu u_{R,b})
(\bar Q_{L,b}^i\gamma_\mu Q_{L,a}^i),\\[2mm]
e^\dagger e:\quad
&(\bar L_e^k e_R)(\bar e_R L_e^k)\\
&\quad=-\frac12
(\bar L_e^k\gamma^\mu L_e^k)
(\bar e_R\gamma_\mu e_R),\\[2mm]
d^\dagger e:\quad
&(\bar Q_{L,a}^k d_{R,a})(\bar e_R L_e^k)\\
&\quad=-\frac12
(\bar Q_{L,a}^k\gamma^\mu L_e^k)
(\bar e_R\gamma_\mu d_{R,a}).
\end{aligned}
\]

### 5.2 Same-projector channels

\[
\begin{aligned}
d^\dagger u:\quad
&\epsilon_{ik}(\bar Q_{L,a}^k d_{R,a})
(\bar Q_{L,b}^i u_{R,b})\\
&\quad=-\frac12\epsilon_{ik}
(\bar Q_{L,a}^k u_{R,b})(\bar Q_{L,b}^i d_{R,a})\\
&\qquad-\frac18\epsilon_{ik}
(\bar Q_{L,a}^k\sigma^{\mu\nu}u_{R,b})
(\bar Q_{L,b}^i\sigma_{\mu\nu}d_{R,a}),\\[2mm]
u^\dagger e:\quad
&\epsilon_{ik}(\bar u_{R,a}Q_{L,a}^i)
(\bar e_R L_e^k)\\
&\quad=-\frac12\epsilon_{ik}
(\bar u_{R,a}L_e^k)(\bar e_R Q_{L,a}^i)\\
&\qquad-\frac18\epsilon_{ik}
(\bar u_{R,a}\sigma^{\mu\nu}L_e^k)
(\bar e_R\sigma_{\mu\nu}Q_{L,a}^i).
\end{aligned}
\]

The reverse cross channels are the Hermitian conjugates. The \(d^\dagger u\) and \(u^\dagger e\) channels require both scalar and tensor structures; retaining only a scalar Fierz projection would be incomplete.

### 5.3 Color decomposition

For the crossed quark contractions in \(d^\dagger d\) and \(u^\dagger u\), use
\[
T^A_{ab}T^A_{cd}
=\frac12\left(\delta_{ad}\delta_{cb}
-\frac13\delta_{ab}\delta_{cd}\right).
\]
For example,
\[
(\bar Q_a\Gamma Q_b)(\bar d_b\Gamma d_a)
=\frac13(\bar Q\Gamma Q)(\bar d\Gamma d)
+2(\bar QT^A\Gamma Q)(\bar dT^A\Gamma d).
\]
The same identity applies to the corresponding \(u_R\) current. The \(d^\dagger u\) scalar/tensor channels also retain crossed color labels after spinor Fierz; their color decomposition must be applied to the rearranged bilinears, not before the spinor-index exchange.

The color decomposition is independent of the spinor Fierz identity. The weak \(\epsilon_{ik}\) contraction and all generation/Yukawa tensors remain attached to their displayed bilinears.


## 6. Derivative labels and d-dimensional Fierz differences

The source-square operator has four product-rule placements for each ordered source pair. The derivative-aware map through the crossed spinor pairing, including the two placements in which both derivatives land in one Fierz-rearranged bilinear, is given in [RC-001-QLD8-derivative-Fierz-IBP-ledger.md](RC-001-QLD8-derivative-Fierz-IBP-ledger.md).

The evanescent differences \(E_{RL}^{(rs)},E_{LR}^{(rs)},E_{RR}^{(rs)},E_{LL}^{(rs)}\) are defined by applying the fixed Fierz-difference convention to each placement, with derivatives remaining on their original fermion fields. The exact covariant-IBP relation applies to the complete source-pair sum, not to each placement separately. This remains an algebraic tree-level reduction; no one-loop evanescent mixing or finite matching is claimed.


## 7. Beyond scalar-pair Fierz: EOM-generated vector and tensor structures

The second-order fermion EOM generates \(\gamma^\mu D_\mu H\) and \(\sigma^{\mu\nu}\mathscr F_{\mu\nu}\) spinor structures. Their exact four-dimensional chiral Fierz projections, including Levi-Civita and self-dual tensor terms, are recorded in [RC-001-QLD-EOM-generated-chiral-Fierz-identities.md](RC-001-QLD-EOM-generated-chiral-Fierz-identities.md). The new exact audit verifies 34 identities in 8704/8704 components. The corresponding d-dimensional Fierz differences must be added to the evanescent basis; the original four scalar-pair evanescents alone are not sufficient.
