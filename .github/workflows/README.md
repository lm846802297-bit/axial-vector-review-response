# GitHub Actions workflow catalog

Inventory reconciled on PR #123 branch on 2026-11-24 after PR #140 merged into main. The 140 YAML files are listed below by provisional topic. This index is not a claim that all workflows are active or that their historical runs passed. 110 of the 140 workflows have individual static YAML reviews recorded in the register; 14 are historical candidates, one is active, and 15 newly added Croon/A0 workflows remain PENDING for full static and execution review. Reviews 80–90 extend the static inventory; the 90th review adds three individually checked closeout workflows. All 14 retained historical candidates have run-history triage: 499 runs across their configured branches, with failures and cancellations preserved in the record. Static review does not establish successful execution or scientific acceptance. See the [C4-C4 review](../../docs/repository-management/workflow-reviews/C4C4_WORKFLOW_REVIEW_2026-11-17.md), [B.2 path workflow review](../../docs/repository-management/workflow-reviews/B2_PATH_WORKFLOW_REVIEW_2026-11-17.md), [outer-profile sensitivity review](../../docs/repository-management/workflow-reviews/B16_OUTER_PROFILE_SENSITIVITY_WORKFLOW_REVIEW_2026-11-17.md), and [muon-profile/neutrino-branch review](../../docs/repository-management/workflow-reviews/B16_MUON_PROFILE_AND_NEUTRINO_BRANCH_WORKFLOW_REVIEW_2026-11-17.md). The historical-candidate triage is recorded in [the final review](../../docs/repository-management/workflow-reviews/HISTORICAL_CANDIDATE_WORKFLOW_TRIAGE_2026-11-17.md). The complete later review series is linked in [the review index](../../docs/repository-management/workflow-reviews/README.md): [B.16 全径向 SFHo EOS 占据数](../../docs/repository-management/workflow-reviews/B16_FULL_RADIAL_EOS_OCCUPATION_WORKFLOW_REVIEW_2026-11-17.md), [C4 EOS 响应与碰撞核](../../docs/repository-management/workflow-reviews/B16_C4_EOS_RESPONSE_AND_COLLISION_WORKFLOW_REVIEW_2026-11-17.md), [B.16 路径积分与剖面敏感性](../../docs/repository-management/workflow-reviews/B16_PATH_QUADRATURE_AND_PROFILE_SENSITIVITY_WORKFLOW_REVIEW_2026-11-17.md), [Bollig 图像与缪子密度来源](../../docs/repository-management/workflow-reviews/BOLLIG_FIGURE_AND_MUON_DENSITY_WORKFLOW_REVIEW_2026-11-17.md), [剖面来源、碰撞积分与 B.2 审计](../../docs/repository-management/workflow-reviews/PROFILE_SOURCE_COLLISION_AND_B2_WORKFLOW_REVIEW_2026-11-17.md), [Fig. 7 源文件与收敛工作流](../../docs/repository-management/workflow-reviews/FIG7_SOURCE_AND_CONVERGENCE_WORKFLOW_REVIEW_2026-11-17.md), [最后六项 collider、response 与吸收工作流](../../docs/repository-management/workflow-reviews/FINAL_COLLIDER_AND_RESPONSE_WORKFLOW_REVIEW_2026-11-17.md).

## Topic groups

### Research governance and structured-result validation (2)

- [`axial-structured-result-validation.yml`](axial-structured-result-validation.yml)
- [`standards-adoption-validation.yml`](standards-adoption-validation.yml)

### Two-VEV extension regressions (1)

- [`axial-goldstone-pmns-regression.yml`](axial-goldstone-pmns-regression.yml)

### Major 4.4 stellar cooling / transport (111)

