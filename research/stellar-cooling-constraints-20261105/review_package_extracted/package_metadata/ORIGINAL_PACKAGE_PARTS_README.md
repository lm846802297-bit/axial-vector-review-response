# Historical package-parts README — archive workflow superseded

**Status:** Historical packaging instructions only. The ZIP/Base64 transfer workflow described in the original version of this file was superseded by PR #94 on 2026-11-13. The current `main` branch contains the individually extracted files under this directory; no ZIP or Base64 shard is required to inspect or use this review package.

Use the parent [README.md](../README.md) as the current entry point. Use [PACKAGE_EXTRACTION_MANIFEST.json](../PACKAGE_EXTRACTION_MANIFEST.json) and [SHA256SUMS.txt](../SHA256SUMS.txt) for extraction provenance and file integrity.

## Historical source-part map

The original package was assembled from disjoint parts covering:

1. Source code, reconstructed SFHo-18.8 profile, profile-curve vertices, and provenance.
2. Axial/vector/endpoint scans, convergence scans, sensitivity scans, and numerical-validation JSON.
3. PDF/PNG figures, luminosity diagnostics, the independent literal Blinov reference implementation, and comparison inputs/results.
4. Tests, polarization/detailed-balance audits, vector-benchmark audits, and supporting 10-MeV follow-up records.

The original source-part names, encoded-text hashes, decoded-archive hashes, byte counts, and member counts are recorded in the extraction manifest. The per-part SHA-256/Git-blob metadata files are retained alongside this note.

## Scientific status

The package remains a fixed-profile, mode-resolved axial-EFT ballistic-cooling benchmark, **not** a final SN1987A exclusion. The pure-vector Blinov Fig. 7 10-MeV strong-absorption discrepancy remains unresolved. No restricted Garching raw simulation data are included; the profile is reconstructed from public paper figures with pinned provenance.
