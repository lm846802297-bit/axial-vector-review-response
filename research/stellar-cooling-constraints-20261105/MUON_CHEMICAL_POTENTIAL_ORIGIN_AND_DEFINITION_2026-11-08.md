# Muon chemical potential: physical origin, convention, and profile audit

**Status:** literature-grounded definition established; the disagreement between the two published SFHo-18.8 figure reconstructions remains unresolved.  
**Scope:** this note concerns the thermodynamic background variable mu_mu(r) used in the pure-vector B.14--B.16 benchmark. It does not modify the axial calculation or the stellar background.

## 1. Physical origin: it is a simulation output, not a free profile

The adopted SFHo-18.8 background is a PROMETHEUS-VERTEX core-collapse simulation with muons and six-species neutrino transport. The muon chemical potential is determined locally by the muon state (net muon density, temperature, and the muon Fermi-gas EOS), while its evolution is coupled to weak reactions and neutrino transport.

The relevant physical process is **muonization**. Initially the trapped net muon-flavor number is approximately zero. As the proto-neutron star evolves, antimuon neutrinos diffuse out more efficiently than muon neutrinos; the associated loss of negative muon-flavor lepton number permits a net excess of mu-minus to build up. In the trapped region, the net muon-flavor number is constrained by transport and lepton-number conservation, rather than by imposing neutrino-transparent beta equilibrium everywhere.

This is why mu_mu(r) must not be replaced by mu_e(r) throughout the core.

## 2. Full chemical potential versus kinetic chemical potential

For a muon with total on-shell energy
\[
E_\mu(p)=\sqrt{p^2+m_\mu^2},
\]
the full relativistic chemical potential mu_mu_full enters
\[
f_{\mu^-}(p)=
\frac{1}{\exp[(E_\mu(p)-\mu_\mu^{\rm full})/T]+1},
\qquad
f_{\mu^+}(p)=
\frac{1}{\exp[(E_\mu(p)+\mu_\mu^{\rm full})/T]+1}.
\]
The net density is
\[
n_\mu^{\rm net}=
\frac{1}{\pi^2}\int_0^\infty dp\,p^2
\left[f_{\mu^-}(p)-f_{\mu^+}(p)\right].
\]

A second convention is sometimes useful in nonrelativistic EOS plots:
\[
\mu_\mu^{\rm kin}=\mu_\mu^{\rm full}-m_\mu.
\]
It is the kinetic chemical potential, with the muon rest mass subtracted. It is **not** interchangeable with mu_mu_full inside a distribution written with the total energy E_mu=sqrt(p^2+m_mu^2).

Bollig's thesis explicitly distinguishes the relativistic chemical potential from the kinetic one and states that some EOS contour plots show the latter for muons. The PRL muon-density calculation instead writes the distribution in terms of E_mu and mu_mu. Ferreira et al. define the charged-lepton Fermi factors with opposite signs of the same positive chemical potential for leptons and antileptons. The numerical implementation in reference.py follows the full-energy convention.

## 3. Weak-equilibrium relation and why mu_mu is not mu_e in the trapped core

For the charged-current reaction
\[
p+\mu^-\leftrightarrow n+\nu_\mu,
\]
chemical equilibrium gives
\[
\mu_p+\mu_\mu=\mu_n+\mu_{\nu_\mu},
\qquad
\mu_\mu=\mu_n-\mu_p+\mu_{\nu_\mu}.
\]
Similarly,
\[
\mu_e=\mu_n-\mu_p+\mu_{\nu_e}.
\]
Consequently,
\[
\boxed{\mu_\mu-\mu_e=\mu_{\nu_\mu}-\mu_{\nu_e}.}
\]

Only in a neutrino-transparent region, where the relevant neutrino chemical potentials vanish, does this reduce to mu_mu=mu_e=mu_n-mu_p. In the trapped core, the neutrino chemical potentials are generally nonzero and flavor dependent. Setting mu_nu_mu=0 everywhere would impose a beta-equilibrium approximation and would erase part of the transport-driven muonization history.

## 4. Figure-level profile consistency: Caputo versus Ferreira

Both Caputo et al. and Ferreira et al. label their displayed model SFHo-18.8 at t_pb=1 s. Their temperature profiles agree at the sub-percent level, but their digitized mu_mu(r) curves differ strongly in the inner core.

The distinction is not a constant rest-mass offset. A direct consistency check is therefore made against the muon density shown in Caputo et al. Using the full relativistic Fermi-Dirac integral above:

- the Caputo mu_mu curve reconstructs the same paper's digitized n_mu(r) at the percent level at representative radii;
- inserting the Ferreira mu_mu curve into the same full-energy distribution implies a different inner-core muon density, despite the near-identical temperature profile.

This comparison does **not** prove which published curve is the correct raw simulation output. It establishes that the two plotted curves cannot be silently combined or treated as alternative conventions related by m_mu. The published figure captions and the currently accessible figure-level data do not explain the discrepancy. The Garching archive identifies the simulation data source, but the relevant radial-profile endpoint is access restricted; no restricted data are accessed or redistributed here.

**Baseline decision:** retain the Caputo mu_mu curve because its chemical potential and independently plotted muon density pass an internal thermodynamic consistency check. Retain the Ferreira curve as a separate diagnostic only. Do not average the two profiles.

## 5. Implications for the B.16 calculation

The muon chemical potential enters more than one place:

1. the muon density and degeneracy factor in the semi-Compton contribution;
2. Pauli blocking and occupation factors in the muonic production/absorption kernels.

Therefore, a profile substitution changes local rates, not merely a normalization constant. It must be tested as a separate background variant and cannot be implemented by rescaling the final luminosity.

The current B.16 benchmark remains tied to the Caputo profile. The separate outer-mu_nu_mu sensitivity test does not change this choice.

## References

1. R. Bollig, W. DeRocco, P. W. Graham, and H.-T. Janka, “Muons in Supernovae: Implications for the Axion-Muon Coupling,” Phys. Rev. Lett. 125, 051104 (2020), [arXiv:2005.07141](https://arxiv.org/abs/2005.07141). See the discussion of muonization, the muon degeneracy parameter, and the Fermi-Dirac occupation.
2. R. G. Bollig, Muon Creation and Effects in Supernovae, PhD thesis, TU München (2018). See Chapter 3, Eqs. (3.1)--(3.11), and Chapters 11--12 for transport, muonization, and the beta-equilibrium comparison.
3. A. Caputo, G. Raffelt, and E. Vitagliano, “Muonic boson limits: Supernova redux,” Phys. Rev. D 105, 035022 (2022), [arXiv:2109.03244](https://arxiv.org/abs/2109.03244). See Fig. 1 and the discussion of the Garching SFHo-18.8 reference profile.
4. R. Z. Ferreira, M. C. D. Marsh, and E. Ravensburg, “ALP couplings to muons and electrons: a comprehensive analysis of supernova bounds,” [arXiv:2510.14469](https://arxiv.org/abs/2510.14469). See Sec. III, Fig. 1, and Eq. (5).
5. [Garching Core-Collapse Supernova Archive](https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/), the simulation-data source cited by the papers.
