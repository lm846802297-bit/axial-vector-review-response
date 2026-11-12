# Moving-muon semi-Compton and thermal dimuon rates

**Status:** local thermal-rate implementation and regression suite added on the stacked research branch. This is not a stellar luminosity or SN1987A exclusion calculation.

## 1. Scope and profile benchmark

This stage converts the existing amplitude-level response kernels into local thermal emissivities. It does not modify the existing stellar transport solver, axial constraint plots, manuscript, or referee response.

The selected profile points are taken from the repository's reconstructed SFHo-18.8, post-bounce 1 s digitized profile:

| Radius | T | mu_mu | mu_nu_mu | lapse |
|---:|---:|---:|---:|---:|
| 0 km | 19.26522111 MeV | 46.67432845 MeV | -58.61375672 MeV | 0.7363304267 |
| 12.5 km | 23.88195915 MeV | 90.21658531 MeV | -2.591655499 MeV | 0.8388424539 |

The chemical-potential convention is the one already checked against the digitized muon density: mu_mu is the mu- chemical potential, and the mu+ chemical potential is -mu_mu. The profile is reconstructed from public figures; it is not the original simulation table.

## 2. Moving-muon semi-Compton integral

The process is

\[
A'(q)+\mu^\pm(P)\leftrightarrow\gamma(K)+\mu^\pm(P').
\]

For a fixed on-shell A' momentum \(q=(\omega,0,0,k_A)\), the absorption and production rates are evaluated separately:

