# Global B.13 exact Compton source-and-opacity audit

Date: 2026-11-09  
Status: **completed for the 10 MeV pure-vector benchmark.** The calculation updates the Compton production and reduced-absorption terms together, while retaining the published scalar, polarization-summed Eq. (B.2) transport prescription. It is a controlled alternative-kernel calculation, not a new Fig. 7 reproduction claim and not an axial-vector result.

## 1. Purpose and physical convention

The local radial comparison showed that the exact moving-muon Compton kernel in Eq. (B.13) differs substantially from the non-relativistic, no-recoil approximation in Eqs. (B.14)--(B.16) at \(m_V=10\) MeV. The paper itself motivates dropping recoil and \(O(m_V^2/\omega^2)\) terms because the Compton channel is expected to matter primarily for \(m_V\lesssim\) MeV. The 10 MeV benchmark is therefore a useful test of the approximation outside its stated regime.

The global calculation replaces both sides of the Compton process:

- Eq. (B.1): the local Compton production rate in the source.
- Eq. (B.2): the Compton reduced-absorption rate in the ray optical depth.

The neutrino inverse-decay source and opacity are unchanged. The calculation keeps the fixed-\(\omega\) path convention and the scalar polarization-summed opacity used in the published equations. It does not substitute the separate mode-resolved transport diagnostic.

### Charge conventions

The two charge cases are kept distinct:

1. **\(\mu^-\) only:** the like-for-like comparison with the single negative-muon distribution in Eq. (B.17).
2. **\(\mu^-+\mu^+\):** an additional charge-summed thermal-gas calculation.

The second case is an extension, not the Eq. (B.17) reference convention. The older local comparison report used a two-charge susceptibility and is explicitly marked as such in the file **finite_mixing/B13_B14_LOCAL_COMPARISON_2026-11-08.md**.
The same-grid B.16 source decomposition gives a Compton fraction of 32.005%; the preceding local report's 18.6% global-share estimate is withdrawn because it cannot be traced to the archived B.1 source decomposition. The direct global B.13 integration reported below supersedes any estimate obtained by multiplying local emissivity ratios by a global channel fraction.

## 2. Fixed inputs and numerical setup

| Input | Value |
|---|---|
| Mediator mass | \(m_V=10\) MeV |
| Current | Pure vector, \(g_V=1,\ g_A=0\), rates per \(g_X^2\) |
| SFHo profile | 1687-row vertex-preserving public-figure reconstruction |
| Profile SHA-256 | 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c |
| Radial quadrature | 40-point composite Gauss rule |
| Energy grid | 142 nodes, 10.00001--1010 MeV |
| Angular quadrature | 16 points |
| Path quadrature | 32 points |
| Exact B.13 kernel orders | \((12,8,8,8)\) |
| Refined local checks | \((16,10,10,10)\) |
| Exact kernel evaluations | 2106 |

The active B.13 calculation covers 27 radial nodes from 0 to 18.660 km and 78 energy nodes above the global emission threshold \(10.87335\) MeV.

At the remaining 15 outer radial nodes, the B.16 Compton term is retained only where its maximum local fraction of total reduced opacity is below \(6.84\times10^{-10}\). The corresponding omitted B.16 Compton contribution is \(3.34\times10^{-14}\) of the total B.16 Compton source and \(2.31\times10^{-12}\) of the source-weighted mean optical depth. This numerical truncation is negligible for the reported benchmark.

## 3. B.16 baseline closure

Before inserting B.13, the script reproduces the archived B.16 calculation on the same radial and energy grids:

\[
\max_i\left|
\frac{L^{\rm recomputed}_{i,\mathrm{B16}}-
L^{\rm archived}_{i,\mathrm{B16}}}
{L^{\rm archived}_{i,\mathrm{B16}}}
\right|=0.
\]

This is a code-to-archive closure check. It does **not** mean that the B.16 curve agrees with the published Fig. 7 curve.

## 4. Global luminosity results

All luminosity differences below are relative to the digitized Fig. 7 reference values.

| Point | B.16 reference implementation | B.13 \(\mu^-\), consistent source + opacity | B.13 \(\mu^-+\mu^+\), consistent source + opacity |
|---|---:|---:|---:|
| Weak endpoint | \(-8.885\%\) | \(-28.109\%\) | \(-28.042\%\) |
| Fig. 7 peak | \(+2.569\%\) | \(-16.340\%\) | \(-16.272\%\) |
| Strong endpoint | \(+92.241\%\) | \(+131.530\%\) | \(+131.591\%\) |
| Mean absolute relative difference over the curve | \(15.732\%\) | \(30.259\%\) | \(30.218\%\) |

