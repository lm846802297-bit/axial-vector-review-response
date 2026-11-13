# Axial stellar-cooling independent-review package index

## Package root

The pinned, self-contained review snapshot is stored as ordinary files under:

`research/stellar-cooling-constraints-20261105/review_package_extracted/`

No ZIP, Base64 ZIP, or split archive part is required.

## Included material

- The complete calculation and independent-review report: `AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md`
- Axial EFT production rates, transport, scan, profile, plotting, and validation source files
- Reconstructed SFHo-18.8 profile inputs and provenance
- Axial/vector scans, endpoint checks, convergence and sensitivity outputs
- Saved numerical JSON, CSV data, and figures
- Independent literal Blinov vector-reference implementation and comparison inputs
- Unit tests and detailed-balance, equation-chain, profile, and opacity audits
- `PACKAGE_EXTRACTION_MANIFEST.json`, `SHA256SUMS.txt`, `requirements-review.txt`, and the preserved per-part metadata in `package_metadata/`

The package manifest records the 12 non-overlapping source parts, their original Base64-text SHA-256 values, decoded ZIP SHA-256 values, byte counts, member counts, and extracted-member hashes. The 18 source/profile SHA-256 records and 24 reference/test Git blob SHA-1 records were checked against the extracted files.

## Pinned source and scope

- Numerical source baseline: `81d9b2faf16eb39879b759b05afce46732c925d7`
- Package staging source commit: `48bbe212d9a239b9e23bc45d455302b1f8fdcec1`
- Profile inputs are reconstructed from public paper figures; no restricted Garching raw simulation tables are included.
- The snapshot is kept separately so its pinned baseline is not overwritten by later active-main edits. All 75 extracted member paths also exist in the canonical research tree; this folder preserves the exact review snapshot and per-file provenance.

## Reproduction

Python 3 with NumPy, SciPy, and Matplotlib is required. Profile extraction additionally requires PyMuPDF. See the package README and requirements file for commands and dependencies.

## Scientific status

This is a reproducible fixed-profile ballistic-cooling benchmark, not a final SN1987A exclusion. The pure-vector Blinov Fig. 7 validation gate remains **NOT PASSED** at the 10 MeV strong-absorption tail. Numerical convergence and software consistency are not physical validation. The unshaded region is not a demonstrated globally allowed parameter region.

## Archive policy

The generated ZIP containers were extracted and removed from the repository's main tree. The package is distributed as individual source, data, output, figure, and provenance files. The separate official SFHo/FRDM upstream EOS source archives are retained under the EOS data directory until a verified extracted-table replacement and reader migration are completed.
