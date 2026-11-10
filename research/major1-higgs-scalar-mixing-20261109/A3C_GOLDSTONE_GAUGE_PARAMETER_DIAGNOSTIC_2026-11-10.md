# Major Point 1 — A3c gauge-parameter diagnostic of Goldstone cuts in \(\Pi_{hs}\)

This is a diagnostic of the A3a Goldstone subset, not a physical prediction. It evaluates the absorptive part at \(p^2=m_h^2\) for a common \(R_\xi\) parameter \(\xi_W=\xi_Z=\xi_X=\xi\), using the two existing benchmarks and \(m_s=m_h=125.25\) GeV for the illustrative point.

## 1. Analytic absorptive part

For equal-mass scalar loops,
\[
\operatorname{Im}B_0(p^2;m^2,m^2)
=\pi\sqrt{1-\frac{4m^2}{p^2}}\,
\Theta(p^2-4m^2).
\]
Therefore the Goldstone part of the A3a mixed self-energy has
\[
\boxed{\begin{aligned}
\frac{\operatorname{Im}\Pi_{hs}^{G}(p^2)}
{\lambda_{HS}vv_S}
=\frac{1}{16\pi}\bigg[
&2\lambda_H\beta_W\,\Theta(p^2-4\xi_Wm_W^2)\\
&+\lambda_H\beta_Z\,\Theta(p^2-4\xi_Zm_Z^2)\\
&+\lambda_S\beta_X\,\Theta(p^2-4\xi_Xm_X^2)
\bigg],
\end{aligned}}
\]
where \(\beta_i=\sqrt{1-4\xi_i m_i^2/p^2}\) in the open channel. This is manifestly gauge-parameter dependent.

## 2. Threshold locations at \(p^2=m_h^2\)

The channel opens when
\[
\xi_i<\frac{m_h^2}{4m_i^2}.
\]
For \(m_h=125.25\) GeV:
\[
\xi_W^{\rm thr}\simeq0.607,\qquad
\xi_Z^{\rm thr}\simeq0.472,
\]
\[
\xi_X^{\rm thr}\simeq
\begin{cases}
39.22 &(A,\ m_X=10~{\rm GeV}),\\
0.988 &(B,\ m_X=63~{\rm GeV}).
\end{cases}
\]
Thus at \(\xi=1\), only the \(a a\) Goldstone cut is open in A; no Goldstone cut is open in B. At \(\xi=0.5\), the charged \(G^\pm\) cut opens in both benchmarks and the \(a a\) cut also opens in B. At \(\xi=40\), all listed Goldstone cuts are closed.

## 3. Numerical diagnostic

The table gives the coefficient
\[
C_\xi\equiv
\frac{\operatorname{Im}\Pi_{hs}^{G}(m_h^2)}
{\lambda_{HS}vv_S},
\]
using \(\lambda_H=m_h^2/(2v^2)\) and \(\lambda_S=m_h^2/(2v_S^2)\) at the illustrative degenerate point.

| \(\xi\) | A: \(C_\xi\) | B: \(C_\xi\) |
|---:|---:|---:|
| 0.5 | 0.0330179 | 0.00326700 |
| 1 | 0.0306564 | 0 |
| 2 | 0.0302526 | 0 |
| 4 | 0.0294286 | 0 |
| 10 | 0.0268048 | 0 |
| 40 | 0 | 0 |

The abrupt threshold changes and nonzero imaginary part are properties of the unphysical Goldstone subset. They cannot be interpreted as a physical \(h-s\) mixing width.

## 4. Physical interpretation

This is precisely why the calculation must retain the full gauge-basis \(2\\times2\) inverse propagator. In A, the physical \(s\\to A'A'\) channel is open and contributes to the diagonal \(ss\) absorptive kernel through the vector sector. The Goldstone \(aa\) cut in the off-diagonal scalar subset is gauge dependent. The physical complex poles are obtained only after assembling the diagonal vector/Goldstone/ghost contributions, the off-diagonal scalar/fermion terms, and all counterterms consistently.

There is no contradiction with the A2 result that no one-loop \(hs\) vector or ghost bubble exists: gauge independence of the poles is a property of the complete matrix and its determinant, not of an isolated off-diagonal entry.

**Acceptance boundary:** this diagnostic demonstrates the gauge dependence of the Goldstone subset and identifies the required gauge-parameter checks. It does not compute the cancellation or a physical pole.
