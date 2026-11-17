# Fig. 7 10 MeV equation-chain workflow review

Review date: 2026-11-17  
Scope: `.github/workflows/fig7-10mev-equation-chain-audit.yml`  
Review type: static YAML and workflow-boundary review; no new Actions run is claimed by this review.

## Previous configuration

The previous workflow was bound to the legacy branch `codex/major44-axial-cooling-constraints-20261105`, although the active research evidence is now carried by `research/b16-energy-grid-diagnostic-20261117`. It granted `contents: write` at workflow scope, installed unpinned `numpy scipy`, and committed the generated JSON in the same job that performed the numerical calculation. That configuration was not suitable for the current PR branch or least-privilege write-back.

## Revised configuration

**Static disposition: `REVIEWED_WITH_NOTES`.**

- Push and manual-dispatch execution are restricted to the exact research branch by a job-level `github.ref` guard.
- The numerical job has only `contents: read`; the write permission is isolated in a separate archival job.
- The archival job runs only after a successful numerical job and only on the exact research branch.
- Python 3.12.16, NumPy 2.5.4 and SciPy 1.18.1 are pinned.
- The diagnostic JSON is checked for the fixed 10 MeV benchmark, the current profile SHA-256, the expected `(88,180,24,64)` quadrature, three declared coupling points, and local Eq. (20)/(31) residual gates.
- The machine-readable JSON is uploaded as an artifact with missing-file failure, then copied and committed to one fixed output path on the diagnostic branch.
- The output JSON is not a push trigger, so the archive commit does not recursively launch the numerical workflow.
- The workflow does not write rates, opacity tables, luminosity curves, axial constraints, or manuscript files.

## Scientific scope and limitations

The driver `diagnose_fig7_10mev_equation_chain.py` evaluates only three representative coupling points (weak, reference peak and high absorption), not all 25 Fig. 7 vertices. It checks the scalar reference implementation's Eqs. (17)–(20) and (31)–(33), plus detailed-balance and quadrature sensitivities. It is not the missing full local-rate/polarization/escape addendum and does not implement the exact B.13 moving-muon kernel.

The currently archived JSON records profile SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`, quadrature `(88,180,24,64)`, and a high-absorption luminosity of approximately `2.43708e52 erg/s` for this particular configuration. Its output remains diagnostic evidence, not a full Fig. 7 acceptance.

## Execution status

No new workflow run is asserted here. The existing JSON and its source script were inspected; the new workflow must execute on the PR branch before its amended YAML can be considered execution-tested. YAML parsing and static branch/permission review are separate from the scientific result.

## Remaining evidence gap

The dedicated 10 MeV local-rate/polarization/escape package still needs its exact producer/helper source, selected-node CSV, machine-readable pointwise output, plot, pinned-input manifest and independent rerun. The 42-point B.13 summary in the 2026-11-14 report is a restricted local-kernel result; it does not by itself provide the missing reproducible 10 MeV addendum or full-band B.2 transport.

No opacity rescaling, physical convention change, Fig. 7 acceptance, SN1987A limit update, or axial-vector constraint update is authorized by this workflow repair.
