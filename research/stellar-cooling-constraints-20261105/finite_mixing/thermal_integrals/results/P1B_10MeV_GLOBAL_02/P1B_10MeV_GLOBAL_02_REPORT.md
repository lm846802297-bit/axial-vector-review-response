# P1-B Global 02 — full radial-knot scan and selected 2D midpoint audit

**Status:** G1 full radial-knot scan complete; G2 selected-subset midpoint audit complete; global interpolation/quadrature acceptance remains OPEN.

## Fixed setup
- Process: exact-recoil moving-muon semi-Compton B.13, muon + photon <-> muon + A'.
- Mediator mass: 10 MeV; pure-vector benchmark gV/gX=1, gA/gX=0.
- Background: SFHo-18.8, t_pb=1 s, 1687-row digitized profile.
- Profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.
- Thermal coordinate: x=(omega_local-m_A')/T(r).
- G1 thermal nodes: [0.5, 2, 6, 18, 36].
- G1 quadrature: (10,6,6,6).

## G1 — complete original radial-knot coverage
- Radial knots: 1687/1687.
- Direct B.13 evaluations: 8435.
- Independently checkpointed chunks: 36.
- All rates finite and nonnegative: true.
- Maximum detailed-balance residual: 1.0934050042089811e-14.
- Maximum final-muon mass-shell residual: 6.214454313524293e-13.
- Maximum sampled local energy: 1422.9884562908824 MeV.

These are pointwise microphysical closure checks at scouting quadrature order. They do not establish quadrature convergence.

## G2 — selected worst-interval midpoint audit
The 60 intervals with the largest adjacent-knot variation were selected. Direct radial-midpoint calculations were performed at the five original x nodes and additional energy midpoints.
- Direct selected midpoint evaluations: 1140.
- At fixed original x nodes, maximum radial-midpoint discrepancy against log-linear endpoint interpolation: below 0.09%.
- After refining the energy grid to 11 knots and using PCHIP in log-rate, the worst checked energy-midpoint discrepancy is 1.0720%, slightly above the 1% target. It occurs near r=14.55–14.60 km, x=10.3923, in the mu+ production longitudinal component.

## Targeted quadrature cross-checks
Five representative points were compared between (10,6,6,6) and (14,8,8,8). At the hot-shell point r=8.4821412 km, omega=417.895 MeV, the worst inspected rate changes by 1.4371%. This fails the 0.1% criterion and requires higher-order local quadrature. Other inspected points are below 0.1%.

## Required next steps
1. Extend direct midpoint checks from the selected 60 intervals to all 1686 radial intervals, with adaptive energy refinement.
2. Refine x<1 and x≈10–12 regions; these remain the current worst selected energy-interpolation regions.
3. Raise quadrature orders at hot-shell/high-energy points until successive changes are below 1e-3 for every charge and polarization component.
4. Only after global interpolation and quadrature acceptance, construct the full kernel table and perform volume-weighted emissivity and GR optical-depth integration.

**No global emissivity, GR optical depth, luminosity, or SN1987A constraint is claimed by this run.**
