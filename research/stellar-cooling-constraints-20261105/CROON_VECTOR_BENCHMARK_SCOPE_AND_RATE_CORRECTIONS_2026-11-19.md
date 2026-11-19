# Croon vector benchmark: scope, rate corrections, and execution plan

Date: 2026-11-19  
Status: **benchmark specification; no new luminosity calculation is claimed in this document**

## Executive decision

Use Croon, Elor, Leane and McDermott, *Supernova Muons: New Constraints on Z' Bosons, Axions and ALPs*, JHEP 01 (2021) 107, arXiv:2006.13942, as a **historical vector-model benchmark and method comparison**, not as the sole or automatically correct reference for the production rates.

The paper explicitly says that it considers **only vector couplings** of the \(Z'\). Its muon interaction is vectorial, with equal left- and right-handed couplings. It does not calculate a spin-1 axial-vector \(A'\) model. Its ALP section concerns spin-0 particles and is not a substitute for an axial-vector calculation.

A second, modern vector reference is Blinov et al., *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, arXiv:2511.09619v2. This paper explicitly re-evaluates thermally averaged production rates, including the neutrino chemical-potential dependence and the semi-Compton detailed-balance / phase-space factors. Therefore, the benchmark must retain separate **Croon-literal** and **updated-rate** lanes. Do not silently patch the Croon formulas and then call the result a reproduction of Croon.

A third, independent trapping-regime comparison is Lai, Leung and Lin, Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023. Its plateau prescription and neutrinosphere treatment are a distinct transport lane; do not combine it algebraically with Croon or Blinov.

## 1. Scope of Croon et al. (2021)

Primary sources:

- Published paper: https://doi.org/10.1007/JHEP01(2021)107
- arXiv: https://arxiv.org/abs/2006.13942
- Full published PDF: https://link.springer.com/content/pdf/10.1007/JHEP01%282021%29107.pdf

