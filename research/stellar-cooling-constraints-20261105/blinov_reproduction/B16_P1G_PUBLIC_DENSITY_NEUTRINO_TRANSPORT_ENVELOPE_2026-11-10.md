# P1-G: Public-density transport envelope for high-energy vector-decay neutrinos

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, pure vector, \(210\leq\omega\leq510\) MeV  
Profile: SFHo-18.8, \(t_{\rm pb}=1\) s  
P1-C vector energy nodes: 10 nodes from 217.292 to 486.861 MeV

## 1. Purpose

P1-F established that the fixed \(R_{\max}=R_\nu\simeq25\) km boundary is not automatically an energy-resolved energy-loss boundary for the high-energy \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) daughters. The same-snapshot raw Garching neutrino transport arrays are not available through the public archive.

A useful intermediate check is nevertheless possible: Caputo, Raffelt, and Vitagliano (2022), Fig. 1, publish the baryon-density profile of the *same* Garching SFHo-18.8 model at \(t_{\rm pb}=1\) s. The plot ends at 20 km. This audit reads off its outer density scale and combines it with the published approximate neutrino-nucleon mean free path to estimate the radial transport optical depth beyond 20 km.

This is explicitly a figure-level transport estimate. It is not a reconstruction of the original Boltzmann solution and does not calculate the heavy-flavor energy sphere.

## 2. Figure-level density tail

The bottom panel of Caputo et al. Fig. 1 gives \(n_B/n_0\), with \(n_0=0.181\ {\rm fm}^{-3}\), for the same SFHo-18.8, 1 s snapshot used in the present benchmark.

The blue \(n_B\) curve gives approximately
\[
\frac{n_B(20\,{\rm km})}{n_0}\simeq10^{-3}.
\]
A log-linear read-off over 18--20 km gives an outer density scale height of approximately
\[
H_\rho\simeq1.2\ {\rm km}.
\]
To avoid treating a rasterized plot as raw data, the diagnostic also varies
\[
n_{B,20}/n_0\in[0.5,2.0]\times10^{-3},\qquad
H_\rho\in[0.9,1.3]\ {\rm km}.
\]
These are deliberately broad figure-read-off stresses, not statistical confidence intervals.

For \(r\geq20\) km the tail is approximated by
\[
n_B(r)=n_{B,20}\exp[-(r-20\,{\rm km})/H_\rho].
\]

## 3. Neutrino-nucleon transport optical depth

Raffelt, Janka, and Fiorillo (2025) quote the representative mean free path
\[
\lambda_{\nu N}\simeq
25\,{\rm cm}\,
\frac{n_0}{n_B}
\left(\frac{100\,{\rm MeV}}{E_\nu}\right)^2
\]
at nuclear density \(n_0\). Applying this approximate scaling to the exponential tail gives
\[
\tau_{\nu N}(E_\nu,r)=
\frac{1}{25\,{\rm cm}}
\left(\frac{E_\nu}{100\,{\rm MeV}}\right)^2
\frac{n_{B,20}}{n_0}
H_\rho e^{-(r-20\,{\rm km})/H_\rho},
\]
where \(H_\rho\) is converted to centimetres in the numerical evaluation.

For the central figure read-off \(n_{B,20}/n_0=10^{-3}\), \(H_\rho=1.2\) km:

| Daughter energy | \(\tau_{\nu N}(25\,{\rm km})\) | Radius where radial \(\tau_{\nu N}=2/3\) |
|---:|---:|---:|
| 100 MeV | 0.074 | 22.37 km |
| 150 MeV | 0.167 | 23.34 km |
| 255 MeV | 0.484 | 24.62 km |
| 500 MeV | 1.860 | 26.23 km |

The 100--255 MeV pair-mean daughter energies therefore have a transport radius around 22--25 km in the central tail model. The upper daughter-energy tail can remain transport-thick somewhat farther out.

Across the broad low/central/high figure-read-off stresses, the estimated \(\tau=2/3\) radii are:
- \(E_\nu=100\) MeV: 20.89--23.57 km;
- \(E_\nu=150\) MeV: 21.62--24.63 km;
- \(E_\nu=255\) MeV: 22.58--26.01 km;
- \(E_\nu=500\) MeV: 23.79--27.76 km.

This supports 25 km as a plausible effective boundary for much of the daughter energy, while allowing the highest-energy tail to remain transport-thick beyond 25 km for a denser/slower outer tail. It does not support treating 30 km as a uniquely determined neutrinosphere.

## 4. Energy-weighted daughter-pair escape proxy

A single daughter energy is insufficient because the vector is highly boosted. For each polarization,
\[
P^E_{{\rm pair},h}(\omega,r)=
\frac{1}{\omega}\int_{-1}^{1}dz\,W_h(z)
\left[
E_1e^{-\tau_{\nu N}(E_1,r)}
+E_2e^{-\tau_{\nu N}(E_2,r)}
\right],
\]
with
\[
E_{1,2}=\frac{\omega}{2}(1\pm\beta z),\qquad
\beta=\sqrt{1-m_V^2/\omega^2}.
\]
The equal-polarization reference is the average over \(h=L,+,-\), with the P1-C weights
\[
W_L=\frac34(1-z^2),\qquad W_\pm=\frac38(1\pm z)^2.
\]

