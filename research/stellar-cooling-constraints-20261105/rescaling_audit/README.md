# Coupling-axis rescaling audit

This directory contains a post-processing audit of the archived vector luminosity curves. It is deliberately separate from the production rate and transport modules.

## What it reads

- **blinov_reproduction/outputs/blinov_literal_scan.json** — the independent scalar/literal Blinov luminosity scan.
- **blinov_reproduction/outputs/fig4_fig7_comparison.json** — archived Fig. 4 contour crossings and Fig. 7 comparison-point metadata.
- **outputs/vector_audit/luminosity_comparison.json** — digitized Fig. 7 reference points and the existing exact_modes vector-control curve.

## What it does not do

The audit does not import or execute rates.py, transport.py, reference.py, run_scan.py, or run_vector_audit.py. It does not rerun B.13 thermal phase-space integrals, Compton matrix elements, opacity integrals, or stellar luminosity scans. It only interpolates the already archived luminosity curves in log-log space.

## Reproduce

From the repository root:

~~~bash
python -m unittest discover \
  -s research/stellar-cooling-constraints-20261105/rescaling_audit \
  -p 'test_*.py' -v

python research/stellar-cooling-constraints-20261105/rescaling_audit/run.py
~~~

The deterministic output is written to outputs/rescaling_audit.json.

## Historical input pin and safe reruns

The committed `outputs/rescaling_audit.json` is the archived 2026-11-07 result. Its three recorded input SHA-256 values match the raw input JSON files at commit `b3af69de1b37e2efc9f590e40e03a4ca85434420` (the head of Actions run [#42302956969](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42302956969)); the recorded script SHA-256 also matches `run.py` at that commit.

The current repository inputs have since advanced. In particular, the archived rescaling result uses profile SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`, whereas the current vertex-preserving profile is `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. The other two luminosity/comparison JSON inputs have also changed. Therefore, a run from the current checkout is a **new input-version diagnostic**, not an exact reproduction of the archived result.

**Do not run the default command above on the current checkout if you need to preserve the historical output:** `run.py` writes to the same default `outputs/rescaling_audit.json` path and will overwrite it. For a current-tree rerun, supply a distinct path, for example:

```bash
python research/stellar-cooling-constraints-20261105/rescaling_audit/run.py \
  --output research/stellar-cooling-constraints-20261105/rescaling_audit/outputs/rescaling_audit_current_2026-11-16.json
```

To reproduce the historical input set, check out commit `b3af69de1b37e2efc9f590e40e03a4ca85434420` before running the script. Keep the historical and current-input outputs separate.

## Rescaling convention

The fit tests

~~~math
L_{\rm calc}(\kappa g_{\rm ref}) \simeq L_{\rm ref}(g_{\rm ref}).
~~~

The search interval is 0.90 <= kappa <= 1.10 with a fixed 0.00025 grid. The objective is the RMS of the logarithmic luminosity ratio. The fit-point set is fixed across all trial values of kappa; no extrapolation is allowed. This prevents the optimizer from improving the score by silently dropping difficult endpoint samples. For the literal scalar fit, the pooled objective contains 69 points with equal weight per point: 32 at 1 MeV, 25 at 10 MeV and 12 at 200 MeV (weights 32/69, 25/69 and 12/69). It is therefore point-weighted, not an equal-mass average; the 1 MeV dataset contributes the largest share.

A fitted mass-specific kappa is diagnostic only. It is not adopted as a coupling redefinition unless a single physically motivated value also passes the independent Fig. 4 contour-boundary check.


## Dedicated CI workflow

The separate Vector coupling rescaling audit workflow runs this directory's regression tests and post-processes the archived JSON curves only. It does not trigger the Major 4.4 full thermal-rate and transport scan workflow, and it does not recalculate B.13.
