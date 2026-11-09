# VLL tadpole, scalar-potential, and EFT dimension-eight UV audit — 2026-11-09

**Scope:** original charged-lepton plus VLL fermion sector only.  
**Benchmarks:** A: \(v_s=70.886458\) GeV; B: \(v_s=315\) GeV; \(M_E=20\) TeV.  
**Convention:** \(\Gamma_{\mathrm{inv}}=p^2 I-\mathcal M_{\mathrm{loc}}^2+\Pi_{\mathrm{RC}}\), \(\Delta_{\mathrm{UV}}=1/\epsilon-\gamma_E+\ln4\pi\).  
**Status:** full-theory VLL potential poles and leading dimension-five EFT light-loop poles are independently mapped and CI-validated. This is not a complete UV–EFT matching or physical pole calculation.

## 1. Main result

For
\[
H^0=\frac{\phi_h}{\sqrt2},\qquad S=\frac{\phi_s}{\sqrt2},
\]
and the original \(2\times2\) charged-lepton/VLL mass matrix
\[
\mathcal M_\ell(\phi_h,\phi_s)=
\begin{pmatrix}
0&y_\ell\phi_h/\sqrt2\\
\lambda_\ell\phi_s/\sqrt2&M_E
\end{pmatrix},
\]
the exact fermion determinant is controlled by
\[
\begin{aligned}
F(\phi_h,\phi_s)
&=\sum_{\ell=\mu,\tau}
\operatorname{Tr}\!\left[(\mathcal M_\ell^\dagger\mathcal M_\ell)^2\right]\\
&=\sum_{\ell=\mu,\tau}\left[
M_E^4+M_E^2|y_\ell|^2\phi_h^2
+\frac{|y_\ell|^4}{4}\phi_h^4
+M_E^2|\lambda_\ell|^2\phi_s^2
+\frac{|\lambda_\ell|^4}{4}\phi_s^4
\right].
\end{aligned}
\]
There is no \(\phi_h^2\phi_s^2\) term. Consequently,
\[
\frac{\partial^2F}{\partial\phi_h\partial\phi_s}=0,
\]
and the one-loop VLL determinant generates no divergent renormalizable portal counterterm at this order.

The fermion determinant and its potential counterterm are
\[
V_{1,\mathrm{VLL}}^{\mathrm{div}}
=+\frac{\Delta_{\mathrm{UV}}}{16\pi^2}F,
\qquad
\delta V_{\mathrm{VLL}}
=-\frac{\Delta_{\mathrm{UV}}}{16\pi^2}F.
\]
The constant \(M_E^4\) term contributes only to the vacuum-energy counterterm and is irrelevant to the one- and two-point functions below.

## 2. Full-theory renormalizable potential counterterms

Writing
\[
\delta V=
-\delta\mu_H^2 H^\dagger H
-\delta\mu_S^2 S^\dagger S
+\delta\lambda_H(H^\dagger H)^2
+\delta\lambda_S(S^\dagger S)^2
+\delta\lambda_{HS}(H^\dagger H)(S^\dagger S),
\]
the VLL-sector pole coefficients are
\[
\boxed{
\begin{aligned}
\delta\mu_H^2&=
+\frac{2M_E^2}{16\pi^2}\sum_\ell |y_\ell|^2,\\
\delta\mu_S^2&=
+\frac{2M_E^2}{16\pi^2}\sum_\ell |\lambda_\ell|^2,\\
\delta\lambda_H&=
-\frac{1}{16\pi^2}\sum_\ell |y_\ell|^4,\\
\delta\lambda_S&=
-\frac{1}{16\pi^2}\sum_\ell |\lambda_\ell|^4,\\
\delta\lambda_{HS}&=0.
\end{aligned}}
\]
Every coefficient in this report multiplies \(\Delta_{\mathrm{UV}}\).

The separate kinetic counterterms obtained from the \(p^2\) poles are
\[
\delta Z_{HH}=-\frac{1}{16\pi^2}\sum_\ell |y_\ell|^2,\qquad
\delta Z_{SS}=-\frac{1}{16\pi^2}\sum_\ell |\lambda_\ell|^2,\qquad
\delta Z_{HS}=0.
\]
They cancel the full-theory \(p^2\) UV coefficients in the stated inverse-propagator convention.

### Numerical coefficients

