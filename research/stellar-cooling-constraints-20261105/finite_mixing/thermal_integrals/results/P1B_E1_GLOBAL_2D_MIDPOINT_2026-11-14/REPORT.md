# P1-B E1 Global-03: full-profile 2D radial-energy midpoint screen

**Profile:** SFHo-18.8, t_pb = 1 s; 1687 radial vertices; SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.  
**Kernel:** exact-recoil moving-muon semi-Compton B.13; m_A' = 10 MeV; pure-vector endpoint gV/gX = 1, gA/gX = 0.  
**Screening quadrature:** `(10,6,6,6)`; both muon charges and all three A' polarizations.

## Coverage

- All 1686 adjacent radial intervals were directly evaluated at the radial midpoint.
- All 17 E1 validation-energy coordinates were sampled at every radial midpoint: **28,662 direct B.13 midpoint evaluations**.
- This gives 28,662 radial-midpoint checks, 13,488 energy-PCHIP midpoint checks, and 13,488 two-dimensional cell-center checks.
- The original E1 radial-node direct-data archive was read-only; profile and E1-source hashes were checked.

## Interpolation results

| Check | Samples | Maximum error | 95th percentile | Samples above 1% |
|---|---:|---:|---:|---:|
| Radial midpoint, all 17 x nodes | 28,662 | 0.08284% | 0.02043% | 0 |
| Energy PCHIP at radial midpoints | 13,488 | 0.73617% | 0.58592% | 0 |
| 2D local bilinear-log cell centers | 13,488 | 5.47244% | 4.96038% | 11,509 |
| 2D sequential PCHIP in sqrt(x), then log-radial cell centers | 13,488 | 0.80678% | 0.59458% | 0 |

The local bilinear-log result is retained as a diagnostic and **must not be used as the production interpolant**. The preferred prescription is the nine-knot PCHIP in sqrt(x) at each radial endpoint, followed by log-linear interpolation in radius. Production, reduced absorption and spectral source are reconstructed from interpolated absorption using exact local detailed balance and the exact spectral phase-space factor.

### Worst locations

- Radial interpolation: interval 1024, r_mid = 15.525 km, x = 0.5, error 0.08284%.
- Energy PCHIP at a radial midpoint: interval 989, r_mid = 14.746175 km, x_mid = 0.78125, error 0.73617%.
- Sequential 2D PCHIP: interval 993, r = 14.85–14.90 km, r_mid = 14.875 km, x_mid = 0.78125, local omega = 20.74734 MeV, error 0.80678%.
- Worst local bilinear-log cell: interval 702, r_mid = 8.480239 km, x_mid = 8.397114, local omega = 339.57979 MeV, error 5.47244%; the sequential PCHIP error at this same cell is 0.45285%.

## Algebraic checks

- Maximum mode-resolved detailed-balance residual: 1.2384e-14.
- Maximum final-muon mass-shell residual: 5.3802e-13.
- All directly evaluated rates are finite and nonnegative.

## Targeted high-order follow-up

Four high-error cells were selected: the three largest sequential-PCHIP errors (intervals 993, 1016 and 1024, all at x_mid = 0.78125) and the largest local-bilinear diagnostic cell (interval 702, x_mid = 8.3971143).

For each selected interval, the nine energy knots at both radial endpoints and the selected cell center were re-evaluated with the order ladder
`(16,10,10,10) -> (20,12,12,12) -> (24,14,14,14) -> (28,16,16,16) -> (32,18,18,18)`.

The x = 36 endpoints of interval 702 required one further extension to `(36,20,20,20)`. Both endpoints passed the 0.1% successive-order criterion:

- r = 8.478337308 km: 0.0810633% change from `(32,18,18,18)` to `(36,20,20,20)`.
- r = 8.482141202 km: 0.0810797% change from `(32,18,18,18)` to `(36,20,20,20)`.

Across the four selected intervals, every tested endpoint and cell-center quadrature passed 0.1%; the largest final successive-order change was 0.0932701%, at the interval-702 cell center. The largest selected high-order PCHIP interpolation discrepancy was 0.806843% (interval 993).

The interval-702 high-order cell-center PCHIP comparison was subsequently recomputed using high-order values at all nine energy knots on both radial endpoints, including the order-36 x=36 endpoint extension. The recomputed PCHIP interpolation discrepancy is 0.418921%; the local bilinear-log discrepancy is 5.39108%. All 19 endpoint/cell-center quadrature nodes in this interval pass the 0.1% successive-order criterion. This removes the provisional interpolation caveat for interval 702.

## Acceptance boundary

**Passed:** complete low-order radial-midpoint, energy-PCHIP-at-radial-midpoint, and sequential 2D PCHIP cell-midpoint screens over all 1686 radial intervals; selected high-order convergence checks for the four worst interpolation cells; exact detailed-balance and mass-shell consistency.

**Not claimed:** a full-profile high-order quadrature scan at every radius/energy point; exhaustive direct high-order checks of every 2D cell; full-star volume emissivity; GR geodesic optical depth; luminosity; Fig. 7 reproduction; or an updated SN1987A limit. PR #113 remains Draft.


## Low-x support audit (Global-05, 2026-11-14)

The existing nine-knot Global-03/04 table covers \(x=(\omega-m_{A'})/T\in[0.5,36]\), and the B.2 interpolator returns zero Compton absorption outside that support. Before extending B.1/B.2 to the full energy range, we directly evaluated B.13 at 16 stratified radial nodes and five lower-energy coordinates \(x=0.05,0.1,0.2,0.35,0.5\), adding 80 low-order direct evaluations.

All 80 points were finite and nonnegative. The maximum detailed-balance residual was \(4.6060\times10^{-15}\), and the maximum final-muon shell residual was \(1.6261\times10^{-13}\).

**Important finding:** the B.13 absorption is not negligible below the existing interpolation support. At \(r=9.95\) km, the \(x=0.05\) to \(x=0.5\) \(\mu^-\) absorption ratios are 7.079 (longitudinal) and 1.817 in each transverse mode. At \(r=15.5\) km the corresponding ratios are 2.468 and 1.244. Thus setting the B.13 Compton term to zero for \(x<0.5\) is not justified by the existing table.

This 80-point screen is not a full radial scan or high-order acceptance, and it does not yet quantify the integrated luminosity impact. It establishes a necessary next task: extend the B.13 table below \(x=0.5\), then redo the full-band B.1/B.2 integration. Until then, the 210–510 MeV band result remains a valid restricted-band calculation, but the current full-band extrapolation is not accepted.
