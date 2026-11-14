# B.13 exact moving-muon Compton audit on the vertex-preserving profile

Date: 2026-11-09  
Status: **local radial comparison completed and numerically converged at the sampled points.** This establishes that the B.13 versus B.14--B.16 difference is non-negligible in the inner production region at \(m_V=10\) MeV. It does not yet provide a source-weighted full-path luminosity correction.

> **Historical local-kernel record (2026-11-15):** the later full-profile B.13/B.2 global work is archived in PR #113, merged on 2026-11-14. This note remains a sampled local radial comparison, not a global luminosity correction or final Fig. 7 validation.

## 1. Input and scope

- \(m_V=10\) MeV.
- Current profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Profile: 1687-row vertex-preserving reconstruction.
- Radial samples: 8, 10, 12.5, 15, 18.5, 20, and 22 km.
- Energy samples: 12, 15, 20, 30, 50, and 80 MeV.
- B.13: exact moving-muon phase-space Compton kernel, with \(\mu^-\) and \(\mu^+\) evaluated separately.
- B.14--B.16: the reference no-recoil approximation used by the scalar baseline.

The purpose is to compare both production and reduced absorption. Replacing only the opacity while retaining the old Compton source would not be a self-consistent B.1/B.2 update.

## 2. Representative local comparisons

The ratio in the third column is the exact B.13 \(\mu^-\) production rate divided by the B.16 reference rate. The fourth column is the change in the **total local reduced opacity** (neutrino inverse decay plus Compton) when the B.16 \(\mu^-\) Compton opacity is replaced by the exact B.13 \(\mu^-\) result.

| \(r\) (km) | \(\omega\) (MeV) | B.13/B.16 \(\mu^-\) production | Change in total local opacity |
|---:|---:|---:|---:|
| 8 | 12 | 0.43151 | -24.21% |
| 8 | 20 | 0.45960 | -20.75% |
| 10 | 12 | 0.45550 | -20.22% |
| 10 | 20 | 0.48117 | -17.24% |
| 12.5 | 12 | 0.56638 | -5.20% |
| 12.5 | 20 | 0.58215 | -4.34% |
| 15 | 20 | 0.70378 | -0.063% |
| 18.5 | 20 | 0.74843 | \(-2.0\times10^{-8}\)% |
| 22 | 20 | 0.75094 | numerically zero |

Across the 24 sampled points in 8--15 km, the B.13/B.16 \(\mu^-\) production ratio ranges from 0.375 to 0.723. The B.13 \(\mu^-\) replacement changes the total local opacity by between -24.28% and -0.063%, depending on radius and energy.

The effect is concentrated in the inner region. At 8 km the B.16 Compton contribution is about 37--43% of the total local opacity in the displayed energy range; by 12.5 km it is about 10--12%, and by 15 km it is about 0.2%. At 18.5--22 km the Compton contribution is negligible compared with neutrino inverse decay.

## 3. Positive-muon contribution

The \(\mu^+\) contribution is small compared with the \(\mu^-\) contribution:

- At 8 km it is about 1.30% of the exact B.13 Compton reduced absorption.
- At 10 km it is about 0.38%.
- At 12.5 km it is about 0.072%.
- At 15 km it is about 0.0084%.

It is therefore a small correction in the dominant inner region and does not change the qualitative B.13/B.16 comparison.

## 4. Numerical validation

| Check | Maximum relative residual |
|---|---:|
| B.13 \(\mu^-\) absorption versus production | \(1.92\times10^{-15}\) |
| B.13 \(\mu^+\) absorption versus production | \(2.83\times10^{-15}\) |
| B.13 \(\mu^-\) detailed balance | \(1.90\times10^{-15}\) |
| B.13 \(\mu^+\) detailed balance | \(3.05\times10^{-15}\) |
| Final muon-shell closure | \(1.42\times10^{-13}\) |

The base quadrature uses orders \([12,8,8,8]\), and the refined check uses \([16,10,10,10]\). The largest displayed refinement change is 0.208% for \(\mu^-\) at \(r=8\) km and \(\omega=15\) MeV; the other two representative checks are at or below 0.021%. The reported local comparisons use the refined calculation.

## 5. Physical interpretation

The exact B.13 kernel changes both sides of the Compton process:

1. It lowers the local Compton production rate relative to B.16, which tends to lower the B.1 source.
2. It also lowers the local Compton reduced absorption, which tends to increase the B.2 escape probability.

These effects compete. The local opacity reduction alone cannot determine the change in escaped luminosity. In particular, it would be incorrect to insert the B.13 opacity into B.2 while leaving the B.16 Compton source in B.1 unchanged.

The outer 22--25 km shell is not where this approximation matters: the Compton contribution there is negligible. The relevant region is 8--15 km, which supplies about 79.6% of the B.1 source in the current vector benchmark.

The B.13/B.16 difference is large enough to justify a separate source-weighted inner-region study if a quantitatively controlled 10 MeV vector prediction is required. It is not, by itself, an explanation of the full \(+92.24\%\) strong-endpoint Fig. 7 luminosity discrepancy. A consistent integrated calculation must update production and absorption together.

## 6. Decision

- Keep the literal B.14--B.16 implementation as the Fig. 7 reproduction baseline.
- Retain the B.13 exact calculation as a separate, more complete local-kernel diagnostic.
- Do not apply an empirical multiplicative correction to the Compton source or opacity.
- Before using B.13 in a global luminosity result, construct and validate a source-weighted approximation/interpolation over the relevant \(r,\omega\) domain, then replace both the B.1 Compton source and B.2 Compton absorption consistently.
- Do not update the axial-vector constraint curve at this stage.

Machine-readable current-profile output:

`outputs/b13_exact_compton_opacity_radial_vertex_preserving_10mev_2026-11-09.json`

Related records:

- `B16_OUTER_SHELL_POLARIZATION_RESOLVED_AUDIT_2026-11-09.md`
- `B16_INNER_PATH_CHANNEL_DIRECTIONAL_AUDIT_VERTEX_PRESERVING_2026-11-09.md`
- `FIG7_VECTOR_BENCHMARK_REEVALUATION_2026-11-09.md`
- `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`
