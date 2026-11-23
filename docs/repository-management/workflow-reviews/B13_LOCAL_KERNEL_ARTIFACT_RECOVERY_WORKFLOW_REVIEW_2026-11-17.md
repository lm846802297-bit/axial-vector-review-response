# P1-B B.13 local-kernel artifact recovery workflow review

Review date: 2026-11-17
Workflow: .github/workflows/b13-local-kernel-artifact-recovery.yml
Review type: static YAML/source review plus local builder/test validation; no new B.13 collision-kernel calculation is claimed.

## Provenance recovery

The original Actions run is [#43376779901](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43376779901), artifact ID 14015517843, artifact name p1b-b13-local-radial-energy-10mev. Its original JSON SHA-256 is 14c4405f9421aca517ff00310232ad9aead4c0cdd61868e2788125875cb84dc0; the artifact ZIP SHA-256 independently verified in the working environment is 2c2e2ef8610abfa16bc9e423937f974061ece101911fb9c6503e65901bb55715.

All seven exact source/input Git blob IDs in the archived source manifest were checked against the active PR branch and matched: the producer script, regression test, moving-muon kernel, rates module, profile loader, profile CSV and provenance JSON. The original source commit is 0f61bfc3e381402cbea9740958b9a2744f006040.

## Recovery workflow boundaries

- The recovery job uses actions: read and contents: read only.
- It downloads the named artifact from the exact historical run ID and verifies the original JSON SHA-256 before processing.
- The post-processor is standard-library-only and creates a long-form CSV (513 grid nodes + 468 direct cell midpoints, each expanded over two charges and three modes), two SVG heatmaps, a README and a manifest.
- Unit tests check point/row counts, both charges, all three polarization modes, nonnegative rates, detailed balance, mass-shell closure, source/profile identity, and that the original failed quadrature/interpolation acceptance remains failed.
- The archival job alone receives contents: write, only after recovery/tests succeed, and writes one fixed evidence directory to the exact diagnostic branch with retry-safe fetch/reset/push.

## Numerical interpretation boundary

The archived original calculation is not accepted. Detailed balance, mass-shell closure and local emissivity energy integration pass. Grid-node quadrature refinement (maximum 0.3368% versus 0.1% target), cell-midpoint refinement (maximum 0.2440%), and direct midpoint/interpolation agreement (maximum 57.13% versus 1% target) fail. The original status remains overall_p1b_pass=false.

This workflow only recovers and visualizes the existing artifact. It does not rerun the B.13 kernel, repair the quadrature/interpolation failures, perform B.2 path transport, reproduce the Fig. 7 10 MeV strong-absorption endpoint, or update any SN1987A/axial-vector constraint.
