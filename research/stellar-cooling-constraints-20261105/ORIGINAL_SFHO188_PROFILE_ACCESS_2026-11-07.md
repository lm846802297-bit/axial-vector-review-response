# Original SFHo-18.8 profile acquisition and validation

**Date:** 2026-11-07  
**Status:** Archive entry identified; access request and exact-model/time confirmation pending. No restricted data downloaded or redistributed.

## 1. Objective

Obtain the original radial background used for the Blinov et al. Fig. 7 benchmark:
\[
\texttt{s18.8-SFHo-MUONS},\qquad t_{\rm pb}=1.0~{\rm s}.
\]
The reconstructed SFHo-18.8 profile currently used by this repository is a fallback, not an equivalent substitute for the simulation snapshot.

## 2. Official archive evidence

The Garching Core-Collapse Supernova Archive lists, under its 1D PROMETHEUS-VERTEX material, an entry titled **“Proto-neutron star neutrino cooling signals, neutrino angular moments, and radial profiles”**. The archive page identifies the simulations as performed by Robert Bollig and Lorenz Hüdepohl and links:
- “Radial neutrino moment profiles, spectral data, and hydro profiles” (Bollig2016_angular_moments);
- “Hydro radial profiles” (Bollig2016_radial_profiles).

The linked directories currently return HTTP 401 Unauthorized when opened without credentials. The archive page explicitly says some archives are password protected, asks users to contact the archive responsible person, and asks users not to redistribute access keys or archive data to third parties without permission.

Official archive:
https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html

Contact listed by the archive:
Hans-Thomas Janka — thj@mpa-garching.mpg.de

**Important qualification:** the archive listing is a strong provenance lead because it names the Bollig/Hüdepohl 1D PROMETHEUS-VERTEX simulations and their radial neutrino/hydro profiles. It does not, by itself, prove that the protected files include the exact s18.8-SFHo-MUONS snapshot at \(t_{\rm pb}=1.0\) s used for Blinov Fig. 7. This must be confirmed by the archive curator or data README after authorized access.

## 3. Access request: exact questions

Request permission to access the two linked data collections and ask the archive curator to confirm:

1. Whether the collection contains the model identifier s18.8-SFHo-MUONS (including exact spelling/case or any archive alias).
2. Whether a snapshot at \(t_{\rm pb}=1.000\) s is available, and whether the time is measured from core bounce.
3. Whether the radial profiles are the original simulation output or a post-processed/interpolated representation.
4. Which files are needed to reconstruct the exact background used by Blinov et al. (2025/2026), Fig. 7.
5. Whether the archive permits local scientific analysis and whether any additional permission is needed to share derived plots/tables or processed data.
6. Whether the archive curator recommends contacting Robert Bollig, Lorenz Hüdepohl, or the Blinov authors for model-specific variables not included in the archive.

## 4. Required-variable inventory

Do not assume every variable is present. Inspect the actual file headers, README, units, radial coordinate, and time metadata before mapping columns.

| Quantity | Symbol / desired data | Why it is needed | Status |
|---|---|---|---|
| Radial coordinate | \(r\), preferably areal radius with units | Integration and geometry | Awaiting file inventory |
| Time | \(t_{\rm pb}\) | Exact 1 s snapshot selection | Awaiting confirmation |
| Temperature | \(T(r)\) | Thermal distributions and rates | Awaiting file inventory |
| Mass density | \(\rho(r)\) | Matter background / consistency | Awaiting file inventory |
| Baryon density | \(n_B(r)\) | EOS and composition consistency | Awaiting file inventory |
| Electron fraction | \(Y_e(r)\) | Charge neutrality / composition | Awaiting file inventory |
| Muon chemical potential | \(\mu_\mu(r)\) | Muon distributions | Awaiting file inventory |
| Muon density | \(n_{\mu^-}(r),n_{\mu^+}(r)\) or net \(n_\mu(r)\) | Compton target density and blocking | Awaiting file inventory |
| Muon fraction | \(Y_\mu(r)\), if available | Cross-check against densities | Awaiting file inventory |
| Neutrino chemical potentials | \(\mu_{\nu_\mu}(r),\mu_{\nu_\tau}(r)\), or equivalent degeneracy parameters | Inverse-decay rates | Awaiting file inventory |
| Neutrino moments/spectra | \(J_\nu,H_\nu,K_\nu\), energy bins, or occupation data | Neutrino transport / closure checks | Awaiting file inventory |
| Metric/gravity | lapse, metric potentials, enclosed mass, or equivalent | Redshift and proper-volume factors | Awaiting file inventory |
| Fluid velocity | \(v(r)\) | Frame and transport corrections | Awaiting file inventory |
| Composition/EOS | species fractions, pressure, entropy, EOS metadata | Reconstruct thermodynamic state | Awaiting file inventory |
| Neutrinosphere data | radius/energy-dependent optical-depth or decoupling information, if available | Cross-check of transport domain | Awaiting file inventory |

