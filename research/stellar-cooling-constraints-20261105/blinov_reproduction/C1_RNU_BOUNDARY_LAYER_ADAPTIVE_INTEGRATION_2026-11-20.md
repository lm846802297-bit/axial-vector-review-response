# C1 neutrinosphere boundary-layer adaptive integration

Date: 2026-11-20

Status: **103/153-node adaptive radial convergence passed; energy-order refinement is the next numerical acceptance gate.**

## 1. Objective

The fixed-grid Simpson transport has a boundary-layer failure at large coupling when the outer integration boundary is exactly the neutrinosphere radius. The source remains finite at the last radial node, while the attenuation is exactly one at that boundary. A fixed endpoint quadrature weight therefore produces a spurious contribution proportional to the radial mesh spacing.

This stage changes only the numerical evaluation of the radial luminosity integral. The old Simpson result remains in the output as a comparison baseline.

## 2. Transport integral

For each energy and physical polarization,

\[
L_h(g_X,\omega)=g_X^2\int_0^{R_\nu}dr\,
S_h(r,\omega)\exp[-g_X^2\tau_h(r,\omega)],
\]

where \(S_h\) is the source coefficient with the common \(g_X^2\) removed and

\[
\tau_h(r,\omega)=\int_r^{R_\nu}dr'\,
\kappa_h(r',\omega),\qquad
\kappa_h=\Gamma_{{\rm abs},h}-\Gamma_{{\rm prod},h}.
\]

The 100 km convention retains the unchanged outer two-flavour vacuum-decay optical depth as a separate multiplicative factor:

\[
L_{100,h}=e^{-g_X^2\tau_{{\rm out},h}}L_{\nu,h}.
\]

## 3. Independent adaptive method

The implementation uses:

1. Shape-preserving PCHIP interpolation for the sampled source and reduced opacity.
2. An inward-from-surface coordinate \(s=(R_\nu-r)/(R_\nu-r_{\min})\), placing the escape layer at \(s=0\).
3. The exact antiderivative of the reversed PCHIP opacity interpolant, constructing \(\tau(s)\) from zero at the surface without subtracting two large optical-depth integrals.
4. QUADPACK adaptive Gauss-Kronrod integration in \(s\).
5. Explicit integration split points at fixed values of \(g_X^2\tau\), together with radial knots inside the optically relevant surface layer.
6. Separate integration for every energy node and each of \(L,+,-\), followed by the original energy quadrature.

Writing \(L_r=R_\nu-r_{\min}\) and \(s=(R_\nu-r)/L_r\), the transformed quantities are

\[
\tau(s)=L_r\int_0^s du\,\kappa(R_\nu-L_r u,\omega),
\]

\[
L_h(g_X,\omega)=g_X^2L_r\int_0^1 ds\,
S_h(R_\nu-L_r s,\omega)e^{-g_X^2\tau_h(s,\omega)}.
\]

In particular, \(\tau(0)=0\) is evaluated directly at the surface; no subtraction of two large optical-depth values is required.

The optical-depth split levels are 80, 64, 48, 32, 16, 8, 4, 2, 1, 0.5, 0.1, and 0.01. This makes the narrow escape layer visible to the adaptive integrator even when it is much thinner than one original radial cell.

The old cumulative-Simpson optical depth and Simpson luminosity remain unchanged. New fields ending in adaptive_quad report the independent calculation.

The QUADPACK error estimate measures integration error for the continuous PCHIP representation. It does not include radial interpolation uncertainty; that is assessed separately by repeating the full transport on the refined radial grid.

## 4. High-coupling check

If the reduced opacity is positive at the surface and the source and opacity are continuous there, the radial integral has the limiting behavior

\[
\lim_{g_X\to\infty}
g_X^2\int_0^{R_\nu}dr\,S_h(r,\omega)e^{-g_X^2\tau_h(r,\omega)}
=
\frac{S_h(R_\nu,\omega)}{\kappa_h(R_\nu,\omega)}.
\]

The code records the energy-integrated surface asymptote separately for each physical polarization. This checks that the high-coupling radial integral saturates rather than inheriting the fixed-grid endpoint weight.

## 5. Regression tests

The adaptive integrator is tested against:

- the analytic constant-source, constant-opacity integral over several coupling decades;
- the surface asymptote \(S(R_\nu)/\kappa(R_\nu)\);
- exact factorization of a constant outer optical-depth tail;
- a synthetic 103-node versus 153-node Simpson endpoint artifact, for which the fixed-grid result changes by approximately one third while the adaptive result remains at the analytic limit;
- a profile with a zero-opacity outer interval;
- an extreme kappa*R test in which the physical escape layer is below the relative machine resolution of an outward radial coordinate.

## 6. First 103-node C1 result

The first complete 10 MeV run used the pinned 1687-row public SFHo-18.8 profile and sampled it at 103 radial nodes. It evaluated 121 couplings over \(10^{-11}\le g_X\le1\), 32 energy nodes, and all three physical polarizations.

The maximum QUADPACK relative error estimate over the full coupling curve and both reported outer-boundary conventions is

\[
\epsilon_{\rm quad}^{\max}=6.13179\times10^{-8}.
\]

At \(g_X=1\), the adaptive result and the independently calculated surface asymptote agree to

\[
\frac{|L_{\rm adaptive}-L_{\rm surf}|}{L_{\rm surf}}
=5.55\times10^{-16}.
\]

The surface asymptote is \(4.7936104404\times10^{51}\) erg/s in each of \(L,+,-\), giving \(1.4380831321\times10^{52}\) erg/s in total. The equality of the three surface limits follows from local detailed balance: at fixed \(\omega\), \(S_h/\kappa_h\) reduces to the same Bose factor for every polarization.

The fixed-grid Simpson result is not reliable on the strong-coupling branch. Representative ratios of legacy Simpson to adaptive luminosity are:

| \(g_X\) (nearest scan point) | \(L_{\rm Simpson}/L_{\rm adaptive}\) |
|---:|---:|
| \(1.00\times10^{-11}\) | 0.99981 |
| \(1.08\times10^{-7}\) | 1.0314 |
| \(1.10\times10^{-6}\) | 67.26 |
| \(9.09\times10^{-6}\) | 4584.9 |
| \(9.26\times10^{-5}\) | 476435.7 |
| \(1.00\) | \(5.55\times10^{13}\) |

This is the fixed endpoint-weight artifact: once the physical escape layer becomes thinner than the radial spacing, the last Simpson endpoint contribution scales with the mesh spacing instead of approaching \(S(R_\nu)/\kappa(R_\nu)\). The adaptive result instead saturates at the finite surface limit.

For a uniform Simpson grid with spacing \(h\), once all interior nodes are exponentially suppressed, the last endpoint alone contributes approximately

\[
L_{\rm Simpson}\simeq g_X^2\,\frac{h}{3}\,S(R_\nu).
\]

It therefore grows as \(g_X^2\) and changes in proportion to \(h\) when the grid is refined. The physical integral instead has the finite limit \(S(R_\nu)/\kappa(R_\nu)\).

The independent 153-node calculation uses the same profile, coupling grid, energy quadrature, angular order, susceptibility order, and polarization definitions. It quantifies radial interpolation uncertainty, which is not included in the QUADPACK error estimate.

## 7. Adaptive 103/153-node radial convergence

The full 121-point coupling curves were compared point by point using
\[
\delta_{\rm rad}^{\max}
=\max_{g_X}\frac{|L_{153}(g_X)-L_{103}(g_X)|}{L_{153}(g_X)}.
\]
The maximum differences are:

| Quantity | Maximum relative difference | Coupling |
|---|---:|---:|
| Total, three modes | \(9.80258\times10^{-4}\) | \(1.33352\times10^{-7}\) |
| Longitudinal \(L\) | \(9.80010\times10^{-4}\) | \(1.33352\times10^{-7}\) |
| Transverse \(+\) | \(9.75527\times10^{-4}\) | \(1.33352\times10^{-7}\) |
| Transverse \(-\) | \(9.85238\times10^{-4}\) | \(1.33352\times10^{-7}\) |

The table above is the \(R_{\rm far}=R_\nu\) interior luminosity. We separately compared the \(R_{\rm far}=100\) km curve, including its unchanged energy-dependent vacuum-neutrino-decay tail. Since the tail can suppress the curve by hundreds of orders of magnitude, the pointwise relative comparison is restricted to points where the 153-node reference exceeds \(10^{-8}\) of its curve peak. The maximum differences are:

| Quantity at \(R_{\rm far}=100\) km | Absolute difference / curve peak | Maximum relevant pointwise relative difference |
|---|---:|---:|
| Total, three modes | \(1.60963\times10^{-4}\) | \(1.10973\times10^{-3}\) |
| Longitudinal \(L\) | \(1.25433\times10^{-4}\) | \(1.01870\times10^{-3}\) |
| Transverse \(+\) | \(1.63399\times10^{-4}\) | \(1.12327\times10^{-3}\) |
| Transverse \(-\) | \(1.87572\times10^{-4}\) | \(1.16930\times10^{-3}\) |

Across both outer-boundary conventions and all three polarizations, the maximum relevant pointwise relative difference is \(0.11693\\%\\), and the largest absolute difference normalized to the corresponding curve peak is \(0.02573\\%\\). The raw all-point relative maximum of \(26.07\\%\\) occurs at \(g_X=8.91251\\times10^{-7}\), where the 100 km reference is only \(8.74\\times10^{-306}\) of its peak; it is a numerical underflow tail and is excluded by the stated flux-relevance criterion.

The integrated surface asymptote also changes by only
\[
\frac{|L_{\rm surf}^{103}-L_{\rm surf}^{153}|}
{L_{\rm surf}^{153}}=1.757\times10^{-9}.
\]
The high-coupling adaptive integral reaches the surface asymptote on both grids with relative residuals below \(4\times10^{-16}\). Across both grids, the maximum QUADPACK relative-error estimate is \(1.38313\times10^{-7}\), and the maximum three-mode sum residual is \(2.21334\times10^{-16}\).

This resolves the earlier \(33.3\%\) 103/153-node discrepancy: that discrepancy belongs to the fixed-grid Simpson endpoint weight and is absent in the surface-centered adaptive integral. It is not a physical radial-grid sensitivity of the converged C1 transport result.

The separate legacy Simpson comparison remains archived. Its large strong-coupling ratios are a diagnostic of the endpoint-weight failure, not alternative luminosity predictions. The two-boundary output audit is reproducible with audit_croon_c1_adaptive_radial_output_convergence.py and passed independently in [workflow #44658776526](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44658776526). Native JSON/CSV SHA-256 checksums were verified; the derived convergence report has its own separate checksum. The adaptive radial result is now the accepted C1 interior-profile numerical baseline. Energy-order convergence of the adaptive integral is the next acceptance gate.


## 8. Acceptance

The 10 MeV C1 baseline uses the reviewed SFHo-18.8 profile, 103 actual radial nodes, 32 energy nodes, 121 coupling points, and all three physical polarizations.

Acceptance requires:

- all analytic and boundary-layer regression tests pass;
- all adaptive luminosities are finite and nonnegative;
- the mode-resolved luminosities close to the total;
- QUADPACK relative error estimates remain below \(10^{-6}\) for total and each mode;
- the high-coupling result approaches the independently recorded surface asymptote;
- the adaptive result is stable under the 103/153 radial-grid comparison.

No A0 result or SN1987A exclusion curve is updated at this stage.
