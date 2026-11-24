# RC-001 — VLL–Higgs–Singlet UV–EFT archive

**Role:** frozen source archive for the general RC-001 UV–EFT matching workstream.  
**Archive status:** complete; exact remote read-back verified.  
**Scientific status:** unchanged from the source records; this archive does not assert full model-level matching completion.

## Canonical entry points

- [Original research index](upstream/research/README.md)
- [Master RC-001 research record](upstream/research/RC-001-vll-higgs-singlet-uv-eft.md)
- [Claim–evidence matrix](upstream/research/RC-001-claim-evidence-matrix.md)
- [Gauge-subgraph subrecord](upstream/research/RC-001-gauge-subgraph-change-record.md)
- [Calculation scripts](upstream/calculations/)
- [Validation records](upstream/validation/)
- [Historical v66 source bundle](upstream/artifacts/higgs-portal-v66-20261019/)
- [Migration status and integrity report](MIGRATION_STATUS.md)
- [Model-application interface](../major1-higgs-scalar-mixing-20261109/RC001_UPSTREAM_INTERFACE.md)

## Frozen provenance

The archive mirrors `high-energy-theory-research` main commit:

`b2dd8f7e4427d0292bc299d273c780c05021fdab`

It contains 480 files and 14,283,294 bytes. All 480 mapped destination paths were read back from GitHub and matched the frozen source by Git blob SHA and file size.

The source-relative layout is retained under `upstream/`. This keeps the original research, calculations, validation, artifacts, and workflow paths stable without overwriting the active Major 1 calculations.

## Scope boundary

- The `upstream/` subtree is an archival snapshot, not an active working directory.
- Its three workflow YAML files are preserved as source artifacts; nested workflows are not active GitHub Actions workflows in this repository.
- PR #9 and PR #14 from the source repository were open at migration time and are not included in the frozen `main` snapshot.
- Use the model-application interface before transferring any archived result into the active Major 1 scalar two-point calculation or manuscript.
- No calculation was rerun and no scientific validation status was changed by this migration.


## Local verification artifacts

The `verification/` directory contains scoped, independently reproducible review checks and their native text outputs. These files are separate from the frozen `upstream/` import and do not modify production calculation sources or archived upstream results.

- `verification/RC-001-QLD-degree5-target-regression.py` and `.txt`: independent regression of the corrected scalar-degree selection, shifted light/heavy propagator expansions and d-dimensional angular-pairing structure counts. It does not repeat the production radial master integrations or hard-soft matching.
- Each verification artifact is tied to the exact upstream producer Git blob and its runtime/output fingerprints in the dated repository review report.
