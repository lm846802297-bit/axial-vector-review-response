# SFHo-18.8 profile-input audit in the sensitive 12--15 km interval

Date: 2026-11-09  
Scope: input provenance and internal consistency of the reconstructed \(t_{\rm pb}=1\) s SFHo-18.8 profile.  
Status: **temperature and lapse inputs are smooth and internally consistent at the level tested; the muon chemical potential has an unresolved source-to-source discrepancy, and the muon-neutrino chemical potential has a plotting-floor/support ambiguity that is directly relevant to the sensitive 12--15 km path shell. No replacement profile is adopted.**

## 1. Why this interval is prioritized

The combined B.2 leave-out audit identifies the 12--15 km path shell as the most sensitive individual shell for emission originating in the dominant 8--15 km source region. The current profile is reconstructed from published figures, not raw Garching simulation tables. This audit therefore checks the actual inputs used in that interval before any opacity or luminosity correction is considered.

## 2. Temperature: two independent figure extractions agree

The baseline temperature is digitized from Caputo et al., arXiv:2109.03244v3, Fig. 1. An independent temperature curve is extracted from Ferreira et al., arXiv:2510.14469v1, Fig. 1.

Across 12--15 km, the maximum pointwise relative difference is \(1.17\times10^{-3}\) (0.117%). Representative comparisons are:

| \(r\) (km) | \(T_{\rm Caputo}\) (MeV) | \(T_{\rm Ferreira}\) (MeV) | Relative difference |
|---:|---:|---:|---:|
| 12.0 | 25.9827 | 25.9818 | \(-0.0036\%\) |
| 12.5 | 23.8820 | 23.8740 | \(-0.0331\%\) |
| 13.0 | 21.7507 | 21.7461 | \(-0.0215\%\) |
| 14.0 | 17.4708 | 17.4721 | \(+0.0077\%\) |
| 15.0 | 13.2314 | 13.2415 | \(+0.0760\%\) |

The temperature reconstruction is therefore not a plausible explanation for a tens-of-percent opacity discrepancy in this interval.

## 3. Lapse: smooth, but only one source extraction is used

The baseline lapse is digitized from the Ferreira et al. SFHo-18.8 curve. It increases smoothly from 0.83350 at 12 km to 0.86350 at 15 km. There is no support boundary or interpolation discontinuity in this interval.

No second independent lapse extraction is present in the current provenance package. Thus the lapse is internally smooth, but it is not independently cross-validated against another figure or raw simulation data. The exterior Schwarzschild continuation begins only beyond the plotted 23.9998 km endpoint and is irrelevant to the 12--15 km interval.

## 4. Muon chemical potential: unresolved 9.5--17.2% source discrepancy

The baseline \(\mu_\mu(r)\) is taken from Caputo et al. The independent Ferreira curve is explicitly labeled as the muon chemical potential for the same SFHo-18.8 profile, but it is systematically higher over 12--15 km.

| \(r\) (km) | \(\mu_{\mu,\rm Caputo}\) (MeV) | \(\mu_{\mu,\rm Ferreira}\) (MeV) | Ferreira relative to Caputo |
|---:|---:|---:|---:|
| 12.0 | 93.733 | 109.826 | \(+17.17\%\) |
| 12.5 | 90.217 | 103.913 | \(+15.18\%\) |
| 13.0 | 85.955 | 97.661 | \(+13.62\%\) |
| 13.5 | 80.988 | 91.102 | \(+12.49\%\) |
| 14.0 | 75.818 | 84.125 | \(+10.96\%\) |
| 14.5 | 69.191 | 76.632 | \(+10.75\%\) |
| 15.0 | 62.283 | 68.649 | \(+10.22\%\) |

The relative discrepancy ranges from 9.48% to 17.17% over the sampled 12--15 km CSV points. It is much larger than the temperature difference.

The existing provenance check finds that the Caputo \(\mu_\mu\) curve, together with the Caputo temperature, reproduces the independently plotted Caputo muon number density at roughly the 0.5--1.1% level at representative radii. This supports internal consistency of the Caputo pair. It does **not** explain why the Ferreira curve labeled \(\mu_\mu\) differs. The two inputs must not be silently averaged or substituted.

A possible difference in chemical-potential convention, equation of state, or extraction interpretation must be checked against the definitions and source data of both papers. No such explanation is established in this audit.

## 5. Muon-neutrino chemical potential: plotting-floor ambiguity at 13.11 km

