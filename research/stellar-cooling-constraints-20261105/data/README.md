# Public-figure reconstruction of the SFHo-18.8 profile

**Date:** 2026-11-06. **Identity:** a reproducible, reconstructed profile benchmark at 1 s post-bounce. These files are **not** the original simulation tables.

The Garching raw radial-profile archive requires authorization. No restricted tables or access credentials were obtained, bypassed, or redistributed. The present numerical inputs are derived from the vector paths already included in public paper figures.

## Baseline file and columns

sfho188_digitized.csv has 501 uniformly spaced radii from 0 through 25 km:

| Column | Definition | Input |
|---|---|---|
| r_km | Radius in km | Sampling grid |
| T_MeV | Temperature in MeV | Caputo et al., arXiv:2109.03244v3, Fig. 1 red solid path |
| mu_mu_MeV | Muon chemical potential, including rest energy convention, in MeV | Same figure, blue solid path |
| mu_numu_MeV | Muon-neutrino chemical potential in MeV | Same figure, blue dashed negative/positive paths |
| lapse | Gravitational lapse, dimensionless | Ferreira et al., arXiv:2510.14469v1, Fig. 1, SFHo-18.8 orange dashed curve |
| T_Ferreira_MeV | Temperature independently extracted from Ferreira | Diagnostic only |
| mu_mu_Ferreira_MeV | Chemical-potential curve labeled muon in Ferreira | Diagnostic only; known discrepancy described below |

Use baseline columns for the selected benchmark. The alternative chemical-potential column must not silently replace the baseline or be mistaken for a second temperature profile.

The *_vertices.csv files preserve all deduplicated numerical vertices before resampling, including curve coordinates outside the visible clipping frame. Their columns are radius and the physical quantity named in the filename. n_mu_over_n0_caputo_vertices.csv is the independent plotted number-density reference with n0=0.181 fm^-3.

## Sources and reproducibility

- Caputo, Raffelt and Vitagliano, *Muonic Boson Limits: Supernova Redux*, corrected [arXiv:2109.03244v3](https://arxiv.org/html/2109.03244v3), Fig. 1. Source archive: https://arxiv.org/src/2109.03244v3, member figures/SNProfile.pdf.
- Ferreira, Marsh and Ravensburg, *ALP couplings to muons and electrons: a comprehensive analysis of supernova bounds*, [arXiv:2510.14469v1](https://arxiv.org/html/2510.14469v1), Fig. 1. Source archive: https://arxiv.org/src/2510.14469v1, member figures/SNModelComparison.pdf.

The PDFs are not redistributed here. From the repository root, regenerate the numerical files with:

    python research/stellar-cooling-constraints-20261105/extract_profile.py --download

The script downloads the public source archives into an ignored latex-build/sources directory, reads only the named PDF member from each archive, verifies its SHA-256, extracts polyline vertices with PyMuPDF, and maps drawing coordinates using explicit axis tick values. It never extracts arbitrary archive paths onto the filesystem. Dependencies: NumPy, SciPy, PyMuPDF.

For previously downloaded source figures:

    python research/stellar-cooling-constraints-20261105/extract_profile.py --source-dir PATH_TO_PDFS

Fixed PDF hashes, curve indices, domain endpoints, interpolation choices and numerical cross-checks are stored in profile_provenance.json.

## Boundary reconstruction and precision

1. The Caputo upper panel starts at **r=0.1 km**, whereas the lower density panel starts at **r=0**. They must not use the same horizontal calibration. The upper-panel temperature/chemical-potential ordinate is logarithmic; the density ordinate is logarithmic as well.
2. The visible Caputo frame ends at 20 km, but the public PDF contains the temperature polyline out to about **56.96 km**. The temperature through 25 km is extracted from those encoded vertices; no tail temperature fit or synthetic extrapolation is introduced.
3. The muon chemical-potential path ends at about **22.19 km** at the logarithmic plot floor of 1 MeV. The benchmark sets it to zero outside this point. The muon density there is exponentially negligible at T around 3 MeV.
4. The neutrino logarithmic plot gives a negative branch through 13.11 km and a positive branch from 16.59 to 18.42 km. In uncovered intervals, where the plotted absolute value is below 1 MeV, the benchmark uses zero. A run with mu_numu=0 everywhere provides a useful separate sensitivity diagnostic.
5. The first plotted core point is at 0.1166 km. Values below it are held constant.
6. The lapse curve is encoded through 23.9998 km. Between that radius and 25 km the benchmark uses the exterior form N(r)=sqrt(1-r_s/r), with r_s fixed continuously by the final plotted N. This is an explicit boundary approximation, not a reconstructed metric solution. Restricting the escape radius to 24 km removes this extrapolation and should be included when testing boundary sensitivity.
7. Values in the CSV are numerical coordinates of the published curves, not simulation precision. Multiple digits permit reproducibility; they do not imply corresponding astrophysical accuracy. The profile-dependent cooling result should be labeled as a reconstructed benchmark.

## Independent consistency check and source discrepancy

The two source temperature profiles agree over 0.2–20 km to **0.267% maximum relative difference** after independent vector-coordinate extraction. At r=0, 5, 8, 10 and 15 km, the muon number density obtained by integrating the Fermi distribution using the Caputo temperature and chemical potential agrees with the independently plotted Caputo density at about **0.5–1.1%**. The density normalization itself was given as n0=0.181 fm^-3 and is rounded.

However, the orange curve labeled mu_mu in Ferreira Fig. 1 differs strongly from Caputo's muon chemical potential despite the same profile label:

| r / km | Caputo mu_mu / MeV | Ferreira curve labeled mu_mu / MeV |
|---:|---:|---:|
| 0 | 46.67 | 254.89 |
| 5 | 56.14 | 233.32 |
| 8 | 91.79 | 167.40 |
| 10 | 102.84 | 131.14 |
| 15 | 62.28 | 68.65 |
| 20 | 14.77 | 12.41 |

The source's caption and text explicitly identify this panel as the muon chemical potential, so this is not a panel-selection ambiguity. Its origin is unresolved here. The baseline retains Caputo's internally density-consistent muon input; Ferreira contributes only the lapse. No claim that the discrepancy has been resolved is made, and no claim that the two entire input datasets are identical should be made.

Representative baseline values: T(25 km)=3.03377 MeV and N(25 km)=0.919912. The reconstruction and the physical approximations in the emission/transport calculation are separate uncertainties.
