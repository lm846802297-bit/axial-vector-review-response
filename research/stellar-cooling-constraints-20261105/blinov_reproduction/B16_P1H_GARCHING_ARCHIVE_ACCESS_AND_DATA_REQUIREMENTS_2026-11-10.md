# P1-H: Garching archive access and minimum data required for energy-sphere closure

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Scope: official archive discovery and access verification; no new physical profile is constructed.

## 1. Official archive entry located

The official Garching Core-Collapse Supernova Archive lists a data collection titled "Proto-neutron star neutrino cooling signals, neutrino angular moments, and radial profiles". The archive page identifies Robert Bollig and Lorenz Hüdepohl as the simulation authors and notes that some results were published in Mirizzi et al. (2016), Bollig et al. (2017), and Bollig et al. (2020).

The archive exposes separate links for:
- neutrino signals;
- radial neutrino moment profiles, spectral data, and hydro profiles;
- hydro radial profiles;
- mass trajectories;
- progenitor data.

Official archive index:
https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html

The relevant archive entries are linked from the official page as:
- \`https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/Bollig2016_angular_moments/\`
- \`https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/Bollig2016_radial_profiles/\`

Direct access checks on 2026-11-10 returned HTTP 401 Unauthorized for both the radial-neutrino-data and hydro-profile endpoints. The archive index itself is public and explicitly states that some archives are password protected and that users should contact the archive responsible person to obtain access. No access control was bypassed, and no credentials or protected data were obtained.

**Important scope qualification:** the archive index establishes that a relevant Bollig/Hüdepohl data collection exists, but the index alone does not prove that every listed file is the exact \(s18.8\)-SFHo-MUONS snapshot used by Blinov et al. The model identifier, post-bounce timestamp, radial convention, and field definitions must be confirmed from the archive metadata or data provider before using any downloaded file.

## 2. Minimum data required for the unresolved B.2 boundary calculation

For a defensible energy-dependent daughter-pair reprocessing calculation at the \(t_{\rm pb}=1\) s benchmark, request or verify the following same-snapshot fields:

1. **Hydrodynamic background:** radius, baryon density, composition (at least neutron/proton fractions), temperature, lapse/metric fields, and fluid velocity, extending through the 25--35 km region.
2. **Heavy-flavor neutrino distributions:** energy- and angle-dependent \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) distribution functions, or sufficient angular moments plus the closure used by the transport scheme.
3. **Collision information:** energy- and flavor-dependent scattering, absorption, emission, and pair-process kernels. Transport opacity alone is insufficient to locate the heavy-flavor energy sphere.
4. **Metadata:** exact model label, EOS, progenitor, post-bounce time, radial coordinate, energy-bin definitions, frame convention (comoving/local versus observer-at-infinity), neutrino species ordering, and units.

The actual quantity needed is the energy-weighted daughter-pair escape/reprocessing probability
\[
P_{\nu\bar\nu}^{E}(\omega,r)
=\frac{1}{\omega}\sum_{h,\alpha}w_{h\alpha}(\omega,r)
\int_{-1}^{1}dz\,W_{h\alpha}(z)
\left[E_1P_{\nu_\alpha}^{\rm esc}(E_1,r)
+E_2P_{\bar\nu_\alpha}^{\rm esc}(E_2,r)\right],
\]
with the mode/flavor weights derived from the actual vector production density matrix and the neutrino escape probabilities calculated using the same-snapshot transport and energy-changing collision terms.

The current P1-G public-density calculation is only a transport-only envelope based on an approximate \(\nu N\) mean-free-path scaling and an extrapolated density tail. It is not a substitute for these data and does not determine the energy sphere.

## 3. What can and cannot be concluded now

The completed P1-F/P1-G calculations establish:
- high-energy daughter neutrinos have pair-mean energies of 105--255 MeV over the selected vector band;
- a simple public-density transport estimate places the corresponding transport transition broadly around 22--28 km, depending on energy and density-tail read-off;
- the smooth pair-energy survival proxy changes through 25--30 km and does not support treating the entire added shell as fully opaque;
- the transport sphere is not the heavy-flavor energy sphere.

They do **not** establish a corrected \(R_{\max}\), a corrected global B.2 luminosity, or a replacement for the literal fixed-\(\omega\), \(R_{\max}=25\) km baseline.

The \(+92.26\%\) strong-endpoint residual therefore remains unresolved by the currently accessible public data. This is an input/physical-boundary limitation, not evidence of a numerical path-integration failure.

## 4. Stop/go rule

**Go:** resume the full ray-, energy-, direction-, flavor-, and polarization-weighted daughter reprocessing calculation only after the data provider confirms that the files correspond to the same \(s18.8\)-SFHo-MUONS snapshot at \(t_{\rm pb}=1\) s and supplies the required transport fields.

**Stop:** until then, do not:
- substitute another progenitor, EOS, or post-bounce snapshot;
- fit \(R_{\max}\) to Fig. 7;
- multiply a source-weighted mean optical depth by the P1-G radial reprocessing fraction;
- apply an empirical opacity/source rescaling;
- update the axial-vector stellar-cooling curve.

PR #57 remains Draft/Open. The fixed-\(\omega\), 25 km scalar B.2 result remains the literal equation-level baseline.

## 5. Source

Garching Core-Collapse Supernova Archive, archive index and access policy:
https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html

The archive index states that access to some collections is password protected and instructs users to contact the responsible person. The present audit records the observed access status only; it does not request credentials, infer protected file contents, or claim that the listed archive files have already been mapped to the exact Blinov snapshot.
