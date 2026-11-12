# Major Point 1 — A4a complete one-loop \(ss\) kernel in the \(U(1)_X\) Abelian-Higgs sector

**Date:** 2026-11-10  
**Scope:** original one-complex-singlet model, \(m_X=2g_Xv_S\), \(\lambda_{HS}^{\rm EFT}(M_E)=0\). This note derives the \(U(1)_X\) vector/Goldstone/ghost contribution to the radial \(ss\) two-point function, adds the singlet-radial scalar loop, and checks its absorptive part against \(s\to A'A'\). It does not yet calculate a complete renormalized complex pole.

## 1. Conventions and quadratic operators

Write
\[
S=\frac{v_S+s+ia}{\sqrt2},\qquad
g_A\equiv 2g_X=\frac{m_X}{v_S},\qquad
m_s^2=2\lambda_Sv_S^2
\]
at the zero-portal tree reference point. The \(R_\xi\) gauge-fixing function is
\[
F_X=\partial_\mu A'^\mu-\xi_Xm_Xa,\qquad
{\cal L}_{\rm GF}=-\frac{F_X^2}{2\xi_X}.
\]
For brevity set \(\xi=\xi_X\) and \(m=m_X\).

Before gauge fixing, the relevant terms from \(|D_\mu S|^2\) are
\[
\frac12(\partial_\mu s)^2+\frac12(\partial_\mu a)^2
+g_A A'^\mu\left[(v_S+s)\partial_\mu a-a\partial_\mu s\right]
+\frac{g_A^2}{2}A'^2\left[(v_S+s)^2+a^2\right].
\]
The \(g_Av_S A'\cdot\partial a\) bilinear is cancelled by \({\cal L}_{\rm GF}\). The remaining interactions relevant to the \(ss\) two-point function are
\[
\begin{aligned}
{\cal L}_{\rm int}\supset{}&
g_A A'^\mu(s\partial_\mu a-a\partial_\mu s)
+g_Am\,s A'_\mu A'^\mu
+\frac{g_A^2}{2}s^2A'_\mu A'^\mu\\
&-\lambda_Sv_Ss a^2-\frac{\lambda_S}{2}s^2a^2
-\lambda_Sv_Ss^3-\frac{\lambda_S}{4}s^4\\
&-\xi\frac{m^2}{v_S}s\,\bar c_Xc_X.
\end{aligned}
\]
The corresponding vertices include
\[
sA'_\mu A'_\nu:\ 2ig_Am\,g_{\mu\nu},\qquad
ssA'_\mu A'_\nu:\ 2ig_A^2g_{\mu\nu},
\]
\[
saa:\ -2i\lambda_Sv_S,\qquad
ssaa:\ -2i\lambda_S,\qquad
s\bar c_Xc_X:\ -i\xi\frac{m^2}{v_S}.
\]
The derivative \(A'sa\) vertex is fixed by the first line; with all momenta incoming it is proportional to \(g_A(p_s-p_a)_\mu\), with the overall \(i\) determined by the Fourier convention.

The quadratic masses are
\[
m_{A'}^2=m^2,\qquad m_a^2=m_{c_X}^2=\xi m^2.
\]

## 2. Diagram census for \(\Pi_{ss}\)

The one-loop bosonic \(ss\) entry contains all of the following:

| Contribution | Internal lines / vertex | Role |
|---|---|---|
| Vector bubble | \(A'A'\), two \(sA'A'\) vertices | Transverse and longitudinal vector modes |
| Vector seagull | \(A'\) tadpole, \(ssA'A'\) | Required quartic gauge vertex |
| Mixed derivative bubble | \(A'a\), two \(A'sa\) vertices | Required by the shifted covariant kinetic term |
| Goldstone bubble | \(aa\), two \(saa\) vertices | \(R_\xi\)-dependent scalar cut |
| Goldstone seagull | \(a\) tadpole, \(ssaa\) | Required scalar quartic |
| Ghost bubble | \(c_X\bar c_X\), two \(s\bar c_Xc_X\) vertices | Complex Grassmann ghost loop |
| Radial bubble | \(ss\), two \(sss\) vertices | Singlet-potential contribution |
| Radial seagull | \(s\) tadpole, \(ssss\) | Singlet-potential contribution |

No \(hs\) vector or ghost bubble is generated: this is a diagonal \(ss\) calculation.

## 3. General-\(R_\xi\) integral representation

Use the Euclidean inverse-propagator convention
\[
\Gamma_E^{(2)}(p_E^2)=p_E^2+m_s^2+\Pi_{ss,E}(p_E^2).
\]
Define
\[
{\cal A}_E(M^2)=16\pi^2\mu^{2\epsilon}
\int\frac{d^dk_E}{(2\pi)^d}\frac1{k_E^2+M^2},
\]
\[
{\cal B}_E(p_E^2;M_1^2,M_2^2)=16\pi^2\mu^{2\epsilon}
\int\frac{d^dk_E}{(2\pi)^d}
\frac1{(k_E^2+M_1^2)((k_E+p_E)^2+M_2^2)},
\]
with \(d=4-2\epsilon\). Their UV poles are
\[
{\cal A}_E(M^2)\big|_{\rm UV}=-\frac{M^2}{\bar\epsilon},
\qquad
{\cal B}_E\big|_{\rm UV}=\frac1{\bar\epsilon}.
\]
The Euclidean vector propagator is
\[
D_{\mu\nu}(k)=
\frac{P^T_{\mu\nu}(k)}{k^2+m^2}
+\frac{\xi P^L_{\mu\nu}(k)}{k^2+\xi m^2},
\quad
P^L_{\mu\nu}=\frac{k_\mu k_\nu}{k^2},\quad
P^T_{\mu\nu}=\delta_{\mu\nu}-P^L_{\mu\nu}.
\]

Writing \(\int_k^\star\equiv16\pi^2\mu^{2\epsilon}\int d^dk/(2\pi)^d\), the complete \(U(1)_X\) vector/Goldstone/ghost subset is
\[
\boxed{\begin{aligned}
16\pi^2\Pi_{ss,E}^{X}(p_E^2)={}&
g_A^2\left[(d-1){\cal A}_E(m^2)+\xi{\cal A}_E(\xi m^2)\right]\\
&-2g_A^2m^2\int_k^\star
D_{\mu\nu}(k)D_{\nu\mu}(k+p_E)\\
&-g_A^2\int_k^\star
\frac{(k-p_E)_\mu D_{\mu\nu}(k+p_E)(k-p_E)_\nu}
{k^2+\xi m^2}\\
&+\lambda_S{\cal A}_E(\xi m^2)\\
&-2\lambda_S^2v_S^2
{\cal B}_E(p_E^2;\xi m^2,\xi m^2)\\
&+\xi^2g_A^2m^2
{\cal B}_E(p_E^2;\xi m^2,\xi m^2).
\end{aligned}}
\]
The terms are, in order: vector seagull, vector bubble, mixed \(A'a\) bubble, Goldstone seagull, Goldstone bubble, and ghost bubble. This expression retains the full transverse/longitudinal propagator and is suitable for a general-\(\xi\) numerical reduction.

The independent radial-scalar contribution is
\[
\boxed{
16\pi^2\Pi_{ss,E}^{\rm radial}(p_E^2)
=3\lambda_S{\cal A}_E(m_s^2)
-18\lambda_S^2v_S^2
{\cal B}_E(p_E^2;m_s^2,m_s^2).
}
\]
The first coefficient is \(6\lambda_S/2\) from the \(ssss\) tadpole; the second is \(-(6\lambda_Sv_S)^2/2\) from the \(sss\) bubble.

## 4. Feynman-gauge reduction to \(A_0/B_0\)

At \(\xi=1\), \(D_{\mu\nu}(k)=\delta_{\mu\nu}/(k^2+m^2)\). The mixed numerator reduces by
\[
(k-p)^2=
2(k^2+m^2)-((k+p)^2+m^2)+2p_E^2-m^2,
\]
so
\[
\int_k^\star
\frac{(k-p)^2}{(k^2+m^2)((k+p)^2+m^2)}
={\cal A}_E(m^2)+(2p_E^2-m^2){\cal B}_E(p_E^2;m^2,m^2).
\]
Combining all vector, mixed, Goldstone and ghost graphs gives the compact result
\[
\boxed{\begin{aligned}
16\pi^2\Pi_{ss,E}^{X,\xi=1}(p_E^2)
={}&\left[(d-1)g_A^2+\lambda_S\right]{\cal A}_E(m_X^2)\\
&-\left[2g_A^2p_E^2
+2(d-1)g_A^2m_X^2
+2\lambda_S^2v_S^2\right]
{\cal B}_E(p_E^2;m_X^2,m_X^2).
\end{aligned}}
\]
Adding the radial contribution from section 3 completes the one-loop bosonic singlet-sector subset at the zero-portal reference point.

The factor \(d-1\) must be retained until the UV subtraction is completed: replacing \(d\) by four too early loses finite terms from \(O(\epsilon)\times1/\epsilon\).

## 5. General-\(\xi\) cancellation checks

Two analytic cancellations are already verified.

### 5.1 Longitudinal vector / ghost tadpole cancellation

The longitudinal-vector contribution to the one-point function is
\[
T_{s,L}^{A'}=+\frac{g_Am_X}{16\pi^2}\xi{\cal A}_E(\xi m_X^2),
\]
while the complex \(U(1)_X\) ghost gives
\[
T_s^{c_X}=-\frac{g_Am_X}{16\pi^2}\xi{\cal A}_E(\xi m_X^2).
\]
They cancel exactly. The remaining one-loop singlet tadpole is
\[
\boxed{
T_s^{(1)}=\frac1{16\pi^2}\left[
(d-1)g_Am_X{\cal A}_E(m_X^2)
+\lambda_Sv_S{\cal A}_E(\xi m_X^2)
+3\lambda_Sv_S{\cal A}_E(m_s^2)
\right].
}
\]
This is the loop tadpole to be combined with the A3b counterterm condition; it must not be added again as a separate mass insertion after the chosen tadpole prescription has absorbed it.

### 5.2 Zero-momentum unphysical-sector cancellation at \(\lambda_S=0\)

At \(p_E=0\), the longitudinal vector seagull, longitudinal vector bubble, ghost bubble and mixed \(A'a\) bubble sum to
\[
\begin{aligned}
&+\xi g_A^2{\cal A}_E(\xi m_X^2)
-2\xi^2g_A^2m_X^2{\cal B}_E(0;\xi m_X^2,\xi m_X^2)\\
&+\xi^2g_A^2m_X^2{\cal B}_E(0;\xi m_X^2,\xi m_X^2)\\
&-\xi g_A^2\left[
{\cal A}_E(\xi m_X^2)
-\xi m_X^2{\cal B}_E(0;\xi m_X^2,\xi m_X^2)
\right]=0.
\end{aligned}
\]
The remaining gauge contribution is exactly the \(d-1\) transverse-vector result. This is an algebraic check of the relative seagull, mixed and ghost coefficients. It is not a claim that the off-shell self-energy is gauge independent for nonzero \(\lambda_S\).

## 6. UV-pole ledger in Feynman gauge

Using the Euclidean pole definitions above, the \(A'\)/Goldstone/ghost subset gives
\[
\boxed{
16\pi^2\Pi_{ss,E}^{X,\rm UV}
=\frac1{\bar\epsilon}
\left[-2g_A^2p_E^2-9g_A^2m_X^2
-\lambda_Sm_X^2-2\lambda_S^2v_S^2\right].
}
\]
The radial-scalar subset gives
\[
16\pi^2\Pi_{ss,E}^{\rm radial,UV}
=\frac1{\bar\epsilon}
\left[-3\lambda_Sm_s^2-18\lambda_S^2v_S^2\right]
=-\frac{24\lambda_S^2v_S^2}{\bar\epsilon},
\]
where \(m_s^2=2\lambda_Sv_S^2\) is used in the last equality.

Thus the complete singlet-bosonic UV pole in this Feynman-gauge subset is
\[
\boxed{
16\pi^2\Pi_{ss,E}^{\rm bos,UV}
=\frac1{\bar\epsilon}
\left[-2g_A^2p_E^2-9g_A^2m_X^2
-\lambda_Sm_X^2-26\lambda_S^2v_S^2\right].
}
\]
The \(p_E^2\) pole fixes the corresponding diagonal field-counterterm requirement. The remaining local poles must be combined with \(\delta\mu_S^2,\delta\lambda_S,\delta v_S\) and the tadpole prescription. This is not yet the full UV counterterm after including the VLL/lepton sector and matching subtraction.

## 7. Optical-theorem validation in Feynman gauge

At \(p^2=m_s^2\), define \(x=m_X^2/m_s^2\) and \(\beta=\sqrt{1-4x}\). The imaginary parts of the four gauge-fixed two-particle cuts have the following coefficients, multiplying \(\pi\beta/(16\pi^2)\):
\[
\begin{array}{c|c}
\text{cut}&C_i\\ \hline
A'A'\text{ vector bubble}&-8g_A^2m_X^2\\
A'a\text{ mixed derivative bubble}&g_A^2(2m_s^2+m_X^2)\\
c_X\bar c_X\text{ ghost bubble}&g_A^2m_X^2\\
aa\text{ Goldstone bubble}&-2\lambda_S^2v_S^2
\end{array}
\]
Using \(g_A=m_X/v_S\) and \(\lambda_S=m_s^2/(2v_S^2)\), their sum is
\[
\boxed{
C_{\rm sum}
=-\frac{m_s^4}{2v_S^2}
(1-4x+12x^2).
}
\]
With the stated Euclidean continuation convention,
\[
-\frac{\operatorname{Im}\Pi_{ss,E}(-m_s^2-i0)}{m_s}
=
\frac{m_s^3}{32\pi v_S^2}
(1-4x+12x^2)\sqrt{1-4x}.
\]
This is exactly the tree-level physical width
\[
\boxed{
\Gamma(s\to A'A')
=\frac{m_s^3}{32\pi v_S^2}
(1-4x+12x^2)\sqrt{1-4x}.
}
\]
The Goldstone, ghost, mixed and vector pieces are not individually physical. Their complete sum reproduces the three-polarization massive-vector result. The radial \(ss\) bubble has no cut at \(p^2=m_s^2\), since its threshold is \(2m_s\).

## 8. Benchmark numerical cross-check

The two established benchmarks are
\[
(A):\quad v_S=70.886458~{\rm GeV},\quad m_X=10~{\rm GeV},
\]
\[
(B):\quad v_S=315~{\rm GeV},\quad m_X=63~{\rm GeV}.
\]
The cut-derived width and the direct two-body width agree to relative residuals below \(3\times10^{-16}\) at every open-channel point.

| \(m_s\) [GeV] | A: \(\Gamma_{A'A'}\) [GeV] | B: \(\Gamma_{A'A'}\) [GeV] |
|---:|---:|---:|
| 10 | 0 (closed) | 0 (closed) |
| 100 | 1.86433080 | 0 (closed) |
| 125.25 | 3.74367566 | 0 (closed; \(2m_X=126\) GeV) |
| 150 | 6.50529209 | 0.12259434 |

At the perturbativity ceilings \(m_s^{\max}=\sqrt{8\pi}v_S\),
\[
\begin{array}{c|c|c}
& m_s^{\max}~[{\rm GeV}]&\Gamma_{A'A'}/m_s\\ \hline
A&355.3719998&0.2488151\\
B&1579.1758130&0.2476241
\end{array}
\]
The limiting ratio approaches \(1/4\) for \(m_s\gg m_X\). Therefore the upper perturbativity endpoint is not a narrow-width regime. The direct-width audit is used here only as an optical-theorem validation; it must not be added a second time to a propagator whose \(\Pi_{ss}\) already contains this cut.

## 9. Acceptance boundary and next task

**Established in A4a:**
- complete one-loop \(U(1)_X\) vector/Goldstone/ghost \(ss\) kernel in general \(R_\xi\) integral form;
- compact Feynman-gauge \(A_E/B_E\) reduction;
- radial-scalar bubble and tadpole contributions;
- longitudinal-vector/ghost tadpole cancellation;
- zero-momentum unphysical-sector cancellation at \(\lambda_S=0\);
- Feynman-gauge optical-theorem reproduction of \(s\to A'A'\);
- benchmark widths and perturbativity-ceiling width ratios.

**Not yet established:**
- the finite real part in a fully fixed subtraction/tadpole scheme;
- general-\(\xi\) on-shell cut cancellation in an explicit numerical reduction;
- combination with the exact fermion \(ss\) self-energy and its EFT matching counterterms;
- the complete renormalized \(ss\) pole;
- the electroweak \(hh\) diagonal sector and the full \(2\times2\) gauge-parameter check.

The next step is A4b: independently reduce the general-\(\xi\) tensor integrals and verify that the on-shell absorptive part is \(\xi_X\)-independent, before using this entry in the complex-pole solver.
