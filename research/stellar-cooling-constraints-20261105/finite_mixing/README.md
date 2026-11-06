# Finite-mixing vector--axial stellar-cooling constraints

**Status (2026-11-07): UV coupling map and amplitude-level mixed Compton/dimuon kernels are implemented and endpoint-tested. No mixed-current luminosity scan or exclusion curve has been produced; the pure-vector literature gate remains blocked.**

This module is a separate research line inside PR #56. Its purpose is to calculate the stellar-cooling constraint for the actual UV-model muon current, which contains both vector and axial components for nonzero right-handed mixing.

## 1. Coupling convention

Use
\[
\mathcal L_{\mu A'} =
A'_\mu\bar\mu\gamma^\mu
(g_V^\mu+g_A^\mu\gamma^5)\mu,
\]
with
\[
g_V^\mu=g_X\sin^2\theta_{\mu R},\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R}.
\]
The chiral couplings are
\[
g_L^\mu=g_V^\mu-g_A^\mu=g_X,\qquad
g_R^\mu=g_V^\mu+g_A^\mu=-g_X\cos(2\theta_{\mu R}).
\]
Thus \(\theta_{\mu R}=0\) is the pure-axial endpoint and \(\theta_{\mu R}=\pi/2\) is the pure-vector endpoint. At the adopted UV benchmark \(\theta_{\mu R}=10^{-2}\),
\[
|g_V^\mu/g_A^\mu|=\tan^2\theta_{\mu R}
\simeq 1.00006667\times10^{-4}.
\]

The existing rates module represents its axial basis as \(\gamma^\mu(-\gamma^5)\). In that basis the coefficient is \(-g_A^\mu\). This sign conversion is explicit in model.py and must be preserved when constructing mixed amplitudes.

The active-neutrino couplings are unchanged:
\[
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X.
\]
They do not scale with the charged-muon mixing angle. Tau leptons are not included as thermal charged particles in the PNS calculation.

## 2. Non-negotiable vector-endpoint gate

A mixed-current calculation is not accepted merely because it approaches the existing axial curve at small angle. Its pure-vector endpoint must first reproduce the published Blinov et al. result with matched inputs. The version of record is JHEP 2026, 155, DOI 10.1007/JHEP06(2026)155; arXiv:2511.09619.

The current state is **BLOCKED**; see VECTOR_ENDPOINT_GATE_2026-11-07.md. In brief:

- The archived independent scalar Appendix-B calculation reproduces four digitized Fig. 4 contour points within 2.60%, but does not reproduce the full Fig. 7 luminosity curve at 10 MeV (91.35% maximum and 15.64% mean absolute relative residual).
- The current mode-resolved vector scan closes at 259.08--259.14 MeV, while the archived digitized Fig. 4 contour ends near 210.98 MeV.
- The two implementations differ in more than one ingredient. No fitted rescaling or arbitrary opacity multiplier is permitted.
- Existing digitized figures were extracted from the arXiv source archive. The published version-of-record Fig. 4 and Fig. 7 must be independently checked and digitized before final acceptance.

A close match to a cooling contour alone is not sufficient: the full luminosity curve controls the escape/trapping behavior used in the mixed-current extension.

## 3. Required calculation after the gate passes

1. The amplitude-level kernels are implemented in rates.py as compton_mixed_matrix_elements / compton_mixed_kernels and charged_muon_decay_rates_mixed. Tests verify exact pure-vector and pure-axial endpoints, photon Ward identity, mode-by-mode detailed balance, and the circular-mode V-A interference. Do not infer full cooling validity from these local-kernel tests. The amplitude is constructed as:
   \[
   \mathcal M_h^{\rm mix}
   =g_V^\mu\mathcal M_{V,h}
    +g_A^\mu\mathcal M_{A,h},
   \]
   with a documented sign convention. Retain the vector--axial interference term until the polarization and phase-space sums demonstrate that it vanishes.
2. Compute the mixed semi-Compton production and inverse absorption kernels for each physical A' polarization. Preserve exact crossing, the photon polarization sum, and mode-by-mode detailed balance.
3. Compute the mixed dimuon decay/inverse-decay kernels above threshold. The spin-summed vacuum width is the sum
   \[
   \Gamma_{\mu\mu}=
   \frac{(g_V^\mu)^2m_{A'}}{12\pi}
   \left(1+\frac{2m_\mu^2}{m_{A'}^2}\right)\beta_\mu
   +\frac{(g_A^\mu)^2m_{A'}}{12\pi}\beta_\mu^3,
   \]
   but the mode-resolved in-medium kernels must retain any vector--axial interference that survives the angular and occupation integrals.
4. Leave the neutrino production/absorption couplings at their original g_X values. Do not rescale them with \(\theta_{\mu R}\).
5. Propagate each polarization with its own reduced opacity and sum escaped luminosities only after attenuation. Do not exponentiate a polarization-summed absorption rate unless a separately justified transport approximation is explicitly being tested.
6. Run three endpoints on identical profile, grid, and transport settings: pure axial (\(\theta_{\mu R}=0\)), pure vector (\(\theta_{\mu R}=\pi/2\)), and the UV benchmark (\(\theta_{\mu R}=10^{-2}\)).
7. Check amplitude-level endpoints, detailed balance, quadrature convergence, and the full luminosity/contour outputs. Archive code hashes, input hashes, numerical settings, and outputs.

## 4. Separation of claims

The published pure-vector curve is an external benchmark, not a substitute for the mixed-current calculation. The existing axial curve is an internal endpoint, not a proof of the mixed calculation. A mixed curve is a new model-specific result and is not obtained by adding or rescaling the two endpoint curves.

Until the vector-endpoint gate passes, the module is limited to the UV coupling map, local mixed-kernel implementations, endpoint regressions, and validation protocol. PR #56 remains Draft, and no referee-response or manuscript file is changed.
