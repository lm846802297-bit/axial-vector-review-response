> **Scope clarification (2026-11-09):** The Fig. 4 result validates the \(\mu_\mu/T\) profile, not the entire thermodynamic background. A subsequent direct comparison finds that Caputo \(T(r)\) also matches Bollig Fig. 1 at below 0.01%, while the absolute density in Bollig Fig. 3 is about 5% lower on average over 5--15 km and about 8.8% lower over 12--15 km than Caputo's curve. Caputo's plotted density is internally consistent with its own relativistic Fermi integral to below 0.54%. The Fig. 3 discrepancy remains unresolved and must not be removed by rescaling. See [the complete density and B.1 source audit](BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md). The conclusions below concerning Fig. 4 remain valid specifically for \(\mu_\mu/T\).

# Independent original-source cross-check of the SFHo-18.8 muon degeneracy profile

Date: 2026-11-09  
Source: Bollig et al., arXiv:2005.07141v7, Fig. 4.  
Status: **the Caputo baseline \(\mu_\mu/T\) profile agrees with the original Bollig Fig. 4 to better than \(3\times10^{-4}\) relative over 12--15 km. The Ferreira-digitized profile does not. This resolves the earlier apparent ambiguity in favor of the Caputo profile for the present SFHo-18.8, 1 s benchmark.**

## 1. Why Fig. 4 is the decisive comparison

The previous profile audit found that Caputo and Ferreira label their curves as SFHo-18.8 at 1 s post-bounce, but their digitized \(\mu_\mu(r)\) values differ by roughly 9.5--17.2% over 12--15 km.

A more direct source-level test is available in the original Bollig paper. Its Fig. 4 plots the muon degeneracy parameter \(\mu_\mu/T\) directly for the four supernova models, including SFHo-18.8. This avoids comparing two separately digitized quantities and is the quantity controlling the muon Fermi distribution in the Compton suppression factor.

The source paper states that the full profile data are available from the Garching archive and identifies SFHo-18.8 as one of its simulation models. The consolidated arXiv v7 PDF also explicitly notes that it incorporates the published erratum and later corrections.

## 2. Reproducible digitization of Bollig Fig. 4

The source PDF is downloaded from:

https://arxiv.org/pdf/2005.07141v7

PDF SHA-256:

8267f8b1de184163308728c44000425ce58085c1d5bd799d0cbc1e4e8d740d61

The PDF vector path for the yellow SFHo-18.8 curve in Fig. 4 is drawing path 193 on page index 2. The axis calibration is taken from the printed tick labels:

- Radius ticks: 5, 10, 15, 20 km.
- Degeneracy ticks: \(-4,-2,0,2,4\).
- The plotted axes are linear in both radius and \(\mu_\mu/T\).

The extracted path is interpolated linearly in PDF coordinates and mapped to physical axes. The complete path inventory, including all vector vertices and text bounding boxes, is archived in:

outputs/bollig_fig3_fig4_vector_paths_2026-11-09.json

The digitization script is:

audit_bollig_muon_profile_crosscheck.py

## 3. Direct comparison in the sensitive 12--15 km interval

At each existing reconstructed-profile CSV node in 12--15 km, compare the digitized Bollig Fig. 4 value with:

\[
\left(\frac{\mu_\mu}{T}\right)_{\rm Caputo}
=\frac{\mu_{\mu,\rm Caputo}}{T_{\rm Caputo}},
\qquad
\left(\frac{\mu_\mu}{T}\right)_{\rm Ferreira}
=\frac{\mu_{\mu,\rm Ferreira}}{T_{\rm Ferreira}}.
\]

The results over 97 profile nodes are:

| Comparison with Bollig Fig. 4 | Mean absolute relative difference | Maximum absolute relative difference |
|---|---:|---:|
| Caputo reconstruction | \(5.18\times10^{-5}\) (0.00518%) | \(1.43\times10^{-4}\) (0.01434%) |
| Ferreira reconstruction | 12.74% | 17.18% |

Representative values:

