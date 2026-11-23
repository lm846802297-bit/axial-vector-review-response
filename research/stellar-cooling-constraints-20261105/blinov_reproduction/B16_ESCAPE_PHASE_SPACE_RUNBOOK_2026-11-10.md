# B.16 10 MeV high-order escape phase-space runbook

This runbook executes the targeted post-processing diagnostic against the archived high-order fixed-\(\omega\) B.16 baseline. It does not change the stellar profile, opacity prescription, source kernel, or production axial-vector outputs.

## 1. Environment

From the repository root, use Python 3.10+ with NumPy and SciPy:

```bash
python -m pip install numpy scipy
```

## 2. Run the binning regression tests first

```bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_b16_escape_phase_space.py' -v
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py
```

The tests verify that energy and direction bins are restricted to the selected emission-radius region and that both regional and global fractions close.

## 3. Run the high-order 10 MeV decomposition

```bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py \
  --mass 10 \
  --nr 200 \
  --opacity-order 640 \
  --ne 200 \
  --na 32 \
  --ns 64 \
  --energy-offset 1000 \
  --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json
```

The script requires exact SHA-256 identity of the source-radius and opacity-radius grids, the reconstructed SFHo-18.8 profile, and the Fig. 7 digitization relative to the archived high-order baseline. The energy grid is compared node-by-node with the immutable 842-node reference at relative tolerance 5e-14 and absolute tolerance 1e-13 MeV. It also requires the recomputed integrated luminosity and optically thin source to close against that baseline to \(2\times10^{-10}\).

## 4. Acceptance checks

The output is accepted only if all of the following hold:

- The regression tests pass.
- The 842 energy nodes match the immutable archived node reference at relative tolerance 5e-14 and absolute tolerance 1e-13 MeV; the original baseline hash is preserved as provenance.
- The luminosity and thin-source closure residuals are each below \(2\times10^{-10}\).
- The angular quadrature weights sum to one within \(10^{-14}\).
- For each region, the emission-radius, energy, four-bin direction, and eight-bin direction partitions each sum to one for both the thin source and escaped luminosity, within \(2\times10^{-10}\).
- The complete radius-energy-direction joint table (not merely its top-ranked cells) must sum to the regional thin source and escaped luminosity within \(2\times10^{-10}\), and its global fractions must reproduce the region's global source and escaped-luminosity fractions.
- The 8--15 km region contributes between 75% and 85% of the global B.1 source.
- The production axial-vector source, transport, JSON, PDF, and PNG files remain unchanged.

A failed closure or normalization test is a calculation failure, not a result to be interpreted physically.

## 5. Archive after successful execution

Only after all acceptance checks pass:

```bash
git add research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json
git commit -m "Archive high-order 10 MeV escape phase-space decomposition"
git push origin research/moving-muon-thermal-rates-20261107
```

## 6. Interpretation boundary

The output partitions the same B.1 source measure multiplied by the same B.2 survival factor. Energy bins are reporting partitions; they do not alter the energy quadrature. The result is a diagnostic of the current reconstructed-profile, fixed-\(\omega\), 25 km vector benchmark. It does not establish the private implementation used for Fig. 7, does not justify an empirical rescaling, and does not update the axial-vector constraint curve.


## 7. Windows PowerShell local execution

The calculation is CPU-based NumPy/SciPy code; it does not use CUDA or the RTX GPU. From a local clone of this exact branch, open PowerShell at the repository root:

```powershell
git switch research/moving-muon-thermal-rates-20261107
git pull --ff-only origin research/moving-muon-thermal-rates-20261107
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy scipy
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p "test_b16_escape_phase_space.py" -v
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py
python research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py --mass 10 --nr 200 --opacity-order 640 --ne 200 --na 32 --ns 64 --energy-offset 1000 --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json
```

