# B.13 local-kernel and B.2 angular/path convergence — 2026-11-18

All calculations in this report were run locally; no GitHub Actions job was used.

## Profile and provenance

- Profile: reconstructed 1687-row SFHo-18.8 public-figure profile; not raw Garching simulation output.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- The global B.2 local-rate NPZ used below was `B13_MODE_RESOLVED_B2_10MEV_ALLRADII_LOCAL_2026-11-18.npz`, with B.13 kernel order `(8,4,4,4)`.

## 1. Refined B.13 local-kernel sample

144 selected radial-energy points were recomputed at orders `(16,10,20,10)`, `(20,12,24,12)`, and `(24,14,28,14)`.

| Check | Result |
|---|---:|
| Sample points | 144 |
| Maximum final successive-order change | `9.8553242e-5` |
| Maximum detailed-balance residual | `2.5584554e-14` |
| Maximum final-muon mass-shell residual | `3.7964548e-13` |
| All rates finite and nonnegative | yes |
| All points below (10^{-3}) | yes |

Worst point: (r=8.6600189564) km, (omega=10.8733512165) MeV.

This is a targeted local-kernel check. It is not a full high-order recomputation of all (44\times78) B.2 grid points.

## 2. B.2 angular/path quadrature

The existing all-radii local-rate table was propagated with ((N_\theta,N_s)=(16,32),(24,48),(32,64)). The B.13 local rate table itself remains at exploratory order ((8,4,4,4)); therefore this section isolates angular/path convergence conditional on that table.

Maximum relative changes over all 25 coupling points:

| Charge convention | Lane | (16,32) → (24,48) | (24,48) → (32,64) |
|---|---|---:|---:|
| (mu^-) | mode-summed scalar | (8.74\times10^{-6}) | (3.43\times10^{-6}) |
| (mu^-) | equal occupation | (4.50\times10^{-6}) | (3.38\times10^{-6}) |
| (mu^-) | independent mode | (4.55\times10^{-6}) | (3.34\times10^{-6}) |
| (mu^-+\mu^+) | mode-summed scalar | (8.73\times10^{-6}) | (3.34\times10^{-6}) |
| (mu^-+\mu^+) | equal occupation | (4.54\times10^{-6}) | (3.28\times10^{-6}) |
| (mu^-+\mu^+) | independent mode | (4.61\times10^{-6}) | (3.23\times10^{-6}) |

The literal B.16 scalar baseline is recovered exactly at ((16,32)). At ((32,64)), its maximum difference from the archived curve is (3.36\times10^{-5}).

### Strong-coupling endpoint, both muon charges

At (g_X=4.1716896502\times10^{-8}):

| Lane | Luminosity [erg s(^{-1})] |
|---|---:|
| B.16 literal scalar baseline | (2.43734\times10^{52}) |
| B.13 mode-summed scalar | (2.93538\times10^{52}) |
| Equal occupation | (1.78744\times10^{54}) |
| Independent mode | (1.78811\times10^{54}) |
| Fig. 7 digitized reference | (1.26781\times10^{52}) |

Equal-occupation and independent-mode lanes differ by about (3.74\times10^{-4}) at the strong endpoint. The very large separation from the mode-summed scalar lane is a state-counting/transport-convention issue, not a validated revision of the SN bound.

## 3. Interpretation and remaining gates

1. B.2 angular/path quadrature is numerically stable for the archived local-rate table.
2. Full-grid high-order B.13 local-kernel convergence is not established: the global table still uses ((8,4,4,4)).
3. The 144-point high-order sample cannot substitute for a complete (44\times78) high-order local-rate evaluation.
4. Radial/source-energy convergence and the polarization-resolved kinetic/state-counting derivation remain open.
5. The Fig. 7 discrepancy remains unresolved. No opacity, source, coupling, or normalization rescaling was applied.
6. No SN1987A or axial-vector constraint is updated.

## Next P0 task

Recompute the complete active B.13 table on the 44 opacity radii × 78 active energies at a converged local-kernel order, or build a validated adaptive correction checked against direct high-order points. Only then repeat the global B.1/B.2 transport comparison.
