# Global B.13 stage-A convergence audit: status (2026-11-09)

## Scope

This report records the numerical-convergence work for the 10 MeV pure-vector B.13 global transport benchmark. The physical collision kernels, fixed-\omega B.2 convention, SFHo-18.8 vertex-preserving profile, and interaction channels are held fixed. No empirical source/opacity/luminosity rescaling is applied. No production axial-vector curve or manuscript file is modified.

The profile fingerprint is:

\[
\texttt{SHA256}= \texttt{9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c}.
\]

The original B.13 reference grid is \(N_r=40\), \(N_E=100\), \(N_\Omega=16\), \(N_s=32\).

## 1. Radial and energy quadrature: completed

The successful GitHub Actions run [42536610504](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42536610504) generated the output file outputs/b13_global_grid_convergence_2026-11-09.json. Each refined B.13 run was paired with a B.16 baseline regenerated on the identical radial, energy, angular, and path grid. The B.16 closure residual was exactly zero for all three configurations.

For the like-for-like \(\mu^-\)-only B.13 variant (the species convention matching the single negative-muon distribution in Eq. (B.17)):

| \(N_r\) | \(N_E\) | Maximum absolute luminosity shift relative to \(40\times100\times16\times32\) |
|---:|---:|---:|
| 60 | 100 | \(0.10630\%\) |
| 40 | 140 | \(0.28410\%\) |
| 60 | 140 | \(0.27316\%\) |

The combined \(60\times140\) radial-energy grid therefore meets the project-level \(1\%\) luminosity-stability target. These are numerical acceptance targets, not physical uncertainty estimates.

At \(60\times140\times16\times32\), the B.13 luminosity differences relative to Fig. 7 are:

| Fig. 7 location | Relative difference |
|---|---:|
| Weak-coupling endpoint | \(-28.3054\%\) |
| Reference peak | \(-16.5636\%\) |
| Strong-coupling endpoint | \(+131.1176\%\) |

For comparison, the original \(40\times100\times16\times32\) summary gives \(-28.1090\%\), \(-16.3397\%\), and \(+131.5300\%\), respectively. The strong-endpoint discrepancy changes by only about \(0.41\) percentage points under the combined radial-energy refinement. Thus the large strong-coupling discrepancy is not explained by insufficient radial or energy quadrature at the tested resolutions.

The optically thin B.13/B.16 source ratio changes from \(0.7889823\) on the original grid to \(0.7888233\) on the \(60\times140\) grid. The strong-endpoint source-weighted escape fraction changes from \(4.94463\times10^{-4}\) to \(4.94935\times10^{-4}\). Both changes are small.

## 2. Angular and path quadrature: in progress

The next audit varies the angular and path quadrature orders while regenerating the B.16 comparison calculation on the same grid for every B.13 run. The current targeted configurations are:

- \(40\times100\times24\times48\): angular/path refinement at fixed radial and energy grids;
- \(60\times140\times24\times48\): combined radial, energy, angular, and path refinement.

The run must pass the B.16 same-grid closure check before its B.13 result is interpreted. The first two attempts of the new workflow failed before computation because the checkout ref was malformed; a subsequent checkout fix succeeded. A further implementation issue (using the \(40\times100\times16\times32\) B.16 baseline for a different grid) was identified and corrected by regenerating the B.16 baseline on each matching grid.

The latest corrected run is tracked at [GitHub Actions run 42541492019](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42541492019); a follow-up run with the corrected result-count validation is queued as [run 42541508076](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42541508076). Neither is treated as a completed numerical result in this report.

## 3. Current decision

- Radial and energy quadrature: passed at the tested resolutions.
- Angular and path quadrature: not yet accepted; same-grid B.16 closure and B.13 luminosity/escape-fraction shifts remain to be checked.
- Local B.13 collision-kernel quadrature: outside this stage-A audit; reserved for the subsequent local-kernel convergence stage.
- Axial-vector production curve: remains frozen.

The stage-A audit is not complete until the angular/path scan and the combined refinement have produced archived JSON outputs and passed their same-grid closure checks.
