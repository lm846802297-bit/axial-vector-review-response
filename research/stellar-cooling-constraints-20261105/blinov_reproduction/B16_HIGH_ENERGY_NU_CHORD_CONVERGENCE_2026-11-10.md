# High-energy neutrino B.2 chord-convergence audit

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Scope

The preceding energy-resolved decomposition identifies neutrino inverse decay as the larger opacity contribution in the dominant \(210\text{--}510\) MeV escape bin. The local Eq. (B.25) Fermi-pair angular average has also been checked independently against direct angular integration to machine precision.

This follow-up isolates the remaining numerical part of the neutrino B.2 kernel: the chord integral itself. It uses the printed fixed-\(\omega\) convention and evaluates 36 rays:

- emission radii: \(8,\ 10,\ 12.5\) km;
- initial directions: \(\cos\theta=-0.25,\ 0.25,\ 0.75,\ 0.95\);
- energies: \(110,\ 210,\ 510\) MeV;
- opacity radial orders: 320, 640, 1280;
- path Gauss-Legendre orders: 32, 64, 128, 256.

Only the neutrino inverse-decay reduced opacity is included, so the test is channel-specific. The opacity grids are independent of the emission radii.

## 2. Maximum refinement changes

| Refinement | Maximum absolute relative change |
|---|---:|
| Path 32 \(\rightarrow\) 64, opacity grid 640 | \(1.987\times10^{-5}\) |
| Path 64 \(\rightarrow\) 128, opacity grid 640 | \(1.017\times10^{-5}\) |
| Path 128 \(\rightarrow\) 256, opacity grid 640 | \(2.822\times10^{-6}\) |
| Opacity grid 320 \(\rightarrow\) 640, path 256 | \(4.575\times10^{-6}\) |
| Opacity grid 640 \(\rightarrow\) 1280, path 256 | \(9.350\times10^{-7}\) |

In percentage units, even the coarsest tested path transition is below \(0.0020\%\), while the final opacity-grid refinement is below \(0.00010\%\).

Representative outward rays at \(210\) MeV give:

| Emission radius | \(\cos\theta\) | \(\tau_\nu\), grid 320 | \(\tau_\nu\), grid 640 | \(\tau_\nu\), grid 1280 |
|---:|---:|---:|---:|---:|
| 8 km | 0.75 | 5.54490257 | 5.54490490 | 5.54490490 |
| 10 km | 0.75 | 5.11421712 | 5.11422226 | 5.11422353 |
| 12.5 km | 0.75 | 4.49659787 | 4.49660592 | 4.49660695 |

The table uses path order 256 for each opacity grid.

## 3. Interpretation

The high-energy neutrino B.2 chord integral is numerically stable on the current 640-node opacity grid and 64-node path grid. The independent targeted-ray refinements are much smaller than the percent-level changes that could plausibly affect the Fig. 7 discrepancy.

This agrees with the existing global 10 MeV B.2 convergence audit, which already passes the path \(48\rightarrow64\), opacity \(480\rightarrow640\), and combined-grid refinements at the stated project numerical screening target. The present calculation is stronger in one respect: it checks the high-energy neutrino channel directly, rather than relying only on the global luminosity.

Consequently, the \(+92.4\%\) B.16 strong-endpoint difference is not explained by under-resolved high-energy neutrino chord quadrature or by radial interpolation of the neutrino reduced opacity.

## 4. Reproducibility and limits

- Machine-readable result: \`outputs/b16_high_energy_nu_chord_convergence_10mev_2026-11-10_v8.json\`
- Reproduction script: \`audit_b16_high_energy_nu_chord_convergence.py\`
- The numerical result in the JSON is from a direct V8 double-precision execution. The accompanying Python script is the repository reproduction implementation and was not executed in this V8 session.
- The radial opacity interpolation is linear, as in the reference B.2 implementation.
- This is a local-ray convergence test, not a new global luminosity calculation.
- It does not test the Compton channel, the stellar profile uncertainty, or the physical energy convention.

No profile, source term, coupling, opacity prescription, or axial-vector result is modified. No empirical rescaling is applied.

## 5. Next physics question

The numerical quadrature is no longer the leading suspect for the high-energy neutrino optical depth. The remaining large sensitivity is the physical propagation-energy convention: the existing global redshift-only diagnostic changes the 10 MeV strong-endpoint luminosity by about \(-28.85\%\) relative to fixed-\(\omega\), while retaining the Euclidean chord. That is not a full-GR ray trace and is not a replacement for the printed fixed-\(\omega\) baseline.

The next useful step is to resolve the energy convention directly against the published B.2 definitions and then compare the high-energy neutrino optical depth under fixed-\(\omega\) and conserved-\(E_\infty\) propagation, without mixing the two into one result.