- [`b13-high-order-provenance-validation.yml`](b13-high-order-provenance-validation.yml)
- [`b13-local-kernel-artifact-recovery.yml`](b13-local-kernel-artifact-recovery.yml)
- [`b16-energy-grid-identity-diagnostic.yml`](b16-energy-grid-identity-diagnostic.yml)
- [`b16-output-validator-tests.yml`](b16-output-validator-tests.yml)
- [`b16-strict-phase-space-reproduction.yml`](b16-strict-phase-space-reproduction.yml)
- [`b13-exact-compton-radial.yml`](b13-exact-compton-radial.yml)
- [`b13-exact-compton-vertex-preserving.yml`](b13-exact-compton-vertex-preserving.yml)
- [`b13-global-convergence-audit.yml`](b13-global-convergence-audit.yml)
- [`b13-global-convergence.yml`](b13-global-convergence.yml)
- [`b13-global-grid-convergence.yml`](b13-global-grid-convergence.yml)
- [`b13-global-transport-summary.yml`](b13-global-transport-summary.yml)
- [`b13-global-transport-vertex-preserving.yml`](b13-global-transport-vertex-preserving.yml)
- [`b13-local-kernel-convergence-audit.yml`](b13-local-kernel-convergence-audit.yml)
- [`b13-local-kernel-low-mass-convergence.yml`](b13-local-kernel-low-mass-convergence.yml)
- [`b13-low-mass-global-convergence.yml`](b13-low-mass-global-convergence.yml)
- [`b13-muon-velocity-diagnostic.yml`](b13-muon-velocity-diagnostic.yml)
- [`b16-b1-independent-source.yml`](b16-b1-independent-source.yml)
- [`b16-dense-local-kernel-audit.yml`](b16-dense-local-kernel-audit.yml)
- [`b16-directional-escape-8-15.yml`](b16-directional-escape-8-15.yml)
- [`b16-directional-escape.yml`](b16-directional-escape.yml)
- [`b16-emission-radius-escape.yml`](b16-emission-radius-escape.yml)
- [`b16-escape-phase-space.yml`](b16-escape-phase-space.yml)
- [`b16-escape-phase-space-closeout.yml`](b16-escape-phase-space-closeout.yml)
- [`b16-flavour-fixed-vs-redshift.yml`](b16-flavour-fixed-vs-redshift.yml)
- [`b16-full-b1b2-independent.yml`](b16-full-b1b2-independent.yml)
- [`b16-global-fig7-vertex-preserving.yml`](b16-global-fig7-vertex-preserving.yml)
- [`b16-global-polarization-transport.yml`](b16-global-polarization-transport.yml)
- [`b16-global-redshift-audit.yml`](b16-global-redshift-audit.yml)
- [`b16-high-order-independent-grid.yml`](b16-high-order-independent-grid.yml)
- [`b16-high-energy-kernel-regression.yml`](b16-high-energy-kernel-regression.yml)
- [`b16-high-energy-strict-numpy-reproduction.yml`](b16-high-energy-strict-numpy-reproduction.yml)
- [`b16-high-energy-global-sensitivities-numpy.yml`](b16-high-energy-global-sensitivities-numpy.yml)
- [`b16-independent-analytic-path-pinned.yml`](b16-independent-analytic-path-pinned.yml)
- [`b16-b1-independent-source-pinned.yml`](b16-b1-independent-source-pinned.yml)
- [`b16-full-b1b2-independent-pinned.yml`](b16-full-b1b2-independent-pinned.yml)
- [`b16-independent-grid-quadrature-convergence.yml`](b16-independent-grid-quadrature-convergence.yml)
- [`b16-inner-numu-branch-sensitivity.yml`](b16-inner-numu-branch-sensitivity.yml)
- [`b16-inner-path-channel-directional.yml`](b16-inner-path-channel-directional.yml)
- [`b16-inner-path-vertex-preserving.yml`](b16-inner-path-vertex-preserving.yml)
- [`b16-lapse-boundary-sensitivity.yml`](b16-lapse-boundary-sensitivity.yml)
- [`b16-local-absorption-vertex-preserving.yml`](b16-local-absorption-vertex-preserving.yml)
- [`b16-local-absorption.yml`](b16-local-absorption.yml)
- [`b16-local-rate-polarization-samples.yml`](b16-local-rate-polarization-samples.yml)
- [`b16-neutrino-flavour-opacity.yml`](b16-neutrino-flavour-opacity.yml)
- [`b16-neutrino-inverse-decay-audit.yml`](b16-neutrino-inverse-decay-audit.yml)
- [`b16-neutrino-inverse-decay-direct.yml`](b16-neutrino-inverse-decay-direct.yml)
- [`b16-numu-positive-branch-sensitivity.yml`](b16-numu-positive-branch-sensitivity.yml)
- [`b16-numu-profile-sensitivity.yml`](b16-numu-profile-sensitivity.yml)
- [`b16-outer-22-25-temperature-sensitivity.yml`](b16-outer-22-25-temperature-sensitivity.yml)
- [`b16-outer-escape-angular-distribution.yml`](b16-outer-escape-angular-distribution.yml)
- [`b16-outer-numu-22-25km-sensitivity.yml`](b16-outer-numu-22-25km-sensitivity.yml)
- [`b16-outer-numu-floor-sensitivity.yml`](b16-outer-numu-floor-sensitivity.yml)
- [`b16-outer-profile-input-audit.yml`](b16-outer-profile-input-audit.yml)
- [`b16-outer-profile-interpolation.yml`](b16-outer-profile-interpolation.yml)
- [`b16-outer-shell-polarization-resolved.yml`](b16-outer-shell-polarization-resolved.yml)
- [`b16-outer-temperature-sensitivity.yml`](b16-outer-temperature-sensitivity.yml)
- [`b16-p1iii-eos-degeneracy.yml`](b16-p1iii-eos-degeneracy.yml)
- [`b16-p1iii-eos-full-profile.yml`](b16-p1iii-eos-full-profile.yml)
- [`b16-p1iii-eos-full-radial-degeneracy-identity.yml`](b16-p1iii-eos-full-radial-degeneracy-identity.yml)
- [`b16-p1iii-eos-full-radial-degeneracy-radial-diagnostics.yml`](b16-p1iii-eos-full-radial-degeneracy-radial-diagnostics.yml)
- [`b16-p1iii-eos-full-radial-degeneracy-step-scan.yml`](b16-p1iii-eos-full-radial-degeneracy-step-scan.yml)
- [`b16-p1iii-eos-full-radial-occupation.yml`](b16-p1iii-eos-full-radial-occupation.yml)
- [`b16-p1iiie-c4a-eos-dynamic-scalar-response.yml`](b16-p1iiie-c4a-eos-dynamic-scalar-response.yml)
- [`b16-p1iiie-c4b1-effective-mass-weak-tensor.yml`](b16-p1iiie-c4b1-effective-mass-weak-tensor.yml)
- [`b16-p1iiie-c4b2-effective-mass-collision-kernel.yml`](b16-p1iiie-c4b2-effective-mass-collision-kernel.yml)
- [`b16-p1iiie-c4c1-exact-outgoing-energy-support.yml`](b16-p1iiie-c4c1-exact-outgoing-energy-support.yml)
- [`b16-p1iiie-c4c2-full-angle-eprime-convergence.yml`](b16-p1iiie-c4c2-full-angle-eprime-convergence.yml)
- [`b16-p1iiie-c4c2-full-angle-total-scattering.yml`](b16-p1iiie-c4c2-full-angle-total-scattering.yml)
- [`b16-p1iiie-c4c3-radial-scattering.yml`](b16-p1iiie-c4c3-radial-scattering.yml)
- [`b16-p1iiie-c4c4-energy-dependence.yml`](b16-p1iiie-c4c4-energy-dependence.yml)
- [`b16-p1iiie-c4c4-quadrature-convergence.yml`](b16-p1iiie-c4c4-quadrature-convergence.yml)
- [`b16-p1iiie-c4c4b-full-radial-energy-dependence.yml`](b16-p1iiie-c4c4b-full-radial-energy-dependence.yml)
- [`b16-path-independent-analytic.yml`](b16-path-independent-analytic.yml)
- [`b16-quadrature-convergence.yml`](b16-quadrature-convergence.yml)
- [`b16-shell-luminosity-sensitivity.yml`](b16-shell-luminosity-sensitivity.yml)
- [`b2-opacity-interpolation-convergence.yml`](b2-opacity-interpolation-convergence.yml)
- [`b2-path-energy-convergence.yml`](b2-path-energy-convergence.yml)
- [`b2-radial-source-convergence.yml`](b2-radial-source-convergence.yml)
- [`bollig-fig3-crosscheck.yml`](bollig-fig3-crosscheck.yml)
- [`bollig-fig4-muon-profile.yml`](bollig-fig4-muon-profile.yml)
- [`bollig-muon-density-b1-audit.yml`](bollig-muon-density-b1-audit.yml)
- [`bollig-outer-thermodynamic-profile.yml`](bollig-outer-thermodynamic-profile.yml)
- [`bollig-profile-vector-audit.yml`](bollig-profile-vector-audit.yml)
- [`build-stellar-cooling-review-archive.yml`](build-stellar-cooling-review-archive.yml)
- [`caputo-muon-density-vector-audit.yml`](caputo-muon-density-vector-audit.yml)
- [`caputo-offframe-thermodynamic-audit.yml`](caputo-offframe-thermodynamic-audit.yml)
- [`direct-collision-integrals.yml`](direct-collision-integrals.yml)
- [`eq-b2-independent-path-integral.yml`](eq-b2-independent-path-integral.yml)
- [`fig12-vector-extraction.yml`](fig12-vector-extraction.yml)
- [`fig7-10mev-equation-chain-audit.yml`](fig7-10mev-equation-chain-audit.yml)
- [`fig7-10mev-three-layer-audit.yml`](fig7-10mev-three-layer-audit.yml)
- [`fig7-digitization-geometry-audit.yml`](fig7-digitization-geometry-audit.yml)
- [`fig7-highres-convergence.yml`](fig7-highres-convergence.yml)
- [`fig7-refined-scan.yml`](fig7-refined-scan.yml)
- [`fig7-six-mass-reproduction.yml`](fig7-six-mass-reproduction.yml)
- [`fig7-source-drawings.yml`](fig7-source-drawings.yml)
- [`fig7-spatial-weight-matrix.yml`](fig7-spatial-weight-matrix.yml)
- [`fig7-ultrafine-0p1.yml`](fig7-ultrafine-0p1.yml)
- [`fig7-ultrafine-light-mass.yml`](fig7-ultrafine-light-mass.yml)
- [`moving-muon-thermal-rates.yml`](moving-muon-thermal-rates.yml)
- [`muon-chemical-potential-audit.yml`](muon-chemical-potential-audit.yml)
- [`muon-profile-sensitivity-10mev.yml`](muon-profile-sensitivity-10mev.yml)
- [`outer-neutrino-absorption-audit.yml`](outer-neutrino-absorption-audit.yml)
- [`p1-b13-exact-polarization-kernel.yml`](p1-b13-exact-polarization-kernel.yml)
- [`p1b-b13-local-kernel-radial-energy.yml`](p1b-b13-local-kernel-radial-energy.yml)
- [`p1b-source-bundle.yml`](p1b-source-bundle.yml)
- [`p1iii-eos-c4c3-radial-scattering.yml`](p1iii-eos-c4c3-radial-scattering.yml)
- [`profile-12-15km-audit.yml`](profile-12-15km-audit.yml)
- [`pure-vector-benchmark-audit.yml`](pure-vector-benchmark-audit.yml)
- [`transport-prescription-audit.yml`](transport-prescription-audit.yml)
- [`vector-rescaling-audit.yml`](vector-rescaling-audit.yml)

