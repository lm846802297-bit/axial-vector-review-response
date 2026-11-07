# Finite-mixing vector--axial stellar-cooling constraints

**Status (2026-11-07): UV coupling map and amplitude-level mixed Compton/dimuon kernels are implemented and endpoint-tested. The published Blinov version-of-record equations have now been audited directly. No mixed-current luminosity scan or exclusion curve has been produced; the pure-vector literature gate remains blocked pending a full Fig. 7 match.**

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

The current state is **BLOCKED**; see VECTOR_ENDPOINT_GATE_2026-11-07.md. A one-factor Ferreira-μ_mu profile swap does not solve the 10 MeV full-curve mismatch; it worsens the overall residual. The baseline Caputo μ_mu profile is independently density-anchored, while the exact source simulation profile is not publicly retrievable in the current audit. In brief:

- The archived independent scalar Appendix-B calculation reproduces four digitized Fig. 4 contour points within 2.60%, but does not reproduce the full Fig. 7 luminosity curve at 10 MeV (91.35% maximum and 15.64% mean absolute relative residual).
- The current mode-resolved vector scan closes at 259.08--259.14 MeV, while the archived digitized Fig. 4 contour ends near 210.98 MeV.
- The two implementations differ in more than one ingredient. No fitted rescaling or arbitrary opacity multiplier is permitted.
- A visual cross-check finds the published version-of-record Fig. 4 and Fig. 7 visually unchanged relative to arXiv v2. The archived numeric vertices are still the arXiv extraction; exact path-level re-digitization from the published PDF remains pending.

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


## 5. Published-vector validation is a two-lane gate

The direct equation-level audit of the published JHEP version is recorded in [VECTOR_ENDPOINT_GATE_2026-11-07.md](VECTOR_ENDPOINT_GATE_2026-11-07.md). It distinguishes:

- **Lane A, literal reproduction:** reproduce Blinov's polarization-summed Appendix-B rates and scalar escape prescription, including the full Fig. 7 luminosity curves and Fig. 4 boundaries. This is the required external pure-vector benchmark.
- **Lane B, mode-resolved transport:** retain the physical polarization-resolved rates and propagate each mode with its own opacity. Quantify its relation to Lane A rather than assuming that a polarization sum can be exponentiated as a single-particle opacity.

The two lanes must not be silently mixed. A contour crossing alone is insufficient; the complete luminosity-versus-coupling curves, particularly the 10 MeV trapping tail, must pass the documented tolerance. The finite-mixing UV scan remains on hold until the vector benchmark is reconciled and the transport prescription is fixed. No rescaling factor or fitted opacity normalization is permitted.

## 6. Revised priority: independent microscopic rates before transport tuning

The 10 MeV three-layer diagnostic assigns about 89.78% of the source-weighted mean reduced optical depth to neutrino inverse decay and 10.22% to inverse Compton. This is a benchmark-specific weighted decomposition, not a universal fraction.

The next P0 task is therefore an independent forward/reverse collision-integral audit, not a Compton normalization adjustment:

1. Neutrino channel: independently integrate both \(f_1f_2\) and \((1-f_1)(1-f_2)\) with adaptive quadrature, separately for \(\nu_\mu\), \(\nu_\tau\), and each \(L,+,-\) mode. Compare with the existing Gauss--Legendre implementation and test \(\Gamma_{\rm abs}/\Gamma_{\rm prod}=e^{\omega/T}\).
2. Semi-Compton channel: independently integrate the forward \(f_\gamma\) and inverse \(1+f_\gamma\) thermal factors in the published B.14--B.19 no-recoil approximation, and compare the summed normalization with B.14/B.16. Keep this distinct from the full moving-muon B.13 integral.
3. Only after both local-rate audits pass, inspect local opacity at representative radii/energies, then the escape probability and full Fig. 7 tail.

The implementation and acceptance criteria are recorded in [DIRECT_COLLISION_INTEGRAL_AUDIT_2026-11-07.md](../DIRECT_COLLISION_INTEGRAL_AUDIT_2026-11-07.md). The independent audit is implemented in [audit_direct_collision_integrals.py](../audit_direct_collision_integrals.py), with regressions in [test_direct_collision_integrals.py](../test_direct_collision_integrals.py). The dedicated workflow archives the JSON output.

The existing neutrino production code already evaluates production and absorption with separate Fermi factors; the new work supplies an independent adaptive-quadrature reference. The current Compton production scan still derives production from detailed balance, so the new direct B.14 thermal integral is a distinct cross-check. Neither local test substitutes for the still-required full Blinov pure-vector Fig. 7 validation. No mixed-current luminosity scan is authorized while that vector gate remains blocked.

