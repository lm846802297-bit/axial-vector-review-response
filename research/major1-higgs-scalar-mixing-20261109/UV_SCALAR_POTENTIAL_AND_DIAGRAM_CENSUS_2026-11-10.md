# Major Point 1 — UV scalar potential, tadpole conditions, and complete diagram census

**Date:** 2026-11-10  
**Scope:** original one-complex-singlet \(S+\mathrm{VLL}\) model in the manuscript; no neutrino-sector extension.  
**Purpose:** freeze the model-level inputs and perturbative counting before extending the pole calculation.  
**Status:** analytic potential expansion and diagram census completed. This is not a completed gauge-independent pole calculation.

## 1. A model-definition issue in the current manuscript

The current model section introduces \(\lambda_{SH}(S^\dagger S)(H^\dagger H)\) and quotes the mixing-angle relation, but does not display the complete renormalizable scalar potential or its tadpole conditions. A reproducible loop calculation should state them explicitly.

For one Higgs doublet and one complex singlet, the most general renormalizable CP-conserving scalar potential is
\[
V(H,S)=-\mu_H^2 H^\dagger H-\mu_S^2S^\dagger S
+\lambda_H(H^\dagger H)^2+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S).
\]
No additional renormalizable scalar operator is allowed by the stated gauge symmetry for this field content.

Use
\[
H=\begin{pmatrix}G^+\\(v+h+iG^0)/\sqrt2\end{pmatrix},\qquad
S=(v_s+s+ia)/\sqrt2.
\]
The tree-level tadpole equations are
\[
\mu_H^2=\lambda_Hv^2+\frac{\lambda_{HS}}2v_s^2,\qquad
\mu_S^2=\lambda_Sv_s^2+\frac{\lambda_{HS}}2v^2.
\]
The CP-even tree mass matrix is
\[
{\cal M}_{0}^{2}=
\begin{pmatrix}
2\lambda_Hv^2&\lambda_{HS}vv_s\\
\lambda_{HS}vv_s&2\lambda_Sv_s^2
\end{pmatrix}.
\]
It reproduces the manuscript convention
\[
\tan2\alpha=\frac{\lambda_{HS}vv_s}{\lambda_Sv_s^2-\lambda_Hv^2}.
\]
The tree-level stationary point is locally stable in the CP-even directions if both eigenvalues are positive; boundedness from below requires \(\lambda_H>0,\lambda_S>0\) and \(\lambda_{HS}>-2\sqrt{\lambda_H\lambda_S}\).

## 2. Scalar and gauge vertices fixed by this potential

The CP-even cubic derivatives (with the convention \(g_{ijk}=\partial_i\partial_j\partial_kV\)) are
\[
g_{hhh}=6\lambda_Hv,\quad g_{sss}=6\lambda_Sv_s,\quad
g_{hhs}=\lambda_{HS}v_s,\quad g_{hss}=\lambda_{HS}v.
\]
The Goldstone cubic derivatives are
\[
g_{hG_HG_H}=2\lambda_Hv,\quad
g_{sG_HG_H}=\lambda_{HS}v_s,\quad
g_{haa}=\lambda_{HS}v,\quad
g_{saa}=2\lambda_Sv_s.
\]
Here \(G_H\) denotes each of the three real electroweak Goldstone components and \(a\) is the \(U(1)_X\) Goldstone.

