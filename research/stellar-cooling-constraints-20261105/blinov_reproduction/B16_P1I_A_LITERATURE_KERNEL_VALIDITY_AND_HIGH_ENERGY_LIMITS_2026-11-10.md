# P1-Ia: Literature-kernel validity and high-energy transfer audit

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107  
Scope: literature cross-check and a local kinematic diagnostic only. No B.2 opacity, luminosity, Fig. 7 curve, or axial-vector constraint is changed.

## 1. Decision

The literature-guided route remains viable, but the initial P1-I proposal needs three qualifications:

1. The Müller--Janka recoil opacity is an effective FMT absorption prescription, not a differential collision kernel and not literal one-collision absorption.
2. The H&R inelastic \(NN\) kernel is a valuable \(Q\to0\) reference, but its long-wavelength approximation cannot be assumed valid for the 100--510 MeV daughter population.
3. The relative importance of inelastic scattering and recoil is model dependent. The statement that inelastic scattering is about ten times stronger applies to its energy-transfer rate relative to pair bremsstrahlung, not universally relative to recoil.

Accordingly, the H&R kernel should be retained as a limiting benchmark and uncertainty bracket. The primary daughter propagation should begin with a finite-recoil, energy- and angle-resolved neutral-current \(\nu n\) and \(\nu p\) collision kernel.

## 2. What the three papers actually establish

### 2.1 Keil, Raffelt & Janka (2003)

