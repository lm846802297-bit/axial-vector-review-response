# P1-IIIc: Moving-nucleon transport moments across the incident-energy grid

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Scope and status

This stage extends the P1-IIIb finite-temperature moving-nucleon collision kernel from a single \(E_\nu=100\) MeV integrated benchmark to
\[
E_\nu=50,\ 100,\ 150,\ 255,\ 500\ {\rm MeV},
\]
for \(\nu n,\bar\nu n,\nu p,\bar\nu p\).

The thermodynamic point is held fixed:
\[
T=3.03\ {\rm MeV},\qquad Y_p=0.10,\qquad n_B/n_0=10^{-3}.
\]
This is an illustrative ideal-gas point, not a reconstructed SFHo-18.8 radial snapshot.

The calculation integrates the moving-nucleon differential collision kernel over outgoing neutrino energy and scattering angle. It reports four moments:
\[
\sigma_{\rm tot},\quad
\sigma_{\rm tr}=\int d\Omega\,(1-\cos\theta)\frac{d\sigma}{d\Omega},
\]
\[
\sigma_{\rm mom}=\int d\Omega dE'\left(1-\frac{E'}{E}\cos\theta\right)
\frac{1}{n_N}\frac{d\Gamma}{dE'd\Omega},
\]
\[
\sigma_{\rm loss}=\int d\Omega dE'\left(1-\frac{E'}{E}\right)
\frac{1}{n_N}\frac{d\Gamma}{dE'd\Omega}.
\]
The last quantity is the **net** energy-transfer moment: upscattering events contribute negatively.

## 2. Energy-window treatment

