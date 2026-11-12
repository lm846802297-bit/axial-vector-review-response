# Bollig original-source thermodynamic cross-check, 15--20 km (2026-11-09)

## Executive result

The Caputo SFHo-18.8 reconstruction agrees with the original Bollig Fig. 1 temperature and Fig. 4 muon degeneracy parameter throughout 15--20 km. Across 294 profile nodes, the mean absolute relative differences are 0.00431% for T and 0.00468% for mu_mu/T; the maximum absolute differences are 0.01628% and 0.01547%, respectively.

The independent absolute-density comparison remains in tension. Where Bollig Fig. 3 is above its lower plotting floor, 90 nodes through r=16.6031 km show that the relativistic Fermi density reconstructed from the published Fig. 1 and Fig. 4 curves exceeds the Fig. 3 curve by 10.38% on average, with a maximum of 12.11%. The same discrepancy is obtained using Caputo T and mu_mu. Fig. 3 reaches its 10^-7 fm^-3 lower plotting floor at r=16.6466 km; beyond that radius it is censored and cannot be treated as a pointwise density measurement.

This is a published-figure-level inconsistency among the three profile quantities. It is not resolved by changing T or mu_mu, because those two quantities independently match Bollig's original figures.

## 1. Source and numerical method

Source: Bollig et al., arXiv:2005.07141v7, Figs. 1, 3, and 4; Caputo et al., arXiv:2109.03244v3, Fig. 1.

The calculation uses the archived original Bollig PDF vector paths:
- Fig. 1 yellow SFHo-18.8 temperature curve;
- Fig. 3 yellow SFHo-18.8 absolute muon-density curve;
- Fig. 4 yellow SFHo-18.8 mu_mu/T curve.

The PDF vector axes are calibrated from the tick marks. At each profile node in 15--20 km, the Caputo T and mu_mu are compared to Bollig Fig. 1 and Fig. 4. The negative-muon density is then evaluated with the full relativistic Fermi--Dirac integral, including two spin states:
\[
n_{\mu^-}=\frac{1}{\pi^2}\int_0^\infty dp\,
\frac{p^2}{\exp[(\sqrt{p^2+m_\mu^2}-\mu_\mu)/T]+1}.
\]
The same integral is also evaluated using T from Bollig Fig. 1 and mu_mu=eta T from Bollig Fig. 4. No empirical rescaling is applied.

## 2. Temperature and degeneracy parameter

| Comparison | Nodes | Mean absolute relative difference | Maximum absolute relative difference |
|---|---:|---:|---:|
| Caputo T vs Bollig Fig. 1, 15--20 km | 294 | 0.004309% | 0.016280% |
| Caputo mu_mu/T vs Bollig Fig. 4, 15--20 km | 294 | 0.004684% | 0.015474% |

The agreement is maintained throughout the interval, not merely at the 15 km boundary. This independently supports the Caputo thermodynamic reconstruction for T and mu_mu/T in the 15--20 km interval.

## 3. Absolute density and the Fig. 3 plotting floor

The Fig. 3 logarithmic density axis has a lower plotting limit of 10^-7 fm^-3. The extracted yellow curve reaches this floor at approximately 16.6466 km. Points at the floor are therefore censored/upper-limit information, not measurements of the true density.

Of 294 profile nodes in 15--20 km:
- 90 nodes are above the Fig. 3 floor and can be used for a direct density comparison;
- 204 nodes are at the floor and are excluded from density residual summaries;
- the last node above the floor is at 16.603079 km;
- the first floor-censored node is at 16.646591 km.

For the 90 uncensored nodes, the density reconstructed from Caputo T,mu_mu is higher than Bollig Fig. 3 by:
- mean absolute relative difference: 10.402%;
- maximum absolute relative difference: 12.019%.

Using Bollig's own Fig. 1 T and Fig. 4 eta gives:
- mean absolute relative difference: 10.385%;
- maximum absolute relative difference: 12.108%.

