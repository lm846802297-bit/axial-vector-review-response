# P1-Ib: Exact free-nucleon recoil and weak-magnetism moments

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107  
Scope: local free-space collision-kernel baseline only. No stellar optical depth, B.2 luminosity, Fig. 7 curve, or axial-vector constraint is changed.

## 1. Main result

The next baseline should not be a universal \(E_\nu^2\) mean-free-path law with identical neutrino and antineutrino opacities.

Horowitz (2002) provides an exact-in-\(E_\nu/M_N\) free-nucleon neutral-current differential cross section for an initially stationary nucleon, including recoil and weak magnetism. Appendix II supplies finite-size form factors. This lets us calculate both angular redistribution and the energy transferred to the nucleon without replacing a collision by complete absorption.

The first numerical implementation is complete for
\[
\nu n,\quad \bar\nu n,\quad \nu p,\quad \bar\nu p
\]
at \(E_\nu=50,100,150,255,500\) MeV.

This is a free-nucleon reference kernel, not yet the finite-temperature, degenerate SFHo-18.8 medium kernel.

## 2. Exact kinematics and differential cross section

For a nucleon initially at rest,
\[
\eta\equiv\frac{E'_\nu}{E_\nu}
=\frac{1}{1+(E_\nu/M_N)(1-\cos\theta)},
\qquad E'_\nu=\eta E_\nu,
\]
and
\[
Q^2=2E_\nu^2\eta(1-\cos\theta).
\]

Horowitz Eqs. (12)--(13) give
\[
\frac{d\sigma}{d\Omega}
=\frac{G_F^2 E_\nu^2}{4\pi^2}\eta^2\,\mathcal B,
\]
where
\[
\begin{aligned}
\mathcal B={}&
c_V^2[1+\eta^2-\eta(1-x)]
+c_A^2[1+\eta^2+\eta(1-x)]\\
&\pm2c_A(c_V+F_2)(1-\eta^2)\\
&+\frac{\eta^2 e^2}{2}(1-x)
\left[F_2^2(3-x)+4c_VF_2(1-x)\right],
\end{aligned}
\]
with \(x=\cos\theta\), \(e=E_\nu/M_N\), and the upper/lower interference sign for neutrinos/antineutrinos.

The \(Q^2\)-dependent \(c_V,c_A,F_2\) are taken from Horowitz Appendix II. The neutral-current couplings for protons and neutrons use Table I. The code evaluates the full angular distribution rather than only an energy-averaged correction factor.

## 3. Three distinct moments

The implementation computes
\[
\sigma_{\rm tot}=\int d\sigma,
\]
\[
\sigma_{\rm ang}=\int(1-\cos\theta)d\sigma,
\]
\[
\sigma_{\rm mom}=\int(1-\eta\cos\theta)d\sigma,
\]
and
\[
\sigma_E=\int(1-\eta)d\sigma.
\]

Here \(\sigma_{\rm ang}\) is Horowitz's conventional angular-transport moment. Horowitz notes that its strict interpretation assumes \(E'_\nu\simeq E_\nu\). The additional \(\sigma_{\rm mom}\) retains the outgoing momentum magnitude and is therefore a useful exact kinematic moment when recoil is appreciable.

The energy-loss moment \(\sigma_E\) measures the energy deposited into a stationary target per unit path length, before medium thermal-motion and blocking corrections are included.

An exact kinematic identity follows:
\[
1-\eta=\frac{e(1-x)}{1+e(1-x)},
\]
\[
1-\eta x=\frac{(1+e)(1-x)}{1+e(1-x)},
\]
hence
\[
\boxed{\frac{\sigma_E}{\sigma_{\rm mom}}
=\frac{E_\nu}{M_N+E_\nu}}.
\]
This identity is independent of the detailed angular matrix element for a stationary target. Numerically, it is satisfied to a relative residual below \(4\times10^{-16}\).

## 4. Numerical results

### 4.1 Neutron targets

Cross sections below are in \(10^{-40}\ {\rm cm}^2\), using the Horowitz finite-size form factors.

