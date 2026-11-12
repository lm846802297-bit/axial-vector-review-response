# Major Point 1 — A4b explicit general-\(R_\xi\) on-shell cut cancellation in \(\Pi_{ss}\)

**Date:** 2026-11-10  
**Purpose:** independently verify that the complete one-loop \(U(1)_X\) absorptive contribution to the radial-scalar two-point function is independent of \(\xi_X\) on the tree-level mass shell. This extends the Feynman-gauge optical-theorem check in A4a to a general-\(\xi_X\) cut decomposition.

## 1. Propagator pole decomposition

In four dimensions the \(R_\xi\) vector propagator can be decomposed into transverse and longitudinal poles:
\[
D_{\mu\nu}(q)\propto
\frac{P^T_{\mu\nu}(q)}{q^2-m_X^2}
+\frac{\xi_XP^L_{\mu\nu}(q)}{q^2-\xi_Xm_X^2},
\]
where
\[
P^L_{\mu\nu}(q)=\frac{q_\mu q_\nu}{q^2},\qquad
P^T_{\mu\nu}(q)=g_{\mu\nu}-P^L_{\mu\nu}(q).
\]
The two pole modes are therefore
\[
T:\quad m_T=m_X,\quad w_T=1,
\qquad
L:\quad m_L=\sqrt{\xi_X}m_X,\quad w_L=\xi_X.
\]
The \(T\) projector has rank three and carries the physical massive-vector polarizations. The \(L\) pole is gauge dependent and is not a physical additional vector state.

The Goldstone and complex ghost masses are both
\[
m_a=m_c=\sqrt{\xi_X}m_X.
\]

## 2. Two-body kinematics and vector-bubble traces

For a cut with internal masses \(m_i,m_j\), define
\[
\beta_{ij}(s)=
\sqrt{\left[1-\frac{(m_i+m_j)^2}{s}\right]
      \left[1-\frac{(m_i-m_j)^2}{s}\right]}
\,\Theta\!\left(s-(m_i+m_j)^2\right).
\]
In the centre-of-mass frame, with \(q_i+q_j=p\),
\[
q_i\cdot q_j=\frac{s-m_i^2-m_j^2}{2},\qquad
K_{ij}=\frac{(q_i\cdot q_j)^2}{m_i^2m_j^2}.
\]
The projector traces are
\[
\begin{aligned}
\operatorname{Tr}(P_T^iP_T^j)&=2+K_{ij},\\
\operatorname{Tr}(P_T^iP_L^j)
=\operatorname{Tr}(P_L^iP_T^j)&=1-K_{ij},\\
\operatorname{Tr}(P_L^iP_L^j)&=K_{ij}.
\end{aligned}
\]
Consequently the vector-bubble cut coefficient, including the two ordered mixed \(TL\) and \(LT\) terms, is
\[
\boxed{
C_{VV}=-2g_A^2m_X^2
\sum_{i,j=T,L}w_iw_j\beta_{ij}
\operatorname{Tr}(P_iP_j).
}
\]

## 3. Mixed \(A'a\) derivative cut

