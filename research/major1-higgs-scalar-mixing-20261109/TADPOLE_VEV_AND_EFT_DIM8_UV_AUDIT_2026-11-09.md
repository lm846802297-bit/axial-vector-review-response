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

## 4. Plan-C scale dependence and dimension-eight running

The UV-pole result also fixes the loop-induced running of the dimension-eight coefficient. In the adopted \(d=4-2\epsilon\) convention, the leading pole is
\[
\delta c_8=-\frac{1}{16\pi^2\epsilon}\sum_\ell |C_{5,\ell}|^4,
\]
and the corresponding leading MS mixing term is
\[
\boxed{
\beta_{c_8}^{\rm loop}
=-\frac{2}{16\pi^2}\sum_\ell |C_{5,\ell}|^4 .
}
\]
This is the running induced by the dimension-five fermion operator. The finite matching boundary in the VLL scalar-potential sector is obtained independently from the heavy-eigenstate Coleman--Weinberg expansion in Sec. 5.

The Plan-C finite soft expression already contains the dimension-five contact-tadpole contribution. Combining it with the Plan-C hard derivative, the residual scale derivative at \(s=m_h^2\) is
\[
\frac{d\Pi_{hs}^{\rm soft+hard}}{d\ln\mu}
=2\,\Pi_{hs,\mathrm{EFT5},B}^{\rm UV},
\]
where the right-hand side is the leading-EFT5 mixed local UV coefficient in the adopted Plan-B convention. The \(O_8\) running contributes the opposite derivative.

### Numerical scale-cancellation check

| Quantity | Benchmark A | Benchmark B |
|---|---:|---:|
| Soft derivative \(d\Pi_{hs}^{\rm soft}/d\ln\mu\) [GeV\(^2\)] | \(-7.20196699\times10^{-2}\) | \(-1.62070454\times10^{-2}\) |
| Hard derivative \(d\Pi_{hs}^{\rm hard}/d\ln\mu\) [GeV\(^2\)] | \(+7.21354041\times10^{-2}\) | \(+1.62330898\times10^{-2}\) |
| Total soft + hard derivative [GeV\(^2\)] | \(+1.15734255\times10^{-4}\) | \(+2.60444171\times10^{-5}\) |
| \(2\Pi_{hs,\mathrm{EFT5},B}^{\rm UV}\) [GeV\(^2\)] | \(+1.15734255\times10^{-4}\) | \(+2.60444171\times10^{-5}\) |
| \(\beta_{c_8}^{\rm loop}\) [GeV\(^{-4}\)] | \(-2.17671771\times10^{-17}\) | \(-5.58229779\times10^{-20}\) |
| \(\Delta c_8(20\,\mathrm{TeV}\to125.25\,\mathrm{GeV})\) [GeV\(^{-4}\)] | \(+1.10428716\times10^{-16}\) | \(+2.83199781\times10^{-19}\) |
| \(O_8\)-induced \(\Delta\Pi_{hs}\) [GeV\(^2\)] | \(+5.87140223\times10^{-4}\) | \(+1.32127907\times10^{-4}\) |
| Plan-C soft + hard \(\Delta\Pi_{hs}\) [GeV\(^2\)] | \(-5.87140223\times10^{-4}\) | \(-1.32127907\times10^{-4}\) |
| Residual after \(O_8\) running [GeV\(^2\)] | \(1.01\times10^{-16}\) | \(1.98\times10^{-17}\) |

A symmetric finite-difference derivative in \(\ln\mu\) agrees with the analytic derivative to relative \(5.35\times10^{-8}\) (A) and \(3.37\times10^{-8}\) (B). The residual after including \(O_8\) running is at relative \(1.73\times10^{-13}\) (A) and \(1.50\times10^{-13}\) (B).

This is a nontrivial leading-order scale-consistency check: the remaining Plan-C scale dependence is canceled by the running of the dimension-eight operator, not by reinterpreting the effect as a renormalizable Higgs portal. It does **not** supply the finite hard matching coefficient \(c_8(M_E)\), nor does it constitute the complete gauge- and scalar-sector UV–EFT matching.

