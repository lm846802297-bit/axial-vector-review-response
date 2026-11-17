# Major 4.2 — momentum-dependent kinetic mixing

## Scope

This folder contains the numerical script and saved output supporting the Major 4.2 response on the physical photon–(A') kinetic-mixing form factor and its conditional comparison with the NA64 electron-beam invisible-dark-photon search.

The reference calculation assumes equal right-handed charged-lepton mixing angles, paired degenerate heavy thresholds, and the boundary condition
\[
\epsilon_{\rm ind}(\mu_{\rm match})=0.
\]
This condition sets the independent local matching coefficient, not the full momentum-dependent physical mixing to zero.

## Files

- `check_kinetic_dark_photon.py`: timelike loop function, threshold behavior, invisible branching fractions and mass-dependent NA64 yield comparison.
- `outputs/kinetic_dark_photon_2026-11-04.json`: numerical output, visual-read-off intervals, runtime and source SHA-256 values.

## Reproduction

From the repository root:

```bash
python research/major4-2-kinetic-mixing-20261117/check_kinetic_dark_photon.py
```

Dependencies: Python 3 and `mpmath`. The archived run used Python 3.14.7 and mpmath 1.3.0.

The script resolves the repository root with `Path(__file__).resolve().parents[2]`; the new directory preserves the original two-directory depth. The output remains under the sibling `outputs/` directory. Both files are byte-identical to their former locations.

## Experimental and physics limits

- The NA64 Fig. 3 curve was read manually from the published log-log plot; the stored intervals include approximately 0.2–0.3 dex read-off uncertainty. They are not official tabulated points.
- The comparison rescales the leading yield by (|\epsilon|\sqrt{\mathrm{Br}_{\rm inv}}); it is not a detector-level recast or a new exclusion contour.
- The 300 MeV point includes the direct dimuon channel. Acceptance and lifetime assumptions must remain explicit.
- Results apply to the stated equal-angle, threshold and matching benchmark; they are not a complete UV parameter-space scan.

See the [Major 4.2 response comparison](../../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-暗光子限制与论文修改对照_2026-11-04.md) and [Major 4.2 validation record](../../审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-验证记录_2026-11-04.md).