Let \(q_a+q_V=p\), where \(q_a^2=m_a^2\), \(q_V^2=m_V^2\), and define
\[
u=p+q_a.
\]
This is the momentum combination from the \(A'sa\) derivative vertex with all momenta incoming. For a vector pole of type \(i=T,L\),
\[
N_L=\frac{(u\cdot q_V)^2}{m_V^2},\qquad
N_T=u^2-N_L.
\]
The mixed-cut coefficient is
\[
\boxed{
C_{Aa}=g_A^2\sum_{i=T,L}w_i\beta_{i,a}N_i.
}
\]
For numerical evaluation,
\[
\begin{aligned}
E_a&=\frac{s+m_a^2-m_V^2}{2\sqrt{s}},&
E_V&=\frac{s+m_V^2-m_a^2}{2\sqrt{s}},\\
q^2&=E_a^2-m_a^2,&
u^2&=(\sqrt{s}+E_a)^2-q^2,\\
u\cdot q_V&=(\sqrt{s}+E_a)E_V+q^2.
\end{aligned}
\]
The sign is fixed by analytic continuation of the Euclidean mixed kernel in A4a. At \(\xi_X=1\), \(N_T+N_L=2s+m_X^2\), reproducing the A4a Feynman-gauge coefficient.

## 4. Goldstone and ghost cuts

The remaining cut coefficients are
\[
\boxed{
C_{c\bar c}=\xi_X^2g_A^2m_X^2\beta_{aa},
\qquad
C_{aa}=-2\lambda_S^2v_S^2\beta_{aa}.
}
\]
The total coefficient is
\[
C_{\rm tot}(\xi_X)=C_{VV}+C_{Aa}+C_{c\bar c}+C_{aa}.
\]
With the A4a Euclidean convention,
\[
\operatorname{Im}\Pi_{ss,E}(-s-i0)
=\frac{C_{\rm tot}(\xi_X)}{16\pi}.
\]

## 5. On-shell cancellation identity

At the tree-level radial mass shell,
\[
s=m_s^2,\qquad
g_A=\frac{m_X}{v_S},\qquad
\lambda_S=\frac{m_s^2}{2v_S^2},
\]
the complete sum is
\[
\boxed{
C_{\rm tot}(\xi_X)=
-\frac{s^2}{2v_S^2}
\left(1-\frac{4m_X^2}{s}+\frac{12m_X^4}{s^2}\right)
\sqrt{1-\frac{4m_X^2}{s}}\,
\Theta(s-4m_X^2),
}
\]
which contains no \(\xi_X\). Therefore
\[
\boxed{
-\frac{\operatorname{Im}\Pi_{ss,E}(-m_s^2-i0)}{m_s}
=\frac{m_s^3}{32\pi v_S^2}
(1-4x+12x^2)\sqrt{1-4x}\,
\Theta(1-4x),
\quad x=\frac{m_X^2}{m_s^2}.
}
\]
This is the physical three-polarization \(s\to A'A'\) width. The result follows from the sum of the vector, mixed, Goldstone and ghost cuts; no individual unphysical cut is interpreted as a physical channel.

## 6. Numerical gauge-parameter scan

The accompanying script evaluates the exact two-body phase-space factors and projector contractions for
\[
\xi_X=0.25,\ 0.5,\ 1,\ 2,\ 4,\ 10.
\]
It tests Benchmark A at \(m_s=100,125.25,150\) GeV and Benchmark B at \(m_s=150,200\) GeV. Across all open points and all six gauge choices, the maximum relative difference between \(C_{\rm tot}(\xi_X)\) and the gauge-independent expression above is
\[
\boxed{\max|\delta C/C|=8.61\times10^{-16}.}
\]
The cut-derived width also agrees with the direct \(s\to A'A'\) formula to the same numerical precision.

For illustration, the decomposition at two representative points is:

**Benchmark A, \(m_s=125.25\) GeV** (all coefficients include their two-body phase-space factors; units GeV\(^2\)):

| \(\xi_X\) | \(C_{VV}\) | \(C_{Aa}\) | \(C_{c\bar c}\) | \(C_{aa}\) | \(C_{\rm tot}\) |
|---:|---:|---:|---:|---:|---:|
| 0.25 | -12.0623 | 852.5724 | 0.1240 | -24409.8864 | -23569.2523 |
| 0.5 | -12.7904 | 774.5050 | 0.4943 | -24331.4612 | -23569.2523 |
| 1 | -15.7165 | 618.3471 | 1.9646 | -24173.8475 | -23569.2523 |
| 2 | -27.4133 | 305.9024 | 7.7547 | -23855.4962 | -23569.2523 |
| 4 | -73.9057 | -319.8255 | 30.1741 | -23205.6952 | -23569.2523 |
| 10 | -391.9832 | -2212.2730 | 171.7741 | -21136.7703 | -23569.2523 |

**Benchmark B, \(m_s=150\) GeV**:

| \(\xi_X\) | \(C_{VV}\) | \(C_{Aa}\) | \(C_{c\bar c}\) | \(C_{aa}\) | \(C_{\rm tot}\) |
|---:|---:|---:|---:|---:|---:|
| 0.25 | -615.7784 | 1997.5464 | 9.0049 | -2315.1125 | -924.3396 |
| 0.5 | -627.2496 | 1723.2438 | 31.9301 | -2052.2638 | -924.3396 |
| 1 | -689.1281 | 1062.7965 | 86.1410 | -1384.1490 | -924.3396 |
| 2 | -924.3396 | 0 | 0 | 0 | -924.3396 |
| 4 | -924.3396 | 0 | 0 | 0 | -924.3396 |
| 10 | -924.3396 | 0 | 0 | 0 | -924.3396 |

The second table is particularly instructive. At \(\xi_X=0.25\), all unphysical thresholds are open and large terms cancel. At \(\xi_X\ge2\), the Goldstone, ghost, mixed and longitudinal-vector thresholds are closed, leaving only the physical transverse-vector cut. The total is unchanged.

## 7. Interpretation and acceptance boundary

A4b establishes the \(\xi_X\)-independence of the **on-shell absorptive part** of the one-loop \(ss\) kernel and its equality to the physical \(s\to A'A'\) width. It also confirms the relative signs and normalization of the mixed derivative, ghost and Goldstone contributions.

It does **not** establish gauge independence of the full complex pole. The real part, tadpole/VEV prescription, UV counterterms, fermion matching, and the electroweak \(hh\) sector must still be combined before solving the full \(2\times2\) determinant. The direct width remains a validation of the cut, not an additional width to add to the same self-energy.
