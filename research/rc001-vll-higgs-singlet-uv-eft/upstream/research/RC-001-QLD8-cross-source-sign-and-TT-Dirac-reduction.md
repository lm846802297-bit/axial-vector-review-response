# RC-001 QLD8: signed cross-source graphs and D-dimensional TT reduction

**Date:** 2026-11-10  
**Stage:** P1.5a–P1.5b  
**Status:** the common Feynman-rule phase and all relative graph/Dirac/color signs are fixed in the stated convention. The four rank-two × rank-two kernels have been contracted and combined into a compact exact-\(D\) tensor. The complete SS+TS+ST+TT counterterm basis, external-gluon gauge completion, and EOM/IBP quotient remain separate acceptance gates.

## 1. Frozen conventions

Keep the original direct spinor pairing
\[
(\bar Q,d)\otimes(\bar d,Q),
\]
with all external momenta incoming at the insertion,
\[
\bar Q(p_1),\quad d(p_2),\quad \bar d(p_3),\quad Q(p_4),
\qquad p_1+p_2+p_3+p_4=0.
\]
The direct color basis is \((C_{1,d},C_{8,d})\), and the tree vector is \((1,0)_d\). No d-dimensional spinor Fierz transformation is used.

Use the propagators and vertices fixed in the open-line numerator note:
\[
S_F(r)=\frac{i\slashed r}{r^2+i0},\qquad
V^\rho=ig_s\gamma^\rho T^A,\qquad
D_{\rho\sigma}^{AB}(\ell)=\frac{-i\delta^{AB}g_{\rho\sigma}}{\ell^2+i0}.
\]
The source insertion is \(iC[q_A^{(ab)}]^2\), with the topology-dependent momentum routing already fixed in P1.1b.

## 2. P1.5a: graph phases and relative signs

For any one of the four cross-source exchanges, the common pre-loop phase is
\[
(iC)(ig_s)^2(i)^2(-i)=+Cg_s^2.
\]
There is no closed fermion loop. The external flavors \(Q\) and \(d\) are distinct, and the external field order is kept fixed, so no additional topology-dependent Grassmann permutation is introduced. With the all-outgoing color-charge convention, the anti-quark representation sign is already included through
\[
T_{\bar q}^A=-T^{A\,T};
\]
it must not be inserted a second time into the Dirac chain.

The logarithmic master integral is normalized by the positive Euclidean UV residue used in P1.4b,
\[
\left.\int\frac{d^D\ell}{(2\pi)^D}
\frac{1}{(\ell^2-m_{\rm IR}^2+i0)^2}\right|_{\rm UV}
=\frac{i}{16\pi^2\epsilon}.
\]
Thus the four graphs have one common \(+i\) 1PI phase in this convention. The counterterm insertion has the opposite sign.

The direct-color action on the tree singlet gives the four cross-source weights
\[
(-1,+1,+1,-1)
\]
for \((\bar Q,Q),(\bar Q,\bar d),(Q,d),(\bar d,d)\), respectively. These are octet components; each cross-source graph has zero singlet component when acting on the tree vector.

Define the Dirac-chain signs relative to the scalar seed \(P_R\otimes P_L\), the mixed seeds \(\Gamma^{\mu\nu}P_R\otimes P_L\) and \(P_R\otimes\Gamma^{\mu\nu}P_L\), and the common TT seed
\[
X_{\alpha\beta}
=(\Gamma^{\alpha\rho}P_R)\otimes(\Gamma^\beta{}_{\rho}P_L),
\qquad \Gamma^{\mu\nu}=\gamma^{[\mu}\gamma^{\nu]}.
\]
The exact direct-pairing Clifford decompositions give:

| Topology | Color action | SS chain | TS chain | ST chain | TT chain relative to \(X\) | Final SS | Final TS | Final ST | Final TT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \((\bar Q,Q)\) | \(-1\) | \(+1\) | \(-1\) | \(-1\) | \(-1\) | \(-1\) | \(+1\) | \(+1\) | \(+1\) |
| \((\bar Q,\bar d)\) | \(+1\) | \(+1\) | \(-1\) | \(+1\) | \(+1\) | \(+1\) | \(-1\) | \(+1\) | \(+1\) |
| \((Q,d)\) | \(+1\) | \(+1\) | \(+1\) | \(-1\) | \(+1\) | \(+1\) | \(+1\) | \(-1\) | \(+1\) |
| \((\bar d,d)\) | \(-1\) | \(+1\) | \(+1\) | \(+1\) | \(-1\) | \(-1\) | \(-1\) | \(-1\) | \(+1\) |

The final TS and ST signs reproduce the already audited mixed-tensor combinations \((+,-,+,-)\) and \((+,+,-,-)\). A key point is that the final TT signs are all positive: the Lorentz-index reversal signs must be multiplied by the color weights before combining the four tensor integrals.

## 3. P1.5b: exact D-dimensional TT contraction

