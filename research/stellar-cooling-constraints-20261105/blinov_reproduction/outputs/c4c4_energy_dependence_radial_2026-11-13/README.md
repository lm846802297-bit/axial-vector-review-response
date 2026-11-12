# C4-C4-B full-radial energy-dependence archive

- Source commit: 42d7c425d34138679c8ce555d671e56927fc9179
- Energies: 10, 20, 40, 60, 100, 150 MeV
- Radial grid: 301 points, 0.20–15.20 km, 0.05 km spacing
- Local rate rows: 7224 (6020 new + 1204 reused from C4-C3 at 100 MeV)
- Stratified high-order cases: 340
- Numerical-integrity status: PASS
- Combined quadrature convergence: PASS
- Radial-grid convergence: PASS
- Maximum C4-C4-A anchor difference: 3.330669e-16

The 100-MeV baseline is reused without recomputation from the byte-pinned C4-C3 301-radius archive. Five new energy slices are computed with the EOS moving-nucleon C4-B2/C4-C1/C4-C2 kernel. The filling factor xi_SPP is applied once in kappa_N = xi_SPP * Gamma_N_available.

The optical depth is a flat-space, fixed-local-energy radial integral. It is not a redshifted transport solution, escape probability, or SN1987A exclusion. The high-order quadrature comparison is stratified at 17 radial points per new energy, not evaluated at every radial point.
