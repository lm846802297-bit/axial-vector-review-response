# Independent direct forward/reverse collision-integral audit

**Date:** 2026-11-07  
**Status:** P0 audit implementation added; numerical CI result pending.  
**Scope:** Internal validation only. No production rates, transport, saved cooling curves, manuscript, or referee-response files are changed.

## 1. Why the priority changes

The 10 MeV three-layer diagnostic finds that the source-weighted mean reduced optical depth is approximately 89.78% neutrino inverse decay and 10.22% inverse Compton. This fraction is specific to the reconstructed SFHo-18.8 profile, the 10 MeV benchmark, and the audited source weighting; it is not a universal statement over mediator mass and coupling.

The 90% contribution makes the neutrino inverse-decay kernel the first microscopic target. A transport comparison cannot validate this kernel if its forward and inverse collision terms have not been checked independently.

## 2. Existing implementation: what is already direct

The function rates.neutrino_rates already evaluates production and absorption separately:
- production uses the two Fermi occupations, \(f_1f_2\);
- absorption uses the two Pauli-blocking factors, \((1-f_1)(1-f_2)\).

Thus the production solver does **not** construct neutrino absorption by multiplying the production rate by \(e^{-\omega/T}\). What was missing was a separately coded adaptive-quadrature reference that checks both integrals mode by mode and flavor by flavor, independently of the production solver's Gauss--Legendre implementation.

By contrast, rates.compton_absorption evaluates the inverse kernel with the photon stimulation factor, while run_scan.py obtains the corresponding production rate from detailed balance. The existing test_stage1_detailed_balance.py checks B.19 at the exact-recoil fixed-target collision-integrand level, pointwise in scattering angle. That is useful, but it is not a full moving-muon thermal phase-space integral.

## 3. New independent audit

Added:
- audit_direct_collision_integrals.py
- test_direct_collision_integrals.py
- .github/workflows/direct-collision-integrals.yml

### 3.1 Neutrino channel

The new reference independently integrates
\[
\Gamma^{\rm prod}_{h,f}
=\frac{m_V^2}{24\pi\omega}
\int_{-1}^{1} dz\,W_h(z)f_1f_2,
\qquad
\Gamma^{\rm abs}_{h,f}
=\frac{m_V^2}{24\pi\omega}
\int_{-1}^{1} dz\,W_h(z)(1-f_1)(1-f_2),
\]
using adaptive quadrature rather than the production solver's Gauss--Legendre nodes. It evaluates \(\nu_\mu\) and \(\nu_\tau\) separately and retains the \(L,+,-\) modes separately.

The independent direct integrals are compared with rates.neutrino_rates at five profile radii, four masses (1, 10, 100, 200 MeV), and three energy-to-mass ratios. The balance ratio is checked independently:
\[
\Gamma^{\rm abs}_{h}/\Gamma^{\rm prod}_{h}
\stackrel{?}{=}e^{\omega/T}.
\]
The identity follows because \(E_1+E_2=\omega\) and the particle/antiparticle chemical potentials cancel. It is tested for each flavor and polarization, not only after summing.

### 3.2 Semi-Compton channel

The new audit directly evaluates both Bose factors in the published B.14--B.19 non-recoil approximation:
\[
\Gamma^{\rm prod}_{h}
=n_\mu^{\rm eff}(v\sigma_h)f_B(\omega),
\qquad
\Gamma^{\rm abs}_{h}
=n_\mu^{\rm eff}(v\sigma_h)[1+f_B(\omega)].
\]
The mode-resolved no-recoil kernel is
\[
v\sigma_h=\frac{2\alpha}{3m_\mu^2}
\left(\frac{m_V^2}{\omega^2},1,1\right).
\]
The susceptibility \(n_\mu^{\rm eff}\) is evaluated independently by adaptive momentum integration for \(\mu^-\) and \(\mu^+\). The summed production rate is separately checked against the B.14/B.16 spin-summed expression.

This validates B.19 within the stated no-recoil approximation. It does **not** validate the exact-recoil stationary-muon rate as a complete thermal rate, nor does it replace the full moving-muon B.13 integral. The exact-recoil fixed-target collision-integrand check remains separate in test_stage1_detailed_balance.py.

## 4. Acceptance criteria

1. Independent adaptive neutrino production and absorption integrals agree with rates.neutrino_rates mode by mode to relative error below \(2\times10^{-9}\) over the audit grid.
2. Neutrino detailed balance holds for each flavor and mode to relative error below \(3\times10^{-10}\).
3. Direct B.14 Compton production and absorption satisfy B.19 mode by mode to relative error below \(3\times10^{-13}\).
4. The summed B.14 Compton production integral agrees with the independently written B.14/B.16 expression to relative error below \(3\times10^{-13}\).
5. All results are archived with the triggering commit and SHA-256 fingerprints.

These are numerical regression tolerances, not astrophysical uncertainties.

## 5. Updated research order

| Priority | Task | Purpose |
|---|---|---|
| P0 | Independent neutrino forward/inverse integrals | Validate the dominant 10 MeV opacity channel |
| P0 | Direct B.14 Compton forward/inverse thermal integrals | Validate B.19 and the no-recoil normalization |
| P0 follow-up | Full moving-muon B.13 Compton thermal integral | Remove the stationary-muon/effective-density approximation |
| P1 | Local opacity at three representative \((r,\omega,m_V)\) points | Locate radial and energy regions driving any discrepancy |
| P1 | Escape probability and full Fig. 7 tail comparison | Separate microscopic opacity from transport effects |
| P2 | Switch to the finite-mixing/axial current | Only after the pure-vector literature gate passes |

## 6. Interpretation and safeguards

- A successful local detailed-balance test is necessary but not sufficient to validate the full Fig. 7 curve.
- A successful neutrino rate comparison does not validate Compton or transport.
- The 89.78% neutrino opacity fraction is a 10 MeV, source-weighted diagnostic, not a universal channel hierarchy.
- No rate rescaling, opacity multiplier, or post-hoc coupling-axis adjustment is allowed.
- The pure-vector Blinov full-curve gate remains mandatory. The finite-mixing scan remains on hold.
- This work changes internal research records only; it does not modify the referee-facing response, manuscript, or existing constraint figures.

## 7. Reproduction

From the repository root:
~~~bash
python -m unittest discover \
  -s research/stellar-cooling-constraints-20261105 \
  -p 'test_direct_collision_integrals.py' -v

python research/stellar-cooling-constraints-20261105/audit_direct_collision_integrals.py
~~~

The dedicated GitHub Actions workflow runs the repository physics test suite and archives outputs/direct_collision_integrals_2026-11-07.json.
