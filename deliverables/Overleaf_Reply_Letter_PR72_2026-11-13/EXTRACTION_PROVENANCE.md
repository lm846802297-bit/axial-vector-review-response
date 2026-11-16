# Overleaf package extraction provenance

- Original archive: Overleaf_Reply_Letter_PR72_2026-11-13.zip (removed after extraction)
- Original archive bytes: 777561
- Original archive SHA-256: 6c3d74091df33f316ea01694738a5b2392d9a882576704a7c3690a6569037323
- Source-main revision in original manifest: 3a3e8bb0eeb54a627cf2b2df315edf8badfe1dc8
- Original external manifest is preserved verbatim as ARCHIVE_ORIGINAL_SHA256SUMS.txt.
- SHA-256 of the original embedded SHA256SUMS.txt: 0aa708866c33b47d5d519b9b1ff22af0e001247fb3dcc23d3990c747973dcc92
- Verification: archive size, archive SHA-256, ZIP CRC, and every embedded file SHA-256 matched the original external manifest.
- The current SHA256SUMS.txt covers every extracted file and this provenance record.
- On 2026-11-16, README_Overleaf.md was extended with an explicit historical-only / not-for-final-submission warning and a link to the authoritative root PDF; SHA256SUMS.txt was refreshed for that README (1,845 bytes). ARCHIVE_ORIGINAL_SHA256SUMS.txt remains unchanged and continues to preserve the original archive manifest verbatim.
- All files are committed individually; no ZIP container is retained.

## Independent binary-capable verification (2026-11-16)

- Extraction PR: #94, from `chore/extract-generated-archives-20261113` into `main`; merged 2026-11-13 at commit `2bebb38c7ff8966b048b133d67c1aa7bd37aa496`.
- The original ZIP was retrieved from the extraction commit's parent `0c7136de89ce81f30f9c0d13371e1566c72a760c`. Its actual bytes are 777561 bytes and SHA-256 `6c3d74091df33f316ea01694738a5b2392d9a882576704a7c3690a6569037323`, matching the preserved external manifest.
- All nine entries in the current `SHA256SUMS.txt`, including both PDFs, were independently checked against repository file bytes and declared sizes; all nine match.
- The eight embedded-file hashes in `ARCHIVE_ORIGINAL_SHA256SUMS.txt` were compared with current extracted files: six match. The only differences are `README_Overleaf.md` (updated 2026-11-16 to mark this snapshot historical-only) and `SHA256SUMS.txt` (refreshed for the updated README). The original manifest remains unchanged.
- The original ZIP's byte hash and size were independently verified from the parent commit. ZIP entry CRC is retained as the extraction-time record; this follow-up did not independently rerun decompression/CRC checks.
