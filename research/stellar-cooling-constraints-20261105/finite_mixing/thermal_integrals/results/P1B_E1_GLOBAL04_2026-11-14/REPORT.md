# P1-B E1 Global-04: expanded high-order quadrature validation

**Benchmark:** SFHo-18.8, t_pb = 1 s; m_A' = 10 MeV; pure-vector endpoint gV/gX = 1, gA/gX = 0. Both muon charges and all three physical polarizations use the exact-recoil moving-muon B.13 kernel.

**Profile SHA-256:** `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

## 1. Top-50 two-dimensional interpolation cells

The 50 largest low-order sequential-PCHIP interpolation-error cells were selected. They span r = 13.85–16.10 km and x_mid = 0.78125. Both radial endpoints at all nine energy knots and the direct 2D cell center were re-evaluated, giving 900 endpoint nodes plus 50 cell centers: **950 high-order B.13 nodes**.

The adaptive quadrature ladder was (16,10,10,10) → (20,12,12,12) → (24,14,14,14) → (28,16,16,16) → (32,18,18,18) → (36,20,20,20).

**50/50 selected cells pass.** All 950 nodes satisfy the 0.1% successive-order criterion. Among 900 endpoint nodes, 871 terminate at (20,12,12,12) and 29 at (24,14,14,14). Maximum endpoint change: 0.09556%; maximum cell-center change: 0.004173%.

High-order direct cell-center comparison with the retained sequential PCHIP prescription:

| Metric | Result |
|---|---:|
| Maximum interpolation discrepancy | **0.806843%** |
| 95th percentile | 0.794451% |
| Median | 0.747481% |
| Cells above 1% | **0/50** |

Maximum detailed-balance residual: 5.35e-15. Maximum final-muon mass-shell residual: 1.09e-13. All rates finite and nonnegative.

## 2. Stratified radial high-order checks

Sixteen radial intervals were selected across the complete 1687-row profile, including interval 1024. At each interval, left endpoint, radial midpoint and right endpoint were directly evaluated at x = {0.5, 0.78125, 6, 18, 36}. This gives **240 high-order direct nodes**. All pass the 0.1% criterion.

| Check | Result |
|---|---:|
| Maximum successive-order change | 0.099067% |
| Maximum radial midpoint interpolation discrepancy | 0.082851% |
| Maximum detailed-balance residual | 8.18e-15 |
| Maximum final-muon mass-shell residual | 5.38e-13 |
| Non-finite or negative rates | 0 |

The closest-to-threshold initial change occurs at interval 481, right endpoint, x = 18. It was independently refined through (32,18,18,18); successive changes decrease from 0.099067% to 0.025733%, 0.006778% and 0.001833%.

Two further near-threshold checks also pass:
- Interval 361, right endpoint, x = 36: (24,14,14,14) → (28,16,16,16) changes by 0.030884%.
- Top-50 endpoint at radial index 981, x = 36: (20,12,12,12) → (24,14,14,14) changes by 0.021444%.

## 3. Disposition

**Passed:** high-order direct quadrature for all 50 worst PCHIP cells; 240 direct nodes across 16 stratified radial intervals; three extra near-threshold refinements; high-order PCHIP errors below 1%; detailed balance, final-muon shell closure and positivity.

**Not claimed:** exhaustive high-order evaluation at every radial-energy node or every 2D cell center; full-star B.1 source integral with exact B.13 Compton; B.2 path optical depth updated with the exact B.13 polarization-resolved Compton kernel; new luminosity; Fig. 7 reproduction; or updated SN1987A limit.

The full-profile low-order 2D interpolation screen and expanded selected high-order checks support retaining nine-knot PCHIP in sqrt(x), followed by log-radial interpolation. The next physics step is to insert the exact B.13 mode-resolved Compton source and reduced absorption consistently into the B.1/B.2 transport comparison. The literal B.16 scalar Fig. 7 baseline and axial-vector exclusion curve remain unchanged.

The reproducibility bundle is `P1B_E1_GLOBAL04_HIGH_ORDER_2026-11-14.zip`, SHA-256:
`c549a2f16c563ea5e44257297cc722c40da8b5a34145109ebcaf012bb362e68d`.
