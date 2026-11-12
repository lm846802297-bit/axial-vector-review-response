# 10 MeV high-energy escape response to outer-temperature stress tests

Date: 2026-11-10  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`  
Input PR head: `d8616f95978e5276cd273192d54a5e2ad9d111d9`  
Machine-readable result: [b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-10.json](outputs/b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-10.json)

## 1. Question

The high-energy B.2 channel audit shows that the (210\text{--}510\,\mathrm{MeV}) band carries 69.76% of the escaped luminosity. The 22--25 km temperature continuation is not directly supported by the original Bollig figure frames, so this calculation asks whether its uncertainty can materially change that dominant escaping band.

This is a **transport-only sensitivity**: B.1 source weights are frozen, and only the B.2 opacity is recomputed after changing the opacity-profile temperature in the specified shell. It is not a self-consistent new stellar profile or a statistical uncertainty band.

## 2. Frozen benchmark and numerical closure

- (m_V=10\,\mathrm{MeV}), (g=4.171689650228597\times10^{-8}).
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- B.1 source radial order: 200.
- B.2 opacity radial order: 640 (642 nodes including endpoints).
- Energy grid: 842 nodes; 10 nodes lie in 210--510 MeV.
- Angular/path orders: 32/64.
- Fixed-`omega` path convention, as printed in B.2.

The baseline high-energy source and escape integrals reproduce the previous channel-resolved phase-space audit:
- source-weight residual: `-3.3307e-16`;
- escaped-integral residual: `0.0000e+0`;
- baseline escape probability: `2.345801e-3`;
- baseline source-weighted mean optical depth: `7.719325`.

The baseline escaped luminosity in this band is (1.70178\times10^{52}\,\mathrm{erg\,s^{-1}}).

## 3. Results

| Opacity-profile variation | High-energy escape probability | Change in 210--510 MeV escaped luminosity |
|---|---:|---:|
| baseline | 2.345801e-3 | +0.000% |
| T(22-25) -30% | 2.336764e-3 | -0.385% |
| T(22-25) -10% | 2.342784e-3 | -0.129% |
| T(22-25) +10% | 2.348822e-3 | +0.129% |
| T(22-25) +30% | 2.354879e-3 | +0.387% |
| T(20-22) -10% | 2.343446e-3 | -0.100% |
| T(20-22) +10% | 2.348158e-3 | +0.100% |

The broad (pm30\%\) stress test of the 22--25 km temperature changes the dominant high-energy escaped luminosity by only (-0.385\%\) to (+0.387\%). The (pm10\%\) test in 20--22 km changes it by only about (pm0.100\%).

The source distribution is held fixed by construction, so these changes are due to the B.2 path opacity alone.

## 4. Why is the high-energy tail so insensitive to outer temperature?

The neutrino reduced-absorption rate is related to the production rate by detailed balance:
[
\Gamma_{\rm abs,\nu}^{*}
=(e^{\omega/T}-1)\Gamma_{\rm prod,\nu}.
]
For (omega/T\gg1), the Bose factor in the production rate cancels the leading exponential in the reduced-absorption factor. In the 22--25 km shell, (mu_{\nu_\mu}=0), and for (omega=210\text{--}510\,\mathrm{MeV}) the daughter-neutrino energies are much larger than the local temperature. Final-state blocking is consequently very small. The reduced neutrino opacity therefore depends only weakly on the uncertain outer temperature in this energy band.

This explains why the 22--25 km shell can contribute a non-negligible optical depth while a large fractional change in its temperature produces only a sub-percent change in the dominant high-energy escaped luminosity.

## 5. Comparison with the existing all-energy stress test

The earlier self-consistent B.1+B.2 stress test in B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md found that a (+30\%\) temperature change over 22--25 km increases the **total** strong-endpoint luminosity by 12.474%. The present transport-only, energy-resolved result shows that the 210--510 MeV band changes by only +0.387%.

These results are not contradictory. The all-energy result includes lower-energy contributions and the recomputed B.1 source, while the present result freezes the source and isolates the dominant escaping high-energy band. It shows that the large high-energy tail is not controlled by the uncertain 22--25 km temperature continuation.

## 6. Interpretation and next decision

The 22--25 km temperature reconstruction cannot plausibly explain the 92.4% fixed-`omega` strong-endpoint excess through its effect on the dominant 210--510 MeV band. The same conclusion holds, at a smaller level, for the 20--22 km (pm10\%\) stress test.

The remaining issue is therefore not a missing local neutrino kernel, under-resolved high-energy chord integral, or the outer temperature alone. The main physical-input limitation is the absence of the original same-snapshot Garching thermodynamic profile and the remaining B.2 path-energy interpretation. The raw profile archive endpoint is access-protected; this calculation does not reconstruct or invent those data.

No temperature profile is changed, no opacity or luminosity is rescaled, and no axial-vector result is updated.
