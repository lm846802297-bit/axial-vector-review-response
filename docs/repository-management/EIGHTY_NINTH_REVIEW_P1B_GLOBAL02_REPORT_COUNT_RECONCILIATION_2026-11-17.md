# Eighty-ninth review: Global-02 report count reconciliation

Date: 2026-11-17  
Branch: `maintenance/repository-organization-audit-20261114`  
Scope: the Global-02 Markdown report and its committed machine-readable summary. This is a documentation/provenance review; no source calculation was run.

## Evidence checked

- `P1B_10MeV_GLOBAL_02_SUMMARY.json`, Git blob `56681fcd09618e13e0727217d81c1738dc1cd744`, records `G2.selected_intervals=60` and `G2.direct_midpoint_evaluations=1080`.
- The Global-02 report previously stated 1,140 direct selected-midpoint evaluations. Its own later addendum noted that the summary JSON does not identify a separate 60-evaluation energy-midpoint subset, so the additional 60 were unsupported.
- The report separately links a later high-order hot-shell refinement. That targeted refinement passes its stated successive-order criterion at the sampled point; it does not establish global high-order quadrature convergence.
- A distinct Global-03 report covers all radial intervals for a low-order sequential-PCHIP interpolation screen. It is not a rerun of Global-02 and does not establish the missing Global-02 count decomposition.

## Correction and disposition

The Global-02 report now uses 1,080, matching the committed summary JSON, and explicitly withdraws the unsupported 1,140 prose total. It makes no claim that an additional 60 energy-midpoint evaluations occurred. The original quadrature orders, selected-interval scope, later hot-shell addendum, and open global-acceptance boundary remain stated.

The baseline register disposition changes from `REVISION_REQUIRED` to `PASS_WITH_NOTES` for record accuracy. This closes the report's internal count inconsistency only. Global interpolation/high-order quadrature acceptance remains open; the record establishes no full-star emissivity, GR optical depth, luminosity, Fig. 7 reproduction, SN1987A limit, or axial-vector constraint.

No workflow, test, or calculation was run. No physics source or numerical output was changed.
