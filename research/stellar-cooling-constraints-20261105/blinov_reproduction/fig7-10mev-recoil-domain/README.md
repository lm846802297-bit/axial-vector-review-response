# Fig. 7, 10 MeV: where the no-recoil approximation is not uniformly small

This diagnostic applies **exact stationary-muon kinematics to label domains**, without substituting any rates in the literal 10 MeV pure-vector Blinov Fig. 7 baseline. [Blinov et al., Appendix B, Eqs. (29)–(35)](https://arxiv.org/html/2511.09619v2) explicitly set the photon energy approximately equal to the vector energy after neglecting recoil. The benchmark uses fixed local vector energy along Euclidean chords on a reconstructed public-figure profile. The analysis holds the source, opacity, plotted couplings and escape integral unchanged; it is not Croon/C1, the targeted B.13 moving-muon rate benchmark, a new luminosity, or a constraint.

## Exact kinematic diagnostics

Let $M=m_\mu$, $m=m_V$, and $k=\sqrt{\omega^2-m^2}$. With an initial muon at rest and $c$ the cosine between photon and vector, the final muon mass-shell condition gives

$$
E_{\gamma,\mathrm{prod}} = \frac{2M\omega-m^2}{2(M-\omega+kc)},\qquad
E_{\gamma,\mathrm{abs}} = \frac{2M\omega+m^2}{2(M+\omega-kc)}.
$$

The production formula is at **fixed outgoing** vector energy. A solution requires $c>(\omega-M)/k$; backward geometry $c=-1$ is excluded from $\omega=(M^2+m^2)/(2M)=53.3024$ MeV onward. The allowed cosine-interval length divided by two is a geometric marker only: it is not a differential rate or an angular emission fraction. The physical no-recoil cross section in the baseline supplies no differential $c$ distribution. At a reference absorption scattering angle of $90^\circ$, $E_{\gamma,\mathrm{abs}}/\omega<1/2$ above 106.5965 MeV. This is an energy-domain marker, not a statement about the actual angle distribution. The chord direction used by B.2 is a different angle.

For forward/inverse reactions compared at the **same invariant** $s=M^2+m^2+2M\omega$, the exact center-of-mass momentum-square ratio is
$$
\frac{p_V^2}{p_\gamma^2}=\frac{\lambda(s,M^2,m^2)}{(s-M^2)^2}
=\frac{\beta_{\rm lab}^2}{(1+m^2/(2M\omega))^2}.
$$
This expression tests only the phase-space part of the reciprocal-cross-section identity; it does not correct matrix elements, the thermal distributions, or the rate. Spin multiplicities are not being changed.

## Weighted results

| Weight on this frozen benchmark | Backward production geometry forbidden at that energy | 90° absorption recoil loss >50% at that energy |
|---|---:|---:|
| Thin semi-Compton source | 89.1724% | 60.7478% |
| Escaping semi-Compton source, weak | 89.1917% | 60.7774% |
| Escaping semi-Compton source, reference peak | 95.8568% | 74.0686% |
| Escaping semi-Compton source, last visible | 99.99987% | 99.7951% |
| Escape-weighted semi-Compton depth, weak | 83.7355% | 51.4489% |
| Escape-weighted semi-Compton depth, reference peak | 94.1888% | 68.3910% |
| Escape-weighted semi-Compton depth, last visible | 99.99989% | 99.8203% |

The first three weighting types are $J_C$, $J_C e^{-\tau}$, and $J_{\rm total}e^{-\tau}\tau_C$, each normalized by its own total including B.2 chord averages. The last is the differential opacity weight established in the archived weighted audit and is not the thin-source-weighted depth. Its shape is reported separately from the source.

In the strong tail the escape-weighted semi-Compton depth has mean $p_V^2/(p_\gamma^2\beta_{\rm lab}^2)=0.996363$, i.e. only a 0.364% difference in this phase-space factor. Thus a near-unity reciprocal phase-space factor does not establish that nonforward laboratory energy recoil is perturbatively small. For scale, just 0.6640% of the strong-end neutrino opacity differential measure is in $\beta_{\rm lab}<0.9$; the neutrino escaped source has 5.2990% there. No massless or recoil-free neutrino rate was substituted.

This diagnostic locates where a recoil assumption is not uniform; it cannot establish the sign/magnitude of a thermal-rate correction, identify the origin of the +92.4284% strict residual, or imply closure of the full moving-muon kernel. The previously published profile, source and opacity all remain unchanged.

## Reproduction

The only input is the existing 13-file [weighted-sensitivity package at exact #121 commit 972f282](https://github.com/lm846802297-bit/axial-vector-review-response/tree/972f282a2958aa39ada1c630901cc5720a451ea2/research/stellar-cooling-constraints-20261105/blinov_reproduction/fig7-10mev-weighted-sensitivity). Extract that folder as `baseline/` beside `recoil.py`, or use the full local bundle. The input SHA manifest passes. The three grid hashes reproduce exactly; at the three representative vertices the reconstructed luminosity and individual source/opacity normalized weights close against the pinned weighted archive to $1.07\times10^{-14}$ absolute or relative as appropriate. Three local tests independently check final-muon mass shell, threshold inequalities and the exact phase-space ratio.

```sh
(cd baseline && sha256sum -c SHA256SUMS)
OPENBLAS_NUM_THREADS=1 python -m unittest -v test_recoil
OPENBLAS_NUM_THREADS=1 python recoil.py /tmp/fig7-recoil-replay.json
cmp native.json /tmp/fig7-recoil-replay.json
```

Runtime: Python 3.12.14/NumPy 2.3.5/SciPy 1.17.0. `native.json` contains the raw diagnostics and closure; `SHA256SUMS` fingerprints the new local package files.
