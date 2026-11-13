# Two-VEV axial microphysics — formula and code cross-check

**Audit date:** 2026-11-13  
**Canonical source:** \`research/stellar-cooling-two-vev-20261105/\` and \`research/stellar-cooling-shared-20261105/\`  
**Integration:** PR #85 merged; the later shared-code consolidation is in current main.  
**Scope:** formula and implementation review of the two-VEV mapping, current-level widths, vacuum semi-Compton amplitude, and homogeneous thermal prototype. This is not a supernova transport calculation.

## 1. Gauge-boson mass and Goldstone directions

Use
\[
S=\frac{v_s+s+i a_s}{\sqrt2},\quad Q_X(S)=2,\qquad
\sigma=\frac{v_\sigma+\sigma_r+i a_\sigma}{\sqrt2},\quad Q_X(\sigma)=1,
\]
with \(D_\mu=\partial_\mu-i g_X Q_X A'_\mu\).

The scalar kinetic terms contain
\[
\frac12(\partial_\mu a_s-2g_Xv_sA'_\mu)^2
+\frac12(\partial_\mu a_\sigma-g_Xv_\sigma A'_\mu)^2.
\]
Consequently,
\[
v_X^2=4v_s^2+v_\sigma^2,\qquad
m_{A'}^2=g_X^2v_X^2.
\]
The eaten and orthogonal CP-odd directions are
\[
G=\frac{2v_sa_s+v_\sigma a_\sigma}{v_X},\qquad
a_\perp=\frac{v_\sigma a_s-2v_sa_\sigma}{v_X}.
\]
The two directions are normalized and orthogonal. The exact inverse map at fixed \((m_{A'},g_X,r_\sigma)\), with \(r_\sigma=v_\sigma^2/(4v_s^2)\), is
\[
v_s=\frac{m_{A'}}{2|g_X|\sqrt{1+r_\sigma}},\qquad
v_\sigma=2v_s\sqrt{r_\sigma}.
\]

**Result:** the gauge-mass relation and the eaten-Goldstone direction in \`two_vev_axial_mapping.py\` are algebraically correct for the stated charge and covariant-derivative conventions.

## 2. Goldstone coupling versus the longitudinal axial current

In the charged-lepton seesaw limit used by this model line, the phase of \(S\) gives a pseudoscalar Yukawa magnitude \(m_\ell/v_s\). Since
\[
a_s=\frac{2v_s}{v_X}G+\frac{v_\sigma}{v_X}a_\perp,
\]
the eaten-Goldstone coupling is
\[
|g_{G\ell\ell}|=\frac{m_\ell}{v_s}\frac{2v_s}{v_X}
=\frac{2m_\ell}{v_X}.
\]
For an on-shell Dirac lepton,
\[
q_\mu\bar u(p')\gamma^\mu\gamma^5u(p)
=2m_\ell\,\bar u(p')\gamma^5u(p)
\]
(up to the overall sign convention for the axial vertex). The longitudinal-current coupling therefore has magnitude \(2|g_A^\ell|m_\ell/m_{A'}\). It agrees with the projected Goldstone coupling only under
\[
|g_A^\ell|=|g_X|,\qquad m_{A'}=|g_X|v_X.
\]
The test in \`test_two_vev_axial_mapping.py\` checks this relation in the default pure-axial convention. If a finite-mixing point has \(|g_A^\ell|\ne|g_X|\), the equality must not be assumed without changing the Goldstone/Yukawa matching.

A second consequence is important: the orthogonal physical pseudoscalar is not absent. Its charged-lepton coupling magnitude from the same \(S\)-phase term is
\[
|g_{a_\perp\ell\ell}|=\frac{m_\ell}{v_s}\frac{v_\sigma}{v_X}.
\]
Its mass and interactions depend on the scalar potential and are not specified by the mapping module. The two-VEV setup therefore adds a physical CP-odd state; it is not merely a relabeling of the one-VEV parameter \(v_s\). This prototype does not calculate that state's spectrum, mixing, decay widths, or constraints.

## 3. Current-level \(A'\) partial widths

For \(r_\ell=m_\ell^2/m_{A'}^2\) and \(\beta_\ell=\sqrt{1-4r_\ell}\), the standard unpolarized two-body factors used by \`axial_decay_widths.py\` are
\[
\Gamma_V(A'\to\ell^+\ell^-)
=\frac{g_V^2m_{A'}}{12\pi}(1+2r_\ell)\beta_\ell,
\]
\[
\Gamma_A(A'\to\ell^+\ell^-)
=\frac{g_A^2m_{A'}}{12\pi}\beta_\ell^3.
\]
The helper's finite-right-mixing parameterization \(g_V=g_X\sin^2\theta_{\ell R}\), \(g_A=-g_X\cos^2\theta_{\ell R}\) is inserted through the squared couplings. The vector and axial terms do not interfere in the fully integrated unpolarized two-body width.

**Boundary:** these are current-level partial widths. They are not automatically the full width of the UV-complete model if additional scalar, heavy-neutrino, or loop-induced kinetic-mixing channels are open.

## 4. PMNS trace and the charged right-handed-neutrino caveat

For the active \(L_\mu-L_\tau\) charge matrix
\[
Q_\nu=\operatorname{diag}(0,+1,-1),
\]
a unitary three-flavour PMNS rotation gives
\[
G_\nu=U_{\rm PMNS}^\dagger Q_\nu U_{\rm PMNS},\qquad
\operatorname{Tr}(G_\nu^\dagger G_\nu)
=\operatorname{Tr}(Q_\nu^\dagger Q_\nu)=2.
\]
Thus the *inclusive active-light-neutrino trace* is independent of a unitary PMNS rotation. In the minimal-model convention with \(U_{\rm PMNS}=I\), the same trace is simply \(0^2+1^2+(-1)^2=2\).

This does **not** establish the full neutral-fermion width in the presence of charged right-handed neutrinos. The helper assumes negligible active-heavy mixing and that all heavy-neutrino thresholds are closed. If the light-state mixing matrix is non-unitary, or if any \(A'\to N_iN_j\) channel is open, the full neutral-fermion charge matrix must be rotated into the mass basis and every kinematically open channel included. The absolute Majorana/Weyl normalization should also be stated explicitly when turning the trace into a width. The helper further omits loop-induced electron channels from kinetic mixing and any scalar channels. Its branching fractions are therefore conditional on the stated restricted channel set.

## 5. Vacuum semi-Compton amplitude

\`stellar_semi_compton_axial_matrix_element.py\` constructs the tree-level \(s\)- and \(u\)-channel muon diagrams for
\[
\gamma(k)+\mu(p)\to\mu(p')+A'(q),
\]
with a vector/axial \(A'\mu\mu\) vertex. The implementation uses massive-vector polarization vectors, averages over the initial muon spin and photon polarization, and sums final spins. The lab and CM differential-cross-section forms use the corresponding two-body phase-space Jacobians.

The recorded checks cover on-shell kinematics, polarization normalization, the electromagnetic Ward contraction obtained by replacing the photon polarization by \(k^\mu\), the conserved-vector Thomson limit, Klein–Nishina agreement, lab/CM total-cross-section agreement, and a numerical axial longitudinal \(1/m_{A'}^2\) scaling check.

Two limitations must remain explicit:

1. The electromagnetic Ward identity is not the same as an independent \(A'\)-current Ward/Goldstone-equivalence test. The present \(\sigma_L\) mass-scaling check is useful evidence, but the code does not yet compare the contracted \(A'\) amplitude directly with an independently constructed Goldstone amplitude.
2. The T/L labels are defined relative to the frame used to construct the polarization vectors. A CM-helicity split is not the medium-rest-frame T/L split when the medium has nonzero velocity in the pair CM frame.

The low-energy vector-reference helper also records a possible T/L label interchange in the cited literature formula: the current regression compares the calculated transverse result with the expression printed under the opposite label. That is a diagnostic of a source-label discrepancy, not a resolution of the underlying literature convention. Keep the independent projector/formula audit open.

## 6. Homogeneous thermal-rate prototype

The shared implementation integrates initial muon and photon distributions, the invariant Møller flux, the CM differential cross section, final-state muon Pauli blocking evaluated using the medium four-velocity in the pair CM frame, and the two charge states \(\mu^\pm\). The optically thin prototype omits final-state \(A'\) occupation and medium-induced dispersion/vertex corrections.

The recorded smoke test reports \(U_{\rm medium}^2=1\) and a medium-frame energy-conservation residual \(3.553\times10^{-15}\). This verifies the tested kinematic transformation and smoke-test point; it is not a full angular/energy-grid proof.

The machine-readable convergence table has
\[
(n_{\rm GL},n_\phi)=(6,12),(8,16),(10,20),(12,24).
\]
The order-10 to order-12 changes are \(-0.0108\%\) in the event rate and \(+0.0202\%\) in emissivity, and the recorded order-10 cutoff variations are sub-percent for the stated benchmark. However, the current order scan changes the Gauss–Legendre order and azimuthal order together. It is therefore a *combined quadrature refinement*, not an isolated \(n_{\rm GL}\) convergence test. A separate \(n_\phi\) scan at fixed \(n_{\rm GL}\), fixed cutoffs, and fixed benchmark is still required before calling the azimuthal integral independently converged.

Most importantly, this is a homogeneous, optically thin, polarization-summed local rate. It is not a medium-rest-frame T/L-resolved emissivity/opacity, inverse-process trapping solution, radial SN transport, diffusion calculation, or SN1987A luminosity.

## 7. Acceptance summary

| Item | Review result | Remaining boundary |
|---|---|---|
| Gauge mass and Goldstone basis | Algebraically correct | Depends on the stated charges and \(D_\mu\) convention |
| Goldstone/axial-current relation | Correct for \(|g_A|=|g_X|\) | Finite-mixing matching must be treated separately |
| Physical CP-odd state | Identified | Scalar potential, mass, mixing, and constraints not calculated |
| Charged-lepton widths | Standard vector/axial factors | Not a complete UV total width |
| PMNS trace | \(2\) for a unitary active three-flavour rotation | Charged \(N_R\), non-unitarity, open heavy thresholds, and Majorana normalization not fully implemented |
| Electromagnetic Ward identity | Numerically tested | Does not replace an \(A'\)-Goldstone Ward/equivalence test |
| Vacuum T/L projections | Frame-defined and numerically checked | CM helicity is not medium-rest T/L |
| Homogeneous thermal integral | Smoke test and combined quadrature/cutoff records exist | Independent azimuthal convergence and full transport remain open |

## 8. Integration decision

PR #85 already integrated the separate two-VEV research line into main. PR #100 was closed as redundant because its four actual changes would have replaced the current shared thermal adapters with older duplicated implementations; it did not contain a new physical result. The canonical implementation remains the main-branch two-VEV matrix element plus the shared thermal module.

No new supernova limit or referee-response result follows from this audit. The pure-vector Blinov Fig. 7 10 MeV strong-absorption gate remains **NOT PASSED**.
