# RC-001 upstream archive migration

**Status:** IN PROGRESS — draft PR #135  
**Source repository:** https://github.com/lm846802297-bit/high-energy-theory-research  
**Frozen source main:** `b2dd8f7e4427d0292bc299d273c780c05021fdab`  
**Target branch:** `migration/rc001-rehome-20261123`

## Scope

The source inventory is 480 files (14,283,294 bytes) under `research/`, `calculations/`, `validation/`, `artifacts/`, and three RC-001-specific workflows. The import destination is this workstream's `upstream/` subtree, preserving the original source-relative paths:

`research/rc001-vll-higgs-singlet-uv-eft/upstream/<original-source-path>`

This nested snapshot is intentionally separate from the target repository's existing Major 1 workstream and does not overwrite any of its canonical files.

## Current migration progress

- 79 source blobs were already present in the target repository with identical Git blob SHA and are referenced without duplicate content storage.
- The initial staged PR batch contained five newly imported text files and reused identical blobs.
- Further batches have been imported with exact Git blob SHA checks.
- The import remains partial. Do not treat the target snapshot as complete until every one of the 480 source paths is present at its mapped destination and each destination blob SHA and size matches the frozen source tree.
- Binary files are imported as base64 blobs; text files are imported from the source Git blob API to avoid truncated file-content previews.

## Important path handling

The source's `research/README.md` collides with the target's existing `research/README.md`; it is retained as `research/RC-001-README.md` at the snapshot root only if an index copy is needed. The authoritative complete source tree is kept under `upstream/`, including its own `research/README.md`, so the original relative links resolve inside the snapshot.

## Unmerged source work

Source PR #9 and PR #14 are still open and are not part of the frozen source `main` inventory. Their proposed changes must remain separate and must not be represented as merged results. If needed, archive their exact PR head commits as separate review snapshots after the main snapshot is complete.

## Acceptance gates

1. All 480 paths present under `upstream/`.
2. For every path, destination Git blob SHA equals the frozen source Git blob SHA and file size equals the source tree size.
3. Source-relative links within the mirrored `upstream/` subtree resolve; target cross-repository interface and index links point to the new canonical snapshot.
4. Relevant target tests and workflows are reviewed and run on the exact PR head; workflow path/trigger assumptions are corrected for the nested snapshot or explicitly retained as historical-only.
5. PR #135 is reviewed and merged before any source deletion.
6. Only after merge and remote read-back verification may a separate source-repository PR remove the migrated research-specific files.

No physics calculation is rerun or changed by this archive migration. Software and archive validation are not physical validation.
