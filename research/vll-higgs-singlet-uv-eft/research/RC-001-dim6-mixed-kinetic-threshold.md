# RC-001 — \(B-A'\) kinetic mixing: divergent trace and finite heavy-lepton threshold

**Status:** the one-loop transverse two-point function from the stated fermion content is evaluated. This is a gauge-sector threshold result, not the \(O(g^2/M_E^2)\) four-point Wilson-coefficient correction.

## 1. Conventions

Take
\[
\mathcal L_{\rm kin}=-\frac14 B_{\mu\nu}B^{\mu\nu}
-\frac14 X_{\mu\nu}X^{\mu\nu}
-\frac{\chi}{2}B_{\mu\nu}X^{\mu\nu},
\]
where \(X_\mu=A'_\mu\). Define the renormalized transverse two-point form factor by
\[
\Gamma^{(2)\,\mu\nu}_{BX}(q)
=i(q^\mu q^\nu-q^2g^{\mu\nu})
\left[\chi(\mu_R)+\Pi_{YX}(q^2;\mu_R)\right].
\]
Use \(d=4-2\epsilon\),
\[
\Delta_\epsilon=\frac1\epsilon-\gamma_E+\ln4\pi,\qquad
L_\ell=\ln\frac{M_{E_\ell}^2}{\mu_R^2}.
\]
The normalized charges are \(Q_X=xQ_\ell\), with \(\eta_\mu=+1\) and \(\eta_\tau=-1\).

For one Dirac fermion of mass \(M\), hypercharge \(Y\), and normalized \(X\)-charge \(x\), the one-loop contribution in this convention is
\[
\Pi_{YX}^{D}(q^2)=
\frac{g_Yg_X Q_\ell}{2\pi^2}Yx
\int_0^1 dz\,z(1-z)
\left[
\Delta_\epsilon-\ln\frac{M^2-z(1-z)q^2-i0}{\mu_R^2}
\right].
\]
At zero momentum,
\[
\Pi_{YX}^{D}(0)=
\frac{g_Yg_X Q_\ell}{12\pi^2}Yx
\left(\Delta_\epsilon-\ln\frac{M^2}{\mu_R^2}\right).
\]

## 2. Divergent trace: cancellation in the complete spectrum

For each flavor, the light lepton doublet contains two Weyl components with \(Y=-1/2,\ x=\eta_\ell\), so
\[
\sum_{L_\ell}Yx=2\left(-\frac12\right)\eta_\ell=-\eta_\ell.
\]
The right-handed charged lepton has \(Y=-1,\ x=-\eta_\ell\), so
\[
Y_{\ell_R}x_{\ell_R}=+\eta_\ell.
\]
Thus the light chiral sector has \(\sum_{\rm Weyl}Yx=0\) flavor by flavor. The complex scalar \(H\) has \(x=0\), and \(S_\ell\) has \(Y=0\), so neither contributes to the additive one-loop \(YX\) trace.

A vector-like Dirac \(E_\ell\) contributes the Dirac weight \((4/3)Yx\) to the divergent gauge-kinetic mixing. Since \(Y_E=-1\) and \(x_E=\eta_\ell\),
\[
\sum_{\ell=\mu,\tau}Y_Ex_E
=-\eta_\mu-\eta_\tau=0.
\]
Therefore the additive one-loop pole proportional to \(\operatorname{Tr}(YX)\) cancels in the full stated spectrum:
\[
\boxed{\left.\Pi_{YX}\right|_{\rm UV\ pole}=0.}
\]
This statement concerns the additive vacuum-polarization divergence. If \(\chi\) is an independent nonzero input, the full kinetic-matrix renormalization and basis convention must still be specified; do not infer \(\chi(\mu_R)=0\).

## 3. Finite heavy threshold

The heavy \(E_\mu,E_\tau\) contributions must be retained separately until their masses are specified. At \(q^2=0\),
\[
\begin{aligned}
\Pi_{YX}^{E}(0)
&=\frac{g_Yg_XQ_\ell}{12\pi^2}
\left[
-\left(\Delta_\epsilon-L_\mu\right)
+\left(\Delta_\epsilon-L_\tau\right)
\right]\\
&=\boxed{\frac{g_Yg_XQ_\ell}{12\pi^2}
\ln\frac{M_{E_\mu}^2}{M_{E_\tau}^2}}.
\end{aligned}
\]
The pole and \(\mu_R\)-dependence cancel between the two heavy flavors. In the stated transverse-kernel convention, matching at zero momentum gives
\[
\boxed{
\chi_{\rm EFT}(\mu_R)=\chi_{\rm UV}(\mu_R)
+\frac{g_Yg_XQ_\ell}{12\pi^2}
\ln\frac{M_{E_\mu}^2}{M_{E_\tau}^2}
}
\]
for the one-loop heavy-fermion threshold, with the same renormalized gauge-coupling and field-basis convention on both sides. If \(M_{E_\mu}=M_{E_\tau}\), this threshold vanishes. If the masses differ, the finite threshold does not vanish merely because the divergent trace cancels.

## 4. Consequence for the four-point matching

The mixed-propagator four-point graphs in the gauge atlas are conditional on the renormalized kinetic matrix. If a nonzero \(\chi\) is an independent tree-level input, a one-loop \(B-A'\) exchange contributes at order \(g_Yg_X\chi\), with the signed pair factor \(Y_i x_j+x_iY_j\) retained.

By contrast, inserting the *one-loop-generated* threshold \(\Pi_{YX}^{E}\) into another one-loop four-point graph is a two-loop effect. The one-loop two-point threshold above must be matched as its own gauge-sector amplitude; it must not be silently used as an order-one tree-level \(\chi\), nor should the conditional mixed-propagator four-point rows be deleted when the input \(\chi\) is nonzero.

The mixed input-parameter counterterm pole sub-block, under the signed propagator convention defined separately, is recorded in [RC-001-dim6-mixed-parameter-counterterms.md](RC-001-dim6-mixed-parameter-counterterms.md). Do not conflate that parameter-renormalization result with this two-point threshold or with the still-open mixed four-point matching.

## 5. Scope boundary

This result fixes the additive \(B-A'\) vacuum-polarization pole and the finite heavy-lepton mass-ratio threshold under the stated charge assignments and sign convention. It does not evaluate the mixed-propagator vertex, self-energy, or crossed-box Wilson-coefficient corrections, and it does not choose the model's renormalized boundary value of \(\chi\). Those entries remain conditional until the input scheme is fixed.
