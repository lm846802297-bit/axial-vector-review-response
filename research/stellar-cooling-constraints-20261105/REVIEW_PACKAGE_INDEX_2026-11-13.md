# Stellar-cooling review package: repository file map

**Prepared:** 2026-11-13  
**Repository:** `lm846802297-bit/axial-vector-review-response`  
**Review branch:** `research/stellar-cooling-review-package-20261113`  
**Pinned calculation source baseline:** `81d9b2faf16eb39879b759b05afce46732c925d7`

## Storage rule

The repository contains the extracted source files, input data, saved numerical outputs, figures, tests, and audit reports in their normal directory structure. No ZIP, Base64-encoded ZIP, or split ZIP parts for this review package are committed. The user-facing ZIP is built from these extracted files and delivered separately; the workflow artifact has a one-day retention period and is not part of the repository tree.

## Version boundary

The production code and saved axial/vector/endpoint arrays used for the displayed constraint figure are pinned to calculation source commit `81d9b2faf16eb39879b759b05afce46732c925d7`. The review branch is synchronized with current main so that later B.13/B.16 audit reports and diagnostic outputs are also available. Those later diagnostics are supplemental evidence; they do not silently replace the pinned inputs or regenerate the plotted axial contour. The archive's `PACKAGE_FILE_INDEX.csv` records each included file's Git blob SHA and SHA-256.

## Repository locations

| Material | Repository path |
|---|---|
| Main calculation report | `research/stellar-cooling-constraints-20261105/AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md` |
| Main production code | `research/stellar-cooling-constraints-20261105/{rates.py,transport.py,run_scan.py,plot_constraints.py,validate_outputs.py}` |
| Reconstructed profile and provenance | `research/stellar-cooling-constraints-20261105/data/` |
| Axial/vector scans, endpoint, convergence and sensitivity results | `research/stellar-cooling-constraints-20261105/outputs/` |
| Independent pure-vector reference and transport audits | `research/stellar-cooling-constraints-20261105/blinov_reproduction/` |
| Polarization and detailed-balance validation | `research/stellar-cooling-constraints-20261105/POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md` and associated tests |
| Independent matrix-element reference required by the Compton test | `research/stellar-cooling-eft-literature-20261105/` |
| Supplemental moving-muon and finite-mixing calculations | `research/stellar-cooling-constraints-20261105/finite_mixing/` |
| Rescaling diagnostic (not applied to the plotted curve) | `research/stellar-cooling-constraints-20261105/rescaling_audit/` |

## Included numerical evidence

The handoff includes the original axial and vector scan JSON, endpoint scan, radial/energy/angular/path convergence scans, coupling refinement, cutoff and profile sensitivities, luminosity checks, digitization audits, vector comparison tables, mode-resolved detailed-balance checks, independent literal Blinov scans, and B.13/B.16 diagnostic outputs. The package also includes the related Python programs, unit tests, and explanatory audit records.

## Scientific interpretation boundary

The plotted result is a fixed-profile ballistic-cooling benchmark, not a final unconditional SN1987A exclusion. The literal pure-vector Blinov Fig. 7 comparison remains **NOT PASSED** at the 10 MeV strong-absorption endpoint (about +92.24%). The axial baseline still uses the initial-muon-rest/effective-density semi-Compton approximation. The moving-muon thermal kernel is kept as a separate supplemental calculation and is not silently substituted into the plotted scan. The mode-resolved axial transport and scalar-opacity literal reference remain separate.

No empirical opacity rescaling is used. Numerical convergence and passing software tests do not establish physical validation of the reconstructed stellar background or transport prescription.

## Reproduction entry points

From the repository root:

```bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105 -p "test_*.py" -v
python research/stellar-cooling-eft-literature-20261105/check_literature_kernels.py --matrix-script research/stellar-cooling-eft-literature-20261105/reference_matrix_element.py --output research/stellar-cooling-eft-literature-20261105/literature_kernel_validation_reproduced.json
python research/stellar-cooling-constraints-20261105/validate_outputs.py
```

The separate EOS-dependent diagnostics require the public SFHo-FRDM release files identified by their own README and SHA-256 manifest. They are not inputs to the displayed fixed-profile axial contour.