The authors state in Sec. 4, immediately before Sec. 4.1, that they remain agnostic about the \(Z'\) mass-generation mechanism and **only consider vector couplings**. Eq. (4.1) couples the left-handed lepton doublet and the right-handed muon with the same coefficient:
\[
\mathcal L \supset g_\mu Z'_\alpha
\left(\bar\ell\gamma^\alpha\ell+\bar\mu_R\gamma^\alpha\mu_R\right).
\]
For the charged muon this is
\[
g_\mu Z'_\alpha\bar\mu\gamma^\alpha\mu,
\qquad g_V=g_\mu,\quad g_A=0.
\]
Thus the Croon \(Z'\) rates and bounds are **not** directly transferable to the axial-vector model.

For \(U(1)_{L_\mu-L_\tau}\), Eq. (4.2) has equal-sign left- and right-handed charged-lepton couplings at tree level. The neutrino interaction is left-chiral. The paper also discusses loop-induced kinetic mixing. These model details must be kept separate from a generic muon-only vector benchmark.

## 2. Two production-rate equations that must not be conflated

### 2.1 Neutrino-pair coalescence

Croon Eq. (4.6) gives
\[
\Gamma^{\rm Croon}_{\nu\bar\nu\to Z'}(\omega)
=\frac{\alpha_{Z'}m_{Z'}^2}{3\omega}
\frac{1}{e^{\omega/T}-1}.
\]
This is a useful **Croon-literal reference expression** under its assumptions.

However, the 2026 Blinov et al. Appendix B, Eqs. (B.7)--(B.10), explicitly finds that the neutrino chemical-potential dependence does not generally cancel in the Fermi-Dirac phase-space integral. The cancellation used in older simplified expressions is recovered only in the Maxwell-Boltzmann / negligible-degeneracy limit. The updated rate is written as
\[
\Gamma^{\rm prod}_{\bar\nu\nu\to V}(\omega)
=\frac{m_V}{\omega}\,3\Gamma_{V\to\bar\nu\nu}
I\!\left(\frac{\mu_\nu}{T},\frac{\omega}{T},v_V\right),
\]
with
\[
\Gamma_{V\to\bar\nu\nu}=\frac{\alpha_Vm_V}{6}
\]
for one flavor of left-handed neutrinos, and the explicit Fermi-Dirac function \(I\) given in Eq. (B.9) of that paper. Its absorption integral independently satisfies
\[
\Gamma^{\rm prod}_{\bar\nu\nu\to V}
=e^{-\omega/T}\Gamma^{\rm abs}_{V\to\bar\nu\nu}.
\]

Implementation rule:

1. Reproduce Croon Eq. (4.6) as a named legacy lane.
2. Implement the chemical-potential-dependent B.7--B.10 expression as a separate updated lane.
3. Compare the updated expression with Croon only after matching the number of neutrino flavors, chiral states, the vacuum-width convention (spin-averaged versus polarization-summed), and the definition of the coupling. Do **not** assume the prefactors coincide: Blinov et al. explicitly state that their Maxwell-Boltzmann limit matches Ref. [17] (Lai et al.), not that it reproduces Croon Eq. (4.6). Resolve this normalization algebraically before using it as a regression test.
4. In the actual SFHo calculation, use the \(\nu_\mu\) and \(\nu_\tau\) chemical potentials separately when supplied by the profile. Do not replace them by zero in the production result merely to improve agreement.

Source: https://arxiv.org/abs/2511.09619, Appendix B, Eqs. (B.7)--(B.10).

### 2.2 Semi-Compton production

Croon Eq. (4.7) uses a Thomson/no-recoil approximation:
\[
\Gamma^{\rm Croon}_{\mu\gamma\to\mu Z'}(\omega)
=
\frac{8\pi\alpha_{\rm EM}\alpha_{Z'}}{3m_\mu^2}
n_\mu F_{\rm deg}
\frac{1}{e^{\omega/T}-1}
\sqrt{1-\frac{m_{Z'}^2}{\omega^2}}.
\]
Croon notes in its footnote that the massive-\(Z'\) matrix element differs technically from ordinary Compton scattering, but regards the approximation as adequate in the low-mass region dominating its constraint.

Blinov et al. 2026 Appendix B, Eqs. (B.13)--(B.19), instead starts from the full thermal phase-space integral and derives the non-recoil limit with the correct inverse/forward phase-space relation:
\[
\Gamma^{\rm prod}_{\mu\gamma\to\mu V}
=
\frac{1}{v_V}n_\mu F_{\rm deg}
\frac{2}{e^{\omega/T}-1}
\sigma(\mu\gamma\to\mu V),
\]
where
\[
\sigma(\mu\gamma\to\mu V)\simeq
\frac{8\pi\alpha_{\rm EM}\alpha_V}{3m_\mu^2}
\left(1+\frac{m_V^2}{2\omega^2}\right)v_V.
\]
The paper explains that the rate contains an additional \(1/v_V\) and a factor 2 relative to some earlier published expressions: the velocity factor follows from the unequal massive-vector and photon phase-space volumes, and the factor 2 accounts for the two photon polarizations because the thermal rate sums initial photon states whereas the cross-section convention averages them.

Consequently, Croon Eq. (4.7) is **not** the corrected formula to use for the production calculation. It remains a legacy comparison. Do not apply a guessed global factor to the final rate; implement B.13--B.19 from the phase-space integral and verify it numerically.

For the same (n_\mu F_{\rm deg}), coupling and Bose factor, direct substitution gives the equation-level ratio
\[
\frac{\Gamma_{\rm B16}}{\Gamma_{\rm Croon}}
=\frac{2\left(1+m_V^2/(2\omega^2)\right)}{v_V},
\qquad v_V=\sqrt{1-m_V^2/\omega^2}.
\]
Thus the ratio tends to 2 for (m_V/\omega\to0), and grows as threshold is approached. This is a controlled comparison of the two printed non-recoil formulae, not a universal correction factor to be applied to arbitrary kernels.

The full moving-muon/recoil kernel already developed in this repository is the next level beyond this non-recoil limit. It must reduce to the updated B.16 expression in the appropriate controlled limit, not necessarily to Croon Eq. (4.7).

Source: https://arxiv.org/abs/2511.09619, Appendix B, Eqs. (B.13)--(B.19).

## 3. Transport prescriptions are separate benchmarks

Croon's luminosity calculation uses its own definitions of the production region, \(R_{\rm far}\), and absorption/escape treatment (Sec. 3, especially Eqs. (3.3)--(3.5)); it adopts \(R_{\rm far}=100\) km in its results. It should be implemented literally for a historical Fig. 2 reproduction.

Blinov et al. 2026 use a revised ballistic treatment, including the vector-speed factor in optical depth, reduced absorption / stimulated emission, the \(R_{\max}=R_\nu\) boundary, and gravitational lapse/redshift effects. These are not optional numerical refinements to be mixed into the Croon lane; they define a different physical calculation.

Lai, Leung and Lin (2024), arXiv:2401.16023, study the trapping regime and argue for a luminosity plateau at large coupling with the attenuation boundary tied to the production boundary. This is a third independent transport prescription. Compare it as its own lane and record the boundary and opacity definitions.

References:

- Croon et al.: https://doi.org/10.1007/JHEP01(2021)107
- Blinov et al.: https://doi.org/10.1007/JHEP06(2026)155
- Lai et al.: https://doi.org/10.1103/PhysRevD.110.103023

## 4. Benchmark lanes and acceptance gates

| Lane | Local rates | Transport | Purpose |
|---|---|---|---|
| C0: Croon-literal | Croon Eqs. (4.6), (4.7) and stated approximations | Croon Sec. 3 literally | Historical reproduction only |
| C1: corrected vector rates | Blinov B.7--B.19, plus full B.13 kernel where needed | Fixed transport prescription explicitly selected | Test rate corrections independently |
| C2: modern vector SN | Blinov B.7--B.19 | Blinov ballistic / redshift / stimulated-emission treatment | Current vector reference |
| C3: trapping comparison | Lai et al. rates and conventions | Lai et al. plateau / boundary prescription | Independent high-opacity comparison |
| A0: axial model | Derive from this project's UV current and Goldstone sector | Reuse only validated transport machinery | Actual target physics |

Do not compare total luminosities until the following are matched or explicitly varied: mediator mass, coupling definition, number of neutrino flavors, neutrino chemical potentials, muon/antimuon convention, muon degeneracy factor, profile and post-bounce time, source radius, \(R_{\rm far}\), lapse/redshift, stimulated emission, opacity definition, polarization sum/average, and energy integration convention.

### Local-rate acceptance

- Croon-literal expressions reproduce the printed equations in their stated limit.
- Corrected neutrino rate has a separately derived Maxwell-Boltzmann limit; compare its normalization with Croon Eq. (4.6) only after matching flavor multiplicity, chiral-state counting, spin averaging, and coupling definitions.
- Corrected semi-Compton rate reproduces Blinov B.16 in the no-recoil limit.
- Full moving-muon B.13 kernel approaches the same controlled limit.
- Forward and inverse rates satisfy detailed balance pointwise, flavor by flavor and polarization by polarization.
- Explicit spinor traces and an independent invariant-amplitude implementation agree.
- No fitted normalization or opacity multiplier is allowed.

### Global-luminosity acceptance

- Reproduce the Croon Fig. 2 only in lane C0 with its own profile, radius, rates and transport assumptions. Any missing raw input or figure-digitization uncertainty must be reported.
- Recompute the same parameter points in lane C1/C2 without tuning to Croon.
- Compare lane C3 only after matching its benchmark profile and its production/attenuation boundaries.
- Report optically thin luminosity, source spectrum, optical depth, escape probability and total luminosity separately. A match in total luminosity alone is insufficient.
- Distinguish numerical quadrature uncertainty from profile, transport and model uncertainty.

## 5. Axial-vector transfer: no direct rate reuse

For the target interaction convention
\[
\mathcal L_{\mu A'}=
A'_\alpha\bar\mu\gamma^\alpha(g_V-g_A\gamma^5)\mu,
\]
the vector benchmark corresponds to \(g_A=0\). The target pure-axial limit has \(g_V=0\). The local matrix elements, polarization-resolved rates, inverse rates and longitudinal behavior must be recalculated.

In this project, do not assume that the neutrino coupling equals the charged-muon axial coupling. Extract the mass-basis couplings from the actual UV model (including finite right-handed mixing where retained). Keep the Goldstone/current Ward identity consistent with the same convention. The spin-0 ALP calculation in Croon is not a substitute for the spin-1 axial-vector calculation.

## 6. Immediate execution order

1. Freeze the Croon PDF version, equations, figure digitization, profile source, and all assumptions in a provenance manifest.
2. Build C0 analytic local-rate checks for Eqs. (4.6) and (4.7).
3. Build C1 corrected local-rate checks using Blinov B.7--B.19.
4. Compare C0 and C1 channel by channel before any luminosity integration.
5. Implement the Croon Sec. 3 luminosity prescription as an isolated transport adapter; do not modify the existing Blinov B.2 production baseline.
6. Reproduce the Croon Fig. 2 benchmark to the precision allowed by public inputs and digitization.
7. Only after C0/C1 are independently validated, proceed to the axial-vector A0 kernel and its Goldstone consistency checks.

## 7. Current status and non-claims

- This document is a literature/formula audit and execution specification.
- It does not claim that Croon Fig. 2 has been reproduced.
- It does not claim that the Croon rates are the corrected modern rates.
- It does not claim that Blinov 2026 is an exact ground truth; it is a more complete, independently checkable reference with its own profile and transport assumptions.
- It does not update any axial-vector luminosity or SN1987A exclusion.
- The existing B.13/B.16 calculations and the open PR #121 remain unchanged by this document.