This is a *transport-only* pair-energy survival proxy. It assumes that a neutrino-nucleon scattering removes the daughter from the unscattered beam. It does not equal the energy-sphere escape probability: scattering can be partly elastic, while pair emission/absorption and other energy-changing processes are not included. The actual production polarization density matrix is also not replaced by equal weights in the physical model; equal weights are used here only as a transparent reference.

For the ten P1-C vector-energy nodes, the central-tail equal-polarization pair-energy survival range is:

| Radius | Minimum over the 10 vector-energy nodes | Maximum |
|---:|---:|---:|
| 25 km | 0.470 | 0.843 |
| 26 km | 0.698 | 0.927 |
| 27.5 km | 0.898 | 0.978 |
| 30 km | 0.986 | 0.997 |

For representative vector energies, the central-tail result is:

| \(\omega\) | \(P^E_{\rm pair}(25\,{\rm km})\) | \(P^E_{\rm pair}(27.5\,{\rm km})\) | \(P^E_{\rm pair}(30\,{\rm km})\) |
|---:|---:|---:|---:|
| 210 MeV | 0.853 | 0.980 | 0.998 |
| 300 MeV | 0.729 | 0.960 | 0.995 |
| 510 MeV | 0.442 | 0.889 | 0.985 |

The broad density-tail stress is substantial. At 25 km, the minimum-to-maximum pair-energy survival across the ten vector nodes is:
- low-density/short-scale-height tail: 0.922--0.984;
- central tail: 0.470--0.843;
- high-density/long-scale-height tail: 0.189--0.620.

Thus the public figure alone does not determine the high-energy daughter escape fraction precisely.

## 5. Interpretation of the P1-D 25--30 km scan

The P1-D outward scan adds the full vacuum-limit vector-to-neutrino opacity outside 25 km. In energy-loss language, that is the sharp-boundary assumption that the daughter pair is fully reprocessed throughout the added shell.

The transport-only estimate instead gives a smooth transition. In the central tail, the 210--510 MeV vector nodes have \(P^E_{\rm pair}\simeq0.47\)--0.84 at 25 km, 0.90--0.98 at 27.5 km, and 0.986--0.997 at 30 km. The fraction of decay energy reprocessed, \(1-P^E_{\rm pair}\), therefore falls continuously through the 25--30 km region.

Consequently:
1. \(R_{\max}=25\) km is a plausible fixed effective approximation, but it may underrepresent reprocessing for the highest-energy daughter tail.
2. The full P1-D 30 km opacity extension is an extreme sharp-boundary diagnostic; it should not be interpreted as the physical smooth transport result.
3. The band-only proxy that nearly matches Fig. 7 at 30 km is not evidence that the correct boundary is 30 km.
4. The physical correction, if any, should be a smooth energy- and polarization-dependent daughter-pair reprocessing probability.

The transport sphere is not the heavy-flavor energy sphere. The latter is associated with the last energy-changing interaction and generally requires pair-process information. This audit therefore cannot select a corrected \(R_{\max}\).

## 6. What this adds to the strong-endpoint diagnosis

The 25 km boundary is not an arbitrary numerical cutoff: it is near the central-tail transport radius for 255 MeV daughters, while the highest-energy daughters can remain transport-thick somewhat farther out. This gives a physical explanation for why the boundary may have an energy-dependent transition rather than a universal sharp surface.

However, the uncertainty envelope does not validate the full 30 km extension, and it does not determine the actual energy sphere. The strong-endpoint \(+92\%\) Fig. 7 discrepancy remains unresolved. No B.2 opacity, \(R_{\max}\), source, profile, or axial-vector curve is changed.

## 7. Required inputs for a genuine energy-sphere calculation

A physical \(P^E_{\rm pair}(\omega,r)\) needs, for the same snapshot:
- baryon density and composition beyond 20 km;
- \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) energy-dependent collision kernels;
- angular moments/distribution functions;
- the energy-changing pair-process opacity needed to distinguish energy and transport spheres;
- the vector production polarization weights over the actual source phase space.

The public Fig. 1 supplies only the density read-off to 20 km. The present exponential tail is therefore a controlled sensitivity model, not an alternative stellar profile.

## 8. Reproducibility and decision

- Script: \`audit_b16_public_density_neutrino_transport_envelope.js\`
- Machine-readable output: \`outputs/b16_public_density_neutrino_transport_envelope_10mev_2026-11-10.json\`
- Input energy nodes: \`outputs/b16_p1c_global_polarization_b14_split_10mev_2026-11-10.json\`

**Decision:** retain the literal \(R_{\max}=25\) km baseline; do not fit a new radius. Treat the energy-dependent daughter transport as a physical systematic whose public-figure envelope is now estimated, but whose exact energy-sphere value remains unavailable. Do not update the axial-vector constraint curve.

## References

1. A. Caputo, G. Raffelt, and E. Vitagliano, “Muonic boson limits: Supernova redux,” Phys. Rev. D 105, 035022 (2022), Fig. 1, DOI: 10.1103/PhysRevD.105.035022.
2. G. G. Raffelt, H.-T. Janka, and D. F. G. Fiorillo, “Neutrinos from core-collapse supernovae,” 2025 review manuscript, p. 5, discussion of neutrino mean free paths and heavy-flavor transport/energy spheres.
3. N. Blinov et al., “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B.
4. K.-C. Lai, C. S. J. Leung, and G.-L. Lin, Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023.
