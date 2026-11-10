# B5-2B1 — diagonal-gauge parameter running and tree-level current-basis map

**Date:** 2026-11-11  
**Parent:** B5-2B, dimension-six EFT operator running and mixing.  
**Status:** the diagonal-gauge UV parameter-pole sub-block for \(C_5,C_{LD},C_{RD}\) is derived and independently checked against the existing \(C_{LD}/C_{RD}\) counterterm ledger. The tree-level \(Q_{LD},Q_{RD}\) EOM/current-basis map is derived with explicit Pauli-matrix normalization. This is **not** the complete gauge-loop UV–EFT matching or the full operator anomalous-dimension matrix.

## 1. Flavor orientation is part of the operator basis

The dimension-five operators use
\[
S_\mu=S,\qquad S_\tau=S^\ast,\qquad
\eta_\mu=+1,\quad \eta_\tau=-1.
\]
For a flavor-specific singlet current define
\[
J_{S_\ell}^{\mu}
=S_\ell^\dagger i\overleftrightarrow D^\mu S_\ell,
\qquad
J_S^\mu=S^\dagger i\overleftrightarrow D^\mu S.
\]
Because \(D_\mu S^\ast=(D_\mu S)^\ast\),
\[
\boxed{J_{S_\ell}^\mu=\eta_\ell J_S^\mu.}
\]
In particular, \(J_{S_\tau}=-J_S\). Thus a coefficient obtained in the \(S_\ell\)-current basis acquires \(\eta_\ell\) when expressed in a common-\(S\) basis.

This orientation factor has now been applied to the \(C_5C_5^\ast\) coefficients of \(O_{LS}\) and \(O_{Se}\) in the B5-2A note, numerical output, and production script. The \(O_{He}\), four-fermion, and \(c_{\partial HS}\) coefficients are orientation-even. The corrected common-\(S\) sums are
\[
\begin{array}{c|rr}
 & A & B\\ \hline
C_{LS}^{C_5C_5^\ast}(M_E)\ [\mathrm{GeV}^{-2}]
&+9.80994105\times10^{-11}&+4.96788853\times10^{-12}\\
C_{He}^{C_5C_5^\ast}(M_E)\ [\mathrm{GeV}^{-2}]
&+9.87956139\times10^{-11}&+5.00314523\times10^{-12}\\
C_{Se}^{C_5C_5^\ast}(M_E)\ [\mathrm{GeV}^{-2}]
&-1.96198821\times10^{-10}&-9.93577706\times10^{-12}
\end{array}
\]
The \(C_{LS}\) and \(C_{Se}\) signs differ from the previous common-\(S\) sums. The underlying flavor-specific coefficients and \(\kappa_\ell=|C_{5,\ell}|^2/(16\pi^2)\) are unchanged.

## 2. Diagonal-gauge parameter poles

Take \(Q_X(L_\ell)=Q_X(E_\ell)=\eta_\ell Q_\ell\), \(Q_X(\ell_R)=-\eta_\ell Q_\ell\), \(Y_L=-1/2\), \(Y_E=Y_{\ell_R}=-1\), and \(C_2(L)=3/4\), \(C_2(E)=C_2(\ell_R)=0\). The diagonal-gauge sub-block uses \(BB\), \(WW\), and \(A'A'\) propagators, with the mixed \(B-A'\) propagator kept conditional on the kinetic-mixing input.

For a Yukawa coupling between two fermions \(f_L,f_R\), the pure-gauge one-loop pole is
\[
\left.\frac{\delta y}{y}\right|_{\rm gauge}
=-\frac{3}{2}\frac{1}{16\pi^2\epsilon}
\sum_A g_A^2\big[C_A(f_L)+C_A(f_R)\big],
\]
and the vector-like Dirac mass pole is
\[
\left.\frac{\delta M_E}{M_E}\right|_{\rm gauge}
=-\frac{3}{16\pi^2\epsilon}
\sum_A g_A^2 C_A(E).
\]
Therefore
\[
\frac{\delta y_\ell}{y_\ell}
=-\frac{1}{16\pi^2\epsilon}
\left(\frac{15}{8}g_Y^2+\frac98g_2^2+3Q_\ell^2g_X^2\right),
\]
\[
\frac{\delta\lambda_\ell}{\lambda_\ell}
=-\frac{1}{16\pi^2\epsilon}
\left(3g_Y^2+3Q_\ell^2g_X^2\right),
\qquad
\frac{\delta M_{E_\ell}}{M_{E_\ell}}
=-\frac{1}{16\pi^2\epsilon}
\left(3g_Y^2+3Q_\ell^2g_X^2\right).
\]

Using
\[
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}},
\qquad
C_{LD,\ell}=\frac{|y_\ell|^2}{M_{E_\ell}^2},
\qquad
C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_{E_\ell}^2},
\]
the parameter-induced pole residues are
\[
\boxed{
\left.\frac{\delta C_{5,\ell}}{C_{5,\ell}}\right|_{\rm param}
=-\frac{1}{16\pi^2\epsilon}
\left(\frac{15}{8}g_Y^2+\frac98g_2^2+3Q_\ell^2g_X^2\right),
}
\]
\[
\boxed{
\left.\frac{\delta C_{LD,\ell}}{C_{LD,\ell}}\right|_{\rm param}
=\frac{1}{16\pi^2\epsilon}
\left(\frac94g_Y^2-\frac94g_2^2\right),
\qquad
\left.\frac{\delta C_{RD,\ell}}{C_{RD,\ell}}\right|_{\rm param}=0.
}
\]
The \(g_X^2\) terms cancel in the \(C_{LD}\) parameter-only combination because \(L_\ell\) and \(E_\ell\) have equal-magnitude \(X\) charges. The entire diagonal-gauge parameter pole cancels in \(C_{RD}\) because \(\lambda_\ell\) and \(M_E\) have identical gauge pole coefficients.

