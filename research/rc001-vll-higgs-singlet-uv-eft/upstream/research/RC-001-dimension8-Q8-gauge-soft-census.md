# RC-001 — Gauge-covariant soft-sector expansion and diagram census for Q8

**Status (2026-11-10):** the exact covariant operator identity and the O(g^2) topology census are recorded. No gauge-corrected soft loop integral has yet been evaluated. In particular, no Ward-identity or UV-pole cancellation is claimed.

## 1. Scope and conventions

For either source spinor
\[
\Psi_{L,\ell}=H^\dagger L_\ell,\qquad
\Psi_{R,\ell}=S_\ell\ell_R,
\]
the tree-level dimension-eight operators are
\[
Q_{a,\ell}^{(8)}=\bar\Psi_{a,\ell}(i\slashed D_a)^3\Psi_{a,\ell},
\qquad
c_{L,\ell}^{(8)}=\frac{|y_\ell|^2}{M_{E\ell}^4},\quad
c_{R,\ell}^{(8)}=\frac{|\lambda_\ell|^2}{M_{E\ell}^4}.
\]
Here D_a is the connection in the representation carried by the complete composite source \Psi_a. The covariant derivative must act on the entire product. The calculation is first organized in the unbroken phase and in a general background gauge field; representation generators and gauge couplings are restored group by group.

Use
\[
[D_\mu,D_\nu]\Psi_a\equiv\Omega_{\mu\nu}^{(a)}\Psi_a,\qquad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].
\]
This definition avoids prematurely fixing the sign convention for \Omega in terms of \(g F_{\mu\nu}^A T^A\). That sign must be matched to the repository's covariant-derivative convention before numerical group factors are inserted.

## 1A. Frozen model representations for the two composite sources

Use the charge table already frozen in the RC-001 dimension-six gauge atlas, with \(\eta_\mu=+1\), \(\eta_\tau=-1\), and \(x=Q_X/Q_\ell\):
\[
\begin{array}{c|ccc}
 & SU(2)_L & Y & x\\ \hline
H&\mathbf2&+\frac12&0\\
L_\ell&\mathbf2&-\frac12&\eta_\ell\\
\ell_R&\mathbf1&-1&-\eta_\ell\\
S_\ell&\mathbf1&0&+2\eta_\ell\\
E_\ell&\mathbf1&-1&+\eta_\ell
\end{array}
\]
The complete composite sources therefore transform as
\[
\Psi_{L,\ell}=H^\dagger L_\ell:
\quad (\mathbf1,-1,+\eta_\ell),
\qquad
\Psi_{R,\ell}=S_\ell\ell_R:
\quad (\mathbf1,-1,+\eta_\ell).
\]
Thus both source spinors transform in exactly the same gauge representation as \(E_\ell\). This is the representation on which the covariant derivative inside the Q8 operator acts. The exact charge check is archived in calculations/RC-001-dimension8-Q8-representation-audit.py and validation/RC-001-dimension8-Q8-representation-audit.txt.

