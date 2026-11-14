# Workflow review: pinned independent B.1 thin-source integration

Review date: 2026-11-15  
Workflow: `b16-b1-independent-source-pinned.yml`  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Pinned runtime: Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1

## 1. Static workflow review

- Trigger: path-filtered push to the maintenance review branch and manual `workflow_dispatch`.
- Branch guard: the job explicitly requires `GITHUB_REF=refs/heads/maintenance/repository-organization-audit-20261114`, so manual dispatch from another branch stops before calculation and write-back.
- Runner: GitHub-hosted `ubuntu-latest`; not the user's Windows self-hosted runner.
- Dependencies: exact Python, NumPy, and SciPy versions are pinned/asserted; the numerical requirements file is shared with the other B.16 pinned audit lanes.
- Tests: six independent B.1 quadrature/Jacobian unit tests.
- Calculation: complete optically-thin B.1 source for the 10 MeV vector benchmark, including independent radial and logarithmic-energy quadrature, source-channel decomposition, high-energy-tail convergence, same-40-node comparison with the archived B.16 source, and local-energy versus \(E_\infty\) variable equivalence.
- Acceptance: checks profile and baseline provenance, source-channel closure, kinematic dimuon closure, radial/energy/tail convergence, energy-variable Jacobian consistency, finite values, and production axial-output invariance.
- Write scope: `contents:write` is used only to commit the generated JSON output to the fixed reviewed branch. The generated-output path is excluded from the push path filter to prevent a write-back loop.
- Secrets: no repository secrets are used.

Outcome: `REVIEWED_WITH_NOTES`.

## 2. Execution

Run: [#43650570961](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43650570961)  
Result: success; all steps completed.

- Six unit tests passed.
- Full B.1 thin-source calculation completed.
- Provenance, convergence, closure, and energy-variable checks passed.
- Production axial-vector outputs were unchanged.
- Output was committed to the maintenance review branch.

## 3. Output and numerical results

Output: [`b16_b1_independent_thin_source_10mev_2026-11-15_numpy_pinned.json`](../../../research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_b1_independent_thin_source_10mev_2026-11-15_numpy_pinned.json)

- Output Git blob SHA: `1bfe090d8c0dd1987f6d8c999dec08424f0ec0cb`.
- Run commit: `6c2cdf858cf908f5ba390f4dfae82e01abb132fc`.
- Script SHA-256: `390e9648ab0dc047c9e5c5bbf6aced92e9f496c3f677cb5ce431e4b375554cf5`.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Archived B.16 baseline SHA-256: `a81832562d1c4a1e92d9219e6e38f37aa43f557cf2825cc3e7fd8a27e59b4d7b`.

| Quantity | Result |
|---|---:|
| Independent 400-node B.1 source | \(4.30436817\times10^{70}\) erg/s per \(g^2\) |
| Archived B.16 B.1 source | \(4.32352241\times10^{70}\) erg/s per \(g^2\) |
| Final total source difference | \(-0.443024\%\) |
| Same 40-node radial grid, direct-energy difference | \(-0.575495\%\) |
| 200-to-400-node radial refinement | \(2.1411\times10^{-5}\) |
| Energy cutoff 1000 vs. 4000 MeV | \(2.5746\times10^{-9}\) |
| Local-energy vs. \(E_\infty\) variable residual | \(2.22\times10^{-16}\) |

The calculation sets the escape factor to one. It validates the independent B.1 source quadrature for the adopted reconstructed profile and shared local kernels; it does not constitute the full trapped luminosity or an independent derivation of the collision kernels.

## 4. Remaining scientific boundary

The sub-percent B.1 source difference does not explain the \(+92\%\) Fig. 7 strong-coupling discrepancy. The next step is the pinned end-to-end B.1+B.2 luminosity calculation, using the pinned B.1 source, pinned B.2 analytic path, archived fixed-\(\omega\) baseline, and digitized Fig. 7 vertices. No empirical source or opacity rescaling is authorized.
