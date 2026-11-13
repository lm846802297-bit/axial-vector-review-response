# P1-B E1 — one-bisection energy interpolation anchor audit

**Status: selected radial-anchor interpolation screening PASS; full 1687-knot radial acceptance OPEN.**

## Fixed physics and profile

- Exact-recoil moving-muon semi-Compton B.13 kernel.
- Pure-vector benchmark: (m_{A'}=10\,\mathrm{MeV}), (g_V/g_X=1), (g_A/g_X=0).
- Both targets ((mu^-), (mu^+)) and all physical modes ((L,+,-)) retained.
- SFHo-18.8, (t_{pb}=1\,\mathrm{s}), 1687-row digitized profile.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

## Energy grid and interpolation test

The original scouting grid is

\[
x=(\omega_{\rm local}-m_{A'})/T(r),\qquad x=\{0.5,2,6,18,36\}.
\]

One bisection in `sqrt(x)` gives the 9-knot interpolation grid

\[
\{0.5,1.125,2,3.73205,6,11.19615,18,26.22792,36\}.
\]

The interpolant is PCHIP in `sqrt(x)` applied to `log Gamma_abs`. Production and reduced absorption are reconstructed at the exact local temperature using detailed balance; they are not independently interpolated.

The 9-knot interpolant is tested at the 8 direct energy midpoints between its knots. All six charge/polarization channels are checked.

## Radial anchor results

| Radial anchor | Temperature (MeV) | Maximum PCHIP error |
|---|---:|---:|
| Center, 0 km | 19.2652 | 0.6828% |
| Peak-temperature shell, 8.48214 km | 39.2497 | 0.4311% |
| Previous G2 worst-energy radius, 14.575 km | 15.0228 | 0.7351% |
| ADAPTIVE-01 patch, 21.63469 km | 3.62888 | 0.3381% |
| Steep-gradient region, 22.1 km | 3.53234 | 0.3289% |
| Muon chemical-potential support edge, 22.191894 km | 3.51524 | 0.3273% |
| Outer profile, 24.5 km | 3.12241 | 0.2891% |

All seven selected anchors pass the 1% interpolation screen. The worst of these is 0.7351% at 14.575 km, in the (mu^-) longitudinal channel near (x=0.78125).

At the previous G2 worst-energy point ((r=14.575\,\mathrm{km}), (x=10.3923048)), direct B.13 evaluation gives a 0.7631% local log-linear interpolation discrepancy between the refined knots (x=8.3971) and (11.1962). The order-24 to order-28 rate change at the three directly evaluated points is at most (1.4881\times10^{-7}).

At the narrow muon-support edge, a simple two-endpoint log-linear interpolation at the first low-energy subcell gives 1.0261%, slightly above 1%; the full 9-knot PCHIP check over all eight energy midpoints reduces the maximum to 0.3273%. This is why the selected interpolation prescription is PCHIP, not piecewise log-linear interpolation.

## Quadrature checks

At the peak-temperature shell, the 17 direct points (9 interpolation knots plus 8 validation midpoints) were checked with an adaptive order ladder. The maximum final successive-order change is (8.8413\times10^{-4}) (0.0884%), below the project criterion (10^{-3}). The worst final pair is ((24,14,14,14)\to(28,16,16,16)) at (x=21.92094); the high-energy points (x=26.22792), (30.92094), and (36) were escalated through ((36,20,20,20)).

At other radial anchors, high-order comparisons were targeted to the worst low-energy interpolation cell and the previous G2 worst-energy point. These targeted changes are all below (10^{-3}); they do not constitute a pointwise quadrature scan of every channel at every energy node for every radius.

Detailed-balance and final-muon mass-shell residuals remain many orders of magnitude below (2\times10^{-10}) in the reported direct checks.

## Scope boundary and next step

This is a 7-anchor E1 validation, not a full 1687-radial-knot E1 scan. The checkpointed low-order global energy-scan driver is included separately and has passed a two-radius smoke test; its full 1687-knot run has not yet completed. No full-star emissivity, GR optical depth, luminosity, or SN1987A constraint is claimed.

Next: execute the checkpointed low-order E1 scan on all 1687 original radial knots, rank the worst radial/energy/channel combinations, then high-order B.13 re-evaluate only those worst points. Preserve all original G1, ADAPTIVE-01, and Run #43376779901 records unchanged.
