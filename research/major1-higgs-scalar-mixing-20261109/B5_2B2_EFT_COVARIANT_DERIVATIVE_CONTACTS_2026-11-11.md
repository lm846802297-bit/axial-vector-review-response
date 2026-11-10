# B5-2B2 — EFT covariant-derivative contact vertices for \(Q_{LD}\) and \(Q_{RD}\)

**Date:** 2026-11-11  
**Status:** the Abelian contact terms and the absence of a direct \(W^I\) contact are derived exactly from the covariant derivative. Both flavor signs are checked. This is the EFT-insertion contact sub-block only; it is not a loop integral, a complete Ward identity, or a finite matching coefficient.

## 1. Conventions and differentiated composites

Use
\[
D_\mu=\partial_\mu
-i g_Y Y B_\mu
-i g_X X A'_\mu
-i g_2 T^I W_\mu^I,
\qquad T^I=\frac{\sigma^I}{2}.
\]
The derivative in the tree-level EFT operators acts on the composites
\[
\Psi_{L,\ell}=H^\dagger L_\ell,\qquad
\Psi_{R,\ell}=S_\ell\ell_R,
\]
so that
\[
Q_{LD,\ell}=\Psi_{L,\ell}^\dagger i\slashed D\Psi_{L,\ell},
\qquad
Q_{RD,\ell}=\Psi_{R,\ell}^\dagger i\slashed D\Psi_{R,\ell}.
\]
The model charges are
\[
Y(H)=+\frac12,\quad Y(L_\ell)=-\frac12,\quad
Y(S_\ell)=0,\quad Y(\ell_R)=-1,
\]
\[
X(L_\ell)=\eta_\ell Q_\ell,\quad
X(S_\ell)=2\eta_\ell Q_\ell,\quad
X(\ell_R)=-\eta_\ell Q_\ell,
\qquad
\eta_\mu=+1,\quad\eta_\tau=-1.
\]
Consequently,
\[
\boxed{
(Y,X,SU(2))(\Psi_{L,\ell})
=(Y,X,SU(2))(\Psi_{R,\ell})
=(-1,\eta_\ell Q_\ell,\mathbf1).
}
\]
The equality of these composite charges is the reason that the two EFT insertion contact vertices have the same Abelian coefficients. This is consistent with the charge assignment in the upstream RC-001 dimension-six gauge atlas, §5, and the one-gauge-field form-factor atlas, §3; the present B5-2B2 record makes the flavor-resolved contact coefficients explicit for the axial model.

## 2. Direct derivation of the contact terms

