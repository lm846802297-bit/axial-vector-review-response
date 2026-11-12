# P1-I: Literature-guided energy-exchange depth for high-energy daughter neutrinos

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, \(210\leq\omega\leq510\) MeV, SFHo-18.8, \(t_{\rm pb}=1\) s

## 1. Decision: raw Garching transport arrays are not a prerequisite for a controlled first estimate

The exact same-snapshot Boltzmann distributions and collision arrays remain unavailable through the public Garching endpoints. This does not prevent further progress.

There are three public ingredients:
1. Caputo, Raffelt, and Vitagliano (2022), Fig. 1, publish the \(n_B(r)\), \(n_p(r)\), temperature, and chemical-potential profiles of the same SFHo-18.8, \(t_{\rm pb}=1\) s reference snapshot used in the present calculation. The density figure extends to 20 km.
2. The current repository already contains the digitized \(T(r)\), \(\mu_\mu(r)\), \(\mu_{\nu_\mu}(r)\), and lapse profile for this benchmark, plus the P1-G figure-level density-tail estimate outside 20 km.
3. Published supernova neutrino-transport papers provide a standard energy-thermalization-depth formalism and approximate heavy-flavor energy-exchange kernels.

The correct next step is therefore a **literature-informed transport estimate on the public SFHo-18.8 background**, not a splice with another progenitor or EOS. Its status must remain distinct from an exact reconstruction of the unpublished Garching transport solution.

## 2. The relevant distinction: transport opacity is not energy-exchange opacity

For heavy-flavor neutrinos, neutral-current scattering on nucleons dominates the total transport opacity. However, approximately elastic scattering can change direction without efficiently changing the neutrino energy. The energy sphere and transport sphere are therefore distinct.

