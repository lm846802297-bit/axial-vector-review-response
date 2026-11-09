# B.16 10 MeV high-order escape phase-space runbook

This runbook executes the targeted post-processing diagnostic against the archived high-order fixed-\(\omega\) B.16 baseline. It does not change the stellar profile, opacity prescription, source kernel, or production axial-vector outputs.

## 1. Environment

From the repository root, use Python 3.10+ with NumPy and SciPy:

\`\`\`bash
python -m pip install numpy scipy
\`\`\`

## 2. Run the binning regression tests first

\`\`\`bash
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p 'test_b16_escape_phase_space.py' -v
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py
\`\`\`

The tests verify that energy and direction bins are restricted to the selected emission-radius region and that both regional and global fractions close.

## 3. Run the high-order 10 MeV decomposition

\`\`\`bash
python research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py \
  --mass 10 \
  --nr 200 \
  --opacity-order 640 \
  --ne 200 \
  --na 32 \
  --ns 64 \
  --energy-offset 1000 \
  --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json
\`\`\`

The script requires exact SHA-256 identity of the source-radius, opacity-radius, and energy grids, the reconstructed SFHo-18.8 profile, and the Fig. 7 digitization relative to the archived high-order baseline. It also requires the recomputed integrated luminosity and optically thin source to close against that baseline to \(2\times10^{-10}\).

## 4. Acceptance checks

The output is accepted only if all of the following hold:

- The regression tests pass.
- The luminosity and thin-source closure residuals are each below \(2\times10^{-10}\).
- The angular quadrature weights sum to one within \(10^{-14}\).
- For each region, the emission-radius, energy, four-bin direction, and eight-bin direction partitions each sum to one for both the thin source and escaped luminosity, within \(2\times10^{-10}\).
- The 8--15 km region contributes between 75% and 85% of the global B.1 source.
- The production axial-vector source, transport, JSON, PDF, and PNG files remain unchanged.

A failed closure or normalization test is a calculation failure, not a result to be interpreted physically.

## 5. Archive after successful execution

Only after all acceptance checks pass:

\`\`\`bash
git add research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json
git commit -m "Archive high-order 10 MeV escape phase-space decomposition"
git push origin research/moving-muon-thermal-rates-20261107
\`\`\`

## 6. Interpretation boundary

The output partitions the same B.1 source measure multiplied by the same B.2 survival factor. Energy bins are reporting partitions; they do not alter the energy quadrature. The result is a diagnostic of the current reconstructed-profile, fixed-\(\omega\), 25 km vector benchmark. It does not establish the private implementation used for Fig. 7, does not justify an empirical rescaling, and does not update the axial-vector constraint curve.


## 7. Windows PowerShell local execution

The calculation is CPU-based NumPy/SciPy code; it does not use CUDA or the RTX GPU. From a local clone of this exact branch, open PowerShell at the repository root:

\`\`\`powershell
git switch research/moving-muon-thermal-rates-20261107
git pull --ff-only origin research/moving-muon-thermal-rates-20261107
py -3.12 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy scipy
python -m unittest discover -s research/stellar-cooling-constraints-20261105/blinov_reproduction -p "test_b16_escape_phase_space.py" -v
python -m py_compile research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py
python research/stellar-cooling-constraints-20261105/blinov_reproduction/audit_b16_escape_phase_space.py --mass 10 --nr 200 --opacity-order 640 --ne 200 --na 32 --ns 64 --energy-offset 1000 --output research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b16_escape_phase_space_10mev_2026-11-10.json
\`\`\`

Do not archive or commit the JSON unless the script exits successfully and all closure/normalization checks pass. The GitHub workflow's final acceptance checks should also be run against the local JSON; the local run is a way to execute the identical diagnostic, not a relaxation of its acceptance standard.
