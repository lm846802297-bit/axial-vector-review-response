# C5 sign and gauge-convention audit (2026-11-10)

**Workstream:** axial-vector PR #69 / RC-001 interface.  
**Scope:** tree-level coefficient sign and gauge-convention dictionary only.  
**No manuscript or formal referee-response edit is made.**

## 1. Signed dimension-five coefficient

For each flavor, the displayed UV mass matrix is
\[
\mathcal M_\ell=
\begin{pmatrix}
0&y_\ell v_h/\sqrt2\\
\lambda_\ell v_s/\sqrt2&M_{E_\ell}
\end{pmatrix}.
\]
Its heavy-block Schur complement is
\[
m_{\ell,\mathrm{Schur}}
=0-\frac{y_\ell v_h}{\sqrt2}
\frac{1}{M_{E_\ell}}
\frac{\lambda_\ell v_s}{\sqrt2}
=-\frac{y_\ell\lambda_\ell v_hv_s}{2M_{E_\ell}}.
\]

With the common operator orientation
\[
\mathcal O_{5,\ell}=S_\ell\bar L_\ell H\ell_R,
\qquad
\mathcal L_{\mathrm{EFT}}^{(5)}
=-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.},
\]
the VEV insertion gives
\[
m_{\ell,\mathrm{EFT}}=C_{5,\ell}\frac{v_hv_s}{2}.
\]
Therefore
\[
\boxed{C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.}
\]
This is the RC-001 convention and follows directly from the original UV Lagrangian and mass matrix.

### Comparison with the printed v6 Eq. (5-d)