## 5. Finite hard matching from the heavy-eigenstate Coleman--Weinberg determinant

For each charged-lepton/VLL block, define the gauge-invariant background variables
\[
X_\ell=|y_\ell|^2 H^\dagger H,\qquad
Y_\ell=|\lambda_\ell|^2 S^\dagger S.
\]
The heavy singular-value squared is
\[
z_{\ell,+}=\frac12\left[
M_E^2+X_\ell+Y_\ell+
\sqrt{(M_E^2+X_\ell+Y_\ell)^2-4X_\ell Y_\ell}
\right].
\]
The light eigenvalue is matched separately to the leading dimension-five EFT loop. The hard potential contribution is the Dirac heavy-eigenstate Coleman--Weinberg term
\[
V_H^{(1)}=-\frac{1}{16\pi^2}\sum_\ell
z_{\ell,+}^2\left[\ln\frac{z_{\ell,+}}{M_E^2}-\frac32\right]
\quad (\mu=M_E).
\]
Expanding in the scalar backgrounds through dimension eight gives
\[
\begin{aligned}
V_H^{(1)}=-\frac{1}{16\pi^2}\sum_\ell\Bigg[
&-\frac32M_E^4-2M_E^2(X_\ell+Y_\ell)+2X_\ell Y_\ell\\
&+\frac{1}{M_E^2}\left(
\frac{(X_\ell+Y_\ell)^3}{3}
-2X_\ell Y_\ell(X_\ell+Y_\ell)\right)\\
&+\frac{1}{M_E^4}\left(
-\frac{(X_\ell+Y_\ell)^4}{12}
+X_\ell Y_\ell(X_\ell+Y_\ell)^2
+2X_\ell^2Y_\ell^2\right)
+O(\mathrm{fields}^{10})\Bigg].
\end{aligned}
\]
The exact heavy-eigenvalue expression and this truncated polynomial agree with the expected fifth-order remainder under a simultaneous rescaling of \(X_\ell,Y_\ell\); this is independently tested at high precision.

### Finite scalar-potential Wilson coefficients at \(\mu=M_E=20\) TeV

The coefficients below multiply the indicated operators in \(V_{\rm EFT}\). They are summed over \(\ell=\mu,\tau\).

| Operator | Dimension | Benchmark A | Benchmark B |
|---|---:|---:|---:|
| \((H^\dagger H)(S^\dagger S)\) | 4 | \(-2.10763976\times10^{-1}\) | \(-1.06733765\times10^{-2}\) |
| \((H^\dagger H)^3\) | 6 | \(-2.42526400\times10^{-11}\) | \(-2.42526400\times10^{-11}\) |
| \((H^\dagger H)^2(S^\dagger S)\) | 6 | \(+3.47656001\times10^{-10}\) | \(+1.76057761\times10^{-11}\) |
| \((H^\dagger H)(S^\dagger S)^2\) | 6 | \(+3.29904905\times10^{-9}\) | \(+8.46057078\times10^{-12}\) |
| \((S^\dagger S)^3\) | 6 | \(-1.04719760\times10^{-8}\) | \(-1.36001900\times10^{-12}\) |
| \((H^\dagger H)^4\) | 8 | \(+2.00024121\times10^{-20}\) | \(+2.00024121\times10^{-20}\) |
| \((H^\dagger H)^3(S^\dagger S)\) | 8 | \(-7.64613237\times10^{-19}\) | \(-3.87210618\times10^{-20}\) |
| \((H^\dagger H)^2(S^\dagger S)^2\) | 8 | \(-3.80925598\times10^{-17}\) | \(-9.76902113\times10^{-20}\) |
| \((H^\dagger H)(S^\dagger S)^3\) | 8 | \(-6.90942609\times10^{-17}\) | \(-8.97342653\times10^{-21}\) |
| \((S^\dagger S)^4\) | 8 | \(+8.22467037\times10^{-17}\) | \(+5.40929021\times10^{-22}\) |

