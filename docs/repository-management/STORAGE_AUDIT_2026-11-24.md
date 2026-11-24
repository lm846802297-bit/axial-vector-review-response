# Storage audit — 2026-11-24

**Scope:** read-only baseline and adoption of the central three-tier scientific data storage policy.  
**Repository:** `lm846802297-bit/axial-vector-review-response`  
**Audited branch:** `main`  
**Audited commit:** `871c9c57feb36ea0df549550bb4c307dacadb8cd` (main immediately before PR #141).  
**Decision:** preserve all existing historical data; no bulk migration and no Git LFS conversion in this change.

## 1. Repository baseline

- GitHub repository metadata size: **405,604 KiB = 396.10 MiB**.
- Complete recursive main tree: **2,218 blobs**, **385.20 MiB** summed uncompressed file bytes.
- Recursive tree response was complete (`truncated=false`).
- Files larger than 1 MiB: **27**.
- Files larger than 10 MiB: **8**.
- Files larger than 50 MiB: **2**.
- Files larger than 100 MiB: **0**.
- No root `.gitattributes` or `.lfsconfig` was found; the current tree contains no declared Git LFS configuration at those paths.

The GitHub repository-size metadata and current-tree byte sum measure different things. The tree sum does not include historical-only Git objects or packfile compression and must not be reported as the repository's complete historical object size.

The 2,218-blob inventory above is a frozen snapshot of the stated audited commit, not a live count for later commits. PR #141 added this audit record, and the subsequent Croon/Lai review work added further files. The storage decision below is based on the audited snapshot; later additions should be assessed against the same size thresholds before any storage migration is considered.

## 2. Largest current files

| Path | Size |
|---|---:|
| `research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/sfho_frdm_bin.zip.part-00` | 60.00 MiB |
| `research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/sfho_frdm_bin.zip.part-01` | 60.00 MiB |
| `research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/sfho_frdm_comp.zip` | 43.23 MiB |
| `research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/sfho_frdm_bin.zip.part-02` | 33.63 MiB |
| `research/radial-scalar-collider-recast-2026-10-28/data/derived/recast-pr52-thetaR-1e-2/belleii_4mu_bounded_width_uv_recast.csv` | 32.99 MiB |
| `research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/sfho_frdm_spp.zip` | 26.93 MiB |
| `research/radial-scalar-collider-recast-2026-10-28/data/derived/scan-pr52-thetaR-1e-2/original_uv_width_scan.csv.gz` | 19.22 MiB |
| `research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/results/P1B_10MeV_LOCAL_KERNEL_ARCHIVE_2026-11-17/p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json` | 10.39 MiB |

The SFHo/FRDM files are already stored as explicitly segmented archive parts, with an adjacent package README and original checksum/provenance records. The derived collider-recast CSV/GZ files and local-kernel JSON are existing scientific outputs. These are not disposable build products.

## 3. Storage-tier decision

### Ordinary Git — retain existing records

Keep source code, scripts, manifests, provenance, validation reports, small/medium native CSV/JSON outputs, and current historical archives in their existing paths.

Retain the existing SFHo/FRDM segmented input files and derived scientific outputs unchanged. They are below GitHub's 100 MiB ordinary-Git per-file hard limit, and their current paths are referenced by project records. Their size is a reason to monitor future growth, not a reason to rewrite history or migrate them now.

### Git LFS — not enabled in this audit

No existing path was identified as an active LFS pointer, and no root LFS configuration was found. Do not introduce LFS merely to reduce the apparent repository size. Evaluate LFS prospectively for a new large binary dataset that must be versioned with the project and whose retrieval remains practical. Any future adoption requires a dedicated PR, remote retrieval verification, and byte-level SHA-256 checks.

### External object storage — not configured in this audit

Use a durable external object store prospectively for bulk scans, very large raw outputs, or long-term datasets whose volume/access pattern makes Git and LFS unsuitable. Keep immutable object/version identity, URI, byte size, source, SHA-256, retrieval instructions, and retention responsibility in a repository-side manifest.

## 4. Integrity and migration boundary

- No existing file was modified, deleted, recompressed, split, or moved.
- No Git history was rewritten.
- No scientific calculation was rerun.
- This audit used GitHub tree/blob metadata to establish the current snapshot. It did not perform a local full-clone historical-object attribution or independently recompute SHA-256 for every large existing file.
- Existing per-package manifests and checksums remain authoritative for their respective historical datasets; this policy-adoption PR does not claim to revalidate them.

## 5. Standards adoption

The downstream lock pins central commit `14155487afc075d301fa7f6cf452c7bff137e869`, which includes central PR #42's Git / Git LFS / external object storage policy. Existing adopted profiles and project-specific extensions are preserved. `standards_release` remains null because no semantic-versioned release for the complete central standards set has been published.

## 6. Conclusion

The repository is substantially larger than the other audited downstream research repositories, but the current files have traceable scientific roles and are below the ordinary-Git hard per-file limit. **Preserve the current repository history and data in place. Do not perform a bulk LFS migration.** Apply the three-tier policy to future additions and reassess only when a concrete file-size, clone-performance, retention, or access problem appears.
