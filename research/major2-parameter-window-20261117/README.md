# Major 2 — Fig. 2 parameter-window numerical check

## Scope

This folder contains the reproducibility entry point and saved output supporting the Major 2 reply's numerical discussion of the displayed Fig. 2 window. It is a benchmark check, not a new experimental recast, likelihood fit, or UV parameter scan.

The current manuscript/reply display window is
\[
10^{-3}\le m_{A'}\le 10^{2}\;\mathrm{GeV},\qquad
10^{-6}\le g_X\le 1.
\]
These are plot-display endpoints, not universal allowed-region boundaries. The low-mass (g-2) line is continued analytically; the approximately 0.57 MeV crossing with the displayed coupling floor is an explanatory point, not a physical lower mass bound.

## Files

- `check_parameter_window.py`: exact one-loop axial (F_A) integral and the 40/60-decimal-digit consistency check.
- `outputs/parameter_window_2026-11-04.json`: inputs, numerical results, runtime versions and source SHA-256 values.

## Reproduction

From the repository root:

```bash
python research/major2-parameter-window-20261117/check_parameter_window.py
```

Dependencies: Python 3 and `mpmath`. The archived run used Python 3.14.7 and mpmath 1.3.0.

The script resolves the repository root using `Path(__file__).resolve().parents[2]`. Its new location deliberately preserves the same two-directory depth below the repository root, and the output remains in the sibling `outputs/` directory. The script and JSON are byte-identical to their former locations.

## Scientific and provenance limits

- Pure axial benchmark, heavy scalar reference, and no cancellation of the negative axial contribution.
- Uses the exact integral and inputs stated in the JSON; it does not refit the Standard Model (g-2) baseline.
- Does not rank all astrophysical/cosmological constraints, scan all UV couplings, or establish a universal allowed region.
- The displayed upper endpoint (g_X=1) is a plot choice; perturbativity of every UV coupling remains model- and scale-dependent.

Canonical interpretation and response wording: [Major 2 comparison](../../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-Fig2参数范围与论文修改对照_2026-11-04.md) and [Major 2 validation record](../../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-验证记录_2026-11-04.md).
