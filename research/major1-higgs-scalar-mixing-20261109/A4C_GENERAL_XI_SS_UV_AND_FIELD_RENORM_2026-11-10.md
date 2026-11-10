# Major Point 1 — A4c general-\(R_{\xi_X}\) UV-pole and field-renormalization audit for \(\Pi_{ss}\)

**Purpose:** determine the general-\(\xi_X\) UV pole of the complete one-loop bosonic \(ss\) subset and isolate the diagonal field-renormalization coefficient. This complements A4a's Feynman-gauge pole and A4b's general-gauge absorptive check.

## 1. Mixed \(A'a\) integral: UV expansion

The only momentum-dependent UV pole comes from the mixed derivative loop
\[
I_{Aa}(p_E)=
\int_k^\star
\frac{(k-p_E)_\mu D_{\mu\nu}(k+p_E)(k-p_E)_\nu}
{k_E^2+\xi_Xm_X^2}.
\]
Set \(K=k_E^2\), \(r=k_E\cdot p_E\), \(P=p_E^2\), and \(M=m_X^2\). The transverse numerator is
\[
N_T=(k-p)^2-\frac{(K-P)^2}{K+2r+P}.
\]
At large \(K\),
\[
N_T=4P-\frac{4r^2}{K}+O(K^{-1}P^{3/2},K^{-1}P^2),
\]
so after angular averaging, \(\langle r^2\rangle=KP/d\),
\[
I_{Aa,T}^{\rm UV}\big|_{p^2}
=4\left(1-\frac1d\right)P\,\frac1{\bar\epsilon}
\longrightarrow 3P\,\frac1{\bar\epsilon}
\quad(d\to4).
\]

For the longitudinal term, the large-\(K\) integrand is proportional to
\[
\frac{\xi}{K}
\frac{(1-P/K)^2}
{(1+2r/K+P/K)(1+2r/K+P/K+\xi M/K)(1+\xi M/K)}.
\]
The \(p_E^2/K\) coefficient after angular averaging is \(-\xi P/K\), hence
\[
I_{Aa,L}^{\rm UV}\big|_{p^2}
=-\xi_XP\,\frac1{\bar\epsilon}.
\]
Therefore
\[
\boxed{
I_{Aa}^{\rm UV}\big|_{p^2}
=(3-\xi_X)p_E^2\,\frac1{\bar\epsilon}.
}
\]
At zero external momentum only the longitudinal projector survives:
\[
I_{Aa}^{\rm UV}(0)
=\xi_X\int_k^\star\frac{k^2}{(k^2+\xi_Xm_X^2)^2}
=-2\xi_X^2m_X^2\,\frac1{\bar\epsilon}.
\]
The mixed self-energy is \(-g_A^2 I_{Aa}\).

## 2. Cancellation of the \(\xi_X^2m_X^2\) local poles

The UV coefficients of the vector seagull, vector bubble, mixed loop, and ghost bubble are
\[
\begin{aligned}
\Pi_{AA,\rm seagull}^{\rm UV}
&=-g_A^2(d-1+\xi_X^2)m_X^2,\\
\Pi_{AA,\rm bubble}^{\rm UV}
&=-2g_A^2(d-1+\xi_X^2)m_X^2,\\
\Pi_{Aa,\rm mixed}^{\rm UV}\big|_{p^2=0}
&=+2g_A^2\xi_X^2m_X^2,\\
\Pi_{c_X\bar c_X}^{\rm UV}
&=+g_A^2\xi_X^2m_X^2.
\end{aligned}
\]
Their sum is
\[
-3(d-1)g_A^2m_X^2,
\]
so all \(\xi_X^2m_X^2\) terms cancel. Adding the Goldstone tadpole and bubble gives the general-\(\xi_X\) vector/Goldstone/ghost pole
\[
\boxed{
16\pi^2\Pi_{ss,E}^{X,\rm UV}
=\frac1{\bar\epsilon}
\left[
-g_A^2(3-\xi_X)p_E^2
-3(d-1)g_A^2m_X^2
-\xi_X\lambda_Sm_X^2
-2\lambda_S^2v_S^2
\right].
}
\]
For \(d=4\), the local gauge contribution is \(-9g_A^2m_X^2\), independent of \(\xi_X\).

The radial-scalar contribution is gauge independent:
\[
16\pi^2\Pi_{ss,E}^{\rm radial,UV}
=-\frac{24\lambda_S^2v_S^2}{\bar\epsilon}.
\]
Thus the complete one-loop singlet-bosonic pole in four dimensions is
\[
\boxed{
16\pi^2\Pi_{ss,E}^{\rm bos,UV}
=\frac1{\bar\epsilon}
\left[
-g_A^2(3-\xi_X)p_E^2
-9g_A^2m_X^2
-\xi_X\lambda_Sm_X^2
-26\lambda_S^2v_S^2
\right].
}
\]
At \(\xi_X=1\) this reduces exactly to A4a.

## 3. Diagonal field counterterm

In the Euclidean convention
\[
\Gamma_E^{(2)}=p_E^2+m_s^2+\Pi_{ss,E},
\]
the \(p_E^2\) pole is cancelled by
\[
\boxed{
\delta Z_s^{X}
=\frac{g_A^2(3-\xi_X)}{16\pi^2\bar\epsilon}.
}
\]
The coefficient \(3-\xi_X\) is the standard covariant-gauge scalar-QED wave-function renormalization coefficient. This provides an independent check of the mixed derivative vertex and the longitudinal propagator normalization.

The local mass poles are not converted into a finite \(\delta m_s^2\) here. They must be combined with the A3b tadpole/VEV prescription and the renormalization of \(\lambda_S,v_S\), and then reconciled with the exact fermion-sector matching.

## 4. Validation

The accompanying symbolic script checks:
1. cancellation of every \(\xi_X^2m_X^2\) term among vector, mixed and ghost graphs;
2. the \((3-\xi_X)p_E^2\) coefficient;
3. the gauge-independent local gauge pole \(-9g_A^2m_X^2\) at \(d=4\);
4. the gauge-dependent Goldstone tadpole pole \(-\xi_X\lambda_Sm_X^2\);
5. reduction to the A4a Feynman-gauge result.

This is a UV-pole and field-counterterm audit, not a finite self-energy calculation. No finite real part, full tadpole renormalization, or complex pole is claimed.
