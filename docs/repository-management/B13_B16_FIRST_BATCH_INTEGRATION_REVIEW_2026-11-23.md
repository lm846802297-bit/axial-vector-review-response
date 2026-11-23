# B.13 / B.16 first-batch integration review — 2026-11-23

## Integration basis

This integration combines the B.16 phase-space and energy-grid evidence from PR #121, the strict output validator and regression tests from PR #134, and the B.13 targeted high-order provenance package from PR #133. The current main tree is the first parent of the integration commit; source branch histories are retained as additional parents.

## B.16 acceptance

- Original archived energy-grid SHA-256 is retained: 036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3.
- Immutable 842-node reference file is retained, with file SHA-256 3a99a994d9cab96fd194cf540d75ef698f871354839c8f55f05eeaa11f02d957.
- Cross-runner node comparison accepts the observed one-ULP difference: maximum absolute difference 5.684341886080802e-14 MeV and maximum relative difference 1.1675488289093305e-16.
- Strict phase-space run #45172485856 passed calculation, sparse joint-table validation, regression tests, and archive write-back.
- Energy-grid diagnostic #45171900209 passed.

The B.16 luminosity closure residual is -2.220446049250313e-16; the optically thin luminosity residual is zero; the escape-probability residual is -5.421010862427522e-20. The Fig. 7 10 MeV luminosity discrepancy remains +92.4284%. No opacity rescaling or axial-vector constraint update is authorized.

## B.13 targeted high-order acceptance

Independent reproduction #45172924204 passed 431/431 frozen target points and archived the native result and independent validation package.

- Maximum radial midpoint interpolation error: 8.311070322862653e-4.
- Maximum energy PCHIP interpolation error: 6.716564877619043e-4.
- Maximum final successive-order change: 3.29220848525901e-4.
- Maximum detailed-balance residual: 5.027846521385086e-15.
- Maximum mass-shell residual: 2.0432421890821873e-13.

This is targeted high-order acceptance, not exhaustive high-order convergence over all 1687 radii.

## Software and provenance checks

- B.16 strict validator: numeric schema, finite-value checks, source/opacity identity, immutable energy-node reference, baseline closure, and sparse joint-to-marginal checks.
- B.16 regression suite: sparse zero-bin handling and hard failure for missing non-zero bins or unexpected labels.
- B.13 provenance: exact source commit, input hashes, local/CI environment records, output hashes, target coverage, and independent result validation.
- Calculation jobs remain read-only; result archival is isolated in separately permissioned jobs.
- Production axial-vector rates, transport outputs, and constraint figures remain unchanged.

## Remaining physical work

1. The +92.4284% Fig. 7 10 MeV strong-absorption discrepancy remains open.
2. B.13 full 1687-radius high-order convergence and global polarization-resolved B.2 transport are not accepted by this targeted run.
3. Repository-wide document inventory and workflow register reconciliation are tracked separately from the numerical acceptance above.
