# Baseline revision-required items: action plan

> **Superseded on 2026-11-17.** This was the seven-item action plan at the time it
> was written. The 90th review has now dispositioned all seven records with
> evidence and updated the baseline register to 0 `REVISION_REQUIRED`.
> Retain this file as the historical plan; the current source of truth is
> [the 90th review](NINETIETH_REVIEW_B16_AND_REPOSITORY_BASELINE_CLOSEOUT_2026-11-17.md)
> and [DOCUMENT_AUDIT_REGISTER.csv](DOCUMENT_AUDIT_REGISTER.csv).


Date: 2026-11-17  
Branch: `maintenance/repository-organization-audit-20261114`  
Source of truth: `docs/repository-management/DOCUMENT_AUDIT_REGISTER.csv`  
Scope: the seven baseline documents currently marked `REVISION_REQUIRED`. This plan organizes the missing evidence and completion criteria; it does not change their dispositions.

## Open items

| Priority | Baseline document | Blocking issue | Evidence required to close |
|---|---|---|---|
| 1 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_ESCAPE_PHASE_SPACE_RUNBOOK_2026-11-10.md` | The inspected high-order run failed before writing its canonical JSON because the energy-grid hash differs from the archived baseline. | Reconcile and pin the intended energy grid and source/profile inputs; obtain the canonical JSON; verify the joint-table and marginal closures against the declared tolerances; record the exact run commit, environment, and checksums. A passed syntax check alone is insufficient. |
| 2 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/FIG7_10MEV_LOCAL_RATE_POLARIZATION_ESCAPE_AUDIT_2026-11-13.md` | The report's claimed 10 MeV local-rate/polarization/escape handoff package is absent. The later exact-B.13 package covers only 210–510 MeV and does not replace it. | Commit the actual producer/helper source, pinned inputs, local-rate CSV, JSON, and plot; link each output to its source/profile fingerprints; record polarization and escape conventions and validate the reconstructed package against its own stated gates. |
| 3 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/MUON_CHEMICAL_POTENTIAL_SOURCE_AUDIT_2026-11-07.md` | The public Caputo Fig. 3 does not establish whether plotted (n_mu) means (n_{mu^-}) or net (n_{mu^-}-n_{mu^+}); profile-A/B and common-shell comparisons also need explicit provenance. | Keep both density definitions separate, identify the figure/source convention if primary evidence permits, compare the same vertices/shells with profile fingerprints, and preserve the distinct single-(mu^-) B.17 source convention. Do not rescale the profile to force agreement. |
| 4 | `research/stellar-cooling-constraints-20261105/blinov_reproduction/PROFILE_INPUT_AUDIT_12_15KM_2026-11-09.md` | The audit JSON lacks the profile CSV SHA-256; its density check uses (n_{mu^-}) only while the plotted charge convention remains unknown. | Add the exact profile fingerprint and report both (n_{mu^-}) and (n_{mu^-}-n_{mu^+}) at common vertices, with units and source rows. Retain the figure-convention ambiguity if the public source does not resolve it. |
| 5 | `research/radial-scalar-collider-recast-2026-10-28/data/derived/scan-pr52-thetaR-1e-2/SHA256SUMS.txt` | The compressed current scan and summary hashes are recorded, but the current uncompressed CSV is absent; the old run record describes an earlier output with reversed bound columns. | Extract the exact current archive, compare its decompressed bytes to the declared CSV hash/size, commit the directly usable CSV if size and redistribution terms permit, and update the run record to distinguish the old reversed-column output from the current scan. Preserve the original archive only as needed for provenance. |
| 6 | `research/stellar-cooling-original-uv-model-20261105/validation-results-2026-11-05.md` | The archived CSV uses `relative_*_percent` with order 10 as zero/reference, while the convergence driver at the recorded source commit emits `relative_*_to_reference` using the highest requested order. The width-script blob also changed during archival, although its formula body reportedly matches. | Identify the exact CSV-producing source/run or explicitly withdraw direct-producer attribution; define the CSV reference formula and preserve the values as a separately identified legacy table if its producer cannot be recovered. Record the old/current width-script blob relation and limit Ward residuals to the stated absolute, benchmark-specific convention. |
| 7 | `research/stellar-cooling-two-vev-20261105/validation-results-2026-11-05.md` | The convergence CSV and driver disagree on the reference convention, and (n_{m GL}) and (n_phi) vary together, so azimuthal convergence is not independently isolated. | Identify the exact CSV producer/reference convention; label the joint ((n_{m GL},n_phi)) scan as joint convergence, not independent azimuthal convergence; separate any numerical correction from model-specific results. The Markdown code-fence escaping has been repaired, but this does not close the data-provenance issue. |

## Order and disposition rules

1. Resolve the 10 MeV B.16 artifact/hash blockers before treating that output as a canonical phase-space result.
2. Keep source-profile convention questions separate from numerical normalization; do not infer a density definition from a visually similar curve alone.
3. Treat the two local semi-Compton CSVs as records with unresolved provenance until the producer/reference convention is established. Do not claim their CSV files are direct output of a different driver schema.
4. For the collider scan, follow the repository's extract-before-upload rule and verify the uncompressed artifact bytes before updating its manifest.
5. A disposition can change only when the row-specific evidence is committed and independently checked. This list itself does not promote any result, run a workflow, or alter a scientific conclusion.

No tests, workflows, calculations, profile rescalings, or manuscript edits were performed for this action-plan document.
