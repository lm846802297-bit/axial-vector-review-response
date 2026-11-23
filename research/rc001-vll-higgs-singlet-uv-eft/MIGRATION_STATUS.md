# RC-001 upstream archive migration

**Archive import status:** COMPLETE  
**Integration/review status:** IN PROGRESS — draft PR #135  
**Source repository:** https://github.com/lm846802297-bit/high-energy-theory-research  
**Frozen source main:** `b2dd8f7e4427d0292bc299d273c780c05021fdab`  
**Target branch:** `migration/rc001-rehome-20261123`

## Canonical location

The exact source-relative tree is mirrored under:

`research/rc001-vll-higgs-singlet-uv-eft/upstream/<original-source-path>`

The imported source set contains 480 files (14,283,294 bytes) across `research/`, `calculations/`, `validation/`, `artifacts/`, and three RC-001-specific workflows. The original source directory hierarchy is retained.

## Remote read-back verification

Compared every frozen source path with its mapped destination path in the target branch:

- Source paths: 480
- Destination paths present: 480
- Missing paths: 0
- Git blob SHA mismatches: 0
- File-size mismatches: 0
- Total source bytes: 14,283,294
- Total mapped destination bytes: 14,283,294

All 480 files match exactly by Git blob SHA and size. The four content-identical paths already present in the target repository were reused without duplicating blob content.

## Repository integration still pending

1. Audit relative Markdown links within the mirrored snapshot. Links to shared infrastructure documents should resolve to the canonical central repository or be represented by explicit navigation stubs; do not alter the byte-identical source snapshot.
2. Audit scripts, test fixtures, and workflow path dependencies. The three imported workflow YAML files are archival snapshots under `upstream/.github/workflows/`; GitHub Actions does not execute workflows from this nested path.
3. Confirm the target index and `RC001_UPSTREAM_INTERFACE.md` point to the local snapshot. The interface file links to the local archived files while retaining old source commit/PR URLs only as historical provenance.
4. Run the relevant path/link and repository tests against the exact final PR head.
5. Review and merge PR #135 before any source cleanup.

## Unmerged source work

Source PR #9 and PR #14 were open at migration time and are not part of the frozen source `main` snapshot. Their proposed changes remain separate review work and are not represented as merged research results.

## Scientific boundary

This is an archival and repository-organization change. No physics calculation has been rerun, modified, or newly validated. Existing scientific claim statuses remain unchanged. The active Major 1 calculations remain separate from the imported snapshot.
