# C4-C4-A energy-dependence anchor scan

- Trigger/source commit: `7f76e9d58f6af5af36694580d5768bc3f9858feb`
- Numerical-integrity status: PASS
- Physical transport/reproduction status: NOT CLAIMED
- Energies: 10, 20, 40, 60, 100, 150 MeV
- Anchor radii: 0.2, 5.0, 10.0, 15.2 km
- Channels: neutron/proton × neutrino/antineutrino
- Cases: 96 total; 80 newly computed and 16 reused at 100 MeV from C4-C2.

The local rate is
`Gamma_N^avail = 2 pi integral dcos(theta) integral dEprime dGamma/(dEprime dOmega')`,
with the exact outgoing-energy support recalculated for every incident energy and angle. The same EOS effective masses, chemical potentials, Fermi occupations, final-state Pauli blocking, and weak form factors as C4-B2/C1/C2 are retained.

The total-volume scattering coefficient is `kappa_N = xi_SPP Gamma_N^avail`; `xi_SPP` is applied once. The mean free path is `lambda_N = 1/kappa_N`.

The six-point energy grid is an exploratory first-pass choice, not a final physical boundary or a user-approved exclusion range. This stage uses fixed local incident energy and flat-space local rates. It does not calculate a radial optical depth, transport solution, escape probability, or SN1987A constraint.

## Provenance

- C1 profile SHA-256: `97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59`
- C2 occupation Git blob SHA: `c472040a4551e68ffadbf7addf9402663f99e7e3`
- C4-C2 100-MeV reference Git blob SHA: `881b6459e8d9a1ac867b0f4dc47ac168d454e488`
- C4-B2/C1/C2 source blob SHAs are recorded in `summary.json`.

See `summary.json` for exact quadrature orders, all acceptance checks, and input provenance.