The agreement between these two independently constructed Fermi densities shows that the residual is not caused by a mismatch between the Caputo and Bollig T or mu_mu/T curves.

Representative values:

| r (km) | Bollig Fig. 3 n_mu (fm^-3) | Fermi density from Bollig Fig. 1+4 (fm^-3) | Relative difference |
|---:|---:|---:|---:|
| 15.00 | 3.6602e-5 | 4.0123e-5 | +9.62% |
| 15.25 | 1.7582e-5 | 1.9338e-5 | +9.99% |
| 15.50 | 7.7473e-6 | 8.4916e-6 | +9.61% |
| 15.75 | 3.1394e-6 | 3.4687e-6 | +10.49% |
| 16.00 | 1.2165e-6 | 1.3444e-6 | +10.51% |
| 16.25 | 4.5398e-7 | 5.0184e-7 | +10.54% |
| 16.50 | 1.6452e-7 | 1.8195e-7 | +10.60% |

At 16.75--20 km, the extracted Fig. 3 curve is pinned to the 10^-7 fm^-3 lower plotting boundary while the Fermi-integral density falls below that value. The resulting apparent order-one residual is a plotting-floor artifact and is not a physical density discrepancy. No direct Fig. 3 pointwise density conclusion is made in this censored region.

## 4. Interpretation

The present comparison establishes:
1. The Caputo T(r) curve reproduces Bollig Fig. 1 in 15--20 km to better than 0.017%.
2. The Caputo mu_mu/T curve reproduces Bollig Fig. 4 in 15--20 km to better than 0.016%.
3. The Fermi density implied by those two published curves is about 10% above Bollig Fig. 3 until the latter reaches its plotting floor.
4. The Fig. 3 lower plotting floor prevents a pointwise density comparison beyond approximately 16.65 km.

The density residual is not removed by changing the B.1 density convention from n_mu- to n_mu- - n_mu+, since the positive-muon population is negligible in this degenerate outer shell. The discrepancy is also not a constant normalization factor established by the data; it remains a source-level inconsistency whose origin is not identified by the public plots.

The original Garching simulation tables remain unavailable. Possible differences in profile version, density definition, and figure data processing cannot be distinguished using the three published plots alone.

## 5. Consequences for B.1 and B.2

No density correction, opacity correction, or luminosity rescaling is justified. The baseline Caputo T and mu_mu fields remain the best-matched thermodynamic input for the Bollig SFHo-18.8 benchmark. The Fig. 3 density residual must remain an explicit systematic uncertainty/limitation of the public-profile reconstruction.

The B.1 implementation uses the one-negative-muon susceptibility convention in Blinov Eq. (B.17); the independent Fermi-integral closure remains at floating-point precision. This source-kernel algebraic closure does not resolve the profile-level Fig. 3 density discrepancy.

## 6. Historical impact estimate using the older profile (superseded)

The published-figure density tension is real, but it must not be translated directly into a 10% correction to the Compton rate. In the one-species convention used by the B.17 degeneracy factor,

\[
n_{\mu^-}F_{\rm deg}
=\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f_{\mu^-}(1-f_{\mu^-})
\equiv \chi_\mu(T,\mu_\mu).
\]

At fixed T and mu_mu, a different normalization assigned to n_mu is compensated by the corresponding inverse change in F_deg. The product entering the Compton source/absorption is the susceptibility, which is fixed by T and mu_mu. Thus the Fig. 3 residual alone does not justify rescaling n_mu F_deg or the Compton kernel. If the discrepancy instead reflects a genuinely different underlying profile, its T, mu_mu, and F_deg must be supplied consistently before a rate correction can be defined.

The older 10 MeV B.16 audit used profile SHA-256 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9 and found the following source/path weights:
- B.1 thin-source fraction from 15--18 km: 0.0036791%;
- B.1 thin-source fraction from 18--20 km: 0.0000931%;
- combined B.1 source fraction from 15--20 km: 0.0037722%;
- B.2 source-weighted mean optical-depth fraction accumulated in 15--20 km: 0.087305%.

