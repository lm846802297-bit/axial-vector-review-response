# Axial stellar-cooling independent-review package

**Prepared:** 2026-11-13  
**Pinned calculation source:** `81d9b2faf16eb39879b759b05afce46732c925d7` (`main`)  
**Review branch:** `research/stellar-cooling-review-package-20261113`

## Download and decode

The review bundle is stored as a Base64 text asset so it can be preserved through the repository file API without changing its binary bytes. Download:

`review_bundle_2026-11-13.zip.b64`

On Windows PowerShell, decode it to the actual ZIP:

```powershell
$b64 = Get-Content .\review_bundle_2026-11-13.zip.b64 -Raw
[IO.File]::WriteAllBytes(
  ".\review_bundle_2026-11-13.zip",
  [Convert]::FromBase64String($b64)
)
```

On Linux/macOS:

```bash
base64 -d review_bundle_2026-11-13.zip.b64 > review_bundle_2026-11-13.zip
```

Then extract the ZIP normally. The top-level archive contains the full calculation report plus four nested ZIPs. Extract each nested ZIP to obtain its files.

## Contents

1. `01_sources_profile_report.zip`: production code, profile extraction code, reconstructed SFHo-18.8 profile, all profile-curve vertices and provenance.
2. `02_scans_and_validation.zip`: axial/vector/endpoint scans, convergence scans, sensitivity scans and numerical-validation JSON.
3. `03_figures_and_vector_reference.zip`: existing PDF/PNG figures, luminosity diagnostic, independent literal Blinov reference implementation and comparison inputs/results.
4. `04_tests_and_audits.zip`: tests, polarization/detailed-balance audits, vector benchmark audit and supporting 10-MeV follow-up records.
5. `AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md`: full calculation chain, formulas, numerical settings, results, caveats and reviewer checklist.

Every nested archive contains `SHA256SUMS_AND_GIT_BLOBS.txt`, with SHA-256 checksums and the corresponding Git blob SHA-1 for each included file. The top-level archive includes checksums for all four nested archives and the report. The separate `review_bundle_2026-11-13.zip.sha256` file records the SHA-256 of the complete decoded ZIP.

## Scientific status

This is a fixed-profile, mode-resolved axial-EFT ballistic-cooling benchmark. It is **not** presented as a final SN1987A exclusion. The pure-vector Blinov Fig. 7 10-MeV strong-absorption discrepancy remains unresolved; the mode-resolved versus scalar-opacity prescription and the moving-muon semi-Compton thermal integral remain open physics gates. See the full report before interpreting the contours.

No restricted Garching raw simulation data are included. The profile is reconstructed from public paper figures with pinned provenance.

## Packaging boundary

The archive is assembled from the committed source and outputs at the pinned main revision above, plus the dated review report. Packaging does not regenerate the PDF/PNG, alter the saved scan JSON, rerun the physical calculation, or claim new test execution. It is an evidence-preserving handoff for independent review.
