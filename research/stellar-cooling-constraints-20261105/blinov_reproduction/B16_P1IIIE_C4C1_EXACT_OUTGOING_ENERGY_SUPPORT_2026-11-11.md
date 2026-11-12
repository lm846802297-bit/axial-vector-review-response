# P1-IIIe-C4C1: exact outgoing-neutrino energy support

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose

C4-C1 removes the arbitrary finite \(E_\nu'\) integration window used in the C4-B2 local diagnostic. It determines the full outgoing-neutrino energy support allowed by the exact moving-nucleon kinematics and the same \(45T\) momentum-tail cutoff used in C4-B2. It then integrates the differential weak collision kernel over that support and measures, rather than assumes, the fraction captured by the old \(\pm60\) MeV window.

The benchmark uses \(E_\nu=100\) MeV and \(\cos\theta=-0.5\), at \(r=0.20,\ 5.00,\ 10.00,\ 15.20\) km, for neutron/proton targets and neutrino/antineutrino. This gives 16 local rate cases and eight distinct kinematic support intervals (the support is independent of the neutrino/antineutrino label).

## 2. Exact outgoing-energy support

For each trial outgoing energy \(E_\nu'\), define
\[
q_0=E_\nu-E_\nu',\qquad
q=\sqrt{E_\nu^2+E_\nu'^2-2E_\nu E_\nu'\cos\theta}.
\]
The exact initial nucleon momentum threshold is evaluated with the local effective mass:
\[
p_{\min}=p_{\min}(q_0,q;m_N^*).
\]
The numerical upper momentum cutoff is the same as C4-B2:
\[
E_{\max}^*=m_N^*+\max(\nu_N,0)+45T,\qquad
p_{\max}=\sqrt{(E_{\max}^*)^2-m_N^{*2}}.
\]
The allowed outgoing-energy interval is therefore defined by
\[
\boxed{p_{\min}(q_0(E_\nu'),q(E_\nu');m_N^*)\le p_{\max}.}
\]
Both endpoints are roots of \(p_{\min}-p_{\max}=0\). They are bracketed on a 2001-point \(E_\nu'\) scan and refined with Brent's method. The maximum relative root residual over all local and cold-limit cases is \(3.85\times10^{-13}\).

The resulting support intervals are broad because \(p_{\max}\) includes a deliberately conservative \(45T\) occupation tail. They are kinematic/numerical support bounds, not a claim that the integrand is equally important throughout the interval.

## 3. Full-support ranges

| Radius [km] | Species | \(E_\nu'{}_{\min}\) [MeV] | \(E_\nu'{}_{\max}\) [MeV] | Support width [MeV] |
|---:|:---:|---:|---:|---:|
| 0.20 | n | 4.07 | 928.54 | 924.47 |
| 0.20 | p | 4.49 | 864.17 | 859.68 |
| 5.00 | n | 3.42 | 1110.45 | 1107.03 |
| 5.00 | p | 3.69 | 1052.30 | 1048.61 |
| 10.00 | n | 3.57 | 1247.71 | 1244.14 |
| 10.00 | p | 3.65 | 1226.08 | 1222.42 |
| 15.20 | n | 13.76 | 462.74 | 448.99 |
| 15.20 | p | 13.86 | 459.60 | 445.74 |

The stationary-target recoil centers are only about \(78\)--\(86\) MeV. The full finite-temperature support is much wider because the initial nucleon carries a broad momentum distribution.

## 4. Does the old \(\pm60\) MeV window capture the full rate?

For each local case, compare
\[
\Gamma_{\rm full}=
\int_{E'_{\min}}^{E'_{\max}}dE_\nu'\,
\frac{d\Gamma}{dE_\nu' d\Omega'}
\]
with
\[
\Gamma_{60}=
\int_{\max(E'_{\min},E'_0-60)}^{\min(E'_{\max},E'_0+60)}
dE_\nu'\,
\frac{d\Gamma}{dE_\nu' d\Omega'}.
\]
The reported window fraction is \(\Gamma_{60}/\Gamma_{\rm full}\).

| Radius [km] | Species | Neutrino fraction | Antineutrino fraction |
|---:|:---:|---:|---:|
| 0.20 | n | 0.8543 | 0.8899 |
| 0.20 | p | 0.8720 | 0.8917 |
| 5.00 | n | 0.7657 | 0.8187 |
| 5.00 | p | 0.8111 | 0.8381 |
| 10.00 | n | 0.7505 | 0.7979 |
| 10.00 | p | 0.7961 | 0.8237 |
| 15.20 | n | 0.9890 | 0.9911 |
| 15.20 | p | 0.9918 | 0.9930 |

Thus the old \(\pm60\) MeV window captures only **75.05%--99.30%** of the full outgoing-energy integral over this benchmark. The largest missing fraction is 24.95%, for a neutron neutrino at 10 km. At 5 km, the neutron-neutrino window misses 23.43%; at 0.20 km it misses 14.57%. The outer 15.20 km cases are close to complete, with approximately 99% captured.

This is a material correction to the interpretation of C4-B2: its \(\pm60\) MeV results are valid finite-window diagnostics, but they are not complete local differential-in-angle rates in the inner and intermediate regions. The full-support C4-C1 values supersede those truncated values for the same benchmark. No B.2 opacity or luminosity was computed from the truncated C4-B2 numbers.

## 5. Quadrature and limiting checks

The full \(E_\nu'\) integral is evaluated with Gauss-Legendre orders 32, 48, and 72, while retaining 48-node initial-momentum and 16-point azimuthal integrations.

| Diagnostic | Maximum relative residual | Acceptance |
|---|---:|---:|
| \(E_\nu'\) order 48 vs 72 | \(7.10\times10^{-5}\) | \(<10^{-2}\) |
| \(E_\nu'\) order 32 vs 72 | \(1.35\times10^{-3}\) | \(<2\times10^{-2}\) |
| Support-root closure | \(3.85\times10^{-13}\) | \(<10^{-7}\) |
| Cold/dilute full-support Horowitz limit | \(8.04\times10^{-6}\) | \(<10^{-3}\) |

In the cold/dilute benchmark \(n_B/n_0=10^{-10}\), \(T=10^{-3}\) MeV, the full-support outgoing-energy interval is approximately 2.725 MeV wide. Integrating it recovers the stationary Horowitz differential cross section within 8.1 parts per million for both species and neutrino/antineutrino.

All 16 local cases have positive full-support rates, and all 6 unit tests pass.

## 6. Independent CI and archived outputs

**C4-C1 status: PASS.**

GitHub Actions Run:
https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43009019757

- 6/6 unit tests passed.
- The exact support roots and all 16 full-support local integrals were independently recomputed.
- The output-validation step passed all nine acceptance conditions.
- Artifact: \`c4c1-exact-outgoing-energy-support\`, ID \`13849588359\`, 90-day retention.

The artifact contains:
- \`summary.json\`;
- \`support_roots.csv\` (eight unique radius/species support intervals);
- \`local_full_support.csv\` (16 neutrino/antineutrino full-support and \(\pm60\) MeV comparisons);
- \`cold_horowitz.csv\` (four cold/dilute limiting cases).

## 7. Physical interpretation and next step

The \(\pm60\) MeV window is not a uniformly accurate approximation to the local outgoing-energy integral. Its error is radius-, species-, and neutrino-sign-dependent, reaching roughly 25% in the selected inner/intermediate neutron cases. Therefore it cannot be used as a global normalization shortcut.

C4-C2 must now integrate over the complete outgoing-angle range, using the full \(E_\nu'\) support established here. The cold/dilute angle-integrated result must recover the total Horowitz cross section before any 301-radius total scattering rate or optical-depth calculation is attempted.

The present C4-C1 result remains differential in outgoing angle and is not a total cross section, total opacity, radial transport solution, or luminosity.
