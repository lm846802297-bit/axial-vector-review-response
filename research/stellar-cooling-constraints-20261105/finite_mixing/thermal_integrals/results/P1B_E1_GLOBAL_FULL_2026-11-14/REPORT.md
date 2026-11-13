# P1-B Global-02: complete radial scan and E1 energy refinement

**Status:** complete low-order scan of all 1687 original SFHo-18.8 radial nodes; selected high-order checks completed. This is not a full high-order quadrature or full-star transport acceptance.

## Fixed benchmark and provenance

- Background: SFHo-18.8, post-bounce time 1 s, original digitized 1687-row radial profile.
- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.
- Kernel: exact-recoil moving-muon semi-Compton B.13.
- Benchmark: m_Aprime=10 MeV, gV/gX=1, gA/gX=0; both muon charges and all L,+,- modes.
- Original Run #43376779901, G1 and ADAPTIVE-01 records were not modified.

## 1. Full radial-by-energy collision-kernel layer

All 1687 original radii were evaluated at 17 energy coordinates per radius, for 28,679 direct low-order B.13 evaluations. The 17 coordinates comprise the original five energy knots, four first-bisection knots, and eight independent validation midpoints. The global screening order was (10,6,6,6).

The interpolation variable is x=(omega_local-m_Aprime)/T(r). The refined energy interpolant is PCHIP of log Gamma_abs in sqrt(x). Production, reduced absorption and spectral source are reconstructed at the local thermodynamic point using detailed balance rather than independently interpolated.

### Original versus one-bisection energy grid

| Metric | Original 5 knots | Refined 9 knots |
|---|---:|---:|
| Median radial-node maximum error | 2.4857% | 0.4806% |
| 95th percentile | 3.0737% | 0.7041% |
| Global maximum | 3.0794% | 0.7362% |
| Radial nodes with error above 1% | 1687/1687 | 0/1687 |

The original five-knot grid fails the 1% screen at every radial node. One bisection reduces the global maximum to **0.7362%**, with zero radial nodes above 1%.

The refined-grid worst point is r=14.74234939 km, x=0.78125, charge mu_minus, mode L.

Global micro-consistency maxima: detailed-balance residual 1.121e-14; final muon mass-shell residual 6.214e-13. All rates are finite and nonnegative.

## 2. Global radial-neighbor ranking and direct midpoint checks

All 1686 adjacent radial intervals were ranked using the maximum symmetric relative change in production/absorption across both charges, all three modes and all 17 energy nodes. The largest neighbor change is 24.76% in interval 1487 (22.19189366–22.19189466 km), at x=0.5, mu_minus, production, mode +. This is a variation indicator, not itself an interpolation error.

The 60 highest-variation intervals were then checked by direct low-order B.13 evaluations at their true radial midpoints and all nine refined energy knots (540 midpoint evaluations). The endpoint log-linear radial interpolation was compared against each direct midpoint.

- Maximum radial midpoint interpolation error: **0.0828%**.
- Intervals exceeding 1%: **0/60**.
- Worst interval: 1024, r=15.50000000–15.55000000 km, at x=0.5.

The narrow support-edge interval near 22.191894 km has a 24.76% neighbor-change indicator but a direct midpoint interpolation error of only 3.078e-09; the steep-gradient interval 22.100000–22.135104 km has a direct midpoint error of 0.0128%. This illustrates why neighbor changes must be followed by midpoint kernel checks.

## 3. Targeted high-order B.13 acceptance

At the global energy-interpolation worst radial node (r=14.74234939 km), the 9 interpolation knots plus the worst energy midpoint were directly re-evaluated with the order ladder. The maximum successive-order change was 7.469e-04 at final order (20,12,12,12), below the 1e-3 quadrature criterion. The high-order PCHIP error at x=0.78125 is 0.7362%, below 1%.

The two worst radial-midpoint intervals that were rechecked at high order also pass the 1e-3 successive-order criterion:

- 15.500–15.550 km: high-order midpoint interpolation error 0.0829%.
- 22.100–22.135104 km: high-order midpoint interpolation error 0.0128%.

The tiny 22.191894–22.191895 km support-edge interval has only the low-order direct midpoint check in this round; its low-order interpolation error is 3.08e-9 and is not counted as high-order verified.

## 4. Acceptance boundary

**Passed:** complete 1687-node low-order energy interpolation screen; all 1687 refined-grid radial nodes below 1%; direct radial midpoint checks for the top 60 neighbor-variation intervals; selected high-order checks of the global energy worst point and two radial-midpoint worst intervals.

**Not claimed:** global high-order quadrature convergence at every radius/energy point; exhaustive radial-midpoint validation of all 1686 intervals; full-star volume emissivity; GR optical depth; luminosity; Fig. 7 reproduction; or updated SN1987A exclusion curves.

Next: retain the 9-knot energy prescription, high-order verify the remaining edge case if needed, then proceed to the volume-weighted production and GR transport only after the vector baseline acceptance gates are met.