| Counterterm coefficient | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\delta\mu_H^2\) [GeV\(^2\)] | \(+1.33703750\times10^7\) | \(+1.33703750\times10^7\) |
| \(\delta\mu_S^2\) [GeV\(^2\)] | \(+6.38870804\times10^7\) | \(+3.23532927\times10^6\) |
| \(\delta\lambda_H\) | \(-2.20544856\times10^{-2}\) | \(-2.20544856\times10^{-2}\) |
| \(\delta\lambda_S\) | \(-1.00001250\) | \(-2.56458041\times10^{-3}\) |
| \(\delta\lambda_{HS}\) | \(0\) | \(0\) |
| \(\delta Z_{HH}\) | \(-1.67129687\times10^{-2}\) | \(-1.67129687\times10^{-2}\) |
| \(\delta Z_{SS}\) | \(-7.98588506\times10^{-2}\) | \(-4.04416159\times10^{-3}\) |
| \(\delta Z_{HS}\) | \(0\) | \(0\) |

### One-point and local two-point poles

The loop 1PI tadpole pole coefficients are
\[
T_h^{(1),\mathrm{UV}}=-\frac{F_h}{16\pi^2}\Delta_{\mathrm{UV}},
\qquad
T_s^{(1),\mathrm{UV}}=-\frac{F_s}{16\pi^2}\Delta_{\mathrm{UV}}.
\]

| Pole coefficient | Benchmark A | Benchmark B |
|---|---:|---:|
| \(T_h^{(1),\mathrm{UV}}\) [GeV\(^3\)] | \(-3.29238293\times10^9\) | \(-3.29238293\times10^9\) |
| \(T_s^{(1),\mathrm{UV}}\) [GeV\(^3\)] | \(-4.52908505\times10^9\) | \(-1.01920888\times10^9\) |
| \(\Pi_{hh,\mathrm{local}}^{\mathrm{UV}}\) [GeV\(^2\)] | \(-1.33743861\times10^7\) | \(-1.33743861\times10^7\) |
| \(\Pi_{hs,\mathrm{local}}^{\mathrm{UV}}\) [GeV\(^2\)] | \(0\) | \(0\) |
| \(\Pi_{ss,\mathrm{local}}^{\mathrm{UV}}\) [GeV\(^2\)] | \(-6.39021553\times10^7\) | \(-3.23609268\times10^6\) |

The derivatives of the gauge-invariant potential counterterm reproduce these one- and two-point coefficients. The largest absolute residual in the archived double-precision cancellation checks is below \(5\times10^{-7}\,\mathrm{GeV}^2\) for the tadpole-per-VEV comparison and below \(8\times10^{-9}\,\mathrm{GeV}^2\) for the local mass matrix.

## 3. Leading dimension-five EFT: the missing contact and dimension-eight operator

Tree-level integration of the heavy VLL gives
\[
\mathcal L_{\mathrm{EFT}}\supset
-C_{5,\ell}(\overline L_\ell H)S\ell_R+\mathrm{h.c.},
\qquad
C_{5,\ell}=\frac{y_\ell\lambda_\ell}{M_E},
\]
so that, for the neutral backgrounds,
\[
m_\ell(\phi_h,\phi_s)
=\frac{C_{5,\ell}}{2}\phi_h\phi_s.
\]
The light-fermion determinant therefore contains
\[
\begin{aligned}
V_{1,\mathrm{EFT5}}^{\mathrm{div}}
&=+\frac{\Delta_{\mathrm{UV}}}{16\pi^2}
\sum_\ell |m_\ell(\phi_h,\phi_s)|^4\\
&=+\frac{\Delta_{\mathrm{UV}}}{16\pi^2}
\sum_\ell |C_{5,\ell}|^4
(H^\dagger H)^2(S^\dagger S)^2.
\end{aligned}
\]
Thus the EFT requires the dimension-eight counterterm
\[
\boxed{
\delta c_8
=-\frac{1}{16\pi^2}\sum_\ell |C_{5,\ell}|^4
}
\]
for \(O_8=(H^\dagger H)^2(S^\dagger S)^2\).

This is not a renormalizable portal counterterm. The distinction matters: the full-theory one-loop VLL determinant has no divergent \(\lambda_{HS}\) term, whereas the dimension-five EFT light loop generates a dimension-eight scalar operator.

For \(F_{\mathrm{EFT5}}=\sum_\ell |m_\ell|^4\), the local UV coefficients split into a light-light bubble and a dimension-five contact contribution:
\[
\begin{array}{lll}
F_{hh}^{\mathrm{EFT5}}=12F_{\mathrm{EFT5}}/v_h^2,
&
F_{hs,\mathrm{bubble}}^{\mathrm{EFT5}}=12F_{\mathrm{EFT5}}/(v_hv_s),
&
F_{hs,\mathrm{contact}}^{\mathrm{EFT5}}=4F_{\mathrm{EFT5}}/(v_hv_s),
\\[2mm]
F_{ss}^{\mathrm{EFT5}}=12F_{\mathrm{EFT5}}/v_s^2.
\end{array}
\]
The \(hs\) contact term is required to obtain the complete mixed two-point UV pole. The bubble alone gives only \(12F/(v_hv_s)\), while the full second derivative is \(16F/(v_hv_s)\).

