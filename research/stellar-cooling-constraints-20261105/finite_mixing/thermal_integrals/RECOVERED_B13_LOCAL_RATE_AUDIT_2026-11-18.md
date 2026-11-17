# Local audit of recovered B.13 10 MeV kernel evidence

Date: 2026-11-18  
Execution: local Python post-processing; no GitHub Actions compute was invoked.

## Scope and identity

The recovered package comes from Actions run [43376779901](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43376779901), artifact 14015517843. The original JSON SHA-256 and the archived CSV SHA-256 match the provenance manifest. The current branch's `data/sfho188_digitized.csv` has Git blob SHA-1 `e41df78c8035540760fbcb7ef592cd830171822e`, identical to the source-run snapshot's profile CSV blob SHA-1. The profile SHA-256 recorded in the original input is `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

This establishes that the current profile file is byte-identical to the profile used in the historical local run. It does not convert the reconstructed profile into raw Garching simulation data.

## Coverage

- 513 radial/energy grid nodes and 468 direct cell-midpoint evaluations.
- 981 unique radius-energy points, with six rows per point.
- Both `mu_minus` and `mu_plus`; all `L`, `+`, and `-` modes.
- Grid-node domain: (r=0)–24 km and (omega=10)–1500 MeV.
- Midpoint domain: (r=1.25)–23.5 km and (omega=10.03125)–1278.2035 MeV.
- All stored production, absorption, reduced-absorption, and spectral-source values are finite and nonnegative.

## Local-rate and polarization checks

The maximum mode-resolved detailed-balance residual is (4.2660\times10^{-14}), below the stored (2\times10^{-10}) criterion. The maximum final-muon mass-shell residual is (7.0487\times10^{-13}), also below (2\times10^{-10}).

The two transverse modes are numerically degenerate: their maximum relative absorption-rate difference over grid points is (7.38\times10^{-15}). This is consistent with the azimuthally symmetric medium-rest-frame setup and the momentum-aligned polarization basis used by the archived calculation. The longitudinal mode is not generally interchangeable with the transverse modes: its relative difference can approach unity in parts of the grid. Thus the archive supports keeping (L) and transverse modes separate in transport, while (+) and (-) may be combined only after confirming the same symmetry assumptions in the B.2 implementation.

At (omega=10) MeV and (8\le r\le15) km, the nine sampled radial nodes show the following mean local coefficients (per (g_X^2)); units are those of the archived CSV:

| Charge/mode | Mean production | Mean absorption |
|---|---:|---:|
| (mu^-/L) | 0.012323 | 0.016348 |
| (mu^-/+) | 0.012318 | 0.016341 |
| (mu^-/−) | 0.012318 | 0.016341 |
| (mu^+/L) | 0.000103 | 0.000133 |
| (mu^+/+) | 0.000103 | 0.000133 |
| (mu^+/−) | 0.000103 | 0.000133 |

These are local pointwise means, not shell-integrated emissivities or optical depths. The charge asymmetry is retained rather than averaged away.

## The two actual numerical blockers

### 1. Quadrature

The maximum grid-node final-refinement change is (3.36775\times10^{-3}), at (r=8.48214) km and (omega=1500) MeV. The project target is (10^{-3}). About 5.46% of grid-node rows exceed that target. The worst point lies near the hot-shell radius but at the extreme high-energy endpoint; it does not by itself establish a large error in the 10 MeV emissivity.

### 2. Radial-energy interpolation

The maximum direct-midpoint versus sequential-log-interpolation relative error is 0.571297, at (r=21.165) km and (omega=888.2035) MeV. The median midpoint error is approximately 0.1224; 90.38% of midpoint rows exceed 1%, and 51.71% exceed 10%.

The error is strongly radius-dependent. The median is about 1.40% in the 8–10 km shell, but rises to roughly 14.6% in 12–15 km, 23.0% in 15–18 km, and 56.4% in 20–22 km. This is a direct warning against treating the archived sequential log interpolation as a validated local-rate representation. The high-energy outer-shell worst cell may carry little emission weight, but that must be established by a weighted B.2 analysis, not assumed.

## Acceptance and next action

| Check | Result |
|---|---|
| Historical JSON/CSV identity | PASS |
| Current profile blob identity | PASS |
| Nonnegative finite rates | PASS |
| Detailed balance | PASS |
| Muon mass shell | PASS |
| Transverse (+/-) degeneracy | PASS |
| Grid-node quadrature at 0.1% | **FAIL** |
| Midpoint interpolation at 1% | **FAIL** |
| Overall P1-B local-kernel acceptance | **FAIL** |

**No B.2 transport or Fig. 7 conclusion is updated by this audit.**

Next, the local B.2 implementation must be inspected before propagation: retain the archived pointwise direct midpoint values as independent checks, and compare (i) scalar opacity/escape treatment and (ii) polarization-resolved opacity/escape treatment. The comparison must report the contribution-weighted impact of interpolation errors, preserve (L) versus transverse modes, and demonstrate whether the transverse degeneracy is preserved. Do not rescale opacity or update axial limits.
