# Croon Fig. 2: outer-profile source and reconstruction audit

**Date:** 2026-11-19  
**Status:** Source audit complete; the physical 25--100 km muon-opacity profile remains unavailable. No outer opacity has been fitted or inserted.  
**Scope:** Croon et al. (2021), Fig. 2, SFHo-18.8 at 1 s post-bounce. This is a separate C0 benchmark and does not modify the validated Blinov B.13/B.16 baseline or any axial-vector result.

## Executive finding

The missing input for the conservative Croon (R_{\rm far}=100\,\mathrm{km}) curve is not merely an outer temperature profile. It is the radial **muon absorptive susceptibility**
\[
n_{\mu^-}(r)F_{\rm deg}(r)
\]
(or enough thermodynamic and composition data to reconstruct it) along the propagation path from the neutrinosphere to (R_{\rm far}).

Croon et al. define
\[
\tau_{\rm abs}(\omega,r)=\int_r^{R_{\rm far}}dr'\,\Gamma_{\rm abs}(\omega,r'),
\qquad R_{\rm far}\simeq100\,\mathrm{km},
\]
while the production integral is restricted to (r<R_\nu\), with (R_\nu\simeq25\,\mathrm{km}) defined by (T=3\,\mathrm{MeV}). Their semi-Compton rate contains (n_\mu F_{\rm deg}), and the text explicitly says that the muon degeneracy factors are taken from the Bollig simulation as functions of radius. Therefore, a complete (R_{\rm far}=100\,\mathrm{km}) calculation needs the simulation's outer muon profile, not just a vacuum-decay tail.

The public figures inspected do not provide that 25--100 km profile. The Garching archive lists the relevant radial-profile collection, but the endpoint is access-controlled. The public SNforMuTau implementation likewise says that the simulation data must be requested from the Bollig et al. authors. The current C0 calculation must therefore remain labeled an **interior-profile calculation with a vacuum-only outer continuation**, not a complete reproduction of the solid Croon curve.

## 1. What Croon actually integrates

Croon et al., *Supernova Muons: New Constraints on Z' Bosons, Axions, and ALPs*, JHEP 01 (2021) 107, arXiv:2006.13942:

- Eq. (3.3) integrates the absorptive width from the emission radius to (R_{\rm far}\sim100\,\mathrm{km}).
- Eq. (3.4) integrates production only inside (R_\nu\sim25\,\mathrm{km}), with (R_\nu) defined by (T=3\,\mathrm{MeV}).
- Eq. (4.7) gives the semi-Compton production rate, proportional to (n_\mu F_{\rm deg}).
- The text immediately below Eq. (4.7) states that the muon (F_{\rm deg}) values are taken from the Bollig simulation as functions of radius.
- The Fig. 2 caption says the dashed 0.1 eV curve changes (R_{\rm far}\to R_\nu) in the trapping/luminosity prescription. The paper uses (R_{\rm far}=100\,\mathrm{km}) for its conservative result.

The paper's (R_{\rm far}\) variation is consequently a change to the **outer absorption path**. It is not a change to the local production normalization. For the sub-MeV curves, semi-Compton production and muon rescattering dominate; the vacuum (Z'\to\nu\bar\nu) width is proportional to (m_{Z'}^2) and is too small at (m_{Z'}=0.1\,\mathrm{eV}) to explain the observed solid/dashed separation in the scanned coupling interval.