| \(E_\nu\) | \(\sigma_{\rm ang}^{\nu n}\) | \(\sigma_{\rm ang}^{\bar\nu n}\) | \(\bar\nu/\nu\) | Mean loss \(\nu n\) | Mean loss \(\bar\nu n\) |
|---:|---:|---:|---:|---:|---:|
| 100 MeV | 2.074 | 1.127 | 0.543 | 9.19% | 7.90% |
| 150 MeV | 3.985 | 1.711 | 0.429 | 12.52% | 10.03% |
| 255 MeV | 7.681 | 2.291 | 0.298 | 17.35% | 12.17% |
| 500 MeV | 10.293 | 2.095 | 0.204 | 21.50% | 12.32% |

The weak-magnetism asymmetry is already substantial at 100 MeV and becomes very large at the upper end of the daughter spectrum.

### 4.2 Proton targets

| \(E_\nu\) | \(\sigma_{\rm ang}^{\nu p}\) | \(\sigma_{\rm ang}^{\bar\nu p}\) | \(\bar\nu/\nu\) | Mean loss \(\nu p\) | Mean loss \(\bar\nu p\) |
|---:|---:|---:|---:|---:|---:|
| 100 MeV | 1.730 | 1.047 | 0.605 | 9.71% | 8.84% |
| 150 MeV | 3.252 | 1.613 | 0.496 | 13.17% | 11.45% |
| 255 MeV | 6.071 | 2.193 | 0.361 | 18.17% | 14.35% |
| 500 MeV | 7.835 | 1.946 | 0.248 | 22.47% | 14.82% |

The proton and neutron contributions must eventually be combined using the same-snapshot \(n_p(r)\) and \(n_n(r)\) profiles. They must not be combined with an unrelated electron fraction.

### 4.3 Finite-size form factors and failure of pure \(E^2\) extrapolation

Relative to the pointlike Horowitz kernel, the neutron-target angular-transport moment is suppressed by:

| \(E_\nu\) | \(\nu n\) form-factor ratio | \(\bar\nu n\) form-factor ratio |
|---:|---:|---:|
| 100 MeV | 0.908 | 0.924 |
| 150 MeV | 0.817 | 0.859 |
| 255 MeV | 0.611 | 0.729 |
| 500 MeV | 0.274 | 0.519 |

Normalizing each species to its own 100 MeV cross section, the ratio to pure \(E_\nu^2\) scaling at 500 MeV is
\[
\frac{\sigma_{\rm ang}^{\nu n}(500)}
{\sigma_{\rm ang}^{\nu n}(100)(500/100)^2}
\simeq0.199,
\]
\[
\frac{\sigma_{\rm ang}^{\bar\nu n}(500)}
{\sigma_{\rm ang}^{\bar\nu n}(100)(500/100)^2}
\simeq0.074.
\]

These are ratios within the same free-nucleon model, not direct correction factors to the P1-G 25 cm reference mean free path. The latter's precise opacity convention must be checked before comparing normalizations.

## 5. Cross-check against Müller--Janka Eq. (A31)

Müller--Janka use
\[
\alpha_{\rm MJ}(E,T)
=\frac{|E-3T|}{m_n}
\]
as an effective recoil absorption fraction multiplying their scattering opacity.

For the outer-profile temperature \(T=3.03\) MeV, the comparison with the exact stationary-target mean energy-loss fraction is:

| \(E_\nu\) | \(\alpha_{\rm MJ}\) | Exact \(\nu n\) loss fraction | Exact \(\bar\nu n\) loss fraction |
|---:|---:|---:|---:|
| 100 MeV | 0.0968 | 0.0919 | 0.0790 |
| 150 MeV | 0.1500 | 0.1252 | 0.1003 |
| 255 MeV | 0.2617 | 0.1735 | 0.1217 |
| 500 MeV | 0.5225 | 0.2150 | 0.1232 |

For this free-target comparison, the A31 estimate is close at 100 MeV but increasingly exceeds the exact energy-loss fraction at higher energies. At 500 MeV the ratios are approximately 2.43 for \(\nu n\) and 4.24 for \(\bar\nu n\).

