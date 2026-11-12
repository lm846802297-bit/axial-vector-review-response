# Cross-mass opacity and energy-convention diagnostic (2026-11-09)

## Scope

This report compares the current vertex-preserving profile B results at (m_V=0.1,1,10) MeV. It uses the archived fixed-(omega) B.16 baseline and the separate path-redshift-only diagnostic. No collision kernel, profile, coupling grid, or production output is changed.

Profile SHA-256:
`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`

Machine-readable source:
`outputs/b16_global_redshift_audit_2026-11-09.json`

## 1. Source-channel and opacity-channel decomposition

| (m_V) | B.16 Compton source fraction | Neutrino source fraction | Compton fraction of source-weighted mean (	au) | Neutrino fraction of source-weighted mean (	au) |
|---:|---:|---:|---:|---:|
| 0.1 MeV | 99.978% | 0.0218% | 99.931% | 0.0692% |
| 1 MeV | 97.870% | 2.130% | 93.471% | 6.529% |
| 10 MeV | 32.005% | 67.995% | 10.222% | 89.778% |

This immediately separates the mass regimes:

- At 0.1 and 1 MeV, the Compton channel controls both production and opacity. The exact B.13 versus approximate B.14--B.16 comparison is therefore a high-priority method check at these masses.
- At 10 MeV, neutrino inverse decay supplies about 68.0% of the optically thin source and 89.8% of the source-weighted mean opacity. The strong-endpoint mismatch at this mass is primarily a neutrino-transport/background problem, although the Compton source is not negligible.

## 2. Radial location of the mean optical depth

| (m_V) | Fraction of source-weighted mean (	au) accumulated at (rge15) km | Contribution from 20--22 km | Contribution from 22--25 km | Combined 20--25 km |
|---:|---:|---:|---:|---:|
| 0.1 MeV | 0.108% | 0.0083% | 0.0124% | 0.0207% |
| 1 MeV | 3.926% | 0.787% | 1.176% | 1.963% |
| 10 MeV | 56.757% | 11.575% | 17.321% | 28.895% |

The outer thermodynamic continuation is not a uniform uncertainty across masses. It is negligible for the 0.1 MeV mean opacity, modest at 1 MeV, and important at 10 MeV. At 10 MeV, more than half of the source-weighted mean optical depth accumulates outside 15 km.

This supports a targeted strategy: do not spend equal effort on the 20--25 km profile for every mass. It is particularly relevant to the 10 MeV neutrino inverse-decay transport.

## 3. Fixed-(omega) versus path-redshift-only comparison

The path-redshift-only diagnostic replaces the local energy along the ray by
[
omega_{m loc}(r')=omega_srac{N(r_s)}{N(r')},
]
while retaining Euclidean chords. It is not the literal fixed-(omega) B.2 baseline and is not full GR.

| (m_V) | Fixed-(omega) strong-endpoint residual | Path-redshift-only residual | Change |
|---:|---:|---:|---:|
| 0.1 MeV | -36.162% | -39.346% | worsens by 3.184 percentage points |
| 1 MeV | -5.345% | -16.166% | worsens by 10.822 percentage points |
| 10 MeV | +92.241% | +36.745% | improves by 55.496 percentage points |

The energy-redshift diagnostic does **not** improve all masses. It moves the 10 MeV strong endpoint toward Fig. 7 but moves the 0.1 and 1 MeV endpoints farther below the reference. Therefore it cannot be adopted as a global correction merely because it improves the 10 MeV point.

The mass-dependent response is physically expected because the opacity composition changes from Compton-dominated at low masses to neutrino-inverse-decay-dominated at 10 MeV. It also demonstrates why a single global rescaling or a blanket path-redshift substitution would be unjustified.

## 4. Strong-absorption scale

The fixed-(omega) source-weighted mean optical depths at the strong endpoint are:

| (m_V) | Source-weighted mean (	au) | Strong-endpoint escape fraction |
|---:|---:|---:|
| 0.1 MeV | (4.349\times10^3) | (1.569\times10^{-7}) |
| 1 MeV | (7.736\times10^1) | (2.783\times10^{-5}) |
| 10 MeV | (1.614\times10^1) | (3.239\times10^{-4}) |

These means are diagnostics only. The luminosity is determined by the nonlinear angle- and energy-resolved average of (exp[-g_X^2	au]), not by exponentiating the mean (	au).

## 5. Decision and next checks

1. Complete the exact B.13 versus B.14--B.16 global comparison at 0.1 and 1 MeV. These are the masses where the paper says Compton absorption is relevant and where Compton dominates the current source and opacity.
2. Keep the 10 MeV B.13 result as a separate diagnostic; the 10 MeV opacity is neutrino dominated, so B.13 cannot by itself resolve the strong-endpoint discrepancy.
3. Keep fixed-(omega) B.2 as the published-formula baseline. The path-redshift-only result remains a non-universal sensitivity diagnostic.
4. Focus further outer-profile and neutrino-absorption work on the 10 MeV case, where 20--25 km contributes 28.9% of the source-weighted mean optical depth.
5. Do not modify the axial-vector production curve until the pure-vector Fig. 7 benchmark is understood.

No empirical correction is applied, and no raw Garching data are required to perform these method-level checks.


## 6. Analytic cancellation in the B.16 reduced Compton opacity

Combining the printed B.16 production rate, B.19 detailed balance, and B.4 reduced absorption gives a useful exact simplification within the B.14--B.16 approximation:

```
Gamma_prod = (1/vV) n_mu Fdeg [2/(exp(omega/T)-1)] sigma(mu gamma -> mu V)
Gamma_abs  = exp(omega/T) Gamma_prod
Gamma_abs* = (1-exp(-omega/T)) Gamma_abs
           = (exp(omega/T)-1) Gamma_prod
           = (2 n_mu Fdeg / vV) sigma(mu gamma -> mu V).
```

Using the B.14 cross section,
```
sigma(mu gamma -> mu V)
 = [8 pi alpha alphaV/(3 m_mu^2)]
   [1 + mV^2/(2 omega^2)] vV,
```
therefore
```
Gamma_abs*
 = [16 pi alpha alphaV/(3 m_mu^2)]
   (n_mu Fdeg) [1 + mV^2/(2 omega^2)].
```

The explicit Bose factor and the explicit thermal factor cancel in the reduced Compton absorption rate. Temperature and chemical potential remain through the susceptibility (n_\mu F_{\rm deg}). The optical-depth integrand in B.2 still contains the additional (1/v_V), so the path opacity is proportional to
```
Gamma_abs*/vV ∝ (n_mu Fdeg) [1 + mV^2/(2 omega^2)] / vV.
```

This clarifies the interpretation of the path-redshift test:
- it does not change a residual Bose enhancement in the reduced Compton opacity, because that factor cancels analytically;
- it changes the explicit finite-mass term and the B.2 (1/v_V) factor through the local energy;
- these changes are small for most of the low-mass thermal support but can be amplified by the nonlinear exponential escape probability near strong trapping.

The exact B.13 calculation does not inherit this cancellation in the same reduced closed form; its recoil and moving-muon phase space must be evaluated directly. This is another reason to keep the B.13-versus-B.16 global scan separate from the redshift-only diagnostic.
