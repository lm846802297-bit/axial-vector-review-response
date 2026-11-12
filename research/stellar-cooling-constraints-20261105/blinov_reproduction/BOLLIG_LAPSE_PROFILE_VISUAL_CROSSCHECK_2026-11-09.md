# Independent lapse-profile visual cross-check for SFHo-18.8 (2026-11-09)

## Executive result

The current profile's lapse column is taken from the Ferreira/SFHo-18.8 public-figure reconstruction. A second public visualization is now identified: Zuowei Liu's 31 October 2026 presentation, slide 65, titled "The SFHo-18.8 SN profiles (SN core)". It explicitly plots the lapse factor against radius from 0 to 20 km and attributes the SFHo-18.8 profiles to Bollig et al., arXiv:2005.07141, and the Garching core-collapse supernova research archive.

The black lapse curve in that presentation visually agrees with the current profile's lapse values over 0--20 km. Representative profile values are 0.7363, 0.7587, 0.8114, 0.8635, and 0.8989 at 0, 5, 10, 15, and 20 km, respectively. The presentation graph reads approximately 0.735, 0.76, 0.81, 0.865, and 0.90 at those radii. The differences are at the level of the visual read-off resolution (roughly a few 10^-3).

This is a qualitative independent-source cross-check, not a high-precision numerical digitization: the PDF is a presentation slide with a rasterized plot, and its plotted axis is not supplied as machine-readable data. The slide's citation and attribution make it useful corroboration, but it is not a substitute for the original Garching lapse table.

## 1. Independent source

- Zuowei Liu, "Supernova constraints on millicharged particles and lepton-flavor-violating axions", 7th Joint Workshop on the Standard Model and Beyond, Nanjing, 31 October 2026.
- Slide 65: "The SFHo-18.8 SN profiles (SN core)".
- The slide plots chemical potentials, temperature, proton/electron effective masses, proton self-energy, and the lapse factor over 0--20 km.
- The slide explicitly cites Bollig, DeRocco, Graham, and Janka, arXiv:2005.07141, and the Garching core-collapse supernova research archive.

Source: [presentation PDF, slide 65](https://indico.ihep.ac.cn/event/29150/contributions/234054/attachments/108992/148044/5th_261031-SN-MCP-LFVALP-Nanjing-Zuowei-Liu.pdf).

## 2. Representative comparison

The presentation graph is read visually, so its values are approximate.

| Radius (km) | Presentation visual read-off | Current profile lapse | Difference (profile - read-off) |
|---:|---:|---:|---:|
| 0 | approx. 0.735 | 0.73633 | +0.00133 |
| 5 | approx. 0.760 | 0.75868 | -0.00132 |
| 10 | approx. 0.810 | 0.81136 | +0.00136 |
| 15 | approx. 0.865 | 0.86350 | -0.00150 |
| 20 | approx. 0.900 | 0.89889 | -0.00111 |

The plot resolution and line thickness do not support a meaningful fit residual below a few 10^-3. The agreement is therefore described as visual consistency, not a precision validation.

The current profile values at intermediate radii are:
- 16 km: 0.87215
- 17 km: 0.87999
- 18 km: 0.88701
- 19 km: 0.89327

These values follow the same smooth, monotonic rise visible in the independent plot.

## 3. What is and is not validated

Validated at the level of an independent public visualization:
1. The current lapse profile has the correct radial trend and normalization over 0--20 km.
2. Its 15--20 km values are visually consistent with a separate presentation of the same SFHo-18.8 Garching model.
3. The lapse column is not an arbitrary extrapolation imported from an unrelated supernova model.

Not validated:
1. A machine-precision comparison to the original Garching lapse table.
2. The 20--22 km continuation, which lies outside the presentation's plotted radial interval.
3. Any full-GR propagation prescription. The current B.2 baseline remains the fixed-omega, straight-chord prescription from the paper.

No lapse values are changed or rescaled.

## 4. Consequence for the current audit

The 15--20 km profile uncertainty is now more constrained than before: T and mu_mu/T match Bollig Figs. 1 and 4 quantitatively, and the lapse curve is independently corroborated visually. The remaining Fig. 3 absolute muon-density discrepancy is separate and has a very small effect on the current-profile outer-shell Compton opacity, as quantified in the vertex-preserving B.16 channel decomposition.

The main unresolved reproduction issue is therefore not an obvious lapse-profile mismatch. It remains the strong-coupling difference between the paper-faithful fixed-omega B.16 global calculation and Fig. 7.

No production source, absorption rate, path integral, coupling, luminosity, or axial-vector constraint is modified.
