# P1-B 10 MeV B.13 calculation source snapshot

This directory contains verbatim copies of the calculation program, exact-recoil moving-muon semi-Compton kernel, supporting rate/profile loader, regression test, and fixed SFHo-18.8 profile inputs used by the original Actions run.

- Original run: [#43376779901](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43376779901)
- Exact source commit: [`0f61bfc3e381402cbea9740958b9a2744f006040`](https://github.com/lm846802297-bit/axial-vector-review-response/commit/0f61bfc3e381402cbea9740958b9a2744f006040)
- Original numerical report: [P1B_10MeV_RUN_43376779901.md](../P1B_10MeV_RUN_43376779901.md)
- Machine-readable run manifest: [P1B_10MeV_RUN_43376779901_manifest.json](../P1B_10MeV_RUN_43376779901_manifest.json)

## Contents

- `program/audit_b13_local_kernel_radial_energy_10mev.py`: full radial-energy and local quadrature audit driver.
- `finite_mixing/moving_muon_compton.py`: exact-recoil B.13 moving thermal-muon collision kernel.
- `rates.py`: mode-resolved local rates and related rate utilities.
- `blinov_reproduction/reference.py`: profile loading and reference background helpers.
- `tests/test_p1b_b13_local_kernel_radial_energy_10mev.py`: regression tests.
- `inputs/sfho188_digitized.csv` and `inputs/profile_provenance.json`: fixed reconstructed background and provenance.

## Reproduction

The authoritative runnable checkout is the repository at the exact source commit above, because the Python package imports rely on the original repository package layout. From a clean checkout:

```bash
git checkout 0f61bfc3e381402cbea9740958b9a2744f006040
python -m pip install numpy scipy
set PYTHONPATH=research/stellar-cooling-constraints-20261105
python -m unittest discover -s research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals -p "test_p1b_b13_local_kernel_radial_energy_10mev.py" -v
python research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/audit_b13_local_kernel_radial_energy_10mev.py --profile research/stellar-cooling-constraints-20261105/data/sfho188_digitized.csv --output research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/outputs/p1b_b13_local_kernel_radial_energy_10mev_reproduced.json
```

Run the exact audit command recorded in the workflow at that commit to reproduce the original JSON. The original numerical JSON is retained unchanged in Actions artifact `p1b-b13-local-radial-energy-10mev` (artifact ID `14015517843`).

## Important scientific status

The original run did **not** pass P1-B acceptance. The recorded quadrature and interpolation discrepancies are documented in the adjacent report. This source snapshot is provided for reproducibility and auditability; it does not convert the result into a validated transport kernel.