The four raw TT chains are
\[
\begin{aligned}
K_{TT}^{(1)}&=I_{\alpha\beta}^{(1)}
(\Gamma^{\rho\alpha}P_R)\otimes(\Gamma^\beta{}_{\rho}P_L),\\
K_{TT}^{(2)}&=I_{\alpha\beta}^{(2)}
(\Gamma^{\rho\alpha}P_R)\otimes(\Gamma_{\rho}{}^\beta P_L),\\
K_{TT}^{(3)}&=I_{\alpha\beta}^{(3)}
(\Gamma^{\alpha\rho}P_R)\otimes(\Gamma^\beta{}_{\rho}P_L),\\
K_{TT}^{(4)}&=I_{\alpha\beta}^{(4)}
(\Gamma^{\alpha\rho}P_R)\otimes(\Gamma_{\rho}{}^\beta P_L).
\end{aligned}
\]
Use the exact, dimension-independent antisymmetry identities
\[
\Gamma^{\rho\alpha}=-\Gamma^{\alpha\rho},\qquad
\Gamma_{\rho}{}^\beta=-\Gamma^\beta{}_{\rho}.
\]
Then the direct-color weighted sum is
\[
\boxed{
-K_{TT}^{(1)}+K_{TT}^{(2)}+K_{TT}^{(3)}-K_{TT}^{(4)}
=J_{\alpha\beta}(D)X^{\alpha\beta},
}
\]
where the tensor on the right is the **sum**, not the alternating sum,
\[
J_{\alpha\beta}=I_{\alpha\beta}^{(1)}+I_{\alpha\beta}^{(2)}
+I_{\alpha\beta}^{(3)}+I_{\alpha\beta}^{(4)}.
\]

For compactness define
\[
q=p_1+p_2=-(p_3+p_4),\qquad d=p_1-p_2,\qquad R=p_3-p_4.
\]
Substituting the full P1.4b2 tensor for all four ordered pairs and using momentum conservation gives the exact identity
\[
\boxed{
\begin{aligned}
J_{\alpha\beta}(D)
={}&\frac{D}{24}(d_\alpha d_\beta+R_\alpha R_\beta)
-\frac{D+12}{24}q_\alpha q_\beta\\
&+\frac{g_{\alpha\beta}}{48}
\left[D(d^2+R^2)+(D-20)q^2\right].
\end{aligned}}
\]
The combined tensor is exactly symmetric, \(J_{\alpha\beta}=J_{\beta\alpha}\); the antisymmetric pieces of the four individual topology tensors cancel in the full TT sum. An independent symbolic-\(D\) transverse-metric check, with both free indices orthogonal to all external momenta, separately reproduces the coefficient multiplying \(g_{\alpha\beta}\).

### 3.1 Explicit \(O(\epsilon)\) form

For \(D=4-2\epsilon\),
\[
\begin{aligned}
J_{\alpha\beta}={}&
\frac16(d_\alpha d_\beta+R_\alpha R_\beta)
-\frac23q_\alpha q_\beta
+\frac{g_{\alpha\beta}}{12}(d^2+R^2-4q^2)\\
&+\epsilon\left[
-\frac1{12}(d_\alpha d_\beta+R_\alpha R_\beta)
+\frac1{12}q_\alpha q_\beta
-\frac{g_{\alpha\beta}}{24}(d^2+R^2+q^2)
\right]+O(\epsilon^2).
\end{aligned}
\]
No \(O(\epsilon)\) numerator coefficient is discarded. Since the common UV factor contains \(1/\epsilon\), this part contributes to the finite local scheme matching.

### 3.2 Evanescent diagnostic

The metric part contains the direct-pairing operator seed
\[
E_{TT}^{LR}
=g_{\alpha\beta}(\Gamma^{\alpha\rho}P_R)\otimes
(\Gamma^\beta{}_{\rho}P_L)
=(\Gamma^{\mu\nu}P_R)\otimes(\Gamma_{\mu\nu}P_L).
\]
An explicit four-dimensional chiral-matrix check gives \(E_{TT}^{LR}=0\), as expected from the opposite dualities of the two chiral tensor bilinears. This is only an evanescence diagnostic. The operator is retained as a D-dimensional seed; it is **not** set to zero in the UV subtraction and no four-dimensional Fierz identity is used.

## 4. Pole normalization and scope

The tensor integral is normalized with the common factor
\[
\frac{\Gamma(\epsilon)}{(4\pi)^{D/2}}(m_{\rm IR}^2)^{-\epsilon}.
\]
At the pole this gives \(1/(16\pi^2\epsilon)\). With the common phase fixed above, the TT contribution to the 1PI four-point function is
\[
\mathcal M_{TT,\,\rm div}^{(1)}
= iC\frac{g_s^2}{16\pi^2\epsilon}
J_{\alpha\beta}^{(0)}
(\Gamma^{\alpha\rho}P_R)\otimes(\Gamma^\beta{}_{\rho}P_L)
+\text{finite},
\]
where \(J^{(0)}\) is the \(D\to4\) coefficient. The displayed \(J^{(1)}\) above is retained for the finite term generated by multiplying the pole. The counterterm has the opposite sign.

This closes the graph-sign and raw D-dimensional TT-kernel tasks. It does **not** yet constitute the merged SS+TS+ST+TT direct-pairing counterterm, a minimal physical/evanescent \(Z\) block, the external-background-gluon completion, or the EOM/IBP quotient. No final anomalous dimension or finite Wilson coefficient is claimed.

## 5. Reproducibility

The companion script
calculations/RC-001-QLD8-cross-source-sign-TT-audit.py
checks the exact compact \(J_{\alpha\beta}(D)\) identity, symmetry, the independent symbolic-\(D\) transverse-metric coefficient, the \(D=4-2\epsilon\) expansion, the Feynman-rule phase product, all final sign weights, 64 explicit four-dimensional gamma-index sign identities, a direct 16×16 matrix comparison of the four TT topologies, and the four-dimensional evanescence of \(E_{TT}^{LR}\). The recorded output is
validation/RC-001-QLD8-cross-source-sign-TT-audit.txt.

The matrix checks are finite-dimensional diagnostics of the index/sign algebra only; the UV kernel and its \(D\)-dependence are obtained from the symbolic D-dimensional tensor expression. No CI pass is claimed by this local audit.
