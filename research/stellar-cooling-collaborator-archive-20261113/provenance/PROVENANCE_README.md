# Original review-package extraction provenance

This directory preserves the *metadata* for the 2026-11-13 independent-review package. It does not contain a second copy of the calculation source tree or any ZIP/Base64 archive.

## Pinned source

- Repository: \`lm846802297-bit/axial-vector-review-response\`
- Original review branch: \`research/stellar-cooling-review-package-20261113\`
- Package source commit: \`48bbe212d9a239b9e23bc45d455302b1f8fdcec1\`
- Numerical source baseline: \`81d9b2faf16eb39879b759b05afce46732c925d7\`
- Preparation date: 2026-11-13
- Original input parts: 12
- Extracted archive members: 75

## Preserved records

- \`PACKAGE_EXTRACTION_MANIFEST.json\`: encoded-part byte counts and SHA-256, decoded ZIP byte counts and SHA-256, member counts, source commit, and numerical baseline.
- \`ORIGINAL_SHA256SUMS.txt\`: original member-level SHA-256 manifest, preserved byte-for-byte. Paths are relative to the original extracted package root.
- \`package_metadata/\`: original part README files and source/test reference records, including Git blob SHA-1 and byte-size information.
- \`ORIGINAL_REVIEW_PACKAGE_README.md\` and \`ORIGINAL_PACKAGE_PARTS_README.md\`: original historical instructions. They describe the old Base64/nested-ZIP delivery mechanism and are retained only as provenance, not as current usage instructions.
- \`ORIGINAL_REQUIREMENTS.txt\`: original package dependency list; the current collaborator package uses \`../requirements-review.txt\`.

## Why the payload is not duplicated

The original 75 archive members were selected from the pinned source tree and are represented by canonical source, data, report, test, and output files elsewhere in the current repository. Those files remain in their normal research directories. The old \`review_package_extracted/\` duplicate tree was retired to avoid maintaining a second mutable copy.

The 12 metadata files preserved here are not byte-identical to files elsewhere in main and are needed to retain the original package-part provenance. No generated ZIP, Base64 shard, or second source-code copy is included.

## Verification

Use \`PACKAGE_EXTRACTION_MANIFEST.json\` to identify the 12 original source parts and \`ORIGINAL_SHA256SUMS.txt\` to verify the 75 original archive members when comparing against a separately retained copy of that historical package. The current collaborator archive has its own fresh \`ARCHIVE_PROVENANCE.json\`, \`SOURCE_FILE_CATALOG.csv\`, and \`SHA256SUMS.txt\` generated locally from its own pinned checkout.

Do not follow the historical Base64 download/decode instructions as the current repository workflow. Current canonical files and local handoff instructions are indexed in \`research/MAIN_RESEARCH_INDEX_2026-11-13.md\` and \`research/stellar-cooling-constraints-20261105/REVIEW_PACKAGE_INDEX_2026-11-13.md\`.