As a conservative scale estimate, a 10% change in all 15--20 km opacity would change the total source-weighted mean optical depth by only about 0.00873% relative. At the strong endpoint, where the baseline source-weighted mean optical depth is about 1.76, this corresponds to an absolute mean-optical-depth shift of order 1.5e-4 and a sub-0.02% attenuation-scale effect. This is an estimate based on the shell-weight decomposition, not a new transport run; the affected density-supported region ends earlier, at 16.603 km, so the all-15--20 km estimate is conservative.

Consequently, the Fig. 3 mismatch remains an unresolved source-profile consistency issue worth documenting, but it is not a plausible explanation for the order-one strong-coupling Fig. 7 discrepancy in the current B.1/B.2 benchmark. No empirical correction is applied.

The source and path fractions above are taken from the archived 10 MeV fixed-omega B.16 global audit (profile SHA-256 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9). The separate 15--20 km profile comparison uses the vertex-preserving profile SHA-256 recorded in Section 1; the two profile fingerprints are not silently treated as identical.

## 7. Current vertex-preserving B.1/B.2 impact assessment

The current global B.16 benchmark is archived separately in `outputs/b16_global_fig7_vertex_preserving_10mev_2026-11-09.json`, with profile SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. Its channel composition differs substantially from the older profile audit; all current impact statements below use this vertex-preserving result.

For the current profile:
- B.1 source fractions in 15--18 km and 18--20 km are 1.6462% and 0.1772%, respectively (1.8234% combined, all source channels).
- B.2 total source-weighted mean optical-depth fraction in 15--20 km is 27.8619%.
- However, the 15--20 km B.2 optical depth is overwhelmingly neutrino inverse decay: 27.8538% of the total mean optical depth.
- The Compton opacity contribution from 15--20 km is only 0.0080846% of the total mean optical depth.
- In the density-comparison region 15--16.5 km, the Compton contribution is 0.0080023% of the total mean optical depth; the neutrino contribution in this shell is independent of the muon number-density discrepancy.

Thus the large 15--20 km total path contribution must not be attributed to the Fig. 3 muon-density residual. It is almost entirely the neutrino inverse-decay channel. The density mismatch can affect only the muon-Compton component.

At fixed T and mu_mu, the one-species B.17 relation is
\[
n_{\mu^-}F_{\rm deg}
=\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f_{\mu^-}(1-f_{\mu^-})
\equiv\chi_\mu(T,\mu_\mu).
\]
A change in the normalization assigned to n_mu is compensated by the inverse change in F_deg when the latter is consistently defined from the same distribution. The product entering the Compton source and absorption is therefore fixed by T and mu_mu. The published Fig. 3 residual alone does not justify a 10% rescaling of the Compton kernel.

As a deliberately conservative diagnostic, a hypothetical 10% change in all 15--16.5 km Compton opacity would change the total source-weighted mean optical depth by only 0.0008002% relative. At the strong endpoint, the baseline source-weighted mean optical depth is 16.1366; the corresponding absolute mean-optical-depth shift is approximately 1.29e-4. This is an attenuation-scale estimate, not a new transport run. A self-consistent alternative profile would have to change T, mu_mu, and F_deg consistently; no such replacement is supported by the public plots.

The current-profile conclusion is therefore narrower and better grounded: the Fig. 3 absolute-density mismatch remains an unresolved profile-level consistency issue, but the large 15--20 km B.2 contribution is not caused by it. No empirical density, source, opacity, or luminosity correction is applied.

## 8. Reproducibility and files

- Workflow: [Run 42557233565](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42557233565)
- Script: `audit_bollig_muon_density_and_b1_source.py`
- Machine-readable output: `outputs/bollig_muon_density_b1_source_audit_2026-11-09.json`
- Original vector paths: `outputs/bollig_fig3_fig4_vector_paths_2026-11-09.json`

The audit does not modify production rates, transport, the vector Fig. 7 comparison, or the axial-vector constraint outputs.
