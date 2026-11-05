# Original-model axial stellar cooling and semi-Compton calculation

**Status:** independent research workstream; the local amplitude and homogeneous optically thin thermal-rate checks are complete for the stated benchmarks. A model-specific supernova transport/recast is **not** complete.  
**Branch:** `research/stellar-cooling-original-uv-model-20261105`  
**Base:** `main` at `d3c8c573e0b219dbcb4be62dc57f77fdc04c4f96` (2026-11-05).  
**Purpose:** internal follow-up research for the original paper's axial-vector model. This work does not modify the manuscript or make a supernova recast a prerequisite for the referee response.

## 1. Model-scope lock — original paper only

This workstream uses only the UV field content and symmetry-breaking pattern of the original paper:

\[
S=\frac{v_s+s+i a_s}{\sqrt2},\qquad Q_X(S)=2.
\]

The original single-VEV relations are

\[
m_{A'}=2|g_X|v_s,\qquad G=a_s,\qquad
v_s=\frac{m_{A'}}{2|g_X|}.
\]

In the small-VLL-mixing, mass-proportional charged-lepton benchmark,

\[
y_{s\ell\ell}=\frac{m_\ell}{v_s}
=\frac{2|g_X|m_\ell}{m_{A'}},
\qquad
g_{G\ell\ell}=\frac{m_\ell}{v_s}.
\]

The phase \(a_s\) is the single eaten Goldstone. No second scalar VEV, second CP-odd direction, or altered scalar sector is part of this calculation.

The \(A'\to\nu\bar\nu\) partial width uses only the original \(L_\mu-L_\tau\) active-flavor gauge current: the massless \(\nu_\mu\) and \(\nu_\tau\) channels with opposite charges and the electron flavor uncoupled. This is a width calculation within the original gauge-current model; it does not introduce or assume a separate neutrino-mass completion or additional neutrino states.

## 2. Calculation modules

- `single_vev_axial_mapping.py`: original one-VEV gauge-mass and eaten-Goldstone map.
- `test_single_vev_axial_mapping.py`: tests for the exact mass relation, Goldstone/current identity, inverse map, and input validation.
- `stellar_semi_compton_axial_matrix_element.py`: exact generic-current \(\gamma\mu\to\mu A'\) matrix element, polarization-resolved CM calculation, Ward checks, lab/CM comparison, and Klein–Nishina reference.
- `stellar_semi_compton_thermal_rate.py`: homogeneous, optically thin thermal production prototype.
- `stellar_semi_compton_thermal_convergence.py`: quadrature-order and cutoff-stability study; reference cutoffs follow the thermal-rate defaults.
- `axial_decay_widths.py`: \(A'\to\nu\bar\nu,\mu^+\mu^-\) partial-width checks using the original active-flavor \(L_\mu-L_\tau\) current and the massless-neutrino approximation; the quoted neutrino fraction is a two-channel \(\nu\bar\nu+\mu^+\mu^-\) approximation, not a complete physical branching fraction.

The semi-Compton amplitude takes \(g_V,g_A,m_{A'}\) as independent physical inputs. Its matrix element does not depend on the scalar VEV map; the UV-to-current/Goldstone relation is isolated in `single_vev_axial_mapping.py`.

## 3. Local validation

The exact source files were fetched from the clean branch before execution. The original-model mapping suite has six tests. The semi-Compton amplitude, partial-width checks, and homogeneous thermal-rate smoke test are also recorded in `validation-results-2026-11-05.md`; machine-readable convergence data are in `thermal-convergence-2026-11-05.csv`.

Representative semi-Compton checks:

\[
\begin{aligned}
|\mathcal W_V|_{\max}&=2.252\times10^{-9},\\
|\mathcal W_A|_{\max}&=2.159\times10^{-9},\\
\sigma_T/\sigma_{\rm Thomson}&=0.999998,\\
\sigma_L/\sigma_T&=5.001\times10^{-7},\\
\sigma_L(m_{A'}=0.1\ {\rm MeV})/
\sigma_L(m_{A'}=0.2\ {\rm MeV})&=4.124195.
\end{aligned}
\]

For \(T=10\) MeV, \(\mu_\mu=0\), \(m_{A'}=1\) MeV and \(g_A=0.01\), changing the quadrature order from 10 to 12 changes the event rate by 0.0108% and the emissivity by 0.0202%. The tested order-10 momentum/photon cutoff variations are below 0.5%.

These checks establish the listed matrix-element identities and the numerical stability of a homogeneous optically thin local production integral at the stated benchmark. They do **not** establish a supernova luminosity or an exclusion.

## 4. Explicit limitations

Not completed in this workstream:

- medium-rest-frame transverse/longitudinal separated emissivities and opacities;
- inverse-process absorption, optical depth, trapping and diffusion;
- realistic radial supernova profiles and transport;
- SN1987A cooling contours, high-energy-neutrino event limits, or LESN energy deposition;
- a model-specific supernova exclusion or allowed region.

The thermal routine is a homogeneous, optically thin, polarization-summed local rate. Do not present it as a transport calculation or as a completed SN1987A/LESN recast.

## 5. Acceptance checklist

- [x] Original one-VEV mass relation and Goldstone map independently checked; 6/6 mapping tests passed under Python 3.13.5.
- [x] Semi-Compton \`--check\` validated on the unchanged executable calculation; the branch copy changes only its documentation pointer.
- [x] Original-model \(A'\) partial-width assumptions checked against the paper's active-flavor current; analytic checks retained.
- [x] Thermal \`--check\` validated on the unchanged executable calculation.
- [x] Higher-order quadrature/cutoff stability data archived.
- [ ] Medium-frame T/L opacity and SN transport: explicitly deferred, not part of this phase.

The validation record distinguishes checks rerun for the single-VEV mapping from generic-current calculations whose executable bodies are unchanged.