Representative calculated luminosities:

| Point | B.16 | B.13 \(\mu^-\) | B.13 \(\mu^-+\mu^+\) |
|---|---:|---:|---:|
| Weak endpoint | \(9.9254\times10^{51}\) | \(7.8313\times10^{51}\) | \(7.8386\times10^{51}\) |
| Fig. 7 peak | \(1.9601\times10^{54}\) | \(1.5987\times10^{54}\) | \(1.6000\times10^{54}\) |
| Strong endpoint | \(2.4373\times10^{52}\) | \(2.9354\times10^{52}\) | \(2.9361\times10^{52}\) |

Units are \(\mathrm{erg\,s^{-1}}\).

**Main result:** the consistent B.13 replacement does not remove the B.16--Fig. 7 discrepancy. At the strong endpoint, it increases the calculated luminosity by about 20.4% relative to the B.16 implementation and changes the Fig. 7 discrepancy from \(+92.24\%\) to \(+131.53\%\). The B.13 calculation is an alternative physical prediction at 10 MeV; it is not expected to reproduce a published curve evaluated with Eqs. (B.14)--(B.16).

## 5. Separate source and opacity effects

The seven-way comparison isolates the competing effects:

| Variant | Weak endpoint | Fig. 7 peak | Strong endpoint |
|---|---:|---:|---:|
| B.16 reference | \(-8.89\%\) | \(+2.57\%\) | \(+92.24\%\) |
| B.13 \(\mu^-\), source only | \(-28.12\%\) | \(-22.17\%\) | \(+25.15\%\) |
| B.13 \(\mu^-\), opacity only | \(-8.87\%\) | \(+10.56\%\) | \(+273.08\%\) |
| B.13 \(\mu^-\), source + opacity | \(-28.11\%\) | \(-16.34\%\) | \(+131.53\%\) |
| B.13 \(\mu^-+\mu^+\), source only | \(-28.05\%\) | \(-22.09\%\) | \(+25.26\%\) |
| B.13 \(\mu^-+\mu^+\), opacity only | \(-8.87\%\) | \(+10.54\%\) | \(+272.72\%\) |
| B.13 \(\mu^-+\mu^+\), source + opacity | \(-28.04\%\) | \(-16.27\%\) | \(+131.59\%\) |

The source-only and opacity-only rows are diagnostic counterfactuals, not self-consistent predictions. The consistent source-plus-opacity rows are the physically relevant comparison.

For the like-for-like \(\mu^-\)-only case:

\[
\frac{L_{\rm thin}^{\rm B13}}{L_{\rm thin}^{\rm B16}}
=0.78898.
\]

Thus the total optically thin source decreases by \(21.10\%\). The B.16 Compton source contributes \(32.005\%\) of the B.16 total source, while the B.13 \(\mu^-\) Compton source contributes \(13.819\%\) of the B.13 total source. Accounting for the change in total source normalization, the integrated B.13 \(\mu^-\) Compton source is only \(34.07\%\) of the B.16 Compton source.

At the strong endpoint:

\[
P_{\rm esc}^{\rm B16}=3.23921\times10^{-4},\qquad
P_{\rm esc}^{\rm B13}=4.94463\times10^{-4},
\]

so

\[
\frac{P_{\rm esc}^{\rm B13}}{P_{\rm esc}^{\rm B16}}
=1.52649.
\]

The effective optical depth inferred from the source-weighted escape fraction decreases by

\[
\Delta\tau_{\rm eff}
=-\ln\left(\frac{P_{\rm esc}^{\rm B13}}{P_{\rm esc}^{\rm B16}}\right)
=-0.42297.
\]

The decrease in Compton production lowers the source, but the reduction in Compton absorption increases the strong-coupling escape probability. The escape enhancement dominates in the strong endpoint.

## 6. Radial origin of the B.13 effect

The source-weighted shell comparison identifies the important region. The ratio in the fourth column is the B.13 \(\mu^-\) Compton source divided by the B.16 Compton source within that emission shell.

