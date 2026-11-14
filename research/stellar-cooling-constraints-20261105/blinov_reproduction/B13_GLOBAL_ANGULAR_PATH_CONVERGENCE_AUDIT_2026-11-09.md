# B.13 global angular/path quadrature convergence audit (2026-11-09)

> **Historical convergence record (2026-11-15):** this is the log-recovered 2026-11-09 PR #57 run; the original full JSON was not archived because the Actions artifact upload failed. Later full-profile B.13/B.2 work was recorded in PR #113, merged on 2026-11-14. Do not treat this compact summary as the complete point-array archive or as current global Fig. 7 validation.

## Executive result

The four B.13 scans completed and the workflow's structural validation passed. All four same-grid B.16 reproduction residuals are exactly zero. The combined (60\times140\times24\times48) grid changes the B.13 luminosity by at most **0.273191%** relative to the original (40\times100\times16\times32) grid; the peak and strong-endpoint changes are **0.267989%** and **0.184207%**, respectively. These are below the predeclared project targets of 1%, 1%, and 2%.

The workflow's overall conclusion is nevertheless **failure**, solely because GitHub rejected the artifact upload after the repository's Actions artifact-storage quota was reached. The original full JSON was generated on the runner but is not available as an artifact or in the branch. This report and the accompanying JSON are therefore explicitly a **log-recovered compact archival record**, not a claim that the original full JSON was downloaded.

## 1. Provenance and fixed inputs

- Workflow: [Run #42542328275](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42542328275)
- Job: `convergence` (job ID `128919874213`)
- Run commit: `7214134a9a42f736b6fe2e707b28b51e3f6274a9`
- PR branch at archival time: `research/moving-muon-thermal-rates-20261107`, HEAD `0bc8f32a30d3dceabd86419601489b74dffccd94`
- Mediator mass: (m_V=10\,\mathrm{MeV})
- Fixed profile SHA256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`
- Four labels and both required B.13 variants are present in the job output.
- The workflow validation confirms the fixed profile fingerprint, exact labels and variants, same-grid B.16 closure, and unchanged production axial files.

The run commit and PR branch were compared for the workflow, convergence script, transport implementation, B.13 summary input, B.16 reference output, and profile CSV; all six blobs were identical. Later documentation-only commits therefore did not change this run's numerical inputs or implementation.

## 2. Four-grid results

All shifts below are relative to the original (40\times100\times16\times32) reference. Values take the largest absolute shift across the (mu^-)-only and both-charge variants.

| Scan | (N_r\times N_E\times N_\Omega\times N_s) | B.16 residual | Max luminosity shift | Peak shift | Strong-endpoint shift | Max escape-fraction shift |
|---|---:|---:|---:|---:|---:|---:|
| angular_only_24x32 | 40×100×24×32 | 0 | 0.001695% | 0.000791% | 0.001695% | 0.001695% |
| path_only_16x48 | 40×100×16×48 | 0 | 0.001597% | 0.000088% | 0.001597% | 0.001597% |
| joint_ray_24x48 | 40×100×24×48 | 0 | 0.000865% | 0.000427% | 0.000865% | 0.000865% |
| combined_60x140_24x48 | 60×140×24×48 | 0 | 0.273191% | 0.267989% | 0.184207% | 0.089418% |

The angular-only, path-only, and joint angular/path scans each change luminosity by less than 0.002%. The combined grid gives a maximum luminosity shift of 0.273191%, a peak shift of 0.267989%, and a strong-endpoint shift of 0.184207%. The maximum escape-fraction shift is 0.089418%. No separate escape-fraction acceptance threshold was predeclared, so this is reported without assigning an additional pass/fail threshold.

The independent radial-energy source cross-check from the archived stage-A JSON gives a B.13/B.16 optically thin source ratio of 0.7889822588 on (40\times100) and 0.7888232697 on (60\times140), a relative change of 0.020151% (decrease). The angular/path refinements do not alter this thin-source integral because they leave radial and energy quadrature unchanged.

## 3. What this establishes—and what it does not

**Established:**
- The four global B.13 quadrature scans completed.
- The expected profile fingerprint, scan labels, and two B.13 variants passed the workflow's structural assertions.
- Every same-grid B.16 closure residual is zero.
- Global luminosity stability passes the stated 1%, 1%, and 2% project targets.

**Not established by this recovered record:**
- The original full JSON's point arrays and detailed diagnostics; the runner generated the file but artifact upload failed.
- A complete local collision-kernel quadrature certification. That remains a separate check.
- Agreement with Fig. 7. The combined-grid log still reports B.13 relative differences of approximately (-28.3\%) at the weak endpoint, (-16.6\%) at the reference peak, and (+131.1\%) at the strong endpoint for the (mu^-)-only variant. Numerical convergence does not remove this reproduction discrepancy.

## 4. Archival and next-step decision

The exact original output path was not present in the branch and the Actions artifact list is empty. GitHub's upload log states: `Failed to CreateArtifact: Artifact storage quota has been hit. Unable to upload any new artifacts. Usage is recalculated every 6-12 hours.`

The accompanying `*_log_recovered_summary.json` preserves the compact per-scan numerical summaries printed by the Actions job, with this limitation recorded in its metadata. The original full JSON should be regenerated or uploaded after the quota becomes available if its full arrays and diagnostics are required.

No physical setting, source, opacity, coupling, or luminosity has been rescaled. No axial-vector production curve, manuscript, or referee response has been changed. PR #57 was Draft/Open at this 2026-11-09 snapshot; later full-profile B.13/B.2 work is documented in PR #113, merged on 2026-11-14.
