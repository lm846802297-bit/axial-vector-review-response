# Individual review: Belle II model-classification and detector-input notes

Baseline `13cb036cc89f04e6444d2e273032e51727dac0d7`, 2026-11-15. Four documents were read individually and compared with the available source, later bounded-width summary and the 69-test local run in the preceding review. These checks do not independently reproduce the Belle II likelihood, detector efficiency, actual finite-width response or all physics derivations.

| Document under `research/radial-scalar-collider-recast-2026-10-28/` | Individual findings and disposition |
|---|---|
| `allowed-mass-classification.md` | One-VEV relations yield the stated scalar-self-coupling upper bound; the four classification categories distinguish missing acceptance from exclusion. This is a research protocol and does not supply a universal allowed interval. PASS_WITH_NOTES. |
| `validation-results-2026-11-05.md` | Dated 14-test snapshot explicitly distinguishes its earlier data status from later table audit. Current local 69-test run is a separate execution and does not prove this older environment. Preserve as history. HISTORICAL. |
| `finite-width-line-shape-inputs-and-validation-2026-11-05.md` | The seven described unit checks are among the tests rerun successfully. Missing double-Crystal-Ball and mass-dependent production/selection inputs prevent interpreting a synthetic convolution as an exact Belle II broad-width limit. The model spectrum and external experimental assumptions were not independently rederived in this review. PASS_WITH_NOTES. |
| `lifetime-dependent-belleii-efficiency-audit-2026-11-05.md` | Geometry proxy and detector efficiency remain explicitly distinct. Added a warning that `1,852/946/15` describe an older width-complete classification; the later bounded-width analysis uses a different treatment and reports different counts (e.g. 2,746 conditional four-muon points). Counts are not universal exclusion claims. Historical publication citations were not freshly verified here. PASS_WITH_NOTES. |

The different archived classification approaches must not be merged or compared as identical without their inputs and decision rules. A DCA requirement is not a decay-radius efficiency curve.