### Major 1 scalar / Higgs / collider (7)

- [`finite-mixing-model-map.yml`](finite-mixing-model-map.yml)
- [`independent-belleii-pointwise-audit.yml`](independent-belleii-pointwise-audit.yml)
- [`independent-fourbody-tensor-audit.yml`](independent-fourbody-tensor-audit.yml)
- [`independent-higgs-scalar-matrix-audit.yml`](independent-higgs-scalar-matrix-audit.yml)
- [`major1-higgs-scalar-mixing.yml`](major1-higgs-scalar-mixing.yml)
- [`major1-scalar-belleii.yml`](major1-scalar-belleii.yml)
- [`scan-archive-integrity-closeout.yml`](scan-archive-integrity-closeout.yml)

### Needs manual classification (1)

- [`major44-eft-regression.yml`](major44-eft-regression.yml)

### Referee-letter LaTeX build (2)

- [`pr55-latex-build.yml`](pr55-latex-build.yml)
- [`pr55-referee-letter-build.yml`](pr55-referee-letter-build.yml)

### Vector–axial response mapping (1)

- [`vector-axial-response-scan.yml`](vector-axial-response-scan.yml)

### Croon/Lai vector benchmark and A0 UV transport (15)

- [`a0-spinor-stability-tests.yml`](a0-spinor-stability-tests.yml)
- [`croon-a0-10mev-adaptive-energy-convergence.yml`](croon-a0-10mev-adaptive-energy-convergence.yml)
- [`croon-a0-10mev-adaptive-radial-convergence.yml`](croon-a0-10mev-adaptive-radial-convergence.yml)
- [`croon-a0-uv-axial-transport.yml`](croon-a0-uv-axial-transport.yml)
- [`croon-c1-10mev-adaptive-energy-convergence.yml`](croon-c1-10mev-adaptive-energy-convergence.yml)
- [`croon-c1-10mev-adaptive-radial-baseline.yml`](croon-c1-10mev-adaptive-radial-baseline.yml)
- [`croon-c1-10mev-grid-convergence.yml`](croon-c1-10mev-grid-convergence.yml)
- [`croon-c1-10mev-high-order.yml`](croon-c1-10mev-high-order.yml)
- [`croon-c1-10mev-result-archive.yml`](croon-c1-10mev-result-archive.yml)
- [`croon-c1-10mev-single-baseline.yml`](croon-c1-10mev-single-baseline.yml)
- [`croon-c1-adaptive-radial-output-audit.yml`](croon-c1-adaptive-radial-output-audit.yml)
- [`croon-c1-b13-vector-transport.yml`](croon-c1-b13-vector-transport.yml)
- [`croon-semcompton-rate-regression.yml`](croon-semcompton-rate-regression.yml)
- [`export-a0-energy-source-bundle.yml`](export-a0-energy-source-bundle.yml)
- [`original-uv-goldstone-ward-regression.yml`](original-uv-goldstone-ward-regression.yml)

