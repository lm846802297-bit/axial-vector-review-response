# B.13 versus B.14--B.16: approximation-regime audit

**Date:** 2026-11-12  
**Status:** local-source comparison validated; not a global luminosity or transport result  
**Background:** reconstructed SFHo-18.8, (t_{\rm pb}=1\,\mathrm{s}) digitized profile  
**Profile SHA-256:** `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`

## 1. Question being tested

The comparison between the exact moving-muon semi-Compton calculation and the compact B.14--B.16 expression must not be interpreted as a requirement that the two agree throughout the supernova profile.

In Blinov et al., arXiv:2511.09619v1, Appendix B:

- Eq. (B.13) is the full (2\leftrightarrow2) phase-space integral for (\mu\gamma\leftrightarrow\mu V), including the initial and final muon distributions and final-state Pauli blocking.
- The text immediately below Eq. (B.13) states that the rate is usually evaluated in the non-relativistic-muon limit and with muon recoil neglected; this gives (E_\gamma\simeq\omega).
- Eq. (B.14) is the corresponding low-energy/Thomson-limit cross-section.
- Eqs. (B.15)--(B.16) convert this approximation to a thermal rate using (n_\mu F_{\rm deg}), the (1/v_V) phase-space factor, and the factor of two for the two photon polarization states.
- Eq. (B.17) defines the Pauli-blocking factor.

The current comparison therefore treats B.14--B.16 as an approximation to B.13, not as an independent exact kernel.

## 2. Three calculations used to separate the effects

All rates are normalized per (g_X^2). The B.14--B.16 formula is compared only with the pure-vector current.

1. **B.13 exact moving muon:** full Fermi--Dirac initial and final muon distributions, both charge species, exact recoil and exact (2\leftrightarrow2) kinematics, with polarization-resolved matrix elements.
2. **Stationary exact recoil:** exact Compton kernel for a muon at rest, using the same (n_\mu F_{\rm deg}) effective susceptibility as the B.16 comparison.
3. **B.14--B.16:** the published non-relativistic-muon, negligible-recoil Thomson-limit approximation, including the explicit (1+m_V^2/(2\omega^2)) correction.

This gives the factorization
\[
\frac{Q_{\rm B13}}{Q_{\rm B16}}
=
\frac{Q_{\rm B13}}{Q_{\rm stationary,exact}}
\frac{Q_{\rm stationary,exact}}{Q_{\rm B16}}.
\]
The numerical factorization residual is at most (1.2\times10^{-16}) in the archived cases.

## 3. SFHo-18.8 reference-mass results

For (m_V=10\,\mathrm{MeV}):

| Quantity | (r=0\,\mathrm{km}) | (r=12.5\,\mathrm{km}) |
|---|---:|---:|
| (T\) [MeV] | 19.2652 | 23.8820 |
| (\mu_\mu\) [MeV] | 46.6743 | 90.2166 |
| (Q_{\rm B13}/Q_{\rm B16}) | 0.479073 | 0.428594 |
| (Q_{\rm B13}/Q_{\rm stationary,exact}) | 0.842632 | 0.799793 |
| (Q_{\rm stationary,exact}/Q_{\rm B16}) | 0.568544 | 0.535881 |

The decomposition identifies two distinct effects:

- The moving-muon treatment changes the exact stationary-target result by about (-15.7\%\) at the center and (-20.0\%\) at 12.5 km.
- The stationary exact-recoil result is about (43.1\%\) and (46.4\%\) below B.14--B.16, respectively. This difference measures the finite-energy/Compton corrections beyond the Thomson approximation with the same effective susceptibility; it is not solely a recoil correction.

## 4. Low-mass check

The same pattern persists for (m_V=0.1\)--(3\,\mathrm{MeV}).

At 12.5 km:

| (m_V) [MeV] | (Q_{\rm B13}/Q_{\rm B16}) | (Q_{\rm B13}/Q_{\rm stationary,exact}) | (Q_{\rm stationary,exact}/Q_{\rm B16}) |
|---:|---:|---:|---:|
| 0.1 | 0.430109 | 0.802264 | 0.536119 |
| 0.3 | 0.430109 | 0.802261 | 0.536121 |
| 1 | 0.430108 | 0.802229 | 0.536141 |
| 3 | 0.430069 | 0.801983 | 0.536256 |

For (m_V=0.1\,\mathrm{MeV}), the integrated explicit B.14 parenthesis correction is only (2.21\times10^{-6}), while the B.13/B.16 difference is approximately (57\%\). At (m_V=3\,\mathrm{MeV}), the explicit correction is still only (1.78\times10^{-3}). Thus the large discrepancy is not caused by the small (m_V^2/(2\omega^2)) term.

## 5. Why the non-relativistic-muon approximation is not controlled here

The B.17-susceptibility-weighted kinematics are:

| Diagnostic | (r=0\,\mathrm{km}) | (r=12.5\,\mathrm{km}) |
|---|---:|---:|
| Mean muon speed | 0.5930 | 0.6712 |
| RMS muon speed | 0.6174 | 0.6903 |
| Mean (p_\mu/m_\mu) | 0.8285 | 1.0369 |
| Fraction with (p_\mu/m_\mu<0.3) | 5.28% | 2.26% |

The susceptibility-weighted muon population in the relevant region is not predominantly non-relativistic. In addition, the thermal photon energies are not uniformly much smaller than (m_\mu). Applying the B.14 Thomson approximation over the full thermal integral is therefore not parametrically controlled for this reconstructed SFHo background.

## 6. Controlled common-limit test

A dedicated regression test checks that the exact B.13 kernel approaches B.14--B.16 when both assumptions are deliberately enforced:

\[
T=0.5\,\mathrm{MeV},\quad
\omega=0.5\,\mathrm{MeV},\quad
m_V=0.05\,\mathrm{MeV},\quad
\mu_\mu=m_\mu+0.05\,\mathrm{MeV}.
\]

The exact moving-muon result agrees with the B.14--B.16 transverse modes and total rate within the test's 5% tolerance. This common-limit test passed in the 74-test finite-mixing/response suite.

## 7. Numerical convergence and interpretation boundary

At (r=12.5\,\mathrm{km}), (m_V=10\,\mathrm{MeV}):

- B.13 energy order 12 to 16 changes the integrated rate by (-1.30\times10^{-4}).
- Refining the inner quadrature from ((12,8,8,8)) to ((16,10,10,10)) changes it by (3.59\times10^{-5}).
- B.16 energy order 64 to 96 changes its integral by (1.78\times10^{-15}).
- The B.13 final-muon on-shell and detailed-balance residuals are below (2\times10^{-13}) and (4\times10^{-15}), respectively.

These are local source comparisons at (r=0) and (12.5\,\mathrm{km}). They do not include a radial luminosity integral, optical depth, escape probability, gravitational propagation, or a global SN1987A exclusion. The exact B.13 result is retained; no empirical rescaling of B.13 or B.16 is introduced.

## 8. Reproducible records

- `outputs/b13_b16_comparison_2026-11-12.json`
- `outputs/b13_b16_low_mass_scan_2026-11-12.json`
- `outputs/validation_manifest_2026-11-12.json`
- `test_b13_b16_comparison.py`
- `test_b13_b16_mass_scan.py`

The JSON outputs include the factorized differences and their numerical closure residuals.