The dimension-six coefficients have units \(\mathrm{GeV}^{-2}\), and the dimension-eight coefficients have units \(\mathrm{GeV}^{-4}\). The dimension-four portal threshold is the previously identified finite VLL threshold; it is not a divergent portal pole.

In particular, the finite matching boundary for the dimension-eight operator is now determined in this restricted VLL scalar-potential basis:
\[
\boxed{
c_8(M_E)
=-\frac{7}{2}\frac{1}{16\pi^2}
\sum_\ell |C_{5,\ell}|^4 .
}
\]
For the two benchmarks,
\[
c_8^A(M_E)=-3.80925598\times10^{-17}\ \mathrm{GeV}^{-4},
\qquad
c_8^B(M_E)=-9.76902113\times10^{-20}\ \mathrm{GeV}^{-4}.
\]
The finite coefficient is \(7/2\) times the magnitude of the UV-pole residue. Its scale dependence,
\[
c_8(\mu)=-\frac{1}{16\pi^2}\sum_\ell |C_{5,\ell}|^4
\left[\frac72-\ln\frac{M_E^2}{\mu^2}\right],
\]
reproduces
\[
\beta_{c_8}=-\frac{2}{16\pi^2}\sum_\ell |C_{5,\ell}|^4,
\]
and therefore agrees with the Plan-C scale-cancellation check in Sec. 4.

This closes the finite hard matching of the VLL-induced scalar-potential operators through dimension eight in the stated background-field/MS scheme. It does not close the derivative-operator basis, the finite tadpole/VEV prescription, or the gauge, Goldstone, ghost, and scalar sectors.

## 6. Local \(h\)-\(s\) curvature from the finite heavy potential

The matched scalar-potential operators also give a definite local mixed curvature at the benchmark vacuum:
\[
\Delta M_{hs,H}^{2}
=\left.\frac{\partial^2 V_H^{(1)}}{\partial h\,\partial s}\right|_{h=s=0}.
\]
For the individual operators, the derivative weights are
\[
\begin{aligned}
(H^\dagger H)(S^\dagger S)&:\quad v_hv_s,\\
(H^\dagger H)^2(S^\dagger S)&:\quad v_h^3v_s,\\
(H^\dagger H)(S^\dagger S)^2&:\quad v_hv_s^3,\\
(H^\dagger H)^3(S^\dagger S)&:\quad \frac34v_h^5v_s,\\
(H^\dagger H)^2(S^\dagger S)^2&:\quad v_h^3v_s^3,\\
(H^\dagger H)(S^\dagger S)^3&:\quad \frac34v_hv_s^5.
\end{aligned}
\]

### Heavy-potential local-curvature decomposition

| Contribution | Benchmark A [GeV\(^2\)] | Benchmark B [GeV\(^2\)] |
|---|---:|---:|
| Dimension-four portal threshold | \(-3.67860356\times10^3\) | \(-8.27819609\times10^2\) |
| Dimension-six operators, sum | \(+6.57195993\times10^{-1}\) | \(+1.47893004\times10^{-1}\) |
| Dimension-eight operators, sum | \(-2.62158187\times10^{-4}\) | \(-5.89951279\times10^{-5}\) |
| Dimension-six plus dimension-eight remainder | \(+6.56933835\times10^{-1}\) | \(+1.47834009\times10^{-1}\) |
| Total heavy-potential curvature before portal cancellation | \(-3.67794663\times10^3\) | \(-8.27671775\times10^2\) |

The dimension-six remainder dominates the dimension-eight correction. Thus, if the finite renormalizable portal threshold is canceled as part of the negligible-portal benchmark, the higher-dimensional heavy-potential terms still leave a local mixed curvature of \(+0.656934\ \mathrm{GeV}^2\) (A) and \(+0.147834\ \mathrm{GeV}^2\) (B).

