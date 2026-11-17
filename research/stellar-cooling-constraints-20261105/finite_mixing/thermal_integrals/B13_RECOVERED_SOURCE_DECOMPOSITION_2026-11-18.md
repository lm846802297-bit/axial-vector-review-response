# Recovered B.13 source decomposition: JSON re-audit

**Date:** 2026-11-18  
**Benchmark:** pure-vector B.13 moving-muon semi-Compton, (m_{A'}=10) MeV, rates per (g_X^2).  
**PR:** #121, branch `research/b16-energy-grid-diagnostic-20261117`.

## Correction and provenance

The historical GitHub Actions artifact was downloaded and inspected directly:

- Run: `43376779901`
- Artifact: `14015517843`
- ZIP SHA-256: `2c2e2ef8610abfa16bc9e423937f974061ece101911fb9c6503e65901bb55715`
- ZIP contains one JSON file, not a CSV: `p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json`
- Extracted JSON SHA-256: `14c4405f9421aca517ff00310232ad9aead4c0cdd61868e2788125875cb84dc0`
- 513 grid nodes; 468 direct radial-energy cell midpoints; 19 radial nodes and 27 local-energy nodes.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

The previous version of the post-processing script expected CSV columns that are not present in this artifact. Its recorded `csv_rows=5886` and lapse-weighted total (1.8066\times10^7) were not supported by the archived input and are superseded here. The old flat-measure fractions did reproduce the direct-midpoint values, but that measure was not the Eq. (B.1) source measure.

## Definition and integration measures

The archive's per-charge, per-polarization spectral source is

[
\mathcal S_{h,Q}(r,\omega)
=\frac{\omega^2\sqrt{\omega^2-m_{A'}^2}}{2\pi^2}
\,\Gamma_{\mathrm{prod},h,Q}^{\mathrm{B.13}}(r,\omega),
]

with (h\in\{L,+,-\}), (Q\in\{\mu^-,\mu^+\}). The source rates are normalized per (g_X^2).

Four measures were recomputed from the 468 archived direct cell-midpoint evaluations:

1. **Historical flat local-source proxy**
   [
   4\pi r^2\,\Delta r\,\Delta\omega\;\mathcal S.
   ]
   This reproduces the earlier local-source fractions, but omits the lapse-squared factor and escape-energy lower bound.

2. **B.1 geometric/lapse midpoint measure, no threshold**
   [
   4\pi r^2 N(r)^2\,\Delta r\,\Delta\omega\;\mathcal S.
   ]

3. **B.1 midpoint threshold**
   Use the same measure, retaining a cell only if its midpoint obeys
   (\omega_{\rm loc}\ge m_{A'}/N(r)).

4. **B.1 fractional-cell threshold (primary diagnostic)**
   Clip the energy-cell width at the local escape threshold:
   [
   \Delta\omega_{\rm allowed}
   =\max\!\left[0,\omega_{i+1}-
   \max\!\left(\omega_i,\frac{m_{A'}}{N(r)}\right)\right].
   ]
   The direct midpoint source is treated as constant over the retained part of that cell.

The local threshold is the condition (E_\infty=N\omega_{\rm loc}\ge m_{A'}). The fractional-cell method is a controlled post-processing diagnostic, not the production B.1 implementation: it does not replace the radial Gauss rule or the piecewise-linear energy weights in `blinov_reproduction/reference.py`. The totals below retain (4\pi), but omit the common km-to-MeV(^{-1}) and MeV(^{2}\)-to-erg/s conversions; use the fractions for comparisons, not as luminosities.

## Numerical results

| Measure | Integral (internal units) | (8\text{–}12) km fraction |
|---|---:|---:|
| Flat local, no lapse/threshold | (2.2480885750\times10^7) | 81.8066% |
| (N^2), no threshold | (1.4523881669\times10^7) | 82.5530% |
| (N^2), midpoint threshold | (1.4512907671\times10^7) | 82.5643% |
| (N^2), fractional threshold | (1.4511885868\times10^7) | 82.5585% |

For the primary fractional-threshold measure:

| Contribution | Fraction |
|---|---:|
| (mu^-) | 99.3354% |
| (mu^+) | 0.6646% |
| Longitudinal (L) | 1.6120% |
| Transverse (+) | 49.1940% |
| Transverse (-) | 49.1940% |
| 8–10 km | 54.1306% |
| 10–12 km | 28.4279% |
| 8–12 km combined | **82.5585%** |

The transverse (+) and (-) source fractions agree to a maximum relative difference of (5.22\times10^{-16}), as expected from the archived isotropic, parity-symmetric pure-vector setup. This equality is a local-source result, not a claim that their optical depths or escaped luminosities must be identical in every transport implementation.

## Threshold and numerical checks

- Lapse range over the direct midpoint cells: (N=0.73796\text{–}0.91458).
- Corresponding local escape threshold: (m_{A'}/N=10.934\text{–}13.551) MeV.
- Applying the (N^2) factor reduces the unthresholded flat-measure total by the factor 0.646055.
- The local escape threshold retains 99.9174% of the lapse-weighted source integral. This small correction is consistent with the (k_{A'}\to0) suppression of the spectral source near threshold.
- Midpoint-cut and fractional-cell-cut totals differ by only (7.04\times10^{-5}) relative.
- Charge-sum closure residual: (2.26\times10^{-16}).
- Maximum transverse (+/-) source difference: (5.22\times10^{-16}).

## Interpretation boundary

The robust result is that the **local B.13 semi-Compton source is concentrated at 8–12 km**, contributing about 82.6% under the B.1-motivated source measure. This supports prioritizing source quadrature refinement in that shell.

It does **not** imply that the B.2 opacity is concentrated there. Photons/vectors emitted in this shell propagate through outer layers; those layers must remain in the ray optical-depth integral even if their local source is negligible.

This calculation also does not include neutrino inverse decay, dimuon production, angular ray averaging, B.2 attenuation, or full GR ray transport. Therefore:

- do not identify these fractions with the complete B.1 thin-source luminosity;
- do not identify them with the B.2 escaped-luminosity fractions;
- do not infer a polarization factor to rescale Fig. 7;
- do not update SN1987A or axial-vector limits.

The original P1-B archive still has `overall_p1b_pass=false`, `interpolation_pass=false`, and `quadrature_pass=false`. This re-audit does not change those gates.

## Reproduction

Extract the Actions artifact JSON, then run:

```bash
python audit_b13_recovered_source_decomposition.py \
  --archive-json p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json \
  --output b13_recovered_source_decomposition_2026-11-18.json
```

The script validates the profile hash, grid dimensions, direct midpoint coordinates, final quadrature order, polarization ordering, and charge-sum closure before writing the output JSON.


## Independent rerun check (2026-11-18)

The committed script was executed again against the extracted historical JSON archive. It reproduced all four integral totals, all four 8--12 km fractions, the profile and archive hashes, the 513-node/468-midpoint counts, and the closure diagnostics exactly to the stored double-precision values. The rerun output JSON was compared field by field with the committed machine-readable result; no numerical differences were found.
