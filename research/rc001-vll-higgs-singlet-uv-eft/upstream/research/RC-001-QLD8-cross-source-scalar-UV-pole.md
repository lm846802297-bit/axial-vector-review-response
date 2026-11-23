# RC-001 QLD8: cross-source scalar-projection UV pole

**Date:** 2026-11-10  
**Stage:** P1.4b0 — four cross-source graphs, physical scalar-scalar projection  
**Status:** the \(P_R\otimes P_L\) projection of all four cross-source kernels has been evaluated through the degree-two UV Taylor coefficient using a common auxiliary denominator mass. The color-weighted result is an octet double-\(\overleftrightarrow D\) derivative structure. Tensor projections and the complete counterterm matrix remain open.

## 1. Scope and conventions

Use the direct spinor pairing
\[
(\bar Q(p_1),d(p_2))\otimes(\bar d(p_3),Q(p_4)),
\qquad p_1+p_2+p_3+p_4=0,
\]
and
\[
q_A=p_1+p_2,\qquad p_4=-p_1-p_2-p_3.
\]
For each ordered cross-source pair \((a,b)\),
\[
r_a=p_a+\ell,\qquad r_b=p_b-\ell,
\qquad q_A^{(ab)}=q_A+s_{ab}\ell,
\]
with \(s_{ab}=+1\) for \((\bar Q,Q)\), \((\bar Q,\bar d)\), and
\(s_{ab}=-1\) for \((Q,d)\), \((\bar d,d)\).

