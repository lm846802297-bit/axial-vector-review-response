# C1 neutrinosphere boundary-layer adaptive integration

Date: 2026-11-20

Status: **Surface-centered adaptive radial integrator implemented; numerical C1 baseline pending.**

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
2. The exact antiderivative of the PCHIP opacity interpolant to construct the continuous optical depth.
3. QUADPACK adaptive Gauss-Kronrod integration in a normalized radial coordinate.
4. Explicit integration split points at fixed values of \(g_X^2\tau\), together with radial knots inside the optically relevant surface layer.
5. Separate integration for every energy node and each of \(L,+,-\), followed by the original energy quadrature.

The optical-depth split levels are 80, 64, 48, 32, 16, 8, 4, 2, 1, 0.5, 0.1, and 0.01. This makes the narrow escape layer visible to the adaptive integrator even when it is much thinner than one original radial cell.

The old cumulative-Simpson optical depth and Simpson luminosity remain unchanged. New fields ending in adaptive_quad report the independent calculation.

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

## 6. Acceptance

The 10 MeV C1 baseline uses the reviewed SFHo-18.8 profile, 103 actual radial nodes, 32 energy nodes, 121 coupling points, and all three physical polarizations.

Acceptance requires:

- all analytic and boundary-layer regression tests pass;
- all adaptive luminosities are finite and nonnegative;
- the mode-resolved luminosities close to the total;
- QUADPACK relative error estimates remain below \(10^{-6}\) for total and each mode;
- the high-coupling result approaches the independently recorded surface asymptote;
- the adaptive result is stable under the 103/153 radial-grid comparison.

No A0 result or SN1987A exclusion curve is updated at this stage.