### EFT numerical coefficients

| Quantity | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\delta c_8\) [GeV\(^{-4}\)] | \(-1.08835885\times10^{-17}\) | \(-2.79114889\times10^{-20}\) |
| EFT \(T_h^{(1),\mathrm{UV}}\) [GeV\(^3\)] | \(-1.02549892\times10^{-3}\) | \(-1.02549892\times10^{-3}\) |
| EFT \(T_s^{(1),\mathrm{UV}}\) [GeV\(^3\)] | \(-3.56201103\times10^{-3}\) | \(-8.01582048\times10^{-4}\) |
| EFT \(\Pi_{hh,\mathrm{local}}^{\mathrm{UV}}\) [GeV\(^2\)] | \(-1.24949101\times10^{-5}\) | \(-1.24949101\times10^{-5}\) |
| EFT \(\Pi_{hs,\mathrm{local}}^{\mathrm{UV}}\) [GeV\(^2\)] | \(-5.78671274\times10^{-5}\) | \(-1.30222086\times10^{-5}\) |
| EFT \(\Pi_{ss,\mathrm{local}}^{\mathrm{UV}}\) [GeV\(^2\)] | \(-1.50748583\times10^{-4}\) | \(-7.63411475\times10^{-6}\) |

The mixed contact pieces in the coefficient of \(F_{hs}\) are
\[
A:\ 2.28450262\times10^{-3}\ \mathrm{GeV}^2,\qquad
B:\ 5.14096188\times10^{-4}\ \mathrm{GeV}^2.
\]
They are additional to the bubble contributions, not an alternative estimate of them.

## 4. Consequence for the earlier bubble-only matching subtraction

The archived exact-SVD light-light two-point calculation contains the bubble UV pole, but it does not by itself include the contact generated by the second derivative of the dimension-five mass operator. Therefore its previous full-minus-light-bubble local-mass subtraction is a bubble-only intermediate quantity.

The new leading-EFT5 calculation supplies the missing operator-level structure:
- the \(p^2\) light-bubble pole still requires the corresponding derivative/field counterterm;
- the local \(hs\) pole additionally requires the dimension-five contact contribution;
- the complete leading-EFT5 local divergence is represented by the dimension-eight operator \(O_8\), not by assigning the whole light contribution to a renormalizable \(\lambda_{HS}\) counterterm.

The exact-SVD bubble and leading-EFT5 bubble differ at the \(5\times10^{-4}\) relative level in these benchmarks. This is the finite-\(M_E\) power-correction diagnostic; the two are not silently identified.

## 5. Perturbative-control flag

For Benchmark A, \(\lambda_\tau=3.5449077\) and
\[
\frac{|\lambda_\tau|^2}{4\pi}=1.0000,\qquad
\frac{|\lambda_\tau|^4}{16\pi^2}=1.0000.
\]
The VLL contribution to the \(\lambda_S\) pole coefficient is therefore of order one. This point sits at the adopted Yukawa perturbativity boundary, so finite one-loop corrections and scale dependence require particular caution; the pole coefficient is not itself a finite correction or an exclusion.

For Benchmark B, \(\lambda_\tau=0.7977332\),
\[
\frac{|\lambda_\tau|^2}{4\pi}=0.05064,\qquad
\frac{|\lambda_\tau|^4}{16\pi^2}=0.002565.
\]
The VLL-sector quartic pole coefficient is much smaller at this benchmark.

## 6. What is and is not established

Established:
1. The full-theory VLL determinant produces a gauge-invariant renormalizable potential pole with \(\delta\lambda_{HS}=0\) at this order.
2. Its derivatives reproduce the VLL-sector tadpole and local two-point UV poles.
3. The full-theory \(p^2\) poles are canceled by the separately recorded diagonal field counterterms.
4. The leading dimension-five EFT light determinant generates \(O_8=(H^\dagger H)^2(S^\dagger S)^2\).
5. The \(hs\) contact contribution is required to complete the leading-EFT5 local two-point UV pole.

Not established:
- a finite tadpole condition or a physical VEV-renormalization prescription;
- the complete same-order EFT operator and counterterm basis beyond this leading light determinant;
- gauge, Goldstone, ghost, scalar, and remaining SM contributions;
- complete finite hard-plus-soft UV–EFT matching or matching-scale cancellation;
- the gauge-complete propagator, complex poles, residues, or near-degenerate observables.

The finite portal threshold at \(M_E\) remains distinct from the vanishing full-theory divergent \(\lambda_{HS}\) pole. No manuscript or formal referee-response file is modified by this research record.