## 7. Vector-to-axial response mapping: no assumed global rescale

The new derivation and acceptance criterion are recorded in [VECTOR_TO_AXIAL_RESPONSE_MAPPING_2026-11-07.md](VECTOR_TO_AXIAL_RESPONSE_MAPPING_2026-11-07.md).

**No Garching raw profile is required for the analytic or local-kernel response study.** The first task is to compare unit-coupling vector and axial response kernels using the existing amplitude-level code in rates.py. Do not duplicate the Dirac-trace implementation.

A universal coupling rescale is admissible only if the same constant relates production and inverse absorption for every relevant reaction channel, polarization, kinematic point, and thermally integrated response, and if it preserves the UV model's unchanged neutrino current. In this model the active-neutrino couplings remain +gX and -gX as theta_muR varies, while the charged-muon current changes. Therefore a rescaling inferred from muon Compton alone does not generally preserve the neutrino contribution to total emissivity or opacity.

The muon semi-Compton vector and axial traces are not assumed proportional; their ratio must be tested over mediator mass, energy, angle, and L,+,- modes. Above dimuon threshold, the vector and axial widths also have different beta factors (beta versus beta^3), so their ratio is mass dependent.

Execution:
1. Audit the existing pure vector/axial Compton endpoint kernels, Ward identity, and mixed interference.
2. Tabulate the mode-resolved unit-coupling Compton response ratio over a kinematic grid.
3. Compare pure vector and axial dimuon rates above threshold.
4. Keep neutrino rates fixed at gX and determine whether any common mapping survives the full channel sum.
5. Only then decide whether a simple rescale is justified or a channel-resolved mixed transport calculation is required.

No axial luminosity or exclusion curve is generated at this stage. The pure-vector Fig. 7 mismatch remains a separate limitation on any final astrophysical exclusion claim.

## 8. First numerical response scan implementation

Added [response_scan.py](response_scan.py), [test_response_scan.py](test_response_scan.py), and the dedicated [GitHub Actions workflow](../../../.github/workflows/vector-axial-response-scan.yml).

The scan reuses the existing Dirac-trace and decay-rate routines in the parent rates.py module. It covers:
- 5 mediator masses and 5 energy-to-mass ratios for semi-Compton;
- 19 scattering angles and all three physical mediator polarizations for differential response ratios;
- angle-integrated v*sigma response ratios for each polarization;
- the UV finite-mixing benchmark at theta_muR=10^-2, retaining amplitude-level vector--axial interference with the physical g_A convention;
- 9 dimuon masses from immediately above threshold to 5 times threshold, including mode-resolved thermal production/absorption ratios and the analytic vacuum-width ratio.

**Validation status:** source, tests, and CI workflow are committed; the workflow result has not yet been retrieved/verified. Do not describe the numerical scan as passed until the Actions job completes and its JSON artifact is inspected. The scan is a local-kernel comparison only. It does not validate stellar transport, the Blinov pure-vector Fig. 7 benchmark, or an axial exclusion curve.

## 9. Extended mode-resolved response output

The response scan now stores the angle-resolved arrays (not only summary statistics) for each of the three mediator polarizations. It also performs the finite-mixing calculation after angular integration, using the mixed-current amplitude rather than adding the pure-vector and pure-axial rates incoherently.

