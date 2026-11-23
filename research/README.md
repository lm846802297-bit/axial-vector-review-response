# Research workstreams

This directory contains the scientific source records, calculations, tests, numerical outputs, literature inputs, and validation reports. It is the primary location for research evidence; the referee-response writing workflow remains under `审稿意见-gpt/`.

## Canonical navigation

- [Main research index — 2026-11-17](MAIN_RESEARCH_INDEX_2026-11-13.md): current workstream map, integration history, acceptance labels and scientific claim boundaries.
- [RC-001 VLL–Higgs–Singlet UV–EFT archive](rc001-vll-higgs-singlet-uv-eft/README.md): frozen 480-file source snapshot, exact Git-blob verified against `high-energy-theory-research` main commit `b2dd8f7e4427d0292bc299d273c780c05021fdab`; kept separate from the active Major 1 scalar two-point calculations.
- [RC-001 model interface](major1-higgs-scalar-mixing-20261109/RC001_UPSTREAM_INTERFACE.md): model-specific map and transfer conditions for the archived UV–EFT calculations.
- [Branch disposition audit](BRANCH_DISPOSITION_2026-11-13.md): branch preservation/deletion decisions.
- [Branch integration audit](BRANCH_INTEGRATION_AUDIT_2026-11-13.md): integration provenance.
- [Branch inventory](BRANCH_INVENTORY_2026-11-13.json): point-in-time branch inventory, not a live branch list.

## Workstream directory map

| Directory | Scope | Boundary / current interpretation |
|---|---|---|
| [major2-parameter-window-20261117/](major2-parameter-window-20261117/README.md) | Major 2 Fig. 2 display-window benchmark and exact axial \(g-2\) integral | Numerical benchmark only; plot endpoints are not universal allowed-region boundaries. |
| [major3-neutrino-response-optional-seesaw-20261117/](major3-neutrino-response-optional-seesaw-20261117/README.md) | Major 3 response-only optional neutrino seesaw construction and charged-lepton/VLL diagnostic | Not part of the original one-VEV manuscript model; no global PMNS/LFV fit or constraint scan. |
| [major4-2-kinetic-mixing-20261117/](major4-2-kinetic-mixing-20261117/README.md) | Major 4.2 momentum-dependent photon–\(A'\) kinetic mixing and conditional NA64 comparison | Equal-angle/matching benchmark with visual-read-off uncertainty; not a detector-level recast. |
| [major1-higgs-scalar-mixing-20261109/](major1-higgs-scalar-mixing-20261109/README.md) | Higgs–singlet scalar mixing, self-energies, counterterms, poles and related fermion-sector audits | Active model-application calculations; keep separate from the frozen upstream RC-001 snapshot and do not treat subcalculation completion as a complete gauge-independent two-pole prediction. |
| [rc001-vll-higgs-singlet-uv-eft/](rc001-vll-higgs-singlet-uv-eft/README.md) | Archived general VLL–Higgs–Singlet UV–EFT derivations, calculation scripts, outputs and validation records | Byte-identical source snapshot only; see [migration status](rc001-vll-higgs-singlet-uv-eft/MIGRATION_STATUS.md) for provenance and dependency audit; use the model interface before transferring any result into Major 1 physical predictions. |
| [radial-scalar-collider-recast-2026-10-28/](radial-scalar-collider-recast-2026-10-28/README.md) | Original-model radial-scalar collider reinterpretation | Keep width, promptness and benchmark assumptions explicit; not a general scalar-sector exclusion. |
| [stellar-cooling-constraints-20261105/](stellar-cooling-constraints-20261105/README.md) | Major 4.4 stellar cooling, supernova rates, transport, Blinov reproduction, EOS/profile provenance and local kernels | Pure-vector Fig. 7 10 MeV strong-absorption physical gate remains NOT PASSED; no final axial limit update is authorized by local checks alone. |
| [stellar-cooling-collaborator-archive-20261113/](stellar-cooling-collaborator-archive-20261113/README.md) | Collaborator-facing reproducibility archive, status matrix, figure audit and review checklist | Read its status matrix and figure audit before interpreting contours. |
| [stellar-cooling-eft-literature-20261105/](stellar-cooling-eft-literature-20261105/README.md) | Literature EFT kernels and independent convention checks | Keep literature-kernel checks distinct from model-specific UV completion. |
| [stellar-cooling-original-uv-model-20261105/](stellar-cooling-original-uv-model-20261105/README.md) | Original one-VEV UV model line | This is the original manuscript model; do not merge assumptions from the two-VEV extension. |
| [stellar-cooling-shared-20261105/](stellar-cooling-shared-20261105/README.md) | Shared infrastructure and reusable microphysics for stellar-cooling studies | Check each module's model applicability before reuse. |
| [stellar-cooling-two-vev-20261105/](stellar-cooling-two-vev-20261105/README.md) | Separate two-VEV axial microphysics extension | Distinct model extension; not a replacement for the original one-VEV manuscript model. |



## Scientific evidence rules

1. Distinguish analytic derivation, code implementation, unit/regression tests, numerical convergence, literature reproduction, transport validation and phenomenological acceptance.
2. Each numerical result must retain exact source commit, input files/checksums, parameter point, command, environment, output and validation report.
3. Keep original one-VEV model and two-VEV extension in separate workstream directories and label all cross-model comparisons.
4. Do not promote a fixed-background local scattering/opacity calculation to a complete SN luminosity or escape-probability result.
5. Preserve historical branches and snapshots when they contain provenance; do not overwrite current-main outputs with older branch copies without a source/input/semantic comparison.
6. Use `PROJECT_STATUS.md` for current repository/PR status and the dated main research index for scientific workstream acceptance boundaries.

## Directory growth policy

New work belongs in an existing workstream directory when it shares the same model, inputs and acceptance criteria. Create a new directory only for a genuinely distinct model, research question or independently reproducible package. Each new workstream must contain a README with scope, source provenance, canonical entry points, reproducibility commands, completed checks, open gates and explicit claim limits.