| Emission shell (km) | B.16 total B.1 source fraction | B.13 total B.1 source fraction | B.13/B.16 Compton source | Strong-endpoint \(P_{\rm esc}\), B.16 | Strong-endpoint \(P_{\rm esc}\), B.13 |
|---|---:|---:|---:|---:|---:|
| 0--5 | 0.91% | 1.13% | 0.434 | \(1.25\times10^{-5}\) | \(3.45\times10^{-5}\) |
| 5--8 | 17.51% | 17.57% | 0.334 | \(1.80\times10^{-4}\) | \(4.37\times10^{-4}\) |
| 8--10 | 39.81% | 35.37% | 0.325 | \(4.02\times10^{-4}\) | \(7.20\times10^{-4}\) |
| 10--12 | 26.08% | 26.90% | 0.367 | \(3.80\times10^{-4}\) | \(4.54\times10^{-4}\) |
| 12--15 | 13.72% | 16.53% | 0.435 | \(1.61\times10^{-4}\) | \(1.61\times10^{-4}\) |
| 15--18 | 1.65% | 2.09% | 0.576 | \(9.27\times10^{-6}\) | \(9.26\times10^{-6}\) |
| 18--25 | 0.32% | 0.41% | 0.713 | \(3.35\times10^{-3}\) | \(3.35\times10^{-3}\) |

The 18--25 km source contribution is very small; the outermost inactive nodes retain B.16 Compton rates under the \(10^{-8}\) local-opacity threshold described above.

The largest B.13/B.16 Compton-source suppression occurs in the 5--10 km region. This region also has a substantial strong-coupling source weight. The corresponding increase in escape probability is largest in the 5--10 km shells. The 10--15 km shells show partial cancellation between the changed source distribution and changed escape probability.

The radial decomposition therefore explains why a local rate ratio at a single radius cannot predict the global luminosity correction.

At the strong endpoint, the corresponding shell contributions to the escaped luminosity are:

| Emission shell (km) | B.16 escaped luminosity (\(\mathrm{erg\,s^{-1}}\)) | B.13 \(\mu^-\) escaped luminosity (\(\mathrm{erg\,s^{-1}}\)) |
|---|---:|---:|
| 0--5 | \(8.58\times10^{48}\) | \(2.31\times10^{49}\) |
| 5--8 | \(2.37\times10^{51}\) | \(4.56\times10^{51}\) |
| 8--10 | \(1.20\times10^{52}\) | \(1.51\times10^{52}\) |
| 10--12 | \(7.46\times10^{51}\) | \(7.25\times10^{51}\) |
| 12--15 | \(1.67\times10^{51}\) | \(1.58\times10^{51}\) |
| 15--18 | \(1.15\times10^{49}\) | \(1.15\times10^{49}\) |
| 18--25 | \(8.18\times10^{50}\) | \(8.18\times10^{50}\) |

The increase in the total strong-endpoint luminosity is dominated by the 5--10 km shells. The 10--15 km shells partially offset this increase, while the 18--25 km contribution is unchanged at the displayed precision.


## 7. Opacity-weighted diagnostics

With the B.16 source distribution held fixed, replacing only the Compton opacity gives

\[
\langle\tau_{\rm C}^{\rm B16\ source}\rangle_{\rm B16}
=9.47794\times10^{14},\qquad
\langle\tau_{\rm C}^{\rm B16\ source}\rangle_{\rm B13}
=3.42080\times10^{14}.
\]

Thus the source-weighted Compton optical depth falls by about \(63.9\%\) at fixed B.16 source weighting. With the B.13 source distribution and B.13 opacity used together, the corresponding mean is \(3.40866\times10^{14}\).

The source-weighted mean **total** optical depth, evaluated with each calculation's own source distribution, changes from

\[
\langle\tau_{\rm total}\rangle_{\rm B16}
=9.27229\times10^{15},\qquad
\langle\tau_{\rm total}\rangle_{\rm B13}
=9.08614\times10^{15},
\]

a reduction of about \(2.01\%\). This comparison includes both the opacity change and the changed source weighting. Neutrino inverse decay remains the dominant contribution to the mean total opacity. Nevertheless, the direction- and energy-dependent escape probability is nonlinear, so a small change in the source-weighted mean total optical depth does not imply a comparably small change in the strong-coupling escape fraction.

These mean optical depths are diagnostics only; the luminosity is evaluated with the full angularly averaged exponential, not by exponentiating a mean optical depth.

## 8. Positive-muon contribution

