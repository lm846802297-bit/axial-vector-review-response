# P1-IIIe-A: Garching EOS nucleon occupation implementation

Date: 2026-11-11  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Scope

This stage implements the local nucleon occupation and static degeneracy factor consistent with the Garching SFHo EOS. It is deliberately separate from the existing vacuum-mass ideal-Fermi-gas branch.

Primary sources:
- D. F. G. Fiorillo et al., *Axion-photon conversion in transient compact stars: Systematics, constraints, and opportunities*, JCAP 03 (2026) 053, [arXiv:2509.13322v2](https://arxiv.org/html/2509.13322).
- M. Hempel, *Nucleon self-energies for supernova equations of state*, Phys. Rev. C 91, 055807 (2015), [arXiv:1410.6337](https://arxiv.org/abs/1410.6337), especially Eqs. (91)-(99) and (107).
- Hempel SFHo EOS table manual v1.04, [official PDF](https://astro.physik.unibas.ch/fileadmin/user_upload/astro_physik/People/Subpage_Hempel/eos/v1.0/manual_v1.04.pdf) and [official EOS data page](https://astro.physik.unibas.ch/en/people/matthias-hempel/equations-of-state/).
- Sec. 4.2: Garching model provenance and archive availability.
- Sec. 4.3, Eqs. (41)-(42): recoil-free degeneracy factor and the two space-time weighting prescriptions.
- Appendix C.1, Eqs. (81)-(82): EOS-consistent nucleon occupation and SFHo kinetic dispersion.

The Garching simulations are stated to have evolved to 10 s post-bounce and to be available upon request. Independently, Hempel's official EOS page provides SFHo/FRDM EOS and complementary single-particle-property tables; the latter contain the total vector self-energies, filling factor, and species-specific effective Dirac masses. The paper does not publish the full local arrays of \(m_N^*,U_N,\mu_N^*\) in its article text.

## 2. Implemented thermodynamics

The implementation uses the tabulated convention in which \(\mu_N^*\) does not include the nucleon rest mass:
\[
f_N(p)=\left[\exp\left(\frac{U_N+K_N(p)-\mu_N^*}{T}\right)+1\right]^{-1},
\qquad
K_N(p)=\sqrt{p^2+m_N^{*2}}-m_N^*.
\]

It defines
\[
\nu_N\equiv\mu_N^*-U_N,
\qquad
f_N(p)=\operatorname{expit}\!\left(\frac{\nu_N-K_N(p)}{T}\right).
\]

The momentum integral gives the local density per available nucleon volume V', denoted n'_N, including the two spin states. In the excluded-volume EOS, the density per total volume is n_N=xi*n'_N, where xi=V'/V is the nucleon filling factor. Thus
\[
n'_N=\frac{1}{\pi^2(\hbar c)^3}\int_0^\infty dp\,p^2f_N(p),\qquad n_N=\xi n'_N.
\]
The recoil-free static blocking factor is
\[
F_{NN}^{\rm deg}
=
\frac{\int_0^\infty dp\,p^2f_N(p)[1-f_N(p)]}
{\int_0^\infty dp\,p^2f_N(p)}.
\]
The spin factor cancels in the ratio.

The code also evaluates the independent thermodynamic identity
\[
f_N(1-f_N)=T\left(\frac{\partial f_N}{\partial\nu_N}\right)_{T,m_N^*},
\qquad
F_{NN}^{\rm deg}
=
\frac{T}{n'_N}
\left(\frac{\partial n'_N}{\partial\nu_N}\right)_{T,m_N^*}.
\]
The derivative check holds \(T,m_N^*,U_N\) fixed; it is not a derivative along a self-consistent EOS trajectory.

For the vacuum-mass limit, the mapping is
\[
m_N^*=m_N,\qquad U_N=0,\qquad
\mu_N^*=\mu_N^{\rm total}-m_N.
\]
With this mapping the new occupation reproduces the existing ideal relativistic Fermi-gas occupation exactly. The old code is not overwritten.

## 3. Global Table 1 targets and exact weights

Fiorillo et al. define the averages over mass coordinate and time:
\[
\langle Q\rangle_{T^3}
=
\frac{\int dM\,dt\,Q(M,t)T^3(M,t)}
{\int dM\,dt\,T^3(M,t)},
\]
and
\[
\langle Q\rangle_{\rho T^{5/2}}
=
\frac{\int dM\,dt\,Q(M,t)\rho(M,t)T^{5/2}(M,t)}
{\int dM\,dt\,\rho(M,t)T^{5/2}(M,t)}.
\]
They state that these averages omit gravitational redshift/lapse effects.

For SFHo-18.8, the published targets are:

| Quantity | \(T^3\) weight | \(\rho T^{5/2}\) weight |
|---|---:|---:|
| \(\langle F_{pp}^{\rm deg}\rangle\) | 0.80 | 0.77 |
| \(\langle F_{nn}^{\rm deg}\rangle\) | 0.48 | 0.42 |

These are global, time-integrated targets. They are not local values and cannot be reproduced from the \(t_{\rm pb}=1\) s Fig. 1/Fig. 12 snapshot alone.

The CSV reader requires the filling factor xi as well as an explicit dMdt_weight column representing the cell measure \(\Delta M\,\Delta t\) (or its equivalent quadrature weight). It does not silently replace the mass-time integration by an equal-weight average over rows.

## 4. Code and tests

- **audit_b16_p1iii_eos_nucleon_distribution.py**: EOS occupation, density, static degeneracy factor, profile-weighted averages, and CSV interface.
- **test_b16_p1iii_eos_nucleon_distribution.py**: unit tests for the dispersion, occupation bounds, common \(U_N,\mu_N^*\) shift invariance, vacuum-mass limit, derivative identity, dilute limit, quadrature convergence, and the two global weighting formulas.
- **.github/workflows/b16-p1iii-eos-degeneracy.yml**: independent CI validation only; it does not commit or modify production outputs.

The CSV interface requires T_MeV, rho_g_cm3, dMdt_weight, xi, and for each species n,p: mstar_n_MeV, U_n_MeV, mu_star_n_MeV, mstar_p_MeV, U_p_MeV, and mu_star_p_MeV. A Hempel SFHo adapter is provided for the single-particle fields mstar_N, SigmaV_N^tot, and mu_N^nonrel. Optional free-nucleon density columns n_n_target_fm3 and n_p_target_fm3 are interpreted per total volume and are compared with xi*n'_N. The filling factor cancels in Fdeg but not in density closure or the later dynamic response normalization.

The Hempel-table mapping follows from Hempel (2015), Eqs. (95)-(99), and the RMF quasiparticle energy
\[
E_N(p)=\sqrt{p^2+m_N^{*2}}+\Sigma_{V,N}^{\rm tot}
\]
and the Hempel convention \(\mu_N^{\rm nonrel}=\mu_N-m_N\):
\[
U_N=m_N^*-m_N+\Sigma_{V,N}^{\rm tot},
\qquad
\mu_N^*=\mu_N^{\rm nonrel}.
\]
This mapping is exact for the Hempel total-self-energy/total-chemical-potential convention: Eq. (95) includes the nucleus-interaction term \(W_N\) in \(\Sigma_{V,N}^{\rm tot}\), Eqs. (96)-(97) use the corresponding total energy and chemical potential, and Eq. (98) shows the \(W_N\) cancellation in the occupation. It is therefore the correct translation for the Hempel SFHo tables. Its equivalence to the specific Garching profile version still requires EOS-version matching and local density closure. The Hempel filling factor \(\xi=V'/V\) is carried separately.

For excluded-volume matter, the Hempel convention distinguishes the local density in the available nucleon volume from the density per total volume:
\[
n'_N=n_N/\xi,\qquad \xi=V'/V.
\]
The Fermi integral computes \(n'_N\), while the EOS mass fraction gives \(n_N=X_N n_B\). The local density-closure condition is therefore \(\xi n'_N=X_N n_B\). The factor \(\xi\) cancels from \(F_{NN}^{\rm deg}\), but a response computed per available volume must be multiplied by \(\xi\) to obtain the total-volume response/opacity, as in Hempel (2015), Eq. (107).

The implementation checks the SFHo effective-mass splitting \(m_n^*-m_p^*=m_n-m_p=1.293333\) MeV (quoted as 1.2933 MeV in Fiorillo et al.) and reports the maximum residual. It does not impose this relation by modifying input data.

## 5. Numerical software self-test

A deterministic synthetic test fixture (not Garching profile data) was evaluated directly:
- Four local states cover neutron/proton species and two temperature scales.
- The direct \(f(1-f)\) integral agrees with the independent finite-difference derivative of the available-volume density \(n'_N\).
- The 256- and 512-node quadratures agree.
- The vacuum-mass mapping reproduces the existing total-chemical-potential occupation.
- A dilute Boltzmann state gives \(F^{\rm deg}\to1\).
- Shifting \(U_N\) and \(\mu_N^*\) by the same constant leaves the distribution unchanged.

The exact numerical residuals are archived in outputs/p1iii_eos_kernel_self_test_2026-11-11.json. These checks validate the implementation, not the four published Garching averages.

## 6. Validation boundary

The published global values 0.80, 0.77, 0.48, and 0.42 are **not yet claimed as reproduced**. A valid reproduction requires the Garching mass-time profiles (or equivalent cell data) for \(T,\rho,m_N^*,U_N,\mu_N^*\) with the mass-time integration measure.

The Hempel EOS files are linked at https://astro.physik.unibas.ch/en/people/matthias-hempel/equations-of-state/ and include the SFHo/FRDM single-particle-property archive (sfho_frdm_spp.zip) and EOS tables. The current execution container could not download the binary archives, so no table values have been interpolated or represented as measured inputs yet. The CompOSE SFHo page also lists eos.thermo, eos.micro, and eos.compo as available individual files.

The Hempel SFHo table is an EOS-microphysics reconstruction route, not a substitute for the Garching time sequence. It can support a local t_pb=1 s reconstruction once the T, n_B, and total proton fraction profiles are assembled, but it cannot reproduce the full mass-time weighted Table 1 averages without the simulation history.

The present stage does not:
- infer \(m_N^*,U_N,\mu_N^*\) from the digitized Caputo/Fig. 12 density curves;
- tune local parameters to force agreement with Table 1;
- replace the old ideal-gas benchmark;
- implement the dynamic weak response \(W_N^{\mu\nu}(q_0,q)\);
- modify B.2 opacity, the pure-vector Fig. 7 benchmark, or any axial cooling curve.

## 7. Next stage

After the Garching profile data become available, run the CSV interface and check:
1. \(n_n(r,t)\) and \(n_p(r,t)\) reconstructed from the same EOS distributions;
2. local density closure against the free-nucleon densities in the archive;
3. the effective-mass splitting and chemical-potential convention;
4. both mass-time weighted Table 1 degeneracy averages.

Only after these checks pass should P1-IIIe-B be considered complete and the EOS quasiparticle dispersion be introduced into the dynamic response in P1-IIIe-C.
