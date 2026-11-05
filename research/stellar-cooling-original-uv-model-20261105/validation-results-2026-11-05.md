# Local validation record — original-model axial stellar-cooling line

**Date:** 2026-11-05  
**Branch:** \`research/stellar-cooling-original-uv-model-20261105\`  
**Base:** \`main\` at \`d3c8c573e0b219dbcb4be62dc57f77fdc04c4f96\`  
**Runtime for the mapping tests:** Python 3.13.5

## Model scope

All UV-to-current and Goldstone statements in this record use only the original paper's single-VEV field content:
\[
S=(v_s+s+i a_s)/\sqrt2,\quad Q_X(S)=2,\quad
m_{A'}=2|g_X|v_s,\quad G=a_s.
\]
The single phase of \(S\) is the eaten Goldstone. The mass-proportional small-VLL-mixing benchmark is \(y_{s\ell\ell}=m_\ell/v_s\). No additional scalar or modified symmetry-breaking sector is included.

The \(A'\to\nu\bar\nu\) partial width uses only the original active-flavor \(L_\mu-L_\tau\) gauge current: massless \(\nu_\mu\) and \(\nu_\tau\) channels with opposite charges, while the electron flavor is uncoupled. No additional neutrino states or neutrino-mass completion are part of this calculation.

## Source blobs in the clean branch

| File | Git blob SHA-1 |
|---|---|
| \`single_vev_axial_mapping.py\` | \`bd31ad4f5896b98612e07dcabee69b278ec33b46\` |
| \`test_single_vev_axial_mapping.py\` | \`bd612334c084ce5c7c971039075dfbf01f9efa38\` |
| \`axial_decay_widths.py\` | \`8f2d320858bd16173f16bed72af3d1cf1d8a8625\` |
| \`stellar_semi_compton_axial_matrix_element.py\` | \`d733eb357748502246e24afbe03f88aa6f192737\` |
| \`stellar_semi_compton_thermal_rate.py\` | \`d37023df57ffea47018593b43ff5b62f7ee34e28\` |
| \`stellar_semi_compton_thermal_convergence.py\` | \`e36ab13ae32216ae4d3c9a2323099485f880a1b0\` |
| \`thermal-convergence-2026-11-05.csv\` | \`075314ff389cfa2eade061d8a6d359473e8225c2\` |

The semi-Compton amplitude, thermal-rate and convergence executable bodies are carried over unchanged from the prior local validation; the amplitude file's only change is its documentation pointer to the original-model mapping module. The decay-width executable formulae are unchanged; only the description of the neutrino-current assumption is corrected to the original flavor-basis current.

## 1. Original-model single-VEV map

Command:
\`\`\`bash
python -m unittest -v test_single_vev_axial_mapping.py
\`\`\`

**Result: 6/6 tests passed** under Python 3.13.5.

Checks cover:
- \(m_{A'}=2|g_X|v_s\);
- the full eaten-Goldstone projection \(G=a_s\);
- equality of \(m_\ell/v_s\) and \(2|g_A^\ell|m_\ell/m_{A'}\) for \(|g_A^\ell|=|g_X|\);
- inverse map from \((m_{A'},g_X)\) to \(v_s\);
- lepton-mass scaling;
- invalid-input rejection.

## 2. Exact semi-Compton amplitude

The previously validated command was:
\`\`\`bash
python stellar_semi_compton_axial_matrix_element.py --check
\`\`\`

**Result: PASS** on the unchanged executable calculation.

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

The checks cover on-shell kinematics, polarization orthonormality, the electromagnetic Ward identity for vector/axial/mixed currents, the conserved-vector Thomson limit, lab/CM total-cross-section agreement, Klein–Nishina agreement, and the axial longitudinal \(1/m_{A'}^2\) scaling.

The T/L labels remain frame-defined. The CM-helicity split is **not** the medium-rest-frame split when the thermal medium moves in the pair CM frame.

## 3. Original-current \(A'\) partial widths

The width formulae are unchanged. Their interpretation is now explicitly tied to the original active-flavor current, with massless \(\nu_\mu,\nu_\tau\) and no additional states.

Representative outputs:

| \(m_{A'}\) (MeV) | \(\Gamma_A^{\mu\mu}/\Gamma_V^{\mu\mu}\) | \(BR_{\nu\nu}^{A}\) |
|---:|---:|---:|
| 220 | 0.052953 | 0.978928 |
| 250 | 0.210371 | 0.867628 |
| 300 | 0.403688 | 0.736578 |
| 600 | 0.824804 | 0.549501 |

The neutrino normalization corresponds to the sum of the two original active-flavor charges squared, \( (+1)^2+(-1)^2=2 \), in the massless flavor basis. It is not a statement about a separate neutrino-mass model.

## 4. Homogeneous optically thin thermal-rate smoke test

The previously validated command was:
\`\`\`bash
python stellar_semi_compton_thermal_rate.py --check
\`\`\`

**Result: PASS** on the unchanged executable calculation.

- \(U_{\rm medium}^2=1.000000000000\);
- medium-frame energy-conservation residual \(3.553\times10^{-15}\);
- smoke-test event rate \(3.090555\times10^{-6}\ {\rm MeV}^4\);
- smoke-test energy emissivity \(7.869960\times10^{-5}\ {\rm MeV}^5\).

This is a homogeneous-cell smoke test, not a converged SN luminosity or opacity calculation.

## 5. Higher-order and cutoff stability

Benchmark:
\[
T=10\ {\rm MeV},\quad \mu_\mu=0,\quad m_{A'}=1\ {\rm MeV},
\quad g_V=0,\quad g_A=0.01.
\]

The thermal routine's default cutoffs are
\(p_{\max}=195.0308057\ {\rm MeV}\) and
\(\omega_{\max}=200\ {\rm MeV}\).

| Quadrature order | Event rate (MeV\(^4\)) | Emissivity (MeV\(^5\)) |
|---:|---:|---:|
| 6 | \(1.9121855\times10^{-6}\) | \(7.4737469\times10^{-5}\) |
| 8 | \(1.9003387\times10^{-6}\) | \(7.2333697\times10^{-5}\) |
| 10 | \(1.8963427\times10^{-6}\) | \(7.2382220\times10^{-5}\) |
| 12 | \(1.8961378\times10^{-6}\) | \(7.2396841\times10^{-5}\) |

The order-10 to order-12 changes are \(-0.0108\%\) in event rate and \(+0.0202\%\) in emissivity.

At order 10, changing one cutoff at a time gives:

| Variation | Relative rate change | Relative emissivity change |
|---|---:|---:|
| \(p_{\max}=160\) MeV | \(-0.1887\%\) | \(-0.4385\%\) |
| \(p_{\max}=240\) MeV | \(+0.0137\%\) | \(+0.0424\%\) |
| \(\omega_{\max}=160\) MeV | \(-0.0126\%\) | \(+0.0084\%\) |
| \(\omega_{\max}=240\) MeV | \(+0.0191\%\) | \(-0.0470\%\) |

Machine-readable values are in \`thermal-convergence-2026-11-05.csv\`.

## 6. What this validation does and does not establish

**Established:** the original paper's single-VEV gauge/Goldstone map, generic-current vacuum semi-Compton amplitude, \(A'\) partial-width checks using the original active-flavor gauge current, and a homogeneous optically thin polarization-summed thermal production integral are validated at the stated benchmarks.

**Not established:** medium-rest-frame T/L-resolved emissivities or opacities, inverse-process/trapping transport, radial SN profiles, diffusion, SN1987A cooling contours, high-energy-neutrino event constraints, or LESN energy deposition. No supernova exclusion or allowed region follows from this record.

A direct \`git clone\` was unavailable in the earlier execution environment; source files were fetched from GitHub and their blob SHAs recorded above. The single-VEV map suite was rerun for this clean branch. CI was not used, and no CI pass is claimed.
