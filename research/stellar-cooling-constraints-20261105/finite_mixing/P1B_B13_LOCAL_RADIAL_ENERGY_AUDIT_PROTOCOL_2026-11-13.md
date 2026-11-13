# P1-B: 10 MeV exact B.13 local radial-energy convergence audit

**Status:** full-profile low-order Global-03 interpolation screen complete; selected high-order follow-up passed; global high-order quadrature acceptance remains pending.  
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

The final base grid contains 10 radii and 14 local mediator energies:

\[
r=\{0,5,8,10,12.5,15,18.66,22,24\}\ {\rm km},
\]

\[
\omega=\{10,10.5,12,15,20,30,50,80,120,200,300,510,720,1500\}\ {\rm MeV}.
\]

The exact threshold \(\omega=m_{A'}\) is retained. Every radial-energy cell is also sampled at its center. Radial midpoints are arithmetic; energy midpoints are centered in \(\sqrt{\omega-m_{A'}}\), matching the threshold variable used by the local emissivity integral.

After one bisection this gives 19 radii × 27 energies = 513 grid nodes and 18 × 26 = 468 direct cell-midpoint checks. The radial grid explicitly includes the profile's maximum-temperature shell at 8.482141 km. The 1500 MeV endpoint covers the finite thermal-integral cutoff (m_{A'}+36T_{max}simeq1422.99) MeV. A runtime guard scans the full 1687-row profile, verifies that the maximum-temperature shell is included in both the radial grid and local emissivity audit, and checks energy coverage before any collision-kernel evaluation.

## 4. Quadrature refinement

The four integration orders are
\[
(n_p,n_{\mu},n_{\gamma},n_{\phi}),
\]
where the variables are the transformed muon kinetic-energy coordinate, initial-muon polar angle, photon polar angle, and relative photon azimuth.

