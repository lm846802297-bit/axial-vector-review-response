# Research Records

简体中文版本：[README.zh-CN.md](README.zh-CN.md)。

This directory contains active Scientific Diff records for substantive research tasks. Each record distinguishes the calculation that has been performed from the checks that have actually run and the physical claims that remain unresolved.

**Project hierarchy:** these records currently document the vll-higgs-singlet-uv-eft workstream within the parent research project axial-vector-model-building. The workstream is not a separate top-level project. See the [project registry](../projects/README.md). RC-001 remains a research-change/record ID; the gauge-subgraph record is a linked subrecord. Existing paths are intentionally unchanged during Phase A.

## Active records

| ID | Research task | Status | Current conclusion |
|---|---|---|---|
| [RC-001](RC-001-vll-higgs-singlet-uv-eft.md) | VLL–Higgs–Singlet UV–EFT one-loop matching: baseline and evidence-chain consolidation | Verification in progress | The exact mass-basis h–s kernel and local pole counterterm for the stated EFT bubble-plus-contact subset are documented. The kernel script passes 15 symbolic checks; the source-aligned §252 off-shell/EOM reproduction passes 46 exact-rational checks; and the §301 coefficient audit passes 5 checks. The historical 4/3 difference between the two-point result and the legacy on-shell four-point representative is reconciled for the specified Yukawa-box sector by the off-shell/EOM completion in master source v153 §§252 and 301.1–301.4. Full model-level Wilson-vector closure, higher-dimensional EFT soft/source insertions, and dimension-eight hard matching remain open. The (C_5^2) soft-potential constant pole is assigned to (X^2Y^2) in the master source's pure-potential representative and independently checked here; this is not the complete dimension-eight Wilson vector. Master §243.4 shows the (Q_{LD},Q_{RD}) VEV wavefunction insertions into the restricted (C_5^2) bubble begin at (O(M_E^{-4})) at fixed VEV, but other coupling sectors and possible IR enhancement remain to be checked. Independent diagram-level validation also remains open. The expanded [EFT soft-topology census](RC-001-eft-soft-topology-census.md) classifies 26 candidate scalar, fermionic, current/source, and dimension-eight topology families, including crossed C5 C5* two-fermion/two-scalar and four-fermion channels and same-order Q6-plus-quartic/gauge corrections. The analytic soft-loop note (RC-001-dim6-soft-loop-integrals-and-checks.md) and SymPy cross-check script (calculations/RC-001-dim6-soft-loop-crosscheck.py) now document 41 exact checks, including independent Feynman-parameter reproduction of the crossed-current and Q6-plus-quartic hard coefficients, crossed-current and four-fermion hard/soft cancellation, and the Q6-plus-quartic EOM kernel. This remains integral-level evidence only: external diagram-package validation, the full gauge/counterterm set, the common-basis EOM/source vector, and complete dimension-eight hard/soft matching remain open. See the [RC-001 claim–evidence matrix](RC-001-claim-evidence-matrix.md). |

| [RC-001-GAUGE-SUBGRAPHS](RC-001-gauge-subgraph-change-record.md) | Dimension-six gauge corrections to \(Q_{LD}\), \(Q_{RD}\), and current/source operators | Verification in progress | Heavy-line and selected scalar master-integral subblocks, the additive \(B-A'\) threshold, signed charge factors for all four conjugate Yukawa vertices, and the (O(M_E^{-2})) cancellation of the complete light-only vertex subfamily are recorded. A conditional mixed B-A' input-parameter counterterm sub-block is also recorded separately from the full mixed-gauge amplitudes. The heavy-containing FF/FS Yukawa-vertex hard sub-blocks are now evaluated; crossed boxes, the full UV–EFT subtraction, Ward identities, and common-basis EOM/source reduction remain open. This is a subrecord of RC-001, not a closed matching result. |

## Rules

- Keep each record tied to an immutable baseline and identifiable artifacts.
- Use stable claim IDs and maintain the claim–evidence matrix.
- Keep live claim rows in a record-specific matrix; leave the generic template free of project-specific claims.
- Do not count Mathematica symbolic checks as FeynArts/FeynCalc diagram-level validation.
- Do not promote a conditional or fixed-sector result into a full-model claim without the missing matching and observable-level steps.