The archived v6 manuscript writes the same operator orientation and Lagrangian sign, but displays
\[
\frac{c_\ell}{\Lambda}=+\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
Identifying \(C_{5,\ell}=c_\ell/\Lambda\), this produces
\[
m_{\ell,\mathrm{EFT}}^{\mathrm{v6}}
=+\frac{y_\ell\lambda_\ell v_hv_s}{2M_{E_\ell}}
=-m_{\ell,\mathrm{Schur}}.
\]
Thus, **for the UV Lagrangian, mass-matrix entries, and operator orientation as printed, Eq. (5-d) has the opposite signed coefficient**. The matching relation consistent with those displayed definitions is the negative sign.

This does not alter the positive physical singular mass or any result depending only on \(|C_5|^2\), \(|C_5|^4\), or the squared seesaw mass. It can matter in interference terms linear in \(C_5\) or in relative phases, so one convention must be used consistently.

### Why a field rephasing does not erase the matching discrepancy

For a real right-handed light-field rephasing \(\ell_R'=-\ell_R\), the UV parameter in the same displayed Lagrangian changes as \(\lambda_\ell'=-\lambda_\ell\), and the EFT operator changes as \(\mathcal O_{5,\ell}'=-\mathcal O_{5,\ell}\). The Schur relation remains
\[
C_{5,\ell}'=-\frac{y_\ell\lambda_\ell'}{M_{E_\ell}}
=-C_{5,\ell},
\qquad
C_{5,\ell}'\mathcal O_{5,\ell}'
=C_{5,\ell}\mathcal O_{5,\ell}.
\]
The matching identity is covariant under rephasing. Rephasing the light field cannot turn \(C_5=-y\lambda/M_E\) into \(C_5=+y\lambda/M_E\) while retaining the same transformed UV parameter and the same operator orientation.

There is a related signed-eigenvalue point in the manuscript's bi-orthogonal diagonalization. For real positive \(y_\ell,\lambda_\ell,M_{E_\ell}\),
\[
\det\mathcal M_\ell=-\frac{y_\ell\lambda_\ell v_hv_s}{2}<0.
\]
The displayed \(U_{\ell L},U_{\ell R}\) are both proper rotations (\(\det=+1\)); hence their diagonal signed masses must have a negative product. In the seesaw limit the light signed eigenvalue is negative and the heavy one positive. The manuscript quotes \(m_\ell^2\), which is consistent with the magnitude, but the signed mass is not positive under those two proper rotations unless an additional sign redefinition is made.

**Internal convention decision:** keep \(C_{5,\ell}=-y_\ell\lambda_\ell/M_{E_\ell}\) for all RC-001/PR #69 calculations. Do not silently change the archived manuscript or formal reply in this research PR. If the manuscript is revised later, correct Eq. (5-d) or explicitly state a complete alternative parameter/operator convention.

## 2. Covariant-derivative sign dictionary

The original axial manuscript uses
\[
D_\mu^-=\partial_\mu-i g_Y YB_\mu^-
-i g_W T^aW_\mu^{a,-}
-i g_{A'}Q_{A'}A_\mu^{\prime-},
\]
whereas the RC-001 electroweak background-field note uses
\[
D_\mu^+=\partial_\mu+i g'YB_\mu^+
+i g_2T^aW_\mu^{a,+}.
\]
Choose
\[
g'=g_Y,\qquad g_2=g_W,\qquad
B_\mu^+=-B_\mu^-,
\quad W_\mu^{a,+}=-W_\mu^{a,-},
\quad A_\mu^{\prime+}=-A_\mu^{\prime-}.
\]
The charge generators are unchanged. In the axial model \(g_X=g_{A'}Q_\ell\); the upstream normalized \(U(1)_X\) charge is \(x=Q_{A'}/Q_\ell\), so the physical product \(g_Xx\) is unchanged.

Then
\[
\boxed{D_\mu^+=D_\mu^-}
\]
on every field, including the charged VLL/light-fermion composites. In particular \(Q_X(H)=0\) in both conventions. Higgs and fermion currents built from the same covariant derivative are unchanged.

For the raw component field strengths, with each convention's non-Abelian commutator term defined consistently with its \(D_\mu\),
\[
F_{\mu\nu}^{a,+}=-F_{\mu\nu}^{a,-},
\qquad B_{\mu\nu}^+=-B_{\mu\nu}^-,
\qquad F_{\mu\nu}^{\prime+}=-F_{\mu\nu}^{\prime-}.
\]
However the matrix curvature defined by
\[
[D_\mu,D_\nu]=i\mathscr F_{\mu\nu}
\]
is invariant:
\[
\mathscr F_{\mu\nu}^+=\mathscr F_{\mu\nu}^-.
\]
The adjoint derivative acting on this curvature is therefore also the same after the field map.

### Operator-level consequences

| Object | Under \(A_+=-A_-\) |
|---|---|
| \(D_\mu\), \(D^2\), Higgs/fermion currents | unchanged |
| Raw component \(F_{\mu\nu}\) | changes sign |
| Commutator curvature \(\mathscr F=[D,D]/i\) | unchanged |
| Operators made only from covariant \(D\), e.g. \(Q_{LD}^{(8)}\), \(Q_{RD}^{(8)}\), \(\mathcal O_S=H^\dagger(-D^2)^3H\) | unchanged, including their Wilson coefficients |
| One-background vertex obtained by expanding a \(D\)-only operator | changes sign with the external gauge-field variable |
| Operators with one explicit raw \(F_A\), e.g. the §5J representatives \(\mathcal O_P,\mathcal O_Q,\mathcal O_{E,H}\) | change sign; their coefficients change sign when translated between raw-\(F\) bases |
| Products of two raw component field strengths \(F_A F_B\) | even under the simultaneous field sign flip |
| Terms written as raw external \(F_A\) times the invariant commutator curvature \(\mathscr F\) | translate using both definitions; do not infer the sign by treating \(\mathscr F\) as a raw \(F\) |

The gauge equations of motion also change their raw-\(F\) sign:
\[
\partial_\rho F_+^{\rho\mu}=+gJ^\mu,
\qquad
\partial_\rho F_-^{\rho\mu}=-gJ^\mu,
\]
with the same current \(J^\mu\), since \(D_\mu\) is identical. Consequently the current-operator coefficients obtained after a gauge-EOM substitution must be translated with this sign. This is why the current-basis expressions in the upstream note cannot be copied into an axial raw-field-strength basis without the explicit map.

## 3. Impact on existing calculations

1. The RC-001/PR #69 tree-level \(C_5\) sign is fixed by the UV mass matrix and remains negative in the adopted operator convention.
2. The v6 Eq. (5-d) displayed positive coefficient is an internal manuscript-sign discrepancy. It is not silently absorbed into the RC-001 convention.
3. The PR #69 EFT determinant, \(O_8^{\rm pot}\) pole, \(c_8\) matching, and current benchmark numbers depend on \(|C_5|^2\) or \(|C_5|^4\); they are unchanged by this sign finding.
4. The derivative-operator Wilson map must use the field-strength dictionary above. \(D\)-only tree-level \(Q_{LD}^{(8)}\) and \(Q_{RD}^{(8)}\) coefficients are unchanged; one-explicit-\(F\) representatives and gauge-EOM current representatives require sign conversion.
5. No QLD8 coefficient is added to \(\Pi_{hh}\), \(\Pi_{hs}\), \(\Pi_{ss}\), or to \(O_8^{\rm pot}\) by this convention audit.

## 4. Reproducibility

The exact-rational bookkeeping is implemented in:
- c5_gauge_convention_audit.py
- test_c5_gauge_convention_audit.py

The tests cover the Schur complement, the printed v6 signed-mass comparison, right-handed field rephasing covariance, the determinant/sign of the bi-orthogonal diagonalization, and the \(D/F/\mathscr F\)/gauge-EOM sign dictionary.

The script is an algebra/convention audit, not a loop calculation and not an independent FeynArts/FeynCalc validation.