A fixed \(E'\) half-window is inefficient: the thermal broadening scales approximately as
\[
\Delta E'\sim q\sqrt{T/M_N}.
\]
It over-resolves the forward region and can under-resolve the recoil peak when a wide interval is integrated with a fixed Gauss order.

We therefore use an angle-dependent window centered on the stationary recoil energy:
\[
E'_0=\frac{E}{1+(E/M_N)(1-\cos\theta)},\qquad
\Delta E'=\max\left[0.5\ {\rm MeV},\ 7q\sqrt{T/M_N}\right],
\]
with the lower endpoint clipped at \(E'=0\). The momentum transfer \(q\) is evaluated at \(E'_0\).

Baseline quadrature:
- transformed angle: 8 Gauss-Legendre nodes, \(s=\sqrt{(1-\cos\theta)/2}\);
- outgoing energy: 24 nodes;
- initial nucleon momentum: 20 nodes;
- azimuth: 6 nodes.

## 3. Results

All cross sections are in units of \(10^{-40}\ {\rm cm}^2\). Ratios are moving finite-\(T\) divided by stationary Horowitz.

| \(E_\nu\) (MeV) | Channel | Total | Angular transport | Momentum transfer | Net energy loss |
|---:|:---:|---:|---:|---:|---:|
| 50 | \(\nu n\) | 1.003410 | 1.010646 | 1.016127 | 0.665595 |
| 50 | \(\bar\nu n\) | 1.000059 | 1.006801 | 1.010982 | 0.681242 |
| 50 | \(\nu p\) | 1.016400 | 1.021522 | 1.027822 | 0.668364 |
| 50 | \(\bar\nu p\) | 1.013591 | 1.018155 | 1.023588 | 0.681275 |
| 100 | \(\nu n\) | 1.009804 | 1.017894 | 1.022034 | 0.851711 |
| 100 | \(\bar\nu n\) | 1.004084 | 1.011737 | 1.013773 | 0.860967 |
| 100 | \(\nu p\) | 1.015118 | 1.019854 | 1.024550 | 0.853838 |
| 100 | \(\bar\nu p\) | 1.010871 | 1.014655 | 1.018001 | 0.861560 |
| 150 | \(\nu n\) | 1.010780 | 1.017565 | 1.020465 | 0.911853 |
| 150 | \(\bar\nu n\) | 1.004705 | 1.011213 | 1.011553 | 0.916911 |
| 150 | \(\nu p\) | 1.012964 | 1.016983 | 1.020300 | 0.913108 |
| 150 | \(\bar\nu p\) | 1.008446 | 1.011247 | 1.012976 | 0.917409 |
| 255 | \(\nu n\) | 1.007777 | 1.011935 | 1.012779 | 0.956655 |
| 255 | \(\bar\nu n\) | 1.003784 | 1.008133 | 1.006029 | 0.957829 |
| 255 | \(\nu p\) | 1.008357 | 1.010859 | 1.012017 | 0.957061 |
| 255 | \(\bar\nu p\) | 1.005239 | 1.006364 | 1.005803 | 0.958050 |
| 500 | \(\nu n\) | 1.002130 | 1.003118 | 1.001628 | 0.980235 |
| 500 | \(\bar\nu n\) | 1.002818 | 1.006357 | 1.001487 | 0.981220 |
| 500 | \(\nu p\) | 1.002285 | 1.002344 | 1.001085 | 0.980203 |
| 500 | \(\bar\nu p\) | 1.003299 | 1.003133 | 1.000041 | 0.980859 |

## 4. Physical interpretation

### 4.1 Total scattering is close to the stationary result

Across this benchmark grid, the total cross-section ratios remain within approximately \(0.1\%\)–\(1.7\%\) of unity. The angular and momentum-transfer moments differ by a few percent or less.

This is consistent with the P1-IIIb conclusion: a stationary-target approximation can describe the total scattering rate rather well at this dilute outer-layer point.

### 4.2 Net energy transfer is much more sensitive at low incident energy

The net energy-loss ratios show a clear energy dependence:

| \(E_\nu\) (MeV) | \(\nu n\) | \(\bar\nu n\) | \(\nu p\) | \(\bar\nu p\) |
|---:|---:|---:|---:|---:|
| 50 | 0.6656 | 0.6812 | 0.6684 | 0.6813 |
| 100 | 0.8517 | 0.8610 | 0.8538 | 0.8616 |
| 150 | 0.9119 | 0.9169 | 0.9131 | 0.9174 |
| 255 | 0.9567 | 0.9578 | 0.9571 | 0.9581 |
| 500 | 0.9802 | 0.9812 | 0.9802 | 0.9809 |

At 50 MeV the net energy-loss moment is about 32%–33% below the stationary-target result. At 100 MeV the reduction is about 14%; by 500 MeV it is about 2%.

This trend is physically expected: at lower incident energy the thermal motion of nucleons is more important relative to stationary-target recoil, so upscattering offsets a larger fraction of the recoil energy loss. As \(E_\nu\) increases, the recoil contribution dominates and the stationary-target energy-transfer moment becomes a better approximation.

The result does **not** mean the total opacity changes by 30%. It is specifically a net energy-exchange moment.

## 5. Numerical checks

Selected higher-order checks use \((N_s,N_{E'},N_p,N_\phi)=(12,32,24,8)\), compared with the baseline \((8,24,20,6)\). The largest relative difference among the checked four-moment ratios is
\[
2.49\times10^{-4}.
\]
The checks include neutron-neutrino points at all five incident energies and proton-antineutrino points at 50, 100, 255, and 500 MeV, plus the 500 MeV antineutrino-neutron point. This is a spot-check, not a claim that every grid point has been recomputed at the highest order.

The outgoing-energy window was varied from \(5q\sqrt{T/M}\) to \(9q\sqrt{T/M}\) for neutron-neutrino points at 50, 100, 255, and 500 MeV. The largest relative change among the four moments is
\[
1.45\times10^{-4}.
\]

The stationary-target Dirac-trace validation already archived in P1-IIIb gives:
- pointwise Horowitz differential-kernel residual \(3.11\times10^{-15}\);
- Ward residual \(1.77\times10^{-14}\);
- maximum VV/AA/VA component residual \(1.11\times10^{-12}\);
- integrated-moment quadrature residual \(1.67\times10^{-14}\).

## 6. Scope boundary

Established:
1. The P1-IIIb moving-nucleon collision kernel has been integrated over outgoing energy and scattering angle on the five-energy grid.
2. The four channels \(\nu n,\bar\nu n,\nu p,\bar\nu p\) are included.
3. Total, angular-transport, momentum-transfer, and net energy-loss moments are separately recorded.
4. The energy-transfer correction is strongly energy dependent and cannot be inferred from the total cross section alone.

Not established:
- EOS-consistent \(Y_p(r)\), \(m_N^*(r)\), or mean fields;
- RPA, NN correlations, or in-medium vertex corrections;
- a complete neutrino Boltzmann transport solution;
- a radial optical depth, energy sphere, or final escape probability;
- a corrected B.2 luminosity or SN cooling bound.

The fixed \(Y_p=0.10\), \(T=3.03\) MeV, \(n_B/n_0=10^{-3}\) point is only a controlled benchmark. No mixed stellar profiles are used.

## 7. Next stage

P1-IIId should now reconstruct co-located \(n_B(r)\), \(Y_p(r)\), and \(T(r)\) from a single public stellar snapshot, with explicit provenance and digitization uncertainties. Only after that should this local kernel be evaluated radially.

The original Blinov B.2 convention, pure-vector Fig. 7 benchmark, and axial cooling curves remain untouched. No use of \(e^{-\tau_{\rm therm}}\) as a final escape probability is permitted.
