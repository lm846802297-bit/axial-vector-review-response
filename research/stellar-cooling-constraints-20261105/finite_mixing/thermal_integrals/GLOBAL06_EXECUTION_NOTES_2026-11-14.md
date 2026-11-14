# Global-06 execution notes

The Global-06 source package is on branch:
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

## Important scope limits

- This Global-06 interval is x in [0.05,0.5]. It does not cover 0 <= x < 0.05.
- The first pass is low-order and the high-order follow-up is targeted, not a full high-order scan of all 1687 x 17 nodes.
- Do not start Global-07 B.1 integration or describe the complete spectrum as covered until the threshold-adjacent interval and both interpolation/high-order checks are resolved.
- Do not alter the original Run #43376779901, G1, ADAPTIVE-01, or merged Global-02–05 outputs.
- Do not change the scalar B.2 baseline, the vector Fig. 7 acceptance status, or any axial/SN1987A limit.