Keil, Raffelt, and Janka (2003), Eq. (1), define the energy-thermalization optical depth
\[
\tau_{\rm therm}(E,r)=
\int_r^\infty dr'\,
\sqrt{
\kappa_E(E,r')
\left[\kappa_T(E,r')+\kappa_E(E,r')\right]
},
\]
where \(\kappa_T=\lambda_T^{-1}\) is the transport opacity and \(\kappa_E=\lambda_E^{-1}\) is the energy-exchange opacity. The energy-thermalization radius is defined by
\[
\tau_{\rm therm}(E,R_{\rm therm})=\frac23.
\]
This is the appropriate first diagnostic for deciding whether a high-energy daughter neutrino can transfer its energy to the medium. It is not equivalent to declaring every neutrino-nucleon scattering an absorption event.

The same paper identifies nucleon bremsstrahlung, inverse bremsstrahlung, inelastic nucleon scattering, recoil in \(\nu N\) scattering, and neutrino-lepton scattering as energy-changing channels. The hierarchy is model dependent.

## 3. Literature inputs for the energy-exchange opacity

### 3.1 Transport opacity

For a first public-profile estimate, retain the representative neutral-current transport mean free path quoted by Raffelt, Janka, and Fiorillo (2025):
\[
\lambda_T(E,r)\simeq
25\ {\rm cm}\,
\frac{n_0}{n_B(r)}
\left(\frac{100\ {\rm MeV}}{E}\right)^2.
\]
This is a representative scale, not a precision high-energy cross section. The production calculation must later compare it with a recoil- and weak-magnetism-corrected differential \(\nu n\) and \(\nu p\) cross section.

### 3.2 Recoil energy exchange

Müller and Janka (2015), Appendix A, Eq. (A31), use the effective heavy-flavor neutrino absorption opacity
\[
\kappa_{E,\rm recoil}(E,r)
\simeq
\frac{|E-3T(r)|}{m_N}\,\kappa_{s,\nu N}(E,r),
\]
to represent energy transfer by recoil in neutrino-nucleon scattering. This provides a literature-based recoil-only baseline for \(\kappa_E\).

This is an effective thermalization opacity, not a statement that a scattering removes the entire neutrino. Their FMT implementation used energy groups up to 197 MeV. Applying the approximation to the 255--510 MeV daughter tail is an extrapolation and must be labelled accordingly.

### 3.3 Nucleon-nucleon bremsstrahlung and inelastic scattering

Hannestad and Raffelt (1998), especially Secs. 2.2--2.3 and 3.4, show that:
- inverse \(NN\) bremsstrahlung changes neutrino number and energy;
- the crossed inelastic process \(\nu NN\leftrightarrow NN\nu\) can transfer energy more efficiently than pair bremsstrahlung;
- the energy-transfer rate from inelastic nucleon scattering can exceed that from bremsstrahlung by roughly an order of magnitude, with order-unity corrections;
- nucleon recoil is also important;
- their perturbative one-pion-exchange treatment is intended for the surface layers, approximately \(\rho\lesssim10^{14}\ {\rm g\,cm^{-3}}\), and omits some correlations.

The next implementation should therefore use the Hannestad--Raffelt spin-density scattering kernel where its assumptions are valid, and bracket the inelastic/recoil contribution rather than silently replacing it by a universal multiplicative factor. For the high-energy daughters, the momentum dependence of the kernel and finite-recoil kinematics must be checked; the long-wavelength approximation is not automatically valid when the momentum transfer is comparable to the pion scale.

### 3.4 Energy-sphere formalism

Keil, Raffelt, and Janka (2003), Eq. (1), and Hannestad and Raffelt (1998), Eqs. (8)--(9), provide mutually consistent effective thermalization-depth prescriptions. The implementation will use the Keil et al. expression above, with separate contributions to \(\kappa_E\) from:
- nucleon recoil;
- inelastic \(\nu NN\leftrightarrow NN\nu\) scattering;
- inverse \(NN\) bremsstrahlung;
- subleading leptonic channels where relevant.

The energy-exchange rates must be assembled at the kernel level where possible. A simple opacity multiplier is only a sensitivity bracket, not a final calculation.

## 4. Recoil-only pilot calculation on the P1-G outer density tail

Before constructing the full collision kernel, a transparent pilot calculation was made using:
- central P1-G density tail: \(n_B(20\,{\rm km})/n_0=10^{-3}\), \(H_\rho=1.2\) km;
- \(T(25\,{\rm km})=3.03\) MeV from the existing profile;
- the P1-G \(\lambda_T\propto n_B^{-1}E^{-2}\) reference;
- the recoil-only effective opacity \(\kappa_E/\kappa_T=|E-3T|/m_N\);
- the energy-sphere criterion \(\tau_{\rm therm}=2/3\).

For the exponential outer tail, treating \(T\) as locally constant over the short tail gives
\[
\kappa_E=\alpha(E)\kappa_T,\qquad
\alpha(E)=\frac{|E-3T|}{m_N},
\]
and hence
\[
\tau_{\rm therm}(E,r)\simeq
\sqrt{\alpha(E)[1+\alpha(E)]}\,\tau_{\nu N}(E,r).
\]

The resulting recoil-only thermalization radii are:

| Daughter energy | P1-G transport radius | Recoil-only \(R_{\rm therm}\) |
|---:|---:|---:|
| 100 MeV | 22.37 km | 21.02 km |
| 150 MeV | 23.34 km | 22.29 km |
| 255 MeV | 24.62 km | 23.95 km |
| 500 MeV | 26.23 km | 26.09 km |

The broad P1-G density-tail read-off envelope gives the following recoil-only \(R_{\rm therm}\) ranges:

| Daughter energy | Low-density tail | Central tail | High-density tail |
|---:|---:|---:|---:|
| 100 MeV | 19.88 km | 21.02 km | 22.11 km |
| 150 MeV | 20.83 km | 22.29 km | 23.48 km |
| 255 MeV | 22.08 km | 23.95 km | 25.29 km |
| 500 MeV | 23.69 km | 26.09 km | 27.61 km |

The low-tail 100 MeV result lies just inside the 20 km end of the figure-read-off profile and should be treated as a boundary diagnostic, not a precise radius.

**Preliminary interpretation:** once recoil is distinguished from total transport scattering, the energy-thermalization radius is inside the transport radius for most of the 100--255 MeV daughter range. The highest-energy daughter tail can remain energy-coupled somewhat farther out. Thus the P1-G assumption that every \(\nu N\) scattering removes a daughter from the energy-carrying beam is conservative for direct unscattered survival, but it is not a calculation of energy deposition.

This pilot does not include the additional inelastic \(NN\) kernel. That contribution can move the energy sphere outward relative to the recoil-only result. The table is therefore a recoil-only reference, not the final energy sphere.

## 5. Why this does not yet give the daughter-pair escape probability

The thermalization depth is a diagnostic for where a neutrino exchanges energy with the medium. It is not itself the probability that a nonthermal daughter pair deposits all its energy.

For the actual vector-decay daughters,
\[
E_{1,2}=\frac{\omega}{2}(1\pm\beta z),\qquad
\beta=\sqrt{1-m_V^2/\omega^2},
\]
and the energy carried by each daughter must be propagated with its own energy-dependent collision kernel. A neutrino-nucleon collision can:
- change the propagation direction;
- transfer only part of the neutrino energy to a nucleon;
- leave a lower-energy neutrino that can still escape;
- be followed by further scattering or pair processes.

Consequently, \(e^{-\tau_{\rm therm}}\) must not be inserted as an exact daughter escape probability. The next physical calculation is a Monte Carlo or discretized Boltzmann propagation of the injected \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) distributions, retaining the energy and angle redistribution. The thermalization-depth calculation is used to validate and interpret that transport solution.

