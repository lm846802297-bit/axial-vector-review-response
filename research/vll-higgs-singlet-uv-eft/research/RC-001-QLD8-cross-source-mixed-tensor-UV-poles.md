# RC-001 QLD8: cross-source mixed rank-two/scalar UV projections

**Date:** 2026-11-10  
**Stage:** P1.4b1 — rank-two \(\otimes\) scalar and scalar \(\otimes\) rank-two projections  
**Status:** the antisymmetric Lorentz projections of all four cross-source kernels have been integrated through the degree-two UV Taylor coefficient. Both color-weighted mixed projections are nonzero at \(D=4\). The rank-two \(\otimes\) rank-two projection and complete graph phase remain open.

## 1. Important left/right momentum orientation

The open-line chains have different momentum order on the two bilinears for the last two topologies. Define \(x_\alpha\) as the momentum multiplying the gamma matrix on the **left** bilinear and \(y_\beta\) as the momentum multiplying the gamma matrix on the **right** bilinear.

| Topology | \(x\) (left bilinear) | \(y\) (right bilinear) | Source sign \(s\) |
|---|---|---|---|
| \((\bar Q,Q)\) | \(p_1+\ell\) | \(p_4-\ell\) | \(+1\) |
| \((\bar Q,\bar d)\) | \(p_1+\ell\) | \(p_3-\ell\) | \(+1\) |
| \((Q,d)\) | \(p_2-\ell\) | \(p_4+\ell\) | \(-1\) |
| \((\bar d,d)\) | \(p_2-\ell\) | \(p_3+\ell\) | \(-1\) |

Thus, in every topology,
\[
x=A+s\ell,\qquad y=B-s\ell,
\]
where
\[
(A_1,B_1)=(p_1,p_4),\quad
(A_2,B_2)=(p_1,p_3),\quad
(A_3,B_3)=(p_2,p_4),\quad
(A_4,B_4)=(p_2,p_3).
\]
This orientation does not change the scalar projection \(x\cdot y=r_a\cdot r_b\), but it is essential for the rank-two projections.

## 2. Antisymmetric tensor integral

Let
\[
W(u,v)\equiv\Gamma^{\mu\nu}u_\mu v_\nu,\qquad
\Gamma^{\mu\nu}=\gamma^{[\mu}\gamma^{\nu]}.
\]
The mixed rank-two terms in the four chains are proportional to
\(\Gamma^{\alpha\beta}x_\alpha y_\beta\), with topology-dependent signs and index order.

Use the same common auxiliary-mass IR rearrangement as in the scalar projection:
\[
\Delta_\ell=\ell^2+m_{\rm IR}^2.
\]
The scalar radial UV factors are
\[
A(D)=\frac D4,\qquad
B(D)=\frac{D(D+2)}{24}.
\]
Expanding
\[
(q+s\ell)^2(A+s\ell)_\alpha(B-s\ell)_\beta
\]
and the two shifted fermion denominators to total external-momentum degree two, then retaining only the antisymmetric part in \(\alpha,\beta\), gives
\[
\begin{aligned}
\mathcal T_{\alpha\beta}^{[2]}
\ \longrightarrow\ 
&A(D)\,A_\alpha B_\beta\\
&+\frac{2A(D)}D
\left[-A_\alpha q_\beta+q_\alpha B_\beta\right]\\
&+\frac{2B(D)}D
\left[-A_\alpha(B-A)_\beta+(B-A)_\alpha B_\beta\right],
\end{aligned}
\]
where the arrow means the coefficient of the common UV logarithmic pole after angular averaging. Contracting with \(\Gamma^{\alpha\beta}\) and using antisymmetry,
\[
\boxed{
\mathcal T^{[2]}(A,B)
=
\left[A(D)-\frac{4B(D)}D\right]W(A,B)
+\frac{2A(D)}D W(q,A+B).
}
\]
Since
\[
A(D)-\frac{4B(D)}D=\frac{D-4}{12},\qquad
\frac{2A(D)}D=\frac12,
\]
the individual topology kernel is
\[
\boxed{
T_i(D)=\frac{D-4}{12}W(A_i,B_i)
+\frac12W(q,A_i+B_i).
}
\]
The result is independent of the sign \(s=\pm1\): the sign in the source factor and the sign in the left/right momentum routing multiply to \(s^2=1\).

## 3. Dirac-chain signs and direct-color weighting

From the explicit Clifford decompositions:
- left rank-two \(\otimes\) scalar signs for topologies 1–4 are \((-,-,+,+)\);
- scalar \(\otimes\) right rank-two signs are \((-,+,-,+)\).

The direct color actions on the tree singlet are \((-1,+1,+1,-1)\). Therefore the color-weighted left and right mixed projections are
\[
K_{T\otimes S}=T_1-T_2+T_3-T_4,
\]
\[
K_{S\otimes T}=T_1+T_2-T_3-T_4.
\]
Using \(q=p_1+p_2\) and \(p_4=-p_1-p_2-p_3\), the sums reduce to
\[
\boxed{
K_{T\otimes S}(D)
=\frac{D+8}{12}\,
W(q,p_4-p_3),
}
\]
\[
\boxed{
K_{S\otimes T}(D)
=-\frac{D+8}{6}\,
W(p_1,p_2).
}
\]
At \(D=4\),
\[
K_{T\otimes S}(4)=W(q,p_4-p_3),
\qquad
K_{S\otimes T}(4)=-2W(p_1,p_2).
\]
These are nonzero physical mixed derivative-tensor momentum structures. They are not eliminated by the scalar-source factorization identity.

For \(D=4-2\epsilon\), the common prefactor is
\[
\frac{D+8}{12}=1-\frac{\epsilon}{6}.
\]
The \(O(\epsilon)\) part is retained for finite scheme bookkeeping. The pole coefficients themselves are the \(D\to4\) limits.

## 4. Validation and boundary

The companion exact-symbolic audit verifies:
1. the angular coefficients \(A(D)=D/4\), \(B(D)=D(D+2)/24\);
2. the simplification \(A-4B/D=(D-4)/12\);
3. the four topology momentum orientations;
4. both direct-color-weighted sums as identities in arbitrary external momentum components;
5. the \(D=4\) limits and \(D=4-2\epsilon\) expansion.

The audit passes exact symbolic component identities and independent rational momentum samples.

**Strict boundary:** this result covers only the mixed rank-two \(\otimes\) scalar and scalar \(\otimes\) rank-two projections. It does not include the rank-two \(\otimes\) rank-two part of the cross-chain numerator, restore the complete common Feynman-rule phase, establish the full gauge-invariant counterterm including external-gluon amplitudes, or perform the EOM/IBP quotient. No complete \(Z\) matrix or finite Wilson coefficient is claimed.
