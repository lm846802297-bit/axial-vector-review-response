# Croon vector benchmark: scope, rate corrections, and execution plan

Date: 2026-11-19  
Status: **benchmark specification; no new luminosity calculation is claimed in this document**

## Executive decision

Use Croon, Elor, Leane and McDermott, *Supernova Muons: New Constraints on Z' Bosons, Axions and ALPs*, JHEP 01 (2021) 107, arXiv:2006.13942, as a **historical vector-model benchmark and method comparison**, not as the sole or automatically correct reference for the production rates.

The paper explicitly says that it considers **only vector couplings** of the \(Z'\). Its muon interaction is vectorial, with equal left- and right-handed couplings. It does not calculate a spin-1 axial-vector \(A'\) model. Its ALP section concerns spin-0 particles and is not a substitute for an axial-vector calculation.

A second, modern vector reference is Blinov et al., *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, arXiv:2511.09619v2. This paper explicitly re-evaluates thermally averaged production rates, including the neutrino chemical-potential dependence and the semi-Compton detailed-balance / phase-space factors. Therefore, the benchmark must retain separate **Croon-literal** and **updated-rate** lanes. Do not silently patch the Croon formulas and then call the result a reproduction of Croon.

A third, independent trapping-regime comparison is Lai, Leung and Lin, Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023. Its plateau prescription and neutrinosphere treatment are a distinct transport lane; do not combine it algebraically with Croon or Blinov.

## 1. Scope of Croon et al. (2021)

Primary sources:

- Published paper: https://doi.org/10.1007/JHEP01(2021)107
- arXiv: https://arxiv.org/abs/2006.13942
- Full published PDF: https://link.springer.com/content/pdf/10.1007/JHEP01%282021%29107.pdf

