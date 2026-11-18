# B.13 exact-Compton plus neutrino mode-resolved B.2 transport protocol

**Date:** 2026-11-18  
**Benchmark:** \(m_{A'}=10\) MeV, pure-vector muon current, \(g_V/g_X=1\), \(g_A/g_X=0\).  
**Background:** reconstructed SFHo-18.8 profile at \(t_{\rm pb}=1\) s.  
**Status:** protocol and local adapter are established; the global B.2 calculation remains a diagnostic until grid convergence and baseline closure pass.

## 1. Why a hybrid implementation is required

Two existing calculations each contain only half of the required physics:

- `blinov_reproduction/audit_b13_global_transport.py` evaluates the exact-recoil moving-muon B.13 kernel, keeps \(\mu^-\) and \(\mu^+\) separate, and replaces the B.14--B.16 Compton source and opacity. It then sums the three vector polarizations before applying the scalar B.2 optical-depth integral.
- `blinov_reproduction/audit_b16_global_polarization_transport.py` propagates the three neutrino inverse-decay modes independently, but the B.14--B.19 scalar Compton term is split equally among \(L,+,-\) as a diagnostic assumption.

Neither calculation is the desired physical no-mixing result. The hybrid must use the **direct B.13 mode-resolved Compton rates** and the **direct mode-resolved neutrino inverse-decay rates** before constructing any optical depth.

## 2. Local channel combination

At each opacity-grid point \((r_i,\omega_j)\), the mode order is \((L,+,-)\). For a charge convention \(Q\in\{\mu^-,\mu^-+\mu^+\}\),

\[
\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}
=\Gamma_{\mathrm{prod},h}^{\nu\bar\nu}
+\Gamma_{\mathrm{prod},h}^{C,Q},
\]

\[
\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot},Q}
=(1-e^{-\omega/T})
\left(\Gamma_{\mathrm{abs},h}^{\nu\bar\nu}
+\Gamma_{\mathrm{abs},h}^{C,Q}\right).
\]

The neutrino rates come from `rates.neutrino_rates`; the exact Compton rates come from `moving_muon_compton_rates` with \((g_V,g_A)=(1,0)\). The primary like-for-like charge lane uses \(\mu^-\) only, matching the one-species B.17 prescription. The \(\mu^-+\mu^+\) lane is retained as a separate thermal-gas extension.

All local rates are per \(g_X^2\). The coupling is inserted once in the source normalization and once in the optical-depth exponent; never pre-multiply the local rates by \(g_X^2\) and then multiply again.

## 3. Four transport lanes that must not be conflated

For each charge convention, retain the following:

| Lane | Source | Ray opacity | Meaning |
|---|---|---|---|
| Literal B.16 scalar reference | Original B.14--B.16 summed source | Original scalar B.2 opacity | Unmodified equation-level Fig. 7 reference |
| B.13 mode-summed scalar | \(\sum_h\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}\) | \(\sum_h\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot},Q}\) | Literal scalar B.2 reading after replacing Compton by exact B.13 |
| Equal-occupation closure | \(\sum_h\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}\) | \(\frac13\sum_h\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot},Q}\) | Scalar closure only under the explicit \(f_L=f_+=f_-\) assumption |
| No polarization mixing | Each \(\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}\) separately | Each \(\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot},Q}\) separately | Physical independent-mode propagation |

The B.13 mode-summed scalar lane is not the equal-occupation lane: the latter has the arithmetic-average per-state opacity. Neither scalar lane is the no-mixing solution.

## 4. Fixed-\(\omega\) B.2 propagation

The published B.2 baseline holds one \(\omega\) fixed along each Euclidean chord. Keep that convention for the primary comparison:

\[
\tau_h^Q(r,\omega,\mu)
=\frac{1}{v_{A'}(\omega)}
\int_{\mathrm{ray}(r,\mu)}ds\,
\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot},Q}
(r(s),\omega),
\qquad
v_{A'}(\omega)=\sqrt{1-\frac{m_{A'}^2}{\omega^2}}.
\]

