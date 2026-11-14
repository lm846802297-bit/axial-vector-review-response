# 10 MeV local-rate, polarization and escape localization audit

**Date:** 2026-11-13  
**Target:** Blinov et al., JHEP 06 (2026) 155, Fig. 7  
**Fixed point:** \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)

## Executive result

The high-order literal scalar Appendix-B.2 calculation gives

\[
L_{\rm calc}=2.439635957\times10^{52}\ {\rm erg\,s^{-1}},
\qquad
L_{\rm Fig.7}=1.267814759\times10^{52}\ {\rm erg\,s^{-1}},
\]

or a \(+92.4284\%\) residual (factor 1.9243, not one order of magnitude).

The optically thin B.1 source is \(7.502477\times10^{55}\) erg/s, 5917.64 times the Fig. 7 luminosity. The computed source-weighted escape fraction is \(3.251774\times10^{-4}\). At fixed source, matching Fig. 7 would require \(1.689862\times10^{-4}\). Thus the actual escape fraction is 1.9243 times the reference-implied value; the final discrepancy appears in the global transport/escape integral.

The result was reproduced with 200 source-radial nodes, 642 opacity-radial nodes, 842 energy nodes, 32 direction nodes and 64 path nodes. The previous lower-order 40/100/16/32 result differs by only about 0.10%, so this is not a simple quadrature-order failure.

## 1. Matched local production and absorption

The audit evaluates local rates at identical \((r,\omega)\) points, with \(r=\{8,12,15,20,22,25\}\) km and \(\omega=\{12,15,20,30,50,100,200,300,500\}\) MeV. It compares scalar B.16 neutrino production/absorption with independently integrated \(L,+,-\) neutrino modes, and computes the Compton reduced opacity directly rather than subtracting it from a neutrino-dominated total.

| Closure check | Maximum relative residual |
|---|---:|
| Neutrino production: mode sum vs scalar | \(1.67\times10^{-14}\) |
| Neutrino absorption: mode sum vs scalar detailed balance | \(1.60\times10^{-14}\) |
| Neutrino mode-by-mode detailed balance, source grid | \(3.33\times10^{-14}\) |
| Neutrino mode-by-mode detailed balance, opacity grid | \(3.42\times10^{-14}\) |
| Integrated B.1 source mode-sum closure | \(6.29\times10^{-16}\) |
| Integrated local reduced-opacity mode-sum closure | \(1.10\times10^{-12}\) |

The largest pointwise relative residual (\(8.9\times10^{-8}\)) is confined to an exponentially negligible outer/high-energy tail where the local rate is about \(10^{-147}\) MeV. The integrated closures and selected physical nodes pass. No missing local polarization-sum factor is indicated.

At \(r=12\) km, \(\omega=300\) MeV, \(T=25.9827\) MeV, the neutrino production rates per \(g^2\) are \(8.0390\times10^{-8}\), \(7.1987\times10^{-8}\), and \(7.3387\times10^{-8}\) MeV for \(L,+,-\). The B.14 no-recoil Compton weights are \(w_L=5.5525\times10^{-4}\), \(w_+=w_-=0.4997224\). The corresponding total reduced opacities per \(g^2\) are \(8.3167\times10^{-3}\), \(1.3115\times10^{-2}\), and \(1.3259\times10^{-2}\) MeV; their sum equals the scalar reduced opacity \(3.4691\times10^{-2}\) MeV.

The B.14 Compton split is a no-recoil Thomson-limit diagnostic, not a full recoil-resolved polarization kernel.

## 2. Source and escape factorization

At 10 MeV the dimuon channel is closed. The optically thin source consists of 67.9259% neutrino coalescence and 32.0741% semi-Compton production.

| Point | Thin source / Fig. 7 | Escape fraction | Final luminosity / Fig. 7 |
|---|---:|---:|---:|
| Weak coupling | 0.9105 | 0.99787 | 0.9085 |
| Reference peak | 2.9016 | 0.35262 | 1.0232 |
| Strong endpoint | 5917.64 | \(3.25177\times10^{-4}\) | 1.92428 |

The weak-coupling \(\sim9\%\) difference is already present in the optically thin source/profile/reference comparison. At the strong endpoint, the remaining factor 1.924 is the ratio of the computed escape fraction to the value required at fixed source. It is not evidence for a missing factor of two in the local production rate.

## 3. Optical depth and energy dependence

