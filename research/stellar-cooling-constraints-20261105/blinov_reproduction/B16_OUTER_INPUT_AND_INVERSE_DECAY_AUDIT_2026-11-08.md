# B.16 outer-shell input and neutrino inverse-decay audit

**Date:** 2026-11-08  
**Scope:** completion record for steps 1 and 2 of the 22--25 km discrepancy investigation.  
**Benchmark:** \(m_V=10\) MeV, fixed-\(\omega\) Appendix-B prescription, \(R_{\max}=25\) km.  
**No production axial output or normalization was changed.**

> **Section-level profile provenance:** Section 1 and its paired outer-profile input JSON use the current 1687-row vertex-preserving profile, SHA-256 `6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`. Section 2 and its paired direct B.6 JSON use the historical 501-node uniform profile, SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`. The Section-2 algebraic kernel checks remain useful, but their sampled background points are historical. The current-profile 512-point outer-shell mode-resolved phase-space check is documented in `B16_OUTER_SHELL_POLARIZATION_RESOLVED_AUDIT_2026-11-09.md`; the cross-version impact is quantified in `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`.


## 1. Step 1 — outer-shell profile and interpolation

### 1.1 Provenance and field-by-field inputs

The current public reconstruction is not the original Garching simulation snapshot. It combines figure-level sources:

| Field | Current source / prescription | Role in B.2 |
|---|---|---|
| \(T(r)\) | Caputo et al. public SFHo-18.8 profile curve, including encoded path vertices beyond the visible frame | Enters local Fermi/Bose factors and reduced absorption |
| \(\mu_\mu(r)\) | Caputo et al. public curve; set to zero after the last encoded point where the plotted value falls below the figure's \(\sim1\) MeV resolution | Enters the muon distribution and Compton susceptibility |
| \(\mu_{\nu_\mu}(r)\) | Caputo et al. plotted branches; set to zero outside branches resolved above the plotted \(|\mu_{\nu_\mu}|\sim1\) MeV floor | Enters the inverse-decay neutrino Fermi factors |
| \(\mu_{\nu_\tau}(r)\) | Set to zero, following Blinov et al.'s explicit statement that the simulation does not provide this profile | Enters the second inverse-decay flavor |
| \(N(r)\) | Ferreira et al. lapse curve through \(r\simeq24\) km, matched to a Schwarzschild exterior through 25 km | Enters B.1 source redshift and local escape-energy threshold, **not** the fixed-\(\omega\) B.2 path opacity |

The last point matters: changing the lapse interpolation in the 22--25 km path does not directly change the B.2 opacity integral. It can affect B.1 source weights and the local lower energy threshold at the emission point. It must therefore be audited separately from \(T,\mu_\mu,\mu_{\nu_\mu}\).

The Garching archive access record remains unresolved: the public archive lists relevant Bollig/Hüdepohl radial-profile collections, but the protected endpoint requires authorization and the exact s18.8-SFHo-MUONS, \(t_{\rm pb}=1\) s file inventory has not yet been confirmed. The reconstructed profile must not be described as raw simulation data.

### 1.2 Interpolation comparison

The uniform 0.05 km base grid contributes 61 nodes in this shell, but the complete vertex-preserving CSV has 222 nodes in 22--25 km (61 base nodes plus 161 retained PDF/support nodes). The minimum spacing is 6.78e-7 km, reflecting intentional near-step support-boundary knots; the maximum spacing remains 0.05 km. The existing composite opacity grid contains only 9 nodes in this shell, with maximum spacing 0.680 km.

Comparing interpolation from the composite grid against direct interpolation of the full vertex-preserving public-figure reconstruction gives:

| Field | Maximum absolute error | Maximum relative error where meaningful |
|---|---:|---:|
| \(T\) | 0.00426 MeV | 0.122% |
| \(N\) | \(3.61\times10^{-5}\) | 0.00396% |
| \(\mu_\mu\) | 2.63 MeV | 9.50% |
| \(\mu_{\nu_\mu}\) | 0 | not applicable in 22--25 km |

The large relative \(\mu_\mu\) error occurs close to the imposed low-value cutoff near 22.2 km. It does not translate into a significant total opacity error: in this shell the peak reduced Compton opacity is only \(1.35\times10^{-15}\) of the peak neutrino reduced opacity.

For the neutrino reduced absorption itself, coarse-versus-dense interpolation gives a maximum relative error of \(8.37\times10^{-4}\) and an RMS relative error of \(2.52\times10^{-4}\), above the \(10^{-12}\)-of-peak rate floor. The total reduced absorption has the same result because the neutrino channel dominates.

### 1.3 Direct 22--25 km optical-depth comparison

Holding the B.1 source fixed and integrating the outer shell directly in the radial coordinate \(r'\), with
\[
ds=\frac{r'}{\sqrt{r'^2-b^2}}\,dr',
\]
the dense 0.05 km profile changes the source-weighted outer-shell mean optical depth by only \(1.23\times10^{-5}\) relative to the composite-grid interpolation.

For the strong endpoint \(g=4.17169\times10^{-8}\), the outer-shell escape factor changes from 0.150413343 to 0.150412262, i.e. \(-7.18\times10^{-6}\) relative. The 8--10, 10--12, and 12--15 km emission-shell subsets show similarly tiny changes in their 22--25 km optical depths.

A separate path-grid refinement from the baseline composite nodes to uniform 0.025 km spacing changes the strong-endpoint full luminosity by \(+0.1775\%\). This is below the independent combined quadrature-convergence envelope of 0.294%.

### 1.4 Figure-floor sensitivity for \(\mu_{\nu_\mu}\)

The baseline takes \(\mu_{\nu_\mu}=0\) in 22--25 km because no resolved branch is present there. Replacing this by \(|\mu_{\nu_\mu}|=1\) MeV throughout the shell, with all other inputs held fixed, changes the outer-shell escape factor by:

- Fig. 7 peak: \(+1.33\times10^{-4}\);
- strong endpoint: \(+4.94\times10^{-4}\).

Thus the unresolved figure-floor convention is not large enough to explain the strong-endpoint discrepancy.

### 1.5 Step-1 conclusion

The tests rule out **numerical interpolation or the plotted \(\mu_{\nu_\mu}\) floor in 22--25 km** as the source of the order-one high-coupling mismatch. The outer lapse is not part of fixed-\(\omega\) B.2 opacity. The muon chemical-potential interpolation has a visibly larger pointwise fractional error near its cutoff, but its Compton contribution is negligible for this 10 MeV benchmark.

This does **not** settle the physical-background uncertainty: the profile remains a reconstruction from public figures rather than the exact Garching snapshot. That provenance limitation is separate from the interpolation error and cannot be cured by increasing quadrature order.

## 2. Step 2 — independent inverse-neutrino-decay absorption

### 2.1 Equation-number correction

The requested equations need to be assigned to the correct channels:

- **B.6** is the inverse-neutrino-decay production phase-space integral.
- **B.10**, not B.19, is the detailed-balance relation for inverse neutrino decay:
  \[
  \Gamma_{\nu\bar\nu\to V}^{\rm prod}
  =e^{-\omega/T}\Gamma_{V\to\nu\bar\nu}^{\rm abs}.
  \]
- **B.4** defines the reduced absorption rate:
  \[
  \Gamma_{\rm abs}^{*}
  =(1-e^{-\omega/T})\Gamma_{\rm abs}.
  \]
  Combining B.4 and B.10 gives
  \[
  \boxed{\Gamma_{\rm abs}^{*}
  =(e^{\omega/T}-1)\Gamma_{\rm prod}.}
  \]
- **B.19 is the Compton-channel detailed-balance relation**, not the inverse-neutrino-decay relation. It is checked separately for the Compton production component.

This distinction is essential; B.19 must not be cited as the neutrino inverse-decay balance equation.

### 2.2 Independent phase-space evaluation

The B.6 two-body phase-space integral was reduced using its on-shell delta function to the daughter-pair angular integral and evaluated directly with 192-point Gauss-Legendre quadrature. This is independent of the logarithmic antiderivative used in reference.py.

For one neutrino flavor,
\[
E_{1,2}=\frac{\omega}{2}(1\pm v_V z),
\]
and the direct production and inverse-absorption angular integrals use, respectively,
\[
f_{\bar\nu}(E_1;-\mu_\nu)f_\nu(E_2;\mu_\nu),
\qquad
[1-f_{\bar\nu}(E_1;-\mu_\nu)]
[1-f_\nu(E_2;\mu_\nu)].
\]
The identity \(E_1+E_2=\omega\) gives the detailed-balance ratio \(e^{-\omega/T}\) pointwise in the angular integrand.

The audit samples \(r=8,10,12,15,17,18,22,23,24,25\) km and \(\omega=10.25,10.5,12,15,20,30,50,100\) MeV. The two active flavors are evaluated separately, with \(\mu_{\nu_\tau}=0\) as in the published profile treatment.

### 2.3 Numerical results

| Check | Maximum relative residual |
|---|---:|
| Direct B.6 angular integral vs analytic Fermi-pair integral, \(\nu_\mu\) | \(4.41\times10^{-14}\) |
| Direct B.6 angular integral vs analytic Fermi-pair integral, \(\nu_\tau\) | \(5.12\times10^{-14}\) |
| Direct B.6 two-flavor production vs current reference implementation | \(4.76\times10^{-14}\) |
| Direct inverse integral vs B.10 absorption | \(1.82\times10^{-15}\) |
| Two equivalent B.4 reduced-absorption forms | \(1.82\times10^{-15}\) |
| B.4 reduced neutrino rate vs current implementation | \(4.77\times10^{-14}\) |
| Maximum absolute logarithmic B.10 residual, either flavor | \(3.55\times10^{-15}\) |

For the 22--25 km subset, the maximum relative difference between the direct B.6 two-flavor production integral and the current code is \(6.58\times10^{-15}\). The maximum absolute logarithmic detailed-balance residual is \(3.55\times10^{-15}\).

The Compton identity was checked separately: the B.19 absorption/production ratio is exact at the stored precision, and its B.4 reduced-rate form agrees to \(3.79\times10^{-16}\). This is an algebraic detailed-balance check of the Compton component; it is not a claim that the full moving-muon Compton thermal phase-space integral has been independently reproduced here.

### 2.4 Step-2 conclusion

The independent angular phase-space calculation finds no normalization, Fermi-blocking, chemical-potential-sign, or detailed-balance discrepancy in the 10 MeV inverse-neutrino-decay kernel. In particular, the 22--25 km neutrino absorption rate is not being underestimated by the existing analytic Fermi-pair expression relative to the direct B.6 integral.

The current evidence therefore shifts attention away from the local neutrino inverse-decay formula and toward the angular/path-resolved accumulation of opacity for vectors emitted in the 8--15 km source region, while retaining the unresolved exact-background provenance as a distinct limitation.

## 3. Reproducibility

- Outer input audit: audit_b16_outer_profile_inputs.py
- Outer path-grid audit: audit_b16_outer_profile_interpolation.py
- Inverse-decay audit: audit_b16_neutrino_inverse_decay.py
- Outer-input machine result: outputs/b16_outer_profile_inputs_10mev_2026-11-08.json
- Path-grid machine result: outputs/b16_outer_profile_interpolation_10mev_2026-11-08.json
- Inverse-decay machine result: outputs/b16_neutrino_inverse_decay_10mev_2026-11-08.json
- Successful outer-input workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42450499283
- Successful inverse-decay workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42450822390
- Successful outer path-grid workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42479382380

All changes remain confined to the research branch and audit records. No production axial output, Fig. 7 normalization, or physical opacity rescaling is changed.
