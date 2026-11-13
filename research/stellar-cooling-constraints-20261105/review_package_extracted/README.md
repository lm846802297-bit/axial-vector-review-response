# Axial stellar-cooling review package — extracted files

This directory is an individually extracted, checksum-verified review snapshot. No ZIP or Base64 archive container is required.

## Provenance
- Repository: lm846802297-bit/axial-vector-review-response
- Numerical source baseline: 81d9b2faf16eb39879b759b05afce46732c925d7
- Source branch: research/stellar-cooling-review-package-20261113
- Source commit: 48bbe212d9a239b9e23bc45d455302b1f8fdcec1
- Profile inputs are reconstructed from public paper figures; no restricted Garching raw simulation tables are included.

## Contents
Production axial EFT rates, transport, scan, profile, plotting and validation code; reconstructed SFHo-18.8 profile and provenance; axial/vector/endpoint scans; convergence/refinement/sensitivity outputs; numerical validation JSON; figures; independent literal Blinov vector reference implementation and comparison inputs; tests and detailed-balance/equation-chain/profile/opacity diagnostics; and the full calculation/review report.

## Reproduction
Python 3 with NumPy, SciPy and Matplotlib is required. Profile extraction additionally requires PyMuPDF. No version-pinned environment lockfile was present.

From the repository root, run:
python -m unittest discover -s research/stellar-cooling-constraints-20261105/review_package_extracted -p "test_*.py" -v
python research/stellar-cooling-constraints-20261105/review_package_extracted/run_scan.py --mass-count 68 --nr 88 --ne 180 --na 24 --ns 64 --nc 40 --gmax 1e-3 --gcount 301 --output research/stellar-cooling-constraints-20261105/review_package_extracted/outputs/axial_reproduced.json
python research/stellar-cooling-constraints-20261105/review_package_extracted/run_scan.py --mass-count 68 --nr 88 --ne 180 --na 24 --ns 64 --nc 40 --current vector --gmax 1e-3 --gcount 301 --output research/stellar-cooling-constraints-20261105/review_package_extracted/outputs/vector_reproduced.json
python research/stellar-cooling-constraints-20261105/review_package_extracted/validate_outputs.py
python research/stellar-cooling-constraints-20261105/review_package_extracted/plot_constraints.py

## Scientific status
This is a reproducible fixed-profile ballistic-cooling benchmark, not a final SN1987A exclusion. The pure-vector Blinov Fig. 7 validation gate remains NOT PASSED at the 10 MeV strong-absorption tail. Numerical convergence and software consistency are not physical validation; the unshaded area is not a demonstrated globally allowed region.

The historical package-parts note and per-part SHA-256/Git-blob records are preserved in package_metadata/. The historical 221-test validation report and machine-readable summary are also included there. The original stdout/stderr logs were not retained. See PACKAGE_EXTRACTION_MANIFEST.json and SHA256SUMS.txt for extraction provenance and file hashes. The repository-level rerun entry point is research/stellar-cooling-constraints-20261105/run_review_validation.py; its future output must be associated with the exact execution commit it records.
