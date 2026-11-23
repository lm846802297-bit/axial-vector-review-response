# RC-001 — Gauge contribution from UV input-parameter counterterms

**Scope:** a partial analytic sub-block only. This note derives the diagonal-gauge \(\overline{\mathrm{MS}}\) pole contribution induced by renormalizing \(y_\ell,\lambda_\ell,M_{E_\ell}\) in the tree coefficients \(C_{LD}=|y_\ell|^2/M_E^2\) and \(C_{RD}=|\lambda_\ell|^2/M_E^2\). It is **not** the complete UV–EFT matching pole and contains no finite hard matching coefficient. Off-diagonal \(B-A'\) kinetic-mixing counterterms are not included in this diagonal-only calculation. A separate, explicitly convention-bound parameter-only sub-block is now recorded in [RC-001-dim6-mixed-parameter-counterterms.md](RC-001-dim6-mixed-parameter-counterterms.md); it does not replace the full mixed-gauge UV–EFT amplitude.

## 1. Conventions and input

Use \(d=4-2\epsilon\), unbroken-phase fields, and the \(\overline{\mathrm{MS}}\) pole convention. Hypercharge is normalized by \(Y_H=+1/2\), and \(Q_X=xQ_\ell\). For this sub-block, take diagonal gauge propagators \(B B\), \(W^I W^I\), and \(A'A'\); keep mixed kinetic propagation and its counterterm as a separate, conditional row.

The two tree-level matching coefficients are
\[
C_{LD,\ell}=\frac{|y_\ell|^2}{M_{E_\ell}^2},\qquad
C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_{E_\ell}^2}.
\]
The gauge-invariant Yukawa interactions relevant here connect \(L_\ell\) to \(E_\ell\) through \(H\), and \(E_\ell\) to \(\ell_R\) through \(S_\ell\).

For a gauge group with fermion quadratic Casimirs \(C_2(f_L),C_2(f_R)\), the one-loop pure-gauge Yukawa counterterm is
\[
\left.\frac{\delta y}{y}\right|_{\rm gauge}
=-\frac{3}{2}\frac{g^2}{16\pi^2\epsilon}
\left[C_2(f_L)+C_2(f_R)\right],
\]
while the vector-like fermion mass counterterm is
\[
\left.\frac{\delta M_E}{M_E}\right|_{\rm gauge}
=-\frac{3g^2}{16\pi^2\epsilon}C_2(E).
\]
For \(U(1)\), replace \(C_2(f)\) by the square of the corresponding charge. These are parameter-renormalization pole terms; the EFT operator counterterm and the graph-level UV–EFT difference are separate contributions.

Because \(C_0=|y_0|^2/M_{E,0}^2\), the parameter-induced pole is
\[
\left.\frac{\delta C}{C}\right|_{y,M}
=2\,\mathrm{Re}\frac{\delta y}{y}
-2\frac{\delta M_E}{M_E}.
\]

## 2. \(Q_{LD}\) parameter-renormalization sub-block

The charges are \(Y_L=-1/2\), \(Y_E=-1\), \(C_2(L)=3/4\), \(C_2(E)=0\), and \(Q_X(L)=Q_X(E)=\eta_\ell Q_\ell\). Therefore
\[
\left.\frac{\delta y_\ell}{y_\ell}\right|_{\rm diag}
=-\frac{1}{16\pi^2\epsilon}
\left(\frac{15}{8}g_Y^2+\frac{9}{8}g_2^2+3Q_\ell^2g_X^2\right),
\]
\[
\left.\frac{\delta M_{E_\ell}}{M_{E_\ell}}\right|_{\rm diag}
=-\frac{1}{16\pi^2\epsilon}
\left(3g_Y^2+3Q_\ell^2g_X^2\right).
\]
Combining these parameter counterterms gives
\[
\boxed{
\left.\frac{\delta C_{LD,\ell}}{C_{LD,\ell}}\right|_{y,M;\,\rm diag}
=\frac{1}{16\pi^2\epsilon}
\left(\frac94 g_Y^2-\frac94 g_2^2+0\cdot g_X^2\right).
}
\]
The \(g_X^2\) term cancels in this *parameter-renormalization sub-block* because \(L_\ell\) and \(E_\ell\) have equal-magnitude \(X\) charges and the same \(X\)-charge contribution appears in the vector-like mass counterterm. This cancellation does **not** imply that the complete \(Q_{LD}\) gauge matching correction or its EFT anomalous dimension vanishes in the \(X\) sector.

## 3. \(Q_{RD}\) parameter-renormalization sub-block

For \(\lambda_\ell\bar E_{\ell L}S_\ell\ell_R\), the fermion charges entering the Yukawa counterterm have \(Y_E=Y_{\ell_R}=-1\), and \(X\) charges \(+\eta_\ell Q_\ell\) and \(-\eta_\ell Q_\ell\). Both fermions are \(SU(2)_L\) singlets. Hence
\[
\left.\frac{\delta\lambda_\ell}{\lambda_\ell}\right|_{\rm diag}
=-\frac{1}{16\pi^2\epsilon}
\left(3g_Y^2+3Q_\ell^2g_X^2\right),
\]
\[
\left.\frac{\delta M_{E_\ell}}{M_{E_\ell}}\right|_{\rm diag}
=-\frac{1}{16\pi^2\epsilon}
\left(3g_Y^2+3Q_\ell^2g_X^2\right),
\]
and therefore
\[
\boxed{
\left.\frac{\delta C_{RD,\ell}}{C_{RD,\ell}}\right|_{\lambda,M;\,\rm diag}=0.
}
\]
Again, this is only the contribution induced by the renormalization of \(\lambda_\ell\) and \(M_E\). It is not a statement that all \(Q_{RD}\) gauge-loop diagrams, EFT contact graphs, operator counterterms, or finite matching terms vanish.

## 4. Boundary of this result

The expressions above supply a known-input-counterterm row for the amplitude ledger. They do not include:

- heavy-line and light-line exchange diagrams;
- vertex and cross-vertex box integrals;
- EFT soft graphs from \(Q_{LD}/Q_{RD}\), including their covariant-derivative contact vertices;
- external-field terms or the EFT operator-mixing counterterm matrix;
- \(B-A'\) mixed propagation, kinetic-mixing renormalization, or its boundary condition;
- the finite hard local polynomial after UV–EFT subtraction;
- Ward-identity, weak-tensor, EOM/source, and current-current projection.

Thus these formulas must be added to the appropriate parameter-counterterm columns, not promoted to the full Wilson-coefficient correction. CI is skipped by explicit project decision; no CI pass is claimed. The remaining graph-level calculation is still open.
