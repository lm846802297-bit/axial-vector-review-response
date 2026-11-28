# Axial SN1987A physics-audit workstream

This branch isolates the physical validation needed before a new axial-vector supernova parameter scan.

## Current status

- **Step 1 — axial current, Goldstone Ward identity, physical polarizations:** PASS_WITH_NOTES.
- **Step 2 — exact moving-muon semi-Compton local rates:** PASS for local matrix elements and thermal integrals.
- **Step 3 — neutrino inverse decay, Pauli blocking, detailed balance:** PASS.
- **Step 4 — decay widths, reduced opacity, optical depth and escape:** PARTIAL. Local expressions and polarization state counting are checked; the exact moving-muon mode-resolved rates are not yet connected to the radial transport kernel.
- **Step 5 — low-mass pseudoscalar and conserved-vector limits:** PASS_WITH_NOTES.
- **Step 6 — axial parameter scan:** NOT STARTED.

## Main record

See [PHYSICS_AUDIT_STAGES1_TO5_2026-11-26.md](PHYSICS_AUDIT_STAGES1_TO5_2026-11-26.md) for derivations, quantitative checks, source identities, provenance and the acceptance gate.

## New independent calculation

- Source: verification/stage5_pseudoscalar_vector_limit_audit.py
- Native result: verification/outputs/stage5_pseudoscalar_vector_limit_audit.json
- Source SHA-256: 6263b808cada52991d95a41fc40a31ddb306a705c11343a5e0f2cbac903520d7
- Native-output SHA-256: 1224735e0f7e08db97aa08f5bf1e94b8e080f80dfb2ebb27a9aa21e1e32acdbd

## Immediate next step

Connect the validated local moving-muon production and absorption kernels to the radial transport solver, retain separate \(L,+,-\) opacities, combine the validated neutrino inverse-decay channel, and complete source-weighted radial/energy/angular convergence. Do not launch the axial parameter scan before this transport gate passes.
