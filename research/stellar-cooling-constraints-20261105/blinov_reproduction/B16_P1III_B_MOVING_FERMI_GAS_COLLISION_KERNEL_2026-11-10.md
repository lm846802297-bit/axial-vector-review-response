# P1-IIIb: Moving-nucleon finite-temperature weak collision kernel

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Result

The stationary-target Dirac trace has now been extended to a moving initial nucleon. The calculation retains the exact relativistic nucleon dispersion, initial Fermi occupation, final-state Pauli blocking, recoil, weak magnetism, Horowitz form factors, and the full azimuthal dependence of the moving nucleon relative to the neutrino scattering plane.

The energy-conserving delta function is integrated analytically over the initial nucleon polar angle. The remaining integrals are over initial momentum magnitude, azimuth, and outgoing neutrino energy.

This is a local free-Fermi-gas collision-kernel benchmark. It is **not** a total opacity, a radial transport solution, or a revised B.2 result.

## 2. Collision-rate expression and normalization

With \(H_N^{\mu\nu}=\tfrac12\mathrm{Tr}[(\slashed p'+M)\Gamma^\mu(\slashed p+M)\bar\Gamma^\nu]\), the invariant rate is
\[
\frac{d\Gamma_N}{dE'\,d\Omega'}=
\frac{G_F^2E'}{64\pi^2E}
\int\frac{d^3p}{(2\pi)^3}
\frac{f_i(1-f_f)}{E_pE_{p'}}
\delta(E+E_p-E'-E_{p'})
L_{\mu\nu}H_N^{\mu\nu}.
\]
Here \(f_i\) is the occupation per nucleon spin state. The spin sum is included exactly once: the factor of two from the occupied nucleon spin states combines with the \(G_F^2/2\) in the squared weak amplitude.

Using
\[
\left|\frac{\partial(E_p-E_{p'})}{\partial\cos\theta_{pq}}\right|
=\frac{pq}{E_{p'}},
\]
and defining the azimuthal average relative to the scattering plane, gives
\[
\boxed{
\frac{d\Gamma_N}{dE'\,d\Omega'}=
\frac{G_F^2E'}{256\pi^4Eq}
\int_{p_{\min}}^\infty dp\,\frac{p}{E_p}
f_i(1-f_f)\overline{L_{\mu\nu}H_N^{\mu\nu}}
}.
\]
The numerical normalization is checked against the stationary-target Horowitz differential cross section after integrating over \(E'\) and dividing by the species number density.

## 3. Cold/dilute limit

Benchmark:
\[
E_\nu=100\ {\rm MeV},\quad \cos\theta=-0.5,\quad
T=10^{-3}\ {\rm MeV},\quad n_B/n_0=10^{-10},\quad Y_p=0.10.
\]

| Channel | \(\sigma_{\rm medium}/\sigma_{\rm Horowitz}\) |
|---|---:|
| \(\nu n\) | 1.00000804 |
| \(\bar\nu n\) | 1.00000623 |
| \(\nu p\) | 1.00000739 |
| \(\bar\nu p\) | 1.00000562 |

Thus the moving-nucleon collision rate recovers the stationary-target result to better than \(8.1\times10^{-6}\) in all four channels at this low-temperature benchmark.

## 4. Finite-temperature dilute benchmark

Use the illustrative ideal-gas point
\[
T=3.03\ {\rm MeV},\quad Y_p=0.10,\quad
n_B/n_0=10^{-3},\quad E_\nu=100\ {\rm MeV},\quad \cos\theta=-0.5.
\]
The outgoing-energy integration uses a \(\pm60\) MeV interval around the stationary-target recoil energy.

| Channel | \(\sigma_{\rm medium}/\sigma_{\rm stationary}\) |
|---|---:|
| \(\nu n\) | 1.022393 |
| \(\bar\nu n\) | 1.016885 |
| \(\nu p\) | 1.022288 |
| \(\bar\nu p\) | 1.016844 |

At this low density, the final-state blocking factor for \(\nu n\) is \(0.997765\); most of the approximately 2% shift is therefore due to thermal motion and the resulting energy/angle redistribution, rather than Pauli suppression.

## 5. Density dependence of Pauli blocking

For the same \(T,E_\nu,\cos\theta,Y_p\), the neutron-neutrino benchmark gives:

| \(n_B/n_0\) | Ratio without final blocking | Ratio with final blocking | Blocking factor |
|---:|---:|---:|---:|
| \(10^{-3}\) | 1.024683 | 1.022393 | 0.997765 |
| \(10^{-2}\) | 1.026872 | 1.001255 | 0.975053 |
| \(10^{-1}\) | 1.046794 | 0.728305 | 0.695748 |

This demonstrates that final-state blocking is strongly density dependent. It cannot be represented by a universal multiplicative opacity correction. The \(10^{-1}n_0\) row is an illustrative ideal-gas stress test, not a claim about the density at a particular SFHo-18.8 radius.

## 6. Numerical convergence

For the dilute \(\nu n\) benchmark:
| \((N_{E'},N_p,N_\phi)\) | Ratio |
|---:|---:|
| (32,32,12) | 1.022392747812 |
| (48,48,16) | 1.022392747626 |
| (64,64,20) | 1.022392747627 |

Varying the outgoing-energy half-window:
| Half-window | Ratio |
|---:|---:|
| 40 MeV | 1.022356547 |
| 50 MeV | 1.022392039 |
| 60 MeV | 1.022392748 |

A separate high-density check at \(n_B=0.1n_0\) gives 0.72830547, 0.72830567, and 0.72830567 for quadrature orders \((48,16,48)\), \((72,24,72)\), and \((96,32,96)\), respectively. Increasing the outgoing-energy half-window to 75 MeV gives 0.72830566.

## 7. Scope boundary

Established:
- full moving-nucleon Dirac trace with exact energy-momentum conservation;
- azimuthal dependence relative to the scattering plane;
- initial Fermi motion and final-state nucleon Pauli blocking;
- cold/dilute recovery of Horowitz in all four channels;
- density-dependent blocking and quadrature convergence.

Not established:
- EOS-consistent \(Y_p(r)\), \(m_N^*(r)\), or mean fields;
- RPA or NN correlations;
- a complete angular/energy grid over the full supernova spectrum;
- radial optical depths, multiple-scattering redistribution, or a Boltzmann solution.

The \(Y_p=0.10\) and density points are illustrative, not extracted from SFHo-18.8. No B.2 opacity, pure-vector Fig. 7 comparison, or axial-vector cooling limit is modified.

## 8. Next step

Expand the moving-nucleon kernel over the relevant \(E_\nu,E',\cos\theta\) domain and compare integrated transport and energy-transfer moments with the stationary-target kernel. Then replace the illustrative composition with co-located \(n_B(r),Y_p(r),T(r)\) from one consistent stellar snapshot. Only after those steps should the local kernel be connected to radial B.2 propagation.
