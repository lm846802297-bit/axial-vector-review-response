# Global-06 execution notes

> Historical stage record: later work can postdate its sequencing statements. Check current project status and subsequent stage records before using it as an execution plan. The reported acceptance is limited to this stage.

The Global-06 source package and compact results are on branch:
research/p1b-global06-low-x-full-radial-20261114

## Drivers

1. run_p1b_global06_low_x_full_radial.py
   - 1687 original radial vertices.
   - 9 formal low-x interpolation knots and 8 independent energy validation points.
   - 28,679 direct low-order B.13 evaluations.
   - All 1686 radial intervals ranked; top 60 receive 540 direct radial-midpoint evaluations.
   - Writes 48-radius chunks, energy interpolation checks, radial ranking, midpoint checks, and GLOBAL06_SUMMARY.json.

2. run_p1b_global06_high_order_targets.py
   - Reads the completed Global-06 output directory.
   - Re-evaluates the worst 10 energy interpolation points and top 10 radial-neighbor intervals.
   - Uses successive order checks through (26,14,14,14), extending to (30,16,16,16) when the last change is >= 0.1%.
   - Checks high-order energy PCHIP and radial midpoint interpolation, not just the raw local quadrature.

## Direct execution

Run from a checkout of this branch with NumPy and SciPy installed:

    python research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/run_p1b_global06_low_x_full_radial.py

After the low-order run finishes:

    python research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/run_p1b_global06_high_order_targets.py

The physics calculation is intended to run in the direct research compute environment. A source-bundle or unit-test CI workflow is not counted as the numerical computation. Do not run the high-order driver until GLOBAL06_SUMMARY.json and the radial/energy output files exist.

## Completed result summary

- 1687/1687 radial vertices, 17 energy coordinates each: 28,679 direct low-order B.13 points.
- All 1686 radial intervals ranked; top 60 received 540 direct midpoint evaluations.
- Maximum energy PCHIP error: 0.0325955%; maximum top-60 radial midpoint error: 0.0830916%.
- Targeted high-order check: 431 unique (r,x) points, 2,155 nominal ordered evaluations; all selected points pass the 0.1% successive-order criterion. Maximum change: 0.0328258%.
- Detailed-balance maximum: 6.8693e-15; mass-shell maximum: 2.0432e-13; all rates finite/nonnegative.
- Raw 36-chunk data and exact local runner scripts are archived in the conversation download bundle. Archive SHA-256: 54b4ce938034d154b2eeb7ede87f720e21eafb24e08f9743380fb313679c05df.

The threshold-edge smoke test at x=0, 1e-4, 1e-3, 0.005, 0.01, 0.025 and 0.05 was finite at r=8.48214, 9.95 and 22.19189 km. Absorption remains finite at x=0 while the spectral source is zero there because k_A'=0. A separate full-radial threshold-edge scan for 0 <= x <= 0.05 is running; do not yet claim complete low-energy coverage.

## Important scope limits

- This Global-06 interval is x in [0.05,0.5]. It does not cover 0 <= x < 0.05.
- The first pass is low-order and the high-order follow-up is targeted, not a full high-order scan of all 1687 x 17 nodes.
- Do not start Global-07 B.1 integration or describe the complete spectrum as covered until the threshold-adjacent interval and both interpolation/high-order checks are resolved.
- Do not alter the original Run #43376779901, G1, ADAPTIVE-01, or merged Global-02–05 outputs.
- Do not change the scalar B.2 baseline, the vector Fig. 7 acceptance status, or any axial/SN1987A limit.
