# P1-B 10 MeV exact B.13 local-kernel archive

This package preserves and expands the original GitHub Actions numerical artifact. The CSV and SVG files are deterministic post-processing of the unchanged JSON, not a new collision-kernel calculation.

- Original Actions run: [#43376779901](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43376779901)
- Original artifact ID: 14015517843; ZIP SHA-256: 2c2e2ef8610abfa16bc9e423937f974061ece101911fb9c6503e65901bb55715
- Original JSON SHA-256: 14c4405f9421aca517ff00310232ad9aead4c0cdd61868e2788125875cb84dc0
- Exact source commit: 0f61bfc3e381402cbea9740958b9a2744f006040
- Reconstructed SFHo-18.8 profile SHA-256: 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c (not raw Garching data)

The JSON contains 513 grid nodes and 468 direct cell-midpoint evaluations. The long-form CSV has 5886 rows, retaining both muon charges and all three polarization modes separately.

## Numerical acceptance (preserved, not promoted)

- Detailed-balance maximum residual: 4.26599e-14 (tolerance 2e-10): PASS.
- Final-muon mass-shell maximum residual: 7.0487e-13 (tolerance 2e-10): PASS.
- Local emissivity energy-order change: 5.32625e-06: PASS.
- Grid-node quadrature refinement maximum: 0.00336775 (target 0.001): FAIL.
- Cell-midpoint refinement maximum: 0.00244042: FAIL.
- Direct midpoint versus interpolation maximum: 0.571297 (target 0.01): FAIL.

**Overall P1-B local-kernel acceptance remains NOT PASSED.** This is not a B.2 optical-depth calculation, full Fig. 7 transport reproduction, or SN1987A constraint. No opacity rescaling or axial-vector limit update is authorized.
