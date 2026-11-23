# RC-001 — Conditional \(B-A'\) contribution to UV input-parameter counterterms

**Status:** analytic parameter-renormalization sub-block derived under an explicit off-diagonal propagator convention. It is not the complete mixed-gauge UV–EFT matching pole, and it does not fix the renormalized kinetic-mixing boundary condition.

## 1. Kinetic and propagator convention

Take
\[
\mathcal L_{\rm kin}\supset
-\frac14 B_{\mu\nu}B^{\mu\nu}
-\frac14 X_{\mu\nu}X^{\mu\nu}
-\frac{\chi}{2}B_{\mu\nu}X^{\mu\nu},\qquad X_\mu=A'_\mu.
\]
To first order in \(\chi\), the inverse kinetic matrix gives an off-diagonal propagator coefficient \(\rho_{BX}=-\chi\) relative to the diagonal propagator. Define \(\rho_{BX}\) by the line-pair exchange factor
\[
g_Y^2Y_iY_j+g_X^2Q_\ell^2x_ix_j
+\rho_{BX}g_Yg_XQ_\ell(Y_ix_j+x_iY_j).
\]
Thus \(\rho_{BX}\) is a signed propagator coefficient, not the Lagrangian parameter \(\chi\). All displayed mixed terms are first order in \(\rho_{BX}\).

## 2. Parameter-counterterm formulas

In the stated \(\overline{\mathrm{MS}}\) convention, the pure-gauge Yukawa and vector-like mass poles are
\[
\left.\frac{\delta y}{y}\right|_{\rm gauge}
=-\frac{3}{2}\frac{q_L^2+q_R^2}{16\pi^2\epsilon},\qquad
\frac{\delta M_E}{M_E}
=-3\frac{q_E^2}{16\pi^2\epsilon},
\]
where \(q_f^2\) denotes the full quadratic gauge-coupling form induced by the propagator metric. Its mixed piece is
\[
\left.q_f^2\right|_{BX}
=2\rho_{BX}g_Yg_XQ_\ell\,Y_fx_f.
\]
Consequently,
\[
\left.\frac{\delta y}{y}\right|_{BX}
=-\frac{3\rho_{BX}g_Yg_XQ_\ell}{16\pi^2\epsilon}
\left(Y_Lx_L+Y_Ex_E\right),
\]
with the corresponding replacement \(L,E\to E,\ell_R\) for \(\lambda_\ell\).

For the two tree coefficients \(C_{LD}=|y_\ell|^2/M_E^2\) and \(C_{RD}=|\lambda_\ell|^2/M_E^2\), the parameter-induced contribution is \(2\delta y/y-2\delta M_E/M_E\) or \(2\delta\lambda/\lambda-2\delta M_E/M_E\), respectively.

## 3. \(Q_{LD}\) parameter-induced mixed pole

Use \(Y_L=-1/2,\ x_L=\eta_\ell,\ Y_E=-1,\ x_E=\eta_\ell\). Then
\[
Y_Lx_L+Y_Ex_E=-\frac32\eta_\ell,\qquad
Y_Ex_E=-\eta_\ell.
\]
It follows that
\[
\left.\frac{\delta y_\ell}{y_\ell}\right|_{BX}
=+\frac92\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon},
\qquad
\left.\frac{\delta M_E}{M_E}\right|_{BX}
=+6\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon}.
\]
Hence the **parameter-induced sub-block only** is
\[
\boxed{
\left.\frac{\delta C_{LD}}{C_{LD}}\right|_{BX,\mathrm{parameter}}
=-3\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon}.
}
\]

## 4. \(Q_{RD}\) parameter-induced mixed pole

For \(Y_E=Y_{\ell_R}=-1,\ x_E=\eta_\ell,\ x_{\ell_R}=-\eta_\ell\),
\[
Y_Ex_E+Y_{\ell_R}x_{\ell_R}=0,\qquad
Y_Ex_E=-\eta_\ell.
\]
The mixed term in the \(\lambda_\ell\) Yukawa counterterm therefore vanishes, but the heavy mass counterterm does not:
\[
\left.\frac{\delta\lambda_\ell}{\lambda_\ell}\right|_{BX}=0,\qquad
\left.\frac{\delta M_E}{M_E}\right|_{BX}
=+6\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon}.
\]
Thus
\[
\boxed{
\left.\frac{\delta C_{RD}}{C_{RD}}\right|_{BX,\mathrm{parameter}}
=-12\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon}.
}
\]

With \(\rho_{BX}=-\chi\), these parameter-induced terms have the opposite sign when expressed in terms of the Lagrangian parameter \(\chi\). The \(\mu\) and \(\tau\) contributions are opposite because \(\eta_\mu=+1\) and \(\eta_\tau=-1\).

## 5. Boundary of the result

These formulas are the mixed part of the **UV input-parameter counterterms** for the stated propagator convention. They are not the mixed-gauge contribution to the matched Wilson coefficients. In particular, they do not include the mixed vertex and box amplitudes, the EFT soft graphs and derivative-contact vertices, the operator-counterterm matrix, or the complete Ward-identity sum. They must not be added on top of an equivalent mass/Yukawa counterterm contribution already included in a graph-level ledger row.

The finite \(B-A'\) two-point threshold is a separate result in `research/RC-001-dim6-mixed-kinetic-threshold.md`. It does not by itself specify \(\chi(\mu_R)\), and a one-loop-generated threshold inserted into another one-loop graph is a higher-order effect.