The baseline \(\mu_{\nu_\mu}\) is reconstructed from the negative branch in Caputo Fig. 1. In the 12--13.1099 km interval it changes smoothly from about \(-4.31\) MeV to the plot floor \(-1\) MeV:

| \(r\) (km) | Baseline \(\mu_{\nu_\mu}\) (MeV) |
|---:|---:|
| 12.0 | \(-4.314\) |
| 12.5 | \(-2.592\) |
| 13.0 | \(-1.287\) |
| 13.05 | \(-1.158\) |
| 13.109927 | \(-1.000\) |
| immediately beyond 13.109927 | \(0\) |

The digitized logarithmic plot only resolves \(|\mu_{\nu_\mu}|\gtrsim1\) MeV. The source polyline ends when it reaches this plotting floor. It does not demonstrate that the physical chemical potential becomes exactly zero at 13.1099 km.

The baseline therefore sets \(\mu_{\nu_\mu}=0\) outside the displayed branch. This is a transparent plotting-support convention, not a source-established physical boundary condition. The positive branch appears only between 16.588 and 18.423 km; the uncovered interval is likewise set to zero because the logarithmic plot does not resolve it.

This assumption is directly relevant to the 12--15 km shell: it changes the neutrino occupation input within the shell, and the abrupt transition at 13.1099 km is a digitization-support boundary. The present audit does not quantify its impact on the full B.2 luminosity.

## 6. Interpolation and sampling checks

The profile extraction script retains every source PDF polyline vertex in the generated CSV, in addition to the 0.05 km base grid. It also inserts \(10^{-6}\) km support knots around the endpoints of the plotted neutrino branches and the muon chemical-potential tail. Thus the \(\mu_{\nu_\mu}\) transition at 13.1099 km is not smeared across a full 0.05 km grid cell by subsequent linear interpolation.

The 12--15 km temperature, \(\mu_\mu\), and lapse curves are continuous across the shell boundaries. The only intentional near-step in this interval is the adopted \(\mu_{\nu_\mu}\) zero-outside-support convention.

## 7. Conclusions and decisions

1. **Temperature:** independently cross-checked; the two figure extractions agree to better than 0.12% throughout 12--15 km.
2. **Lapse:** smooth and correctly interpolated in the interval, but presently supported by only one source extraction.
3. **Muon chemical potential:** unresolved source discrepancy of roughly 9.5--17.2%; retain Caputo as the baseline because its pair with the Caputo temperature reproduces the plotted Caputo muon density. Do not substitute Ferreira or average the two without resolving the convention.
4. **Muon-neutrino chemical potential:** the zero-outside-support assumption is not fixed by the plot. It requires a dedicated sensitivity calculation, especially around 13.11 km and across the 13.11--16.59 km gap.
5. **Raw profile:** the original Garching profile tables remain unavailable. Figure digitization cannot establish simulation-level precision.

## 8. Required next calculation

Before modifying any opacity or transport code, run a controlled profile-input sensitivity study with all physics kernels and numerical settings fixed:

- Baseline: current Caputo \(T,\mu_\mu,\mu_{\nu_\mu}\) and Ferreira lapse.
- Variant A: set \(\mu_{\nu_\mu}=0\) throughout 12--15 km, leaving all other inputs unchanged.
- Variant B: replace only the 12--15 km \(\mu_\mu\) input by the Ferreira digitization, explicitly as a diagnostic rather than a preferred physical profile.
- Variant C: vary the \(\mu_{\nu_\mu}\) transition over a narrow, documented radial interval, without inventing a new central value outside the plotted information.

For each variant, compare local \(\nu_\mu\) and \(\nu_\tau\) reduced absorption, the optical-depth contribution of the 12--15 km shell, and the strong-endpoint source-weighted escape probability. Do not rescale the vector curve or update the axial curve unless a source-supported profile choice is established.

## 9. Reproducibility and source files

- data/sfho188_digitized.csv: baseline and independent diagnostic columns.
- data/profile_provenance.json: source hashes, curve indices, endpoints, and extraction assumptions.
- data/README.md: figure provenance, reconstruction conventions, and the unresolved \(\mu_\mu\) source discrepancy.
- extract_profile.py: PDF-polyline extraction and profile reconstruction.
- audit_b16_inner_path_channel_directional.py: B.2 shell/channel/direction sensitivity.

The profile remains a reconstructed public-figure benchmark, not the raw Garching simulation.
