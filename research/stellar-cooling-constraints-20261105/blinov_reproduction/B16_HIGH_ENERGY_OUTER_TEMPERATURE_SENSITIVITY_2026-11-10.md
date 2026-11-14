# 10 MeV high-energy escape response to outer-temperature stress tests

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Input PR head: \`d8616f95978e5276cd273192d54a5e2ad9d111d9\`  
Machine-readable result: [b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-10.json](outputs/b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-10.json)

## 1. Question and scope

The high-energy B.2 channel audit finds that the \(210\text{--}510\,\mathrm{MeV}\) band carries about \(69.76\%\) of the escaped luminosity. The \(22\text{--}25\) km temperature continuation is not directly supported by the original Bollig figure frames, so this calculation asks whether its uncertainty can materially change that dominant escaping band.

This is a **transport-only sensitivity**: B.1 source weights are frozen, and only the B.2 opacity is recomputed after changing the opacity-profile temperature in the specified shell. It is not a self-consistent new stellar profile or a statistical uncertainty band.

## 2. Frozen benchmark and baseline closure

- \(m_V=10\,\mathrm{MeV}\), \(g=4.171689650228597\times10^{-8}\).
- Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
- B.1 source radial order: 200.
- B.2 opacity radial order: 640 (642 nodes including endpoints).
- Energy grid: 842 nodes; 10 nodes lie in \(210\text{--}510\) MeV.
- Angular/path orders: 32/64.
- Path convention: fixed \(\omega\), as displayed in Eq. (B.2).

The V8 baseline reproduces the previous channel-resolved phase-space audit:
- source-weight residual: \(-3.3307\times10^{-16}\);
- escaped-integral residual: \(0.0000\);
- baseline escape probability: \(2.345801\times10^{-3}\);
- baseline source-weighted mean optical depth: \(7.719325\).

The baseline escaped luminosity in this band is \(1.70178\times10^{52}\,\mathrm{erg\,s^{-1}}\).

## 3. Results

| Opacity-profile variation | High-energy escape probability | Change in \(210\text{--}510\) MeV escaped luminosity |
|---|---:|---:|
| baseline | \(2.345801\times10^{-3}\) | \(0.000\%\) |
| \(T(22\text{--}25)\) \(-30\%\) | \(2.336764\times10^{-3}\) | \(-0.385\%\) |
| \(T(22\text{--}25)\) \(-10\%\) | \(2.342784\times10^{-3}\) | \(-0.129\%\) |
| \(T(22\text{--}25)\) \(+10\%\) | \(2.348822\times10^{-3}\) | \(+0.129\%\) |
| \(T(22\text{--}25)\) \(+30\%\) | \(2.354879\times10^{-3}\) | \(+0.387\%\) |
| \(T(20\text{--}22)\) \(-10\%\) | \(2.343446\times10^{-3}\) | \(-0.100\%\) |
| \(T(20\text{--}22)\) \(+10\%\) | \(2.348158\times10^{-3}\) | \(+0.100\%\) |

The broad \(\pm30\%\) stress test of the \(22\text{--}25\) km temperature changes the dominant high-energy escaped luminosity by only \(-0.385\%\) to \(+0.387\%\). The \(\pm10\%\) test in \(20\text{--}22\) km changes it by about \(\pm0.100\%\).

The source distribution is held fixed by construction, so these changes arise from the B.2 path opacity alone. No predeclared pass/fail tolerance is specified; these are sensitivity values, not a numerical convergence acceptance test.

## 4. Why is the high-energy tail weakly sensitive to outer temperature?

The neutrino reduced-absorption rate is related to the production rate by detailed balance:
\[
\Gamma_{\rm abs,\nu}^{*}
=(e^{\omega/T}-1)\Gamma_{\rm prod,\nu}.
\]

For \(\omega/T\gg1\), the Bose factor in the production rate cancels the leading exponential in the reduced-absorption factor. In the \(22\text{--}25\) km shell, \(\mu_{\nu_\mu}=0\), and for \(\omega=210\text{--}510\,\mathrm{MeV}\) the daughter-neutrino energies are much larger than the local temperature. Final-state blocking is consequently small. The reduced neutrino opacity therefore depends only weakly on the uncertain outer temperature in this energy band.

This explains why the \(22\text{--}25\) km shell can contribute a non-negligible optical depth while a large fractional change in its temperature produces only a sub-percent change in the dominant high-energy escaped luminosity.

## 5. Comparison with the existing all-energy stress test

The earlier self-consistent B.1+B.2 stress test in [B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md](B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md) found that a \(+30\%\) temperature change over \(22\text{--}25\) km increases the **total** strong-endpoint luminosity by \(12.474\%\).

The present transport-only, energy-resolved result shows that the \(210\text{--}510\) MeV band changes by only \(+0.387\%\). These results are not contradictory: the all-energy result includes lower-energy contributions and recomputes the B.1 source, while the present result freezes the source and isolates the dominant escaping high-energy band.

## 6. Reproducibility qualification

The referenced JSON declares \`direct_V8_transport_only_sensitivity\`, uses the V8 JavaScript binary64 engine, and records the profile hash and elapsed time. It does not contain a Python script hash. No matching Python implementation of this **frozen-source, energy-resolved transport-only** calculation is present in the inspected repository.

The existing Python temperature-sensitivity scripts recompute the self-consistent B.1+B.2 result and therefore are not equivalent substitutes for this fixed-source \(210\text{--}510\) MeV calculation. The V8 JSON is retained as a cross-runtime diagnostic only. A separate NumPy implementation and Python output archive are required before this record can pass strict-reproduction review.

## 7. Interpretation and physical disposition

The \(22\text{--}25\) km temperature reconstruction cannot plausibly explain the \(92.4\%\) fixed-\(\omega\) strong-endpoint excess through its effect on the dominant \(210\text{--}510\) MeV band. The same conclusion holds, at a smaller level, for the \(20\text{--}22\) km \(\pm10\%\) stress test.

The printed Eq. (B.2) remains the fixed-\(\omega\) baseline. The path-redshift branch is a separate alternative sensitivity, not an ambiguity in the displayed equation and not a full-GR ray trace. The remaining physical-input limitation is the absence of the original same-snapshot Garching thermodynamic profile.

No temperature profile is changed, no opacity or luminosity is rescaled, and no axial-vector result is updated.

## 8. Strict NumPy reproduction (2026-11-15)

A matching NumPy implementation has now been executed for the exact frozen-source, energy-resolved transport sensitivity described above. The output is archived at [b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-15_numpy.json](outputs/b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-15_numpy.json).

- Output SHA-1 (Git blob): \`3ac5533202ca10d69f6c4972d60016575327405e\`.
- Script SHA-256: \`d18de99fd57e7d894d0861d68b362d3d40b4c6afd17b1329f6be486f36fc918e\`.
- Run commit: \`9d7665560d61479b2cda653b2dd842a4340b14d6\`.
- Execution and five V8-comparison tests: [GitHub Actions #43648694518](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43648694518).

The calculation uses the full 842-node B.1 energy quadrature to preserve the source weights, then retains the ten \(210\text{--}510\) MeV nodes for the opacity and escape calculation. The source is held fixed in all seven temperature scenarios; only the B.2 opacity profile is changed. The principal escape-probability and escaped-luminosity observables agree with V8 to better than \(2.5\times10^{-7}\) relative across the seven scenarios. The absolute differences in the small fractional-change observables are below \(2.5\times10^{-7}\).

This supersedes the earlier statement in Section 6 that no matching Python implementation or output existed. The strict reproduction confirms the original conclusion: even a \(\pm30\%\) stress of \(T(22\text{--}25\,\mathrm{km})\) changes the dominant high-energy escaped luminosity by only about \(\mp0.386\%\). It does not explain the \(+92.4\%\) fixed-\(\omega\) strong-endpoint discrepancy. The test is a transport-only sensitivity, not a self-consistent new stellar profile or a statistical uncertainty interval.
