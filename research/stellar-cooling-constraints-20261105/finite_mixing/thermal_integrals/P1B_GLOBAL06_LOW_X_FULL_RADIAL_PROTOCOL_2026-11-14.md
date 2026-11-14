# P1-B Global-06: full-radial low-x B.13 extension

> Historical stage record: later work can postdate its sequencing statements. Check current project status and subsequent stage records before using it as an execution plan. The reported acceptance is limited to this stage.

**Date:** 2026-11-14  
**Status:** execution package prepared; no new Global-06 numerical result is claimed by this protocol commit.  
**Parent baseline:** merged main after PR #106 and #113.  
**Profile:** SFHo-18.8, t_pb = 1 s, 1687 radial rows; SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.

## 1. Scope

Extend the exact-recoil moving-muon semi-Compton B.13 local collision kernel into the low-energy support interval
\[
x=(\omega_{\rm local}-m_{A'})/T(r)\in[0.05,0.5].
\]
The benchmark remains m_A' = 10 MeV, g_V/g_X = 1, g_A/g_X = 0. Both muon charges and all three A' polarization modes remain separate. The scalar B.2 reference, Run #43376779901, G1, ADAPTIVE-01, and merged Global-02–05 outputs are read-only.

This interval extension does **not** cover 0 <= x < 0.05. That threshold-adjacent interval must be tested separately before calling the later B.1 energy integral complete.

## 2. Energy grid

Start from the established five knots
\[
x_0=(0.05,0.1,0.2,0.35,0.5).
\]
Bisect each interval once in sqrt(x), yielding nine formal interpolation knots:
\[
(0.05,0.0728553391,0.1,0.1457106781,0.2,
0.2697875656,0.35,0.4216650066,0.5).
\]
The eight midpoints between these formal knots in sqrt(x) are independent direct validation points. Every one of the 1687 original radial vertices receives all 17 energy evaluations: 28,679 low-order direct B.13 points.

## 3. Quadrature and output

The first-layer screening rule is (10,6,6,6), with the same variable/order convention as the existing B.13 audit. The driver writes 48-radius chunks to avoid a monolithic output file. It retains, separately for mu_minus and mu_plus:
- absorption and production for L,+,-;
- reduced absorption and spectral source;
- detailed-balance residual, final-muon shell residual, charge-sum closure, and finite/nonnegative flags.

Production and reduced absorption are not independently interpolated. The interpolation check uses PCHIP(log absorption) in sqrt(x), followed by exact local detailed-balance reconstruction.

## 4. Radial interpolation audit

All 1686 adjacent radial intervals are ranked by the maximum symmetric relative change across both charges, all three modes, production and absorption, at the nine formal low-x knots. The top 60 intervals receive direct midpoint evaluations at all nine formal knots (540 extra B.13 points). Endpoint log interpolation of absorption is compared with the direct midpoint kernel. This is a targeted radial midpoint screen, not an exhaustive midpoint validation of all 1686 intervals.

## 5. Acceptance criteria

These are project numerical screening criteria, not literature uncertainties:
- low-x energy interpolation: maximum direct validation error < 1%;
- top-60 radial midpoint interpolation: maximum direct midpoint error < 1%;
- detailed balance residual < 2e-10;
- final-muon mass-shell relative residual < 2e-10;
- every computed rate finite and nonnegative.

A low-order screen passing these criteria does not establish high-order quadrature convergence. The companion targeted driver re-evaluates the worst energy-validation points and top radial intervals with the order ladder
(10,6,6,6) -> (14,8,8,8) -> (18,10,10,10) -> (22,12,12,12) -> (26,14,14,14), extending to (30,16,16,16) if needed. Its scope is selected points only, not a global high-order scan.

## 6. Next gates

1. Execute the low-order full-radial driver in a direct research compute environment (not by treating a CI/source-bundle job as the physics computation).
2. Inspect the worst energy channels, radial intervals, and any non-finite/negative rates.
3. Execute the targeted high-order driver and archive its raw results.
4. If either interpolation criterion fails, refine the corresponding x/r grid and repeat only the affected region.
5. Only after Global-06 is accepted, combine low-x and high-x tables for Global-07 B.1. Before that integration, separately test 0 <= x < 0.05 and confirm the energy-domain lower-bound behavior.

No full-band B.1/B.2, luminosity, Fig. 7, SN1987A, or axial-limit result is claimed here.
