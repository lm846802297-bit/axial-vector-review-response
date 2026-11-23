# C1 10 MeV structured result archive

- Run: C1-10MeV-153R-48E-20261120-44656225572
- Physics workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44656225572
- Radial workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44650913407
- Grid: 153 actual radial nodes, energy order 48, 121 coupling points, L/T+/T-.
- Radial convergence: 0.00116929568 (threshold 0.0012).
- Energy convergence: 1.30310648e-07 (threshold 0.0001).
- Numerical convergence: PASS; physical scope: PARTIAL.

This directory includes byte-for-byte snapshots of the SFHo profile, 103/153-node radial results, the 153x48 final transport JSON/CSV, original convergence reports and checksum manifests, plus the generated 121-point coupling curve. The source code is pinned by the physics commit and SHA-256 in run_manifest.json.

Outer 25-100 km B.13 semi-Compton opacity is omitted. This is not a final SN1987A exclusion curve. The archive generator packages existing outputs only; it does not rerun the physics calculation.
