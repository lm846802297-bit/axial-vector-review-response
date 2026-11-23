# RC-001 — Hard-region heavy-line Yukawa-vertex contributions to \(Q_{LD}\) and \(Q_{RD}\)

**Status:** analytic heavy-line vertex sub-block evaluated in Feynman gauge, including oriented relative signs, charge factors, the \(O(\epsilon)\) numerator term, UV poles, and finite hard pieces. This is **not** the complete gauge-corrected Wilson coefficient: crossed boxes, heavy-line insertions/counterterms in one common organization, EFT contact graphs, and the full Ward-identity/basis sum remain open.

## 1. Target and conventions

The tree-level derivative operators are
\[
Q_{LD,\ell}=(\bar L_\ell H)i\slashed D(H^\dagger L_\ell),\qquad
C_{LD,\ell}=\frac{|y_\ell|^2}{M_{E_\ell}^2},
\]
\[
Q_{RD,\ell}=S_\ell^\ast\bar\ell_R i\slashed D(S_\ell\ell_R),\qquad
C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_{E_\ell}^2}.
\]
The UV interactions are
\[
\mathcal L_{\rm int}\supset
-y_\ell\bar L_\ell H E_{\ell R}
-\lambda_\ell S_\ell\bar E_{\ell L}\ell_R
-M_{E_\ell}\bar E_{\ell L}E_{\ell R}+\mathrm{h.c.}
\]
with \(Y_E=-1\), \(Y_L=-1/2\), \(Y_{\ell_R}=-1\), \(x_E=x_L=\eta_\ell\), \(x_{\ell_R}=-\eta_\ell\), \(x_{S_\ell}=2\eta_\ell\), \(\eta_\mu=+1\), \(\eta_\tau=-1\). The singlet \(E_\ell\) has no \(SU(2)_L\) gauge vertex.

