# P1-B: 10 MeV exact B.13 local radial-energy convergence audit

**Status:** numerical workflow launched; final numerical disposition pending.  
**Research line:** PR #106 v2, research/fig7-10mev-transport-localization-20261113-v2.

## 1. Purpose and boundary

P1-B tests whether the exact moving-muon B.13 local semi-Compton collision kernel is numerically stable over the radial and mediator-energy region needed by a later global transport calculation.

This stage is deliberately restricted to the **pure-vector endpoint**:
\[
m_{A'}=10\ {\rm MeV},\qquad g_V/g_X=1,\qquad g_A/g_X=0.
\]
This is the required external vector benchmark lane. The mixed UV current and the production axial-vector scan remain frozen until the pure-vector benchmark and transport prescription are reconciled.

The kernel is the already-existing finite_mixing/moving_muon_compton.py, which was independently checked against explicit Dirac spinors in B13_EXPLICIT_SPINOR_INDEPENDENT_AUDIT_2026-11-13.md. P1-B does not introduce a second production matrix-element implementation.

## 2. Fixed background

Use the repository's reconstructed SFHo-18.8, \(t_{\rm pb}=1\) s profile:
- data/sfho188_digitized.csv;
- 1687 retained rows;
- SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.

This is a vertex-preserving reconstruction of published profile figures, not the raw Garching simulation table. The profile identity is checked at runtime. All rates are local-frame coefficients per \(g_X^2\).

## 3. Radial-energy grid

The node grid contains 9 radii and 12 local mediator energies:

\[
r=\{0,5,8,10,12.5,15,18.66,22,24\}\ {\rm km},
\]

\[
\omega=\{10,10.5,12,15,20,30,50,80,120,200,300,510\}\ {\rm MeV}.
\]

The exact threshold \(\omega=m_{A'}\) is retained. Every radial-energy cell is also sampled at its center. Radial midpoints are arithmetic; energy midpoints are centered in \(\sqrt{\omega-m_{A'}}\), matching the threshold variable used by the local emissivity integral.

This gives 108 grid nodes and 88 direct cell-midpoint checks.

## 4. Quadrature refinement

The four integration orders are
\[
(n_p,n_{\mu},n_{\gamma},n_{\phi}),
\]
where the variables are the transformed muon kinetic-energy coordinate, initial-muon polar angle, photon polar angle, and relative photon azimuth.

Every grid node is evaluated with
\[
(12,8,8,8),\quad(16,10,10,10),\quad(20,12,12,12).
\]
Every cell midpoint is evaluated with
\[
(16,10,10,10),\quad(20,12,12,12).
\]
If the last successive refinement exceeds the screening target, the point is adaptively refined to
\[
(24,14,14,14),\quad(28,16,16,16).
\]

The pointwise comparison is made separately for both target charges and all three physical mediator modes \(L,+,-\), and separately for:
- production \(\Gamma_{{\rm prod},h}\);
- absorption \(\Gamma_{{\rm abs},h}\);
- reduced absorption \((1-e^{-\omega/T})\Gamma_{{\rm abs},h}\);
- local spectral emissivity factor \(\omega^2\sqrt{\omega^2-m_{A'}^2}\Gamma_{{\rm prod},h}/(2\pi^2)\).

The quadrature screening target is a maximum relative change below \(10^{-3}\) (0.1%) between the final two available orders. This is a project numerical criterion, not a published physical uncertainty.

## 5. Radial-energy interpolation check

At each of the 88 cell centers, the directly evaluated rates are compared with a bilinear interpolation of the four surrounding grid-node values in log(rate), falling back to linear interpolation if any corner is exactly zero.

The same charge, mode, and observable decomposition is retained. The screening target is a maximum direct-midpoint/interpolant discrepancy below \(10^{-2}\) (1%). This is an interpolation-resolution criterion, distinct from the local quadrature criterion.

The ten worst interpolation cells are retained in the output to guide any necessary local grid refinement.

## 6. Algebraic and kinematic checks

At every evaluated point:
1. production and absorption satisfy mode-by-mode detailed balance for each charge,
   \[
   \Gamma_{{\rm prod},h}^{(Q)}
   =e^{-\omega/T}\Gamma_{{\rm abs},h}^{(Q)};
   \]
2. the final muon remains on shell;
3. rates are finite and nonnegative;
4. the sum of the charge-resolved rates closes onto the returned total rate.

Tolerances are \(2\times10^{-10}\) for detailed balance and final-muon shell closure. The minimum pre-roundoff-clipping matrix element is retained.

At the worst grid point, the four quadrature dimensions are also varied individually to identify which integration coordinate controls the residual.

## 7. Execution and output

- Audit script: thermal_integrals/audit_b13_local_kernel_radial_energy_10mev.py
- Regression tests: thermal_integrals/test_p1b_b13_local_kernel_radial_energy_10mev.py
- Workflow: .github/workflows/p1b-b13-local-kernel-radial-energy.yml
- Initial workflow run: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43373577571
- Expected JSON: thermal_integrals/outputs/p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json

The workflow first compiles the sources and runs the regression tests, then executes the dense grid and archives the complete JSON as an Actions artifact. The final pass/fail decision is based on the numerical JSON, not merely on successful job execution.

## 8. Explicit non-claims

P1-B is a local collision-kernel and sampled interpolation audit only. It does not calculate:
- the global B.1 source integral;
- the B.2 path optical depth;
- the scalar-B.2 luminosity;
- equal-occupation scalar closure;
- independent-mode global propagation;
- an axial-vector cooling curve or SN1987A exclusion.

Only after P1-B passes should the project proceed to P2: matched global propagation of \(L,+,-\), with scalar B.2, equal-occupation closure, and independent-mode transport kept as separate prescriptions.
