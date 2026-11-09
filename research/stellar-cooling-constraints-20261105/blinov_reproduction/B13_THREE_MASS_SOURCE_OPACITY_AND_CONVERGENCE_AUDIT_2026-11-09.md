# B.13/B.16 three-mass source, opacity, and convergence audit (2026-11-09)

## Executive result

The formal moving-muon Compton expression B.13 has now been integrated globally with the source and reduced absorption replaced consistently at 0.1, 1, and 10 MeV, on the same reconstructed profile and literal fixed-omega B.2 ray prescription. This is a method-level comparison; it does not determine which unpublished implementation the authors used for Fig. 7.

The exact B.13 source is substantially smaller than the B.16 reduced source in the dominant 5--12 km emitting region. The B.13/B.16 source ratio, weighted by the B.16 source distribution over 5--12 km, is 0.338 at 0.1 and 1 MeV and 0.340 at 10 MeV. The corresponding source-weighted Compton reduced-opacity ratios are 0.353, 0.352, and 0.360. These are not global luminosity rescalings; they are diagnostics of the two collision prescriptions evaluated on the same profile.

## 1. Global Fig. 7 comparison

The B.13 consistent variant means the exact moving-muon source and reduced absorption are both substituted, while neutrino inverse decay, dimuon channels, background, and B.2 geometry remain unchanged.

| mV | B.13 peak residual | B.13 weak-end residual | B.13 strong-end residual |
|---:|---:|---:|---:|
| 0.1 MeV | -23.73% | -66.11% | +0.33% |
| 1 MeV | -34.79% | -64.70% | +138.84% |
| 10 MeV | -16.27% | -28.04% | +131.59% |

The 10 MeV point is a stress test outside the paper's stated mV less than or approximately 1 MeV Compton-dominance regime. The primary comparison for judging the reduced Compton prescription is therefore 0.1 and 1 MeV.

The strong-endpoint response is not determined by the optically thin source alone. B.13 changes both the emitted source and the optical-depth integrand; the escape probability depends exponentially on the integrated opacity. Source-only and opacity-only substitutions are therefore useful diagnostics but are not physical alternatives to the consistent replacement.

## 2. Dominant-region source and opacity ratios

| mV | B.13/B.16 source ratio in 5--12 km (B.16-source weighted) | B.13/B.16 Compton reduced-opacity ratio (B.16-source weighted) |
|---:|---:|---:|
| 0.1 MeV | 0.3377 | 0.3526 |
| 1 MeV | 0.3377 | 0.3518 |
| 10 MeV | 0.3399 | 0.3596 |

The 5--12 km interval captures the dominant source region. The shell-by-shell ratios are stable across the three masses: about 0.325 in 8--10 km and 0.368 in 10--12 km. The similarity of the ratios at 0.1 and 1 MeV is consistent with the low-mass limit, where the explicit mV-dependent correction in B.14 is small compared with the change induced by the moving-muon/no-recoil reduction.

The source-weighted total-opacity ratio is 0.353 at 0.1 MeV and 0.400 at 1 MeV. At 10 MeV the total opacity is dominated by neutrino inverse decay, so its total-opacity ratio is close to unity; the Compton-only ratio remains about 0.360.

## 3. High-order local-kernel convergence

The exact B.13 local kernel has been tested at three representative source-weighted points:
(r, omega) = (8 km, 15 MeV), (12.5 km, 20 MeV), and (15 km, 30 MeV).

The order ladder is (12,8,8,8), (16,10,10,10), (20,12,12,12), and (24,14,14,14), for muon kinetic energy, initial-muon polar angle, photon polar angle, and relative photon azimuth.

| mV | Maximum change from (20,12,12,12) to (24,14,14,14) |
|---:|---:|
| 0.1 MeV | 0.02831% |
| 1 MeV | 0.02880% |
| 10 MeV | 0.03016% |

All three sampled-mass audits pass the project's explicitly adopted 0.1% local screening target. This is a sampled-point convergence test, not a uniform error bound over the full continuous radius-energy domain. The global B.1/B.2 luminosity integrals still need a dedicated convergence study with the high-order kernel at the source- and opacity-dominant nodes.

Successful low-mass workflow: [Run #42575922722](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42575922722). The 10 MeV high-order audit is archived in [Run #42575916846](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42575916846).

## 4. Algebraic and detailed-balance checks

The B.13 local kernel retains charge-resolved and polarization-resolved production and absorption. Across the global scans, final-muon mass-shell residuals are approximately 4e-13, and mode-by-mode detailed-balance residuals are approximately 1e-14. The high-order local convergence runs reduce the detailed-balance residuals to below 2e-15.

The B.14 non-relativistic susceptibility diagnostic finds a source-weighted mean muon speed of 0.761 and 93.2% of the susceptibility weight at v_mu greater than 0.5. This is evidence that the non-relativistic reduction is not parametrically controlled in the dominant source region; it is not itself a direct rate-error estimate. The B.13/B.16 source and opacity comparison supplies the direct rate-level diagnostic.

## 5. Interpretation

Established:
1. The exact moving-muon B.13 kernel is numerically stable at the sampled dominant-region points for all three masses.
2. Its dominant-region Compton source and reduced opacity are both about one third of the B.16 reduced result on the same profile.
3. The global B.13 replacement has been evaluated at 0.1, 1, and 10 MeV, with source-only, opacity-only, mu-minus-only, and both-charge controls.
4. The strong-coupling luminosity response is nonlinear and cannot be inferred from a simple source ratio.

Not established:
1. A uniform local-kernel error bound across all global radius-energy nodes.
2. Convergence of the full B.13 B.1+B.2 luminosity curves under refinement of the kernel, energy, radial, angular, and path quadratures together.
3. Whether the unpublished Fig. 7 implementation used B.13 or B.14--B.16.
4. Whether the B.2 fixed-omega path prescription in the authors' code follows the literal printed expression or an implicit local redshift conversion.

No empirical rescaling is applied. No axial-vector curve or production output is changed.

## 6. Reproducibility

- Global three-mass summaries:
  - `outputs/b13_global_transport_summary_vertex_preserving_0p1mev_2026-11-09.json`
  - `outputs/b13_global_transport_summary_vertex_preserving_1mev_2026-11-09.json`
  - `outputs/b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json`
- Local high-order convergence:
  - `outputs/b13_local_kernel_quadrature_convergence_0.1mev_2026-11-09.json`
  - `outputs/b13_local_kernel_quadrature_convergence_1mev_2026-11-09.json`
  - `outputs/b13_local_kernel_quadrature_convergence_10mev_2026-11-09.json`
- Global three-mass compact archive workflow: [Run #42574536735](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42574536735)
- Exact-kernel local convergence workflows: [Run #42575922722](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42575922722), [Run #42575916846](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42575916846)
