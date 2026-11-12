# 2026-11-13 branch integration audit

Audit baseline: main at `4fdb7ea3b0e85412525322b6b3d584365a852363`, after the C4-C4-B and separate two-VEV integrations.

## Integration completed

- **PR #84 — merged:** C4-C4-B full-radial, energy-dependent local-scattering archive. It adds the 7,224-row result set, 340 stratified high-order comparisons, radial-grid checks, provenance, and checksums. This remains a fixed-local-energy, flat-space total-scattering diagnostic; it is not full SN transport, an escape probability, a Blinov Fig. 7 reproduction, or an SN1987A exclusion.
- **PR #85 — merged:** separate two-VEV axial microphysics benchmark. It preserves the exact two-VEV Goldstone map, generic vacuum semi-Compton amplitude, current-level widths, homogeneous optically thin rate, tests, and convergence record. It is explicitly an alternative model extension, not the original one-VEV model used in the paper.
- **PR #82 — closed as superseded by #84.** The older PR replayed the long pre-squash C4-C4 branch history and was conflict-marked; #84 transferred only the true incremental result files onto current main.
- **PR #83 — closed as duplicate of #77.** Its head commit was already merged by #77.
- No open PRs remained at the end of this audit.

## How to interpret the branch comparison

GitHub listed 90 non-main branch refs at the audit. 75 reported `ahead_by > 0` against main. This is not equivalent to 75 unmerged research packages: many branches were integrated by squash merge, so their old commit ancestry remains divergent even when the corresponding file content is already in main.

The following major research workstreams are already represented in main through merged PRs:

- Original-model axial stellar-cooling mapping and semi-Compton microphysics: PR #53.
- Major 4.4 axial-EFT benchmark and the moving-muon/EOS work carried through its base branch: PR #56 (with the PR #57 work merged into that base before the final PR #56 integration).
- Original-model Belle II radial-scalar reinterpretation: PR #68.
- Higgs–singlet mixing and UV–EFT matching audits: PR #69.
- Neutrino-mass response: PR #72.
- Research-result archival, extraction-before-upload, and CI-optional policies: PRs #73, #80, and #81.
- C4-C4-A/Aq source and runner: PR #79; the subsequent C4-C4-B results are now in PR #84.

These branches must not be re-imported solely because their ahead counts remain large.

## Branches intentionally not promoted in this pass

- `research/higgs-signal-strength-two-benchmarks-2026-10-28`: preliminary non-degenerate screening based on inherited fixed-self-energy proxy values. Its limitations are explicit, and the later PR #69 work contains the more developed mass-eigenstate, portal-threshold, and complex-pole analysis. Do not treat the old proxy as a current physical mixing angle or Higgs exclusion.
- `research/radial-scalar-two-vev-belleii-20261105-current-main`: raw supplemental-data fragments only. Its scalar four-muon table is a formatting variant of the Belle II source table already archived with provenance in PR #68; the additional vector-control file is not accompanied by a self-contained source manifest or analysis record.
- `transfer/p1iii-eos-latest-source-20261111`: temporary source-package workflow, not a new EOS calculation/result archive.
- `transfer/pr57-source-bundle-20261110` and `transfer/sfho-frdm-release-transfer-20261111`: no tree-level file delta against main; their source/data content is already represented in the merged research history.
- `work/hs-mixing-one-loop-20261027`: older one-loop working note and response draft, superseded by PR #69 and the later matching/pole records.
- The old PR #30 axial recast and PR #32/#52 radial-scalar drafts are superseded by the later original-model archives in PRs #53/#56 and #68, respectively.
- Historical `docs/*` and `review/*` branches map to already merged response, audit, or archival PRs. They are not separate new results.

## Scientific boundaries retained

- The pure-vector Blinov Fig. 7 reproduction remains **not passed** at the 10 MeV strong-absorption end; this audit does not change that status.
- PR #84 does not turn a local total-scattering optical depth into an absorption-only transport solution or an SN cooling limit.
- PR #85 is a separately scoped two-VEV extension and does not alter the original one-VEV manuscript model.
- Neither PR #84 nor PR #85 modifies the manuscript or referee-facing response.

## Repository workflow

Future research integrations should start from current main, use a focused clean branch, preserve native calculation outputs and provenance, and submit a PR. Do not merge stale divergent branch histories wholesale merely to eliminate `ahead_by` counts. CI is optional and is not a prerequisite for research execution or integration.
