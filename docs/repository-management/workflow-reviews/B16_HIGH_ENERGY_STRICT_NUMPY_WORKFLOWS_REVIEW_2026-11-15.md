# Workflow review: strict NumPy B.16 high-energy reproductions

Review date: 2026-11-15  
Topic: independent numerical reproduction of the archived B.16 high-energy V8 diagnostics  
Pinned runtime: Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1

## 1. b16-high-energy-strict-numpy-reproduction.yml

Workflow: [.github/workflows/b16-high-energy-strict-numpy-reproduction.yml](../../../.github/workflows/b16-high-energy-strict-numpy-reproduction.yml)  
Reviewed revision: 83f36f06ae4d4442fa0a1faf5632a22d64a821b0  
Run: [#43647616434](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43647616434)  
Output commit: ffea309c5bb70880e8970c8d4ccddb928de517cc

- Trigger: push to the maintenance review branch with source/data/workflow path filters; manual workflow_dispatch.
- Runner: GitHub-hosted ubuntu-latest; this is an independent hosted reproduction run, not the user's Windows self-hosted runner.
- Permissions: contents: write, used only to commit the two generated JSON outputs to the reviewed branch.
- Calculations: complete B.1+B.2 channel-resolved result and 36-ray high-energy neutrino chord convergence.
- Provenance: both outputs contain the script SHA-256, run commit, profile SHA-256, and Fig. 7 input SHA-256.
- Outcome: success. Full channel luminosity agrees with V8 to \(9.22\times10^{-13}\); escape probability to \(8.35\times10^{-13}\); source-weighted mean optical depth to \(1.75\times10^{-14}\). All five chord refinement metrics agree with V8 to a maximum relative difference of \(1.19\times10^{-9}\).

## 2. b16-high-energy-global-sensitivities-numpy.yml

Workflow: [.github/workflows/b16-high-energy-global-sensitivities-numpy.yml](../../../.github/workflows/b16-high-energy-global-sensitivities-numpy.yml)  
Reviewed revision: 9d7665560d61479b2cda653b2dd842a4340b14d6  
Run: [#43648694518](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43648694518)  
Output commit: b14c4d2

- Trigger: push to the maintenance review branch with source/data/V8-reference path filters; manual workflow_dispatch.
- Runner: GitHub-hosted ubuntu-latest.
- Permissions: contents: write, used only to archive the two generated JSON outputs.
- Calculations: seven frozen-source outer-temperature scenarios and the global \(210\text{--}510\) MeV fixed-\(\omega\)/path-redshift comparison.
- Interpolation fidelity: path-redshift strict reproduction uses the archived V8 bilinear interpolation in radius and local energy. Direct local-rate recomputation is retained as a separate interpolation-method sensitivity.
- Tests: five V8-versus-NumPy tests cover channel, chord, outer-temperature, path-redshift, and the direct-versus-bilinear method distinction.
- Outcome: success; all five tests pass. The outer-temperature main observables agree with V8 to better than \(2.5\times10^{-7}\) relative; path-redshift bilinear observables agree to better than \(3\times10^{-14}\).

## 3. Security, scope, and scientific limitations

- The workflows run on GitHub-hosted runners and use no repository secrets.
- The write token is used only to add generated output JSONs to the same reviewed branch.
- The workflows do not edit the reconstructed source profile, Fig. 7 digitization, production source/opacity code, couplings, manuscript, or axial-vector constraints.
- These are independent strict NumPy reproductions of the archived high-energy diagnostics. They do not resolve the \(+92\%\) strong-endpoint Fig. 7 discrepancy.
- The path-redshift branch remains a sensitivity calculation, not the printed fixed-\(\omega\) Eq. (B.2) baseline and not a full-GR ray trace.
- Full-GR transport remains blocked by the absence of same-snapshot \(A(r)\) or \(M(r)\) data.

Outcome: REVIEWED_WITH_NOTES for both workflows.