The \(\mu^+\) contribution is small:

\[
\frac{Q_{\mu^+}}{Q_{\mu^-}+Q_{\mu^+}}
=0.672\%
\]

for the integrated B.13 Compton source in the current benchmark.

The \(\mu^-+\mu^+\) consistent result changes the strong-endpoint luminosity by only about \(0.026\%\) relative to the \(\mu^-\)-only result. The single-negative-muon Eq. (B.17) convention is therefore an adequate like-for-like baseline for this benchmark; the two-charge extension is retained as a small physical correction.

## 9. Numerical validation

| Check | Result |
|---|---:|
| B.16 recomputation versus archived B.16 output | Exact closure, maximum relative residual 0 |
| B.13 \(\mu^-\) mode-resolved detailed balance | \(1.39\times10^{-14}\) |
| B.13 \(\mu^+\) mode-resolved detailed balance | \(1.53\times10^{-14}\) |
| B.13 \(\mu^-\) absorption/production closure | \(1.37\times10^{-14}\) |
| B.13 \(\mu^+\) absorption/production closure | \(1.44\times10^{-14}\) |
| Final muon-shell closure | \(3.71\times10^{-13}\) |
| Angular-weight normalization residual | 0 |

Refinement from \((12,8,8,8)\) to \((16,10,10,10)\) changes the \(\mu^-\) production rate by:

- \(0.206\%\) at \(r=8\) km, \(\omega=15\) MeV;
- \(0.0205\%\) at \(r=12.5\) km, \(\omega=20\) MeV;
- \(0.0158\%\) at \(r=15\) km, \(\omega=30\) MeV.

The largest sampled refinement change is much smaller than the global differences discussed above, but a dedicated energy- and radial-grid convergence scan remains appropriate before treating the B.13 result as a final precision prediction.

## 10. Interpretation and decision

1. The B.13 exact moving-muon kernel materially changes the 10 MeV Compton source and opacity.
2. The consistent B.13 source-plus-opacity replacement does not resolve the independent B.16--Fig. 7 discrepancy. It increases the strong-endpoint excess from \(+92.24\%\) to \(+131.53\%\).
3. The source-only result must not be used as a correction because it leaves the B.16 opacity unchanged. The opacity-only result is likewise a counterfactual.
4. The positive-muon correction is negligible for the current benchmark.
5. The published scalar mode-summed Eq. (B.2) prescription is retained for this comparison. The separate polarization-resolved propagation result remains an extension, not a replacement for the published Fig. 7 baseline.
6. No empirical source, opacity, coupling, or luminosity rescaling is applied.
7. No production axial-vector curve or referee-response result is modified.

The published paper states that Eq. (B.13) sums over polarization states, that the factor of three in the inverse-decay production rate accounts for the difference between polarization-summed thermal production and the polarization-averaged vacuum decay width, and that Eq. (B.14) is the non-relativistic/no-recoil approximation usually used when \(m_V\lesssim\) MeV. See [arXiv:2511.09619, Appendix B](https://arxiv.org/abs/2511.09619), Eqs. (B.6)--(B.19). The current calculation follows the single-\(\mu^-\) Eq. (B.17) convention in its like-for-like case.

## 11. Next steps

The next priority is not another empirical adjustment to the Compton rate. It is to:

1. Complete a dedicated radial- and energy-grid convergence scan for the global B.13 source-and-opacity calculation.
2. Keep the published scalar, polarization-summed B.2 implementation as the vector Fig. 7 reproduction baseline, while retaining the mode-resolved result as a separate transport extension.
3. Revisit the remaining B.16--Fig. 7 difference through the source-weighted neutrino inverse-decay path contributions and the independently reconstructed background inputs.
4. Only after the pure-vector benchmark is understood, evaluate the axial-vector kernel. No axial-vector constraint curve is updated in this report.

## 12. Reproducibility

- Full machine-readable local-rate grid and global result: **outputs/b13_global_transport_vertex_preserving_10mev_2026-11-09.json**
- Compact summary: **outputs/b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json**
- Calculation script: **audit_b13_global_transport.py**
- Summary extractor: **summarize_b13_global_transport.py**
- Workflow: **.github/workflows/b13-global-transport-vertex-preserving.yml**
- Summary workflow: **.github/workflows/b13-global-transport-summary.yml**

The work remains on the Draft PR #57 branch. No merge is performed.