Use Feynman gauge, \(d=4-2\epsilon\), and
\[
\Delta_{\rm UV}=\frac1{\epsilon_{\rm UV}}-\gamma_E+\ln4\pi,\quad
L_\ell=\ln\frac{M_{E_\ell}^2}{\mu_R^2}.
\]
For a mixed \(B-A'\) propagator use the signed coefficient \(\rho_{BX}\), defined so a line pair \(i,j\) contributes
\[
\rho_{BX}g_Yg_XQ_\ell F_{BX}(i,j),\qquad
F_{BX}=Y_i x_j+x_iY_j.
\]
For the Lagrangian convention \(-\chi B_{\mu\nu}X^{\mu\nu}/2\), the linearized convention used elsewhere in RC-001 is \(\rho_{BX}=-\chi+O(\chi^2)\).

## 2. Oriented vertex kernels and signs

There are two genuinely heavy-containing Yukawa-vertex topologies:

1. **Heavy–light fermion exchange (FF):** the gauge boson joins the heavy \(E_\ell\) segment and the light-fermion segment. The projected numerator is
   \[
   N_{\rm FF}=\gamma^\mu\slashed k P_{R,L}\slashed k\gamma_\mu
   =d\,k^2P_{R,L}.
   \]
   The denominator is \(k^2\,k^2(k^2-M_E^2)\); one \(k^2\) cancels, leaving the kernel \(dB_0\).

2. **Heavy–scalar exchange (FS):** the gauge boson joins the heavy \(E_\ell\) segment and the scalar leg. The scalar-gauge vertex supplies the internal momentum; after the chiral projection and symmetric integration, the numerator reduces to \(k^2P_{R,L}\), leaving \(B_0\).

With the all-fields-incoming charge factors \(F_B=Y_iY_j\), \(F_X=x_ix_j\), and \(F_{BX}=Y_ix_j+x_iY_j\) used in the RC-001 charge table, the oriented graph factors for these heavy-containing topologies are \(-F\) times the corresponding scalar kernel. This sign follows from the full oriented Feynman-rule product; it is not inferred from the charge table alone. The conjugate Yukawa vertices give the same real gauge correction. As an internal sign-convention cross-check, the parent research source's general gauge-kernel table in §273.9 gives the corresponding Feynman-gauge structures \(+d\,q_Lq_E B_0\), \(+d\,q_Rq_E B_0\), \(-q_Eq_H B_0\) for the \(\bar LHE_R\) vertex, and \(+q_Eq_S B_0\) for the \(S\bar E_L\ell_R\) vertex. Translating those oriented line charges to the all-incoming \(F\) factors reproduces \(-F\) for the rows above. This is a convention cross-check against the existing analytic record, not an independent diagram-package validation.

The scalar kernels are
\[
B_0(0;0,M_E^2)=\Delta_{\rm UV}+1-L_\ell,
\]
\[
dB_0=(4-2\epsilon)B_0
=4\Delta_{\rm UV}+2-4L_\ell+O(\epsilon).
\]
The finite \(+2\) in the second line retains \((-2\epsilon)(1/\epsilon)=-2\).

These are the hard-region kernels for the local Yukawa-vertex form factor, which multiplies the derivative structure supplied by the other tree-level heavy propagator. The light-only fermion–scalar exchange is excluded from the hard sub-block: it must be kept in the common UV/EFT soft and contact bookkeeping, where it cancels under the conditions recorded in the subtraction ledger.

## 3. Charge factors at both conjugate vertices

The entries below are the charge products in the declared all-incoming convention. Each pair has the same factor at the conjugate vertex.

| Operator | Pair | \(F_B\) | \(F_X\) | \(F_{BX}\) |
|---|---|---:|---:|---:|
| \(Q_{LD}\), \(y_\ell\) and \(y_\ell^\ast\) | FF: \(\bar L-E_R\) / \(\bar E_R-L\) | \(-1/2\) | \(-1\) | \(+3\eta_\ell/2\) |
| \(Q_{LD}\), \(y_\ell\) and \(y_\ell^\ast\) | FS: \(H-E_R\) / \(\bar E_R-H^\dagger\) | \(-1/2\) | \(0\) | \(+\eta_\ell/2\) |
| \(Q_{RD}\), \(\lambda_\ell\) and \(\lambda_\ell^\ast\) | FF: \(\bar E_L-\ell_R\) / \(\bar\ell_R-E_L\) | \(-1\) | \(+1\) | \(0\) |
| \(Q_{RD}\), \(\lambda_\ell\) and \(\lambda_\ell^\ast\) | FS: \(S_\ell-\bar E_L\) / \(S_\ell^\ast-E_L\) | \(0\) | \(-2\) | \(+2\eta_\ell\) |

There is no \(W^I\) contribution to these hard vertex topologies because the heavy \(E_\ell\) is an \(SU(2)_L\) singlet. This does not remove \(W\)-exchange boxes or other EFT operator contributions from the full \(Q_{LD}\) matching.

## 4. One-vertex hard factors

Define the dimensionless correction \(v\) by
\[
\frac{\mathcal V^{(1)}_{\rm hard}}{\mathcal V^{(0)}}
=\frac{1}{16\pi^2}
\left[g_Y^2v_B+g_X^2Q_\ell^2v_X+
\rho_{BX}g_Yg_XQ_\ell v_{BX}\right].
\]
For each gauge structure, the numerator-reduced expression is
\[
v=-\left(F_{\rm FF}\,dB_0+F_{\rm FS}\,B_0\right).
\]

### \(Q_{LD}\) Yukawa vertex

\[
\boxed{v_{LD,B}=\frac52\Delta_{\rm UV}+\frac32-\frac52L_\ell,}
\]
\[
\boxed{v_{LD,X}=4\Delta_{\rm UV}+2-4L_\ell,}
\]
\[
\boxed{v_{LD,BX}=-\frac{13}{2}\eta_\ell\Delta_{\rm UV}
-\frac72\eta_\ell+\frac{13}{2}\eta_\ell L_\ell.}
\]

### \(Q_{RD}\) Yukawa vertex

\[
\boxed{v_{RD,B}=4\Delta_{\rm UV}+2-4L_\ell,}
\]
\[
\boxed{v_{RD,X}=-2\Delta_{\rm UV}+2L_\ell,}
\]
\[
\boxed{v_{RD,BX}=-2\eta_\ell\Delta_{\rm UV}
-2\eta_\ell+2\eta_\ell L_\ell.}
\]

The \(Q_{RD}\) pure-\(X\) finite constant cancels between its FF and FS vertex graphs at \(\mu_R=M_E\); its pole and logarithm do not cancel in this vertex-only sub-block.

## 5. Contribution of both conjugate vertices to the tree coefficients

Because the two conjugate Yukawa vertices carry the same real gauge correction, the vertex-only contribution to \(C\) is twice the one-vertex factor. Before adding self-energy, box, counterterm, and EFT contact contributions,
\[
\boxed{\begin{aligned}
\left.\frac{\delta C_{LD,\ell}}{C_{LD,\ell}}\right|_{\rm heavy\ vertex,hard}
=\frac{1}{16\pi^2}\Big\{&
g_Y^2(5\Delta_{\rm UV}+3-5L_\ell)\\
&+g_X^2Q_\ell^2(8\Delta_{\rm UV}+4-8L_\ell)\\
&+\rho_{BX}g_Yg_XQ_\ell\eta_\ell
(-13\Delta_{\rm UV}-7+13L_\ell)\Big\},
\end{aligned}}
\]
\[
\boxed{\begin{aligned}
\left.\frac{\delta C_{RD,\ell}}{C_{RD,\ell}}\right|_{\rm heavy\ vertex,hard}
=\frac{1}{16\pi^2}\Big\{&
g_Y^2(8\Delta_{\rm UV}+4-8L_\ell)\\
&+g_X^2Q_\ell^2(-4\Delta_{\rm UV}+4L_\ell)\\
&+\rho_{BX}g_Yg_XQ_\ell\eta_\ell
(-4\Delta_{\rm UV}-4+4L_\ell)\Big\}.
\end{aligned}}
\]

At the matching scale \(\mu_R=M_{E_\ell}\), the **finite parts of this vertex sub-block only**, after separating its displayed UV poles, are
\[
\left.\frac{\delta C_{LD,\ell}}{C_{LD,\ell}}\right|_{\rm vertex,finite}
=\frac{3g_Y^2+4g_X^2Q_\ell^2
-7\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2},
\]
\[
\left.\frac{\delta C_{RD,\ell}}{C_{RD,\ell}}\right|_{\rm vertex,finite}
=\frac{4g_Y^2
-4\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2}.
\]
These expressions are not the full Wilson-coefficient corrections. In particular, the displayed poles must not be interpreted as uncanceled physical divergences; the complete amplitude and counterterm organization is still required.

## 6. Independent algebra checks and limitations

The exact-rational checker calculations/RC-001-dim6-heavy-vertex-hard-pieces.py expands \(dB_0\) while retaining the \(O(\epsilon)\) numerator, reproduces all six one-vertex factors, doubles them for the two conjugate vertices, and verifies that the charge factors agree between conjugate orientations for \(\eta_\ell=\pm1\). Its output is recorded in validation/RC-001-dim6-heavy-vertex-hard-pieces.txt.

What is established:
- The Feynman-gauge hard-region numerator kernels, their oriented \(-F\) charge prefactors, and the resulting vertex-only UV poles/logs/finite constants.
- The \(Q_{LD}\) and \(Q_{RD}\) conjugate-vertex sums in the declared \(\overline{\mathrm{MS}}\) convention.

What is **not** established:
- The complete UV–EFT four-point amplitude or the final nonredundant Wilson coefficients.
- The crossed-box sum, full heavy-line counterterm organization, light external-field/contact graphs, operator-counterterm matrix, or summed Ward identity.
- A diagram-package reproduction; the local check is symbolic coefficient algebra, not FeynArts/FeynCalc validation.

## 7. Next calculation

Add the crossed-box hard amplitudes with explicit external momentum routing and Dirac/weak-index projection. Then combine them with the heavy-line self-energy and parameter-counterterm records exactly once, add the EFT contact/soft contributions, and verify the common UV/IR pole table and Ward-identity cancellation before updating any final Wilson coefficient.