Do not archive or commit the JSON unless the script exits successfully and all closure/normalization checks pass. The GitHub workflow's final acceptance checks should also be run against the local JSON; the local run is a way to execute the identical diagnostic, not a relaxation of its acceptance standard.


## 8. Archive status at the 2026-11-15 review

The canonical Python output named above, `outputs/b16_escape_phase_space_10mev_2026-11-10.json`, is not present on either the research branch or the repository-maintenance branch checked for this review. The committed V8 cross-runtime JSON is present, but it explicitly records `status=cross_runtime_computation_not_strict_numpy_grid_acceptance` and `grid_hashes_match=false`; it is not a substitute for the strict Python artifact.

The Python unit-test module currently contains three binning/partition helper tests. The Python driver emits the complete joint radius-energy-direction table, but the inspected driver and unit tests do not themselves assert the runbook's full joint-table closure criterion. That criterion therefore needs a named, automated acceptance checker (or an explicit CI step) before the runbook can be considered fully closed. The current install commands also request unpinned latest NumPy/SciPy; the accepted run must record and pin the Python, NumPy, and SciPy versions used. Until the strict Python JSON, pinned environment, and joint-table check are archived, treat the V8 result as a cross-runtime cross-check only.


## Follow-up: archived workflow execution evidence (2026-11-17)

The repository contains an explicit CI acceptance step for the complete joint radius-energy-direction table and its one-dimensional marginals in `.github/workflows/b16-escape-phase-space.yml`. This corrects the earlier scope note that the inspected driver/tests did not themselves assert the joint-table closure criterion: the workflow does assert it, but the step has not yet been reached in a successful run.

The latest inspected run for this workflow is [run 43205614274](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43205614274), run number 12, on commit `f19a4485a19f1d862d9dcd6f7703bc72259566ae` (2026-11-12). Its three binning regression tests passed and the diagnostic compiled, but the high-order computation stopped before writing the canonical JSON. The source-grid and opacity-grid hashes matched the archived baseline; the energy-grid hash did not:

- expected energy grid: `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`
- actual energy grid: `db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639`

The run has no uploaded artifacts. The run log records Python 3.12.16, NumPy 2.5.4 and SciPy 1.18.1; the workflow currently requests Python 3.12 and installs unpinned `numpy scipy`, rather than consuming the repository's pinned `requirements-b16-audit.txt`. The strict Python output `outputs/b16_escape_phase_space_10mev_2026-11-10.json` is still absent; the V8 cross-runtime JSON is not a substitute for that canonical output.

**Disposition remains `REVISION_REQUIRED`.** The next repair must reconcile the energy-grid construction with the archived high-order baseline, then rerun the strict Python driver and reach the workflow's joint-table closure checks. This follow-up reads an existing failed run only; it does not rerun the calculation or alter its physics inputs.


---

## 2026-11-17 superseding strict-NumPy closeout

This section supersedes the 2026-11-15/17 notes above that state the canonical
strict-NumPy JSON is absent or the energy-grid hash mismatch is unresolved.
The old failure was real; the repaired producer now reconstructs the archived
energy nodes from the stored B.1 spectral measure and compares the physical
nodes at a tight floating-point tolerance.

### Reproduction command

From the repository root:

```bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_b16_escape_phase_space.py' -v
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py
python research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py \
  --mass 10 --nr 200 --opacity-order 640 --ne 200 \
  --na 32 --ns 64 --energy-offset 1000 \
  --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json \
  --csv-output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.csv \
  --svg-output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.svg
```

### Successful workflow evidence