At the strong endpoint, the scalar B.2 source-weighted total optical depth has mean 16.1287, median 14.1307 and \(p_{90}=26.2521\). The escape-weighted mean is 5.29436.

The mean optical-depth split is 89.78% neutrino inverse decay and 10.22% Compton. A channel-removal Shapley diagnostic attributes 65.61% of the total luminosity suppression to neutrino opacity and 34.39% to Compton opacity. This is nonlinear because the escape probability is exponential.

The reconstructed source has mean emission radius 9.83 km and median 9.51 km, but 56.71% of the source-weighted mean optical depth accumulates at \(r\ge15\) km; the 22--25 km shell contributes 17.37%.

| Energy bin | Thin-source fraction | Escaped-luminosity fraction | Mean source-weighted \(\tau\) |
|---|---:|---:|---:|
| 60--110 MeV | 35.925% | 0.963% | 16.13 |
| 110--210 MeV | 33.611% | 24.674% | 11.08 |
| 210--510 MeV | 9.670% | 69.756% | 7.72 |
| 510--1010 MeV | 0.0214% | 1.170% | 4.76 |

The 110--510 MeV interval supplies 94.43% of the escaping luminosity. The 210--510 MeV bin alone contributes nearly 70% despite supplying less than 10% of the thin source. High-energy opacity and path-energy treatment therefore have disproportionate leverage on the strong-absorption tail.

## 4. Three-mode propagation is a separate prescription

The neutrino-only source fractions are \(L=34.74\%\), \(+=31.50\%\), and \(-=33.75\%\). Including the B.14 Compton split, total source fractions are \(L=23.86\%\), \(+=37.31\%\), and \(-=38.83\%\).

| Mode | Source-weighted mean \(\tau_h\) | Escape fraction |
|---|---:|---:|
| \(L\) | 5.418 | 2.928% |
| \(+\) | 5.400 | 2.392% |
| \(-\) | 5.475 | 2.298% |

Independent mode propagation gives \(1.8631\times10^{54}\) erg/s, 76.37 times the literal scalar B.2 result. This is **not** a correction to the baseline: the published scalar B.2 prescription exponentiates the polarization-summed opacity, whereas independent mode propagation exponentiates each mode separately. These are distinct transport prescriptions. The literal scalar baseline is retained.

## 5. Leading physical sensitivity: path-energy convention

An archived conserved-\(E_\infty\) local-energy diagnostic, retaining the same Euclidean chord length, gives \(L=1.73580\times10^{52}\) erg/s and a \(+36.91\%\) residual, compared with \(+92.43\%\) for fixed local \(\omega\). It lowers the strong-endpoint luminosity by 28.85%, so the energy convention is a leading sensitivity, but it does not close the discrepancy. This redshift-only diagnostic is not full GR ray tracing because the spatial metric/path-length correction is absent.

A previously archived consistent B.13 moving-muon source-plus-opacity alternative gives a \(+131.59\%\) strong-endpoint residual, so replacing B.16 by B.13 does not resolve the mismatch. The B.13 source-only variant is not accepted because it does not update the paired opacity.

No opacity multiplier is adopted. The earlier Compton-opacity-only factor-of-two stress test changes opacity while holding the source fixed and therefore breaks detailed balance.

## 6. Decision and next step

- Local neutrino production/absorption sums and detailed balance pass on the tested physical domain.
- The 1.924 residual is localized to the global B.2 path/angle escape integral.
- Leading unresolved sensitivities are fixed-\(\omega\) versus conserved-\(E_\infty\) path-energy convention, high-energy escape weighting, and outer-radius opacity accumulation.
- The reconstructed profile is from public figure paths, not the original Garching simulation table.
- No mass scan was expanded; no source normalization, opacity rescaling, axial scan or published contour was changed.

Next, keep the mass fixed at 10 MeV and perform a one-factor path-energy audit using a consistent GR metric/path measure, then isolate the \(r\ge15\) km opacity contribution and the 110--510 MeV escape band. Only after those checks should the pure-vector Fig. 7 gate be reconsidered.

## Reproduction

The self-contained executable diagnostic, selected-node CSV, machine-readable JSON, plot, pinned inputs and helper source are supplied in the 10 MeV localization addendum delivered with this audit. It contains the direct-run script and three fast regression tests. The calculation was run directly in the local Python environment; CI is not the primary calculation engine.
