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

PR #123 remains Draft. The 72-test workflow run [44487078124](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44487078124) completed successfully on commit \`6005a51e4ab3ff7032ff1270ba803586b020ba46\`. The PR branch has advanced since that run, but GitHub's commit comparison shows only Markdown files changed between the tested commit and the current branch head; no calculation-code files changed. Thus the 72 tests cover the same calculation code, but there is no workflow run attached to the exact current PR head. Do not describe the run as having tested that exact head.

No manuscript, referee response, validated Blinov baseline, or axial-vector exclusion curve is changed by this source audit.


## 9. Conditional monotonic-tail upper-envelope diagnostic

A separate numerical diagnostic was run using the same Fermi--Dirac susceptibility integral implemented in \`croon_c0_luminosity.py\`. It is not a full replacement C0 run; it tests whether a smooth, non-increasing continuation of the resolved profile could plausibly account for the published solid/dashed luminosity separation.

### Resolved edge susceptibility

At the last nonzero \(\mu_\mu\) sample in the current CSV,
\[
r_{\rm edge}=22.191893657~\mathrm{km},\quad
T_{\rm edge}=3.51524346~\mathrm{MeV},\quad
\mu_{\mu,\rm edge}=0.999999834~\mathrm{MeV},
\]
the C0 susceptibility integral gives
\[
\chi_{\mu,\rm edge}
=n_\mu F_{\rm deg}
=1.13518337\times10^{-10}~\mathrm{MeV}^3.
\]
For comparison, the zero-filled endpoint used at \(T=3\,\mathrm{MeV}\), \(\mu_\mu=0\), gives
\[
\chi_\mu(3~\mathrm{MeV},0)
=3.82364561\times10^{-13}~\mathrm{MeV}^3.
\]

### Deliberately conservative continuation

Assume, conditionally, that for \(r\ge r_{\rm edge}\):

1. \(\chi_\mu(r)\le\chi_{\mu,\rm edge}\) (no outer resurgence);
2. \(T(r)\le3\,\mathrm{MeV}\);
3. the edge value is held constant all the way to 100 km, maximizing the path-integrated semi-Compton opacity under those assumptions.

For \(m_{Z'}=0.1\,\mathrm{eV}\), \(g=0.03\), and a 75 km outer path, the resulting energy-dependent optical depths are:

| \(\omega\) (MeV) | \(\tau_{\rm sc}^{\rm edge\ envelope}\) |
|---:|---:|
| 0.1 | 0.5162 |
| 1 | 0.05970 |
| 3 | 0.02677 |
| 10 | 0.01755 |
| 30 | 0.01692 |

The very soft end has a larger Bose enhancement, but it carries little source energy. Weighting the attenuation with the representative semi-Compton source spectrum
\[
Q_\omega\propto\frac{\omega^3}{e^{\omega/T_{\rm src}}-1}
\]
and integrating from the \(0.1\,\mathrm{eV}\) mass threshold gives:

| \(T_{\rm src}\) (MeV) | \(L_{\rm with\ edge\ envelope}/L_{\rm without\ outer\ tail}\) | Luminosity suppression factor |
|---:|---:|---:|
| 10 | 0.98311 | 1.01718 |
| 20 | 0.98320 | 1.01708 |
| 30 | 0.98322 | 1.01707 |
| 40 | 0.98322 | 1.01707 |
| 50 | 0.98322 | 1.01707 |

Thus, under the monotonic-tail assumptions, the integrated suppression is only about 1.7%, not the factor 3.38 inferred from the Fig. 2 solid/dashed pair.

### Effective susceptibility needed to reproduce the plotted separation

In the same representative energy-weighted model, matching the median published ratio 3.38190 at \(g=0.03\) would require a constant outer susceptibility of approximately
\[
\chi_{\mu,\rm req}
=(8.13\text{--}8.17)\times10^{-9}~\mathrm{MeV}^3,
\]
about 72 times the last resolved value. This is an effective constant-tail equivalent, not a reconstructed radial profile. Because the optical depth scales as \(g^2\chi_\mu\), the equivalent susceptibility at \(g=3\times10^{-6}\) would be about \(0.813\,\mathrm{MeV}^3\) in this simplified model.

### Interpretation and limitations

This diagnostic **rules out only the simple monotonic continuation** of the currently resolved public profile as an explanation of the full solid/dashed separation. It does not rule out:

- a non-monotonic muon-rich outer shell in the original simulation;
- a difference between the current digitized reconstruction and the original Garching table;
- an additional outer-medium absorption process;
- an issue in the published transport convention or in our curve interpretation.

The calculation uses a single representative source spectrum and a constant outer envelope, so it is a screening bound rather than the final radial/energy-resolved C0 result. The raw Garching profile remains necessary to decide among the possibilities. No luminosity curve, opacity coefficient, or profile has been tuned.