The authors state in Sec. 4, immediately before Sec. 4.1, that they remain agnostic about the \(Z'\) mass-generation mechanism and **only consider vector couplings**. Eq. (4.1) couples the left-handed lepton doublet and the right-handed muon with the same coefficient:
\[
\mathcal L \supset g_\mu Z'_\alpha
\left(\bar\ell\gamma^\alpha\ell+\bar\mu_R\gamma^\alpha\mu_R\right).
\]
For the charged muon this is
\[
g_\mu Z'_\alpha\bar\mu\gamma^\alpha\mu,
\qquad g_V=g_\mu,\quad g_A=0.
\]
Thus the Croon \(Z'\) rates and bounds are **not** directly transferable to the axial-vector model.

For \(U(1)_{L_\mu-L_\tau}\), Eq. (4.2) has equal-sign left- and right-handed charged-lepton couplings at tree level. The neutrino interaction is left-chiral. The paper also discusses loop-induced kinetic mixing. These model details must be kept separate from a generic muon-only vector benchmark.

## 2. Two production-rate equations that must not be conflated

### 2.1 Neutrino-pair coalescence

Croon Eq. (4.6) gives
\[
\Gamma^{\rm Croon}_{\nu\bar\nu\to Z'}(\omega)
=\frac{\alpha_{Z'}m_{Z'}^2}{3\omega}
\frac{1}{e^{\omega/T}-1}.
\]
This is a useful **Croon-literal reference expression** under its assumptions.

However, the 2026 Blinov et al. Appendix B, Eqs. (B.7)--(B.10), explicitly finds that the neutrino chemical-potential dependence does not generally cancel in the Fermi-Dirac phase-space integral. The cancellation used in older simplified expressions is recovered only in the Maxwell-Boltzmann / negligible-degeneracy limit. The updated rate is written as
\[
\Gamma^{\rm prod}_{\bar\nu\nu\to V}(\omega)
=\frac{m_V}{\omega}\,3\Gamma_{V\to\bar\nu\nu}
I\!\left(\frac{\mu_\nu}{T},\frac{\omega}{T},v_V\right),
\]
with
\[
\Gamma_{V\to\bar\nu\nu}=\frac{\alpha_Vm_V}{6}
\]
for one flavor of left-handed neutrinos, and the explicit Fermi-Dirac function \(I\) given in Eq. (B.9) of that paper. Its absorption integral independently satisfies
\[
\Gamma^{\rm prod}_{\bar\nu\nu\to V}
=e^{-\omega/T}\Gamma^{\rm abs}_{V\to\bar\nu\nu}.
\]

Implementation rule:

1. Reproduce Croon Eq. (4.6) as a named legacy lane.
2. Implement the chemical-potential-dependent B.7--B.10 expression as a separate updated lane.
3. Compare the updated expression with Croon only after matching the number of neutrino flavors, chiral states, the vacuum-width convention (spin-averaged versus polarization-summed), and the definition of the coupling. Do **not** assume the prefactors coincide: Blinov et al. explicitly state that their Maxwell-Boltzmann limit matches Ref. [17] (Lai et al.), not that it reproduces Croon Eq. (4.6). Resolve this normalization algebraically before using it as a regression test.
4. In the actual SFHo calculation, use the \(\nu_\mu\) and \(\nu_\tau\) chemical potentials separately when supplied by the profile. Do not replace them by zero in the production result merely to improve agreement.

Source: https://arxiv.org/abs/2511.09619, Appendix B, Eqs. (B.7)--(B.10).

### 2.1.1 Matched two-flavour normalization: resolved

For the \(L_\mu-L_\tau\) benchmark, the Blinov B.7 rate includes both \(\nu_\mu\) and \(\nu_\tau\), with their chemical potentials kept separately. The one-flavour spin-averaged vacuum width in Blinov Eq. (B.8) is
\[
\Gamma_{V\to\bar\nu\nu}^{(1\,{\rm flavour})}
=\frac{\alpha_Vm_V}{6}.
\]
The factor 3 in Eq. (B.7) converts this spin-averaged width into the polarization-summed production rate. Summing the two flavours gives
\[
\Gamma_{\rm B7}^{(\nu_\mu+\nu_\tau)}
=\frac{m_V^2}{8\pi\omega}
\left[I_{\nu_\mu}+I_{\nu_\tau}\right]
\]
per \(g_{\mu\tau}^2\).

Croon Eq. (4.6), as printed, is
\[
\Gamma_{\rm Croon}^{\rm generic}
=\frac{\alpha_Vm_V^2}{3\omega}f_B(\omega),
\qquad f_B(\omega)=\frac1{e^{\omega/T}-1}.
\]
This is the generic one-neutrino-flavour normalization used for the Croon Fig. 2 baseline. Croon Sec. 4.4 explicitly states that the \(U(1)_{L_\mu-L_\tau}\) model has an additional factor of two in both the differential neutrino power \(Q\) and the neutrino absorptive optical depth \(\tau_{\rm abs}\). Therefore
\[
\Gamma_{\rm Croon}^{L_\mu-L_\tau}
=2\Gamma_{\rm Croon}^{\rm generic}.
\]

The two relevant ratios are consequently
\[
\boxed{
\frac{\Gamma_{\rm B7}^{(\nu_\mu+\nu_\tau)}}{\Gamma_{\rm Croon}^{\rm generic}}
=\frac32\,\frac{I_{\nu_\mu}+I_{\nu_\tau}}{f_B(\omega)},
\qquad
\frac{\Gamma_{\rm B7}^{(\nu_\mu+\nu_\tau)}}{\Gamma_{\rm Croon}^{L_\mu-L_\tau}}
=\frac34\,\frac{I_{\nu_\mu}+I_{\nu_\tau}}{f_B(\omega)}
}.
\]
In the Maxwell-Boltzmann / negligible-occupation limit, \(I_{\nu_\mu}\simeq I_{\nu_\tau}\simeq e^{-\omega/T}\) and \(f_B\simeq e^{-\omega/T}\). Thus the polarization-summed two-flavour B.7 rate is three times the **generic** Croon Eq. (4.6) rate, but \(3/2\) times the **flavour-matched \(L_\mu-L_\tau\)** Croon rate. The factor 3 is the vector-polarization sum in B.7; the factor 2 is the additional neutrino-flavour multiplicity specified in Croon Sec. 4.4. These factors are distinct and must not be conflated.

This is consistent with Lai et al. Eq. (10), which gives the two-flavour Maxwell-Boltzmann rate
\[
\Gamma_{\rm Lai}^{\rm MB}
\simeq\frac{g_{\mu\tau}^2m_V^2}{4\pi\omega}e^{-\omega/T}.
\]
The B.7 two-flavour rate reduces to this expression in the stated limit. Croon Eq. (4.6) is retained literally as the generic one-flavour benchmark; for \(L_\mu-L_\tau\), its Sec. 4.4 factor of two must be applied to both neutrino production and absorption. We do not silently insert a factor 3 into Croon's code.

Away from the Maxwell-Boltzmann limit, the ratio is not a constant. For \(E_1+E_2=\omega\), the exact Fermi identity
\[
f_{\bar\nu}(E_1;-\mu_\nu)f_\nu(E_2;\mu_\nu)
=f_B(\omega)\left[1-f_{\bar\nu}(E_1;-\mu_\nu)-f_\nu(E_2;\mu_\nu)\right]
\]
shows how Pauli occupancy suppresses the B.7 integral relative to the Bose factor used in Croon Eq. (4.6).

A direct 1024-point Gauss-Legendre integration of the B.6 angular average was performed at \(m_V=10\) MeV using the archived SFHo-18.8 profile (SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c); \(\mu_{\nu_\tau}=0\) follows the published profile assumption. The pointwise B.7/Croon-generic ratio is:

| Radius | \(\omega=12\) MeV | \(\omega=50\) MeV | \(\omega=210\) MeV |
|---:|---:|---:|---:|
| 0 km | 0.2724 | 1.0175 | 2.3788 |
| 8 km | 0.2235 | 0.8812 | 2.2178 |
| 12.5 km | 0.3738 | 1.3488 | 2.5278 |
| 15 km | 0.6655 | 1.9454 | 2.7394 |

For the same-model \(L_\mu-L_\tau\) ratio, divide these entries by two. Neither a universal factor 3 nor the Croon Bose-factor spectrum reproduces the local B.7 spectrum over the full SN energy range.

Reproduction code:
- blinov_reproduction/croon_neutrino_rate_comparison.py
- blinov_reproduction/test_croon_neutrino_rate_comparison.py
- blinov_reproduction/outputs/croon_blinov_neutrino_rate_comparison_2026-11-19.json

Sources: Croon et al., https://arxiv.org/abs/2006.13942, Sec. 4.4 and Eqs. (4.5)--(4.6); Blinov et al., https://arxiv.org/abs/2511.09619, Appendix B, Eqs. (B.6)--(B.10); Lai et al., https://arxiv.org/abs/2401.16023, Eq. (10) and the discussion immediately below it.

### 2.1.2 Full-profile energy-integrated local emissivity scan

The local spectral comparison was extended to the complete archived SFHo-18.8 profile. At each of the 1687 profile radii, both rates were integrated over the same massive-vector phase space,
\[
Q(r)=\frac1{2\pi^2}\int_{m_V}^{m_V+36T(r)}
d\omega\;\omega^2\sqrt{\omega^2-m_V^2}\,
\Gamma_{\rm prod}(\omega,r).
\]
The B.7 integrand uses the two flavours separately, with the tabulated \(\mu_{\nu_\mu}(r)\) and \(\mu_{\nu_\tau}=0\); the Croon integrand uses Eq. (4.6) literally. All results are per \(g_X^2\), with \(m_V=10\) MeV.

**Flavour-matched comparison:** Croon Eq. (4.6) is the generic one-neutrino-flavour normalization used for the Fig. 2 baseline. Croon Sec. 4.4 explicitly states that the \(U(1)_{L_\mu-L_\tau}\) model has an additional factor of two in both the differential neutrino power and the neutrino absorptive optical depth. Thus the generic ratio below is an equation-level comparison, not the same-model comparison. For the latter, use \(Q_{\rm Croon}^{L_\mu-L_\tau}=2Q_{\rm Croon}^{\rm generic}\), so every B.7/generic ratio below must be divided by two.

The 1687-point radial scan gives
\[
1.05929\leq \frac{Q_{\rm B7}^{(\nu_\mu+\nu_\tau)}(r)}
{Q_{\rm Croon}^{\rm Eq.(4.6)}(r)}
\leq 2.31942,
\]
with the minimum at \(r=0\) km and the maximum at \(r=25\) km.

The same-model \(L_\mu-L_\tau\) ratios are therefore
\[
0.529645\leq
\frac{Q_{\rm B7}^{(\nu_\mu+\nu_\tau)}(r)}
{Q_{\rm Croon}^{L_\mu-L_\tau}(r)}
\leq 1.15971.
\]
At the six radii in the table, the corresponding ratios are respectively 0.529645, 0.720485, 0.749456, 0.799087, 1.10301 and 1.15971. These are obtained from the archived generic-rate output by the exact factor-two prescription; the updated machine-readable output separately stores both normalizations.

| Radius | \(T\) [MeV] | \(\mu_{\nu_\mu}\) [MeV] | \(Q_{\rm B7}\) [MeV\(^5\)] | \(Q_{\rm Croon}\) [MeV\(^5\)] | Ratio |
|---:|---:|---:|---:|---:|---:|
| 0 km | 19.2652 | -58.6138 | \(2.19077\times10^3\) | \(2.06815\times10^3\) | 1.05929 |
| 8.482 km | 39.2497 | -18.0203 | \(2.71734\times10^4\) | \(1.88577\times10^4\) | 1.44097 |
| 12.5 km | 23.8820 | -2.59166 | \(6.09637\times10^3\) | \(4.06719\times10^3\) | 1.49891 |
| 15 km | 13.2314 | 0 | \(9.81433\times10^2\) | \(6.14097\times10^2\) | 1.59817 |
| 22 km | 3.55139 | 0 | 8.41804 | 3.81594 | 2.20602 |
| 25 km | 3.03377 | 0 | 3.99954 | 1.72437 | 2.31942 |

This does **not** contradict the fixed-energy table, where the B.7/Croon ratio can be below one at low \(\omega/T\). The emissivity integral weights the spectrum by \(\omega^2\sqrt{\omega^2-m_V^2}\); the higher-energy part of the spectrum consequently has much more leverage on \(Q\) than the low-energy pointwise rate. One must not infer an integrated emissivity correction from a single fixed-\(\omega\) ratio.

The full radial scan used energy order 64 and angular order 128. At six anchors (0, 8.482, 12.5, 15, 22 and 24 km), refinement to energy order 96 and angular order 256 changed \(Q_{\rm B7}\) by at most \(3.8\times10^{-15}\) and \(Q_{\rm Croon}\) by at most \(2.5\times10^{-15}\). This is a selected-anchor convergence check, not an exhaustive high-order scan at all 1687 radii.

Machine-readable full profile (1687 rows, generic and flavour-matched ratios): [GitHub Actions artifact](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495081528). Artifact SHA-256: \`494a74a0b772a00c6f5f5d24989439b408880fa0dbdb8323ef1c9e6101f4a2ac\`. The input profile SHA-256 is \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.

This is an energy-integrated **local emissivity** comparison only. It does not perform the radial proper-volume integral, lapse/redshift weighting, attenuation, escape-probability calculation, or total luminosity integration.

Reproduction code and tests:
- \`blinov_reproduction/croon_blinov_neutrino_emissivity.py\`
- \`blinov_reproduction/test_croon_blinov_neutrino_emissivity.py\`

### 2.1.3 Optically-thin volume-integrated neutrino-coalescence contribution

The full-profile \(Q(r)\) scan was next integrated over the Croon Eq. (3.1) flat spherical volume, using the \(T=3\) MeV neutrinosphere definition and the same two local rate prescriptions. The profile's final tabulated point is at 25 km with \(T=3.03377\) MeV; linear extrapolation of the last two temperature nodes gives
\[
R_\nu=25.1511683\ {\rm km}.
\]
The last 0.15117 km is filled by a linear extrapolation of the local emissivity. The radial integral is evaluated analytically for piecewise-linear \(Q(r)\):
\[
L_{\nu\bar\nu}^{\rm free}
=\int_0^{R_\nu}4\pi r^2\,dr\,Q_{\nu\bar\nu}(r).
\]
The conversion from natural units to erg/s is performed after the volume integral.

For the \(m_V=10\) MeV benchmark, the resulting **neutrino-coalescence channel only**, per \(g_X^2\), is
\[
\boxed{
L_{\rm B7}^{\rm free}/g_X^2
=4.45183\times10^{70}\ {\rm erg\,s^{-1}},
\qquad
L_{\rm Croon}^{\rm free}/g_X^2
=3.05794\times10^{70}\ {\rm erg\,s^{-1}}
}
\]
and
\[
\boxed{
L_{\rm B7}^{\rm free}/L_{\rm Croon}^{\rm free}=1.455827.
}

Here \(L_{\rm Croon}^{\rm free}\) is the **generic one-flavour** Eq. (4.6) result. For the same \(L_\mu-L_\tau\) model as B.7, Croon Sec. 4.4 gives
\[
L_{\rm Croon,\,L_\mu-L_\tau}^{\rm free}/g_X^2
=6.11588\times10^{70}\ {\rm erg\,s^{-1}},
\qquad
\frac{L_{\rm B7}^{\rm free}}{L_{\rm Croon,\,L_\mu-L_\tau}^{\rm free}}
=0.72791354.
\]
Thus the earlier 1.455827 ratio is retained only as a generic one-flavour equation comparison; 0.72791354 is the flavour-matched ratio. The Croon factor of two must also be applied to its absorptive optical depth before comparing finite-coupling luminosity curves.
The direct trapezoidal cross-check differs from the analytic piecewise-linear radial integral by only \(5.8\times10^{-6}\) for each channel.

At \(g_X=10^{-9}\), these channel-only optically-thin values scale to \(4.45183\times10^{52}\), \(3.05794\times10^{52}\), and \(6.11588\times10^{52}\) erg/s for B.7, generic Croon, and flavour-matched Croon, respectively. This is a useful normalization comparison against the \(3\times10^{52}\) erg/s Raffelt scale, **not a cooling bound**: this calculation has no attenuation, no semi-Compton contribution, no lapse/redshift factor, and no transport/escape probability. In particular, one must not interpret the \(g_X=10^{-9}\) scaling point as necessarily lying in the free-streaming regime.

The updated 1687-row profile artifact stores both generic and flavour-matched local emissivities and their volume integrals: [GitHub Actions artifact](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495081528). Artifact SHA-256: \`494a74a0b772a00c6f5f5d24989439b408880fa0dbdb8323ef1c9e6101f4a2ac\`.

### 2.1.4 C0 luminosity with absorption: generic Croon versus \(L_\mu-L_\tau\)

A separate C0 calculation evaluates the energy-dependent local source, radial optical depth and attenuated luminosity,
\[
L_{Z'}^{\rm free}=\int_0^{R_\nu}4\pi r^2dr
\int d\omega\,
\frac{\omega^2\sqrt{\omega^2-m_V^2}}{2\pi^2}
\left[\Gamma_{\nu\bar\nu}^{\rm prod}+
\Gamma_{\gamma\mu}^{\rm prod}\right]e^{-\tau(\omega,r)}.
\]
It follows Croon Eqs. (3.3)--(3.4), (4.6)--(4.7): flat \(4\pi r^2dr\), no lapse/redshift, no angular escape average, and no explicit \(1/v_V\) in the optical-depth integral. The standard outer boundary is \(R_{\rm far}=100\) km and retains the vacuum \(Z'\to\nu\bar\nu\) absorption tail. The \(R_{\rm far}=R_\nu\) result is retained as a separate sensitivity.

For \(m_V=10\) MeV, the optically-thin channel luminosities per \(g_X^2\) are:

| Channel | Generic one-flavour Croon | \(L_\mu-L_\tau\) transfer |
|---|---:|---:|
| Neutrino coalescence | \(3.05794\times10^{70}\) | \(6.11588\times10^{70}\) |
| Semi-Compton | \(1.05404\times10^{70}\) | \(1.05404\times10^{70}\) |
| Total | \(4.11198\times10^{70}\) | \(7.16992\times10^{70}\) |

The \(L_\mu-L_\tau\) transfer doubles the neutrino source and neutrino absorption only; it does not double the semi-Compton source.

Using the \(3\times10^{52}\) erg/s Raffelt reference line and \(R_{\rm far}=100\) km, the two provisional crossings are:

| Model | Low-\(g_X\) crossing | High-\(g_X\) crossing |
|---|---:|---:|
| Generic one-neutrino-flavour | \(8.60466\times10^{-10}\) | \(3.19141\times10^{-8}\) |
| \(L_\mu-L_\tau\), factor two in \(Q_\nu\) and \(\tau_\nu\) | \(6.52618\times10^{-10}\) | \(2.18470\times10^{-8}\) |

At \(g_X=10^{-9}\), the attenuated total luminosities are \(4.03156\times10^{52}\) erg/s and \(6.88108\times10^{52}\) erg/s, respectively. These are C0 volume-emission reference curves, not complete SN1987A exclusion limits.

The numerical audit gives:
- baseline quadrature \((N_\omega,N_{\tau,\omega},N_p)=(64,301,128)\);
- high-order quadrature \((96,601,192)\);
- maximum relative change in total luminosity below \(1.95\times10^{-4}\);
- adding \(\mu^+\) changes the total at \(g_X=10^{-9}\) by 0.18%;
- using \(R_{\rm far}=R_\nu\) shifts the high-\(g_X\) crossing to \(8.60158\times10^{-8}\) (generic) or \(6.20862\times10^{-8}\) (\(L_\mu-L_\tau\)), while the low-\(g_X\) crossing changes by less than 1%.

The independent 0.05 km Simpson implementation of the full Croon Fig. 2 mass sweep gives, at 10 MeV, low/high crossings \(8.60711\times10^{-10}\) and \(3.18779\times10^{-8}\). These agree with the 1687-node C0 adapter to 0.03% and 0.11%, respectively. This checks numerical implementation consistency, not agreement with digitized Fig. 2 data.

Outputs from successful workflow run [#44449522338](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338):
- [Generic 10 MeV C0 curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495061522)
- [\(L_\mu-L_\tau\) 10 MeV C0 curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495290606)
- [High-order C0 curve](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495071605)
- [Charge-conjugate sensitivity](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495400333)
- [Convergence and convention audit](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14495515156)
- [Full Croon Fig. 2 mass sweep](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44449522338/artifacts/14494204948)

This remains a public-profile reconstruction. The original raw Garching radial table is unavailable in the current workspace; no claim of raw-profile reproduction or final cooling-bound reproduction is made.

### 2.2 Semi-Compton production

Croon Eq. (4.7) uses a Thomson/no-recoil approximation:
\[
\Gamma^{\rm Croon}_{\mu\gamma\to\mu Z'}(\omega)
=
\frac{8\pi\alpha_{\rm EM}\alpha_{Z'}}{3m_\mu^2}
n_\mu F_{\rm deg}
\frac{1}{e^{\omega/T}-1}
\sqrt{1-\frac{m_{Z'}^2}{\omega^2}}.
\]
Croon notes in its footnote that the massive-\(Z'\) matrix element differs technically from ordinary Compton scattering, but regards the approximation as adequate in the low-mass region dominating its constraint.

Blinov et al. 2026 Appendix B, Eqs. (B.13)--(B.19), instead starts from the full thermal phase-space integral and derives the non-recoil limit with the correct inverse/forward phase-space relation:
\[
\Gamma^{\rm prod}_{\mu\gamma\to\mu V}
=
\frac{1}{v_V}n_\mu F_{\rm deg}
\frac{2}{e^{\omega/T}-1}
\sigma(\mu\gamma\to\mu V),
\]
where
\[
\sigma(\mu\gamma\to\mu V)\simeq
\frac{8\pi\alpha_{\rm EM}\alpha_V}{3m_\mu^2}
\left(1+\frac{m_V^2}{2\omega^2}\right)v_V.
\]
The paper explains that the rate contains an additional \(1/v_V\) and a factor 2 relative to some earlier published expressions: the velocity factor follows from the unequal massive-vector and photon phase-space volumes, and the factor 2 accounts for the two photon polarizations because the thermal rate sums initial photon states whereas the cross-section convention averages them.

Consequently, Croon Eq. (4.7) is **not** the corrected formula to use for the production calculation. It remains a legacy comparison. Do not apply a guessed global factor to the final rate; implement B.13--B.19 from the phase-space integral and verify it numerically.

For the same (n_\mu F_{\rm deg}), coupling and Bose factor, direct substitution gives the equation-level ratio
\[
\frac{\Gamma_{\rm B16}}{\Gamma_{\rm Croon}}
=\frac{2\left(1+m_V^2/(2\omega^2)\right)}{v_V},
\qquad v_V=\sqrt{1-m_V^2/\omega^2}.
\]
Thus the ratio tends to 2 for (m_V/\omega\to0), and grows as threshold is approached. This is a controlled comparison of the two printed non-recoil formulae, not a universal correction factor to be applied to arbitrary kernels.

The full moving-muon/recoil kernel already developed in this repository is the next level beyond this non-recoil limit. It must reduce to the updated B.16 expression in the appropriate controlled limit, not necessarily to Croon Eq. (4.7).

Source: https://arxiv.org/abs/2511.09619, Appendix B, Eqs. (B.13)--(B.19).

### 2.2.1 Existing B.13-to-B.16 numerical cross-check

The repository already contains a direct pure-vector comparison between the exact moving-muon B.13 kernel and the B.14--B.16 non-recoil approximation. We re-ran its controlled-limit and independent-spinor regression gates in this benchmark workflow.

For the physical SFHo-18.8, \(t_{\rm pb}=1\) s profile and \(m_V=10\) MeV, the local energy-integrated vector Compton source gives:

| Radius | \(T\) | \(\mu_\mu\) | \(Q_{\rm B13}\) | \(Q_{\rm B16}\) | B13/B16 |
|---:|---:|---:|---:|---:|---:|
| 0 km | 19.265 MeV | 46.674 MeV | 13.6975 MeV\(^5\) | 28.5916 MeV\(^5\) | 0.4791 |
| 12.5 km | 23.882 MeV | 90.217 MeV | 381.1135 MeV\(^5\) | 889.2185 MeV\(^5\) | 0.4286 |

These are **not** acceptance failures of the exact B.13 kernel. They show that the non-relativistic/no-recoil B.14--B.16 approximation is not quantitatively reliable at these hot, muon-rich SFHo points. It overestimates the exact moving-muon vector source by factors of about 2.09 and 2.33, respectively. We must not calibrate B.13 to B.16 at these physical points.

The existing three-level audit further separates this difference without changing the underlying B.13 or B.16 calculations. Inserting the stationary-muon exact-recoil kernel between them gives

| Radius | \(Q_{\rm B13}/Q_{\rm stationary,exact}\) | \(Q_{\rm stationary,exact}/Q_{\rm B16}\) | Product \(Q_{\rm B13}/Q_{\rm B16}\) |
|---:|---:|---:|---:|
| 0 km | 0.842632 | 0.568544 | 0.479073 |
| 12.5 km | 0.799793 | 0.535881 | 0.428594 |

Thus the exact stationary-target Compton result is already 43.1% and 46.4% below B.14--B.16. Allowing the muon target to move in the full thermal distribution then lowers the rate by a further 15.7% and 20.0% relative to the stationary exact-recoil result. The first difference measures finite-energy/Compton corrections beyond the Thomson approximation with the same effective susceptibility; it should not be described as recoil alone. The second isolates the additional moving-muon thermal-kinematic effect within the project's matched comparison.

The explicit \(1+m_V^2/(2\omega^2)\) correction in B.14 changes the *energy-integrated* B.16 emissivity by only 2.23% at 0 km and 1.56% at 12.5 km. It therefore cannot explain the 52.1% and 57.1% total B.13/B.16 differences. The susceptibility quadrature is converged: changing its Gauss-Legendre order from 128 to 192 changes \(n_\mu F_{\rm deg}\) by less than \(5\times10^{-15}\) in both cases. The B.13/B.16 energy and angular integrations are also converged at the recorded orders.


The same B.13 implementation does pass its controlled common-limit test: \(T=0.5\) MeV, \(\mu_\mu=m_\mu+0.05\) MeV, \(m_V=0.05\) MeV and \(\omega=0.5\) MeV. In that non-relativistic, low-recoil regime, the transverse-mode ratios and total B.13/B.16 rate agree within the existing 5% acceptance tolerance. The B.13 detailed-balance residual at the physical points is below \(5.0\times10^{-15}\); the archived quadrature refinements change the integrated source by \(1.6\times10^{-4}\) or less.

The independent explicit-spinor audit separately verifies the B.13 Dirac-trace implementation, photon Ward identity, vector longitudinal Ward shift, and on-shell final muon. These checks validate the exact kernel; they do not make the B.16 approximation valid outside its controlled limit.

Reproduction records:
- \`finite_mixing/outputs/b13_b16_comparison_2026-11-12.json\`
- \`finite_mixing/test_b13_b16_comparison.py\`
- \`finite_mixing/test_b13_moving_muon_spinor_reference.py\`

The current benchmark workflow re-runs both regression suites. The B.13/B.16 comparison is vector-only and does not assign the vector B.14 approximation to the axial or UV-mixed current.



## 3. Transport prescriptions are separate benchmarks

Croon's luminosity calculation uses its own definitions of the production region, \(R_{\rm far}\), and absorption/escape treatment (Sec. 3, especially Eqs. (3.3)--(3.5)); it adopts \(R_{\rm far}=100\) km in its results. It should be implemented literally for a historical Fig. 2 reproduction.

### 3.1 C0 transport adapter: literal geometry and outer opacity

Croon Eqs. (3.2)--(3.4) define
\[
L_C(g)=\int_0^{R_\nu}4\pi r^2dr
\int_{m_V}^{\infty}d\omega\,
\frac{\omega^2\sqrt{\omega^2-m_V^2}}{2\pi^2}
\Gamma_{\rm prod}(\omega,r;g)e^{-\tau_C(\omega,r;g)},
\]
\[
\tau_C(\omega,r;g)=\int_r^{R_{\rm far}}dr'\,
\Gamma_{\rm abs}(\omega,r';g),
\qquad
\Gamma_{\rm prod}=e^{-\omega/T}\Gamma_{\rm abs}.
\]
The literal printed prescription is a **radial path integral**. Eq. (3.3) contains no explicit \(1/v_V\), and the luminosity has no angular escape average. These omissions must remain in the C0 reproduction; adding \(1/v_V\), a direction average, lapse factors, or the B.2 reduced-opacity prescription would define a different lane.

For the two Croon channels, detailed balance gives
\[
\Gamma_{\rm abs}^{\nu\bar\nu}
=e^{\omega/T}\Gamma_{\rm prod}^{\nu\bar\nu}
=\frac{\alpha_Vm_V^2}{3\omega}(1+f_B),
\]
\[
\Gamma_{\rm abs}^{\mu\gamma}
=e^{\omega/T}\Gamma_{\rm prod}^{\mu\gamma}
=\frac{8\pi\alpha_{\rm EM}\alpha_V}{3m_\mu^2}
n_\mu F_{\rm deg}\,v_V(1+f_B).
\]
Both channels are proportional to \(g^2\), so the optical depth can be tabulated per \(g^2\) and scaled without re-evaluating the local thermodynamics.

The current profile-B file has \(T(25\,{\rm km})=3.0337707\) MeV. Linear extrapolation of its last two nodes gives
\[
R_\nu(T=3\,{\rm MeV})=25.1512\ {\rm km}.
\]
This is consistent with Croon's stated approximate \(R_\nu\simeq25\) km. The current profile ends at 25 km, so the final 0.151 km inside the production boundary requires a short interpolation/extrapolation.

Croon uses \(R_{\rm far}=100\) km. The profile-B file does not extend to 100 km. This does **not** mean the outer opacity can be set to zero: the neutrino-pair inverse-decay opacity tends to the vacuum decay width as \(T\to0\). For \(r>R_\nu\), the C0 adapter must retain the analytic vacuum tail
\[
\tau_{\nu,{\rm out}}=
(R_{\rm far}-R_\nu)\frac{\alpha_Vm_V^2}{3\omega}
\]
in natural units, with an optional finite-temperature correction bracket. The semi-Compton opacity is negligible outside the muon-rich region once \(n_\mu F_{\rm deg}\) vanishes.

For \(m_V=10\) MeV, \(R_{\rm far}-R_\nu=74.8488\) km, and the literal Croon vacuum tail is
\[
\frac{\tau_{\nu,{\rm out}}}{g^2}
=
\begin{cases}
1.0062\times10^{17}, & \omega=10\ {\rm MeV},\\
8.3847\times10^{16}, & \omega=12\ {\rm MeV},\\
5.0308\times10^{16}, & \omega=20\ {\rm MeV},\\
2.0123\times10^{16}, & \omega=50\ {\rm MeV}.
\end{cases}
\]
At the threshold, taking the entire outer 74.85 km to remain at the maximum allowed \(T=3\) MeV would increase the vacuum decay opacity by only \(f_B(10\,{\rm MeV},3\,{\rm MeV})=3.70\%\); the correction is smaller at larger \(\omega\). Thus the unknown outer temperature profile can be bracketed between the vacuum tail and the \(T=3\) MeV upper envelope for this 10 MeV benchmark, rather than silently set to zero.

The input provenance is explicit: Croon cites the Bollig et al. SFHo-18.8, \(t_{\rm pb}=1\) s Garching profile. The current profile-B reconstruction is the Caputo-based public-figure reconstruction selected by the existing Bollig Fig. 4 cross-check; it is not the raw Garching file. Therefore any resulting curve must be labelled a **public-profile Croon-literal reproduction**, with the profile reconstruction uncertainty retained.



Blinov et al. 2026 use a revised ballistic treatment, including the vector-speed factor in optical depth, reduced absorption / stimulated emission, the \(R_{\max}=R_\nu\) boundary, and gravitational lapse/redshift effects. These are not optional numerical refinements to be mixed into the Croon lane; they define a different physical calculation.

Lai, Leung and Lin (2024), arXiv:2401.16023, study the trapping regime and argue for a luminosity plateau at large coupling with the attenuation boundary tied to the production boundary. This is a third independent transport prescription. Compare it as its own lane and record the boundary and opacity definitions.

References:

- Croon et al.: https://doi.org/10.1007/JHEP01(2021)107
- Blinov et al.: https://doi.org/10.1007/JHEP06(2026)155
- Lai et al.: https://doi.org/10.1103/PhysRevD.110.103023

## 4. Benchmark lanes and acceptance gates

| Lane | Local rates | Transport | Purpose |
|---|---|---|---|
| C0: Croon-literal | Croon Eqs. (4.6), (4.7) and stated approximations | Croon Sec. 3 literally | Historical reproduction only |
| C1: corrected vector rates | Blinov B.7--B.19, plus full B.13 kernel where needed | Fixed transport prescription explicitly selected | Test rate corrections independently |
| C2: modern vector SN | Blinov B.7--B.19 | Blinov ballistic / redshift / stimulated-emission treatment | Current vector reference |
| C3: trapping comparison | Lai et al. rates and conventions | Lai et al. plateau / boundary prescription | Independent high-opacity comparison |
| A0: axial model | Derive from this project's UV current and Goldstone sector | Reuse only validated transport machinery | Actual target physics |

Do not compare total luminosities until the following are matched or explicitly varied: mediator mass, coupling definition, number of neutrino flavors, neutrino chemical potentials, muon/antimuon convention, muon degeneracy factor, profile and post-bounce time, source radius, \(R_{\rm far}\), lapse/redshift, stimulated emission, opacity definition, polarization sum/average, and energy integration convention.

### Local-rate acceptance

- Croon-literal expressions reproduce the printed equations in their stated limit.
- Corrected neutrino rate has a separately derived Maxwell-Boltzmann limit; compare its normalization with Croon Eq. (4.6) only after matching flavor multiplicity, chiral-state counting, spin averaging, and coupling definitions.
- Corrected semi-Compton rate reproduces Blinov B.16 in the no-recoil limit.
- Full moving-muon B.13 kernel approaches the same controlled limit.
- Forward and inverse rates satisfy detailed balance pointwise, flavor by flavor and polarization by polarization.
- Explicit spinor traces and an independent invariant-amplitude implementation agree.
- No fitted normalization or opacity multiplier is allowed.

### Global-luminosity acceptance

- Reproduce the Croon Fig. 2 only in lane C0 with its own profile, radius, rates and transport assumptions. Any missing raw input or figure-digitization uncertainty must be reported.
- Recompute the same parameter points in lane C1/C2 without tuning to Croon.
- Compare lane C3 only after matching its benchmark profile and its production/attenuation boundaries.
- Report optically thin luminosity, source spectrum, optical depth, escape probability and total luminosity separately. A match in total luminosity alone is insufficient.
- Distinguish numerical quadrature uncertainty from profile, transport and model uncertainty.

## 5. Axial-vector transfer: no direct rate reuse

For the target interaction convention
\[
\mathcal L_{\mu A'}=
A'_\alpha\bar\mu\gamma^\alpha(g_V-g_A\gamma^5)\mu,
\]
the vector benchmark corresponds to \(g_A=0\). The target pure-axial limit has \(g_V=0\). The local matrix elements, polarization-resolved rates, inverse rates and longitudinal behavior must be recalculated.

In this project, do not assume that the neutrino coupling equals the charged-muon axial coupling. Extract the mass-basis couplings from the actual UV model (including finite right-handed mixing where retained). Keep the Goldstone/current Ward identity consistent with the same convention. The spin-0 ALP calculation in Croon is not a substitute for the spin-1 axial-vector calculation.

## 6. Immediate execution order

1. Freeze the Croon PDF version, equations, figure digitization, profile source, and all assumptions in a provenance manifest.
2. Build C0 analytic local-rate checks for Eqs. (4.6) and (4.7).
3. Build C1 corrected local-rate checks using Blinov B.7--B.19.
4. Compare C0 and C1 channel by channel before any luminosity integration.
5. Implement the Croon Sec. 3 luminosity prescription as an isolated transport adapter; do not modify the existing Blinov B.2 production baseline.
6. Reproduce the Croon Fig. 2 benchmark to the precision allowed by public inputs and digitization.
7. Only after C0/C1 are independently validated, proceed to the axial-vector A0 kernel and its Goldstone consistency checks.

## 7. Current status and non-claims

- This document is a literature/formula audit and execution specification.
- It does not claim that Croon Fig. 2 has been reproduced.
- It does not claim that the Croon rates are the corrected modern rates.
- It does not claim that Blinov 2026 is an exact ground truth; it is a more complete, independently checkable reference with its own profile and transport assumptions.
- It does not update any axial-vector luminosity or SN1987A exclusion.
- The existing B.13/B.16 calculations and the open PR #121 remain unchanged by this document.