### 2.1 Gauge-only running implied by these poles

For the dimensionful Wilson coefficients in the four-dimensional limit, twice the simple-pole residue gives the gauge part of the parameter-induced beta function:
\[
\boxed{
16\pi^2\frac{\left.\beta_{C_{5,\ell}}\right|_{\rm param,g}}{C_{5,\ell}}
=-\frac{15}{4}g_Y^2-\frac94g_2^2-6Q_\ell^2g_X^2,
}
\]
\[
\boxed{
16\pi^2\frac{\left.\beta_{C_{LD,\ell}}\right|_{\rm param,g}}{C_{LD,\ell}}
=+\frac92g_Y^2-\frac92g_2^2,
\qquad
\left.\beta_{C_{RD,\ell}}\right|_{\rm param,g}=0.
}
\]
The \(C_5\) result has an independent EFT-side check: the gauge contribution to the Yukawa-type operator \(S_\ell\bar L_\ell H\ell_R\) is
\[
-3\left[
\left(Y_L^2+Y_{\ell_R}^2\right)g_Y^2
+C_2(L)g_2^2
+\left(X_L^2+X_{\ell_R}^2\right)g_X^2
\right],
\]
which reproduces the displayed \(C_5\) coefficient exactly.

These are **parameter-induced gauge pieces**, not the full EFT anomalous dimensions of \(Q_{LD}\), \(Q_{RD}\), or the current operators. In particular, the cancellation of \(g_X^2\) in the \(C_{LD}\) parameter row and the zero \(C_{RD}\) parameter row do not imply that the corresponding gauge-loop amplitudes vanish. The EFT insertion graphs, covariant-derivative contact terms, heavy-line/vertex/box contributions, and common-basis counterterms are still required.

## 3. Tree-level \(Q_{LD}\) and \(Q_{RD}\) current/EOM map

The tree-level derivative operators are
\[
Q_{LD}=(\bar L_\ell H)i\slashed D(H^\dagger L_\ell),
\qquad
Q_{RD}=S_\ell^\ast\bar\ell_R i\slashed D(S_\ell\ell_R).
\]
The following identities are modulo total derivatives. Define Pauli-normalized currents
\[
\begin{aligned}
J_H^{(1)\mu}&=H^\dagger i\overleftrightarrow D^\mu H,
&
J_L^{(1)\mu}&=\bar L_\ell\gamma^\mu L_\ell,\\
J_H^{(3)I\mu}&=H^\dagger i\sigma^I\overleftrightarrow D^\mu H,
&
J_L^{(3)I\mu}&=\bar L_\ell\sigma^I\gamma^\mu L_\ell.
\end{aligned}
\]
Here \(\sigma^I\) are Pauli matrices, not \(SU(2)\) generators \(\sigma^I/2\).

Symmetrizing the composite-fermion kinetic form,
\[
\Psi_L=H^\dagger L_\ell,\qquad
Q_{LD}=\Psi_L^\dagger i\slashed D\Psi_L
\doteq \frac{i}{2}\left[
\Psi_L^\dagger\gamma^\mu D_\mu\Psi_L
-(D_\mu\Psi_L^\dagger)\gamma^\mu\Psi_L
\right],
\]
and applying the exact \(2\times2\) Pauli completeness identities gives
\[
\boxed{
\begin{aligned}
Q_{LD}\doteq{}&
-\frac14J_H^{(1)}\!\cdot J_L^{(1)}
-\frac14J_H^{(3)I}\!\cdot J_L^{(3)I}\\
&+\frac14(H^\dagger H)
  \big(\bar L_\ell i\overleftrightarrow{\slashed D}L_\ell\big)\\
&+\frac14(H^\dagger\sigma^I H)
  \big(\bar L_\ell\sigma^I i\overleftrightarrow{\slashed D}L_\ell\big).
\end{aligned}
}
\]
Thus, in this Pauli-current normalization, the tree-level current coefficients are
\[
C_{HL}^{(1)}=-\frac14C_{LD,\ell},
\qquad
C_{HL}^{(3)}=-\frac14C_{LD,\ell},
\]
before the fermion-EOM terms are reduced. If instead both triplet currents are defined with \(T^I=\sigma^I/2\), their product is \(1/4\) of the Pauli-current product, and the coefficient of that \(T^I\)-normalized triplet operator is \(-C_{LD,\ell}\).

