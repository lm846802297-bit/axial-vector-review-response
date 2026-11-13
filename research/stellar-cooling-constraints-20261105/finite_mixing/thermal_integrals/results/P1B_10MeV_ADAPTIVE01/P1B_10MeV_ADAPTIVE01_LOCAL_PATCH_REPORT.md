# P1-B ADAPTIVE-01 — targeted local 2D refinement result

**Status: local patch passes its stated midpoint interpolation criterion; global P1-B acceptance remains OPEN.**

## Fixed physics and input

- (m_{A'}=10\,\mathrm{MeV}), pure-vector endpoint (g_V/g_X=1,;g_A/g_X=0).
- Exact-recoil moving-muon semi-Compton B.13 kernel.
- Three vector modes (L,+,-); both (mu^-) and (mu^+) targets.
- Reconstructed SFHo-18.8, (t_{pb}=1\,\mathrm{s}), 1687-row profile.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

## Local 2D interpolation patch

- Radial domain: 20.33–22.00 km; 22 radial nodes.
- Energy domain: 720–1074.271329 MeV; 4 nodes in (y=\sqrt{\omega-m_{A'}}).
- 88 direct grid nodes plus 63 direct cell-midpoint checks; 151 unique direct points.
- Interpolant: sequential tensor PCHIP in radius and (y), applied to (log \Gamma_{abs}); production and reduced absorption reconstructed from exact local detailed balance.

| Interpolation order | Maximum direct-midpoint relative error | Result |
|---|---:|---|
| radius then energy | 0.5883848% | PASS |
| energy then radius | 0.5883848% | PASS |

Worst cell: (r=21.6346875\,\mathrm{km}), (omega=801.8687065\,\mathrm{MeV}). The worst channel is (mu^+) absorption (0.5884%).

Maximum detailed-balance residual over direct midpoints: (4.97\times10^{-14}). Maximum final-muon mass-shell residual: (1.30\times10^{-13}).

## Targeted quadrature follow-up

The 12 worst direct cell midpoints were independently recalculated at order ((32,18,18,18)) and compared with the stored order-((28,16,16,16)) values. All 12 pass the 0.1% successive-order criterion. The maximum change is (9.3747\times10^{-5}) (0.009375%). The maximum detailed-balance residual among these 12 new calculations is (2.18\times10^{-14}); the maximum mass-shell residual is (5.83\times10^{-14}).

This is a targeted 12-point quadrature check, not a full quadrature scan of all 151 direct points.

## Finite-patch weighted diagnostic

A midpoint-weighted diagnostic was computed over this patch using (4\pi r^2N^2\,dr\,d\omega\,\omega^2k/(2\pi^2)). For the charge-summed modes, the relative differences between interpolated and directly evaluated patch integrals are:

| Quantity | Longitudinal | Each transverse mode |
|---|---:|---:|
| Production | 0.03619% | 0.02537% |
| Absorption | 0.01738% | 0.004328% |

This is a finite-patch diagnostic only. It is **not** the full-star GR luminosity, an optical-depth integral, or a substitute for pointwise interpolation checks.

## Interpretation and remaining work

The local radial-energy patch now passes the 1% midpoint interpolation test, and the 12 worst interpolation midpoints pass the 0.1% targeted quadrature comparison. The profile input was not smoothed or modified. The narrow (mu_mu) support edge is retained as a separate explicit background feature.

Still outstanding:
1. Extend adaptive interpolation validation to the full radial and energy domain.
2. Complete pointwise quadrature convergence over all relevant nodes and cell midpoints, not just the targeted 12.
3. Recompute full-star volume-integrated emissivity and GR optical depths using the validated global kernel.
4. Only then proceed to global independent-polarization transport.

No axial-vector SN1987A limit is updated by this local patch.


## Additional targeted checks: hot shell and muon-support edge

### High-temperature shell, highest energy endpoint

At (r=8.4821412022467\,\mathrm{km}), (T=39.2496793414\,\mathrm{MeV}), and (\omega=1500\,\mathrm{MeV}), the order ladder was extended through ((36,20,20,20)). The final successive change is (9.43932\times10^{-4}), just below the (10^{-3}) pointwise criterion. Detailed balance and final-muon mass-shell residuals remain below (10^{-12}). This is one worst-point check, not global quadrature acceptance.

### Narrow muon chemical-potential support edge

The fixed digitized profile contains adjacent values:
- (r=22.1918936570485\,\mathrm{km}), (\mu_\mu=0.9999998342\,\mathrm{MeV});
- (r=22.1918946570485\,\mathrm{km}), (\mu_\mu=0\).

The transition width is (10^{-6}\,\mathrm{km}=10^{-3}\,\mathrm{m}). Five direct samples (including three interior points) at (\omega=20\,\mathrm{MeV}) were compared between quadrature orders ((20,12,12,12)) and ((28,16,16,16)). The maximum relative change is (7.14\times10^{-8}); detailed balance and mass-shell residuals are at the (10^{-15}) level. The original profile is retained without smoothing. The edge must remain explicitly represented in any future radial interpolation grid.

## Current P1-B status

The local patch passes the 1% midpoint interpolation criterion, and the selected 12 worst midpoints pass the 0.1% quadrature comparison. The hot-shell endpoint and the narrow muon-support edge also pass their respective targeted pointwise checks. **Global P1-B remains OPEN**: pointwise quadrature has not been checked at every one of the 151 patch points, the full radial-energy domain is not covered by this interpolation patch, and no full-star GR emissivity or optical-depth integration has been recomputed.
