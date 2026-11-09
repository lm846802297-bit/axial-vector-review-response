# B.2 radial opacity-interpolation convergence audit

## Scope

The B.1 source radial quadrature is fixed at order 40. The energy, angular, and path quadratures are also fixed. Only the radial grid used to tabulate and interpolate local absorption rates along the B.2 chord is refined.

The fixed-omega prescription follows the printed Eq. (B.2). The redshifted variant uses conserved energy at infinity, $E_\infty=N(r)\omega_{\rm source}$ and $\omega_{\rm local}(s)=E_\infty/N(r'(s))$, while retaining the same Euclidean chord. It is a sensitivity diagnostic, not full GR ray tracing.

## Results

| $m_V$ (MeV) | opacity grid | max fixed-$\omega$ luminosity change | max redshifted luminosity change | max redshift-effect change |
|---:|---:|---:|---:|---:|
| 0.1 | 40 → 80 | 32.3957% | 31.9812% | 0.7481 pp |
| 0.1 | 80 → 120 | 3.3104% | 3.2774% | 0.0768 pp |
| 0.1 | 120 → 160 | 1.4780% | 1.4410% | 0.0343 pp |
| 0.1 | 160 → 240 | 1.7427% | 1.7012% | 0.0383 pp |
| 0.1 | 240 → 320 | 0.4355% | 0.4308% | 0.0099 pp |
| 1 | 40 → 80 | 7.6090% | 7.4456% | 0.1345 pp |
| 1 | 80 → 120 | 0.7648% | 0.7502% | 0.0128 pp |
| 1 | 120 → 160 | 0.5426% | 0.5321% | 0.0092 pp |
| 1 | 160 → 240 | 0.4039% | 0.3960% | 0.0069 pp |
| 1 | 240 → 320 | 0.1015% | 0.0996% | 0.0017 pp |
| 10 | 40 → 80 | 0.1304% | 0.1249% | 0.0090 pp |
| 10 | 80 → 120 | 0.0196% | 0.0194% | 0.0006 pp |
| 10 | 120 → 160 | 0.0170% | 0.0163% | 0.0005 pp |
| 10 | 160 → 240 | 0.0025% | 0.0027% | 0.0003 pp |
| 10 | 240 → 320 | 0.0036% | 0.0033% | 0.0002 pp |

## Interpretation

The source quadrature and energy grid are held fixed, so luminosity changes across this scan isolate the radial tabulation/interpolation of the B.2 absorption kernel. The numerical thresholds are project diagnostics, not physical uncertainty bounds.

Machine-readable output: outputs/b2_opacity_interpolation_convergence_2026-11-09.json
Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c