For reference, an additional finite shift in the renormalizable portal that would cancel this residual **at this particular vacuum** is
\[
\Delta\lambda_{HS}^{\rm extra}
=-\frac{\Delta M_{hs,H}^{2,\ d=6,8}}{v_hv_s}
=
\begin{cases}
-3.76387\times10^{-5},&A,\\
-1.90608\times10^{-6},&B.
\end{cases}
\]
This last quantity is a renormalization-condition diagnostic, not a physical mixing angle or a universal Wilson coefficient. A local zero-mixing condition at one vacuum does not remove the higher-dimensional operators from other amplitudes.

The exact heavy-eigenvalue Coleman--Weinberg derivative and the dimension-eight-truncated potential derivative agree to relative \(2.96\times10^{-11}\) at both benchmarks. The corresponding high-precision regression test is included in the CI suite.

## 7. Consequence for the earlier bubble-only matching subtraction

The archived exact-SVD light-light two-point calculation contains the bubble UV pole, but it does not by itself include the contact generated by the second derivative of the dimension-five mass operator. Therefore its previous full-minus-light-bubble local-mass subtraction is a bubble-only intermediate quantity.

The new leading-EFT5 calculation supplies the missing operator-level structure:
- the \(p^2\) light-bubble pole still requires the corresponding derivative/field counterterm;
- the local \(hs\) pole additionally requires the dimension-five contact contribution;
- the complete leading-EFT5 local divergence is represented by the dimension-eight operator \(O_8\), not by assigning the whole light contribution to a renormalizable \(\lambda_{HS}\) counterterm.

The exact-SVD bubble and leading-EFT5 bubble differ at the \(5\times10^{-4}\) relative level in these benchmarks. This is the finite-\(M_E\) power-correction diagnostic; the two are not silently identified.

## 8. Perturbative-control flag

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

## 9. What is and is not established

Established:
1. The full-theory VLL determinant produces a gauge-invariant renormalizable potential pole with \(\delta\lambda_{HS}=0\) at this order.
2. Its derivatives reproduce the VLL-sector tadpole and local two-point UV poles.
3. The full-theory \(p^2\) poles are canceled by the separately recorded diagonal field counterterms.
4. The leading dimension-five EFT light determinant generates \(O_8=(H^\dagger H)^2(S^\dagger S)^2\).
5. The \(hs\) contact contribution is required to complete the leading-EFT5 local two-point UV pole.

Not established:
- a finite tadpole condition or a physical VEV-renormalization prescription;
- the complete EFT operator basis beyond the scalar-potential operators through dimension eight, including derivative operators and the remaining gauge/scalar sectors;
- gauge, Goldstone, ghost, scalar, and remaining SM contributions;
- complete finite UV–EFT matching beyond the VLL scalar-potential subsector: the finite heavy-VLL scalar-potential coefficients through dimension eight and the leading Plan-C scale cancellation are fixed, but derivative operators and the gauge/scalar sectors remain open;
- the gauge-complete propagator, complex poles, residues, or near-degenerate observables.

The finite portal threshold at \(M_E\) remains distinct from the vanishing full-theory divergent \(\lambda_{HS}\) pole. No manuscript or formal referee-response file is modified by this research record.


## 7. Finite heavy-VLL potential matching through dimension eight

The same scalar-background calculation also isolates the heavy-eigenstate Coleman–Weinberg contribution at \(\mu=M_E=20\) TeV. In the \(\overline{\mathrm{MS}}\) scheme, define
\[
X_\ell=|y_\ell|^2H^\dagger H,\qquad
Y_\ell=|\lambda_\ell|^2S^\dagger S.
\]
The heavy-eigenstate contribution is expanded as
\[
\begin{aligned}
V_H^{(1)}=-\frac{1}{16\pi^2}\sum_\ell\Bigg[
&-\frac32M_E^4-2M_E^2(X_\ell+Y_\ell)+2X_\ell Y_\ell\\
&+\frac{(X_\ell+Y_\ell)^3/3-2X_\ell Y_\ell(X_\ell+Y_\ell)}{M_E^2}\\
&+\frac{-(X_\ell+Y_\ell)^4/12
+X_\ell Y_\ell(X_\ell+Y_\ell)^2+2X_\ell^2Y_\ell^2}{M_E^4}
+\mathcal O(\text{fields}^{10})\Bigg].
\end{aligned}
\]
This gives a finite, scheme- and matching-scale-specific portal threshold and higher-dimensional scalar-potential Wilson coefficients. It does not contradict the vanishing divergent renormalizable portal pole in Section 2: a zero UV pole does not imply a zero finite threshold.

