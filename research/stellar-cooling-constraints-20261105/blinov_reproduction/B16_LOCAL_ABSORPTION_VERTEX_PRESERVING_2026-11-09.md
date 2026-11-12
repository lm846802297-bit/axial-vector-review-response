# Independent local absorption audit on the vertex-preserving profile (2026-11-09)

## Executive result

The independent B.6--B.10 and B.13--B.19 local absorption audit has been rerun on the current 1687-row vertex-preserving profile, SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. It samples 16 radii and six local vector energies (96 radius-energy points), including the resolved positive \(\mu_{\nu_\mu}\) branch in 16.75--18.25 km and the 20--22 km shell.

All independent local production, absorption, and reduced-absorption comparisons close at or below \(3.05\times10^{-14}\). The result confirms that the current local implementation faithfully reproduces the printed Appendix-B reference formulae at the sampled points. It does not establish the physical accuracy of the no-recoil Compton approximation or the correctness of the global path/source integration; those are separate tests.

## 1. Current input and numerical setup

- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Profile: public-figure reconstruction of SFHo-18.8, not raw Garching simulation data.
- Mediator mass: 10 MeV.
- Sampled radii (km): 8, 10, 12, 15, 16.75, 17.5, 18.25, 18.5, 19, 20, 20.5, 21.5, 22, 23, 24, 25.
- Local vector energies: 12, 15, 20, 30, 50, 100 MeV.
- Direct neutrino angular integration: 512-point Gauss--Legendre.
- Independent B.17 susceptibility integral: 256-point transformed Gauss--Legendre.
- Total sampled radius-energy points: 96.

The radii 16.75, 17.5, and 18.25 km explicitly sample the positive Caputo \(\mu_{\nu_\mu}\) branch. The 20.5 and 21.5 km points sample the 20--22 km shell where the original Bollig Fig. 1/4 curves no longer provide direct coverage.

## 2. Independent checks

The neutrino inverse-decay rates are reconstructed by direct integration over the two-body angular phase space, with \(\nu_\mu\) and \(\nu_\tau\) treated separately. The inverse-occupation absorption integrals are evaluated directly and compared with B.10 detailed balance and B.4 reduced opacity.

The Compton reference rate is independently reconstructed from B.14--B.17 using a transformed Gauss--Legendre evaluation of the one-species B.17 susceptibility. B.19 detailed balance and B.4 reduced absorption are checked separately. The explicit B.14 velocity factor and B.16 \(1/v_V\) cancellation are retained.

## 3. Maximum residuals

| Check | Maximum relative residual |
|---|---:|
| \(\nu_\mu\) B.6 direct production vs analytic expression | \(2.105\times10^{-14}\) |
| \(\nu_\tau\) B.6 direct production vs analytic expression | \(1.411\times10^{-14}\) |
| \(\nu_\mu\) B.10 detailed balance | \(1.734\times10^{-15}\) |
| \(\nu_\tau\) B.10 detailed balance | \(1.734\times10^{-15}\) |
| Neutrino B.4 reduced absorption | \(1.657\times10^{-15}\) |
| Compton B.16 production vs current reference implementation | \(4.903\times10^{-14}\) |
| Compton B.19 detailed balance | \(2.555\times10^{-16}\) |
| Compton B.4 reduced absorption | \(2.223\times10^{-16}\) |
| Total local production closure | \(3.024\times10^{-14}\) |
| Total local absorption closure | \(3.035\times10^{-14}\) |
| Total local reduced-absorption closure | \(3.048\times10^{-14}\) |

The closure residuals are numerical comparisons of independently evaluated local formulae; they are not a fit to Fig. 7.

## 4. Positive-branch and outer-shell samples

| r (km) | T (MeV) | \(\mu_{\nu_\mu}\) (MeV) | Maximum local residual at this radius |
|---:|---:|---:|---:|
| 16.75 | 7.85672 | +1.27448 | \(9.50\times10^{-15}\) |
| 17.50 | 6.60122 | +1.78527 | \(8.02\times10^{-15}\) |
| 18.25 | 5.62131 | +1.24259 | \(7.71\times10^{-15}\) |
| 18.50 | 5.34946 | 0 | \(7.62\times10^{-15}\) |
| 19.00 | 4.88202 | 0 | \(7.04\times10^{-15}\) |
| 20.50 | 3.97328 | 0 | \(5.67\times10^{-15}\) |
| 21.50 | 3.65949 | 0 | \(5.69\times10^{-15}\) |
| 22.00 | 3.55139 | 0 | \(5.60\times10^{-15}\) |

The resolved positive \(\mu_{\nu_\mu}\) branch is therefore included in the independent local neutrino-kernel check; the audit is not relying only on the zero-chemical-potential outer points.

The independent susceptibility calculation also reports the mu-plus fraction of the total susceptibility. It remains below 0.05% through 22 km in the sampled profile. At 23--25 km, where \(\mu_\mu=0\), the mu-plus fraction becomes 50%, but the muon susceptibility is exponentially dilute and the current global B.2 decomposition assigns a negligible Compton opacity to that outer region. The printed one-species B.17 convention remains the benchmark; no ad hoc factor of two is introduced.

## 5. What this does and does not establish

Established:
1. The current-profile local \(\nu_\mu\) and \(\nu_\tau\) B.6 production formulae match direct angular phase-space integration.
2. B.10 detailed balance and B.4 reduced absorption close independently for both flavors.
3. The current-profile Compton B.16, B.19, and B.4 implementation matches an independent susceptibility-based reconstruction.
4. The sampled positive-\(\mu_{\nu_\mu}\) and 20--22 km points show no local algebraic or numerical closure failure.

Not established:
1. The physical accuracy of the B.14--B.16 non-relativistic/no-recoil Compton approximation at 10 MeV. The exact moving-muon B.13 integral remains a separate approximation diagnostic.
2. The correctness of the full B.1 global source measure and B.2 ray integration beyond their separate global closure tests.
3. Agreement with Fig. 7. Local formula closure cannot by itself establish a correct global luminosity.

No production rate, path opacity, coupling, luminosity, vector reference curve, or axial-vector constraint is rescaled.

## 6. Reproducibility

- Workflow: [Run 42558231626](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42558231626)
- Machine-readable output: `outputs/b16_local_absorption_vertex_preserving_10mev_2026-11-09.json`
- Audit script: `audit_b16_local_absorption.py`
- Tests: `test_b16_local_absorption.py`