For a composite \(\Psi\) with Abelian charges \(Y_\Psi,X_\Psi\),
\[
i\slashed D\Psi
=i\slashed\partial\Psi
+g_Y Y_\Psi\slashed B\Psi
+g_X X_\Psi\slashed A'\Psi
+g_2 T_\Psi^I\slashed W^I\Psi.
\]
Both \(\Psi_{L,\ell}\) and \(\Psi_{R,\ell}\) are weak singlets, so \(T_\Psi^I=0\). With \(Y_\Psi=-1\) and \(X_\Psi=\eta_\ell Q_\ell\),
\[
\boxed{
Q_{LD,\ell}\supset
-g_Y B_\mu\,\mathcal J_{L,\ell}^\mu
+\eta_\ell Q_\ell g_X A'_\mu\,\mathcal J_{L,\ell}^\mu,
}
\]
\[
\boxed{
Q_{RD,\ell}\supset
-g_Y B_\mu\,\mathcal J_{R,\ell}^\mu
+\eta_\ell Q_\ell g_X A'_\mu\,\mathcal J_{R,\ell}^\mu,
}
\]
where
\[
\mathcal J_{L,\ell}^\mu
=(\bar L_\ell H)\gamma^\mu(H^\dagger L_\ell),
\qquad
\mathcal J_{R,\ell}^\mu
=(S_\ell^\dagger S_\ell)
(\bar\ell_R\gamma^\mu\ell_R).
\]
Thus the contact coefficient is \(-g_Y\) for \(B_\mu\), \(+\eta_\ell Q_\ell g_X\) for \(A'_\mu\), and zero for a direct \(W_\mu^I\) contact. In the EFT Lagrangian these terms are multiplied by \(C_{LD,\ell}\) or \(C_{RD,\ell}\), respectively.

For \(\mu\) and \(\tau\) explicitly:
\[
\begin{array}{c|rrr}
 & B_\mu & A'_\mu & W_\mu^I\\ \hline
Q_{LD,\mu}\ {\rm contact} &-g_Y&+Q_\ell g_X&0\\
Q_{LD,\tau}\ {\rm contact} &-g_Y&-Q_\ell g_X&0\\
Q_{RD,\mu}\ {\rm contact} &-g_Y&+Q_\ell g_X&0\\
Q_{RD,\tau}\ {\rm contact} &-g_Y&-Q_\ell g_X&0
\end{array}
\]
The \(\tau\) sign reversal is only in the \(A'\) contact, because \(S_\tau=S^\ast\) changes the composite \(X\)-charge. The hypercharge contact is flavor independent.

## 3. Why the direct \(W^I\) contact vanishes

For the left composite, the weak-covariant product rule gives
\[
D_\mu(H^\dagger L_\ell)
=(D_\mu H)^\dagger L_\ell+H^\dagger D_\mu L_\ell.
\]
The weak pieces cancel:
\[
(D_\mu H)^\dagger L_\ell\big|_W
=+ig_2H^\dagger T^I W_\mu^I L_\ell,
\]
\[
H^\dagger D_\mu L_\ell\big|_W
=-ig_2H^\dagger T^I W_\mu^I L_\ell,
\]
and hence
\[
D_\mu(H^\dagger L_\ell)\big|_W=0.
\]
This is the direct consequence of \(H^\dagger L_\ell\) being an \(SU(2)_L\) singlet. The right composite \(S_\ell\ell_R\) is also an \(SU(2)_L\) singlet, so it has no \(W^I\) coupling at the composite derivative insertion.

This does **not** remove \(WW\) corrections to \(Q_{LD}\): virtual \(W\) bosons still attach to the individual external \(L_\ell\) and \(H\) lines in the UV and EFT amplitudes. It does mean that no \(W^I\) contact graph is to be added at the \(Q_{LD}\) derivative insertion. There is no \(WW\) sector for \(Q_{RD}\), whose elementary fields are all weak singlets.

## 4. Consequences for the UV–EFT subtraction

The EFT side of every \(Q_{LD}\) or \(Q_{RD}\) gauge correction must include:
1. the ordinary virtual-gauge attachments to the individual external matter lines;
2. the \(B_\mu\) and \(A'_\mu\) derivative-contact graphs above;
3. the same external-leg/LSZ and parameter-renormalization convention used on the UV side;
4. the appropriate mixed-propagator attachments if the renormalized \(B-A'\) kinetic matrix is non-diagonal.

The contact term is a five-point EFT insertion (two fermions, two scalars, one gauge field). It is not itself a local four-point Wilson coefficient. Its role is to complete the gauge-covariant derivative insertion and the Ward identity. Do not replace it by a gauge-reducible current-exchange graph or count it again as a separate four-point local operator.

For a mixed \(B-A'\) propagator, the contact vertices are unchanged; the off-diagonal propagator contracts the \(B\) and \(A'\) endpoints. Its contribution remains conditional on the chosen kinetic-mixing boundary and propagator convention. The present result assumes only the diagonal contact vertices and does not set or calculate a mixed four-point coefficient.

## 5. Exact audit and acceptance boundary

The companion script b5_2b2_eft_contact_vertex_audit.py checks:
- \(Y(H^\dagger L_\ell)=Y(S_\ell\ell_R)=-1\);
- \(X(H^\dagger L_\ell)=X(S_\ell\ell_R)=\eta_\ell Q_\ell\) for both \(\eta_\ell=\pm1\);
- equality of the \(Q_{LD}\) and \(Q_{RD}\) Abelian contact coefficients;
- the opposite \(\mu/\tau\) \(A'\) contact signs;
- exact cancellation of the \(W^I\) terms in \(D_\mu(H^\dagger L_\ell)\).

The local symbolic reproduction passes these charge and weak-generator identities. The regression tests are in test_b5_2b2_eft_contact_vertex_audit.py.

**Not claimed:** no UV gauge-loop numerator, Feynman integral, UV/IR pole table, finite \(O(g^2/M_E^2)\) matching coefficient, summed Ward identity, or complete current anomalous-dimension matrix has been calculated here.

The next calculation can now use a fixed EFT contact-vertex set. Begin with the \(BB\) and \(WW\) \(Q_{LD}\) amplitudes, remembering that the \(WW\) sector has no derivative-insertion contact but does have matter-line attachments. Then evaluate the \(A'A'\) \(Q_{LD}\) and \(BB/A'A'\) \(Q_{RD}\) sectors separately.
