# Major Point 1 — A4d tadpole-improved zero-momentum \(ss\) kernel

**Purpose:** connect the A4a–A4c self-energy calculation to the A3b tadpole/VEV counterterm algebra and identify an exact cancellation that is invisible if one inspects only the 1PI two-point graphs.

## 1. One-loop tadpole

The A4a result gives
\[
T_s^{(1)}=\frac1{16\pi^2}\left[
(d-1)g_Am_X{\cal A}_E(m_X^2)
+\lambda_Sv_S{\cal A}_E(\xi_Xm_X^2)
+3\lambda_Sv_S{\cal A}_E(m_s^2)
\right].
\]
The longitudinal-vector and complex-ghost one-point functions cancel before this expression is formed.

Dividing by \(v_S\) and using \(g_A=m_X/v_S\),
\[
\frac{T_s^{(1)}}{v_S}
=\frac1{16\pi^2}\left[
(d-1)g_A^2{\cal A}_E(m_X^2)
+\lambda_S{\cal A}_E(\xi_Xm_X^2)
+3\lambda_S{\cal A}_E(m_s^2)
\right].
\]

## 2. Exact zero-momentum identity

At \(p_E^2=0\), the general-\(\xi_X\) A4a kernel reduces to
\[
\begin{aligned}
16\pi^2\Pi_{ss,E}(0)={}&
g_A^2[(d-1){\cal A}_E(m_X^2)+\xi_X{\cal A}_E(\xi_Xm_X^2)]\\
&-2g_A^2m_X^2[(d-1){\cal B}_E(0;m_X^2,m_X^2)
+\xi_X^2{\cal B}_E(0;\xi_Xm_X^2,\xi_Xm_X^2)]\\
&-\xi_Xg_A^2[{\cal A}_E(\xi_Xm_X^2)
-\xi_Xm_X^2{\cal B}_E(0;\xi_Xm_X^2,\xi_Xm_X^2)]\\
&+\xi_X^2g_A^2m_X^2{\cal B}_E(0;\xi_Xm_X^2,\xi_Xm_X^2)\\
&+\lambda_S{\cal A}_E(\xi_Xm_X^2)
-2\lambda_S^2v_S^2{\cal B}_E(0;\xi_Xm_X^2,\xi_Xm_X^2)\\
&+3\lambda_S{\cal A}_E(m_s^2)
-18\lambda_S^2v_S^2{\cal B}_E(0;m_s^2,m_s^2).
\end{aligned}
\]
Subtracting the tadpole divided by the VEV gives the exact identity
\[
\boxed{\begin{aligned}
16\pi^2\left[
\Pi_{ss,E}(0)-\frac{T_s^{(1)}}{v_S}
\right]={}&
-2(d-1)g_A^2m_X^2
{\cal B}_E(0;m_X^2,m_X^2)\\
&-2\lambda_S^2v_S^2
{\cal B}_E(0;\xi_Xm_X^2,\xi_Xm_X^2)\\
&-18\lambda_S^2v_S^2
{\cal B}_E(0;m_s^2,m_s^2).
\end{aligned}}
\]
All tadpole-type \(A_E\) terms cancel. The entire \(\xi_X\)-dependent longitudinal-vector/mixed/ghost sector cancels. Only the transverse-vector bubble and the two scalar bubbles remain.

This identity is exact at \(p_E^2=0\), not merely a UV-pole relation.

## 3. Gauge-independent UV pole of the tadpole-improved curvature

Since each \({\cal B}_E\) has unit UV pole,
\[
\boxed{
16\pi^2\left[
\Pi_{ss,E}(0)-\frac{T_s^{(1)}}{v_S}
\right]_{\rm UV}
=
-\frac{2(d-1)g_A^2m_X^2+20\lambda_S^2v_S^2}
{\bar\epsilon}.
}
\]
In four dimensions,
\[
\boxed{
16\pi^2\left[
\Pi_{ss,E}(0)-\frac{T_s^{(1)}}{v_S}
\right]_{\rm UV}
=
-\frac{6g_A^2m_X^2+20\lambda_S^2v_S^2}
{\bar\epsilon},
}
\]
which is independent of \(\xi_X\).

This is consistent with the A3b parameter-counterterm relation. For the singlet potential at zero portal,
\[
\delta T_s=-v_S\delta\mu_S^2
+v_S^3\delta\lambda_S+2\lambda_Sv_S^2\delta v_S.
\]
Eliminating \(\delta\mu_S^2\) with the renormalized tadpole condition puts the term \(-T_s^{(1)}/v_S\) into the mass-parameter counterterm. It must be included once, not added again as a separate tadpole insertion.

## 4. Interpretation and boundary

A4d provides a direct algebraic bridge between the one-point and two-point functions:
- vector, Goldstone and radial-scalar seagulls cancel against their corresponding tadpole/VEV pieces;
- the longitudinal-vector, mixed \(A'a\), and ghost sector cancels at zero momentum;
- the remaining zero-momentum UV pole is independent of \(\xi_X\).

This does not imply that \(\Pi_{ss}(p^2)\) is gauge independent at nonzero momentum, nor does it determine the physical complex pole. The full momentum dependence, common finite renormalization conditions, exact fermion matching, and electroweak \(hh\) sector are still required.


## 5. Momentum-dependent tadpole-improved UV pole

The same A4c general-\(\xi_X\) pole and the A4a tadpole give, in four dimensions,
\[
16\pi^2\left[\Pi_{ss,E}(p_E^2)-\frac{T_s^{(1)}}{v_S}\right]_{\rm UV}
=
\frac1{\bar\epsilon}
\left[-g_A^2(3-\xi_X)p_E^2
-6g_A^2m_X^2-20\lambda_S^2v_S^2\right].
\]
Thus the **local mass pole is \(\xi_X\)-independent at arbitrary external momentum**; only the diagonal field-renormalization pole retains the expected \((3-\xi_X)\) dependence.

In Feynman gauge the full tadpole-improved bosonic kernel has the compact form
\[
\boxed{\begin{aligned}
16\pi^2\widehat\Pi_{ss,E}^{\xi_X=1}(p_E^2)
={}&-\left[2g_A^2p_E^2+2(d-1)g_A^2m_X^2
+2\lambda_S^2v_S^2\right]
{\cal B}_E(p_E^2;m_X^2,m_X^2)\\
&-18\lambda_S^2v_S^2
{\cal B}_E(p_E^2;m_s^2,m_s^2),
\end{aligned}}
\]
where \(\widehat\Pi\equiv\Pi-T_s^{(1)}/v_S\). This is a one-loop tadpole-improved kernel, not yet the fully renormalized physical inverse propagator.
