# Public availability audit: SFHo-18.8 profiles, metric data, and TOV solver

Date: 2026-11-09  
Scope: determine whether the remaining same-snapshot thermodynamic and metric inputs can be obtained from a public, unauthenticated source. This is a source-availability audit only; no physical profile or production calculation is changed.

## 1. Official Garching archive index

The official Garching Core-Collapse Supernova Archive index lists the data collection for simulations performed by Robert Bollig and Lorenz Hüdepohl. Under that entry it exposes separate links for:

- neutrino signals;
- radial neutrino moment profiles, spectral data, and hydro profiles;
- hydro radial profiles;
- mass trajectories;
- progenitor data.

The index explicitly states that some archives are password protected and asks users to contact the archive responsible person when access is needed.

Sources:
- Official archive index: https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html
- Relevant Bollig/Hüdepohl archive entry, links 110--114 in the index.
- Archive access notice: some archives are password protected; contact Hans-Thomas Janka.

## 2. Direct endpoint checks

The two most relevant radial-data endpoints were tested directly:

| Resource | Archive endpoint | Result |
|---|---|---|
| Radial neutrino moments, spectra, and hydro profiles | `/ccsnarchive/data/Bollig2016_angular_moments/` | HTTP 401 Unauthorized |
| Hydro radial profiles | `/ccsnarchive/data/Bollig2016_radial_profiles/` | HTTP 401 Unauthorized |

The archive index also lists a separate resource, **Python TOV solver (2020), author Robert Bollig**. Its directory endpoint,

`https://wwwmpa-garching.mpg.de/ccsnarchive/data/Bollig2020_TOV_solver/index.html`,

also returns HTTP 401 Unauthorized.

These are authentication responses from the official host, not evidence that the files do not exist. No attempt is made to bypass access controls, infer credentials, or redistribute restricted data.

## 3. Independent recent-paper cross-check

Wang and Zhang, *Revisiting supernova constraints on dark gauge bosons*, arXiv:2610.35379 (submitted 26 October 2026), state that their SFHo-18.8 and LS220 profiles use radially dependent quantities supplied by the corresponding simulations and that the full profile data are available from the Garching archive.

This is useful independent confirmation that the same simulation profiles are used by later supernova gauge-boson analyses. It does not provide a second public mirror of the raw data: the cited source is the same Garching archive.

Source:
- https://arxiv.org/abs/2610.35379
- Searchable PDF text: https://borowiecki.dev/pdf/2610.35379

The paper is not treated as a direct reproduction of Blinov et al.'s Fig. 7: its production channels, model-specific assumptions, and observables must be compared equation by equation before any numerical curve can be used as a benchmark.

## 4. Consequence for the metric reconstruction

The archive's TOV-solver listing does not close the metric-data gap because the solver itself is not currently accessible without authorization. More importantly, a generic TOV solver is not a substitute for the metric of a time-dependent proto-neutron-star snapshot.

A same-snapshot reconstruction of
[
A(r)=\left(1-\frac{2GM(r)}{r}\right)^{-1/2}
]
would require a justified enclosed-mass/energy-density profile, and a full ray calculation would also require a consistent treatment of the time-dependent hydrodynamic state and the relevant metric convention. The current public-figure reconstruction does not provide those inputs with sufficient provenance.

No (A(r)) is inferred from the lapse (N(r)) alone. No static-TOV approximation is promoted to a same-snapshot GR result.

## 5. Decision and next action

1. The public unauthenticated search for the exact Bollig/Hüdepohl radial profile tables and the listed Bollig TOV solver is exhausted for the endpoints identified in the official index.
2. The current SFHo-18.8, 1 s background remains a published-figure reconstruction, not the raw simulation table.
3. The lapse cross-check remains visual and does not validate (A(r)) or (M(r)).
4. The only legitimate route to exact same-snapshot data is authorized archive access or a data transfer explicitly authorized by the archive/data owners.
5. If such access is not pursued, the metric and outer-profile limitations remain explicit. Do not construct a synthetic TOV star, splice another progenitor/time snapshot, or tune a profile to reduce the Fig. 7 residual.

The fixed-\(\omega\) B.16 vector benchmark remains the paper-reproduction baseline. The path-redshift calculation remains a diagnostic. No axial-vector curve is recalculated or updated.