Their Eq. (1) defines
\[
\tau_{\rm therm}(E,r)=\int_r^\infty dr'\,
\sqrt{\kappa_E(E,r')\,[\kappa_T(E,r')+\kappa_E(E,r')]}.
\]
This is an effective depth for an energy-changing process in a scattering atmosphere. It distinguishes the energy sphere from the transport sphere.

However, §2.3 explicitly warns that recoil transfers only a small fraction of the neutrino energy per scattering. The authors therefore state that it is not straightforward to define an energy sphere for nucleon recoil alone. In §3.2.1 they also omit \(\nu NN\leftrightarrow NN\nu\) in their Monte Carlo runs because it was not important relative to recoil in the models they studied.

This does not invalidate H&R. It establishes that the hierarchy depends on the stellar background and the adopted approximations. We must not promote either hierarchy to a universal rule.

### 2.2 Müller & Janka (2015), Eq. (A31)

The effective heavy-flavor recoil opacity is
\[
\kappa_{a,\nu N}^{\rm eff}
=\frac{|\epsilon_\nu-3k_{\rm B}T|}{m_n c^2}\,
\kappa_{s,\nu N}.
\]
It is introduced to mimic the energy transfer from nucleon recoil in their FMT scheme. It is useful as an energy-transfer-moment cross-check.

It is not a microscopic absorption process. In particular, it does not specify the outgoing neutrino energy and direction after each collision. Therefore:

- retain it as an effective-opacity diagnostic;
- compare its implied energy-transfer moment with the explicit recoil kernel;
- do not use it as the full daughter transport operator;
- do not interpret its \(\tau_{\rm eff}=2/3\) radius as an exact escape surface.

The recoil-only radii in the original P1-I note should consequently be read as *recoil-effective-depth diagnostics*, not as a complete physical energy sphere.

### 2.3 Hannestad & Raffelt (1998)

The distinction between the two quoted ratios matters.

Their Eq. (3) compares the energy-transfer rates of inelastic \(NN\) scattering and pair bremsstrahlung. The leading ratio is 20, with order-unity corrections reducing the practical estimate to roughly 10.

Their Eq. (7), however, compares inelastic scattering with nucleon recoil:
\[
\frac{\Delta Q_{\rm inelastic}}{\Delta Q_{\rm recoil}}
\simeq 1.21\,\eta_*^{3/2}.
\]
After including the vector-current recoil contribution and finite-pion-mass effects, they suggest the estimate
\[
\frac{\Delta Q_{\rm inelastic}}{\Delta Q_{\rm recoil}}
\sim 0.5\,\eta_*^{3/2}.
\]
For \(\eta_*=2\)--4 this is approximately 1.4--4.0, not a universal factor of ten.

H&R provide a particularly useful Boltzmann starting point. Their Eq. (23) contains pair emission, pair absorption, and neutrino scattering terms in one collision integral. Their Eq. (32) gives the differential scattering cross section in final neutrino energy and angle:
\[
\frac{d\sigma_1}{d\epsilon_2\,d\Omega_2}
=\frac{3-\cos\theta}{4\pi}\,
\frac{C_A^2G_F^2}{\pi}\,
\epsilon_2^2\,
\frac{S_\sigma(\epsilon_1-\epsilon_2)}{2\pi}.
\]
This is conceptually much closer to the transport problem we need than a scalar absorption opacity.

But the nuclear response used in H&R is derived in the long-wavelength limit. Its kernel is a function of energy transfer \(S_\sigma(\omega)\), without the finite neutrino momentum-transfer dependence \(S_\sigma(\omega,\mathbf Q)\). Their approximations also include:

- nonrelativistic nucleons;
- one-pion exchange in Born approximation;
- neutron-neutron interactions only;
- no neutron-proton contribution in the main kernel;
- no nucleon-nucleon correlations;
- applicability to surface layers with \(\rho\lesssim10^{14}\ {\rm g\,cm^{-3}}\).

The analytic interpolation in their Eqs. (49)--(50) is accurate at the 5--10% level in the physically interesting parameter range quoted by the authors. That accuracy concerns their adopted long-wavelength kernel; it does not remove the finite-\(\mathbf Q\) limitation.

### 2.4 Independent finite-momentum-transfer warning

Fischer (2016), in the discussion of the \(\nu NN\leftrightarrow NN\nu\) process, notes that the correct inelastic momentum-transfer dependence needed for Boltzmann collision integrals had not yet been derived in that treatment.

This is directly relevant to our problem. We should not turn the H&R \(Q=0\) response into a purported finite-\(Q\) kernel by inserting the daughter energy into its energy-only fit.

## 3. Numerical diagnostic: how much daughter phase space is at small momentum transfer?

I evaluated the kinematic support of the H&R long-wavelength limit for the existing \(m_V=10\) MeV vector benchmark.

For an incident daughter with energy \(E\), the elastic limit \(E'=E\) gives
\[
Q=|\mathbf k-\mathbf k'|
=2E\sin\frac{\theta}{2}.
\]
Using the H&R angular weight \(3-\cos\theta\), the fraction of scattering-angle weight satisfying \(Q<Q_c\) is
\[
F(E;Q_c)=
\frac{\displaystyle\int_{-1}^{1}d\cos\theta\,
(3-\cos\theta)\,
\Theta(Q_c-Q)}
{\displaystyle\int_{-1}^{1}d\cos\theta\,(3-\cos\theta)}.
\]

I then averaged this fraction over the actual two-body daughter energies
\[
E_{1,2}=\frac{\omega}{2}(1\pm\beta z),\qquad
\beta=\sqrt{1-\frac{m_V^2}{\omega^2}},
\]
using the longitudinal and transverse production weights separately and weighting each daughter by its share of the vector energy.

For a transparent scale diagnostic, I use \(Q_c=m_\pi\), \(m_\pi/2\), and \(m_\pi/4\). These are illustrative thresholds, not a claim that \(Q<m_\pi\) is the exact formal validity condition. The true long-wavelength requirement is stronger and depends on the characteristic nucleon momentum and response scale in the local medium.

| Vector energy \(\omega\) | \(Q_c=m_\pi\) | \(Q_c=m_\pi/2\) | \(Q_c=m_\pi/4\) |
|---:|---:|---:|---:|
| 210 MeV | 29.1% | 9.72% | 3.03% |
| 300 MeV | 16.7% | 5.37% | 1.64% |
| 510 MeV | 7.05% | 2.17% | 0.643% |

These are equal-mode averages over \(L,+,-\), not the physical polarization mixture.

There are two important qualifications:

1. This calculation uses the elastic limit \(E'=E\). For an inelastic event, \(Q_{\min}=|E-E'|\), so the phase space available at small \(Q\) can only decrease.
2. The fractions are kinematic support diagnostics. They are not collision probabilities, rates, or multiplicative corrections to the H&R kernel.

Even with the deliberately generous \(Q_c=m_\pi\) criterion, the energy-weighted daughter support falls from about 29% at \(\omega=210\) MeV to 7% at \(\omega=510\) MeV. This is enough to rule out treating the long-wavelength approximation as a controlled full-phase-space description of the high-energy daughter transport.

## 4. Revised implementation hierarchy

The calculation should now be organized as follows.

### A. Primary transport baseline: one-nucleon neutral-current scattering

Implement the differential \(\nu n\) and \(\nu p\) cross sections with:

- exact recoil kinematics;
- weak-magnetism corrections;
- vector and axial form factors;
- separate neutrino and antineutrino channels;
- energy and angle of the outgoing neutrino retained.

This provides the finite-\(Q\) baseline for daughter redistribution. The existing \(E^2\) mean-free-path prescription remains a comparison scale, not the final opacity.

### B. Nuclear-response correction

Use the H&R \(S_\sigma(\omega)\) kernel as the \(Q\to0\) reference. Do not claim it is the finite-\(Q\) response.

The next theoretical task is to determine whether a sufficiently controlled \(S_\sigma(\omega,Q)\) can be obtained from a published response-function treatment over the daughter kinematics. If not, retain H&R as a low-\(Q\) bracket and quantify the unmodelled finite-\(Q\) region rather than extrapolating it.

### C. Recoil effective-opacity cross-check

Use Müller--Janka Eq. (A31) to compare the integrated recoil energy-transfer moment against the explicit one-nucleon recoil kernel. It is a cross-check, not an additional independent absorption channel to be blindly added to the same collision operator.

### D. Pair processes

Implement inverse bremsstrahlung and pair emission as separate channels with detailed balance. Their contribution to the propagation of a nonthermal high-energy daughter must be evaluated using the actual background neutrino distributions, not inferred from the thermal energy-sphere radius.

### E. Energy-angle transport

Solve the linearized test-particle Boltzmann problem for the injected \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) daughters. Keep the outgoing energy and angle after each collision.

The observables must distinguish:
\[
E_{\rm injected}
=
E_{\rm escaped,\nu}
+
E_{\rm deposited}
+
E_{\rm other\ channels},
\]
with the last term explicitly accounting for any included pair conversion or other sinks. The unscattered component is recorded separately from the total escaping neutrino energy.

## 5. Data and profile status

The current repository's sfho188_digitized.csv contains the thermodynamic and lapse columns, but not \(n_B(r)\) or \(n_p(r)\). The profile provenance records the Caputo \(n_\mu/n_0\) vector path, but the baryon and proton density paths have not yet been added to the committed profile.

Thus the first profile task remains:

1. identify the Caputo Fig. 1 \(n_B\) and \(n_p\) PDF vector paths;
2. digitize and archive both curves with source hashes and axis calibration;
3. compare their common support and continuity;
4. form \(n_n=n_B-n_p\) only after confirming that both plotted quantities use the same baryon-number convention;
5. attach the existing P1-G outer-tail uncertainty envelope without silently replacing the published profile.

No unrelated progenitor, EOS, or post-bounce snapshot is to be spliced into SFHo-18.8.

## 6. Stopping rules

- Keep the literal Blinov B.2 baseline at \(R_{\max}=25\) km.
- Do not use \(e^{-\tau_{\rm therm}}\) as a daughter escape probability.
- Do not treat the recoil-only effective-depth radius as a physical energy sphere.
- Do not multiply the H&R kernel by an empirical high-energy correction.
- Do not infer a universal factor-of-ten enhancement over recoil.
- Do not update the pure-vector Fig. 7 comparison or the axial-vector cooling curve.
- Keep the public-profile uncertainty separate from the collision-kernel uncertainty.

## 7. Reproducibility

- Diagnostic script: audit_b16_p1i_long_wavelength_support.py
- Machine-readable output: outputs/p1i_long_wavelength_support_2026-11-10.json
- Parent P1-I proposal: B16_P1I_LITERATURE_GUIDED_NEUTRINO_THERMALIZATION_2026-11-10.md

## References

1. M. Th. Keil, G. G. Raffelt, and H.-T. Janka, “Monte Carlo Study of Supernova Neutrino Spectra Formation,” Astrophys. J. 590, 971 (2003), especially Eqs. (1)--(2), §2.3, and §3.2.1. https://arxiv.org/abs/astro-ph/0208035
2. S. Hannestad and G. Raffelt, “Supernova Neutrino Opacity from Nucleon-Nucleon Bremsstrahlung and Related Processes,” Astrophys. J. 507, 339 (1998), especially Eqs. (3), (7), (14), (23), and (32). https://arxiv.org/abs/astro-ph/9711132
3. B. Müller and H.-Th. Janka, “Non-radial instabilities and progenitor asphericities in core-collapse supernovae,” Mon. Not. R. Astron. Soc. 448, 2141 (2015), Appendix A, Eq. (A31). https://doi.org/10.1093/mnras/stv101
4. T. Fischer, “The role of medium modifications for neutrino-pair processes from nucleon-nucleon bremsstrahlung,” Astron. Astrophys. 593, A103 (2016), https://arxiv.org/abs/1608.05004
5. A. Caputo, G. Raffelt, and E. Vitagliano, “Muonic boson limits: Supernova redux,” Phys. Rev. D 105, 035022 (2022), Fig. 1. https://arxiv.org/abs/2109.03244
