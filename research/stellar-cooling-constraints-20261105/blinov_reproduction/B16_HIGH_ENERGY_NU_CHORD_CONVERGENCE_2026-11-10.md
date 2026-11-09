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

## 5. Energy-convention question resolved against the printed equations

The paper's Eq. (B.1) integrates over the **local energy at the production point**. Its lower limit \(\omega_{\min}=m_V/N(r)\) is the gravitational escape condition \(E_\infty=N(r)\omega\ge m_V\), not the local kinematic threshold. The prefactor \(N(r)^2\) accounts for the redshift of the emitted energy and the time-dilation factor in the luminosity measured by a distant observer. The paper states these points explicitly in its gravitational-effects discussion.

The displayed Eq. (B.2), however, writes the local reduced-absorption rate as \(\Gamma_{\rm abs}^*(r'(s),\omega)\) and the speed as \(v_V(\omega)\), with the same \(\omega\) along the chord. It does not display an \(s\)-dependent \(\omega_{\rm local}(s)\) or an additional lapse ratio in the path integrand. Thus the fixed-\(\omega\) calculation remains the literal equation-level reproduction baseline.

The conserved-\(E_\infty\) variant tested separately,
\[
\omega_{\rm local}(s)=\omega_{\rm source}\frac{N(r_{\rm source})}{N(r'(s))},
\]
is a useful propagation sensitivity, but it is **not** the printed Eq. (B.2) prescription and is not a full GR ray trace. On the 27 selected high-energy neutrino rays it increases \(\tau_\nu\) by \(4.94\%\text{--}9.87\%\); the previously archived global redshift-only test lowers the 10 MeV strong-endpoint luminosity by about \(28.85\%\), but still leaves it \(36.93\%\) above Fig. 7.

## 6. Current conclusion and next calculation

The following are now independently checked:

1. local neutrino pair average: direct angular integration;
2. local neutrino kernel: published Eq. (B.9), Eq. (B.7) normalization, and Eq. (B.10) detailed balance;
3. high-energy neutrino B.2 chord integral: path-order and radial-opacity-grid convergence;
4. fixed-\(\omega\) versus conserved-\(E_\infty\) path sensitivity, with the two conventions kept separate.

The \(+92.4\%\) B.16 strong-endpoint difference is therefore not explained by a local neutrino-kernel error or by under-resolved high-energy neutrino chord integration. The redshift-only path variant is material but does not close the discrepancy and must not be silently substituted for the printed baseline.

The next calculation should test the **high-energy B.1 source measure and reconstructed local thermodynamic inputs** separately: first verify the \(\omega\)-integration measure and \(m_V/N(r)\) escape threshold against Eq. (B.1), then quantify the sensitivity of the \(210\text{--}510\) MeV source and escape contribution to the reconstructed \(T(r)\), \(\mu_{\nu_\mu}(r)\), and lapse profiles. Keep the published fixed-\(\omega\) B.2 path prescription as the baseline throughout.
