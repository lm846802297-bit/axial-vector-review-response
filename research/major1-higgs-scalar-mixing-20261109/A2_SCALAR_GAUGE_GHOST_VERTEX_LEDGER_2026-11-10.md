# Major Point 1 — A2 scalar, gauge and Faddeev–Popov vertex ledger

**Scope.** This is the gauge-basis vertex ledger for the original one-doublet/one-complex-singlet model, with \(y_{\mu\tau}=0\), diagonal gauge kinetic terms at the matching reference scale, and the conditional negligible-renormalized-portal benchmark. It does not calculate the loop integrals or claim a gauge-independent pole result.

## 1. Conventions inherited from the model

The paper has
\[
Q_S=2Q_\ell,\qquad g_X=g_SQ_\ell,\qquad m_X=m_{A'}=2g_Xv_S.
\]
Thus the physical \(U(1)_X\) charge-coupling of \(S\) is \(2g_X\), not \(g_X\). Use
\[
H=\begin{pmatrix}G^+\\(v+h+iG^0)/\sqrt2\end{pmatrix},\qquad
S=(v_S+s+ia)/\sqrt2,
\]
and
\[
X_H\equiv H^\dagger H=G^+G^-+\frac{(v+h)^2+(G^0)^2}{2},\qquad
X_S\equiv S^\dagger S=\frac{(v_S+s)^2+a^2}{2}.
\]
The scalar potential is
\[
V=-\mu_H^2X_H-\mu_S^2X_S+
\lambda_HX_H^2+\lambda_SX_S^2+\lambda_{HS}X_HX_S.
\]
Tadpole conditions are imposed before extracting interaction vertices. The table below gives derivatives of \(V\); the corresponding scalar Feynman rule is \(-i\) times the listed derivative.

## 2. Complete nonzero scalar cubic vertices

Define \(\kappa_{ijk}\equiv\partial_i\partial_j\partial_kV|_{\rm vev}\).

| Fields | \(\kappa_{ijk}\) |
|---|---:|
| \(hhh\) | \(6\lambda_Hv\) |
| \(sss\) | \(6\lambda_Sv_S\) |
| \(hhs\) | \(\lambda_{HS}v_S\) |
| \(hss\) | \(\lambda_{HS}v\) |
| \(hG^0G^0\) | \(2\lambda_Hv\) |
| \(hG^+G^-\) | \(2\lambda_Hv\) |
| \(sG^0G^0\) | \(\lambda_{HS}v_S\) |
| \(sG^+G^-\) | \(\lambda_{HS}v_S\) |
| \(haa\) | \(\lambda_{HS}v\) |
| \(saa\) | \(2\lambda_Sv_S\) |

This list is complete for cubic interactions among \(h,s,G^\pm,G^0,a\) in the CP-conserving potential. In particular, \(hG^0a\), \(sG^0a\), \(hG^\pm a\), and \(sG^\pm a\) vanish.

## 3. Complete nonzero scalar quartic vertices

Define \(\lambda_{ijkl}\equiv\partial_i\partial_j\partial_k\partial_lV|_{\rm vev}\). The nonzero derivatives are

| Fields | \(\lambda_{ijkl}\) |
|---|---:|
| \(hhhh\) | \(6\lambda_H\) |
| \(ssss\) | \(6\lambda_S\) |
| \(hhss\) | \(\lambda_{HS}\) |
| \(hhG^0G^0\) | \(2\lambda_H\) |
| \(hhG^+G^-\) | \(2\lambda_H\) |
| \(ssG^0G^0\) | \(\lambda_{HS}\) |
| \(ssG^+G^-\) | \(\lambda_{HS}\) |
| \(hhaa\) | \(\lambda_{HS}\) |
| \(ssaa\) | \(2\lambda_S\) |
| \(G^0G^0G^0G^0\) | \(6\lambda_H\) |
| \(G^0G^0G^+G^-\) | \(2\lambda_H\) |
| \(G^0G^0aa\) | \(\lambda_{HS}\) |
| \(G^+G^+G^-G^-\) | \(4\lambda_H\) |
| \(G^+G^-aa\) | \(\lambda_{HS}\) |
| \(aaaa\) | \(6\lambda_S\) |

The absence of an \(hs\phi\phi\) quartic for a single common Goldstone species \(\phi\) is important. The \(hhss\) vertex has one internal \(h\) and one internal \(s\) when \(h,s\) are external; with zero renormalized tree \(h-s\) propagator it does not generate a one-vertex diagonal tadpole contraction.

## 4. Gauge-boson vertices from the covariant kinetic terms

In the gauge basis, the mass-term part of the kinetic Lagrangian is
\[
\begin{aligned}
{\cal L}_{\rm mass,gauge}={}&
m_W^2\left(1+\frac hv\right)^2W_\mu^+W^{-\mu}
+\frac{m_Z^2}{2}\left(1+\frac hv\right)^2Z_\mu Z^\mu\\
&+\frac{m_X^2}{2}\left(1+\frac{s}{v_S}\right)^2A'_\mu A'^\mu.
\end{aligned}
\]
Consequently the nonzero CP-even two-vector vertices and their rule coefficients are
\[
\begin{array}{c|c}
\text{vertex}&\text{Feynman rule}\\ \hline
hW^+_\mu W^-_\nu&2i\,m_W^2v^{-1}g_{\mu\nu}\\
hZ_\mu Z_\nu&2i\,m_Z^2v^{-1}g_{\mu\nu}\\
sA'_\mu A'_\nu&2i\,m_X^2v_S^{-1}g_{\mu\nu}\\
hhW^+_\mu W^-_\nu&2i\,m_W^2v^{-2}g_{\mu\nu}\\
hhZ_\mu Z_\nu&2i\,m_Z^2v^{-2}g_{\mu\nu}\\
ssA'_\mu A'_\nu&2i\,m_X^2v_S^{-2}g_{\mu\nu}
\end{array}
\]
There are no gauge-basis \(hA'A'\), \(sW^+W^-\), or \(sZZ\) vertices. These do not become local gauge-basis vertices merely because a loop-induced \(h-s\) self-energy exists.

The derivative scalar-current vertices from the same kinetic terms have magnitudes \(g_2/2\) for \(W^\pm hG^\mp\), \(g_Z/2\) for \(ZhG^0\), and \(g_X\) for \(A'sa\), where \(g_Z=\sqrt{g_2^2+g_Y^2}\). Their momentum dependence is the usual antisymmetric scalar-current structure \((p_1-p_2)_\mu\); the overall \(i\) signs follow the covariant-derivative convention. There is no \(W sG\), \(ZsG^0\), or \(A'h a\) vertex in the gauge basis.

## 5. Faddeev–Popov operator and scalar-dependent entries

Fix the gauge-transformation convention
\[
\delta A_\mu^A=\partial_\mu\alpha^A+g_A f^A{}_{BC}A_\mu^B\alpha^C,\qquad
\delta\Phi=-i\alpha^A g_AT^A\Phi,
\]
with the broken-generator parameters normalized so that
\[
\delta G_W^a=-m_W\left(1+\frac hv\right)\alpha_W^a+\cdots,\quad
\delta G_Z=-m_Z\left(1+\frac hv\right)\alpha_Z+\cdots,
\]
\[
\delta a=-m_X\left(1+\frac{s}{v_S}\right)\alpha_X,\qquad
m_X=2g_Xv_S.
\]
For \(F^A=\partial\cdot A^A-\xi_A m_A G_A\), the exact Faddeev–Popov operator is
\[
\boxed{
{\cal M}^{AB}(x,y)=
\frac{\delta F^A(x)}{\delta\alpha^B(y)}
=
\left[
\partial^\mu\!\left(\partial_\mu\delta^{AB}
+g_A f^A{}_{CB}A_\mu^C\right)
-\xi_A m_A\frac{\delta G_A}{\delta\alpha^B}
\right]\delta^{(4)}(x-y).
}
\]
Here \(T^A\) are the \(SU(2)_L\) doublet generators, \(Y_H=1/2\), and the singlet has \(U(1)_X\) charge-coupling \(2g_X\). This functional expression fixes all off-diagonal ghost--Goldstone and ghost--gauge entries; the scalar-dependent diagonal entries relevant to external \(h,s\) are
\[
\begin{aligned}
{\cal M}_{W}^{\rm scalar}&=\xi_Wm_W^2\left(1+\frac hv\right),\\
{\cal M}_{Z}^{\rm scalar}&=\xi_Zm_Z^2\left(1+\frac hv\right),\\
{\cal M}_{X}^{\rm scalar}&=\xi_Xm_X^2\left(1+\frac{s}{v_S}\right).
\end{aligned}
\]
Thus
\[
{\cal L}_{\rm FP}\supset
-\xi_W\frac{m_W^2}{v}h\,\bar c^-c^+
-\xi_Z\frac{m_Z^2}{v}h\,\bar c_Zc_Z
-\xi_X\frac{m_X^2}{v_S}s\,\bar c_Xc_X
+\text{h.c. for the charged sector}.
\]
The \(U(1)_X\) coefficient is
\[
\boxed{\frac{m_X^2}{v_S}=2m_Xg_X=4g_X^2v_S.}
\]
There is no gauge-basis \(s\bar c_Wc_W\), \(s\bar c_Zc_Z\), \(h\bar c_Xc_X\), or \(h-s\) ghost vertex. The photon ghost has no scalar coupling. The remaining entries of \({\cal M}^{AB}\) are the usual non-Abelian gauge/ghost and Goldstone-dependent terms fixed by the displayed functional derivative; they must be retained in gauge-dependent subgraphs where applicable.

## 6. Important correction to the earlier diagram census

In the gauge basis with vanishing renormalized tree portal at the reference scale:

- \(hh\) receives SM electroweak vector/Goldstone/ghost loops and the fermion sector.
- \(ss\) receives \(A'\)/\(a\)/\(U(1)_X\)-ghost loops and the fermion sector.
- There is **no one-loop \(hs\) vector-boson bubble**: \(h\) couples to \(W,Z\), while \(s\) couples to \(A'\), and there is no common vector species at the two external vertices.
- There is **no one-loop \(hs\) ghost bubble** for the same reason: \(h\) couples to electroweak ghosts and \(s\) to the \(X\) ghost.
- A physical-state mixing angle can induce apparent \(sWW\) or \(hA'A'\) couplings after rotating fields, but those are not independent gauge-basis 1PI vertices. Including them as extra diagrams while also using the full \(h,s\) propagator would double count mixing.

This corrects the overly broad wording in the previous order-classification note that suggested one-loop portal-induced \(sVV\) and \(hA'A'\) vertices in the gauge basis.

## 7. The actual one-loop-topology \(hs\) scalar bubbles at next combined order

When the renormalized portal is counted as \(O(\hbar)\), one-loop scalar bubbles with one portal vertex are \(O(\hbar^2)\). The possible common internal pairs and products of cubic couplings are:

| Internal pair | Coupling product | Symmetry factor |
|---|---:|---:|
| \(hh\) | \((6\lambda_Hv)(\lambda_{HS}v_S)\) | \(1/2\) |
| \(ss\) | \((\lambda_{HS}v)(6\lambda_Sv_S)\) | \(1/2\) |
| \(G^+G^-\) | \((2\lambda_Hv)(\lambda_{HS}v_S)\) | \(1\) |
| \(G^0G^0\) | \((2\lambda_Hv)(\lambda_{HS}v_S)\) | \(1/2\) |
| \(aa\) | \((\lambda_{HS}v)(2\lambda_Sv_S)\) | \(1/2\) |

Up to the overall sign convention for \(\Pi\), their scalar-integral structure is
\[
\Pi_{hs}^{\rm scalar}(p^2)\propto
\frac{1}{16\pi^2}
\sum_{\phi\phi}
S_{\phi\phi}\,\kappa_{h\phi\phi}\kappa_{s\phi\phi}
B_0(p^2;m_\phi^2,m_\phi^2).
\]
The common UV-pole coupling combination is proportional to
\[
\boxed{
\lambda_{HS}v v_S(6\lambda_H+4\lambda_S)
}
\]
before adding tadpole, VEV, portal, and field counterterms. This is a diagnostic for the scalar-bubble subset, not the complete renormalized \(hs\) pole.

Goldstone masses are \(R_\xi\)-dependent, so the finite parts of the Goldstone terms cannot be interpreted physically before the complete counterterm and gauge-sector calculation. The UV pole must be combined with the portal counterterm in the same scheme.

## 8. Power-counting and no-double-counting rules

Under the conditional matching assignment \(\lambda_{HS}=O(\hbar)\):
- the exact \(\mu,\tau+E_\mu,E_\tau\) fermion two-point matrix is the leading new-physics \(O(\hbar)\) contribution;
- the one-loop scalar bubbles in section 7 are \(O(\hbar^2)\);
- pure electroweak and \(X\)-gauge loops contribute to the diagonal \(hh\) and \(ss\) entries already at ordinary one-loop order;
- no \(hs\) vector/ghost bubble is added in the gauge basis;
- SM contributions already absorbed into the measured Higgs pole input must not be added again;
- the heavy VLL portal threshold, EFT light bubbles, contact tadpoles, and explicit fermion absorptive cuts must each appear once only.

## 9. A2 acceptance boundary

The symbolic audit script checks every listed nonzero scalar cubic/quartic derivative, the CP-even gauge-boson mass-term vertices, the absence of the forbidden gauge-basis vector vertices, and the scalar-dependent FP radial coefficients. It does not yet expand every non-Abelian ghost-vector entry, calculate the PV integrals, or demonstrate cancellation of \(\xi\)-dependence. Those remain A2b/A3 tasks.