Every refined-grid node and cell midpoint is evaluated with
\[
(16,10,10,10),\quad(20,12,12,12).
\]
If the successive difference is too large, both are adaptively refined to
\[
(24,14,14,14),\quad(28,16,16,16).
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

At each cell center, the directly evaluated rates are compared with sequential log interpolation: first in the threshold-adapted coordinate \(\sqrt{\omega-m_{A'}}\), then in radius. If a rate endpoint is exactly zero, that one-dimensional interpolation falls back to linear interpolation. The absorption kernel is interpolated; production and reduced absorption are reconstructed from detailed balance at the exact midpoint temperature.

The same charge, mode, and observable decomposition is retained. The screening target is a maximum direct-midpoint/interpolant discrepancy below \(10^{-2}\) (1%). This is an interpolation-resolution criterion, distinct from the local quadrature criterion.

The ten worst interpolation cells are retained in the output to guide any necessary local grid refinement. The output key is maximum_direct_midpoint_vs_sequential_log_interpolation_error.

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


## 9. First coarse-grid result and refinement decision

The first 9-radius by 12-energy pass completed on Actions run #43373577571. The local quadrature screen passed at all 108 grid nodes and 88 cell midpoints:
- maximum final grid-node refinement change: \(9.9600\times10^{-4}\);
- maximum final cell-midpoint refinement change: \(8.6649\times10^{-4}\);
- maximum mode-by-mode detailed-balance residual: \(1.9926\times10^{-14}\);
- maximum final-muon shell residual: \(2.0432\times10^{-13}\).

The interpolation screen did not pass. The initial worst discrepancy was dominated by a combination of coarse radial/energy spacing and an overly broad linear fallback when a spectral-source corner was exactly zero at the mediator threshold. The latter was corrected by interpolating the positive production rate first and applying the exact \(\omega^2|\mathbf k|/(2\pi^2)\) phase-space factor at the midpoint. The interpolation is now performed sequentially in \(\sqrt{\omega-m_{A'}}\) and radius.

To test whether the remaining discrepancy is a grid-resolution problem, the next run bisects every original radial and threshold-adapted energy interval. The refined grid therefore contains 17 radii and 25 energies (425 nodes), with 384 direct cell-midpoint checks. The 720 MeV endpoint is required because the existing local emissivity integral uses (x_{max}=36), and the central profile temperature implies (omega_{max}=m_{A'}+36T_{max}simeq703.55) MeV. The local kernel and physical inputs are unchanged. The refined-grid run is the current P1-B continuation; P2 remains blocked until the interpolation criterion is met or a direct-evaluation strategy is adopted.


A post-processing check of the first coarse-grid JSON, using sequential log interpolation and the exact midpoint spectral phase-space factor, also gives diagnostic volume-weighted discrepancies of approximately 27.3% for the spectral source, 15.8% for reduced absorption, and 12.5% for reduced absorption weighted by the local spectral source. The volume weight used for this diagnostic is \(4\pi r^2 N(r)^2\,\Delta r\,\Delta\omega\). These are grid-interpolation diagnostics only, not a completed B.1 source integral or B.2 optical-depth calculation. They show that the coarse-grid problem is not confined to numerically negligible tails.


## 10. Detailed-balance-preserving interpolation

The refined interpolation now uses only the absorption kernel as the interpolated rate table. At each midpoint, the exact local temperature is taken from the fixed background, and the other channels are reconstructed using the exact identity
\[
\Gamma_{{\rm prod},h}^{(Q)}
=e^{-\omega/T(r)}\Gamma_{{\rm abs},h}^{(Q)},\qquad
\Gamma_{{\rm abs},h}^{*,(Q)}
=(1-e^{-\omega/T(r)})\Gamma_{{\rm abs},h}^{(Q)}.
\]
The spectral source then uses the exact midpoint phase-space factor. This avoids treating the steep thermal Boltzmann factor as an independent interpolated function and enforces detailed balance by construction. It does not remove the need to resolve the radial dependence of the absorption kernel itself.

The regression suite now includes a synthetic check that the reconstructed production, reduced absorption, and spectral source obey these exact midpoint relations.


## 11. Full-profile temperature maximum and final energy coverage

A scan of all 1687 rows of the fixed profile shows that the maximum temperature is not at the center:
\[
T_{\max}=39.24967934\ {\rm MeV},\qquad
r(T_{\max})=8.482141202\ {\rm km}.
\]
The local emissivity routine uses the finite thermal variable
\[
x=(\omega-m_{A'})/T\in[0,36],
\]
so the maximum required energy is
\[
\omega_{\max}=10+36T_{\max}=1422.988456\ {\rm MeV}.
\]
The final grid therefore includes the exact peak-temperature radius and extends to 1500 MeV. The local emissivity energy-integral audit also includes this radius as an explicit anchor. The runtime guard reads the complete profile table rather than estimating its maximum from the sparse grid nodes.

The final one-bisection grid is 19 radii × 27 energies = 513 nodes, with 468 direct cell-midpoint evaluations. This supersedes the earlier 17 × 25 planning count recorded during the intermediate refinement.


## 12. Global-02/Global-03 full-profile extension (2026-11-14)

The original 19 x 27 P1-B grid remains the fixed local-kernel protocol grid. In addition, an independent full-profile extension was run using the same exact-recoil moving-muon B.13 kernel and the fixed 10 MeV pure-vector endpoint:

\[
m_{A'}=10\ {\rm MeV},\qquad g_V/g_X=1,\qquad g_A/g_X=0.
\]

The background remains the 1687-row reconstructed SFHo-18.8, \(t_{\rm pb}=1\) s profile, SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

### Global-02: radial-node energy interpolation

- All 1687 radial nodes were evaluated at 17 local energy coordinates: 28,679 direct low-order B.13 evaluations.
- The original five-knot energy PCHIP had a maximum direct-midpoint discrepancy of 3.0794%.
- One bisection to a nine-knot PCHIP in \(\sqrt{x}\) reduced the maximum to 0.7362%; no radial node exceeded 1%.
- Maximum detailed-balance residual was \(1.121\times10^{-14}\); final-muon mass-shell residual was \(6.214\times10^{-13}\).

### Global-03: full radial-midpoint and 2D cell-midpoint screen

For all 1686 adjacent radial intervals, B.13 was directly evaluated at the true radial midpoint and all 17 E1 validation-energy coordinates, adding 28,662 direct evaluations. The 13,488 energy midpoints and 13,488 2D cell centers were checked.

| Interpolation check | Maximum discrepancy | Samples above 1% |
|---|---:|---:|
| Radial midpoint, all 17 energy coordinates | 0.08284% | 0 |
| Energy PCHIP at radial midpoints | 0.73617% | 0 |
| Local bilinear-log 2D interpolation | 5.47244% | 11,509 |
| Nine-knot PCHIP in \(\sqrt{x}\), then log-radial interpolation | 0.80678% | 0 |

The local bilinear-log interpolant is rejected for this kernel grid. The retained prescription is PCHIP in \(\sqrt{x}\) at each radial endpoint, followed by log-linear interpolation in radius. Absorption is interpolated; production, reduced absorption and spectral source are reconstructed from exact midpoint detailed balance and the exact spectral phase-space factor.

The maximum detailed-balance residual in Global-03 was \(1.2384\times10^{-14}\), and the maximum final-muon mass-shell residual was \(5.3802\times10^{-13}\). All rates were finite and nonnegative.

### Selected high-order follow-up

Four high-error cells were selected (radial intervals 702, 993, 1016 and 1024). The nine energy knots at both endpoints and the selected cell centers were re-evaluated with the high-order ladder. All selected points passed the 0.1% successive-order criterion after the two interval-702 \(x=36\) endpoints were extended to \((36,20,20,20)\). The largest final successive-order change was \(9.3270\times10^{-4}\).

The interval-702 high-order PCHIP cell-center interpolation comparison initially used order-32 endpoint values. The \(x=36\) endpoint convergence was subsequently extended to order 36; the PCHIP cell-center interpolation value is being independently recomputed with the updated endpoint values. Until that recomputation is archived, that one high-order interpolation number remains provisional.

### Acceptance boundary

**Passed:** complete low-order full-profile radial-midpoint, energy-PCHIP-at-radial-midpoint and sequential 2D PCHIP cell-midpoint screens; selected high-order checks for the four worst cells; exact detailed balance and final-muon shell closure.

**Not claimed:** full-profile high-order quadrature convergence at every radius/energy point; exhaustive high-order evaluation of every 2D cell; full-star B.1 source integral; B.2 optical depth; GR geodesic transport; luminosity; Fig. 7 reproduction; or an updated SN1987A limit. The vector endpoint gate remains a separate acceptance requirement, and the axial exclusion curve remains frozen.

Reproducible results are archived under `thermal_integrals/results/P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14/`; the direct midpoint data and source/input bundle are retained in the separate Global-03 archive.