The physical no-mixing luminosity is

\[
L_{\mathrm{no\ mix}}^Q(g_X)
=g_X^2\sum_{h=L,+,-}
\int d\mathcal P\,
\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}
e^{-g_X^2\tau_h^Q}.
\]

The equal-occupation closure instead uses

\[
\bar\tau^Q=\frac13\sum_h\tau_h^Q,
\qquad
L_{\mathrm{equal}}^Q(g_X)
=g_X^2\int d\mathcal P\,
\left(\sum_h\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}\right)
e^{-g_X^2\bar\tau^Q}.
\]

The mode-summed scalar lane uses \(\sum_h\tau_h^Q\) in the scalar exponent, exactly as the literal summed-rate interpretation. The three exponentials are generally different; no factor-of-three rescaling is permitted to force agreement.

The source measure \(d\mathcal P\) must be identical across all lanes and must retain the Eq. (B.1) lapse-squared factor, the escape threshold \(\omega_{\min}=m_{A'}/N(r)\), and the phase-space factor \(\omega^2 k/(2\pi^2)\). The source quadrature and opacity quadrature may be independent, but the interpolation between them must be validated.

## 5. Reconstructed muon-support edge

The reconstructed profile has a sharp support transition in \(\mu_\mu(r)\) at approximately

\[
r_{\mathrm{last\ support}}=22.191893657048542\ \mathrm{km},
\qquad
r_{\mathrm{first\ zero}}=22.191894657048542\ \mathrm{km}.
\]

This is a profile-support convention, not evidence of a resolved physical discontinuity in the supernova medium. The opacity path grid must explicitly include both profile vertices. Otherwise linear interpolation between sparse Gauss nodes can smear the support transition and bias the outer-shell B.13 opacity.

For a clean comparison:
1. Keep the original source radial quadrature and B.1 energy grid unchanged.
2. Add the last-supported and first-zero profile vertices to the opacity interpolation grid.
3. Recompute the literal B.16 scalar opacity on both the original and augmented opacity grids. Their difference isolates the numerical effect of resolving the support edge.
4. Use the augmented grid for all B.13 and neutrino mode-resolved opacity channels.
5. Keep the two charge lanes separate at the support edge.

## 6. Numerical acceptance gates

A global result is not accepted until all of the following are reported:

1. **Local channel closure:** neutrino mode sum versus the independent scalar neutrino rate; B.13 charge sum versus the kernel total; production and absorption detailed balance for each charge and mode.
2. **Positivity and kinematics:** all rates finite and nonnegative; final-muon mass-shell residual below \(2\times10^{-10}\).
3. **Kernel quadrature:** order ladder at representative hot-core, threshold, support-edge, and high-energy points; global sampled order-change maximum below the declared tolerance.
4. **Radial convergence:** compare at least two source/opacity radial orders and directly test interpolation across the support edge and the highest source-weighted radial intervals.
5. **Energy convergence:** compare the 100-node reference energy grid with a denser grid; preserve the exact threshold and high-energy tail, and report the source-weighted change.
6. **Ray convergence:** vary angular and path quadrature orders; compare the B.16 scalar baseline before and after the support-edge grid augmentation.
7. **B.1 closure:** source mode sum equals the sum of the independently calculated neutrino and B.13 channel sources; no extra factor of three.
8. **B.2 state counting:** report the literal mode-summed scalar, equal-occupation, and no-mixing lanes side by side. Do not identify any one of them with another by definition.
9. **Benchmark gate:** keep the 10 MeV vector baseline and its Fig. 7 discrepancy separate from all axial-vector constraints. No axial curve, SN1987A bound, or manuscript figure is updated here.

## 7. Scope

This is a 10 MeV pure-vector benchmark. The dimuon channel is kinematically closed. The current result is a reconstructed public-figure profile calculation, not a calculation on the raw Garching SFHo-18.8 simulation table. The fixed-\(\omega\) path is the primary lane; a conserved-energy-at-infinity redshifted path remains a separately labeled sensitivity diagnostic and must not be mixed into the published B.2 reproduction.
