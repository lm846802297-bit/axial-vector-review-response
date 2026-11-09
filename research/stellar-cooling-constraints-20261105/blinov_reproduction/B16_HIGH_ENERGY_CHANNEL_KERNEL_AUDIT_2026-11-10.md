# 10 MeV B.16 high-energy source and opacity channel audit

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: pure vector, \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
Profile: reconstructed SFHo-18.8, \(t_{\rm pb}=1\) s, profile SHA-256  
\`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Question

The preceding phase-space audit found that the \(210\text{--}510\) MeV interval contributes \(69.76\%\) of the escaping luminosity while containing only \(9.67\%\) of the optically-thin B.1 source. This calculation resolves that high-energy tail into the two active B.16 channels:

- neutrino inverse decay, \(\nu_\mu\bar\nu_\mu+\nu_\tau\bar\nu_\tau\leftrightarrow V\);
- semi-Compton production/absorption, \(\mu\gamma\leftrightarrow\mu V\), using the B.14--B.16 no-recoil/non-relativistic-muon reference kernel.

For each channel, the B.1 source and the B.2 reduced absorption are kept separate. The total survival factor is always
\[
P_{\rm esc}(\omega,r,\cos\theta)
=\exp[-\tau_\nu-\tau_C].
\]
The source-channel escape fractions therefore use the same physical total opacity; they are not obtained by switching off the other channel.

## 2. Global channel decomposition

The B.1 optically-thin source is:

| Channel | Fraction of B.1 source |
|---|---:|
| Neutrino inverse decay | 67.926% |
| Semi-Compton | 32.074% |

After propagation through the full B.2 opacity, the escaped luminosity is:

| Emission channel | Fraction of escaped luminosity | Escaped luminosity |
|---|---:|---:|
| Neutrino inverse decay | 54.110% | \(1.32009\times10^{52}\) erg/s |
| Semi-Compton | 45.890% | \(1.11954\times10^{52}\) erg/s |

The \(8\text{--}15\) km region supplies \(79.652\%\) of the B.1 source and \(86.855\%\) of the escaping luminosity. Within this region, the source fractions are \(66.626\%\) neutrino and \(33.374\%\) Compton; after escape weighting they become \(52.358\%\) and \(47.642\%\).

## 3. Energy-resolved result

| Energy | B.1 source fraction | Escaped-luminosity fraction | Source: \(\nu/C\) | Escaped: \(\nu/C\) | Source-weighted \(\langle\tau_\nu\rangle/\langle\tau_C\rangle\) |
|---|---:|---:|---:|---:|---:|
| 60--110 MeV | 35.925% | 0.963% | 71.53 / 28.47% | 79.67 / 20.33% | 14.52 / 1.62 |
| 110--210 MeV | 33.611% | 24.674% | 61.79 / 38.21% | 63.93 / 36.07% | 9.35 / 1.73 |
| 210--510 MeV | 9.670% | **69.756%** | 49.88 / 50.12% | 48.40 / 51.60% | 5.91 / 1.81 |
| 510--1010 MeV | 0.0214% | 1.170% | 31.98 / 68.02% | 31.75 / 68.25% | 2.88 / 1.88 |

The dominant escaping energy interval is therefore a genuinely mixed source: neutrino inverse decay and semi-Compton contribute almost equally to its production and to its escaping luminosity. However, its source-weighted mean optical depth is still larger from neutrino inverse decay:
\[
\langle\tau_\nu\rangle_{210-510}=5.912,\qquad
\langle\tau_C\rangle_{210-510}=1.808.
\]
The \(60\text{--}110\) MeV interval has a much larger source but is strongly attenuated; its escape probability is only \(8.72\times10^{-6}\). The \(210\text{--}510\) MeV bin has escape probability \(2.346\times10^{-3}\), about 269 times larger.

## 4. Which opacity suppresses the luminosity?

The source-weighted mean optical depths over the complete B.1 distribution are
\[
\langle\tau_\nu\rangle_{\rm source}=14.481,\qquad
\langle\tau_C\rangle_{\rm source}=1.648.
\]
Thus neutrino inverse decay supplies about \(89.8\%\) of the source-weighted mean optical depth. The escape-weighted means are \(4.544\) and \(0.750\), respectively.

To account for the nonlinearity of \(e^{-\tau}\), four luminosities are computed with the *same total B.1 source*:

| Opacity retained | Luminosity |
|---|---:|
| Both \(\nu\) and Compton | \(2.43964\times10^{52}\) erg/s |
| Neutrino opacity only | \(6.07380\times10^{52}\) erg/s |
| Compton opacity only | \(2.34813\times10^{55}\) erg/s |
| No opacity (optically thin) | \(7.50248\times10^{55}\) erg/s |

The one-channel rows are counterfactual diagnostics, not alternative physical predictions. A symmetric Shapley decomposition of the total luminosity suppression assigns:

- **65.61%** to neutrino inverse-decay opacity;
- **34.39%** to semi-Compton opacity.

The Compton share of the suppression is larger than its \(10.2\%\) share of the source-weighted mean \(\tau\). This is not a contradiction: the luminosity suppression depends on the full correlation among emission radius, energy, direction, and opacity, rather than on exponentiating a single mean optical depth.

## 5. Independent local check of the high-energy neutrino kernel

The analytic Eq. (B.25) Fermi-pair angular average is independently checked by direct numerical integration:
\[
I(\mu,\omega,T)
=\frac12\int_{-1}^{1}d\cos\vartheta\,
f\!\left(\frac{\omega}{2}(1+v\cos\vartheta),\mu\right)
f\!\left(\frac{\omega}{2}(1-v\cos\vartheta),-\mu\right).
\]

The comparison covers \(r=8,10,12.5,15\) km, \(\omega=60,110,210,510,1010\) MeV, both \(\mu_{\nu_\mu}(r)\) and \(\mu=0\), and direct Gauss-Legendre orders 128, 256, 512, and 1024.

| Direct angular order | Maximum absolute relative residual vs analytic Eq. (B.25) |
|---:|---:|
| 128 | \(2.89\times10^{-15}\) |
| 256 | \(3.11\times10^{-15}\) |
| 512 | \(2.66\times10^{-15}\) |
| 1024 | \(3.11\times10^{-15}\) |

This independently verifies the local Fermi-pair angular average used in the high-energy neutrino source and, through detailed balance, its local reduced-absorption factor. It does not by itself certify the complete radial interpolation or chord integration.

## 6. Relation to the existing exact B.13 Compton calculation

The existing global B.13 run replaces the Compton source and opacity together, rather than mixing an exact source with an approximate opacity. Its strong-endpoint discrepancy is \(+131.53\%\) relative to Fig. 7; the subsequent combined radial-energy refinement gives \(+131.12\%\). See:

- \`B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md\`
- \`B13_GLOBAL_STAGE_A_CONVERGENCE_STATUS_2026-11-09.md\`

Thus the exact moving-muon B.13 replacement does not remove the existing B.16--Fig. 7 strong-endpoint discrepancy. It moves the 10 MeV global result further above Fig. 7. This is a separate physical-kernel comparison, not a reason to modify the B.16 reproduction baseline.

## 7. Numerical closure and scope

The direct V8 calculation uses the same quadrature prescription and node counts as the archived high-order B.16 result:

- source radius: 200 nodes;
- opacity radius: 642 nodes;
- energy: 842 nodes;
- direction: 32 nodes;
- path: 64 nodes;
- muon susceptibility: 512-point Gauss-Legendre integration.

It reproduces the archived high-order B.16 luminosity with relative residual \(-9.22\times10^{-13}\), the optically-thin source with residual \(-8.74\times10^{-14}\), and the escape probability with absolute residual \(-2.72\times10^{-16}\). The profile and Fig. 7 input SHA-256 hashes match the archived baseline. V8-generated quadrature nodes are not bitwise identical to NumPy-generated nodes, so this is explicitly a cross-runtime calculation, not the strict NumPy-grid acceptance run.

A Python/NumPy/SciPy reproduction script is added at \`audit_b16_channel_resolved_energy.py\`. The numerical values archived in the accompanying JSON are from the direct V8 execution; the Python script is the canonical reproducibility implementation and has not been executed in this V8 session.

No profile, source normalization, opacity prescription, coupling, axial-vector result, or constraint curve is changed. No empirical rescaling is applied.

## 8. Decision and next calculation

The local analytic neutrino-pair kernel is not the source of the high-energy discrepancy at the tested points: direct angular integration reproduces Eq. (B.25) to machine precision. The energy-resolved result also shows that neutrino inverse decay remains the larger opacity contribution in the dominant \(210\text{--}510\) MeV escape bin and dominates the global luminosity suppression.

The next targeted calculation should therefore be an independent **high-energy neutrino B.2 chord-convergence audit** at \(r_{\rm em}=8\text{--}12\) km, outward directions, and \(\omega=110\text{--}510\) MeV. Vary path quadrature and opacity interpolation separately, retaining the same fixed-\(\omega\) prescription and without changing the physical input. Only after that check should the residual strong-endpoint discrepancy be assigned to a physical background or propagation convention.
