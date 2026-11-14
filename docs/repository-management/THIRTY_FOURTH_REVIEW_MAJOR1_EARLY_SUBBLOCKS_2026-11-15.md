# Individual review: Major 1 early subblocks and fermion-sector records

Review date: 2026-11-15. Baseline branch: `maintenance/repository-organization-audit-20261114`. This batch reviewed the next six pending baseline documents in register order and repaired two already-reviewed navigation/evidence files where concrete rendering defects were found.

| Document | Outcome | Review findings |
|---|---|---|
| `research/major1-higgs-scalar-mixing-20261109/B5_2B1_GAUGE_PARAMETER_AND_CURRENT_BASIS_2026-11-11.md` | `PASS_WITH_NOTES` | The simple-pole combinations follow from the stated y, lambda and M_E counterterms: delta C5/C5 = delta y/y + delta lambda/lambda - delta M_E/M_E; delta CLD/CLD = 2 delta y/y - 2 delta M_E/M_E; and delta CRD/CRD = 2 delta lambda/lambda - 2 delta M_E/M_E. An independent SymPy derivation reproduces the displayed C5, CLD and CRD residues and the factor-of-two beta coefficients. The Pauli completeness identities underlying the current map were independently checked. The script and seven-test module exist. The test module itself was inspected but not freshly executed; its matrix identities do not constitute a complete spinor-level EOM derivation or a full gauge-loop calculation. The document correctly labels these as parameter-only pieces and keeps the full BB/WW/A'A', EFT insertion, mixed B-A', UV/IR and Ward/Slavnov–Taylor work open. |
| `research/major1-higgs-scalar-mixing-20261109/C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md` | `PASS_WITH_NOTES` | The Schur complement gives m_l = -y_l lambda_l v_h v_s/(2 M_E), consistent with C5 = -y_l lambda_l/M_E under the displayed EFT sign. An exact rational check independently reproduces the sign. The rephasing discussion is covariant. The D-plus equals D-minus, raw-F sign flip, invariant commutator curvature and gauge-EOM sign dictionary are internally consistent. The source and seven-test module are present. Coverage limitation: some tests assert the declared sign map rather than derive a complete gauge-fixed Feynman-rule set; the note explicitly disclaims a loop or FeynArts/FeynCalc validation. |
| `research/major1-higgs-scalar-mixing-20261109/CALCULATION_PROTOCOL.md` | `PASS` | The protocol cleanly separates frozen conventions, full-theory/EFT matching, propagator/pole work, validation gates and evidence labels. It explicitly prevents selected diagram subsets or intermediate mixing diagnostics from being reported as physical matched observables. No stale or contradictory instruction was found. |
| `research/major1-higgs-scalar-mixing-20261109/EXISTING_WORK_AUDIT.md` | `HISTORICAL` | The evidence ledger accurately distinguishes fermion/scalar subcalculations from complete UV-EFT matching and physical poles. It is a dated baseline snapshot, not a current task list. Repaired a malformed RC-001 convention display, restored inline math delimiters and corrected a duplicated section number (§8 to §9). Its quantitative and scope statements were retained; no scientific result was changed. |
| `research/major1-higgs-scalar-mixing-20261109/FERMION_SECTOR_INDEPENDENT_AUDIT_2026-11-09.md` | `HISTORICAL` | The audit correctly states that the five tests are regression/consistency checks, not an independent implementation, and explicitly withholds gauge independence, full pole/residue and line-shape claims. Its next-calculation sequence is a dated 2026-11-09 snapshot; the current work order is in the Major 1 README. |
| `research/major1-higgs-scalar-mixing-20261109/FERMION_SECTOR_MATRIX_AUDIT_2026-11-09.md` | `HISTORICAL` | The script, JSON output and test log are present. Parsed JSON values reproduce the document's A/B hard momentum differences, absorptive matrices and eigenvalues. The archived test log reports five tests passing. These are same-implementation regression tests, not independent numerical validation; the document correctly limits the result to the mu/tau+VLL fermion sector and disclaims physical poles/residues/observables. |

## Repairs to already-reviewed navigation/evidence files

### Major 1 README

- Repaired two A3a display equations whose delimiters were literal square brackets rather than proper display-math delimiters.
- Restored the missing inline math delimiters in the A3a prose.
- Added a B5-2B1 section linking the note, SymPy audit script and test module, with the parameter-pole/current-map results and the explicit incomplete-matching boundary.
- The exact referenced fermion-matrix JSON and test-log paths were confirmed to exist. The JSON agrees with the reported A/B values; the log records five tests passing.

### Existing-work audit

- Added an explicit historical-snapshot notice and directed readers to the live Major 1 README/PROJECT_STATUS.
- Corrected the broken RC-001 EFT-sign equation and inline math.
- Renumbered the duplicate section heading.

## Independent algebra checks

An independent SymPy calculation reproduced the displayed C5, CLD and CRD parameter-pole combinations and verified the Pauli singlet/triplet completeness identities. An exact rational Schur-complement check gives C5 = -y lambda/M_E; the v6 printed positive coefficient yields the opposite signed mass under the displayed convention.

## Updated baseline register

The register remains 462 documents. After this batch:

- `PASS`: 2
- `PASS_WITH_NOTES`: 138
- `HISTORICAL`: 66
- `REVISION_REQUIRED`: 8
- `PENDING`: 248
- Individually reviewed: 214 / 462

No physics script, numerical production output, manuscript or referee response was changed or rerun in this batch. The algebra checks above are independent symbolic checks; they are not a substitute for the outstanding complete gauge-loop matching, Ward/Slavnov–Taylor closure, full propagator and physical-pole calculation.
