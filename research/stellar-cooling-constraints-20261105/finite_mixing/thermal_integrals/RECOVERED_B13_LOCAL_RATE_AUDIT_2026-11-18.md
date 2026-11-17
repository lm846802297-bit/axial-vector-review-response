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


## Important scope correction: this archive is the semi-Compton channel only

The archived local kernel is explicitly the pure-vector process
`muon + photon <-> muon + A'` (B.13). It is **not** the complete local opacity entering B.2. The neutrino inverse-decay contribution must be supplied separately from the corresponding B.1/B.4 kernel and combined only at the transport stage according to the chosen closure. Therefore none of the tabulated B.13 rates may be relabeled as total absorption.

The B.2 state-counting audit already recorded in `B2_POLARIZATION_BOLTZMANN_STATE_COUNTING_AUDIT_2026-11-13.md` distinguishes three different objects:
- literal scalar equation-level reproduction using the paper's summed opacity convention;
- no-polarization-mixing transport, propagating each (h=L,+,-) with its own (	au_h) and summing escaped mode luminosities;
- equal-occupation scalar closure, for which the attenuation coefficient is the arithmetic-average per-state opacity (sum_hGamma^*_{\mathrm{abs},h}/3).

These are not interchangeable after exponentiation. The local B.13 archive supplies only the Compton part of the mode-resolved rates; a fair comparison must combine it with the same separately validated neutrino inverse-decay rates in all lanes. The scalar lane must remain a literal equation-reproduction lane and must not be silently redefined as the physical no-mixing lane.

## Interpolation cross-check

An additional post-processing comparison was made using the same four grid corners and the direct midpoint values. For the absorption channel alone, bilinear interpolation in (logGamma_{\rm abs}) gives a median relative error of 7.64%, a maximum of 57.13%, and 82.37% of charge/mode midpoint rows above 1%. Ordinary bilinear interpolation in (Gamma_{\rm abs}) gives a median of 21.24%, a maximum of 96.70%, and 86.40% of rows above 1%. This confirms that the log method is better than the linear alternative for this table, but neither passes the project tolerance. The per-midpoint archive acceptance metric is stricter because it takes the maximum across charges, modes, and all four derived rate fields.


## Source-weighted interpolation diagnostic (not a B.2 result)

I also integrated the direct midpoint B.13 spectral source over each radial-energy cell using the diagnostic measure (4\pi r^2\,dr\,d\omega), and compared it with the same cell source reconstructed from the archived log-interpolated absorption and midpoint detailed balance. The result is:
- direct local Compton-source integral: (2.24809\times10^7) in the archive's internal units;
- interpolated local Compton-source integral: (2.20743\times10^7);
- integrated difference: (-1.8084\%);
- source-weighted pointwise relative error: (2.1662\%).

Multiplying the diagnostic measure by the midpoint lapse changes the integrated difference only slightly, to (-1.8090\%). This confirms that the interpolation problem does not disappear merely by weighting with the local Compton source. However, this remains a local-source diagnostic: it omits neutrino inverse decay, ray geometry, path attenuation, and the complete GR transport measure. It must not be quoted as the Fig. 7 luminosity error or as a B.2 error estimate.

Reproduction: `audit_b13_source_weighted_interpolation.py`; result: `outputs/b13_source_weighted_interpolation_diagnostic_2026-11-18.json`.


## Reconciliation with later full-profile PCHIP audits

The 57.13% maximum above belongs specifically to the historical 513-node/27-energy-node fixed-(omega) bilinear-log screen. It is **not** the best available production interpolation prescription in this repository and must not be presented as a failure of every B.13 interpolator.

Later full-profile calculations already tested a better thermal coordinate (x=(omega-m_{A'})/T(r)):
- Global-03's sequential 2D PCHIP in (sqrt{x}), followed by log-linear radial interpolation, was checked at all 1686 radial intervals. Its maximum cell-center error was 0.80678%, with zero of 13,488 checked centers above 1%.
- Global-06 extended the low-energy range to (0.05\le x\le0.5). Its full-radial energy PCHIP maximum error was 0.03260%; the top-60 radial midpoint maximum was 0.0831%. Targeted high-order checks passed, but global high-order quadrature acceptance remained false.
- The remaining explicit energy-coverage gap is (0\le x<0.05). The Global-06 summary marks full-band B.1/B.2 as not yet accepted.

Accordingly, the next B.2 implementation should use the already audited thermal-coordinate PCHIP prescription, not the coarse fixed-(omega) bilinear-log interpolation tested in the recovered historical artifact. The 1.808% source-integral shift reported above is a diagnostic of that coarse interpolation only; it is not an estimate of the error of the Global-03/Global-06 PCHIP prescription.

This reconciliation changes no acceptance flag: the recovered historical artifact remains failed under its original criteria, while the later PCHIP interpolation screens are separate successful partial validations. Neither establishes the missing (x<0.05) contribution, global high-order quadrature, B.2 optical depths, or Fig. 7 reproduction.
