# Local validation record — two-VEV axial stellar-cooling line

**Date:** 2026-11-05  
**Branch:** \`research/stellar-cooling-two-vev-20261105\`  
**Base:** \`main\` at \`aaed93697dfaefdc6fa80a6bc5d5f5eee192e759\`  
**Runtime:** Python 3.13.5, NumPy 2.3.5

## Source integrity and execution method

A direct \`git clone\` was attempted but this execution environment has no outbound connection to \`github.com\`. To avoid treating a reconstructed or stale copy as branch evidence, each Python source was fetched from this exact branch and its Git blob SHA-1 was independently reproduced from the local bytes before execution.

| File | Git blob SHA-1 |
|---|---|
| \`two_vev_axial_mapping.py\` | \`5b45faf292e49183f97445a6f6ae4ac6c6ffd798\` |
| \`test_two_vev_axial_mapping.py\` | \`e38e9479955f7df28dbc2059d3df4e6567a70a5c\` |
| \`stellar_semi_compton_axial_matrix_element.py\` | \`3317339e663fbe59739045771902fb0927260c2f\` |
| \`stellar_semi_compton_thermal_rate.py\` | \`d37023df57ffea47018593b43ff5b62f7ee34e28\` |
| \`stellar_semi_compton_thermal_convergence.py\` (reference-cutoff update) | \`e36ab13ae32216ae4d3c9a2323099485f880a1b0\` |
| \`axial_decay_widths.py\` (light-neutrino trace caveat) | \`be2aefbd9078f43b8aa586f5516ce4caf953a107\` |

The GitHub clone itself was not available, but the executed local source bytes matched the branch blobs listed above.

## 1. Two-VEV map tests

Command:

\`\`\`bash
python -m unittest -v test_two_vev_axial_mapping.py
\`\`\`

**Result: 6/6 tests passed.**

Checks cover:

- \(m_{A'}^2=g_X^2(4v_s^2+v_\sigma^2)\);
- equality of the projected S-phase Goldstone Yukawa and the axial-current divergence result;
- recovery of the single-VEV limit;
- inverse map from \((m_{A'},g_X,r_\sigma)\) to \((v_s,v_\sigma)\);
- orthogonality/normalization of eaten and physical CP-odd directions;
- invalid-input rejection.

## 2. Exact semi-Compton amplitude

Command:

\`\`\`bash
python stellar_semi_compton_axial_matrix_element.py --check
\`\`\`

**Result: PASS.**

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

## 3. Current-level decay widths

Command:

\`\`\`bash
python axial_decay_widths.py
\`\`\`

**Result: PASS.**

Representative outputs:

| \(m_{A'}\) (MeV) | \(\Gamma_A^{\mu\mu}/\Gamma_V^{\mu\mu}\) | \(BR_{\nu\nu}^{A}\) |
|---:|---:|---:|
| 220 | 0.052953 | 0.978928 |
| 250 | 0.210371 | 0.867628 |
| 300 | 0.403688 | 0.736578 |
| 600 | 0.824804 | 0.549501 |

The neutrino width is the inclusive light-neutrino trace result
\(\mathrm{Tr}(G_\nu^\dagger G_\nu)=2\) for a unitary three-flavour PMNS rotation. It assumes negligible active-heavy mixing and closed heavy-neutrino thresholds. It is not a complete total-width calculation if \(A'\to N_iN_j\) or other new channels are open.

## 4. Homogeneous optically thin thermal-rate smoke test

Command:

\`\`\`bash
python stellar_semi_compton_thermal_rate.py --check
\`\`\`

**Result: PASS.**

- \(U_{\rm medium}^2=1.000000000000\);
- medium-frame energy-conservation residual \(3.553\times10^{-15}\);
- smoke-test event rate \(3.090555\times10^{-6}\ {\rm MeV}^4\);
- smoke-test energy emissivity \(7.869960\times10^{-5}\ {\rm MeV}^5\).

This is a low-order, homogeneous-cell smoke test, not a converged SN luminosity or opacity calculation.

## 5. Higher-order and cutoff stability

Benchmark for the convergence study:

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

The order-6 cutoff scan is visibly less stable; it is retained as a diagnostic of why low-order results must not be promoted. The higher-order order-10/12 comparison and the order-10 cutoff checks are stable at the sub-percent level for this stated benchmark.

Machine-readable values are in \`thermal-convergence-2026-11-05.csv\`.

## 6. What this validation does and does not establish

**Established:** the branch's two-VEV Goldstone mapping, generic vacuum semi-Compton amplitude, current-level \(A'\) partial-width checks under stated light-neutrino assumptions, and a homogeneous optically thin polarization-summed thermal production integral are locally executable and pass their stated checks.

**Not established:** medium-rest-frame T/L-resolved emissivities or opacities, inverse-process/trapping transport, radial SN profiles, diffusion, SN1987A cooling contours, high-energy neutrino event constraints, or LESN energy deposition. No supernova exclusion or allowed region follows from this record.

The local clone was blocked by the environment's outbound network restriction. The source blobs were fetched and SHA-1 verified before execution; CI was not used.
