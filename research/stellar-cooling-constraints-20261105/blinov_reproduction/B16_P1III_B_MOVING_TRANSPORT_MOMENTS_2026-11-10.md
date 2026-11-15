# P1-IIIb: Energy/angle-integrated transport and energy-transfer moments

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Benchmark

The moving-nucleon collision kernel has now been integrated over both outgoing neutrino energy and scattering angle for one controlled benchmark:
\[
E_\nu=100\ {\rm MeV},\quad T=3.03\ {\rm MeV},\quad
Y_p=0.10,\quad n_B/n_0=10^{-3},
\]
on a neutron target with an incident neutrino.

The angular integral uses
\[
s=\sqrt{\frac{1-\cos\theta}{2}},\qquad
\cos\theta=1-2s^2,\qquad d\cos\theta=4s\,ds.
\]
This transformation clusters quadrature nodes toward the forward direction, where a uniform \(\cos\theta\) grid converges more slowly.

## 2. Moment definitions

The medium moments are formed from the full outgoing-energy distribution:
\[
\sigma_{\rm tot}=\int d\Omega\,\frac{1}{n_n}\int dE'\,\frac{d\Gamma}{dE'd\Omega},
\]
\[
\sigma_{\rm tr}=\int d\Omega\,(1-\cos\theta)\,
\frac{1}{n_n}\int dE'\,\frac{d\Gamma}{dE'd\Omega},
\]
\[
\sigma_{\rm mom}=\int d\Omega\,\frac{1}{n_n}\int dE'\,
\left(1-\frac{E'}{E}\cos\theta\right)\frac{d\Gamma}{dE'd\Omega},
\]
\[
\sigma_{\rm loss}=\int d\Omega\,\frac{1}{n_n}\int dE'\,
\left(1-\frac{E'}{E}\right)\frac{d\Gamma}{dE'd\Omega}.
\]
The last expression is a **net** energy-transfer moment; it retains upscattering contributions rather than imposing stationary-target recoil kinematics.

## 3. Numerical result

All cross sections below are in units of \(10^{-40}\,\mathrm{cm}^2\).

| Moment | Moving finite-\(T\) kernel | Stationary Horowitz | Ratio |
|---|---:|---:|---:|
| Total | 2.111552 | 2.111540 | 1.000006 |
| Angular transport | 2.110954 | 2.074116 | 1.017761 |
| Momentum transfer | 2.060508 | 2.016387 | 1.021881 |
| Net energy loss | 0.165173 | 0.193964 | 0.851563 |

At this benchmark, the total scattering cross section is essentially unchanged, while the angular-transport and momentum-transfer moments increase by about 1.8% and 2.2%. The net energy-loss moment decreases by about 14.8%.

This is the key physical distinction: matching the total scattering rate does not guarantee that the energy-transfer kernel is reproduced. Thermal nucleon motion redistributes the outgoing neutrino energy, including upscattering, and therefore changes the net energy-exchange moment.

## 4. Angular convergence

The two transformed-angle resolutions give:

| \(N_s\) | Total ratio | Transport ratio | Momentum ratio | Energy-loss ratio |
|---:|---:|---:|---:|---:|
| 8 | 0.999968 | 1.017727 | 1.021838 | 0.851477 |
| 16 | 1.000006 | 1.017761 | 1.021881 | 0.851563 |

The changes are \(3.8\times10^{-5}\), \(3.3\times10^{-5}\), \(4.3\times10^{-5}\), and \(8.6\times10^{-5}\), respectively. Both calculations use 48 outgoing-energy nodes, 48 initial-momentum nodes, 16 azimuthal nodes, and a 60 MeV outgoing-energy half-window.

## 5. Interpretation and scope

This benchmark demonstrates that the moving-nucleon tensor can be integrated into local transport and energy-transfer moments while recovering the cold/dilute Horowitz limit.

It is not yet a supernova cooling result:
- the composition and density are illustrative ideal-gas inputs, not a same-snapshot SFHo-18.8 profile;
- no EOS mean fields, effective masses, RPA, or NN correlations are included;
- no radial optical depth, multiple-scattering transport, or escape probability has been calculated.

No B.2 opacity, pure-vector Fig. 7 curve, or axial-vector cooling constraint is modified.

## 6. Next step (updated 2026-11-15)

The five-energy grid and all four neutrino/antineutrino neutron/proton channels are now covered by P1-IIIc. The Caputo figure-derived density/composition profile and the SFHo-EOS-mapped profile are also available as separate 301-point artifacts. The present moment calculation, however, remains a single ideal-gas benchmark at \(E_\nu=100\) MeV, \(T=3.03\) MeV, \(Y_p=0.10\), and \(n_B/n_0=10^{-3}\).

The next calculation is a radial evaluation using the same EOS-mapped \(n_B(r),Y_p(r),T(r),m_N^*(r)\), and vector mean fields. Until then, the moments are local kernel diagnostics, not a supernova opacity or energy sphere.


## 7. Independent review qualification (2026-11-15)

The transformed-angle mapping \(s=\sqrt{(1-\cos\theta)/2}\) has \(|d\cos\theta|=4s\,ds\), so the stated Jacobian and forward-node clustering are correct. The four weights also have distinct physical meanings: \(1\), \(1-\cos\theta\), \(1-(E'/E)\cos\theta\), and \(1-E'/E\). In particular, the last is a signed net energy-transfer moment and correctly retains upscattering contributions.

The archived 8-versus-16 angular comparison changes the four ratios by \(3.8\times10^{-5}\), \(3.3\times10^{-5}\), \(4.3\times10^{-5}\), and \(8.6\times10^{-5}\). This is a useful angular convergence check at the selected benchmark, not a global error bound over energy, density, composition, or the full outgoing-energy support. The later P1-IIIc grid expands the energy/channel coverage but still fixes one thermodynamic point.

The JSON output matches the checked-in moment script's compact two-resolution result. No dedicated unittest or workflow currently exercises this P1-IIIb moments driver; its convergence comparison is an in-script diagnostic.

**Review disposition: PASS_WITH_NOTES.** No radial opacity, B.2 baseline, Fig. 7 curve, or axial-vector constraint is changed.
