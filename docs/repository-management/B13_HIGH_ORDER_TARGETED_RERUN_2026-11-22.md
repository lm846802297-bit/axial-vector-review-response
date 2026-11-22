# B.13 targeted high-order rerun — 2026-11-22

The local primary calculation completed with exit status 0: 431 unique ((r,x)) points, 2,155 ordered quadrature evaluations, four workers and 343.5815 s runtime. All targeted quadrature, radial midpoint interpolation, energy PCHIP, detailed-balance, mass-shell and finite/non-negative rate checks passed. The native local raw JSON, summary and independent validation report are archived in the branch. GitHub Actions run #45041173008 independently recomputed the same 431 task keys and matched all 10,344 charge/mode rate components exactly; its calculation and validation passed. The first artifact archive step failed only because CI_RUN.log is ignored by .gitignore, and the workflow now uses an explicit force-add.

Exact source driver, target input, profile and imported dependencies were verified against the Git blob identities at PR #121 head `e49908762e90271f4bc84be75e19577431febd4c`. See the [run report](../../research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_RERUN_2026-11-22/README.md) and its provenance JSON.

The calculation is a targeted high-order audit, not full 1687-node global acceptance. No production rate, opacity, transport output or axial-vector constraint is changed.
