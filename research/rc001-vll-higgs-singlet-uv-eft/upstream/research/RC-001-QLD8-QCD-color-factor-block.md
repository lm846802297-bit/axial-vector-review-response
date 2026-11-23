# RC-001 QLD8: exact QCD color-factor block for the \(d^\dagger d\) pilot

**Date:** 2026-11-10  
**Stage:** P1.1a — group-theory factorization for the first four-quark channel  
**Status:** all six pairwise color-generator matrices and the color-conservation sum pass exact SU(3) checks. No loop kernel or UV pole is calculated here.

## 1. External-leg ordering and color basis

For the \(d^\dagger d\) channel, after the spinor Fierz rearrangement the external fields are ordered as
\[
(\bar Q,\ Q,\ \bar d,\ d),
\]
with color indices \((i,j,k,l)\). All four external legs are treated as outgoing. Fundamental and antifundamental generators act as
\[
T^A_q=T^A,\qquad T^A_{\bar q}=-T^{A\,T},
\qquad \operatorname{tr}(T^AT^B)=\frac12\delta^{AB}.
\]

Use the two-current basis
\[
C_1^{ij;kl}=\delta_{ij}\delta_{kl},\qquad
C_8^{ij;kl}=T^A_{ij}T^A_{kl}.
\]
The source-pair contraction before spinor Fierz is
\[
(\bar Q_a d_a)(\bar d_b Q_b).
\]
After crossing the spinor pairing, its color tensor is
\[
C_X^{ij;kl}=\delta_{il}\delta_{kj}.
\]
The exact SU(3) completeness relation gives
\[
\boxed{C_X=\frac13C_1+2C_8.}
\]
Thus the tree-level source tensor is the color vector
\[
c_X=\begin{pmatrix}1/3\\2\end{pmatrix}
\]
in the ordered basis \((C_1,C_8)\). A singlet-current-only truncation is not closed under QCD exchange.

## 2. Pairwise exchange matrices

Define the color operator for an exchange between external legs \(a,b\) by
\[
\mathbf T_a\!\cdot\!\mathbf T_b
=\sum_A T_a^A T_b^A.
\]
The matrix convention is
\[
\mathbf T_a\!\cdot\!\mathbf T_b\, C_\alpha
=\sum_{\beta=1,8} C_\beta
\left(M_{ab}\right)_{\beta\alpha}.
\]
With the outgoing-leg antifundamental sign fixed above, explicit Gell-Mann matrices give:

| Exchanged legs | \(M_{ab}\) in \((C_1,C_8)\) |
|---|---|
| \(\bar Q,Q\) | \(\begin{pmatrix}-4/3&0\\0&1/6\end{pmatrix}\) |
| \(\bar Q,\bar d\) | \(\begin{pmatrix}0&2/9\\1&-1/3\end{pmatrix}\) |
| \(\bar Q,d\) | \(\begin{pmatrix}0&-2/9\\-1&-7/6\end{pmatrix}\) |
| \(Q,\bar d\) | \(\begin{pmatrix}0&-2/9\\-1&-7/6\end{pmatrix}\) |
| \(Q,d\) | \(\begin{pmatrix}0&2/9\\1&-1/3\end{pmatrix}\) |
| \(\bar d,d\) | \(\begin{pmatrix}-4/3&0\\0&1/6\end{pmatrix}\) |

The matrices are the color-generator factors only. The relative signs from the actual Feynman rules, fermion flow, momentum routing, and Lorentz numerator remain attached to the corresponding diagram; they must not be inferred from this table alone.

## 3. Exact color-conservation check

The four external legs form a total color singlet. Therefore
\[
\left(\sum_{a<b}\mathbf T_a\!\cdot\!\mathbf T_b\right)C
=-\frac12\left(\sum_a C_a\right)C
=-2C_F C
=-\frac83 C.
\]
The six matrices above satisfy
\[
\boxed{\sum_{a<b}M_{ab}=-\frac83\,\mathbf1_{2\times2}.}
\]
They also reproduce the direct action of every pairwise generator on the crossed source tensor \(C_X\). This is a useful independent check on the antifundamental signs and the singlet/octet normalization.

## 4. How this enters the QCD UV calculation

For the \(d^\dagger d\) pilot, the six one-gluon exchange topologies are:
\[
(\bar Q,Q),\quad(\bar Q,\bar d),\quad(\bar Q,d),\quad
(Q,\bar d),\quad(Q,d),\quad(\bar d,d).
\]
Each topology carries its own Dirac/momentum kernel multiplied by the corresponding \(M_{ab}\). The four derivative placements remain separate kinematic labels until the complete local UV polynomial is projected.

The source \(J_d=\bar d_RY_d^\dagger Q_L\) is a color singlet. Its composite covariant derivative has no direct QCD connection. If the operator is expanded into derivatives on the individual constituent fields, the QCD gauge-contact pieces cancel only in the complete product-rule sum. If the crossed color tensor is instead represented by singlet/octet currents, the octet currents require adjoint-covariant derivatives and their contact vertices. The two descriptions must agree after the full derivative-placement sum; omitting the octet contact terms in the Fierz basis would spoil that equivalence.

The color matrices here are therefore reusable factors for the loop kernels, not a substitute for the full covariant-derivative Feynman rules. The QCD pilot must still include external-leg counterterms and the complete gauge-invariant sum.

## 5. Validation and boundary

The companion exact-arithmetic script:
- constructs all eight \(SU(3)\) generators with \(\operatorname{tr}(T^AT^B)=\delta^{AB}/2\);
- checks \(C_X=C_1/3+2C_8\) component by component;
- evaluates all six \(\mathbf T_a\cdot\mathbf T_b\) actions on both basis tensors;
- reconstructs each action in the \((C_1,C_8)\) basis;
- checks the total color-conservation identity.

The audit passes exactly. It does **not** evaluate any one-loop momentum integral, Dirac numerator, UV pole, wavefunction counterterm, \(Z\) matrix, anomalous dimension, or finite matching coefficient. The next calculation is the Feynman-gauge/nonexceptional-momentum QCD kernel for each of these six topologies, with the original covariant-derivative operator and the Fierz/color basis cross-checked.
