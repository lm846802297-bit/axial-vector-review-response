# Axial-vector Domain Extension to RCRPS v1.0.1

**Status:** Project-specific extension to the centrally maintained RCRPS v1.0.1 standard.  
**Central source commit:** 142267bc803c90aa681110293b66b73947bbcaa1

The normative JSON record roles, common fields, source-control provenance, CSV contract, status semantics, and validation requirements are defined by the [central RCRPS v1.0.1 standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/142267bc803c90aa681110293b66b73947bbcaa1/docs/STRUCTURED_RESULT_DATA_STANDARD_v1.0.1.md). This file defines only the axial-vector project's domain-specific metadata and local validator entry points.

The local schemas and validator are synchronized byte-for-byte with the central copies at the pinned source commit. The local copies are retained because the repository's workflow validates files within this repository. Update them only through a reviewed downstream PR that also updates `research/standards-lock.yaml`.

## 1. Local implementation

- Historical v1.0.0 schema: `docs/repository-management/schemas/research-result-record-v1.0.0.schema.json`
- Adopted v1.0.1 schema: `docs/repository-management/schemas/research-result-record-v1.0.1.schema.json`
- Validator: `docs/repository-management/schemas/validate_result_records.py`
- Regression tests: `docs/repository-management/schemas/tests/`
- Pinned dependency: `docs/repository-management/schemas/requirements-result-validation.txt`

Install the pinned dependency and run the local regression suite:

```powershell
python -m pip install -r docs/repository-management/schemas/requirements-result-validation.txt
python -m unittest discover -s docs/repository-management/schemas/tests -v
python -m compileall -q docs/repository-management/schemas
```

For a v1.0.1 run manifest, use the local validator with the explicit schema path:

```powershell
python docs/repository-management/schemas/validate_result_records.py --schema docs/repository-management/schemas/research-result-record-v1.0.1.schema.json --repo-root . <run_manifest.json> <result_summary.json> <validation_report.json>
```

The v1.0.0 schema remains available only for historical compatibility. New substantial runs use v1.0.1 and must record the complete `execution.source_control` object required by the central schema. Do not fabricate missing source-control or run metadata for historical calculations.

## 2. Axial-vector domain extension

Use the `extensions` object in the common record schema. Keep these fields project-local; do not add them to common top-level fields.

### 2.1 Supernova transport

Under `extensions.supernova_transport`, record as applicable:

- (m_{A'}), (g_X), vector/axial-vector coupling components, and their normalization;
- background model (for example, SFHo), snapshot time, profile source/version/SHA-256, radial coverage, (R_\nu), and (R_{\rm far});
- (T(r)), chemical potentials, species densities, and their definitions;
- production/absorption channels, neutrino flavor, (mu^-)/(mu^+), and L/T+/T− polarization modes;
- opacity/reduced-opacity definitions, detailed-balance convention, gravitational redshift, escape path, and boundary conditions;
- radial/energy/angular integration nodes, local-kernel quadrature order, integrator, and tolerances;
- per-channel/per-polarization local rates, optically thin luminosities, optical depths, escape probabilities, and total luminosity.

### 2.2 UV–EFT and loop calculations

Record VLL/scalar parameters, renormalization scheme and scale, gauge and (gamma_5) conventions, IR treatment, operator basis, matching scale, and diagram/counterterm coverage. Different physical models and benchmarks require distinct `run_id` values.

## 3. Historical preservation

Existing JSON/CSV records, figures, source snapshots, and archived calculation outputs remain unchanged. This adoption does not require rewriting historical numerical files or assigning metadata that cannot be verified from the original execution.

A future sidecar `run_manifest.json` or `validation_report.json` may reference an existing output only when the exact source revision, inputs, parameters, command, and other provenance fields can be verified. Large coupling/energy/radial arrays should be stored as native CSV files with explicit dimensions and units.

In particular, existing C1/A0 research outputs and the files in active research PRs are not modified by this governance migration. The PR #123 C1 baseline JSON/CSV remain as submitted; this standard does not promote their scientific status or claim a new calculation.
