# P1-Ic: Finite-momentum response domain versus high-energy daughter transport

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107  
Scope: literature-domain audit plus a local kinematic support calculation. No B.2 opacity, luminosity, Fig. 7 curve, or axial-vector constraint is changed.

## 1. Question

Can the published finite-temperature response functions used in ordinary supernova neutrino transport be applied directly to the \(100\)--\(510\) MeV nonthermal \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) daughters produced in our vector-decay calculation?

The answer is: some of the response formalisms are useful, but their commonly used low-\(q\) approximations do not cover most of the transport- and energy-transfer-weighted phase space of these daughters.

## 2. What the in-medium response papers actually cover

### 2.1 Reddy, Prakash & Lattimer (1999)

Their neutral-current differential rate is written in terms of the density and spin-density dynamic structure functions:
\[
\frac{1}{V}\frac{d^3\sigma}{d\Omega^2\,dq_0}
=
\frac{G_F^2}{8\pi^3}E_3^2[1-f_\nu(E_3)]
\left[
c_V^2(1+\cos\theta)S_{00}(q_0,q)
+c_A^2(3-\cos\theta)S_{10}(q_0,q)
\right],
\]
with
\[
q_0=E_1-E_3,\qquad
q=|\mathbf k_1-\mathbf k_3|.
\]
Their free-gas response includes Pauli blocking through the finite-\((q_0,q)\) Lindhard function, and their RPA construction modifies the density and spin responses.

The important qualification is in their discussion of the particle-hole interaction: for the temperatures and thermal-neutrino energies of interest in the PNS, \(q_0\) and \(q\) are typically below a few tens of MeV. They therefore neglect the momentum dependence of the effective particle-hole interaction.

This is a well-motivated approximation for thermal supernova neutrinos. It is not automatically a controlled high-\(q\) interaction model for the nonthermal daughters considered here.

### 2.2 Horowitz et al. (2017), virial response

The virial calculation provides a useful low-density axial response \(S_A(n,T,Y_p)\) and connects low-density virial results to Burrows--Sawyer RPA calculations. However, the published virial result is explicitly in the long-wavelength limit.

It is therefore a valuable \(q\to0\) medium-correlation benchmark, not a finite-\(q\) transport kernel for 100--510 MeV daughters.

### 2.3 Bedaque et al. (2018)

Their dynamical structure factors are calculated for a hot, dilute neutron gas using a virial expansion. The scaling relations quoted by the authors apply to
\[
T=5\text{--}10\ {\rm MeV},\qquad q<30\ {\rm MeV}.
\]
The paper is especially useful for understanding low-\(q\) backscattering suppression in the neutrinosphere. It does not establish the same correction at \(q\sim100\text{--}500\) MeV.

## 3. Kinematic support calculation

I used the Horowitz (2002) free-nucleon neutral-current differential cross section, including recoil, weak magnetism, and the Appendix-II finite-size form factors.

For an initially stationary nucleon,
\[
E'=\frac{E}{1+(E/M)(1-\cos\theta)},
\]
and the spatial momentum transfer is
\[
q=|\mathbf k-\mathbf k'|
=\sqrt{E^2+E'^2-2EE'\cos\theta}.
\]

