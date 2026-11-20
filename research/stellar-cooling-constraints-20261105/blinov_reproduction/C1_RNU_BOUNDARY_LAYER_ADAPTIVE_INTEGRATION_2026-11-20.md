# C1 neutrinosphere boundary-layer adaptive integration

Date: 2026-11-20

Status: **103-node C1 adaptive calculation completed successfully; independent 153-node radial refinement is running.**

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

The independent 153-node calculation uses the same profile, coupling grid, energy quadrature, angular order, susceptibility order, and polarization definitions. Its purpose is to quantify the radial interpolation uncertainty, which is not included in the QUADPACK error estimate.

The earlier Simpson-based C1 grid audit provides an independent diagnosis of the problem. Raising the requested radial grid from 101 to 151 points (103 to 153 actual nodes) changed the \(R_{\rm far}=R_\nu\) total and each mode curve by \(0.3333333\), while the corresponding \(R_{\rm far}=100\) km curves changed by only \(2.47\times10^{-4}\). The thin-source changes were at most \(5.65\times10^{-4}\). By contrast, increasing the energy order from 32 to 48 changed the \(R_\nu\) total curve by only \(1.32\times10^{-7}\), and increasing the B.7 neutrino angular order from 128 to 192 changed it by less than \(10^{-14}\). The \(33.3\%\) radial change is therefore isolated to the \(R_\nu\) Simpson endpoint contribution; the adaptive 103/153 comparison directly tests whether that artifact is removed.


## 7. Acceptance

The 10 MeV C1 baseline uses the reviewed SFHo-18.8 profile, 103 actual radial nodes, 32 energy nodes, 121 coupling points, and all three physical polarizations.

Acceptance requires:

- all analytic and boundary-layer regression tests pass;
- all adaptive luminosities are finite and nonnegative;
- the mode-resolved luminosities close to the total;
- QUADPACK relative error estimates remain below \(10^{-6}\) for total and each mode;
- the high-coupling result approaches the independently recorded surface asymptote;
- the adaptive result is stable under the 103/153 radial-grid comparison.

No A0 result or SN1987A exclusion curve is updated at this stage.
