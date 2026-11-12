# Vector-to-axial response mapping: derivation strategy and rescaling criterion

**Date:** 2026-11-07  
**Status:** analytic criterion established; numerical response scan is the next local-kernel task. No stellar luminosity curve or exclusion boundary is produced here. Original Garching data are not required for this microscopic comparison.

## 1. Decision

Do not assume a universal vector-to-axial coupling rescaling. Derive the response kernels from the two currents using the same kinematics, polarization basis, thermal distributions, and phase-space conventions. Test whether the ratio is constant only after resolving reaction channel, polarization, mediator energy, and local thermodynamic variables.

If a common constant is demonstrated over all channels and the stellar phase space that materially contributes to luminosity and opacity, a coupling rescaling may be used. Otherwise the mapping must be channel- and mode-resolved and inserted into the transport calculation.

## 2. UV current and sign convention

The UV model gives
\[
\mathcal L_{\mu A'}=
A'_\alpha\bar\mu\gamma^\alpha
(g_V^\mu+g_A^\mu\gamma^5)\mu,
\quad
g_V^\mu=g_X\sin^2\theta_{\mu R},
\quad
g_A^\mu=-g_X\cos^2\theta_{\mu R}.
\]
The rates module uses \(\gamma^\alpha(-\gamma^5)\) as its positive unit-axial basis. Therefore the coefficient passed to that basis is
\[
g_{A,\mathrm{code}}=-g_A^\mu=g_X\cos^2\theta_{\mu R}.
\]
The neutrino charges remain \(g_{\nu_\mu}=+g_X\), \(g_{\nu_\tau}=-g_X\); they do not depend on \(\theta_{\mu R}\).

## 3. Why a single rescaling is not automatic

For a reaction \(i\) and physical polarization \(h\), define the unit-coupling response
\[
K_{J,h}^{(i)}(x)=
\frac{\Gamma_{J,h}^{(i)}(x)}{g_J^2},
\qquad J=V,A,
\]
where \(x\) denotes the relevant kinematics and medium variables. A universal mapping requires
\[
K_{A,h}^{(i)}(x)=C\,K_{V,h}^{(i)}(x)
\]
with the same positive constant \(C\) for every relevant channel, mode, and phase-space point. Only then can \(g_A=g_V/\sqrt C\) preserve all corresponding rates.

This condition is stronger than equality of a vacuum total width or an angle-integrated cross section at one benchmark point. Stellar cooling depends on both emissivity and inverse absorption, and on the mode-dependent optical depth inside an escape probability.

### 3.1 Neutrino coalescence / inverse decay

In the UV completion, the active-neutrino current is unchanged when \(\theta_{\mu R}\) varies. Thus the neutrino channel is not a muon-current vector-to-axial replacement: its coupling remains \(g_X\) and its rate remains the same at fixed \(g_X,m_{A'}\), medium profile, and neutrino-current convention.

Consequently, a rescaling of \(g_X\) that is inferred from the muon Compton channel also changes the neutrino rate by the square of that rescaling. The two channels cannot both be preserved by a single coupling-axis transformation unless the muon and neutrino response factors happen to coincide or one channel is demonstrably negligible in the relevant source/opacity integral.

For massless chiral neutrinos, changing the mediator Lorentz label on the charged-muon current does not justify changing the neutrino coupling. Keep the neutrino current exactly as specified by the UV model.

### 3.2 Muon semi-Compton

The amplitudes are generated from
\[
\Gamma^\alpha,\qquad \Gamma^\alpha\gamma^5
\]
at the mediator vertex, with both diagrams, the physical photon polarization sum, and the physical mediator polarization retained. The axial and vector traces contain different mass- and momentum-dependent terms. In general,
\[
\frac{|\mathcal M_{A,h}|^2}{|\mathcal M_{V,h}|^2}
\]
depends on mediator mass, energy, scattering angle, and polarization. The mixed current must be evaluated at amplitude level:
\[
|\mathcal M_{\rm mix}|^2=
|g_V^\mu\mathcal M_V+g_A^\mu\mathcal M_A|^2,
\]
including interference until it is shown to vanish after the relevant sums. Do not add pure-vector and pure-axial rates by assumption.

The repository already contains compton_matrix_elements, compton_mixed_matrix_elements, compton_kernels, and compton_mixed_kernels in rates.py. The immediate task is to use these existing implementations for unit-coupling, mode-resolved response ratios and endpoint checks, not to duplicate the trace code.

### 3.3 Muon-pair inverse decay / decay

Above \(m_{A'}=2m_\mu\), vector and axial widths have different threshold factors:
\[
\Gamma_V\propto \beta_\mu(1+2m_\mu^2/m_{A'}^2),\qquad
\Gamma_A\propto\beta_\mu^3.
\]
The ratio is mass dependent. The existing charged_muon_decay_rates and charged_muon_decay_rates_mixed provide the pure and mixed kernels; verify their mode-resolved normalization and thermal blocking before including this channel in any response map.

## 4. Exact criterion for a useful rescaling

A single coupling rescaling is admissible only if all of the following hold over the relevant phase space:

1. The unit-coupling production kernels are proportional with the same constant for every contributing channel and polarization.
2. The inverse absorption kernels have the same proportionality constant, so detailed balance and reduced opacity are preserved.
3. The same proportionality survives the thermal integrations over photon, muon, and neutrino distributions.
4. The total optical depth and escape probability transform consistently. A rate-level constant alone is insufficient if different channels scale differently.
5. The mapping preserves the UV relation between the charged-muon current and the unchanged active-neutrino current.

If any condition fails, no global \(g_X\) rescale exists. One may still construct a channel-resolved response mapping, but obtaining the luminosity then requires evaluating
\[
\tau_h(E,r)=\int ds\,
\left[\Gamma_{\nu,h}^{\rm red}
+\Gamma_{\mu\gamma,h}^{\rm red}
+\Gamma_{\mu\mu,h}^{\rm red}+\cdots\right]
\]
with the correct UV couplings and mode-specific transport. The escaped luminosity is not obtained by rescaling the published total luminosity curve.

## 5. What can be done without the original stellar profile

The microscopic response ratios can be derived and tested without Garching data:
- vacuum traces and differential cross sections;
- mode-resolved vector/axial ratios as functions of \((m,\omega,\cos\vartheta)\);
- exact pure-vector and pure-axial endpoint tests;
- mixed-current interference;
- local thermal response ratios on the already archived reconstructed profile.

The reconstructed profile is sufficient for a diagnostic test of whether the ratio is constant. It is not sufficient to claim exact reproduction of Blinov or to publish a precision supernova exclusion curve. If the response ratio varies substantially over the phase-space region that contributes to transport, the next calculation needs the best documented stellar profile, but this does not make an original-data application a prerequisite for the analytic result.

## 6. Ordered implementation plan

1. **P0 — audit existing local kernels:** verify exact pure-vector and pure-axial endpoints of the mixed Compton matrix element, Ward identity, mode normalization, and interference sign. Reuse existing code; do not create a second trace implementation.
2. **P0 — derive neutrino mapping:** show explicitly that the UV active-neutrino rates remain fixed at \(g_X\) as \(\theta_{\mu R}\) changes. This is already sufficient to rule out treating the entire stellar luminosity as a muon-current rescale.
3. **P0 — compute response ratios:** tabulate \(K_{A,h}/K_{V,h}\) for Compton over mass, energy, angle, and mode; separately compare pure vector and axial dimuon rates above threshold.
4. **P1 — thermal response:** integrate production and absorption separately over the same distributions and test whether any constant ratio survives.
5. **P1 — UV mixed response:** evaluate the actual \(g_V^\mu=g_X\sin^2\theta_{\mu R}\), \(g_{A,\rm code}=g_X\cos^2\theta_{\mu R}\), retaining interference. Keep neutrino rates at \(g_X\).
6. **P2 — transport:** only after the pure-vector reference issue is sufficiently characterized, use the existing reconstructed profile for a clearly labelled diagnostic transport comparison. Do not call it an exact Blinov reproduction.

## 7. Claims boundary

- No Garching application is required to complete the analytic and local-kernel response study.
- No universal rescaling is assumed or claimed in advance.
- No axial exclusion curve is generated by rescaling the current Blinov vector curve.
- The Blinov 10 MeV Fig. 7 mismatch and reconstructed-profile limitation remain explicit.
- This module does not change the manuscript, referee response, existing production rates, opacity normalization, or saved cooling figures.
