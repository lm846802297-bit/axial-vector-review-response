# RC-001 QLD8: cross-source rank-two × rank-two UV kernel

**Date:** 2026-11-10  
**Stage:** P1.4b2 — full degree-two Lorentz tensor kernel  
**Status:** the complete D-dimensional degree-two tensor integral \(I_{\alpha\beta}\) has been derived. Its formal D-dimensional trace reproduces the scalar projection, and its antisymmetric part reproduces both mixed rank-two projections. This supplies the raw momentum tensor for the rank-two × rank-two chains; gamma/color reduction and the complete graph phase remain open.

## 1. Common tensor integral

For each topology use the left/right momentum orientation
\[
x=A+s\ell,\qquad y=B-s\ell,
\]
and source factor \((q+s\ell)^2\), with \(s=\pm1\). The four pairs are
\[
(A_i,B_i)=(p_1,p_4),(p_1,p_3),(p_2,p_4),(p_2,p_3).
\]
The denominators are the same three shifted massless propagators as in the scalar audit, with a common auxiliary IR mass introduced for the UV Taylor expansion.

Define the degree-two UV tensor coefficient by
\[
I_{\alpha\beta}(A,B;q)
=\left[
\int\frac{d^D\ell}{(2\pi)^D}
\frac{(q+s\ell)^2x_\alpha y_\beta}
{(\ell^2+m_{\rm IR}^2)
((\ell+p_a)^2+m_{\rm IR}^2)
((\ell-p_b)^2+m_{\rm IR}^2)}
\right]_{\mathrm{UV},\,p^2}.
\]
The common pole factor
\[
\frac{\Gamma(\epsilon)}{(4\pi)^{D/2}}
(m_{\rm IR}^2)^{-\epsilon}
\]
is factored out. Let
\[
\Delta=B-A,\quad u=A\cdot B,\quad
A^2=A\cdot A,\quad B^2=B\cdot B,\quad q^2=q\cdot q,
\]
and
\[
a_D=\frac D4,\quad
b_D=\frac{D(D+2)}{24},\quad
c_D=\frac{D(D+2)(D+4)}{192}.
\]
Then the complete degree-two tensor is
\[
\boxed{\begin{aligned}
I_{\alpha\beta}={}&
a_D\left[
A_\alpha B_\beta
+\frac2D(-A_\alpha q_\beta+q_\alpha B_\beta)
-\frac{q^2}{D}g_{\alpha\beta}
\right]\\
&+\frac{2b_D}{D}
\left[-A_\alpha\Delta_\beta+\Delta_\alpha B_\beta\right]\\
&-\frac{4b_D}{D(D+2)}
\left[g_{\alpha\beta}(q\cdot\Delta)
+q_\alpha\Delta_\beta+\Delta_\alpha q_\beta\right]\\
&+\frac{b_D}{D}(A^2+B^2)g_{\alpha\beta}\\
&-\frac{4c_D}{D(D+2)}
\left[
g_{\alpha\beta}(A^2+B^2-u)
+2A_\alpha A_\beta+2B_\alpha B_\beta
-A_\alpha B_\beta-B_\alpha A_\beta
\right].
\end{aligned}}
\]
The sign \(s\) cancels from this tensor coefficient: the source-factor sign and the left/right momentum-routing sign occur together, and all terms in the degree-two Taylor coefficient are even under \(s\to-s\).

## 2. Checks against the previously computed projections

### Formal D-dimensional trace

The trace must be performed with \(g^\alpha{}_\alpha=D\), not by taking the trace of a literal four-dimensional matrix while retaining symbolic \(D\). It gives
\[
\begin{aligned}
g^{\alpha\beta}I_{\alpha\beta}
={}&a_D\left[u-q^2+\frac2Dq\cdot\Delta\right]\\
&+b_D\left[\frac{2\Delta^2}{D}
-\frac4Dq\cdot\Delta+A^2+B^2\right]\\
&-\frac{4c_D}{D}(A^2+B^2-u).
\end{aligned}
\]
This is exactly the scalar-scalar kernel \(K_{ab}^{SS}(D)\) obtained independently in P1.4b0, after translating \(\Delta_d=s\Delta\).

### Antisymmetric part

The antisymmetric part is
\[
I_{\alpha\beta}-I_{\beta\alpha}
=
\frac{D-4}{12}(A_\alpha B_\beta-A_\beta B_\alpha)
+\frac12\left[
q_\alpha(A+B)_\beta-q_\beta(A+B)_\alpha
\right].
\]
Consequently,
\[
\Gamma^{\alpha\beta}I_{\alpha\beta}
=
\frac{D-4}{12}W(A,B)+\frac12W(q,A+B),
\]
which reproduces the P1.4b1 mixed rank-two projection exactly.

The radial factors expand as
\[
\begin{aligned}
a_D&=1-\frac\epsilon2+O(\epsilon^2),\\
b_D&=1-\frac{5\epsilon}{6}+O(\epsilon^2),\\
c_D&=1-\frac{13\epsilon}{12}+O(\epsilon^2).
\end{aligned}
\]
All three \(O(\epsilon)\) terms are retained for later finite-scheme bookkeeping.

## 3. Rank-two × rank-two contractions for the four topologies

Using the explicit direct-pairing Clifford decompositions, the raw rank-two × rank-two contribution is
\[
\begin{aligned}
K_{TT}^{(1)}&=
I^{(1)}_{\alpha\beta}
(\Gamma^{\rho\alpha}P_R)\otimes
(\Gamma^\beta{}_\rho P_L),\\
K_{TT}^{(2)}&=
I^{(2)}_{\alpha\beta}
(\Gamma^{\rho\alpha}P_R)\otimes
(\Gamma_\rho{}^\beta P_L),\\
K_{TT}^{(3)}&=
I^{(3)}_{\alpha\beta}
(\Gamma^{\alpha\rho}P_R)\otimes
(\Gamma^\beta{}_\rho P_L),\\
K_{TT}^{(4)}&=
I^{(4)}_{\alpha\beta}
(\Gamma^{\alpha\rho}P_R)\otimes
(\Gamma_\rho{}^\beta P_L).
\end{aligned}
\]
Here \(I^{(i)}=I(A_i,B_i;q_A)\). The tree-singlet direct-color weights are
\((-1,+1,+1,-1)\), so the weighted raw tensor contribution is
\[
K_{TT}^{\rm color}
=-K_{TT}^{(1)}+K_{TT}^{(2)}
+K_{TT}^{(3)}-K_{TT}^{(4)}.
\]
This is the full D-dimensional momentum tensor to be reduced in the chosen direct physical/evanescent basis. It is deliberately not Fierz-crossed.

## 4. Exact audit and strict boundary

The companion script verifies:
1. the complete \(I_{\alpha\beta}\) tensor has the required antisymmetric part;
2. its **formal D-dimensional trace** equals the independent scalar kernel;
3. the radial factors and their \(D=4-2\epsilon\) expansions.

The symbolic checks pass.

This completes the raw scalar, mixed rank-two/scalar, and rank-two × rank-two numerator projections at the level of the UV Taylor tensor. It does **not** yet perform the D-dimensional gamma/color contraction into a minimal local operator basis, restore the common graph phase and complete relative Feynman-rule signs, add external-gluon amplitudes required for gauge completion, or perform EOM/IBP reduction. Therefore no complete QCD counterterm matrix or Wilson coefficient is claimed.