| \(r\) (km) | Bollig Fig. 4 \(\mu_\mu/T\) | Caputo \(\mu_\mu/T\) | Ferreira \(\mu_\mu/T\) |
|---:|---:|---:|---:|
| 8.0 | 2.3624 | 2.3630 | 4.3095 |
| 10.0 | 3.0308 | 3.0313 | 3.8669 |
| 12.0 | 3.6079 | 3.6075 | 4.2271 |
| 12.5 | 3.7780 | 3.7776 | 4.3525 |
| 13.0 | 3.9524 | 3.9518 | 4.4910 |
| 14.0 | 4.3399 | 4.3397 | 4.8148 |
| 15.0 | 4.7073 | 4.7072 | 5.1844 |

The agreement of the Caputo reconstruction with the original Bollig curve is at the level expected when the same underlying simulation profile is being digitized independently. The Ferreira curve differs visibly and systematically.

## 4. Interpretation: the baseline profile choice is no longer ambiguous

This comparison establishes the following specifically for the degeneracy parameter (the absolute-density comparison is treated separately in BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md):

1. The Caputo \(\mu_\mu/T\) profile reproduces the original Bollig SFHo-18.8 degeneracy curve over the interval most relevant to the present transport calculation.
2. The Ferreira digitization does not reproduce that original Fig. 4 curve.
3. The earlier 9.5--17.2% difference in \(\mu_\mu\) should therefore not be treated as two equally plausible reconstructions of the same numerical background for this calculation.
4. The Caputo \(T,\mu_\mu\) pair remains the correct baseline reconstruction for the current Bollig SFHo-18.8, \(t_{\rm pb}=1\) s comparison.
5. The Ferreira curve remains useful as a diagnostic of a distinct published profile representation, but it must not replace the baseline or be used to tune the opacity.

This resolves the choice of the \\(\\mu_\\mu/T\\) profile for the present benchmark. It does not resolve the absolute-density discrepancy in Bollig Fig. 3. It does not prove that every radial and thermodynamic variable in the reconstructed profile exactly reproduces the original private Garching tables.

## 5. Consequences for the previous B.1+B.2 sensitivity tests

The controlled sensitivity calculations remain valid as numerical diagnostics:

- Setting \(\mu_{\nu_\mu}=0\) in 12--15 km changes the strong-endpoint escape probability by only about \(1.1\times10^{-4}\) fractionally.
- Extending the unresolved \(\mu_{\nu_\mu}\) branch to the 1 MeV plotting-floor envelope has a similarly negligible effect.
- Replacing the Caputo \(\mu_\mu\) curve by the Ferreira curve changes the B.1 source and B.2 escape probability appreciably.

However, the Ferreira substitutions B and B2 are now clearly **off-baseline profile diagnostics**, not candidate corrections to the original Bollig background. Their changes in luminosity must not be interpreted as a physical correction to the Fig. 7 vector curve.

In particular, the B2 result that changes the escaped B.1 integral by roughly 15.5% is not evidence that the baseline opacity is wrong. It quantifies the sensitivity to a profile that fails the direct original-source \(\mu_\mu/T\) cross-check.

## 6. Updated decisions

1. Retain Caputo \(T,\mu_\mu,\mu_{\nu_\mu}\) as the baseline reconstruction for the SFHo-18.8, 1 s profile.
2. Remove the earlier description of the Caputo--Ferreira \(\mu_\mu\) difference as an unresolved two-way profile ambiguity. The original Bollig Fig. 4 selects the Caputo curve for this benchmark.
3. Keep the Ferreira substitution results in the audit archive, clearly labeled as non-baseline sensitivity diagnostics.
4. Do not rescale B.1, B.2, any absorption channel, or the total luminosity.
5. Keep the vector Fig. 7 reproduction and the axial-vector cooling curve frozen until the remaining inner-path transport and source discrepancies are independently resolved.

## 7. Remaining checks

The next independent cross-check is to compare the Caputo and Bollig muon number-density curves directly using Bollig Fig. 3, and then to inspect the \(\mu_\mu/T\) agreement over the full 5--15 km region rather than only 12--15 km. The current Fig. 4 result already establishes the baseline choice in the sensitive shell.

No production rate, transport implementation, reference luminosity, or axial-vector output is changed by this audit.