Reference: [Croon et al., arXiv:2006.13942](https://arxiv.org/abs/2006.13942).

## 2. What the public profile papers do and do not show

### Bollig et al. (2020)

Bollig et al., *Muons in supernovae: implications for the axion-muon coupling*, arXiv:2005.07141, identify the SFHo-18.8 model and show:

- Fig. 3: the muon number-density profile;
- Fig. 4: the muon degeneracy parameter \(\mu_\mu/T\).

The displayed radial range is approximately 1--20 km. These figures are valuable independent checks of the inner muon-rich region, but they do not show the 25--100 km tail required by Croon's (R_{\rm far}=100\,\mathrm{km}) integral.

Reference: [Bollig et al., arXiv:2005.07141](https://arxiv.org/abs/2005.07141).

### Caputo, Raffelt and Vitagliano (2022)

*Muonic boson limits: Supernova redux*, arXiv:2109.03244, displays temperature, chemical potentials and particle densities for the same SFHo-18.8 reference model. The plotted radial range also stops at approximately 20 km. The paper notes that the muon abundance decreases exponentially near the PNS surface in its 1D reference models, while 3D motions could redistribute muons.

This is useful physical context, but it is not a tabulated outer profile and does not establish that the muon susceptibility is exactly zero beyond the plotted region.

Reference: [Caputo et al., arXiv:2109.03244](https://arxiv.org/abs/2109.03244).

### Esseili and Kribs (2026)

*Hiding a light vector boson from terrestrial experiments: a chargephobic dark photon*, Phys. Rev. D 114, 016023 (2026), Fig. 12, shows the temperature and particle-density profiles for SFHo-18.8. The plotted radius again ends near 20 km. In its PNS cooling calculation, the authors explicitly choose (R_{\max}=R_\nu\simeq25\,\mathrm{km}), and discuss the different trapping results obtained in earlier work with (R_{\max}\sim100\) or (1000\,\mathrm{km}).

This is an important comparison of transport conventions, but it does not supply the missing muon susceptibility from 25 to 100 km.

Reference: [Esseili and Kribs, Phys. Rev. D 114, 016023 (2026)](https://doi.org/10.1103/718s-7k7v).

## 3. The current digitized input has an unresolved outer edge

The current public input is:

- File: `research/stellar-cooling-constraints-20261105/data/sfho188_digitized.csv`
- SHA-256: `e41df78c8035540760fbcb7ef592cd830171822e`
- Rows: 1687
- Radial coverage: 0--25 km.

A direct scan of the committed CSV finds:

| Quantity | Value |
|---|---:|
| Last nonzero \(\mu_\mu\) sample | \(r=22.191893657\,\mathrm{km}\) |
| Last nonzero \(\mu_\mu\) value | \(0.999999834\,\mathrm{MeV}\) |
| First subsequent zero-filled sample | \(r=22.191894657\,\mathrm{km}\) |
| Temperature at that boundary | \(3.51524\,\mathrm{MeV}\) |
| Final radius in file | 25 km |
| \(\mu_\mu\) values after the boundary | zero through the end of the CSV |

The transition from almost exactly 1 MeV to zero at the next sample is a digitization/representation boundary. It is **not evidence that the physical muon chemical potential or muon density is exactly zero** outside 22.19 km. In particular, the interval 22.19--25 km is not a measured zero-susceptibility shell, and the file contains no data at all for 25--100 km.

The current C0 implementation uses the public profile inside (R_\nu\), zero-fills the unresolved muon tail, and includes only the vacuum neutrino-decay continuation outside (R_\nu\). That is an explicit approximation, not the original Garching outer medium.

## 4. Archive and code-repository access check

The Garching Core-Collapse Supernova Archive lists the Bollig/Hüdepohl 1D PROMETHEUS-VERTEX material, including the collection titled “Hydro radial profiles”:

- [Garching archive index](https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html)
- [Bollig radial-profile data endpoint](https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/Bollig2016_radial_profiles/)

The radial-profile endpoint returns HTTP 401 without credentials. The archive page says some archives are password-protected and directs users to contact the archive responsible person. This is not a public download.

The public [SNforMuTau repository](https://github.com/spinjo/SNforMuTau) contains code but no simulation tables. Its README explicitly states that the simulation data must be requested from the authors of Bollig et al. (arXiv:2005.07141).

The repository's historical [original-profile access note](ORIGINAL_SFHO188_PROFILE_ACCESS_2026-11-07.md) contains a draft request to the archive contact. It explicitly records that no email was sent and no access was granted. This audit does not send an email or attempt to bypass access controls.

## 5. Why the SFHo EOS alone cannot uniquely reconstruct the tail

An SFHo EOS table is necessary for a thermodynamically consistent calculation, but it does not by itself determine (n_\mu F_{\rm deg}(r)) outside the neutrinosphere.

At minimum, an EOS-based reconstruction would need a consistent radial state including:

- (T(r)), baryon density (n_B(r)), and composition such as (Y_e(r));
- the relevant lepton-number constraints or neutrino chemical potentials;
- the equilibrium/non-equilibrium prescription for the muon sector;
- the treatment of charge neutrality and any mean-field or rest-energy convention;
- fluid velocity and frame conventions if the rate is evaluated in a moving medium.

A table of (T,n_n,n_p) alone does not fix the muon chemical potential unless the weak-equilibrium and neutrino-lepton conditions are also specified. Imposing (mu_\mu=\mu_e) or setting neutrino chemical potentials to zero would be an additional physical assumption, not a consequence of the SFHo nuclear EOS. The published figures examined here do not provide all of these quantities through 100 km.

Therefore, the EOS can support a **separate sensitivity model** once its assumptions are stated, but it cannot be used to claim recovery of Croon's original outer profile.

## 6. Interpretation of the Fig. 2 discrepancy

The no-fit comparison of the two published 0.1 eV curves gives a median solid/dashed luminosity ratio of about 3.38 over the selected strong-coupling interval. The current model gives a ratio essentially equal to one because it has no measured muon opacity outside (R_\nu). The logarithm of the missing suppression, \(\ln(3.38)\simeq1.22\), is an **effective integrated-luminosity diagnostic**, not a local optical depth and not a unique reconstruction of \(\Gamma_{\rm abs}(r,\omega)\).

The existing finite-temperature/vacuum neutrino-decay tail tests are much too small to account for this low-mass separation. Additional outer-medium absorption remains one possible explanation, but a quantitative conditional test below shows that a simple monotonic continuation of the currently resolved muon susceptibility is far too small. A non-monotonic outer muon-rich layer, a different raw radial profile, another opacity prescription, or a mismatch in the interpretation of the solid/dashed comparison must be investigated. The luminosity ratio is not used to fit a local opacity.

## 7. Required next steps

1. **Authorized source recovery:** ask the Garching archive to confirm whether the protected collection contains the exact `s18.8-SFHo-MUONS` model at (t_{\rm pb}=1.0\,\mathrm{s}), and whether it includes (T,\mu_\mu,n_\mu) or equivalent composition variables out to 100 km.
2. **If raw data are unavailable:** build a separately labeled EOS-consistent outer-profile sensitivity family. State the weak-equilibrium, neutrino-lepton, and composition assumptions explicitly; do not label it Croon's original profile.
3. **Rate-level calculation:** compute the Croon semi-Compton absorptive width from the reconstructed (n_\mu F_{\rm deg}), then integrate the outer optical depth along the actual propagation path. Keep the energy dependence and detailed balance.
4. **Independent checks:** vary radial interpolation and outer boundary treatment; compare radial-shell contributions; verify the (R_{\rm far}=R_\nu) and (R_{\rm far}=100\,\mathrm{km}) limits without changing the inner production source.
5. **No fitting:** do not infer a local opacity profile from the Fig. 2 luminosity ratio, do not rescale the rate, and do not use the fitted luminosity suppression as an EOS input.

Until these steps are complete, keep the (R_{\rm far}=R_\nu) curve as the cleanest comparison available from the public inner profile, and keep the (R_{\rm far}=100\,\mathrm{km}) solid curve explicitly marked as incomplete.

## 8. CI / PR bookkeeping

PR #123 remains Draft. The new full source-weighted outer-opacity calculation is implemented in `audit_croon_outer_muon_opacity_envelope.py`, with four regression tests in `test_audit_croon_outer_muon_opacity_envelope.py`.

GitHub Actions run [44509948112](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44509948112) completed successfully on calculation-code commit `77e98c42e47c92246b21f1d9927915b6fb8a9e2f`. The new test class passed **4/4 tests**. The workflow also regenerated the machine-readable result artifact:

- [Outer muon-opacity envelope JSON artifact](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44509948112/artifacts/14522621089)
- Artifact SHA-256: `d21316f7d12153d4ef70a5b4ca951710165d5b6dccaa834f8af723fa6b9b1e1b`
- Committed result: `blinov_reproduction/outputs/croon_outer_muon_opacity_envelope_2026-11-19.json`

Eight subsequent commits only refined the documentation and added the generated JSON result as a tracked file; no calculation code changed after the tested commit. The earlier 72-test run [44487078124](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44487078124) remains the previous full-suite baseline; run 44509948112 is the current successful workflow verification for the new envelope code.

No manuscript, referee response, validated Blinov baseline, or axial-vector exclusion curve is changed by this source audit.

## 9. Conditional monotonic-tail upper-envelope diagnostic

This section tests a deliberately conservative continuation of the last nonzero point in the public digitization. It is a conditional sensitivity calculation, not a reconstruction of the protected Garching radial profile.

### 9.1 Digitized edge and screening estimate

The last nonzero digitized muon-chemical-potential sample is

\[
r_{\rm edge}=22.191893657~\mathrm{km},\quad
T_{\rm edge}=3.515243457~\mathrm{MeV},\quad
\mu_{\mu,\rm edge}=0.999999834~\mathrm{MeV}.
\]

The value near 1 MeV is the lower plotting floor of the logarithmic source curve. It is not a measurement that the physical chemical potential remains exactly 1 MeV at this radius. The current CSV sets the subsequent values to zero; that zero-filled continuation is likewise not a measurement of the physical outer profile.

Using the same free relativistic Fermi--Dirac susceptibility integral as the C0 calculation gives

\[
\chi_{\mu,\rm edge}
=n_\mu F_{\rm deg}
=1.13518337\times10^{-10}~\mathrm{MeV}^3.
\]

At \(T=3\,\mathrm{MeV}\), \(\mu_\mu=0\), the same integral gives

\[
\chi_\mu(3~\mathrm{MeV},0)
=3.82364561\times10^{-13}~\mathrm{MeV}^3.
\]

For the first screening estimate, the outer path is specifically \(R_\nu\to R_{\rm far}\), not \(r_{\rm edge}\to R_{\rm far}\). The conditional assumptions are:

1. \(\chi_\mu(r)\le\chi_{\mu,\rm edge}\) for \(r\ge R_\nu\);
2. \(T(r)\le3\,\mathrm{MeV}\) for \(r\ge R_\nu\);
3. the upper-envelope value \(\chi_{\mu,\rm edge}\) is held constant from \(R_\nu\) to 100 km.

This gives an outer path of \(100-R_\nu\simeq74.85\) km. At \(m_{Z'}=0.1\,\mathrm{eV}\), \(g=0.03\), the energy-dependent semi-Compton optical depths are:

| \(\omega\) (MeV) | \(\tau_{\rm sc}^{\rm edge\ envelope}\) |
|---:|---:|
| 0.1 | 0.5162 |
| 1 | 0.05970 |
| 3 | 0.02677 |
| 10 | 0.01755 |
| 30 | 0.01692 |

The very soft end has a larger Bose enhancement, but carries little source energy. The earlier representative-spectrum estimate, using \(Q_\omega\propto\omega^3/[e^{\omega/T_{\rm src}}-1]\), gave an additional suppression of about 1.7%. That was a screening estimate; the full source-weighted result is reported next.

### 9.2 Full C0 source-weighted re-evaluation

A separate calculation now uses the complete C0 source and transport structure rather than a representative source spectrum:

- profile B, SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c, 1687 radial nodes;
- \(m_{Z'}=0.1\,\mathrm{eV}\);
- both \(\nu_\mu\) and \(\nu_\tau\) in the \(L_\mu-L_\tau\) source and inverse-decay opacity;
- the local energy measure \(d\omega\,k\omega^2/(2\pi^2)\), with the emitted-particle energy included exactly once;
- the radius-dependent semi-Compton and neutrino source terms;
- detailed-balance absorption and source-radius-dependent optical depth;
- susceptibility order 256, local energy order 96, and 601 optical-depth energy nodes.

Two conditional outer semi-Compton envelopes are evaluated:

1. **Neutrinosphere envelope:** \(\chi_\mu=\chi_{\mu,\rm edge}\) from \(R_\nu\) to 100 km at \(T=3\,\mathrm{MeV}\).
2. **Edge-temperature envelope:** \(\chi_\mu=\chi_{\mu,\rm edge}\) from \(r_{\rm edge}\) to 100 km at \(T=T_{\rm edge}=3.51524\,\mathrm{MeV}\). This also fills the digitized zero interval between \(r_{\rm edge}\) and \(R_\nu\), and is the more conservative of the two envelopes under its stated assumptions.

The table distinguishes the vacuum neutrino-decay tail from the additional semi-Compton envelope. All entries are ratios of integrated luminosities; they are not local optical depths.

| \(g_X\) | \(L(R_\nu)/L_{\rm vacuum}\) | \(L_{\rm vacuum}/L_{T=3}\) | \(L(R_\nu)/L_{T=3}\) | \(L(R_\nu)/L_{\rm edge,T_{\rm edge}}\) |
|---:|---:|---:|---:|---:|
| \(3\times10^{-6}\) | 1.0000000000493 | 1.0000000001692 | 1.0000000002185 | 1.0000000002254 |
| \(10^{-5}\) | 1.0000000006821 | 1.0000000018830 | 1.0000000025651 | 1.0000000026438 |
| \(10^{-4}\) | 1.0000000913252 | 1.0000001892098 | 1.0000002805350 | 1.0000002889455 |
| \(10^{-3}\) | 1.0000115082120 | 1.0000190648679 | 1.0000305732993 | 1.0000314918106 |
| \(10^{-2}\) | 1.0014142774149 | 1.0019299684399 | 1.0033469753655 | 1.0034498037086 |
| \(3\times10^{-2}\) | 1.0139797238872 | 1.0176116217081 | 1.0318375512040 | 1.0328408123192 |

At the upper end of the scanned coupling interval:

- the vacuum neutrino-decay tail alone gives a factor 1.01398;
- the \(T=3\) MeV outer semi-Compton envelope adds a further factor 1.01761 relative to that vacuum-tail calculation;
- the combined \(R_\nu\)-to-100 km suppression is a factor 1.03183;
- the more conservative edge-to-100 km, \(T=T_{\rm edge}\) envelope gives a combined factor 1.03284.

The published median solid/dashed ratio is 3.38190. Thus even the more conservative full C0 envelope accounts for only about 3.3% suppression, leaving a factor

\[
\frac{3.38190}{1.03284}=3.27437
\]

unexplained. This is a stronger statement than the earlier 1.7% representative-spectrum estimate because it includes both the actual source-weighted outer semi-Compton attenuation and the vacuum neutrino tail.

### 9.3 Effective constant-susceptibility equivalents

The full source-weighted calculation also solves for the constant susceptibility on \(R_\nu\to100\) km that would be needed to reproduce the published median ratio 3.38190. The numerator is the \(R_{\rm far}=R_\nu\) luminosity; the denominator includes the vacuum neutrino tail and the trial outer semi-Compton opacity.

| Coupling | Required constant \(\chi_\mu\) (MeV\(^3\)) | Ratio to digitized edge value |
|---:|---:|---:|
| \(3\times10^{-6}\) | 0.81769954 | \(7.2032\times10^9\) |
| \(3\times10^{-2}\) | \(7.8634185\times10^{-9}\) | 69.2700 |

These are effective constant-tail equivalents, not inferred physical profiles. The same median luminosity ratio requires constant susceptibilities differing by about \(1.04\times10^8\) between the two coupling endpoints. A single constant outer susceptibility therefore cannot reproduce the same median suppression at both endpoints. This does not exclude a non-monotonic radial profile or a more structured outer medium.

### 9.4 Interpretation and limitations

The full source-weighted result rules out only the following conditional explanation: a smooth/non-increasing continuation whose outer susceptibility never exceeds the last nonzero digitized value. It does not rule out:

- a non-monotonic muon-rich outer shell in the original simulation;
- a difference between the published-figure reconstruction and the original Garching table;
- another outer-medium absorption process;
- a difference in the authors' transport convention or in our reading of the solid/dashed comparison.

The edge-temperature envelope assumes the outer temperature never exceeds the last digitized edge temperature. Neither envelope is a substitute for the protected Garching profile. The source-weighted calculation is archived and tested separately; no luminosity curve, opacity coefficient, or profile has been fitted or rescaled.


### 9.5 Inventory of the opacity channels in the published Croon benchmark

Croon et al. Sec. 4.2 identify two leading rates for the muon-coupled vector benchmark:

1. Neutrino-pair coalescence, Eq. (4.6), whose inverse process supplies the neutrino-decay absorptive opacity.
2. Semi-Compton scattering, Eq. (4.7), whose inverse process supplies the muon absorptive opacity.

Both are present in the C0 implementation. The neutrino channel includes the two \(L_\mu-L_\tau\) neutrino flavours. The semi-Compton channel uses the local susceptibility \(n_\mu F_{\rm deg}\), with the detailed-balance factor \(1+f_B\), and the full source-weighted outer-envelope calculation explicitly tests its continuation beyond \(R_\nu\).

The paper also discusses other processes in Appendix A:

- **\(\nu\nu\to Z'Z'\), Appendix A.1:** this is a two-vector production process and is suppressed by an additional power of the gauge coupling relative to the leading single-\(Z'\) channels. It is not an omitted leading single-particle absorptive width in Eq. (3.3).
- **Loop-induced nucleon bremsstrahlung, Appendix A.2:** this is induced by kinetic mixing. The Fig. 2 benchmark is the no-kinetic-mixing \(L_\mu-L_\tau\) case, so this channel is not part of that plotted baseline. The paper also discusses plasma screening for the mixing-induced contribution.
- **Muon-proton bremsstrahlung, Appendix A.3:** the paper estimates it to be suppressed relative to semi-Compton by an additional \(\alpha_{\rm EM}\) and the three-body final-state phase space.

Thus, within the stated no-kinetic-mixing Croon benchmark, the two leading single-\(Z'\) opacity channels have already been included and the additional channels identified by the authors are subdominant or absent from that benchmark. The present factor-3.38 outer-segment discrepancy cannot currently be assigned to an unexamined leading Croon opacity channel. The remaining data-driven possibilities are the true Garching outer profile or a difference in the original profile, implementation convention, or digitized figure.

#### Charge-conjugate muon target sensitivity

The printed degeneracy prescription quoted by Croon from Bollig et al. defines
\[
F_{\rm deg}=\frac{1}{n_{\mu,\rm th}}
\int\frac{2\,d^3p}{(2\pi)^3}
f_\mu(E;\mu_\mu)\,[1-f_\mu(E;\mu_\mu)],
\]
with one \(f_\mu(E;\mu_\mu)\) distribution. This is the literal single-\(\mu^-\) convention used in C0. A vector interaction also couples to \(\mu^+\), whose equilibrium distribution is \(f_\mu(E;-\mu_\mu)\). We therefore added a separate charge-conjugate sensitivity that replaces the single-species susceptibility by
\[
\chi_{\mu^\pm}
=\int\frac{d^3p}{\pi^2}
\left[
f_\mu(E;\mu_\mu)(1-f_\mu(E;\mu_\mu))
+f_\mu(E;-\mu_\mu)(1-f_\mu(E;-\mu_\mu))
\right].
\]
This extension is applied consistently to both the local source and the inverse semi-Compton opacity. It is not silently substituted into the literal Croon baseline. The full source-weighted result is recorded in the following update after the high-order regression completes.

## 10. Primary-data recovery route

The Croon paper itself states that the full profile data used for its SFHo-18.8 calculation are available through the Garching Core-Collapse Supernova Archive (arXiv:2006.13942, footnote on p. 4). The official archive states that some datasets are password-protected and that access should be requested from the archive contact. The specific Bollig radial-profile endpoint is access-controlled (HTTP 401), consistent with that policy.

Official sources:

- Croon et al., arXiv:2006.13942, p. 4: https://arxiv.org/pdf/2006.13942
- Garching Core-Collapse Supernova Archive: https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/archive.html
- Bollig radial profiles: https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/Bollig2016_radial_profiles/
- Archive contact: Hans-Thomas Janka, thj@mpa-garching.mpg.de

A data request should identify the exact target as the SFHo-18.8 model at \(t_{\rm pb}=1\,\mathrm{s}\), and ask for the radial profile extending through at least \(R_{\rm far}=100\) km. The minimum fields needed to close the present opacity question are:

1. radius and temperature \(T(r)\);
2. \(\mu_\mu(r)\) or separately \(n_{\mu^-}(r)\) and \(n_{\mu^+}(r)\), with the chemical-potential/dispersion convention;
3. the muon degeneracy factor or sufficient thermodynamic information to reconstruct \(n_\mu F_{\rm deg}\);
4. the neutrino chemical potentials and relevant neutrino thermodynamic fields used for the \(Z'\to\nu\bar\nu\) channel;
5. the exact snapshot identifier, radial sampling, and any profile-version notes.

The immediate priority is the outer interval \(25\lesssim r\le100\) km, but the complete profile is preferable so the source and opacity are derived from one consistent snapshot.

**Disposition:** no email has been sent, no access key has been requested or obtained, and no access restriction has been bypassed. The current public-figure reconstruction remains the only numerical input used in the committed calculation. The full-profile request is the next data-dependent step; the conditional envelopes in Sec. 9 remain sensitivity tests until that data is available.