The four cross-source numerator chains are exactly those in
\`research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md\`.
The direct color actions on the tree singlet \((1,0)_d\) are
\[
\begin{array}{c|rrrr}
(a,b)&(\bar Q,Q)&(\bar Q,\bar d)&(Q,d)&(\bar d,d)\\ \hline
\text{octet coefficient}&-1&+1&+1&-1.
\end{array}
\]
The calculation below strips the common Feynman-rule phase and \(g_s^2\);
these relative color and numerator signs are retained.

## 2. Exact scalar projection of each Dirac chain

Define
\[
\mathcal P_{SS}[\mathcal N]
=\frac14\operatorname{Tr}_{16}
\big[(P_R\otimes P_L)\mathcal N\big].
\]
For each of the four topologies, the two chiral traces give
\[
\operatorname{tr}(P_R\gamma^\mu\slashed r)
=2r^\mu,\qquad
\operatorname{tr}(P_L\slashed r\gamma^\mu)
=2r^\mu,
\]
with the same result for the reversed gamma ordering appearing in the other
two chains. Consequently,
\[
\boxed{\mathcal P_{SS}[\mathcal N_{ab}]=r_a\cdot r_b.}
\]
This was checked using explicit \(4\times4\) Dirac matrices for all four
topologies at three independent momentum samples (12/12 exact checks).

The scalar-projected integrand is therefore
\[
I_{ab}^{SS}
=\int\frac{d^D\ell}{(2\pi)^D}
\frac{(q_A+s_{ab}\ell)^2
[(\ell+p_a)\cdot(p_b-\ell)]}
{\ell^2(\ell+p_a)^2(\ell-p_b)^2}.
\]
Writing
\[
\Delta=p_b-p_a,\qquad u=p_a\cdot p_b,
\]
the numerator identity is
\[
(\ell+p_a)\cdot(p_b-\ell)
=-\ell^2+\ell\cdot\Delta+u.
\]

## 3. IR rearrangement and UV Taylor coefficient

To separate the UV logarithm from the zero-momentum IR singularity, introduce
a common auxiliary mass \(m_{\rm IR}\) in the three denominators:
\[
\ell^2+m_{\rm IR}^2,\quad
(\ell+p_a)^2+m_{\rm IR}^2,\quad
(\ell-p_b)^2+m_{\rm IR}^2.
\]
This is an auxiliary IR rearrangement only; it is not a physical mass
assignment. The UV pole is read from the degree-two Taylor coefficient in
the external momenta. The three radial integrals have a common factor
\[
\frac{\Gamma(\epsilon)}{(4\pi)^{D/2}}
(m_{\rm IR}^2)^{-\epsilon}
\]
and relative coefficients
\[
A(D)=\frac D4,\qquad
B(D)=\frac{D(D+2)}{24},\qquad
C(D)=\frac{D(D+2)(D+4)}{192}.
\]
After the \(D\)-dimensional angular averages, the scalar UV kernel is
\[
\boxed{
\begin{aligned}
K_{ab}^{SS}(D)
={}&A(D)\left[
u-q_A^2+\frac{2s_{ab}}{D}q_A\cdot\Delta
\right]\\
&+B(D)\left[
\frac{2\Delta^2}{D}
-\frac{4s_{ab}}{D}q_A\cdot\Delta
+p_a^2+p_b^2
\right]\\
&-\frac{4C(D)}{D}
(p_a^2+p_b^2-u).
\end{aligned}
}
\]
In particular, at \(D=4\),
\[
\boxed{
K_{ab}^{SS}(4)
=p_a\cdot p_b-q_A^2
+\frac12(p_a^2+p_b^2)
-\frac{s_{ab}}2q_A\cdot(p_b-p_a).
}
\]
The common \(\overline{\rm MS}\) pole factor is
\(1/(16\pi^2\epsilon)\). The expressions below are the relative numerator
kernel coefficients before restoring the common amplitude phase and
\(g_s^2\).

## 4. Four topology results

Use the independent invariants
\[
s_{11}=p_1^2,\quad s_{22}=p_2^2,\quad s_{33}=p_3^2,\quad
s_{12}=p_1\cdot p_2,\quad
s_{13}=p_1\cdot p_3,\quad
s_{23}=p_2\cdot p_3.
\]
The exact \(D=4\) coefficients are:

| Topology | \(K_{ab}^{SS}(4)\) |
|---|---|
| \((\bar Q,Q)\) | \(\frac12s_{33}-\frac12s_{12}+\frac12s_{13}+\frac32s_{23}\) |
| \((\bar Q,\bar d)\) | \(-s_{22}+\frac12s_{33}-\frac32s_{12}+\frac12s_{13}-\frac12s_{23}\) |
| \((Q,d)\) | \(\frac12s_{33}-\frac12s_{12}+\frac32s_{13}+\frac12s_{23}\) |
| \((\bar d,d)\) | \(-s_{11}+\frac12s_{33}-\frac32s_{12}-\frac12s_{13}+\frac12s_{23}\) |

These are separate graph kernels; the color weights must be applied only
after each topology has been evaluated.

## 5. Color-weighted scalar pole and operator interpretation

Applying the direct-basis tree-vector color weights
\((-1,+1,+1,-1)\) gives
\[
K_{\rm cross}^{SS}(4)
=-K_1^{SS}+K_2^{SS}+K_3^{SS}-K_4^{SS}.
\]
The six independent momentum invariants collapse to
\[
\boxed{
K_{\rm cross}^{SS}(4)
=p_1^2-p_2^2+2p_1\cdot p_3-2p_2\cdot p_3
=(p_1-p_2)\cdot(p_3-p_4).
}
\]
Thus the scalar-scalar part of the cross-source UV pole is in the direct
color-octet channel and has the momentum polynomial of the candidate
dimension-eight operator
\[
\mathcal O_{8,\leftrightarrow D}^{(8)}
=
(\bar Q_i T^A_{il}P_R\,i\overleftrightarrow D_\mu d_l)
(\bar d_k T^A_{kj}P_L\,i\overleftrightarrow D^\mu Q_j),
\]
where
\[
\bar\psi\,i\overleftrightarrow D_\mu\,\chi
\equiv i\bar\psi D_\mu\chi-i(D_\mu\bar\psi)\chi.
\]
With all four external momenta incoming, the product of the two
\(\overleftrightarrow D\) factors gives
\((p_1-p_2)\cdot(p_3-p_4)\). The covariant derivatives here act on the
individual fundamental fields; the complete gauge-invariant operator also
has the corresponding amplitudes with external gluons.

The \(D\)-dependent scalar projection is especially compact:
\[
\boxed{
K_{\rm cross}^{SS}(D)
=\frac{D^2+10D-8}{48}
(p_1-p_2)\cdot(p_3-p_4).
}
\]
For \(D=4-2\epsilon\),
\[
K_{\rm cross}^{SS}(D)
=\left(1-\frac34\epsilon+\frac1{12}\epsilon^2\right)
(p_1-p_2)\cdot(p_3-p_4).
\]
The \(O(\epsilon)\) term is recorded for later finite-scheme bookkeeping;
it is not, by itself, a finite Wilson coefficient.

## 6. Validation and strict boundary

The companion script
\`calculations/RC-001-QLD8-cross-source-scalar-UV-audit.py\`
checks:
1. the scalar projection of each of the four open-line chains against
   \(r_a\cdot r_b\) (12/12 exact checks);
2. the four topology polynomials in the six independent Lorentz invariants;
3. the direct-color-weighted sum;
4. the exact \(D\)-dependent factor and its \(D=4-2\epsilon\) expansion.

This is **only the \(P_R\otimes P_L\) scalar projection** of the four
cross-source graphs. It is not the complete Dirac numerator pole:
rank-two\(\otimes\)scalar, scalar\(\otimes\)rank-two, and
rank-two\(\otimes\)rank-two projections still have to be calculated.
The common graph phase/sign must be restored in the full amplitude
convention. The auxiliary-mass rearrangement has not yet been promoted to
a complete \(R^*\) subtraction for the full operator basis. No complete
QCD \(Z\) matrix, anomalous-dimension block, EOM/IBP quotient, or finite
UV-minus-EFT Wilson coefficient is claimed.