For the dimuon channel, the scan now records:
- pure axial/vector thermal production and absorption ratios;
- finite-mixing production/vector and absorption/vector ratios;
- the interference fraction in production and absorption, mode by mode;
- the analytic vacuum-width ratio
  \[
  \frac{\Gamma_A}{\Gamma_V}
  =\frac{\beta_\mu^2}{1+2m_\mu^2/m_{A'}^2},
  \qquad
  \beta_\mu=\sqrt{1-\frac{4m_\mu^2}{m_{A'}^2}}.
  \]

The new regression tests check that the raw angle arrays are preserved and that finite-mixing observables are present for all three polarizations. These tests complement, but do not replace, the existing pure-vector/pure-axial endpoint tests in `test_mixed_rates.py`.

**Important interpretation:** the finite-mixing rates are local microscopic response functions. They do not include the unchanged active-neutrino channel, radial profile integration, reduced opacity, escape probability, or gravitational redshift. They cannot be converted directly into a supernova luminosity or exclusion curve.

## 10. First executed numerical results (2026-11-07)

The dedicated workflow completed successfully after switching the JSON archival method from Actions artifacts (the repository had exhausted its artifact-storage quota) to a deterministic commit on this research branch.

- Workflow: [Run #42329656102](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42329656102)
- Result: 22/22 finite-mixing and response-scan tests passed; the numerical scan completed and its JSON output was committed.
- Machine-readable output: [vector_axial_response_scan.json](outputs/vector_axial_response_scan.json)

Representative unit-coupling semi-Compton results (polarization-summed angular-integrated ratio, axial/vector) are:

| m (MeV) | E/m | L ratio | each transverse ratio | polarization-summed ratio |
|---:|---:|---:|---:|---:|
| 0.01 | 1.001 | 2.012 | 2.002 | 2.005 |
| 0.01 | 10 | 39669 | 2.989 | 200.517 |
| 1 | 1.001 | 2.002 | 1.993 | 1.996 |
| 1 | 10 | 29256 | 2.885 | 160.742 |
| 10 | 1.001 | 1.920 | 1.912 | 1.914 |
| 10 | 10 | 5048 | 2.115 | 40.898 |
| 100 | 1.001 | 1.420 | 1.418 | 1.419 |
| 100 | 10 | 62.53 | 1.212 | 2.405 |

The large longitudinal ratios at high E/m arise because the vector current is conserved (its longitudinal amplitude is Ward-suppressed), whereas the axial current is not conserved for a massive muon. This is precisely why a single polarization-independent, kinematics-independent rescaling is not justified by these kernels. The table is a local fixed-muon-rest-frame kernel result; it is not yet a thermal supernova production or transport result.

For the finite-mixing benchmark theta_muR=10^-2, the polarization-summed mixed/vector response is nearly the axial/vector response because |g_V/g_A|=tan^2(theta_muR) is about 10^-4. The scan nevertheless evaluates the full mixed amplitude. The maximum absolute Compton interference fraction in the sampled differential grid is about 1.97e-4.

For dimuon decay, the analytic pure-current vacuum-width ratio is
Gamma_A/Gamma_V = beta_mu^2/(1+2 m_mu^2/m_A'^2). It rises from 1.3332e-4 at m_A'/(2m_mu)=1.0001 to 0.94118 at m_A'/(2m_mu)=5. The finite-mixing thermal rates show the same threshold dependence to the displayed precision; the mode-resolved interference remains explicitly included and is largest close to threshold (about 3.94e-5 in magnitude for the chosen benchmark).

**What has and has not been validated:** the pure-vector and pure-axial endpoints agree with their existing rate kernels in the 22 passing tests; the mixed-current Ward and detailed-balance tests also pass. This validates internal kernel consistency and the numerical scan execution. It does **not** yet demonstrate that the full pure-vector stellar luminosity curve reproduces Blinov Fig. 7, nor does it justify rescaling the published vector supernova exclusion into an axial or finite-mixing exclusion. The next required physics step is to use these response results to build and independently check the channel-resolved thermal rates before any stellar transport calculation.



## 11. Full dimuon mediator-momentum thermal integral: first implementation

A new isolated module is added at [thermal_integrals/dimuon.py](thermal_integrals/dimuon.py). It reuses the existing exact mode-resolved `charged_muon_decay_rates_mixed` kernel and integrates over the full mediator momentum magnitude,
\[
Q_h=\frac{1}{2\pi^2}\int_0^\infty dk\,k^2\omega\,
\Gamma^{\rm prod}_{h}(\omega),\qquad
\omega=\sqrt{k^2+m_{A'}^2}.
\]
It retains the inverse absorption rate as a differential function of mediator energy and polarization, which is the quantity required by the optical-depth calculation. It does **not** integrate \(\Gamma_{\rm abs}\) over mediator phase space: that integral is not a finite emissivity or a physical total absorption rate. The semi-infinite momentum range for the production emissivity is mapped to a finite interval with Gauss--Legendre quadrature. The channel is exactly zero at and below \(m_{A'}=2m_\mu\).

The new test module checks threshold closure, pointwise production/absorption detailed balance, pure-current nonzero limits, positivity/finite output for a mixed-current benchmark, and quadrature convergence. This is the first implementation of the dimuon momentum integral; it is not yet a validated result until the dedicated Actions run passes and the order-convergence output is inspected.

The moving-muon semi-Compton integral remains a separate next implementation. The stationary-target kernel is not silently promoted to the full thermal result. No transport scan, cooling curve, manuscript edit, or referee-response edit is included.