This does not prove that the Müller--Janka FMT prescription is incorrect in its intended supernova application. A31 includes a thermal-motion estimate, while the present calculation uses a stationary target and omits Pauli blocking and medium response. It does show that A31 should not be extrapolated uncritically to 500 MeV daughter neutrinos.

## 6. Independent validation

The pointlike angular-transport integral reproduces Horowitz's analytic Eqs. (37)--(42) with a maximum relative residual of
\[
1.4\times10^{-13}.
\]

The exact stationary-target identity
\[
\sigma_E/\sigma_{\rm mom}=E/(M_N+E)
\]
closes to a relative residual below \(4\times10^{-16}\).

Gauss--Legendre integration at 64, 128, 256, 512, and 1024 nodes changes the hardest 500 MeV angular moments by less than \(1.1\times10^{-14}\) relative to the 1024-node result.

## 7. Physical interpretation and limits

The free-nucleon calculation establishes three points:

1. Recoil transfers a non-negligible fraction of the energy per collision for 100--500 MeV daughters.
2. Weak magnetism makes the antineutrino transport opacity substantially smaller than the neutrino opacity.
3. Finite nucleon form factors strongly suppress the high-energy cross section, invalidating an unqualified \(E^2\) extrapolation to 500 MeV.

But the calculation is not yet a supernova-medium transport result. It omits:

- thermal motion of initial nucleons;
- Pauli blocking of final nucleon states;
- mean-field energy shifts and effective masses;
- RPA and other nucleon-nucleon correlations;
- the dynamic structure functions \(S_{n,p}(Q,\omega)\);
- possible strange axial contributions.

Horowitz explicitly separates free-space corrections from these density-dependent medium effects. The next step is to add them using a response model consistent with the adopted SFHo-18.8 background.

## 8. Next implementation order

1. Digitize \(n_B(r)\) and \(n_p(r)\) from Caputo Fig. 1; form \(n_n(r)\) only after confirming the density conventions.
2. Build the local \(\nu n,\bar\nu n,\nu p,\bar\nu p\) finite-temperature collision kernels, including initial nucleon distributions and final-state Pauli blocking.
3. Compare the dilute limit against the Horowitz free-nucleon kernel archived here.
4. Add the finite-\(Q\) response/correlation treatment; keep H&R \(Q\to0\) as a separate limit.
5. Integrate the full energy-angle collision operator for the actual vector-decay daughter distribution.
6. Only then compute radial energy-deposition and escape fractions.

Do not update the literal B.2 \(R_{\max}=25\) km baseline, the pure-vector Fig. 7 comparison, or the axial-vector cooling curve at this stage.

## Reproducibility

- Script: audit_b16_p1i_horowitz_transport_moments.py
- Output: outputs/p1i_horowitz_transport_summary_2026-11-10.json
- Previous kernel-validity audit: B16_P1I_A_LITERATURE_KERNEL_VALIDITY_AND_HIGH_ENERGY_LIMITS_2026-11-10.md

## References

1. C. J. Horowitz, “Weak magnetism for antineutrinos in supernovae,” Phys. Rev. D 65, 043001 (2002), https://arxiv.org/abs/astro-ph/0109209.
2. B. Müller and H.-Th. Janka, “Non-radial instabilities and progenitor asphericities in core-collapse supernovae,” MNRAS 448, 2141 (2015), Appendix A, Eq. (A31), https://doi.org/10.1093/mnras/stv101.
3. S. Hannestad and G. Raffelt, “Supernova Neutrino Opacity from Nucleon-Nucleon Bremsstrahlung and Related Processes,” ApJ 507, 339 (1998), https://arxiv.org/abs/astro-ph/9711132.
4. M. Th. Keil, G. G. Raffelt, and H.-T. Janka, “Monte Carlo Study of Supernova Neutrino Spectra Formation,” ApJ 590, 971 (2003), https://arxiv.org/abs/astro-ph/0208035.