These 15 workflows are registered as `PENDING`; their triggers and permissions have been inventoried, but full per-workflow review and latest-run triage remain open. Push-triggered workflows and workflows with `contents: write` must be checked against the central compute policy before being treated as active/reviewed.

## Individual audit register

See [WORKFLOW_AUDIT_REGISTER.csv](WORKFLOW_AUDIT_REGISTER.csv). Current register totals are 110 `REVIEWED_WITH_NOTES`, 1 `ACTIVE`, 14 `HISTORICAL_CANDIDATE`, and 15 `PENDING`. Individual review records are grouped in [batch 1](../../docs/repository-management/workflow-reviews/WORKFLOW_REVIEW_BATCH_2026-11-14.md), [batch 2](../../docs/repository-management/workflow-reviews/WORKFLOW_REVIEW_BATCH_2_2026-11-14.md), [B.13 kernel and global review](../../docs/repository-management/workflow-reviews/B13_WORKFLOW_REVIEW_BATCH_2026-11-14.md), [B.14/B.16 local review](../../docs/repository-management/workflow-reviews/B14_B16_LOCAL_WORKFLOW_REVIEW_2026-11-14.md), [B.16 escape benchmark review](../../docs/repository-management/workflow-reviews/B16_ESCAPE_BENCHMARK_WORKFLOW_REVIEW_2026-11-14.md), and [B.16 high-order inner-path review](../../docs/repository-management/workflow-reviews/B16_HIGH_ORDER_INNER_PATH_REVIEW_2026-11-14.md), and [B.16 outer-profile and polarization review](../../docs/repository-management/workflow-reviews/B16_OUTER_PROFILE_AND_POLARIZATION_WORKFLOW_REVIEW_2026-11-15.md). The [first-batch B.13/B.16 and governance workflow review, 2026-11-23](../../docs/repository-management/workflow-reviews/FIRST_BATCH_B13_B16_AND_GOVERNANCE_WORKFLOW_REVIEW_2026-11-23.md) records the seven newly reconciled workflows and their execution evidence. The [2026-11-17 local-rate, escape-phase-space and PR52 archive workflow review](../../docs/repository-management/workflow-reviews/B16_LOCAL_RATE_ESCAPE_AND_SCAN_ARCHIVE_WORKFLOW_REVIEW_2026-11-17.md) covers the three new closeout workflows. The older [batch 2 summary](../../docs/repository-management/workflow-reviews/WORKFLOW_REVIEW_BATCH_2.md) is retained as an earlier review note.

## Classification and maintenance rules

- Topic groups are provisional filename-based classifications; correct them only after inspecting each workflow's actual paths and commands.
- For every workflow, record its exact triggers, branch filters, path filters, permissions, runner, Python/TeX versions, dependencies, commands, artifact behavior, write-back behavior and known latest run.
- Use status labels `ACTIVE`, `HISTORICAL_CANDIDATE`, `SUPERSEDED`, `EXPERIMENTAL`, `REVIEWED_WITH_NOTES`, or `PENDING`.
- A workflow pinned to a retired branch is not automatically safe to delete: check historical run links, callers, branch refs and whether the workflow remains manually dispatchable.
- Minimize write permissions. Workflows that only test should use `contents: read`; workflows that commit results require an explicit output/provenance contract.
- Keep CI/software status distinct from scientific acceptance. A green workflow cannot close a physical validation gate by itself.
- Do not consolidate workflows solely because they share Python dependencies; different physical gates and inputs may need separate validation lanes.
