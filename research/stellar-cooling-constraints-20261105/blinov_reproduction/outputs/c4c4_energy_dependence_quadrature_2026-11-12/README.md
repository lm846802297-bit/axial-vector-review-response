# C4-C4-Aq combined quadrature-convergence audit

- Source commit: `7cc76155ce73e6e1380f041fa71e6ea5e171165e`
- Cases: 80 (five new energies × four radii × two targets × two signs)
- Base orders: cosine 8, outgoing energy 48, initial momentum 36, azimuth 12
- High orders: cosine 12, outgoing energy 72, initial momentum 48, azimuth 16
- Relative-difference threshold: 1.0%
- Numerical-integrity checks: PASS
- Combined quadrature convergence: PASS

All 80 high-order calculations are compared with the exact matching row in the byte-pinned C4-C4-A base archive. The high-order calculation increases all four quadrature orders simultaneously; it does not isolate individual sources of numerical error. If the 1% threshold is exceeded, the diagnostic rows remain archived and the quadrature dimensions must be separated in the next study.

This is a local-rate numerical convergence check, not physical transport or literature-reproduction acceptance.