\[
\begin{aligned}
\Gamma^{\rm abs}_h(q)
&=\frac{1}{2\omega}\sum_{\pm,s}
\int d\Pi_Pd\Pi_{P'}d\Pi_K\,(2\pi)^4
\delta^{(4)}(P+q-P'-K)\,
\overline{|\mathcal M_{h,\pm}|^2}\,
f_{\mu^\pm}(E_P)[1-f_{\mu^\pm}(E_{P'})][1+n_B(k)],\\
\Gamma^{\rm prod}_h(q)
&=\frac{1}{2\omega}\sum_{\pm,s}
\int d\Pi_Pd\Pi_{P'}d\Pi_K\,(2\pi)^4
\delta^{(4)}(P+q-P'-K)\,
\overline{|\mathcal M_{h,\pm}|^2}\,
f_{\mu^\pm}(E_{P'})[1-f_{\mu^\pm}(E_P)]n_B(k).
\end{aligned}
\]

The initial-muon spin average in the trace is accompanied by the physical spin degeneracy two. The two muon charges are integrated separately. Charge conjugation reverses the relative axial term for a mu+ target; this is retained before summing the charge-resolved rates.

Choose the muon azimuth to be zero using axial symmetry. With \(c=\cos\theta_\gamma\),

\[
C=E_P+\omega-\mathbf p\cdot\hat{\mathbf k}-k_Ac,
\qquad
k=\frac{m_{A'}^2+2P\cdot q}{2C},
\qquad
P'=P+q-K.
\]

The final-muon on-shell condition is imposed exactly. After the photon-energy delta function is integrated out, the local rate becomes

\[
\Gamma_h^{\rm abs/prod}
=\frac{1}{128\pi^4\omega}
\sum_{\pm}\int dx\,d\cos\theta_P\,d\cos\theta_\gamma\,d\phi_\gamma\,
T p\frac{k}{C}\,
\overline{|\mathcal M_{h,\pm}|^2}\,
\mathcal F_{\rm abs/prod},
\]

where

\[
x=\frac{E_P-m_\mu}{T},\qquad
p=\sqrt{Tx(2m_\mu+Tx)}.
\]

The prefactor includes the two muon spin states and the integrated initial-muon azimuth. The longitudinal vector polarization uses the Ward-equivalent shifted polarization; the axial longitudinal polarization remains physical. The real-photon sum uses \(-g_{\mu\nu}\), with the photon Ward identity checked pointwise for moving targets and both muon charges.

The production and absorption statistical factors obey pointwise

\[
\frac{f(E_{P'})[1-f(E_P)]n_B(k)}
{f(E_P)[1-f(E_{P'})][1+n_B(k)]}
=e^{-\omega/T},
\]

so the integrated mode-resolved rates satisfy

\[
\Gamma^{\rm prod}_h=e^{-\omega/T}\Gamma^{\rm abs}_h.
\]

The A' momentum integral is then completed:

\[
Q_{\mu\gamma,h}
=\frac{1}{2\pi^2}\int_{m_{A'}}^\infty
d\omega\,\omega^2\sqrt{\omega^2-m_{A'}^2}\,
\Gamma^{\rm prod}_h(\omega).
\]

This is a local emissivity per \(g_X^2\), not a radial luminosity.

## 3. Semi-Compton results

The central-profile mass scan uses \(m_{A'}=(0.01,0.1,1,10,100,220)\) MeV, with 12-point outer energy quadrature and inner orders \((12,8,8,8)\). Representative polarization-summed results are:

| m_A' (MeV) | Q_V (MeV^5) | Q_A (MeV^5) | Q_A/Q_V |
|---:|---:|---:|---:|
| 0.01 | 1.39168e1 | 4.51690e8 | 3.24565e7 |
| 0.1 | 1.39168e1 | 4.51691e6 | 3.24566e5 |
| 1 | 1.39167e1 | 4.51917e4 | 3.24731e3 |
| 10 | 1.36975e1 | 4.73464e2 | 3.45658e1 |
| 100 | 1.57191 | 2.96046 | 1.88335 |
| 220 | 1.32216e-2 | 1.72169e-2 | 1.30218 |

All Q values are per \(g_X^2\). These are local profile-point results, not integrated stellar luminosities.

At 10 MeV and the center, the mode-resolved axial/vector ratios are approximately

\[
R_L\simeq9.40\times10^2,\qquad
R_+ = R_-\simeq2.43,
\]

while the polarization-summed ratio is about 34.6. At 12.5 km, the corresponding summed ratio is about 43.2. Thus the thermally averaged response is both polarization- and profile-dependent; a universal vector-to-axial rescaling is not supported.

For \(\theta_{\mu R}=10^{-2}\), the UV benchmark uses

\[
g_V/g_X=\sin^2\theta_{\mu R},\qquad
g_A/g_X=-\cos^2\theta_{\mu R}.
\]

The summed mixed-current emissivity is close to the pure-axial result because the vector admixture is small. The V-A interference is nevertheless retained: it produces opposite-sign contributions in the two circular modes (about \(\pm3.9\times10^{-5}\) of the corresponding mode emissivity at the central 10 MeV benchmark), which cancel in the total after summing all three modes. The mode-resolved rates, not only the total, must therefore be retained for opacity work.

At the central 10 MeV benchmark, increasing the outer A' energy quadrature from 12 to 16 at fixed inner orders \((14,10,10,10)\) changes the pure-axial emissivity by about \(-2.13\times10^{-4}\). An inner refinement from \((14,10,10,10)\) to \((18,14,14,14)\) changes it by about \(-1.6\times10^{-5}\).

## 4. Full dimuon energy integral

For \(m_{A'}>2m_\mu\), the existing mixed-current angular trace and mode-resolved thermal rates are integrated over the full on-shell A' momentum distribution:

\[
Q_{\mu\mu,h}
=\frac{1}{2\pi^2}\int_{m_{A'}}^\infty
d\omega\,\omega^2\sqrt{\omega^2-m_{A'}^2}\,
\Gamma^{\rm prod}_{\mu\mu,h}(\omega).
\]

The exact threshold is

\[
m_{A'}^{\rm th}=2m_\mu=211.316751\ \mathrm{MeV}.
\]

Below and at threshold the on-shell dimuon channel is closed. Both muon Fermi factors and their Pauli-blocking complements are retained. Production and absorption are evaluated separately and obey mode-by-mode detailed balance.

At the central profile point, the polarization-summed thermal emissivity ratio agrees with the analytic vacuum-width ratio over all nine threshold factors from 1.0001 to 5:

\[
\frac{Q_A^{\mu\mu}}{Q_V^{\mu\mu}}
=\frac{\Gamma_A}{\Gamma_V}
=\frac{\beta_\mu^2}{1+2m_\mu^2/m_{A'}^2}.
\]

This equality is not an accidental fit: after summing the three mediator polarizations, the normalized vector and axial decay angular distributions both become isotropic. The thermal Fermi factors therefore preserve the total-width ratio. Individual polarization rates remain distinct, and the V-A interference splits the two circular modes with opposite signs; it cancels only after their sum.

The 16-to-32 energy-quadrature change at \(m_{A'}=1.05(2m_\mu)\) is below \(10^{-9}\) for the selected central benchmark.

## 5. Regression and validation

The dedicated test file covers:

1. Stationary-target pointwise limit against the existing Compton kernel for pure vector and pure axial currents.
2. Pointwise photon Ward identity for moving muons and both charge signs.
3. Final-muon on-shell kinematics.
4. Mode-by-mode Compton detailed balance.
5. Charge-conjugate cancellation of V-A interference at zero muon chemical potential.
6. Charge-resolved interference at nonzero muon chemical potential.
7. Cold, dilute moving-muon limit against the stationary-target \(v\sigma\) kernel.
8. Positive full Compton emissivity and its detailed-balance/shell residuals.
9. Exact dimuon threshold closure.
10. Thermal dimuon axial/vector ratio against the analytic width ratio and energy-quadrature convergence.

The machine-readable scan is archived as `outputs/thermal_response_scan.json` by the dedicated workflow. It includes the profile hash, code hashes, mode-resolved spectra, charge-resolved mixed Compton emissivity, and quadrature settings.

## 6. Interpretation boundary

This stage completes local semi-Compton and dimuon thermal phase-space integrals. It does **not** include the unchanged active-neutrino channel, radial integration, reduced opacity, escape probabilities, redshifted luminosity, hydrodynamic backreaction, or a SN1987A exclusion contour. It therefore does not pass the separate pure-vector Blinov Fig. 7 literature gate and does not authorize a finite-mixing stellar-cooling curve.

The existing PR #56 remains unchanged. This work is isolated in a stacked Draft PR based on the PR #56 research branch.