## 6. Concrete next calculation

1. Digitize the full \(n_B(r)\) and \(n_p(r)\) curves from Caputo et al. Fig. 1 through 20 km, preserving the figure-read-off uncertainty. Set \(n_n=n_B-n_p\) and join continuously to the existing P1-G outer-tail envelope.
2. Interpolate the already archived \(T(r)\) profile and use the same radial coordinate and snapshot convention.
3. Implement the relativistic neutral-current \(\nu n\) and \(\nu p\) differential cross sections with recoil, weak magnetism, and nucleon form factors for the transport kernel. Retain the P1-G \(E^2\) mean-free-path scaling as a comparison baseline.
4. Implement the recoil effective opacity of Müller--Janka as a cross-check of the energy-transfer moment.
5. Implement the Hannestad--Raffelt inelastic \(NN\) scattering and inverse-bremsstrahlung kernel in its stated domain of validity. Compare nondegenerate, partially degenerate, and correlation-stress variants; do not extrapolate the long-wavelength kernel to 500 MeV without a momentum-transfer check.
6. Compute \(\tau_{\rm therm}(E,r)\) and \(R_{\rm therm}(E)\) for daughter energies over the full kinematic support, not only at \(\omega/2\).
7. Propagate the actual daughter energy-angle distribution through the radial background. Keep neutrino and antineutrino, muon and tau flavors, and the vector polarization weights separate.
8. Compare the energy deposited in the medium, the energy escaping in neutrinos, and the unscattered component. Only the full energy-weighted result can replace the P1-G proxy in a physical B.2 boundary study.

## 7. Scope and stopping rules

- Keep \(R_{\max}=25\) km as the literal Blinov B.2 reproduction baseline.
- Do not fit an energy-dependent radius to Fig. 7.
- Do not treat the recoil-only \(R_{\rm therm}\) table as a corrected B.2 luminosity.
- Do not infer a factor-of-three polarization correction.
- Do not update the axial-vector constraint curve until the pure-vector benchmark and the energy-redistribution model have independent acceptance.
- The lack of raw Garching arrays is a limitation on precision, not a reason to stop: the public-profile/literature calculation can provide a controlled estimate and an explicit uncertainty envelope.

## References

1. M. Th. Keil, G. G. Raffelt, and H.-T. Janka, “Monte Carlo Study of Supernova Neutrino Spectra Formation,” Astrophys. J. 590, 971 (2003), especially Eqs. (1)--(2), arXiv:astro-ph/0208035.
2. S. Hannestad and G. Raffelt, “Supernova Neutrino Opacity from Nucleon-Nucleon Bremsstrahlung and Related Processes,” Astrophys. J. 507, 339 (1998), especially Secs. 2.2--2.3 and 3.4, arXiv:astro-ph/9711132.
3. B. Müller and H.-Th. Janka, “Non-radial instabilities and progenitor asphericities in core-collapse supernovae,” Mon. Not. R. Astron. Soc. 448, 2141 (2015), Appendix A, especially Eq. (A31), DOI: 10.1093/mnras/stv101.
4. G. G. Raffelt, H.-T. Janka, and D. F. G. Fiorillo, “Neutrinos from core-collapse supernovae,” 2025 review, Sec. 2.2, arXiv:2509.16306.
5. A. Caputo, G. Raffelt, and E. Vitagliano, “Muonic boson limits: Supernova redux,” Phys. Rev. D 105, 035022 (2022), Fig. 1, DOI: 10.1103/PhysRevD.105.035022.
6. N. Blinov et al., “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” JHEP 06 (2026) 155, Appendix B, arXiv:2511.09619.