For the singlet,
\[
\boxed{
Q_{RD}\doteq
+\frac12
(S_\ell^\dagger i\overleftrightarrow D_\mu S_\ell)
(\bar\ell_R\gamma^\mu\ell_R)
+\frac12(S_\ell^\dagger S_\ell)
(\bar\ell_R i\overleftrightarrow{\slashed D}\ell_R).
}
\]
Consequently, in the common-\(S\) basis,
\[
\boxed{C_{Se,\ell}^{\rm tree,common}
=+\frac{\eta_\ell}{2}C_{RD,\ell}.}
\]
The \(\mu\) and \(\tau\) tree-level current coefficients therefore have opposite signs when expressed with the same \(S^\dagger i\overleftrightarrow D S\) current.

For the original flavor-diagonal model, the renormalizable \(\mu,\tau\) charged-lepton Yukawa sources vanish. The displayed fermion-EOM terms therefore generate no independent dimension-six Yukawa-source operators for these flavors. Inserting the dimension-five \(C_5\) source instead starts at dimension seven in this reduction and is outside the strict \(M_E^{-2}\) basis.

### 3.1 Numerical tree-level current coefficients

Using the existing \(M_E=20\) TeV, \(\theta_L=10^{-2}\), \(v_S\) benchmarks:
\[
C_{LD,\ell}=3.299007795034\times10^{-9}\ {\rm GeV}^{-2}
\]
for both flavors, so
\[
C_{HL}^{(1)}=C_{HL}^{(3)}
=-8.247519487585\times10^{-10}\ {\rm GeV}^{-2}.
\]
The common-\(S\) singlet-current coefficients from \(Q_{RD}\) are
\[
\begin{array}{c|rr}
 & \mu & \tau\\ \hline
A &+5.5541974420\times10^{-11}&-1.5707963284\times10^{-8}\\
B &+2.8127216713\times10^{-12}&-7.9547277894\times10^{-10}
\end{array}
\quad {\rm GeV}^{-2}.
\]
These are tree-level EOM-basis coefficients. They must be kept distinct from the one-loop \(C_5C_5^\ast\) hard-current coefficients in B5-2A, although both contribute to the same common operator \(O_{Se}\).

## 4. Perturbative-order and matching boundary

The present block contains:
1. Tree-level \(Q_{LD},Q_{RD}\) matching and their EOM/current-basis images.
2. One-loop diagonal-gauge parameter renormalization of \(y_\ell,\lambda_\ell,M_E\), hence the parameter-induced running of \(C_5,C_{LD},C_{RD}\).
3. The already evaluated one-loop \(C_5C_5^\ast\) current/four-fermion hard subset, with the corrected \(\eta_\ell\) orientation factors.

It does **not** contain gauge dressing of the already one-loop \(C_5C_5^\ast\) current coefficients; that would be a higher-loop correction. The missing one-loop gauge matching at \(O(g^2/M_E^2)\) is instead the UV/EFT correction to the tree-level \(Q_{LD},Q_{RD}\) amplitudes and their current form factors.

The mixed \(B-A'\) propagator and its parameter counterterms are not included in this diagonal sub-block. They remain conditional on the declared kinetic-mixing matrix/boundary. No finite \(O(g^2/M_E^2)\) coefficient is inferred from a parameter pole alone.

## 5. Acceptance boundary and next calculation

**Passed in this sub-block**
- Exact rational combination of the \(y,\lambda,M_E\) gauge poles into \(C_5,C_{LD},C_{RD}\).
- Independent EFT Casimir reproduction of the \(C_5\) gauge coefficient.
- Exact Pauli singlet/triplet decomposition of \(Q_{LD}\).
- Exact conjugate-current identity \(J_{S^\ast}=-J_S\).
- Common-\(S\) tree-current coefficients for benchmarks A/B.
- Regression tests are recorded in test_b5_2b_gauge_current_subblock.py.

**Still open**
- The complete UV one-loop gauge vertex, heavy-line, crossed-box, and scalar-line amplitudes for \(Q_{LD},Q_{RD}\).
- The EFT insertion diagrams, including \(B,A'\) covariant-derivative contact terms and the \(W\) external-doublet attachments.
- UV/IR pole separation with common nonexceptional external momenta, counterterms, and Ward/Slavnov–Taylor completion.
- The one-gauge-field current form factors and local-versus-reducible current-exchange separation.
- The weak singlet/triplet projection of the full loop amplitudes, followed by EOM/IBP/Fierz reduction exactly once.
- Conditional mixed \(B-A'\) contributions and the full common-basis anomalous-dimension matrix.

The next integral task is the diagonal \(BB\) and \(WW\) \(Q_{LD}\) sector in the declared Feynman-gauge setup, with the \(A'A'\) \(Q_{LD}\) sector and the \(BB/A'A'\) \(Q_{RD}\) sectors kept as separate charge blocks. The existing atlas is an attachment-class census only; no individual graph coefficient is promoted until the complete UV-minus-EFT amplitude and its Ward identity are assembled.