For each incident energy and each \(\nu n,\bar\nu n,\nu p,\bar\nu p\) channel, I integrated the fraction of three moments lying below a chosen momentum-transfer cut:
\[
F_{\rm tot}(q_c)=
\frac{\int_{q<q_c}d\sigma}{\int d\sigma},
\]
\[
F_{\rm ang}(q_c)=
\frac{\int_{q<q_c}(1-\cos\theta)d\sigma}
{\int(1-\cos\theta)d\sigma},
\]
\[
F_E(q_c)=
\frac{\int_{q<q_c}(1-E'/E)d\sigma}
{\int(1-E'/E)d\sigma}.
\]

The boundary \(q=q_c\) is solved before integration, so the step function is not sampled on a coarse angular grid. The 400- versus 800-node convergence check gives a maximum absolute difference below \(3.2\times10^{-14}\) for the representative cases.

### 3.1 Neutron target: representative results

The table gives the fractions for a neutron target. Each entry is shown as \(\nu n/\bar\nu n\).

| Incident \(E\) | \(q_c\) | Total-scattering fraction | Angular-transport fraction | Energy-loss fraction |
|---:|---:|---:|---:|---:|
| 100 MeV | 30 MeV | 2.34% / 3.61% | 0.05% / 0.10% | 0.06% / 0.11% |
| 100 MeV | 100 MeV | 27.21% / 36.84% | 7.29% / 11.02% | 8.00% / 11.99% |
| 255 MeV | 30 MeV | 0.54% / 1.20% | below 0.01% / 0.01% | below 0.01% / 0.01% |
| 255 MeV | 100 MeV | 5.99% / 12.62% | 0.28% / 0.86% | 0.36% / 1.06% |
| 255 MeV | 200 MeV | 23.93% / 42.79% | 4.59% / 11.35% | 5.71% / 13.45% |
| 500 MeV | 30 MeV | 0.29% / 0.71% | below 0.01% / below 0.01% | below 0.01% / below 0.01% |
| 500 MeV | 100 MeV | 3.19% / 7.62% | 0.05% / 0.25% | 0.08% / 0.32% |
| 500 MeV | 200 MeV | 12.33% / 27.08% | 0.82% / 3.43% | 1.19% / 4.39% |
| 500 MeV | 300 MeV | 26.21% / 50.73% | 3.92% / 13.80% | 5.54% / 17.10% |

The proton-target results are archived in the accompanying JSON file and follow the same trend.

### 3.2 Interpretation

The low-\(q\) region can contribute a non-negligible fraction of the *total* scattering rate, especially for antineutrinos. But it contributes a much smaller fraction of the angular-transport and energy-loss moments.

For example, at 500 MeV, the \(q<30\) MeV region accounts for only about 0.29% of the total \(\nu n\) cross section and essentially none of its angular-transport or energy-loss moment. Even extending the cut to \(q<100\) MeV captures only about 0.05% of the \(\nu n\) angular-transport moment and 0.08% of the energy-loss moment.

This is the relevant distinction for our problem. A low-\(q\) response correction can be important for thermal neutrino decoupling while having very little leverage over the energy redistribution of a 500 MeV daughter.

These fractions are kinematic support diagnostics, not collision probabilities and not multiplicative corrections to the cross section.

## 4. Consequence for the P1-I model

The literature-driven model should be split by momentum-transfer domain.

1. **High-\(q\) baseline:** use the Horowitz finite-recoil, weak-magnetism, finite-form-factor free-nucleon kernel as the starting point.
2. **Low-\(q\) medium correction:** use Reddy/Burrows--Sawyer or virial response functions only in the domain where their particle-hole interactions and response fits are controlled.
3. **Intermediate/high-\(q\) response:** do not extrapolate the low-\(q\) virial fit or a constant-\(V_{ij}\) RPA interaction. A momentum-dependent response or a justified impulse-approximation treatment is required.
4. **Composition:** combine neutron and proton channels only after digitizing \(n_B(r)\) and \(n_p(r)\) from the same published SFHo-18.8 profile and confirming their density conventions.

The \(q<30\) MeV virial response should not be applied as a universal multiplier to the 100--510 MeV daughter opacity.

## 5. Remaining limitations

The kinematic support calculation assumes a stationary free nucleon. It does not include:

- thermal motion of the initial nucleon;
- final-state Pauli blocking;
- mean fields and effective masses;
- RPA or other nucleon correlations;
- finite-temperature broadening of the response.

These effects must be included in the next medium-response calculation. They do not alter the main domain warning: the high-energy daughter transport moments sample a broad, substantially higher-\(q\) region than the low-\(q\) virial response fits.

## 6. Next step

The next calculation should implement a finite-\((q_0,q)\) free Fermi-gas response with Pauli blocking and compare it against the Horowitz stationary-target limit. The medium response should then be upgraded using a momentum-dependent interaction only where a published model supports that extrapolation.

Do not update the literal B.2 \(R_{\max}=25\) km baseline, the pure-vector Fig. 7 comparison, or the axial-vector cooling curve yet.

## Reproducibility

- Script: audit_b16_p1i_momentum_transfer_support.py
- Output: outputs/p1i_momentum_transfer_support_2026-11-10.json
- Free-nucleon kernel: audit_b16_p1i_horowitz_transport_moments.py
- Previous validity audit: B16_P1I_A_LITERATURE_KERNEL_VALIDITY_AND_HIGH_ENERGY_LIMITS_2026-11-10.md

## References

1. S. Reddy, M. Prakash, J. M. Lattimer, and J. A. Pons, “Effects of Strong and Electromagnetic Correlations on Neutrino Interactions in Dense Matter,” Phys. Rev. C 59, 2888–2918 (1999), https://doi.org/10.1103/PhysRevC.59.2888.
2. C. J. Horowitz et al., “Neutrino-nucleon scattering in supernova matter from the virial expansion,” Phys. Rev. C 95, 025801 (2017), https://arxiv.org/abs/1611.05140.
3. P. F. Bedaque, S. Reddy, S. Sen, and N. C. Warrington, “Neutrino-nucleon scattering in the neutrino-sphere,” Phys. Rev. C 98, 015802 (2018), https://arxiv.org/abs/1801.07077.
4. C. J. Horowitz, “Weak magnetism for antineutrinos in supernovae,” Phys. Rev. D 65, 043001 (2002), https://arxiv.org/abs/astro-ph/0109209.
