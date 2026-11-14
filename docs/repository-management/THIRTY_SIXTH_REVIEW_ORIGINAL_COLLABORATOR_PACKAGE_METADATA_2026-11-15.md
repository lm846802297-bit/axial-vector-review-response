# Individual review: original collaborator-package metadata

Review date: 2026-11-15. Scope: the eight next pending metadata/requirements records under the 2026-11-13 stellar-cooling collaborator archive.

| Document | Outcome | Findings |
|---|---|---|
| `research/stellar-cooling-collaborator-archive-20261113/provenance/original-review-package/ORIGINAL_REQUIREMENTS.txt` | `HISTORICAL` | This is the unpinned direct-dependency list preserved from the original collaborator package. Its four entries (NumPy, SciPy, Matplotlib, PyMuPDF) are consistent with its stated purpose; it is not the environment specification for the newer archive handoff. |
| `.../package_metadata/part_01_sources_profile_report_README.txt` | `HISTORICAL` | The description correctly points to the full calculation/review report in the top-level research package; that report exists at `research/stellar-cooling-constraints-20261105/AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md`. |
| `.../package_metadata/part_04A_source_tests_reference_GIT_BLOB_SHA_AND_SIZES.txt` | `HISTORICAL` | All 12 listed Git blob SHA values and byte sizes match their files at the pinned source commit `81d9b2faf16eb39879b759b05afce46732c925d7`. |
| `.../package_metadata/part_04A_source_tests_reference_README.txt` | `HISTORICAL` | The stated source pin matches the exact commit used for the 12-file manifest. The current `blinov_reproduction/README.md` has since evolved; its mismatch against the old manifest is expected and disappears when checked at the pinned commit. |
| `.../package_metadata/part_04B_reference_diagnostics_and_audits_GIT_BLOB_SHA_AND_SIZES.txt` | `HISTORICAL` | All 12 listed Git blob SHA values and byte sizes match their files at the same pinned source commit. This includes the independent benchmark/audit notes and six JSON outputs. |
| `.../package_metadata/part_04B_reference_diagnostics_and_audits_README.txt` | `HISTORICAL` | The description correctly identifies the independent vector benchmark diagnostics and detailed physics validation records and carries the same source pin. |
| `.../package_metadata/part_04C_reference_helpers_README.txt` | `HISTORICAL` | The description identifies additional reference-test/benchmark helpers. No Part 04C-specific SHA/size manifest is present in this metadata directory, so this README is descriptive only and does not make a file-integrity claim. Canonical files remain in the main research tree/catalog. |
| `research/stellar-cooling-collaborator-archive-20261113/requirements-review.txt` | `PASS_WITH_NOTES` | The newer reproducibility environment adds version ranges and test/acceleration dependencies (pytest and numba) to the original unpinned runtime list. Added comments clarifying the distinction and the Python 3.11 recommendation from the archive README. |

## Verification detail

- Part 04A: 12/12 blob hashes and 12/12 byte sizes match at the pinned commit.
- Part 04B: 12/12 blob hashes and 12/12 byte sizes match at the pinned commit.
- A comparison against the current maintenance branch initially showed one expected Part 04A README mismatch: the current README is 24,595 bytes, while the pinned package version is 21,774 bytes. Fetching the same path at the declared source commit restores the expected blob SHA and exact 21,774-byte size.
- The pinned commit `81d9b2faf16eb39879b759b05afce46732c925d7` exists in this repository.
- The full calculation report referenced by Part 01 exists at the path stated above.
- The Part 04C README has no companion manifest; no checksum coverage is claimed for that part.
- `ORIGINAL_REQUIREMENTS.txt` is intentionally unpinned historical input. `requirements-review.txt` is the newer bounded environment and includes pytest/numba; these files serve different purposes and are not contradictory.

## Updated register

- `PASS`: 2
- `PASS_WITH_NOTES`: 143
- `HISTORICAL`: 75
- `REVISION_REQUIRED`: 8
- `PENDING`: 234
- Individually reviewed: 228 / 462

No source code, physics output, collaborator archive payload or original package metadata was modified. Only the current `requirements-review.txt` received explanatory comments.
