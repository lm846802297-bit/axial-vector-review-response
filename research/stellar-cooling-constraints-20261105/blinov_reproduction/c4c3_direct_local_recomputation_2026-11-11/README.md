# C4-C3 direct local recomputation

Date: 2026-11-11

## Result

The 301-point, 1204-case EOS moving-nucleon total-scattering calculation was
re-executed locally. GitHub Actions was not used to perform this calculation.

- Incident local neutrino energy: 100 MeV
- Radial grid: 301 points, 0.20–15.20 km, 0.05 km spacing
- Target species: neutron and proton
- Incoming states: neutrino and antineutrino
- Quadrature: 8 outgoing-angle nodes, 48 outgoing-energy nodes,
  36 initial-nucleon momentum nodes, 12 azimuth nodes
- Exact outgoing-energy support scan: 10001 points
- Opacity convention: `kappa_N = xi_SPP * Gamma_N_available`; `xi_SPP`
  is applied exactly once.
- Optical depth: fixed-local-energy, flat-space radial integral to 15.2 km.

## Independent checks

1. The 16 local anchor integrals were recomputed with the original,
   unmodified C4-B2/C4-C1/C4-C2 implementation.
2. The full 301-point run recomputed all 1204 local cases. A Numba
   implementation of the innermost Dirac-matrix contraction was used only
   as a numerically equivalent acceleration. Representative phase-space
   contractions and all 16 original-kernel anchors were cross-checked.
3. The 16 original-kernel anchor integrals agree with the accelerated
   full-run values to relative `2.22e-16`.
4. All 1204 local rates agree with the archived 1204-case table to maximum
   relative difference `5.55e-16`.
5. All 16 anchor integrals agree with the C4-C2 reference to maximum relative
   difference `5.55e-16`.
6. Reconstructed radial optical depths agree with the archived C4-C3
   radial table to maximum absolute difference `5.46e-12`.
7. Both 0.10 km and 0.25 km radial-grid diagnostics pass the 1% criterion.

## Main files

- `local_independent_radial_rates_301x4.csv`: all 1204 locally recomputed
  integrated-rate cases.
- `radial_opacity_tau_0p05km.csv`: local opacity and radial optical depths.
- `radial_tau_grid_convergence.csv`: 0.10 km and 0.25 km comparisons.
- `local_anchor16_vs_c4c2.csv`: original-kernel anchor re-computation.
- `local_independent_c4c2_anchor16.csv`: independent C4-C2 anchor values.
- `local_vs_archived_1204_comparison.csv`: row-by-row local/archived comparison.
- `radial_species_asymmetry.csv`: radial neutron/proton and nu/antinu ratios.
- `rates_checkpoint.jsonl`: per-radius resume/checkpoint records.
- `summary.json` and `local_recompute_status.json`: machine-readable acceptance.
- `run_local_c4c3_full301_numba.py`: local calculation driver.
- `SOURCE_PROVENANCE.md`: source snapshot and Git blob verification.
- `ARCHIVE_PROVENANCE.txt`: original uploaded archive digest and extraction note.
- `SHA256SUMS.txt`: checksums for every file in this directory, excluding the
  checksum manifest itself.

The C4-B2, C4-C1, C4-C2 source scripts and the EOS profile/occupation inputs
are already present in the parent PR tree. Their exact Git blob SHAs are
recorded in `SOURCE_PROVENANCE.md`; they are not duplicated into a nested
snapshot directory.

## Scope limitation

This is a fixed-local-energy, flat-space radial scattering optical-depth
diagnostic. It is not a redshifted transport optical depth, a full escape
probability, or a transport solution. Total scattering, angular transport,
and energy-transfer moments remain separate.

## Separating composition from per-target response

Because the common filling factor cancels,
`kappa_n/kappa_p = (nprime_n/nprime_p) * (sigma_n/sigma_p)`.
At the four anchor radii:

| r (km) | nprime_n/nprime_p | sigma_n/sigma_p (nu) | kappa_n/kappa_p (nu) | sigma_n/sigma_p (antinu) |
|---:|---:|---:|---:|---:|
| 0.20 | 3.6027 | 0.6054 | 2.1812 | 0.5720 |
| 5.00 | 3.6436 | 0.6963 | 2.5370 | 0.6467 |
| 10.00 | 5.2832 | 0.9714 | 5.1319 | 0.9003 |
| 15.20 | 25.1766 | 0.9875 | 24.8619 | 0.9337 |

In the inner region the per-target proton response is larger, partially
compensating for neutron-rich composition. Toward the outer region the
per-target responses approach one another, so the opacity ratio approaches
the available neutron/proton density ratio.