The model may not provide \(\mu_{\nu_\tau}\) as a separately tabulated quantity. If the simulation assumes equal muon- and tau-neutrino thermodynamics, that assumption must be confirmed from metadata or the original simulation paper; do not silently infer it.

## 5. Comparison protocol after authorized receipt

1. Keep the original files unchanged in a local, access-controlled workspace. Do not commit protected raw files, archive passwords, tokens, or access keys to the public repository.
2. Record provenance locally: archive URL, model identifier, snapshot time, file names, file hashes, license/permission conditions, and README version. Only publish metadata/hashes if permitted.
3. Parse each file with explicit units and column definitions. Reject ambiguous columns rather than guessing.
4. Interpolate the reconstructed profile onto the original radial grid and compare every shared quantity. Report absolute and relative residuals, radial coverage, central values, outer-boundary values, and treatment of discontinuities.
5. Identify quantities absent from the archive. Request them from the archive team or original simulation authors; do not synthesize them from unrelated profiles without clearly labelling the approximation.
6. Re-run the six Fig. 7 mass curves with the original snapshot, keeping the published microphysics, opacity convention, and transport prescription fixed. Compare against the digitized published curves without fitted rescaling.
7. Preserve the reconstructed-profile results as a separate reproducibility lane; do not overwrite them.

## 6. Data-handling rules

The archive's stated policy allows non-commercial use subject to citation, requests notification when data are used in a scientific publication, and explicitly asks users not to provide access keys or archive data to third parties without permission. Follow any additional conditions supplied with the credentials. Until written permission is clear:
- no protected archive files or credentials in public GitHub;
- no redistribution to collaborators or external services;
- no public derived dataset if the permission terms do not allow it;
- keep public repository records limited to the fact of access, non-sensitive metadata, and reproducible code.

## 7. Draft access-request email

**To:** thj@mpa-garching.mpg.de  
**Subject:** Access request and model confirmation: s18.8-SFHo-MUONS radial profiles at 1 s post-bounce

Dear Professor Janka,

I am working on an independent reproduction of the supernova vector-boson luminosity calculation in Blinov et al., where the benchmark background is identified as s18.8-SFHo-MUONS at \(t_{\rm pb}=1\) s.

I found the Garching Core-Collapse Supernova Archive entry “Proto-neutron star neutrino cooling signals, neutrino angular moments, and radial profiles,” which links the Bollig2016_angular_moments and Bollig2016_radial_profiles collections. The linked directories appear to require authentication.

Could you please let me know whether these collections contain the exact s18.8-SFHo-MUONS simulation and its radial snapshot at 1.0 s after bounce? If so, may I request access for non-commercial academic research and independent reproduction of the published calculation?

I am particularly interested in the radial hydrodynamic and thermodynamic profiles, muon quantities, neutrino moments or spectra, and any metric/gravity variables required to reproduce the background consistently. If some of these quantities are not included, I would be grateful for guidance on the appropriate data contact or publication.

I will follow the archive's citation and data-handling conditions, will not redistribute credentials or protected files, and will notify the archive if the data are used in a scientific publication.

Thank you very much for your time and help.

Best regards,

[Your name]  
[Your affiliation]  
[Contact information]

---

## 8. Current decision

This is now a P0 source-acquisition task, ahead of further high-resolution scans on the reconstructed profile. The 176/360/64/128 scan may be retained as a numerical convergence diagnostic, but it must not be presented as resolving the background-model discrepancy.

No production code, opacity normalization, Fig. 7/4 result, manuscript, or referee-response text is changed by this acquisition task. The finite-mixing/axial scan remains blocked until the pure-vector benchmark is validated using the best available documented background.
