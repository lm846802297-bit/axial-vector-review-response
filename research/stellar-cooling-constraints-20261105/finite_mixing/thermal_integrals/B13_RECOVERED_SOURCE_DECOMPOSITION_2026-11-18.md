# Recovered B.13 direct-midpoint source decomposition

Date: 2026-11-18  
Execution: local post-processing of the recovered historical CSV; no Actions compute was invoked.

## Provenance and scope

- Historical source run: `43376779901`.
- Original artifact: `14015517843`.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Input coverage: 513 grid nodes, 468 direct cell midpoints, 5,886 CSV rows.
- Process: B.13 `muon + photon <-> muon + A'` semi-Compton only.

The direct midpoint source was integrated using the cell measure
`4*pi*r^2*Delta_r*Delta_omega`, where each midpoint cell width is reconstructed from its bracketing grid-node coordinates. This reproduces the previously archived source-weighted total to numerical precision:
`2.2480885750463076e7` in the archive's internal units. The lapse-weighted diagnostic is `1.806583976373589e7`.

This is not a B.2 luminosity: it excludes neutrino inverse decay, ray geometry, path attenuation, and the complete GR transport measure.

## Charge and polarization decomposition

| Component | Fraction of direct local B.13 source |
|---|---:|
| mu_minus | 99.3181% |
| mu_plus | 0.6819% |
| L | 1.6243% |
| + | 49.1879% |
| - | 49.1879% |

The transverse modes are degenerate in the archived setup, so their source fractions agree. The longitudinal fraction is a source fraction only; it must not be carried over as an escaped-luminosity fraction because each mode has its own attenuation in a no-mixing transport calculation.

## Radial decomposition

| Shell | Fraction |
|---|---:|
| 0–2 km | 0.00312% |
| 2–4 km | 0.09634% |
| 4–6 km | 1.26279% |
| 6–8 km | 14.82210% |
| 8–10 km | 54.64495% |
| 10–12 km | 27.16166% |
| 12–14 km | 1.84919% |
| 14–16 km | 0.15986% |
| 16–18 km | negligible |
| 18–24 km | negligible |

The 8–12 km region contributes 81.8066% of this local B.13 source integral. Thus subsequent source-grid convergence should prioritize 8–12 km, while the opacity/path grid must still retain the outer absorber shells: a small local source outside the production shell does not imply a negligible optical-depth contribution along rays.

## Consequences for the next B.2 calculation

1. Preserve all six charge/mode channels at the local-kernel interface.
2. It is reasonable to test combining (+) and (-) only after verifying that the ray and polarization-basis implementation preserves the transverse symmetry.
3. Do not approximate (L) by either transverse mode.
4. Report source-weighted and escaped-luminosity-weighted mode fractions separately.
5. Keep the literal scalar B.2 equation-reproduction lane, the no-mixing mode-resolved lane, and equal-occupation average-opacity lane distinct.
6. Add neutrino inverse decay as a separate channel before constructing total B.2 opacity.

The historical local archive's quadrature and interpolation acceptance flags remain failed. This decomposition does not change those flags, does not validate the PCHIP table, and does not update Fig. 7, SN1987A, or any axial-vector exclusion curve.

## Reproduction

Run:

```bash
python audit_b13_recovered_source_decomposition.py \
  --csv results/P1B_10MeV_LOCAL_KERNEL_ARCHIVE_2026-11-17/p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.csv \
  --output outputs/b13_recovered_source_decomposition_2026-11-18.json
```

Machine-readable result: `outputs/b13_recovered_source_decomposition_2026-11-18.json`.
