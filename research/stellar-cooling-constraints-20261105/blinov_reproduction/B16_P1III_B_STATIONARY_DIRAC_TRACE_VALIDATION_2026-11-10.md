# P1-IIIb: Stationary-target weak-current Dirac trace validated

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Result

An independent Dirac-trace implementation reproduces the Horowitz neutral-current stationary-nucleon differential kernel for \(\nu n,\bar\nu n,\nu p,\bar\nu p\). The validation covers \(E_\nu=50,100,150,255,500\) MeV and nine angles from \(\cos\theta=-0.999\) to \(+0.999\): 180 pointwise comparisons.

This closes the stationary-target tensor normalization and gamma-algebra test. It does **not** yet close the finite-temperature medium integral.

## 2. Conventions

Metric \(g^{\mu\nu}=(+---)\), \(q^\mu=p'^\mu-p^\mu=k^\mu-k'^\mu\), \(Q^2=-q^2\), and
\[
\Gamma_N^\mu=F_1^N\gamma^\mu+
i\frac{F_2^N}{2M_N}\sigma^{\mu\alpha}q_\alpha
-G_A^N\gamma^\mu\gamma^5,\quad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].
\]
The initial-spin-averaged hadronic tensor is
\[
H_N^{\mu\nu}=\frac12\operatorname{Tr}[
(\slashed p'+M_N)\Gamma_N^\mu
(\slashed p+M_N)\overline\Gamma_N^\nu].
\]
For neutrinos,
\[
L_{\mu\nu}^{(\nu)}=\operatorname{Tr}[
\slashed k'\gamma_\mu(1-\gamma^5)
\slashed k\gamma_\nu(1-\gamma^5)].
\]
For antineutrinos, \(k\) and \(k'\) are interchanged. The form factors and weak couplings are exactly those in the existing Horowitz 2002 baseline script.

## 3. Exact normalization bridge

The trace calculation gives
\[
L_{\mu\nu}H_N^{\mu\nu}
=32M_N^2E_\nu^2\,\mathcal B_H(E_\nu,\cos\theta),
\]
where \(\mathcal B_H\) is the Horowitz differential-cross-section bracket. Hence
\[
\frac{d\sigma}{d\Omega}
=\frac{G_F^2\eta^2}{128\pi^2M_N^2}L_{\mu\nu}H_N^{\mu\nu}
=\frac{G_F^2E_\nu^2\eta^2}{4\pi^2}\mathcal B_H.
\]
This fixes the normalization and the relative weak-magnetism/VA signs.

## 4. VV, AA and VA decomposition

The hadronic tensor was split into \(H_{VV}+H_{AA}+H_{VA}\), with \(H_{VV}\) containing both Dirac and Pauli vector pieces. At \(E_\nu=500\) MeV, neutron target, \(\cos\theta=-0.5\):
| Channel | normalized VV | normalized AA | normalized VA |
|---|---:|---:|---:|
| \(\nu n\) | 0.0860582 | 0.2110459 | +0.2518856 |
| \(\bar\nu n\) | 0.0860582 | 0.2110459 | -0.2518856 |

The VA sign reversal is obtained by swapping the incoming and outgoing momenta in the antineutrino leptonic trace.

## 5. Numerical validation

| Check | Maximum residual |
|---|---:|
| Pointwise \(d\sigma/d\Omega\) vs Horowitz | \(3.11\times10^{-15}\) |
| Normalized trace vs Horowitz bracket | \(3.11\times10^{-15}\) |
| Vector Ward identity \(q_\mu H_{VV}^{\mu\nu}=0\) | \(1.77\times10^{-14}\) |
| Hadronic-tensor Hermiticity | \(3.66\times10^{-17}\) |
| VV+AA+VA tensor decomposition | \(1.72\times10^{-15}\) |
| Separate VV/AA/VA bracket components | \(1.11\times10^{-12}\) |
| Integrated moments: 32/64/128 vs 256 angular nodes | \(1.67\times10^{-14}\) |

Selected neutron moments, in units of \(10^{-40}\,\mathrm{cm}^2\):
| \(E_\nu\) | Channel | \(\sigma_{\rm tot}\) | \(\sigma_{\rm tr}\) | \(\sigma_{\rm mom}\) | \(\sigma_{\rm loss}\) |
|---:|---|---:|---:|---:|---:|
| 100 MeV | \(\nu n\) | 2.11154 | 2.07412 | 2.01639 | 0.193964 |
| 100 MeV | \(\bar\nu n\) | 1.34710 | 1.12701 | 1.10608 | 0.106398 |
| 500 MeV | \(\nu n\) | 16.9127 | 10.2930 | 10.4713 | 3.63698 |
| 500 MeV | \(\bar\nu n\) | 6.87047 | 2.09511 | 2.43772 | 0.846687 |

## 6. Correction to the medium-tensor angular reduction

A factor-of-two issue was found in the preliminary P1-IIIb specification. Starting from
\[
W_N^{\mu\nu}=2\pi\int\frac{d^3p}{(2\pi)^3}
\frac{f(1-f')}{4E_pE_{p'}}
\delta(q_0+E_p-E_{p'})\,2H_N^{\mu\nu},
\]
where \(H=\tfrac12\mathrm{Tr}[\cdots]\), angular integration gives
\[
W_N^{\mu\nu}=\frac{1}{4\pi q}
\int_{p_{\min}}^\infty dp\,\frac{p}{E_p}f(1-f')\,
\overline H_N^{\mu\nu},
\quad
\overline H=\frac{1}{2\pi}\int d\phi\,H.
\]
The coefficient is \(1/(4\pi q)\), not \(1/(8\pi q)\), when the explicit spin degeneracy 2 is retained. The specification has been corrected in this commit.

## 7. Scope and next task

Completed: stationary-target Dirac traces; neutrino/antineutrino contractions; weak-magnetism and form-factor convention; differential and integrated Horowitz validation; vector Ward identity; Hermiticity; corrected medium-tensor angular normalization.

Not completed: moving initial nucleons, finite-temperature Pauli blocking with the full weak tensor, EOS-consistent matter composition, RPA/NN correlations, radial optical depths, or B.2 escape probabilities.

Next implement the moving-nucleon tensor with the azimuthal average relative to the neutrino scattering plane. Its dilute/cold limit must recover stationary-target \(d\sigma/d\Omega\) after division by target density before finite-temperature benchmarks are used. No B.2, pure-vector Fig. 7, or axial-vector constraint is changed.
