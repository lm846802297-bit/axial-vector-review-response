# Published Fig. 7 Compton-baseline method audit

Date: 2026-11-09  
Target: Blinov et al., *L_mu-L_tau gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, arXiv:2511.09619.

## 1. Executive conclusion

The faithful reproduction target for the published Fig. 7 is the **non-relativistic-muon, no-recoil Compton prescription encoded by Eqs. (B.14)--(B.19)**, not a numerical evaluation of the fully moving-muon phase-space integral in Eq. (B.13).

Equation (B.13) is the general thermal phase-space expression. The authors immediately describe the usual non-relativistic-muon/no-recoil reduction, give the approximate cross section in Eq. (B.14), derive the thermal rates in Eqs. (B.15) and (B.16), and define the degeneracy factor in Eq. (B.17). Most decisively, the paragraph immediately following Fig. 7 identifies the low-mass Compton absorption rate with Eq. (B.14), including its mass-independent (m_V\to0) limit.

The exact moving-muon B.13 calculation remains a useful relativistic correction study, but it is **not the baseline against which the published Fig. 7 should be judged**.

## 2. Primary source and Fig. 7 specification

Published article: [JHEP 06 (2026) 155](https://doi.org/10.1007/JHEP06(2026)155)  
PDF: [Springer published PDF](https://link.springer.com/content/pdf/10.1007/JHEP06(2026)155.pdf)  
arXiv: [2511.09619](https://arxiv.org/abs/2511.09619)

The Fig. 7 caption specifies:
- the (s18.8\text{-SFHo-MUONS}) supernova model;
- post-bounce time (t_{\rm pb}=1\,\mathrm{s});
- luminosity (L_V\) versus (α_V);
- mediator masses (10^{-6},10^{-5},0.1,1,10,200\,\mathrm{MeV});
- the black dashed Raffelt luminosity criterion.

The accompanying text says that the low-mass trapping regime is dominated by Compton absorption and explicitly refers to Eq. (B.14) for its mass-independent (m_V\to0) behavior. Above the MeV scale, inverse neutrino decay becomes the dominant trapping process.

## 3. What Eqs. (B.13)--(B.19) mean for the implementation

### 3.1 General expression: Eq. (B.13)

Equation (B.13) is the full thermal phase-space integral for
\[
\mu^-+\gamma\to\mu^-+V,
\]
including the initial muon Fermi distribution, final-state muon Pauli blocking, photon Bose distribution, the four-dimensional phase-space delta function, and the spin/polarization sum.

### 3.2 Published approximation: Eqs. (B.14)--(B.17)

The text then adopts the non-relativistic-muon limit and neglects muon recoil. The approximate cross section is
\[
\sigma(\mu\gamma\to\mu V)
\simeq
\frac{8\pi\alpha\alpha_V}{3m_\mu^2}
\left(1+\frac{m_V^2}{2\omega^2}\right)
\sqrt{1-\frac{m_V^2}{\omega^2}}.
\]
With
\[
v_V=\sqrt{1-\frac{m_V^2}{\omega^2}},
\qquad
F_{\rm deg}
=\frac{1}{n_\mu}
\int\frac{2d^3p}{(2\pi)^3}
f_\mu(E,\mu_\mu)\,[1-f_\mu(E,\mu_\mu)],
\]
the thermal production rate in Eq. (B.16) is
\[
\Gamma^{\rm prod}_{\mu\gamma\to\mu V}(\omega)
=
\frac{n_\mu F_{\rm deg}}{v_V}
\frac{2}{e^{\omega/T}-1}
\sigma(\mu\gamma\to\mu V).
\]
The (1/v_V) factor and the factor 2 associated with the two photon polarization states are explicitly discussed in the paper. They must not be dropped.

Equation (B.19) fixes the absorption rate by detailed balance:
\[
\Gamma^{\rm abs}_{\mu\gamma\to\mu V}(\omega)
=e^{\omega/T}\,
\Gamma^{\rm prod}_{\mu\gamma\to\mu V}(\omega).
\]

## 4. Cross-check against the repository implementation

The current B.16 reference implementation matches this structure:

| Published ingredient | Repository implementation |
|---|---|
| (n_\mu) and (F_{\rm deg}), Eq. (B.17) | `negative_muon_density_and_degeneracy()` in `reference.py` |
| No-recoil cross section, Eq. (B.14) | `compton_production()` |
| (2/v_V) and Bose factor in Eq. (B.16) | `compton_production()` |
| Detailed-balance absorption, Eq. (B.19) | `local_rates()` |
| Reduced opacity used in transport | `reduced_absorption=(1-e^{-\omega/T})\Gamma^{\rm abs}` in `local_rates()` |

In particular, `compton_production()` evaluates the B.14 cross section and multiplies it by
`n_mu * f_deg * (2/velocity) * 1/expm1(omega/temperature)`,
which is the B.16 structure. The downstream luminosity scan uses (g^2=4\pi\alpha_V), as recorded in the B.16 audit output.

The baseline uses the single negative-muon distribution appearing in the published formula. The positive-muon branch in the B.13 diagnostic is an additional charge-conjugate comparison, not part of the baseline implementation.

## 5. Interpretation of the completed B.13 global calculation

The three-mass B.13 global run is a useful extension that replaces the B.16 non-relativistic/no-recoil kernel with the full moving-muon phase-space calculation. Its different luminosity curves are therefore not, by themselves, evidence of a numerical error or a failure to reproduce Fig. 7.

The archived B.13/B.16 comparison shows large source differences at 0.1 and 1 MeV. Those differences quantify the physical impact of relaxing the non-relativistic-muon/no-recoil approximation. They should be presented as a separate correction study, not used to redefine the Fig. 7 baseline.

See:
- `B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md`
- the archived three-mass B.13 outputs in `outputs/`.

## 6. Background-data limitation

The published paper identifies the (s18.8\text{-SFHo-MUONS}) model at (t_{\rm pb}=1\,\mathrm{s}), but does not provide an associated numerical code/data archive. The repository profile is explicitly a reconstruction from public figure paths, not the original Garching simulation table.

This does **not** prevent reproducing the published calculation method. It does mean that, after the B.14--B.19 implementation and all numerical integrations are converged, any remaining discrepancy may still contain a profile-reconstruction component. That component must be assessed separately; it must not be absorbed into an empirical luminosity or coupling rescaling.

## 7. Revised calculation priority

1. Treat B.14--B.19 as the primary pure-vector Fig. 7 benchmark.
2. Complete the independent-grid B.1/B.2 source and opacity convergence checks.
3. Run the high-order B.16 global luminosity with the fixed opacity grid, converged source radial order, and independently checked energy/angular/path quadratures.
4. Compare the fixed-ω Eq. (B.2) prescription to Fig. 7 first. Keep the path-redshift calculation as a separate diagnostic, since Eq. (B.2) uses fixed ω along the chord.
5. Once the B.16 benchmark is accepted, retain B.13 as a separate relativistic correction study.
6. Only after the pure-vector baseline passes may the axial-vector kernel be switched back on. No empirical rescaling and no modification of the formal axial-vector production outputs are permitted during this audit.