- Workflow: [B.16 baseline closeout run #44035746636](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44035746636)
- Checked-out source commit: `b2280807acf0669717152d2a3a58ead5d11f258c`
- Run conclusion: `success`; all 8 regression tests, compilation, high-order calculation, closure/normalization checks, and archival steps passed.
- Runtime: Python 3.12.16, NumPy 2.5.4, SciPy 1.18.1.
- Profile: `data/sfho188_digitized.csv`, SHA-256
  `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Archived energy grid: 842 nodes; baseline and current exact grid SHA-256 both
  `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`.
  Reconstructed-node maximum absolute difference is
  (1.14\times10^{-13}\) MeV and maximum relative difference is
  (2.69\times10^{-16}\), within the explicit (10^{-13}\) MeV /
  (5\times10^{-14}\) comparison tolerance.

### Archived outputs

| Artifact | Git blob SHA-1 | SHA-256 / size |
|---|---|---|
| JSON | `9dda96c2e851b94ab5a65b38febe3023d80ba63b` | canonical full result and run metadata |
| CSV | `af40a7b3e0bd164f6833a1ec29fbf69e7e7ac4b9` | SHA-256 `38e18c97225f08d653feed1dc0e359f5a4e62f569439dd8af645d352b8a4bfec`; 166,149 bytes; 660 rows × 13 columns |
| SVG | `cd776943218642b9f80b9f18830dbb1568c4041a` | SHA-256 `808e30611da404c1d9194de141b978b5d775adb7090eaa227c6638a70083755c`; 137,196 bytes; 8 direction-resolved panels |

The CSV contains all 508 non-empty joint bins for all emission radii plus all
152 non-empty joint bins for the selected 8--15 km core. The SVG shows the
escaped-luminosity fraction over emission shell and energy, separately for
the four (cos\theta) bins and for the full/core regions. Its logarithmic
color scale clips values below (10^{-8}) of the maximum to the lightest
shade; this is a visualization floor only and does not remove rows from the
CSV or JSON.

### Numerical result and physical disposition

| Quantity | Result |
|---|---:|
| Calculated 10 MeV luminosity | (2.4396359574\times10^{52}\) erg/s |
| Fig. 7 reference luminosity | (1.2678147591\times10^{52}\) erg/s |
| Relative difference | (+92.4284\%\) |
| Global source-weighted escape probability | (3.2517740194\times10^{-4}\) |
| 8--15 km fraction of total B.1 source | 79.6522% |
| 8--15 km fraction of escaped luminosity | 86.8551% |

The luminosity closure residual against the archived high-order baseline is
(-2.22\times10^{-16}\); the optically thin luminosity residual is zero, and
the escape-probability absolute residual is (-5.42\times10^{-20}\).
The complete joint partitions close to one for both source and escaped
luminosity. These are internal reproduction and decomposition checks.

**Do not interpret this as a successful Fig. 7 physical reproduction.** The
literal fixed-(omega), scalar B.2 result remains 92.43% above the plotted
reference. The decomposition explains where the current result comes from;
it does not explain the mismatch, correct the opacity, or justify a fit or
rescaling. The public-figure-reconstructed profile is not the original raw
Garching table. No axial-vector output or constraint curve is changed.

The former `REVISION_REQUIRED` disposition for the **missing producer/output
package and strict energy-grid gate** is superseded by successful artifact
generation. The separate physical Fig. 7 acceptance gate remains blocked.


## 2026-11-23 cross-runner energy-grid identity

The original archived energy-grid fingerprint remains `036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3`. The immutable 842-node reference is stored in `outputs/b16_energy_grid_reference_10mev_2026-11-09.json`; its file SHA-256 is `3a99a994d9cab96fd194cf540d75ef698f871354839c8f55f05eeaa11f02d957`.

A cross-runner diagnostic produced runtime hash `db6f613c...`, but all 842 nodes matched the reference with maximum absolute difference 5.684341886080802e-14 MeV, maximum relative difference 1.1675488289093305e-16, and maximum ULP difference 1. Another independent run reproduced the original `036e6d77...` byte hash. The two hashes therefore reflect last-bit floating-point representation, not different physical energy grids.

The production result records the full energy-node array and reference-file fingerprint. The validator checks the immutable reference and complete node array; neither the baseline hash nor the reference file is rewritten.
