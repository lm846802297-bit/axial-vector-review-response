# RC-001 QLD8 non-Abelian IBP/EOM completion

## Scope and conventions

This note extends the Abelian transverse-pair reduction in the parent QLD one-background record to the full electroweak covariant derivative. It is an operator-algebra result; it does not add a loop integral or close the full dimension-eight Wilson vector.

Use
\[
D_\mu H=\left(\partial_\mu+i g'Y_H B_\mu+i g_2W_\mu^aT^a\right)H,
\qquad Y_H=\frac12,\qquad T^a=\frac{\sigma^a}{2},
\]
and \(q_X(H)=0\). Define the matrix-valued curvature by
\[
[D_\mu,D_\nu]H=i\mathscr F_{\mu\nu}H,\qquad
\mathscr F_{\mu\nu}=g'Y_HB_{\mu\nu}\mathbf1+g_2W_{\mu\nu}^aT^a.
\]
The external-background coupling/charge factors are stripped in the same way as in §5J. For an external Abelian field \(F_A\), its insertion \(t_A\) is \(\mathbf1\); for an external weak field \(W^a\), \(t_A=T^a\). The derivative on an adjoint-valued object is
\[
(\mathcal D_\mu^{\rm adj}Z)^a
=\partial_\mu Z^a-g_2\epsilon^{abc}W_\mu^bZ^c.
\]
For the Higgs bilinears write
\[
X=H^\dagger H,\qquad X^a=H^\dagger T^aH,\qquad
j_H^\mu=iH^\dagger\overleftrightarrow D^\mu H,\qquad
j_H^{a\mu}=iH^\dagger T^a\overleftrightarrow D^\mu H.
\]

## 1. Full covariant IBP identity

For an external gauge background \(A\), define the corresponding representatives
\[
\mathcal O_P^A
=iF_A^{\mu\nu}(D_\rho D_\mu H)^\dagger t_A D^\rho D_\nu H,
\]
\[
\mathcal O_Q^A
=-i(D_\mu H)^\dagger t_A D_\nu H\,
(\mathcal D_{\rm adj}^2F_A^{\mu\nu}).
\]
For an Abelian background, \(\mathcal D_{\rm adj}^2=\Box\). For \(W^a_{\mu\nu}\), it is the adjoint covariant Laplacian and the weak generator \(T^a\) is retained between the Higgs fields.

The covariant product rule is
\[
\mathcal D_\rho^{\rm adj}
\left[(D_\mu H)^\dagger t_A D_\nu H\right]
=(D_\rho D_\mu H)^\dagger t_A D_\nu H
+(D_\mu H)^\dagger t_A D_\rho D_\nu H.
\]
For \(t_A=T^a\), the adjoint connection on the bilinear is essential; it cancels the commutator generated when the ordinary derivative acts on the generator insertion. Applying the product rule twice and integrating by parts gives
\[
\mathcal O_Q^A\doteq
-iF_A^{\mu\nu}\left[
(D^2D_\mu H)^\dagger t_A D_\nu H
+2(D_\rho D_\mu H)^\dagger t_A D^\rho D_\nu H
+(D_\mu H)^\dagger t_A D^2D_\nu H
\right].
\]
Consequently, for Abelian and non-Abelian backgrounds alike,
\[
\boxed{\mathcal O_P^A+\frac12\mathcal O_Q^A
\doteq\mathcal O_{E,H}^A}
\]
with
\[
\mathcal O_{E,H}^A
=-\frac i2F_A^{\mu\nu}\left[
(D^2D_\mu H)^\dagger t_A D_\nu H
+(D_\mu H)^\dagger t_A D^2D_\nu H
\right].
\]
Thus the amplitude-level coefficient reparameterization is unchanged:
\[
a_A\mathcal O_P^A+b_A\mathcal O_Q^A
\doteq a_A\mathcal O_{E,H}^A+
\left(b_A-\frac{a_A}{2}\right)\mathcal O_Q^A.
\]
This is an action-level identity modulo a total derivative, not a statement that the full right-hand side vanishes.

## 2. Matrix-ordered commutator completion

The step from \(D^2D_\mu H\) to \(D_\mu D^2H\) must retain the full matrix curvature:
\[
[D^2,D_\mu]H
=i\left[(\mathcal D_\rho\mathscr F^\rho{}_\mu)H
+2\mathscr F^\rho{}_\mu D_\rho H\right].
\]
Here \(\mathcal D_\rho\mathscr F\) is the matrix adjoint derivative. Writing
\(\mathcal O_{E,H}^A=\mathcal O_{E,H,\mathrm{ord}}^A+
\mathcal O_{\mathrm{comm}}^A\), with
\[
\mathcal O_{E,H,\mathrm{ord}}^A
=-\frac i2F_A^{\mu\nu}\left[
(D_\mu D^2H)^\dagger t_A D_\nu H
+(D_\mu H)^\dagger t_A D_\nu D^2H
\right],
\]
the exact matrix-ordered remainder is
\[
\boxed{\begin{aligned}
\mathcal O_{\mathrm{comm}}^A={}&
-\frac12F_A^{\mu\nu}\left[
H^\dagger(\mathcal D_\rho\mathscr F^\rho{}_\mu)t_A D_\nu H
+(D_\nu H)^\dagger t_A(\mathcal D_\rho\mathscr F^\rho{}_\mu)H
\right]\\
&-F_A^{\mu\nu}\left[
(D_\rho H)^\dagger\mathscr F^\rho{}_\mu t_A D_\nu H
+(D_\nu H)^\dagger t_A\mathscr F^\rho{}_\mu D_\rho H
\right].
\end{aligned}}
\]
The ordering \(\mathscr F t_A\) versus \(t_A\mathscr F\) is physical in the non-Abelian sector and must not be interchanged. The first line is the gauge-EOM direction; the second is the genuine two-background \(F_A\mathscr F H^2D^2\) contact family.

## 3. Explicit \(SU(2)_L\) same-group decomposition

For an external \(W^a_{\mu\nu}\) and the internal \(SU(2)_L\) part of \(\mathscr F\), the two matrix products are
\[
T^bT^a=\frac14\delta^{ab}\mathbf1-\frac i2\epsilon^{abc}T^c,
\qquad
T^aT^b=\frac14\delta^{ab}\mathbf1+\frac i2\epsilon^{abc}T^c.
\]
They give the exact bilinear identities
\[
\begin{aligned}
&H^\dagger T^bT^aD_\nu H
+(D_\nu H)^\dagger T^aT^bH\\
&\hspace{1cm}=
\frac14\delta^{ab}\partial_\nu X
-\frac12\epsilon^{abc}j_{H,\nu}^c,
\end{aligned}
\]
and
\[
\begin{aligned}
&(D_\rho H)^\dagger T^bT^aD_\nu H
+(D_\nu H)^\dagger T^aT^bD_\rho H\\
&\hspace{1cm}=
\frac14\delta^{ab}S_{\rho\nu}
+\frac12\epsilon^{abc}K_{\rho\nu}^c,
\end{aligned}
\]
where
\[
S_{\rho\nu}=(D_\rho H)^\dagger D_\nu H
+(D_\nu H)^\dagger D_\rho H,
\]
\[
K_{\rho\nu}^c
=i\left[(D_\nu H)^\dagger T^cD_\rho H
-(D_\rho H)^\dagger T^cD_\nu H\right].
\]
Therefore the same-group commutator pieces are
\[
\mathcal O_{\mathrm{comm},DW}^{W^a}
=-\frac{g_2}{2}W^{a\mu\nu}
(\mathcal D_\rho^{\rm adj}W^{\rho}{}_\mu)^b
\left(\frac14\delta^{ab}\partial_\nu X
-\frac12\epsilon^{abc}j_{H,\nu}^c\right),
\]
\[
\mathcal O_{\mathrm{comm},W^2}^{W^a}
=-g_2W^{a\mu\nu}W^{b\rho}{}_\mu
\left(\frac14\delta^{ab}S_{\rho\nu}
+\frac12\epsilon^{abc}K_{\rho\nu}^c\right).
\]
The first expression contains both a singlet Higgs-gradient current and an \(\epsilon^{abc}\) weak-current structure. The second is a genuine two-background contact and is not fixed by the one-background form-factor rank.

## 4. Mixed \(B\)-\(W\) backgrounds and the \(U(1)_X\) boundary

Restoring the full electroweak connection also generates mixed-background terms. For an external Abelian field \(F_A=B\) or \(F_X\), \(t_A=\mathbf1\), and the internal weak-field pieces are
\[
\mathcal O_{\mathrm{comm},DW}^{A\leftarrow W}
=-\frac{g_2}{2}F_A^{\mu\nu}
(\mathcal D_\rho^{\rm adj}W^{\rho}{}_\mu)^b
(\mathcal D_\nu^{\rm adj}X)^b,
\]
\[
\mathcal O_{\mathrm{comm},F W}^{A\leftarrow W}
=-g_2F_A^{\mu\nu}W^{b\rho}{}_\mu
\left[(D_\rho H)^\dagger T^bD_\nu H
+(D_\nu H)^\dagger T^bD_\rho H\right].
\]
For an external \(W^a\) and an internal hypercharge field, the corresponding terms are
\[
\mathcal O_{\mathrm{comm},\partial B}^{W^a}
=-\frac{g'Y_H}{2}W^{a\mu\nu}
(\partial_\rho B^{\rho}{}_\mu)
(\mathcal D_\nu^{\rm adj}X)^a,
\]
\[
\mathcal O_{\mathrm{comm},BW}^{W^a}
=-g'Y_HW^{a\mu\nu}B^\rho{}_\mu
\left[(D_\rho H)^\dagger T^aD_\nu H
+(D_\nu H)^\dagger T^aD_\rho H\right].
\]
For an external hypercharge field, its same-group pieces are
\[
\mathcal O_{\mathrm{comm},\partial B}^{B}
=-\frac{g'Y_H}{2}B^{\mu\nu}
(\partial_\rho B^{\rho}{}_\mu)\partial_\nu X,
\]
\[
\mathcal O_{\mathrm{comm},B^2}^{B}
=-g'Y_HB^{\mu\nu}B^\rho{}_\mu
\left[(D_\rho H)^\dagger D_\nu H
+(D_\nu H)^\dagger D_\rho H\right].
\]
For external \(F_X\), the same mixed \(B\)- and \(W\)-generated expressions apply after \(B^{\mu\nu}\) is replaced by \(F_X^{\mu\nu}\); there is no internal \(X\)-curvature because \(q_X(H)=0\).

This sharpens the charge statement in §5K.3: \(q_X(H)=0\) removes the *same-\(U(1)_X\)-sector* commutator terms in the single-Abelian-background truncation. It does **not** remove mixed \(F_XB\) or \(F_XW\) two-background contacts when the full SM covariant derivative is restored.

## 5. Gauge-EOM current representatives

With the convention \(-B_{\mu\nu}B^{\mu\nu}/4-W_{\mu\nu}^aW^{a\mu\nu}/4\), define the complete EFT matter currents by
\[
\partial_\rho B^{\rho\mu}=g'J_Y^\mu,\qquad
(\mathcal D_\rho^{\rm adj}W^{\rho\mu})^a=g_2J^{a\mu}.
\]
The currents include all charged light fields, not only the Higgs current. Thus, for an external Abelian \(F_A\),
\[
\mathcal O_{\mathrm{comm},DW}^{A\leftarrow W}
\ \longrightarrow\
-\frac{g_2^2}{2}F_A^{\mu\nu}J_\mu^b
(\mathcal D_\nu^{\rm adj}X)^b,
\]
and for external \(B\) or \(F_X\),
\[
\mathcal O_{\mathrm{comm},\partial B}^{A}
\ \longrightarrow\
-\frac{g'^2Y_H}{2}F_A^{\mu\nu}J_\mu^Y\partial_\nu X.
\]
For an external \(W^a\), the same-group weak-current term becomes
\[
\boxed{
-\frac{g_2^2}{8}W^{a\mu\nu}J_\mu^a\partial_\nu X
+\frac{g_2^2}{4}W^{a\mu\nu}\epsilon^{abc}
J_\mu^b j_{H,\nu}^c
}
\]
and the mixed hypercharge-current term becomes
\[
-\frac{g'^2Y_H}{2}W^{a\mu\nu}J_\mu^Y
(\mathcal D_\nu^{\rm adj}X)^a.
\]
Each derivative-of-field-strength representative and its gauge-EOM current representative are alternatives; they must not both be retained in the same basis.

## 6. Higgs-EOM source map with the external generator retained

The ordered part is reduced with the same project convention
\[
D^2H=-f_HH-\mathcal J_H,\qquad
f_H=-\mu_H^2+2\lambda_HX+\lambda_{HS}Y.
\]
For \(t_A=\mathbf1\) or \(T^a\), define
\[
j_H^{A\mu}=iH^\dagger t_A\overleftrightarrow D^\mu H,
\quad
\mathcal O_{FH}^{(6),A}
=iF_A^{\mu\nu}(D_\mu H)^\dagger t_A D_\nu H,
\]
\[
\mathcal O_{F\mathcal J_H}^{(8),A}
=\frac i2F_A^{\mu\nu}\left[
(D_\mu\mathcal J_H)^\dagger t_A D_\nu H
+(D_\mu H)^\dagger t_A D_\nu\mathcal J_H
\right].
\]
Then
\[
\boxed{
\mathcal O_{E,H,\mathrm{ord}}^A
\doteq f_H\mathcal O_{FH}^{(6),A}
-\frac12F_A^{\mu\nu}j_{H,\mu}^A\partial_\nu f_H
+\mathcal O_{F\mathcal J_H}^{(8),A}
+\mathcal O_{\rm EOM}^A,
\qquad
\mathcal E_H=D^2H+f_HH+\mathcal J_H,
\]
where
\[
\mathcal O_{\rm EOM}^A
=-\frac i2F_A^{\mu\nu}\left[
(D_\mu\mathcal E_H)^\dagger t_A D_\nu H
+(D_\mu H)^\dagger t_A D_\nu\mathcal E_H
\right].
\]
For an external weak field, \(j_H^{A\mu}=j_H^{a\mu}\) is the adjoint Higgs current. For external \(B\) or \(F_X\), it is the singlet current. The potential companions are obtained from
\[
\partial_\mu f_H=2\lambda_H\partial_\mu X
+\lambda_{HS}\partial_\mu Y.
\]
The Yukawa-source and source-square companions remain those listed in §5K; no source term is discarded by the non-Abelian extension. For the original axial model, the charged-lepton source uses the flavor-diagonal assumption: the \\(\bar L_\mu H\tau_R\\) and \\(\bar L_\tau H\mu_R\\) entries are gauge-allowed but set to zero by the block-diagonal model definition, whereas the diagonal \\(\mu,\tau\\) renormalizable entries are gauge-forbidden. See [RC-001-QLD-Higgs-source-EOM-model-map.md](RC-001-QLD-Higgs-source-EOM-model-map.md) for the explicit charge matrix and the dimension-five source.

## 7. Hard coefficient map and interpretation

The non-Abelian IBP identity does not alter the algebraic coefficient reparameterization. In particular, the \(SU(2)_L\) hard coefficients of §5J give
\[
b_W-\frac{a_W}{2}
=-\frac{12/\epsilon_{\rm IR}+12L_M+13}{576},
\]
with the external \(T^a\) insertion understood as in §5J. The coefficient multiplying the EOM direction and all its commutator/source companions is \(a_W\). These are still hard-region coefficients with IR poles, not finite renormalized Wilson coefficients.

The same logic applies to the Abelian sectors:
\[
b_X-\frac{a_X}{2}
=-\frac{30/\epsilon_{\rm IR}+30L_M+28}{1440},
\qquad
b_Y-\frac{a_Y}{2}
=\frac{60/\epsilon_{\rm IR}+60L_M+47}{5760}.
\]
The \(c_S=1/192\) scalar-source coefficient is a separate amplitude column and is not changed by this transverse-pair IBP identity.

## 8. Validation and acceptance boundary

The exact SymPy audit in calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py checks:
1. all nine \(SU(2)\) fundamental-generator products;
2. the adjoint product rule for \(H^\dagger T^aG\);
3. the matrix-ordered commutator formula for singlet and adjoint external insertions, with a general \(u(2)\) internal curvature containing both hypercharge and weak pieces;
4. the \(\delta^{ab}/\epsilon^{abc}\) decomposition of the derivative-current bracket;
5. the corresponding two-background \(F^2H^2D^2\) bracket;
6. the derivative-of-\(f_H\) Higgs-EOM identity for singlet and adjoint insertions;
7. the retained \(b_W-a_W/2\) hard coefficient.

This closes the algebraic non-Abelian IBP/commutator map for the restricted Higgs-current representatives. The complete **leading-renormalizable light-field** hypercharge, weak-isospin, and normalized axial \(U(1)_X\) currents for the original one-VEV model are now expanded in [RC-001-QLD-total-current-expansion.md](RC-001-QLD-total-current-expansion.md), with an exact-rational bookkeeping audit in [calculations/RC-001-QLD-total-current-expansion-audit.py](../calculations/RC-001-QLD-total-current-expansion-audit.py) and its recorded checks in [validation/RC-001-QLD-total-current-expansion-audit.txt](../validation/RC-001-QLD-total-current-expansion-audit.txt).

This closes the leading-renormalizable current expansion for the displayed gauge-EOM representatives, **not** the final nonredundant dimension-eight basis. The fermion-current operators still require fermion EOM/Fierz and flavor-basis reduction; all mixed-background structures must be included in the full off-shell Green-function matching; remaining EFT soft insertions, counterterms, and independent FeynArts/FeynCalc validation remain open.