| Heavy-sector finite Wilson coefficient at \(\mu=M_E\) | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Delta\lambda_{HS}^{\rm hard}\) | \(-0.21076398\) | \(-0.01067338\) |
| \(c_{(H^\dagger H)^2(S^\dagger S)}\) [GeV\(^{-2}\)] | \(+3.47656\times10^{-10}\) | \(+1.76058\times10^{-11}\) |
| \(c_{(H^\dagger H)(S^\dagger S)^2}\) [GeV\(^{-2}\)] | \(+3.29905\times10^{-9}\) | \(+8.46057\times10^{-12}\) |
| \(c_{(H^\dagger H)^2(S^\dagger S)^2}^{\rm hard}\) [GeV\(^{-4}\)] | \(-3.80926\times10^{-17}\) | \(-9.76902\times10^{-20}\) |

At the benchmark VEVs, the dimension-six terms shift the local \(hs\) curvature by \(+0.65720\) GeV\(^2\) (A) and \(+0.14789\) GeV\(^2\) (B); the dimension-eight terms contribute \(-2.62158\times10^{-4}\) GeV\(^2\) (A) and \(-5.89951\times10^{-5}\) GeV\(^2\) (B). These are small compared with the hard dimension-four portal contributions, \(-3678.60\) GeV\(^2\) (A) and \(-827.82\) GeV\(^2\) (B), in this selected matching benchmark.

The quoted hard Wilson coefficients are the heavy VLL contribution in the specified \(\overline{\mathrm{MS}}\) scalar-background basis. They are not the complete gauge-, scalar-, Goldstone-, ghost-, and derivative-operator EFT matching coefficients.

## 8. Plan-C scale-dependence check and the role of \(O_8\) running

At \(s=m_h^2\), the scale derivative of the Plan-C hard-plus-soft expression is not zero if the dimension-eight EFT operator is omitted. The residual is precisely the leading \(O_8\) running contribution within the retained VLL/EFT5 sector.

| Scale-derivative diagnostic | Benchmark A [GeV\(^2\)] | Benchmark B [GeV\(^2\)] |
|---|---:|---:|
| Soft derivative \(d\Pi_{hs}^{\rm soft}/d\ln\mu\) | \(-7.20197\times10^{-2}\) | \(-1.62070\times10^{-2}\) |
| Hard derivative \(d\Pi_{hs}^{\rm hard}/d\ln\mu\) | \(+7.21354\times10^{-2}\) | \(+1.62331\times10^{-2}\) |
| Residual before \(O_8\) running | \(+1.15734\times10^{-4}\) | \(+2.60444\times10^{-5}\) |
| Residual after \(O_8\) running | \(1.01\times10^{-16}\) | \(1.98\times10^{-17}\) |
| Relative residual after \(O_8\) running | \(1.72\times10^{-13}\) | \(1.50\times10^{-13}\) |

The leading coefficient obeys
\[
\beta_{c_8}=\frac{dc_8}{d\ln\mu}
=-\frac{2}{16\pi^2}\sum_\ell|C_{5,\ell}|^4.
\]
The corresponding \(O_8\) running cancels the soft-plus-hard scale residual to the numerical precision shown. The analytic scale-derivative identity has relative residuals below \(3.0\times10^{-14}\), and an independent finite-difference check has relative residuals below \(5.4\times10^{-8}\).

**Matching-scope distinction:** the finite heavy-VLL coefficient of \(O_8\) in Section 7 is calculated. The complete EFT boundary coefficient \(c_8(M_E)\), after all hard/soft subtractions and all other UV sectors/operators are consistently included, is not yet established. The running check verifies the cancellation of the retained scale dependence; it does not by itself establish the complete finite matching condition or a physical scalar pole.

