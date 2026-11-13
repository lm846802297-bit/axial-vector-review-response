# P1-B Global Pilot 01 — sparse full-domain scouting calculation

**Status: pilot completed; global P1-B acceptance remains OPEN.**

## Fixed physics and input

- Process: exact-recoil moving-muon semi-Compton B.13, muon + photon ↔ muon + A′.
- Mediator mass: 10 MeV; pure-vector endpoint (g_V/g_X=1, g_A/g_X=0).
- Modes: L,+,-; target charges: μ− and μ+.
- Background: reconstructed SFHo-18.8 at t_pb=1 s, 1687-row digitized profile.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Local energy coordinate: (x=(\omega-m_{A'})/T(r)), sampled at [0.5, 2, 6, 18, 36].
- Radii (km): [0, 8.4821412022467, 12.5, 20.33, 21, 21.6346875, 22.1918941570485, 24.5].
- Quadrature orders: (16,10,10,10).

## Results

- Direct B.13 points: 40.
- Runtime: 22.717 s.
- All rates finite and nonnegative: true.
- Maximum detailed-balance residual: (5.994724\times10^{-15}).
- Maximum final-muon mass-shell residual: (3.796455\times10^{-13}).
- Maximum local energy reached: 1422.988456291 MeV.
- Profile maximum temperature: 39.249679341 MeV.

The maximum energy covers the full-profile cutoff (10+36T_{\max}=1422.9884563) MeV.

## Interpretation boundary

This 8-radius × 5-thermal-energy grid is a coarse scouting calculation. It is **not** a converged global radial-energy kernel table, not a global interpolation acceptance, not a full-star GR emissivity, not an optical-depth integration, and not a luminosity or SN1987A constraint. It seeds the next adaptive mesh.

## Reproduction

Install numpy, scipy and threadpoolctl, then run the committed driver from the source snapshot root:

```bash
python run_global_pilot_01.py --output results/P1B_10MeV_GLOBAL_PILOT_01.json --csv results/P1B_10MeV_GLOBAL_PILOT_01.csv
```

## Checksums

- Driver SHA-256: `b7810974e829614ced29a8f49b39880df0e3f279a87637f8c25f26adf3d26740`
- JSON SHA-256: `6993051408f08cdf70afc797fe0439a56773137d857240e30b981d489ea4f7ee`
- CSV SHA-256: `909243758ef84a9322e8df0197f607545cb62236f11814c7a5b89338da81bc0a`