From \(|D_\mu S|^2\), with \(m_{A'}=2g_Xv_s\),
\[
{\cal L}\supset \frac12m_{A'}^2(1+s/v_s)^2A'_\mu A'^\mu,
\]
so the \(sA'A'\) vertex is \(2im_{A'}^2g_{\mu\nu}/v_s\) and the \(ssA'A'\) vertex is \(2im_{A'}^2g_{\mu\nu}/v_s^2\), with all momenta incoming. The physical scalar couplings follow after the same CP-even rotation used in the manuscript.

The charged-lepton/VLL scalar vertices are derivatives of the field-dependent mass matrix with respect to \(v\) and \(v_s\), followed by the exact left/right SVD rotations. The archived exact-basis fermion calculation already implements this prescription for \(hh,hs,ss\).

## 3. Perturbative counting implied by the chosen matching benchmark

The conditional boundary used in Plan C-lite is
\[
\lambda_{HS}^{\rm EFT}(M_E)=0,\qquad
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{\rm hard}.
\]
Since \(\Delta\lambda_{HS}^{\rm hard}\) is generated at one VLL loop, this choice counts \(\lambda_{HS}^{\rm UV}=O(\hbar)\) in the combined expansion. It is a tuned matching benchmark, not a symmetry prediction.

Consequences:
- The tree-level UV off-diagonal mass entry \(\lambda_{HS}^{\rm UV}vv_s\) and the hard one-loop VLL threshold must be combined before interpreting low-energy mixing.
- The leading nonzero matched \(hs\) two-point function is \(O(\hbar)\): full VLL/lepton one-loop contribution minus the EFT light contribution, plus the matched local derivative operators and all same-order EFT soft/counterterm terms.
- A scalar bubble with one portal cubic and one ordinary scalar cubic is \(O(\hbar^2)\) in this combined counting. The CP-even subset already archived in P2-lite is therefore a next-order subset, not a complete next-order answer.
- Portal-induced Goldstone, \(W/Z\), \(A'\), top and ghost contributions, together with their counterterms, enter the same next-order completion where the corresponding portal-induced vertices are present.
- The diagonal \(hh\) and \(ss\) self-energies have ordinary one-loop pieces even when the portal is small. They must either be included with a consistent on-shell/pole renormalization prescription or absorbed into explicitly defined physical mass and residue inputs. Fixed widths cannot be combined with explicit cuts that are already included in the self-energy.

## 4. Diagram and counterterm census

| Sector | \(hh\) | \(hs\) | \(ss\) | Status / required treatment |
|---|---|---|---|---|
| \(\mu,\tau,E_\mu,E_\tau\) fermion loops | yes | yes | yes | Exact mass-eigenstate one-loop matrix exists; EFT light subtraction and matching ledger not fully closed |
| Higgs/radial CP-even scalar loops | yes | portal-dependent | yes | Selected \(hs\) bubble subset exists; complete tadpole and counterterm set absent |
| Electroweak Goldstones | yes | portal-dependent | yes | Vertices derived; must be combined with gauge/ghost sector in \(R_\xi\) gauge |
| \(U(1)_X\) Goldstone | portal-dependent | portal-dependent | yes | Vertices derived; combine with \(A'\), ghost and tadpole terms |
| \(W,Z\) gauge bosons | yes | portal/mixing-induced | no direct \(s\) vertex in gauge basis | Include for gauge-complete next-order physical poles |
| \(A'\) gauge boson | portal/mixing-induced | portal/mixing-induced | yes | Include \(A'\) self-energy and associated Goldstone/ghost terms |
| SM fermions (especially top) | yes | portal/mixing-induced | no direct \(s\) Yukawa in gauge basis | Standard \(hh\) part may be absorbed into SM pole inputs; mixing-induced terms belong to the declared higher order |
| VLL plus scalar/gauge mixed two-loop graphs | yes | yes | yes | Not calculated; required only if claiming the complete next order |
| Tadpoles and VEV counterterms | yes | yes | yes | Must be fixed consistently; not optional for un-subtracted pole masses |
| Field and mass counterterms | yes | yes | yes | Fermion-sector UV coefficients exist; full gauge/scalar counterterm closure remains open |

## 5. Required renormalization prescription

For a complete pole calculation, state:
1. dimensional regularization and \(\overline{\rm MS}\) for UV matching coefficients;
2. the gauge choice (use general \(R_\xi\) for the gauge-independence check, with a fixed reference gauge for intermediate numerics);
3. a tadpole prescription (Fleischer--Jegerlehner or an explicitly equivalent scheme);
4. whether \(v,v_s\) are defined by renormalized tadpole conditions or by physical inputs;
5. the renormalization of \(\lambda_H,\lambda_S,\lambda_{HS}\), \(v,v_s\), and the \(h,s\) field matrix;
6. whether \(m_h,m_s\) are tree parameters, on-shell masses, or pole masses;
7. the matching scale and the EFT operator/counterterm basis.

Do not combine the Plan-B, RC-001 and P2-lite self-energies until their inverse-propagator signs, field normalizations, subtraction points and tadpole conventions are converted to this common prescription.

## 6. Pole and observable completion

The renormalized inverse propagator is
\[
\Gamma_{\rm inv}(s)=s{\bf1}-{\cal M}_0^2+\widehat\Pi(s),
\]
where \(\widehat\Pi\) includes the complete self-energy matrix and counterterms in the declared scheme. Physical complex poles solve
\[
\det\Gamma_{\rm inv}(s_i)=0.
\]
For each pole, compute the residue matrix from the derivative of the inverse propagator. Near overlapping poles, form the coherent amplitude
\[
{\cal A}_{I\to F}(s)=
{\cal V}_{I}^{\,T}(s)\,\Gamma_{\rm inv}^{-1}(s)\,{\cal V}_{F}(s)
+{\cal A}_{\rm nonres}(s),
\]
including interference and the experimental mass response. A real mixing angle or a pole eigenvector component alone is not an observable.

## 7. Acceptance boundary and next calculation

This census establishes the missing ingredients and prevents double counting. It does not yet provide a gauge-independent physical pole or LHC exclusion.

The next calculation should first close the leading \(O(\hbar)\) UV--EFT \(hs\) matching: explicitly list each full-theory fermion diagram, each EFT light diagram/contact insertion, the local portal and derivative counterterms, and the scale dependence. Only after this matching is closed should the leading two-state pole calculation be promoted. The \(O(\hbar^2)\) portal-induced scalar/gauge completion is a separate next-order project; do not present the existing CP-even P2-lite subset as that complete correction.
