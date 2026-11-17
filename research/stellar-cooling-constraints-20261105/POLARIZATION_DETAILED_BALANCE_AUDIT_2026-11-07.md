# Blinov Appendix B.7–B.19: polarization-resolved rates and code audit

**Date:** 2026-11-07  
**Scope:** Stage 1 only. This note derives polarization-resolved production/absorption rates for the vector benchmark and compares them with the existing Python implementation. It does not alter production code, transport normalization, saved scans, the manuscript, or the referee response.

> **Historical stage record (2026-11-15):** The direct forward/reverse integral sub-block was subsequently checked in `DIRECT_COLLISION_INTEGRAL_AUDIT_2026-11-07.md`. This note remains the detailed polarization-convention record; it does not close the B.2 scalar-opacity ambiguity or the moving-muon thermal B.13 integral. PR #56 later merged on 2026-11-12. See `AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md` for the later benchmark status.

Primary source: [Blinov et al., arXiv:2511.09619v2](https://arxiv.org/abs/2511.09619), Appendix B, especially Eqs. (B.2), (B.4), and (B.6)–(B.19).

## 1. Conventions

Work in the local medium rest frame and choose the emitted vector momentum along $+z$:
\[
q^\mu=(\omega,0,0,k),\qquad k=\sqrt{\omega^2-m_V^2},\qquad v_V=k/\omega.
\]
The physical vector modes are $h=L,+,-$. All rates below are for unit $g_X^2$; multiply by $g_X^2$ for the physical rate. We use
\[
\alpha_V=\frac{g_X^2}{4\pi}.
\]
The labels $+,-$ depend on the circular-polarization and daughter-particle conventions. Interchanging those labels does not change a polarization-summed observable, but the convention must be fixed when comparing individual helicity rates.

For every reaction, the distinction is:
- $\Gamma_h^{\rm prod}$: production rate into a specified final vector mode $h$;
- $\Gamma_h^{\rm abs}$: inverse absorption rate for an incident vector in mode $h$;
- $\Gamma_h^*=(1-e^{-\omega/T})\Gamma_h^{\rm abs}$: reduced opacity entering the linearized Boltzmann attenuation term.

The detailed-balance relation is mode-by-mode:
\[
\boxed{\Gamma_h^{\rm prod}=e^{-\omega/T}\Gamma_h^{\rm abs}},
\qquad
\boxed{\Gamma_h^*=\Gamma_h^{\rm abs}-\Gamma_h^{\rm prod}}.
\]
The energy in these factors is the **vector energy** $\omega$, not the outgoing photon energy in the Compton process.

This follows directly from the equilibrium identities
\[
\frac{f_F(E,\mu)}{1-f_F(E,\mu)}=e^{-(E-\mu)/T},
\qquad
\frac{f_B(E)}{1+f_B(E)}=e^{-E/T},
\]
together with energy conservation. Since the relation holds pointwise in phase space, it remains true after integration for each fixed vector polarization, provided the forward and inverse collision integrals use the same phase-space and polarization conventions.

## 2. Inverse neutrino decay: Eqs. (B.6)–(B.10)

### 2.1 Mode-resolved production

For one active neutrino flavor, let $z=\cos\theta^*$ be the angle of the first daughter in the vector rest frame relative to the boost direction. The daughter energies in the medium frame are
\[
E_{1,2}=\frac{\omega}{2}(1\pm v_V z).
\]
For a chiral neutrino current, the normalized angular weights in the convention used by `rates.neutrino_rates` are
\[
W_L(z)=\frac34(1-z^2),\qquad
W_+(z)=\frac38(1+z)^2,\qquad
W_-(z)=\frac38(1-z)^2.
\]
They follow from the spin-1 helicity amplitudes: \(W_h=(3/2)|d^1_{h,\Delta\lambda}(\theta)|^2\), with \(|\Delta\lambda|=1\). The sign assignment of the two transverse weights depends on which chiral daughter is called particle 1.
Each mode is normalized separately:
\[
\int_{-1}^{1}dz\,W_h(z)=1,
\qquad
W_L(z)+W_+(z)+W_-(z)=\frac32.
\]
The mode-resolved production rate is therefore
\[
\Gamma_{h,\nu\bar\nu}^{\rm prod}(\omega)
=\frac{m_V}{\omega}\,\Gamma_{V\to\nu\bar\nu}^{(1)}
\int_{-1}^{1}dz\,W_h(z)
 f_\nu(E_1;\mu_\nu)f_{\bar\nu}(E_2;-\mu_\nu),
\]
where the vacuum width for **one flavor and one fixed vector polarization** is
\[
\Gamma_{V\to\nu\bar\nu}^{(1)}=\frac{g_X^2m_V}{24\pi}.
\]
Vacuum rotational invariance makes the width equal for each fixed polarization. The polarization average in the conventional unpolarized vacuum width is thus not an additional factor in a fixed-$h$ rate.

Define the uniform angular average used in the scalar expression by
\[
I(\mu_\nu/T,\omega/T,v_V)
=\frac12\int_{-1}^{1}dz\,
 f_\nu(E_1;\mu_\nu)f_{\bar\nu}(E_2;-\mu_\nu).
\]
Using the sum of the three weights gives
\[
\sum_h\Gamma_{h,\nu\bar\nu}^{\rm prod}
=3\frac{m_V}{\omega}\Gamma_{V\to\nu\bar\nu}^{(1)} I.
\]
This is precisely the origin of the explicit factor 3 in Blinov Eq. (B.7): the vacuum width is averaged over the three initial vector polarizations, whereas the thermal production expression is summed over the three final vector polarizations. The paper applies this formula separately to $\nu_\mu$ and $\nu_\tau$, with their respective chemical potentials.

### 2.2 Mode-resolved absorption and detailed balance

For fixed $h$, replace the two Fermi occupation factors in the production integral by final-state blocking factors:
\[
\Gamma_{h,\nu\bar\nu}^{\rm abs}
=\frac{m_V}{\omega}\Gamma_{V\to\nu\bar\nu}^{(1)}
\int_{-1}^{1}dz\,W_h(z)
[1-f_\nu(E_1;\mu_\nu)]
[1-f_{\bar\nu}(E_2;-\mu_\nu)].
\]
Since $E_1+E_2=\omega$, the chemical potentials cancel:
\[
\frac{f_\nu(E_1;\mu_\nu)f_{\bar\nu}(E_2;-\mu_\nu)}
{[1-f_\nu(E_1;\mu_\nu)][1-f_{\bar\nu}(E_2;-\mu_\nu)]}
=e^{-\omega/T}.
\]
Consequently,
\[
\Gamma_{h,\nu\bar\nu}^{\rm prod}
=e^{-\omega/T}\Gamma_{h,\nu\bar\nu}^{\rm abs}
\]
for each $h$, and summing over $h$ gives the scalar relation in Eq. (B.10).

**Helicity convention:** B.6 writes the antineutrino as daughter 1, while the current code writes the neutrino as daughter 1. This is the change \(z\to-z\), which interchanges the labels \(+\leftrightarrow-\). The longitudinal rate and polarization sum are unchanged. At nonzero neutrino chemical potential the two circular-mode rates need not be equal, so this label swap must be kept explicit in a mode-by-mode comparison.

### 2.3 Code comparison

- `rates.neutrino_rates` implements the three $W_h$ weights, exact two-body kinematics, Fermi occupation factors and Pauli blocking. It sums the two active flavors separately.
- The prefactor $m_V^2/(24\pi\omega)$ is the time-dilated one-flavor fixed-polarization vacuum width at unit coupling.
- `vector_reference.summed_decay_production` independently evaluates the scalar Fermi-pair integral corresponding to Eq. (B.7)/(B.9).
- Existing tests cover the mode-by-mode detailed-balance identity and the unequal circular-mode rates at nonzero chemical potential (`test_rates.py::test_neutrino_detailed_balance_and_circular_modes)); the total mode sum is compared with the independent scalar integral (`test_vector_reference.py::test_spin_sums_against_blinov_closed_form`).

**Assessment:** the current neutrino implementation is consistent with the mode-resolved decomposition of B.6–B.10. The total-rate comparison alone would not have established this; the per-mode balance test is also needed.

## 3. Inverse dimuon decay: Eqs. (B.11)–(B.12)

This channel is open for $m_V>2m_\mu$. Define
\[
\beta_\mu=\sqrt{1-\frac{4m_\mu^2}{m_V^2}},
\qquad u=v_V\beta_\mu,
\qquad E_{1,2}=\frac{\omega}{2}(1\pm u z).
\]
For the vector current used in the Blinov benchmark, the vacuum width into both muon chiralities is
\[
\Gamma_{V\to\mu^+\mu^-}
=\frac{g_X^2m_V}{12\pi}
\left(1+\frac{2m_\mu^2}{m_V^2}\right)\beta_\mu,
\]
which is Eq. (B.12) after using $\alpha_V=g_X^2/(4\pi)$.  This unpolarized width equals the width of each fixed polarization in vacuum.

The normalized angular weights for the three fixed vector modes are
\[
W_L^\mu(z)=
\frac{1-\beta_\mu^2z^2}{2(1-\beta_\mu^2/3)},
\]
\[
W_+^\mu(z)=W_-^\mu(z)=
\frac{1-\frac12\beta_\mu^2(1-z^2)}
{2(1-\beta_\mu^2/3)}.
\]
They obey
\[
\int_{-1}^{1}dz\,W_h^\mu(z)=1,
\qquad
\sum_hW_h^\mu(z)=\frac32.
\]
Thus
\[
\Gamma_{h,\mu^+\mu^-}^{\rm prod}
=\frac{m_V}{\omega}\Gamma_{V\to\mu^+\mu^-}
\int_{-1}^{1}dz\,W_h^\mu(z)
 f_{\mu^-}(E_1;\mu_\mu)f_{\mu^+}(E_2;-\mu_\mu).
\]
Summing over $h$ yields the factor 3 in Eq. (B.11), with the argument $u=v_V\beta_\mu$ in the same Fermi-pair integral $I$.

Replacing $ff$ by $(1-f)(1-f)$ gives the absorption rate. Since $E_1+E_2=\omega$, the same mode-by-mode detailed-balance identity follows:
\[
\Gamma_{h,\mu^+\mu^-}^{\rm prod}
=e^{-\omega/T}\Gamma_{h,\mu^+\mu^-}^{\rm abs}.
\]

### Code comparison

- `rates.charged_muon_decay_rates(current="vector")` uses the exact vector vacuum width and the $W_L^\mu,W_T^\mu$ angular weights above.
- The code retains the finite $m_\mu$ threshold and Fermi blocking.
- `test_rates.py::test_dimuon_angular_weights_from_dirac_trace` compares the longitudinal/transverse angular tensors with an explicit Dirac trace.
- `test_rates.py::test_charged_muon_decay_width_and_balance` checks the vacuum width and detailed balance mode by mode.
- `test_vector_reference.py::test_spin_sums_against_blinov_closed_form` checks the total rate against the independent B.11 scalar expression.

**Assessment:** the vector-current dimuon implementation is consistent with B.11–B.12, including the per-mode decomposition. The axial-current branch in the same function is a separate extension and is not part of this Blinov vector benchmark.

## 4. Semi-Compton scattering: Eqs. (B.13)–(B.19)

### 4.1 Mode-resolved collision integrals

For production into a specified final vector polarization $h$, the collision integral is
\[
\Gamma_{h,\mu\gamma\to\mu V}^{\rm prod}(\omega)
=\frac{1}{2\omega}\int d\Pi_{p_1}d\Pi_{p_2}d\Pi_k
(2\pi)^4\delta^4(p_1+k-p_2-q)
\sum_{s_\mu,s'_\mu,\lambda_\gamma}
|\mathcal M_h|^2
f_\mu(E_1;\mu_\mu)f_\gamma(E_\gamma)
[1-f_\mu(E_2;\mu_\mu)].
\]
Here $h$ is fixed; the sum is over muon spin states and the photon polarization states. The inverse process has a fixed incident vector polarization $h$, with the same matrix element by crossing. Its final-state photon polarization is summed.

At the integrand level,
\[
\frac{f_\mu(E_1)f_\gamma(E_\gamma)[1-f_\mu(E_2)]}
{[1-f_\mu(E_1)][1+f_\gamma(E_\gamma)]f_\mu(E_2)}
=e^{-(E_1+E_\gamma-E_2)/T}
=e^{-\omega/T}.
\]
Therefore B.19 also holds for each fixed $h$, not only after summing the three vector polarizations:
\[
\boxed{\Gamma_{h,\mu\gamma\to\mu V}^{\rm prod}
=e^{-\omega/T}\Gamma_{h,\mu V\to\mu\gamma}^{\rm abs}}.
\]

### 4.1.1 Independent B.19 collision-integrand regression

A new regression test evaluates the **actual mode-resolved matrix elements** from `rates.compton_matrix_elements` at three $(m_V,\omega)$ benchmarks and several scattering angles. It uses exact two-body recoil in the fixed-target inverse kinematics, obtains the outgoing muon energy from energy conservation, and multiplies the same $|\mathcal M_h|^2$ by the forward and inverse Fermi/Bose statistical factors. The ratio is checked separately for $h=L,+,-$ and for both signs of the muon chemical potential.

This is a pointwise collision-integrand test of B.19. It is **not** a full moving-muon thermal phase-space integration and does not remove the effective-density approximation in the production scan. See `test_stage1_detailed_balance.py::test_b19_collision_integrand_balance_for_each_vector_mode`.

### 4.2 How B.14–B.18 encode polarization sums

The non-relativistic-muon, negligible-recoil production cross section printed in B.14 is
\[
\sigma(\mu\gamma\to\mu V)\simeq
\frac{8\pi\alpha\alpha_V}{3m_\mu^2}
\left(1+\frac{m_V^2}{2\omega^2}\right)v_V.
\]
It is a polarization-summed production cross section with the conventional initial-state spin averages.

Let $\sigma_h^{\rm inv}$ be the inverse cross section for a fixed incident vector mode $h$, averaged over the initial muon spin and summed over final muon spin and photon polarization. Define the unpolarized inverse cross section by
\[
\sigma_{\rm inv}^{\rm unpol}=\frac13\sum_h\sigma_h^{\rm inv}.
\]
In the non-relativistic-muon, negligible-recoil approximation used to obtain B.15–B.18, $E_\gamma\simeq\omega$, and
\[
\Gamma_{h}^{\rm prod}
=\frac{n_\mu F_{\rm deg}}{e^{\omega/T}-1}
v_V\sigma_h^{\rm inv}.
\]
Summing over $h$ gives
\[
\sum_h\Gamma_h^{\rm prod}
=\frac{n_\mu F_{\rm deg}}{e^{\omega/T}-1}
3v_V\sigma_{\rm inv}^{\rm unpol},
\]
which is B.15. The factor 3 is the average over the three incident vector polarizations undone when the final vector polarization is summed in the production rate.

B.18 states
\[
\frac{\sigma(\mu\gamma\to\mu V)}
{\sigma(\mu V\to\mu\gamma)}
=\frac32v_V^2.
\]
The factor $3/2$ is the ratio of the vector and photon spin degeneracies; $v_V^2$ is the two-body phase-space factor. The initial photon-spin average in the cross section must be undone in the thermal rate, giving the explicit factor 2 in B.16:
\[
\sum_h\Gamma_h^{\rm prod}
=\frac{n_\mu F_{\rm deg}}{v_V}
\frac{2}{e^{\omega/T}-1}
\sigma(\mu\gamma\to\mu V).
\]
Thus B.15 and B.16 are total vector-polarization-summed production rates. They do not by themselves specify the three individual $\sigma_h^{\rm inv}$.

### 4.3 Per-mode Thomson limit

For a conserved vector muon current, the no-recoil Thomson limit of the inverse kernel resolves into
\[
v_V\sigma_L^{\rm inv}
=\frac{2\alpha}{3m_\mu^2}\frac{m_V^2}{\omega^2},
\qquad
v_V\sigma_+^{\rm inv}
=v_V\sigma_-^{\rm inv}
=\frac{2\alpha}{3m_\mu^2}.
\]
Consequently,
\[
v_V\sum_h\sigma_h^{\rm inv}
=\frac{2\alpha}{3m_\mu^2}
\left(2+\frac{m_V^2}{\omega^2}\right),
\]
which, inserted into the mode-resolved thermal rate above, reproduces B.14–B.16. In particular, the longitudinal inverse cross section is suppressed as $m_V^2/\omega^2$ in the light-vector limit; it is not equal to either transverse mode.

### 4.4 Code comparison and approximation boundary

- `rates.compton_matrix_elements` evaluates the crossed inverse amplitude for a **fixed incident vector polarization** and sums the final photon polarizations. The initial muon spin is averaged in the trace.
- `rates.compton_kernels` integrates the two-body inverse cross section separately for $L,+,-$, returning the angle-resolved $v_Vd\sigma_h^{\rm inv}$ weights.
- `rates.compton_absorption` multiplies these weights by an effective muon susceptibility density and the final-state photon stimulation factor. It returns three separate absorption rates.
- `run_scan.py` forms the production rates as $\Gamma_h^{\rm prod}=e^{-\omega/T}\Gamma_h^{\rm abs}$ and the reduced opacity as $\Gamma_h^*=(1-e^{-\omega/T})\Gamma_h^{\rm abs}$, mode by mode.
- `test_rates.py::test_vector_thomson_limit` checks the per-mode vector Thomson limit. `test_vector_reference.py::test_photon_factor_two_and_velocity` checks the summed B.16 normalization and the photon factor 2.

**Comparison-control caveat:** `run_vector_audit.py` does not make `exact_modes` versus `blinov_literal` a pure polarization-only comparison. The literal branch uses the analytic no-recoil B.14–B.16 semi-Compton kernel and the scalar summed decay integrals; the exact branch uses the finite-recoil stationary-muon kernel `rates.compton_absorption(rates.compton_kernels(...))` together with the mode-resolved decay rates. Thus the contour difference mixes the opacity/polarization prescription with the Compton recoil/thermal approximation. The current numerical comparison cannot attribute the full difference to the factor-of-three issue alone.

A clean Stage-2 diagnostic, if needed, must vary one ingredient at a time: (i) hold the B.14 no-recoil microscopic rates fixed and compare mode-resolved propagation with summed/averaged scalar-opacity diagnostics; (ii) hold the mode-resolved propagation fixed and compare B.14 no-recoil rates with the current finite-recoil stationary-muon kernel. No such scan is performed or production code changed in Stage 1.

There is an important approximation boundary. Blinov explicitly states that B.13 is usually evaluated in the non-relativistic-muon, negligible-recoil limit, $E_\gamma\simeq\omega$. The production scan instead uses exact vacuum two-body recoil with the initial muon at rest, then folds it with an effective muon density; it does **not** perform the full moving-muon thermal phase-space integral in B.13. The factor $e^{-\omega/T}$ is imposed consistently at the effective-rate level, but the present implementation does not independently evaluate both sides of the exact moving-muon collision integral. It should therefore be described as a mode-resolved stationary-muon/effective-density approximation, not as an exact thermal evaluation of B.13.

A second convention requires explicit tracking: B.17 is printed with $2\int d^3p\,f_\mu(1-f_\mu)$, whereas `transport.effective_muon_density` includes both $\mu^-$ and $\mu^+$ distributions, each with two spin states. The printed equation does not explicitly state whether the symbol $n_\mu F_{\rm deg}$ includes the charge-conjugate species. This note does not decide that convention or change the code; it records it as a separate input-normalization question.
### 4.5 Quantitative B.17 charge-conjugate susceptibility audit

The ambiguity is now quantified on the selected Caputo SFHo-18.8 profile. For each charge separately, the susceptibility is evaluated independently as
\[
n_{\mu^\mp}^{\rm eff}
=2\int\frac{d^3p}{(2\pi)^3}
 f_{\mu^\mp}(E;\pm\mu_\mu)
 [1-f_{\mu^\mp}(E;\pm\mu_\mu)]
=\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f(1-f).
\]
The table reports the positive-muon fraction of the sum of both charge states. Densities are in MeV$^3$.

| $r$ (km) | $n_{\mu^-}^{\rm eff}+n_{\mu^+}^{\rm eff}$ | Positive-muon fraction |
|---:|---:|---:|
| 0 | $7.32\times10^2$ | 0.802% |
| 5 | $3.50\times10^3$ | 1.273% |
| 8 | $3.16\times10^4$ | 1.170% |
| 10 | $2.92\times10^4$ | 0.336% |
| 15 | $3.05\times10^2$ | 0.00835% |
| 20 | $5.24\times10^{-7}$ | 0.0887% |
| 25 | $1.15\times10^{-12}$ | 50% |

The equal charge fraction at 25 km occurs because the reconstructed profile sets $\mu_\mu=0$ there; the absolute susceptibility is negligible. In the dense inner 0–10 km region, including $\mu^+$ changes the combined susceptibility by approximately 0.3–1.3% relative to the $\mu^-$ contribution alone. This is a small but nonzero convention dependence, not a basis for silently choosing the source's intended definition.

The saved 100-point Gauss–Legendre implementation agrees with the independent adaptive quadrature to better than $2\times10^{-5}$ through 15 km. The relative discrepancy grows to 0.39% at 20 km and 1.60% at 25 km, where the absolute susceptibility is already tiny. No production-code change is made on this basis.

Reproduction:
- Script: [audit_muon_susceptibility.py](audit_muon_susceptibility.py)
- Saved numerical output: [muon_susceptibility_charge_audit.json](outputs/vector_audit/muon_susceptibility_charge_audit.json)
- Regression test: `test_stage1_detailed_balance.py::test_effective_density_matches_independent_two_charge_integral`


## 5. What B.2 does—and does not—define

B.2 writes a scalar attenuation exponent,
\[
\mathcal O(r,\omega)=\frac12\int_{-1}^{1}dc_\theta
\exp\left[-\int ds\,
\frac{\Gamma_{\rm abs}^*(r'(s),\omega)}{v_V}\right],
\]
and B.4 defines $\Gamma_{\rm abs}^*=(1-e^{-\omega/T})\Gamma_{\rm abs}$. The printed B.2 contains no polarization label and does not state whether $\Gamma_{\rm abs}$ is a sum, an arithmetic average, or a production-weighted effective rate.

This omission matters because B.6 and B.13 explicitly sum over vector polarizations in the production rate, with the factors 3 in B.7 and B.15–B.16. The corresponding inverse rates obtained by replacing occupations with blocking factors inherit the same mode sum if the same convention is used. But the survival probability of a vector in a specified state is determined by that state's absorption rate, not by a sum over mutually exclusive incident polarizations.

The mode-resolved luminosity that follows from the collision terms is
\[
L_V\propto\sum_h\int d\Pi\,
\Gamma_h^{\rm prod}(r,\omega)\,
\mathcal O_h(r,\omega),
\]
where
\[
\mathcal O_h(r,\omega)=\frac12\int_{-1}^{1}dc_\theta
\exp\left[-\int ds\,
\frac{\Gamma_h^*(r'(s),\omega)}{v_V}\right].
\]
One can rewrite this in the scalar form $\Gamma_{\rm prod}\mathcal O_{\rm eff}$ only by defining
\[
\Gamma_{\rm prod}=\sum_h\Gamma_h^{\rm prod},
\qquad
\mathcal O_{\rm eff}
=\frac{\sum_h\Gamma_h^{\rm prod}\mathcal O_h}
{\sum_h\Gamma_h^{\rm prod}}.
\]
In general, $\mathcal O_{\rm eff}$ is a production-weighted average of exponentials; it is not the exponential of the sum or the arithmetic average of the mode optical depths. A single scalar $\Gamma_{\rm abs}^*$ reproduces it only when the mode opacities are equal or under an explicitly stated approximation.

**Stage-1 conclusion on B.2:** the paper's displayed equations do not uniquely specify how the summed production rates in B.7/B.15 are paired with the scalar opacity in B.2 when the three mode opacities differ. This is a definition/implementation ambiguity in the printed prescription. It is not evidence that the authors' private numerical code is wrong, and it does not identify which convention their code used.

## 6. Existing Python implementation: item-by-item verdict

| Blinov item | Existing implementation | Stage-1 verdict |
|---|---|---|
| B.6–B.9 neutrino production | `rates.neutrino_rates`; independent total-rate check in `vector_reference.summed_decay_production` | Mode decomposition and total sum are consistent; per-mode detailed balance is tested |
| B.10 neutrino absorption | `rates.neutrino_rates` returns mode-resolved production and absorption | Per-mode balance is consistent; circular modes can differ at nonzero chemical potential |
| B.11–B.12 dimuon production/width | `rates.charged_muon_decay_rates(current="vector")` | Vector width, finite threshold, angular weights and total sum are consistent |
| B.11–B.12 dimuon absorption | Same function returns mode-resolved absorption | Per-mode detailed balance is tested |
| B.13–B.14 semi-Compton kernel | `rates.compton_matrix_elements`, `compton_kernels` | Per-incident-mode vacuum kernel is implemented; thermal convolution is an effective stationary-muon approximation |
| B.15–B.18 semi-Compton normalization | `vector_reference.thomson_absorption_modes` and `test_photon_factor_two_and_velocity` | Summed no-recoil/Thomson normalization, photon factor 2 and velocity factor are checked; per-mode Thomson limit is checked separately |
| B.19 semi-Compton balance | `run_scan.py` constructs (\Gamma_h^{\rm prod}=e^{-\omega/T}\Gamma_h^{\rm abs}) | Mode-wise relation is imposed at the effective-rate level; not an independent full moving-muon thermal-integral check |
| B.2/B.4 opacity | `transport.angular_columns` accepts a separate $h$ axis; `luminosities` sums after applying $e^{-\tau_h}$ | The production scan uses mode-resolved propagation; the scalar summed-opacity diagnostic is kept separate |

Relevant existing tests:
- `test_rates.py::test_neutrino_detailed_balance_and_circular_modes`
- `test_rates.py::test_charged_muon_decay_width_and_balance`
- `test_rates.py::test_dimuon_angular_weights_from_dirac_trace`
- `test_rates.py::test_vector_thomson_limit`
- `test_rates.py::test_compton_broadcast_and_stimulation`
- `test_rates.py::test_explicit_spinors_per_mode` (the explicit-spinor mode test currently uses the axial option; vector-current checks include the summed kernel and Thomson limit)
- `test_vector_reference.py::test_spin_sums_against_blinov_closed_form`
- `test_vector_reference.py::test_photon_factor_two_and_velocity`
- `test_vector_reference.py::test_polarization_sum_is_not_decay_probability`

The existing neutrino and dimuon mode-by-mode balance tests remain in `test_rates.py`. The Stage-1 supplement adds three tests in `test_stage1_detailed_balance.py`: a pointwise B.19 test using the actual three-mode inverse-Compton matrix elements, a check that the inverse kernel retains all three incident modes, and an independent two-charge susceptibility quadrature. The complete discovered suite contains 30 tests. The saved B.17 charge audit is regenerated and checked by `audit_muon_susceptibility.py --check` in the PR workflow.

## 7. Decision for the next stage

Stage 1 establishes:

1. The neutrino and dimuon decay channels can be decomposed consistently into three normalized polarization rates. Their mode-by-mode detailed-balance relations follow exactly from equilibrium Fermi factors.
2. The semi-Compton vector kernel is mode-resolved at the vacuum cross-section level and reproduces the published summed Thomson normalization. Its thermal treatment remains an effective stationary-muon approximation, not the full B.13 integral.
3. B.2 does not print an unambiguous polarization convention for the scalar opacity. When mode opacities differ, the physically transparent construction is to propagate each mode and sum escaped luminosities afterward.
4. The existing production solver already follows that mode-resolved transport structure. The `blinov_literal` and `blinov_average` branches are scalar diagnostic interpretations and must not be promoted to the physical per-mode solver.
5. The B.17 charge-conjugate muon-density convention remains ambiguous in the printed paper. Its numerical impact is now quantified with an independent adaptive-quadrature script; the current implementation includes both charges and is unchanged.

**No production rate, transport normalization, or saved scan is changed in this stage.** The added tests and B.17 audit are diagnostic/reproducibility assets only. Stage 2 was the next step at this 2026-11-07 snapshot. PR #56 later merged on 2026-11-12; the later pure-vector Fig. 7 comparison remains unpassed, and the manuscript and referee response remain untouched by this Stage-1 audit.
