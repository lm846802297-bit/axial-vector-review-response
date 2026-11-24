# Repository structure and navigation

This document describes the current repository organization and the intended ownership of each area. It is an organizational map, not a claim that every file has passed scientific review. Shared governance and document-review requirements are defined by the pinned central standards in [research/standards-lock.yaml](../../research/standards-lock.yaml).

The 90th-review closeout integration was merged via [PR #122](https://github.com/lm846802297-bit/axial-vector-review-response/pull/122) on 2026-11-22; PR #129 and #130 completed status reconciliation. The B.13/B.16 first-batch integration was subsequently merged via [PR #140](https://github.com/lm846802297-bit/axial-vector-review-response/pull/140) at `871c9c57feb36ea0df549550bb4c307dacadb8cd`, superseding PRs #121, #133 and #134. The separate Croon/Lai vector benchmark was merged via [PR #123](https://github.com/lm846802297-bit/axial-vector-review-response/pull/123); its C1 10 MeV result remains a pure-vector, partial-scope benchmark, with the outer 25–100 km semi-Compton opacity omitted. The PR #142 review snapshot has 912 Markdown/text files and 140 workflow YAMLs; the supplemental register has 450 entries (205 PASS_WITH_NOTES, 6 HISTORICAL, 240 PENDING, 3 REVISION_REQUIRED). Seven of the 26 new Croon/C1 documents have been reviewed as PASS_WITH_NOTES and 19 remain PENDING. The 92nd and 93rd reviews each inspected five RC-001 validation outputs. Four records from the 92nd review remain PENDING pending fresh execution provenance. In the 93rd review, four exact source reruns passed with byte-identical stdout; the Q8 output, P1.5c direct-singlet color-projection output, and UV-triangle Ward output remain REVISION_REQUIRED. The 95th review executed five sources; the Ward source passes in corrected routing, but its archived output retains an earlier contradictory sign PASS that must be explicitly retired. The 96th review executed four more sources with byte-identical output; one hard-degree-five integrand record remains PENDING because its producer script was not located. The mixed-kinetic threshold coefficient is supported by its companion analytic vacuum-polarization derivation; the paired script checks the trace/log identities. The 93rd and 94th reviews executed ten exact source scripts; eight outputs now have byte-identical reruns and PASS_WITH_NOTES dispositions. All 15 new workflows have received individual static review and are recorded as REVIEWED_WITH_NOTES. The 91st supplemental review individually dispositioned five older pending documents. The Fig. 7 +92.4284% discrepancy and Croon outer-opacity discrepancy remain open.

## Canonical top-level layout

The active Major 2 / Major 3 / Major 4.2 script relocation is documented in [ACTIVE_SCRIPT_RELOCATION_AUDIT_2026-11-17.md](ACTIVE_SCRIPT_RELOCATION_AUDIT_2026-11-17.md) and its [path/blob manifest](ACTIVE_SCRIPT_RELOCATION_MANIFEST_2026-11-17.csv).

The 2026-11-17 root-file relocation and directory entry points are recorded in [the relocation audit](ROOT_RELOCATION_AUDIT_2026-11-17.md) and [its blob/size manifest](ROOT_RELOCATION_MANIFEST_2026-11-17.csv).

| Path | Responsibility | Rules |
|---|---|---|
| `README.md`, `README-先读这里.md` | Project entry points | Keep short; link to authoritative sources rather than duplicating status. |
| `仓库分类索引.md` | Repository classification and reading map | Navigation only; live status is in `PROJECT_STATUS.md`, scientific workstream authority is in `research/MAIN_RESEARCH_INDEX_2026-11-13.md`; keep path links current. |
| `AGENTS.md` | Mandatory contributor/agent rules | Normative project instructions plus links to the pinned central standards. |
| `research/standards-lock.yaml` | Adopted central standards revision | Full central commit SHA, selected profiles, local extensions, and deviations. |
| `PROJECT_STATUS.md` | Current project status | Single current status source; dated historical snapshots must be labeled. |
| `GIT_MERGE_POLICY.md` | Compatibility entry point to central Git policy | Shared PR/merge requirements are maintained centrally. |
| `research/` | Scientific workstreams, calculations, validation and evidence | Each workstream owns a README, inputs, code, tests, outputs and limitations. |
| `审稿意见-gpt/` | Referee-response analysis, writing rules, meeting records and revision history | Separate reviewer-facing text from internal notes. |
| `deliverables/` | Extracted, directly usable handoff files | Preserve manifests and extraction provenance. |
| `archive/` | Frozen historical packages and snapshots | Read-only unless a new dated snapshot is explicitly created. |
| `overleaf-source/` | Pinned manuscript source snapshots | Treat as source archives; do not silently overwrite. |
| `计算脚本/` | Legacy calculation materials and their audit records | Preserve historical paths until cross-references are migrated. |
| `work/` | Temporary or intermediate working material | Never treat as authoritative without promotion and review. |
| `.github/workflows/` | Reproducible automation | Each workflow must identify its scientific scope, inputs, outputs and acceptance criteria. |

工作流 YAML 保留在 `.github/workflows/`；静态审查报告现集中于 [workflow-reviews](workflow-reviews/README.md)，迁移清单记录原路径和文件哈希。历史工作目录、附件和已停用材料分别见 [work](../../work/README.md)、[附件](../../附件/README.md)、[弃用](../../弃用/README.md)。

## Research workstream rules

1. Keep distinct physical models in separate directories (in particular, original one-VEV and two-VEV extensions).
2. Keep source code, immutable inputs, generated outputs, tests and reports distinguishable.
3. Every numerical result must identify source commit, input provenance, parameter point, command, environment and validation status.
4. Do not overwrite a validated result with an older branch copy or a result produced under different conventions.
5. A passing software test is not equivalent to physical validation or a phenomenological exclusion.
6. Preserve original PDFs, raw source data and historical snapshots; add a reviewed/current pointer instead of silently replacing them.

## Review coverage and reports

- [First-batch B.13/B.16 integration review](FIRST_BATCH_B13_B16_INTEGRATION_REVIEW_2026-11-23.md) — historical review of the 877-document integration checkpoint; PR #140 is now merged. Current PR #123 inventory is reconciled separately in `PROJECT_STATUS.md` and the audit registers.
The merged PR #115 integration review records the retained disposition for the seven baseline `REVISION_REQUIRED` items at the PR #115 review checkpoint, verifies 499 Actions runs across the 14 retained workflow candidates, and reviews the complete 386-file change set: [FINAL_INTEGRATION_REVIEW_2026-11-17.md](FINAL_INTEGRATION_REVIEW_2026-11-17.md).

The original baseline contains 462 Markdown/text documents and is fully dispositioned: 304 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, 0 `REVISION_REQUIRED`, and 0 `PENDING`. The current PR #123 branch contains 907 Markdown/text files (658 `.md`, 249 `.txt`). The supplemental register contains 445 entries: 183 `PASS_WITH_NOTES`, 6 `HISTORICAL`, and 256 `PENDING`. Five older pending documents have been individually reviewed; 237 pre-existing documents remain pending (233 RC-001 archive files and four low-mass axial-vector package documents). The separate C1 high-order SHA256SUMS text manifest is individually registered as `PASS_WITH_NOTES`. Of 26 new Croon/C1 documents, 7 are `PASS_WITH_NOTES` and 19 remain `PENDING`. All 907 paths are registered exactly once. The current tree contains 2,536 Git-tree entries (2,371 files and 165 directories). Baseline reviewed-version fingerprints remain historical metadata; current blob SHA/size fields are reconciled separately. See the [baseline audit register](DOCUMENT_AUDIT_REGISTER.csv), [supplemental register](SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv), and dated review reports:

- [Initial governance and entry review](INITIAL_REVIEW_REPORT_2026-11-14.md)
- [Second review batch](SECOND_REVIEW_REPORT_2026-11-14.md)
- [Third workstream review](THIRD_REVIEW_REPORT_2026-11-14.md)
- [Major 1 derivation review](FOURTH_REVIEW_REPORT_MAJOR1_2026-11-14.md)
- [Referee and neutrino history review](FIFTH_REVIEW_REPORT_REFEREE_NEUTRINO_2026-11-14.md)
- [Major 1 portal reference review](SIXTH_REVIEW_REPORT_MAJOR1_PORTAL_2026-11-14.md)
- [Root-file and build-dependency review](ROOT_FILE_AUDIT_REPORT_2026-11-14.md)
- [Navigation, workflow catalog and reply archive review](EIGHTH_REVIEW_REPORT_NAVIGATION_ARCHIVE_2026-11-14.md)
- [PR template and coherent spectral-area diagnostic review](NINTH_REVIEW_SPECTRAL_AREA_2026-11-14.md)
- [Historical attachment review](TENTH_REVIEW_ATTACHMENTS_2026-11-14.md)
- [Manifest and checksum review](MANIFEST_REVIEW_2026-11-14.md)
- [Legacy calculation-log review](LEGACY_LOG_REVIEW_2026-11-14.md)
- [Root PDF extraction audit](ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md) (supplementary technical audit)
- [Link and relocation audit](LINK_AND_RELOCATION_AUDIT_2026-11-14.md) (supplementary technical audit)

- [B.13 global transport, moving-muon kernel and B.2 convergence review](THIRTY_NINTH_REVIEW_B13_TRANSPORT_AUDITS_2026-11-15.md)
- [B.16 high-energy propagation and GR review](FORTY_SECOND_REVIEW_B16_HIGH_ENERGY_PROPAGATION_2026-11-15.md)
- [B.16 independent B.1 source and B.1+B.2 luminosity review](FORTY_THIRD_REVIEW_B16_INDEPENDENT_B1B2_LUMINOSITY_2026-11-15.md)
- [B.2 polarization and B.13 collision-physics review](FORTY_FOURTH_REVIEW_B13_B2_PHYSICAL_CONTENT_2026-11-15.md)
- [Weak-current tensor, SFHo EOS and recoil-moment review](FORTY_FIFTH_REVIEW_WEAK_TENSOR_EOS_RECOIL_PHYSICS_2026-11-15.md)
- [B.1 energy variables and B.2 lapse-redshift propagation review](FORTY_SIXTH_REVIEW_B2_LAPSE_REDSHIFT_PHYSICS_2026-11-15.md)
- [EOS moving-nucleon response and scattering-opacity review](FORTY_SEVENTH_REVIEW_EOS_MOVING_NUCLEON_COLLISION_PHYSICS_2026-11-15.md)
- [B.16 inner-path, local absorption, radial synthesis and paper cross-check](FORTY_EIGHTH_REVIEW_B16_INNER_PATH_LOCAL_ABSORPTION_2026-11-15.md)
- [B.16 outer-shell and thermodynamic-input records](FORTY_NINTH_REVIEW_B16_OUTER_SHELL_THERMODYNAMIC_INPUTS_2026-11-15.md)
- [B.16 P1-C/P1-D and P1-E/P1-F source records](FIFTIETH_REVIEW_B16_P1C_P1D_P1E_2026-11-15.md)
- [B.16 P1-G/P1-H and P1-IIId composition/source records](FIFTY_FIRST_REVIEW_B16_P1G_P1H_P1IIID_2026-11-15.md)
- [P1-IIId vector/NSE provenance and P1-IIIe-A/B/C2 EOS occupation records](FIFTY_SECOND_REVIEW_P1IIID_P1IIIE_2026-11-15.md)
- [P1-IIIe C3 degeneracy validation, full radial EOS mapping, and P1-IIIa scalar response](FIFTY_THIRD_REVIEW_P1IIIE_C3_P1III_2026-11-15.md)
- [P1-IIIb/P1-IIIc moving-nucleon kernels and P1-I finite-Q literature domain](FIFTY_FOURTH_REVIEW_P1III_MOVING_KERNEL_AND_P1I_Q_DOMAIN_2026-11-15.md)
- [P1-I thermalization, B.2 propagation, gravity and vector benchmark records](FIFTY_FIFTH_REVIEW_P1I_B16_BENCHMARK_RECORDS_2026-11-15.md)
- [B.2 polarization/energy audits and Bollig profile cross-checks](FIFTY_SIXTH_REVIEW_B2_BOLLIG_PROFILE_RECORDS_2026-11-15.md)
- [Bollig Fig. 4, outer profile, B.2 path integral and Fig. 7 records](FIFTY_SEVENTH_REVIEW_BOLLIG_FIG4_EQB2_FIG7_RECORDS_2026-11-15.md)
- [10 MeV Fig. 7 local rates, three-layer transport, Compton method, digitization and redshift records](FIFTY_EIGHTH_REVIEW_FIG7_10MEV_METHOD_DIGITIZATION_BENCHMARK_2026-11-15.md)

The 462-row register covers Markdown/text documents. Root-level TeX, BibTeX, bibliography styles and binary PDFs are additionally covered by the [root-file audit report](ROOT_FILE_AUDIT_REPORT_2026-11-14.md); workflow YAML files are covered by the separate workflow register.

## Status vocabulary

**Review outcome** (what the individual review established):
- `PASS`: all applicable checks completed within the recorded scope.
- `PASS_WITH_NOTES`: usable within scope, with caveats recorded.
- `REVISION_REQUIRED`: actionable content, consistency, citation or formatting issue found.
- `BLOCKED`: cannot validate because required source, data or context is unavailable.
- `HISTORICAL`: retained as historical material; not a current instruction/result.
- `PENDING`: inventory only; no individual content review completed.

**Lifecycle/authority** (a separate property): current authoritative, working draft, superseded, duplicate candidate, archival, or generated. A document may be historically important while still having a revision-required formatting issue; do not conflate lifecycle with review outcome.

## Safe migration policy

Do not move or delete files solely from their names. Before a move, search and update inbound relative links, code imports, workflow paths, LaTeX inputs, scripts, manifests and external handoff instructions. Keep a relocation manifest mapping old path to new path and preserve blob hashes where bytes are unchanged.

- [Portal A2–A3 individual review](ELEVENTH_REVIEW_PORTAL_A2_A3_2026-11-15.md)
- [Legacy EFT calculation and audit artifact review](THIRTY_FIRST_REVIEW_LEGACY_CALCULATIONS_2026-11-15.md)
- [Exact-momentum pole quadrature follow-up](../../research/major1-higgs-scalar-mixing-20261109/POLE_QUADRATURE_TOLERANCE_AUDIT_2026-11-15.md) (supplementary numerical audit)
- [B5 portal RGE/EFT work-record review](THIRTY_SECOND_REVIEW_B5_RGE_EFT_2026-11-15.md)
- [C4-C3/C4-C4 individual archive review](TWELFTH_REVIEW_C4C3_C4C4_2026-11-15.md)
- [C4-C4 research-report review](THIRTEENTH_REVIEW_C4C4_REPORTS_2026-11-15.md)
- [Global-06 individual protocol review](FOURTEENTH_REVIEW_GLOBAL06_2026-11-15.md)
- [Portal A4–A5 output review](FIFTEENTH_REVIEW_PORTAL_A4_A5_2026-11-15.md)
- [Portal A4–A5 research-note review](SIXTEENTH_REVIEW_PORTAL_A4_A5_NOTES_2026-11-15.md)
- [Portal A5b/B5 output review](SEVENTEENTH_REVIEW_PORTAL_B5_OUTPUTS_2026-11-15.md)
- [B5 triplet output review](EIGHTEENTH_REVIEW_TRIPLET_OUTPUTS_2026-11-15.md)
- [B5 triplet research-note review](NINETEENTH_REVIEW_TRIPLET_NOTES_2026-11-15.md)
- [B.16 sensitivity note review](TWENTIETH_REVIEW_B16_SENSITIVITY_2026-11-15.md)
- [Profile provenance and B.2 interpolation review](TWENTY_FIRST_REVIEW_PROFILE_PROVENANCE_2026-11-15.md)
- [Belle II scan logs and metadata review](TWENTY_SECOND_REVIEW_BELLE_SCAN_LOGS_2026-11-15.md)
- [Belle II raw supplement review](TWENTY_THIRD_REVIEW_BELLE_SUPPLEMENTS_2026-11-15.md)
- [Belle II method and detector-input review](TWENTY_FOURTH_REVIEW_BELLE_METHOD_2026-11-15.md)
- [Belle II bounded-recast review](TWENTY_FIFTH_REVIEW_BELLE_RECAST_2026-11-15.md)
- [Historical Belle II scan and recast review](TWENTY_SIXTH_REVIEW_BELLE_HISTORY_2026-11-15.md)
- [Belle II evidence and protocol review](TWENTY_SEVENTH_REVIEW_BELLE_PROTOCOLS_2026-11-15.md)
- [Belle II benchmark mapping review](TWENTY_EIGHTH_REVIEW_BELLE_MAPPING_2026-11-15.md)
- [Pole, scalar and UV RGE output review](TWENTY_NINTH_REVIEW_POLE_AND_RGE_OUTPUTS_2026-11-15.md)
- [Pole and scalar-width research note review](THIRTIETH_REVIEW_POLE_RESEARCH_NOTES_2026-11-15.md)


### Latest document-review batches and targeted follow-ups (2026-11-16)

- [Fifty-ninth review: profile and outer-neutrino audits](FIFTY_NINTH_REVIEW_PROFILE_AND_OUTER_NEUTRINO_AUDITS_2026-11-15.md)
- [Sixtieth review: 10 MeV profile and B.13 audits](SIXTIETH_REVIEW_10MEV_PROFILE_AND_B13_AUDITS_2026-11-15.md)
- [Sixty-first review: moving-muon and vector-to-axial records](SIXTY_FIRST_REVIEW_MOVING_MUON_AND_VECTOR_AXIAL_2026-11-16.md)
- [Sixty-second review: P1-B global convergence and polarization](SIXTY_SECOND_REVIEW_P1B_GLOBAL_AND_POLARIZATION_2026-11-16.md)
- [Sixty-third review: P1-B E1, rescaling and original-UV records](SIXTY_THIRD_REVIEW_P1B_E1_RESCALING_AND_ORIGINAL_UV_2026-11-16.md)
- [Sixty-fourth review: two-VEV and V57 records](SIXTY_FOURTH_REVIEW_TWOVEV_AND_V57_2026-11-16.md)
- [Sixty-fifth review: V57, portal and neutrino records](SIXTY_FIFTH_REVIEW_V57_PORTAL_NEUTRINO_2026-11-16.md)
- [Sixty-sixth review: meeting archive and historical handbook](SIXTY_SIXTH_REVIEW_MEETING_ARCHIVE_AND_HANDBOOK_2026-11-16.md)
- [Sixty-seventh review: current manuals and Major 4.2–4.4 technical audit](SIXTY_SEVENTH_REVIEW_CURRENT_MANUALS_AND_TECHNICAL_AUDIT_2026-11-16.md)
- [Sixty-eighth review: PMNS, portal and scalar-constraint sources](SIXTY_EIGHTH_REVIEW_PMNS_PORTAL_SCALAR_CONSTRAINTS_2026-11-16.md)
- [Sixty-ninth review: final 54 baseline documents](SIXTY_NINTH_REVIEW_FINAL_54_DOCUMENT_AUDIT_2026-11-16.md)
- [Seventieth review: supplemental review-report records](SEVENTIETH_REVIEW_SUPPLEMENTAL_REVIEW_REPORTS_2026-11-16.md)
- [Seventy-first review: Belle II, profile provenance and pole/RGE records](SEVENTY_FIRST_REVIEW_BELLE_PROFILE_POLE_DOCUMENTS_2026-11-16.md)
- [Seventy-second review: Belle II protocol, history and supplement records](SEVENTY_SECOND_REVIEW_BELLE_PROTOCOL_HISTORY_SUPPLEMENTS_2026-11-16.md)
- [Seventy-third review: workflow audit records](SEVENTY_THIRD_REVIEW_WORKFLOW_AUDIT_RECORDS_2026-11-16.md)
- [Seventy-fourth review: final research READMEs and checksum/environment manifests](SEVENTY_FOURTH_REVIEW_FINAL_RESEARCH_READMES_AND_MANIFESTS_2026-11-17.md)
- [Seventy-fifth review: baseline archive reclassification](SEVENTY_FIFTH_REVIEW_BASELINE_ARCHIVE_RECLASSIFICATION_2026-11-17.md)
- [Seventy-sixth review: B.16 escape phase space and 10 MeV Fig. 7 follow-up](SEVENTY_SIXTH_REVIEW_B16_ESCAPE_AND_FIG7_FOLLOW_UP_2026-11-17.md)\n- [Seventy-seventh review: C4-C4 workflow wiring and archival boundaries](workflow-reviews/C4C4_WORKFLOW_REVIEW_2026-11-17.md)
- [Seventy-eighth review: B.2 path and source workflow wiring](workflow-reviews/B2_PATH_WORKFLOW_REVIEW_2026-11-17.md)
- [Seventy-ninth review: outer-profile sensitivity workflow wiring](workflow-reviews/B16_OUTER_PROFILE_SENSITIVITY_WORKFLOW_REVIEW_2026-11-17.md)
- [Eightieth review: muon-profile and neutrino-branch workflow wiring](workflow-reviews/B16_MUON_PROFILE_AND_NEUTRINO_BRANCH_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-first review: B.16 全径向 SFHo EOS 占据数](workflow-reviews/B16_FULL_RADIAL_EOS_OCCUPATION_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-second review: C4 EOS 响应与碰撞核](workflow-reviews/B16_C4_EOS_RESPONSE_AND_COLLISION_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-third review: B.16 路径积分与剖面敏感性](workflow-reviews/B16_PATH_QUADRATURE_AND_PROFILE_SENSITIVITY_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-fourth review: Bollig 图像与缪子密度来源](workflow-reviews/BOLLIG_FIGURE_AND_MUON_DENSITY_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-fifth review: 剖面来源、碰撞积分与 B.2 审计](workflow-reviews/PROFILE_SOURCE_COLLISION_AND_B2_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-sixth review: Fig. 7 源文件与收敛工作流](workflow-reviews/FIG7_SOURCE_AND_CONVERGENCE_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-seventh review: 最后六项 collider、response 与吸收工作流](workflow-reviews/FINAL_COLLIDER_AND_RESPONSE_WORKFLOW_REVIEW_2026-11-17.md)
- [Eighty-eighth review: historical-candidate workflow triage](workflow-reviews/HISTORICAL_CANDIDATE_WORKFLOW_TRIAGE_2026-11-17.md)
- [Eighty-ninth review: Global-02 report count reconciliation](EIGHTY_NINTH_REVIEW_P1B_GLOBAL02_REPORT_COUNT_RECONCILIATION_2026-11-17.md)
- [Historical action plan: seven baseline revision-required records](REMAINING_BASELINE_REVISION_REQUIRED_ACTION_PLAN_2026-11-17.md) — superseded by the 90th review.
- [Ninetieth review: B.16 and repository baseline closeout](NINETIETH_REVIEW_B16_AND_REPOSITORY_BASELINE_CLOSEOUT_2026-11-17.md)
- [Thermal-convergence CSV provenance disposition](THERMAL_CONVERGENCE_CSV_PROVENANCE_2026-11-17.md)
- [B.16 local-rate, escape-phase-space and PR52 archive workflow review](workflow-reviews/B16_LOCAL_RATE_ESCAPE_AND_SCAN_ARCHIVE_WORKFLOW_REVIEW_2026-11-17.md)
- [Thermal-convergence CSV provenance disposition](THERMAL_CONVERGENCE_CSV_PROVENANCE_2026-11-17.md)
- [B.16 local-rate, escape-phase-space and PR52 archive workflow review](workflow-reviews/B16_LOCAL_RATE_ESCAPE_AND_SCAN_ARCHIVE_WORKFLOW_REVIEW_2026-11-17.md)
- [Targeted follow-up: Major 1 endpoint quadrature repair](SIXTY_SIXTH_REVIEW_MAJOR1_ENDPOINT_QUADRATURE_2026-11-16.md) and [independent numerical audit](POLE_QUADRATURE_INDEPENDENT_AUDIT_2026-11-16.md). This follow-up closes three earlier baseline `REVISION_REQUIRED` entries. The sixty-first review follow-up corrected three stale-status/normalization records; the [Wang–Zhang direct-projector audit update](../../research/stellar-cooling-constraints-20261105/finite_mixing/WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md) synchronized its status; the Global-Full interval-1487 report narrative and scalar-source-note math were corrected; and the legacy 2026-10-19 single-loop review is now `HISTORICAL`. At the end of the sixty-ninth review the baseline had 13 `REVISION_REQUIRED`; the subsequent ninth-review follow-up closed one additional documentation entry, leaving 12. These targeted repairs do not replace the numbered 59th–69th review chronology.
