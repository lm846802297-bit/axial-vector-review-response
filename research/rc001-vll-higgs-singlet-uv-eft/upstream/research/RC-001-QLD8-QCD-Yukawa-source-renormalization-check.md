# RC-001 QLD8: QCD renormalization of the Yukawa-weighted Higgs source

**Date:** 2026-11-10  
**Stage:** P1.4a — factorized same-source/wavefunction/Yukawa check  
**Status:** the one-loop QCD renormalization of the Yukawa-weighted source \(J_d\) cancels exactly in \(\overline{\rm MS}\). This gives a nontrivial check on the sum of the two within-source exchange graphs, four external-leg terms, and the SM Yukawa counterterm. It is not the full four-fermion \(Z\) factor.

## 1. Separate the Yukawa spurion from the scalar density

Write
\[
J_d=\bar d_RY_d^\dagger Q_L
=Y_d^\dagger S_d,\qquad
S_d=\bar d_R Q_L.
\]
The color-singlet scalar density \(S_d\) has the same QCD renormalization as the non-singlet scalar quark density. The Higgs field is a QCD singlet, so the QCD part of the SM Yukawa renormalization is the same as the quark-mass renormalization.

Use the convention
\[
Y_{d,0}=Z_{Y_d}Y_d(\mu),\qquad
S_{d,0}=Z_S S_d(\mu),
\]
where the subscript \(0\) denotes bare quantities and the renormalized operator convention is \(S_{d,0}=Z_S S_d\).

At one loop in \(\overline{\rm MS}\),
\[
Z_m=Z_{Y_d}
=1-\frac{3C_Fg_s^2}{16\pi^2\epsilon}
+O(g_s^4),
\]
while the bare scalar density in the convention above has
\[
Z_S=Z_m^{-1}
=1+\frac{3C_Fg_s^2}{16\pi^2\epsilon}
+O(g_s^4).
\]
The relation \(Z_mZ_S=1\) follows from the renormalized mass term
\(m_0S_{d,0}=m(\mu)S_d(\mu)\).

## 2. The Yukawa-weighted source has no factorized QCD pole

Combining the two factors,
\[
\begin{aligned}
J_{d,0}
&=Y_{d,0}^\dagger S_{d,0}\\
&=Z_{Y_d}^\dagger Z_S\,Y_d^\dagger S_d\\
&=J_d+O(g_s^4).
\end{aligned}
\]
Therefore
\[
\boxed{Z_{J_d}^{(s)}=1+O(g_s^4).}
\]
Since the QCD renormalization factor is spacetime independent and \(J_d\) is a color singlet,
\[
D_\mu J_{d,0}=\partial_\mu J_{d,0}
=\partial_\mu J_d+O(g_s^4).
\]
Consequently, the factorized QCD renormalization of the source-square operator,
\[
(D_\mu J_{d,0}^\dagger)(D^\mu J_{d,0}),
\]
also cancels at one loop:
\[
\boxed{Z_{\rm fact}^{(s)}=1+O(g_s^4).}
\]

This cancellation is specific to keeping the renormalized SM Yukawa matrix inside the source, as in the Higgs-EOM definition. If one factors \(Y_d\) out and renormalizes the four-fermion scalar-density product at fixed Yukawa spurion, the scalar-density counterterm \(Z_S^2\) must instead be displayed explicitly; the Yukawa counterterm then cancels it when the physical source is reconstructed.

## 3. Diagrammatic meaning for the \(d^\dagger d\) pilot

The factorized source renormalization consists of:
- the \((\bar Q,d)\) within-source vertex correction;
- the \((\bar d,Q)\) within-source vertex correction;
- all four external-quark wavefunction contributions;
- the QCD counterterm of \(Y_d^\dagger Y_d\).

For each scalar current separately, the within-source vertex plus its two external-leg terms must reproduce the scalar-density renormalization \(Z_S=Z_m^{-1}\). The Yukawa counterterm \(Z_{Y_d}=Z_m\) cancels that factor. This is a stringent sign and normalization check for the explicit Feynman-gauge diagram calculation.

In the direct color basis, the two within-source exchange matrices act on the tree singlet vector as
\[
M_{\bar Q,d}^{(d)}\binom10
=M_{Q,\bar d}^{(d)}\binom10
=-C_F\binom10.
\]
The remaining QCD renormalization of the full source-square four-point function comes from the four cross-source exchange topologies and their mixing into the direct singlet/octet and derivative-correlated operator basis. Those contributions are not canceled by the factorized source identity.

## 4. Scope and bookkeeping convention

For the QLD8 QCD pilot, retain \(Y_d\) as the renormalized SM Yukawa spurion inside \(J_d\). Then:
1. group the two within-source vertex corrections with all four external-leg self-energies;
2. add the \(Y_d\) Yukawa counterterm;
3. verify that this complete factorized subset has zero net QCD pole in \(J_d\);
4. calculate the four cross-source exchange graphs separately in the direct color/spinor basis.

Do not count the scalar-density factor \(Z_S^2\) and the Yukawa factor \(Z_{Y_d}^2\) twice. Conversely, if the calculation is temporarily organized at fixed \(Y_d\), keep \(Z_S^2\) explicit and restore the Yukawa counterterm before quoting the source-square result.

This identity does not determine the full QLD8 counterterm matrix, the cross-source mixing, the EOM/IBP quotient, or any finite UV-minus-EFT Wilson coefficient. It does not contribute to the PR #69 \(hh,hs,ss\) scalar two-point functions.
