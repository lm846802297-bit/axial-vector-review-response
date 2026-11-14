# Independent fermion-sector matrix audit snapshot

> **Checksum note (2026-11-14):** the historical `SHA256SUMS.txt` does not match the snapshot README (expected `c0b1c5a7…`; pre-note file was `8ed7898c…`), while its five other entries matched. It is retained unchanged as historical evidence. Use `SHA256SUMS_CURRENT_2026-11-14.txt` to check the current snapshot files and the preserved historical manifest. The four unit tests were rerun locally; a passing test is not proof of the historical README provenance or full physical-pole validation.

This folder preserves one pinned independent numerical subcalculation from the Major 1 Higgs–singlet mixing workstream. It is a self-contained snapshot and must not overwrite the active Major 1 source files.

## Scope and method

- Fermion sector: charged muon/tau plus the original vector-like-lepton (VLL) sector only.
- Numerical method: SciPy SVD (gesvd) and 45-digit mpmath integration of the Feynman-parameter representation of B0.
- Renormalization scale: 20,000 GeV.
- External momentum squared: 15,687.5625 GeV^2.
- Benchmarks: A_open_AA and B_closed_AA.
- The implementation is independent of the archived fermion-sector matrix routine.

## Recorded validation

The preserved test log reports four passing unit tests covering the zero-momentum equal-mass B0 limit, the heavy equal-mass below-threshold imaginary part, the light-pair positive absorptive part above threshold, and the chiral-coefficient/explicit-Dirac-trace comparison.

The JSON comparison to the archived calculation is marked PASS for both benchmarks. The maximum absolute hard-difference errors recorded are 1.49e-8 GeV^2 (A) and 1.86e-9 GeV^2 (B).

## Interpretation limits

This is an independent numerical check of a fermion-sector subcalculation, not a complete gauge-independent self-energy. It excludes top, W, Z, A-prime, Goldstone, ghost, scalar, tadpole, and VEV-renormalization contributions. The hard momentum differences are not physical pole shifts. No complex poles, residues, mixing angle, line shape, signal strength, or exclusion is inferred. If explicit mu/tau absorptive cuts are retained in a future propagator, their partial widths must not be inserted again as external diagonal widths.

## Reproduction

From this directory, install NumPy, SciPy, and mpmath, then run:

- python -m unittest -v test_independent_fermion_sector_matrix_audit.py
- python independent_fermion_sector_matrix_audit.py --help

The archived test output and original checksum manifest are preserved in this folder. SHA256SUMS.txt checksums every snapshot file except itself.
