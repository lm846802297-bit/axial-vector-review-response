# Coherent two-pole integration-window audit — 2026-11-14

## Finding and disposition

The archived [calculation script](coherent_two_pole_spectral_area.py) initializes quadrature breakpoints with `{lo, hi, MH, ms}` and then integrates between every adjacent pair after sorting. When `ms=100` or `150` GeV, this extends the integral to 100–126 or 124.5–150 GeV, respectively, although the [calculation note](COHERENT_TWO_POLE_SPECTRAL_AREA_2026-11-10.md) states a 124.5–126.0 GeV window. At `ms=125.25` GeV the extra point is inside the window.

The historical script and output are retained unchanged. The note now labels their integration-window mismatch and defines the implementation's propagator parameters. No experimental or physical conclusion is revised on the basis of this check.

## Comparison

The [audit script](spectral_window_audit_2026-11-14.py) uses the same imported propagator and widths and the same quadrature settings, but includes internal breakpoints only if they lie strictly within the stated window. The [CSV output](spectral_window_audit_2026-11-14.csv) records all six pairs.

| Benchmark | ms (GeV) | Archived | Restricted window | Difference |
|---|---:|---:|---:|---:|
| A | 100 | 1.000030466318 | 1.000030492611 | +2.6292e-8 |
| A | 125.25 | 0.999339661592 | 0.999339661592 | -2.2e-16 |
| A | 150 | 0.999967184825 | 0.999967157969 | -2.6856e-8 |
| B | 100 | 1.000001635123 | 1.000001636534 | +1.4106e-9 |
| B | 125.25 | 0.987765074066 | 0.987765074066 | 0 |
| B | 150 | 0.999998628205 | 0.999998627084 | -1.1210e-9 |

## Reproduction and boundaries

- Input snapshot: commit `5564c1a2b33b012f1105ec7ea4b55e91c3cd57f7`; archived script Git blob `7a7780c9c5144527af8bc606a0da7a962a5f1793`.
- Run from this directory: `python spectral_window_audit_2026-11-14.py > spectral_window_audit_2026-11-14.csv`.
- Environment for this run: Python 3.12.14, SciPy 1.17.0.
- The original script was also executed and passed its six existing tolerance checks. Those checks compare ratios to stored constants with tolerance 2e-6; they do not detect the window discrepancy.
- This is a same-kernel numerical comparison, not an independent physics derivation, convergence study, detector simulation, signal-strength fit or exclusion. The selected propagator and fixed-width approximation remain conditional.
