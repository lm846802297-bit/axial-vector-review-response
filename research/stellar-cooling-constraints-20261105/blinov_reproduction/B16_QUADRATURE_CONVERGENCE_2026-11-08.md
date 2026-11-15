# B.16 fixed-omega quadrature convergence at mV = 10 MeV

> **HISTORICAL — not the current profile-B convergence result.** The machine-readable output records profile SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`; the current vertex-preserving profile B used by the 10 MeV baseline is `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. The six-configuration values below remain valid for their archived input, but the stated 0.3% convergence envelope must not be quoted as a full six-configuration rerun on profile B.


**Status:** six-configuration quadrature audit completed; all closure checks pass.  
**Benchmark:** pure-vector B.14--B.16, SFHo-18.8 figure-reconstructed background at t_pb = 1 s.  
**Important provenance limitation:** the radial thermodynamic profile is digitized from public figures, not the original Garching simulation table.

## 1. Configurations

The baseline uses \((N_r,N_E,N_\Omega,N_s)=(40,100,16,32)\). Four one-factor tests independently increase radial, energy, angular, and path quadrature orders. A combined test uses \((60,150,24,48)\).

| Configuration | \(N_r\) | \(N_E\) | \(N_\Omega\) | \(N_s\) |
|---|---:|---:|---:|---:|
| Baseline | 40 | 100 | 16 | 32 |
| Radial refinement | 60 | 100 | 16 | 32 |
| Energy refinement | 40 | 150 | 16 | 32 |
| Angular refinement | 40 | 100 | 24 | 32 |
| Path refinement | 40 | 100 | 16 | 48 |
| Combined refinement | 60 | 150 | 24 | 48 |

## 2. Luminosity convergence

At the weak-coupling endpoint, the reference luminosity peak, and the strong-absorption endpoint, the maximum relative changes with respect to the baseline are:

| Refinement | Maximum absolute luminosity change |
|---|---:|
| \(N_r:40\to60\) | 0.199% |
| \(N_E:100\to150\) | 0.322% |
| \(N_\Omega:16\to24\) | 0.00512% |
| \(N_s:32\to48\) | 0.00568% |
| All refinements together | 0.294% |

At the reference luminosity peak, the combined refinement changes the result by -0.281%. At the strong-absorption endpoint it changes the result by -0.132%. The energy quadrature is the largest single numerical contribution among the tested refinements; angular and path quadratures are already stable at the \(10^{-4}\) level in luminosity.

The source mean radius changes by only \(-6.8\times10^{-5}\) in relative terms under the combined refinement. The median and 90th-percentile radii move by 0.32 km and -0.48 km because these quantiles are read from a finite set of Gauss-Legendre radial nodes; they should not be interpreted as smooth continuous quantile estimates. The shell-integrated source fractions are the more robust radial summary.

## 3. Internal closure

For every configuration:

- channel-resolved source terms reconstruct the total B.1 source to better than \(6\times10^{-16}\);
- the sum of radial-shell opacity columns reconstructs the direct chord integral to better than \(7\times10^{-16}\);
- the emission/absorption-shell matrix reconstructs the direct source-weighted mean optical depth to machine precision;
- angular weights agree exactly between the compared calculations.

These checks verify the numerical bookkeeping and quadrature implementation, not the accuracy of the digitized supernova profile relative to the original simulation.

## 4. Interpretation

The baseline quadrature \((40,100,16,32)\) is adequate for the present Fig. 7 comparison at the sub-percent level. The 0.3% convergence envelope is far smaller than the discrepancy at the strong-absorption end of the 10 MeV curve (about 92% at the last visible point in the current baseline reconstruction). That discrepancy cannot be explained by the tested radial, energy, angular, or path quadrature resolution.

The next investigation should therefore not increase quadrature orders indiscriminately. It should isolate physical/input differences in the high-coupling tail, especially the source/opacity response to the reconstructed outer profile, the exact semi-Compton susceptibility input, and any assumptions about the radial extent and interpolation of the SFHo-18.8 background. The published Fig. 7 digitization geometry has separately passed the raw-PDF coordinate audit.

## 5. Reproducibility

- Script: audit_b16_quadrature_convergence.py
- Machine-readable output: outputs/b16_quadrature_convergence_10mev_2026-11-08.json
- Workflow: B.16 fixed-omega quadrature convergence
- Baseline orders: \((40,100,16,32)\)
- Combined orders: \((60,150,24,48)\)

## 6. Profile-version disposition (2026-11-15)

The JSON output outputs/b16_quadrature_convergence_10mev_2026-11-08.json records profile_sha256=08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9. The later vertex-preserving baseline uses profile B with SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. The checked-in driver defaults to the profile imported as DEFAULT_PROFILE from audit_b16_emission_radius_escape.py, and the archived JSON confirms that the six-configuration scan was run on the earlier profile.

Accordingly, the six one-factor/combined refinement values and internal closures are retained as a historical quadrature study for the old profile. They do not establish the same convergence envelope for profile B. Later current-profile work independently checks the B.2 high-energy chord and path integrations, but does not constitute a rerun of this full six-configuration, 25-point luminosity scan. A current-profile six-configuration rerun would be required before reusing the 0.3% figure as a profile-B numerical uncertainty.

**Review disposition: HISTORICAL.** Preserve the original output and its provenance; do not overwrite or relabel its profile hash.
