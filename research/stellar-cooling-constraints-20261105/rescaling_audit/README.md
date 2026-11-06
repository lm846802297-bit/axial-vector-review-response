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

The deterministic output is written to rescaling_audit/outputs/rescaling_audit.json (relative to this directory).

## Rescaling convention

The fit tests

~~~math
L_{\rm calc}(\kappa g_{\rm ref}) \simeq L_{\rm ref}(g_{\rm ref}).
~~~

The search interval is 0.90 <= kappa <= 1.10 with a fixed 0.00025 grid. The objective is the RMS of the logarithmic luminosity ratio. The fit-point set is fixed across all trial values of kappa; no extrapolation is allowed. This prevents the optimizer from improving the score by silently dropping difficult endpoint samples.

A fitted mass-specific kappa is diagnostic only. It is not adopted as a coupling redefinition unless a single physically motivated value also passes the independent Fig. 4 contour-boundary check.


## Dedicated CI workflow

The separate Vector coupling rescaling audit workflow runs this directory's regression tests and post-processes the archived JSON curves only. It does not trigger the Major 4.4 full thermal-rate and transport scan workflow, and it does not recalculate B.13.