Important distinction for the diagram ledger:
- At the **Q8 insertion itself**, the composite connection contains \(B_\mu\) and \(A'_\mu\), but no direct \(W_\mu^I\) connection because \(H^\dagger L_\ell\) is an SU(2) singlet and \(S_\ell\ell_R\) is also a singlet.
- In the **full QLD soft amplitude**, ordinary \(W\) exchange still attaches separately to the \(L_\ell\) and \(H\) constituent lines. The absence of a direct W contact at the composite Q8 insertion does not remove those diagrams.
- The QRD amplitude has no W attachments because both \(\ell_R\) and \(S_\ell\) are SU(2) singlets.

The normalized X charges of \(S_\mu=S\) and \(S_\tau=S^*\) are respectively \(+2\) and \(-2\); the corresponding composite source charge is \(+\eta_\ell\) in both flavor sectors. This fixes the relative sign of the \(A'\) vertices before loop integration.

## 2. Exact covariant expansion

The Clifford identity is
\[
(i\slashed D)^2=-D^2+\frac{i}{2}\sigma^{\mu\nu}\Omega_{\mu\nu}.
\]
Consequently, with the operator ordering acting on the complete \Psi,
\[
\boxed{
(i\slashed D)^3\Psi
=-i\gamma^\rho D_\rho D^2\Psi
-\frac12\gamma^\rho\sigma^{\mu\nu}
\left[(D_\rho\Omega_{\mu\nu})\Psi+
\Omega_{\mu\nu}D_\rho\Psi\right].
}
\]
The derivative on \Omega is the adjoint covariant derivative. The second line is the explicit field-strength sector; neither term may be dropped. The first term also contains gauge interactions through all three covariant derivatives.

The first term is an ordered product of three covariant derivatives. Its one-, two-, and three-gauge-field vertices are to be generated recursively from
\[
D_\mu=\partial_\mu+\mathcal A_\mu,\qquad
D_\rho D_\mu D^\mu\Psi
=(\partial_\rho+\mathcal A_\rho)
(\partial_\mu+\mathcal A_\mu)
(\partial^\mu+\mathcal A^\mu)\Psi,
\]
without commuting adjacent \(D\)'s. This compact ordered expression is the definition used for the vertex expansion. The commutator terms in \(\Omega_{\mu\nu}\) reorganize the antisymmetric field-strength content and must be retained together with the ordered derivative vertices.
## 3. Soft topology census at quadratic gauge order

The previously evaluated gauge-free one-insertion scalar tadpole is zero because it is scaleless. The first gauge-corrected contribution to that same two-external-scalar projection is order \(g_A^2 c_a^{(8)}\). It is a **two-loop EFT contribution**: one closed light-fermion loop plus one internal gauge propagator (or an equivalent gauge tadpole contraction). It must not be described as a one-loop Q8 correction.

For each gauge factor A, the complete O(g_A^2) census for the scalar two-point projection contains:

1. **Ordinary fermion-line exchange:** two standard gauge vertices on the closed light-fermion loop, joined by one gauge propagator. Include both orderings around the loop.
2. **One-Q8-gauge contact plus one ordinary vertex:** the term linear in \mathcal A from the covariant Q8 insertion joined to one ordinary fermion-gauge vertex. Include all placements and both orientations.
3. **Two-gauge contact at Q8:** the quadratic-\mathcal A term from the covariant Q8 insertion with its two gauge legs contracted.
4. **Field-strength contact sector:** the \Omega_{\mu\nu}D_\rho and (D_\rho\Omega_{\mu\nu}) terms, including their one- and two-gauge-field pieces. These must be combined with items 1–3 rather than counted as extra independent copies when they are simply another expansion of the same covariant vertex.
5. **Gauge-fixing/ghost sector:** include only if the chosen gauge and external Green function produce a ghost attachment at this order; ghosts do not couple directly to the fermion bilinear, so there is no automatic ghost graph.
6. **Counterterm insertions:** Q8 operator renormalization, light-fermion wavefunction/gauge-vertex counterterms, and any lower-dimensional counterterm mixing allowed by the chosen off-shell projection.

For a non-Abelian factor, include the generator products and the gauge self-interaction/ghost contributions required by the Ward/Slavnov–Taylor identity. For Abelian U(1) factors, the structure simplifies but the contact terms remain mandatory.

## 4. Group and flavor bookkeeping

Do not combine the gauge groups into a single effective \(g^2\). Keep separate labels for every representation acting on \Psi_L and \Psi_R. The \(Q_{LD}^{(8)}\) source is \(H^\dagger L_\ell\); the \(Q_{RD}^{(8)}\) source is \(S_\ell\ell_R\). Their quadratic Casimirs and Abelian charges are not interchangeable.

The flavor sum is over \ell=\mu,\tau with the original model's \(S_\mu=S\), \(S_\tau=S^*\) convention. The conjugate scalar reverses the Abelian charge, but a quadratic charge factor is unchanged. Do not add a \mu-\tau interference term without a flavor-changing insertion.

## 5. Required integral and Ward-identity checks

For each group factor and each of L/R sectors:

- keep nonzero external Euclidean momentum until UV and IR poles have been separated;
- calculate the ordinary exchange, one-gauge contact, two-gauge contact, and field-strength pieces with a common routing and regulator;
- sum the complete gauge-covariant set before testing transversality;
- verify the appropriate Ward identity (Abelian) or Slavnov–Taylor identity (non-Abelian);
- reduce the local UV pole to a gauge-invariant operator basis, retaining EOM/source operators;
- only then compare the soft UV pole with the IR pole of the corresponding full-theory hard region.

A vanishing gauge-free scaleless tadpole is not evidence that the gauge-corrected sum vanishes. Conversely, an individual gauge-dependent diagram is not a physical contribution before the covariant set is summed.

## 6. Explicit acceptance boundary

Completed in this record:
- exact ordered covariant identity for \((i\slashed D)^3\);
- identification of the field-strength and derivative-of-field-strength pieces;
- O(g^2) diagram census for the restricted scalar two-point projection;
- correct loop-order classification as two-loop EFT.

Not completed:
- fixing every model-specific generator/charge and sign from the frozen UV convention;
- explicit two-loop soft integrals for \(Q_{LD}^{(8)}\) and \(Q_{RD}^{(8)}\);
- Ward/Slavnov–Taylor sum;
- local UV-pole and counterterm mixing matrix;
- matching hard regions and finite Wilson coefficients;
- independent diagram-generation validation.

No gauge-corrected Q8 soft coefficient or dimension-eight Wilson coefficient is claimed.
