# B.6--B.10 and B.13--B.19: independent local absorption audit

> **Historical profile version:** the paired numerical output for this report uses the 501-node uniform profile, SHA-256 `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`. The current working input is the 1687-row vertex-preserving profile, SHA-256 `6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc`. The current-profile rerun and quantitative old/new comparison are documented in `PROFILE_VERSION_RECONCILIATION_2026-11-09.md`; see also `outputs/b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json`. Keep this report as a historical record and do not combine its numerical output with current-profile results.


Date: 2026-11-09  
Scope: pure-vector Blinov reference prescription at \(m_V=10\) MeV.  
Status: **the local implementation of the published B.6--B.10 and B.14--B.19 formulae closes numerically; the physical accuracy of the B.14--B.16 no-recoil approximation at 10 MeV remains a separate unresolved question.**

## 1. Executive result

The independent local audit compares the reference implementation against:

- direct two-body angular phase-space integration for \(\nu_\mu\) and \(\nu_\tau\), separately;
- direct inverse-occupation integrals for the neutrino absorption rate;
- an independently evaluated B.17 muon susceptibility using a transformed Gauss--Legendre integral;
- the B.14--B.17 Compton formula, followed independently by B.19 and B.4;
- the total local production, absorption, and reduced-absorption sums.

For the sampled \(m_V=10\) MeV profile points, the maximum residual in the total local reduced absorption is \(2.26\times10^{-14}\). The Compton B.16 production rate agrees with the reference implementation to \(4.91\times10^{-14}\) after fixing a low-density quadrature-tolerance problem in reference.py.

No axial production code, transport code, luminosity output, or plotted constraint curve is changed.

## 2. Equation map and conventions

The published Appendix B distinguishes the following relations:

| Equation | Use in this audit |
|---|---|
| B.4 | \(\Gamma_{\rm abs}^*=(1-e^{-\omega/T})\Gamma_{\rm abs}\) |
| B.6--B.9 | Neutrino inverse-decay production |
| B.10 | Neutrino inverse-decay detailed balance |
| B.13 | Full \(\mu\gamma\to\mu V\) thermal phase-space integral |
| B.14--B.18 | Non-relativistic/no-recoil Compton approximation and its cross-section relations |
| B.19 | Compton detailed balance |

The neutrino and Compton detailed-balance equations are checked separately. B.10 is not used as a substitute for B.19.

For the Compton reference calculation, the printed one-species B.17 convention is followed:
\[
n_\mu F_{\rm deg}
=
\int \frac{2\,d^3p}{(2\pi)^3}
f_\mu(E;\mu_\mu)\,[1-f_\mu(E;\mu_\mu)]
=
\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f_\mu(1-f_\mu).
\]

With \(\alpha_V/g_X^2=1/(4\pi)\), B.14 and B.16 give
\[
\frac{\Gamma_{\rm C}^{\rm prod}}{g_X^2}
=
\frac{4\alpha}{3m_\mu^2}\,
\frac{n_\mu F_{\rm deg}}{e^{\omega/T}-1}
\left(1+\frac{m_V^2}{2\omega^2}\right).
\]
The \(v_V\) in the B.14 cross section cancels the explicit \(1/v_V\) in B.16. Applying B.19 and B.4 then gives
\[
\boxed{
\frac{\Gamma_{\rm C}^{*,\rm abs}}{g_X^2}
=
\frac{4\alpha}{3m_\mu^2}\,
n_\mu F_{\rm deg}
\left(1+\frac{m_V^2}{2\omega^2}\right)
}.
\]
This closed form is evaluated independently of the production routine.

## 3. Independent numerical methods

### 3.1 Neutrino inverse decay

For each flavor, the audit integrates the angular variable directly:
\[
E_{1,2}=\frac{\omega}{2}(1\pm v_V z),
\qquad
v_V=\sqrt{1-\frac{m_V^2}{\omega^2}}.
\]
The three polarization weights are integrated separately. Production uses the two Fermi occupations; absorption uses the two blocking factors. The direct results are compared with the analytic Fermi-pair antiderivative in reference.py.

### 3.2 Compton susceptibility

The B.17 integral is evaluated independently with
\[
x=\frac{E-m_\mu}{T}=t^2,
\qquad
p=\sqrt{Tx(2m_\mu+Tx)}.
\]
This transformation resolves the \(p=0\) endpoint and is numerically independent of the adaptive momentum-space quadrature in reference.py.

The independent susceptibility is then inserted into B.14--B.17. B.19 and B.4 are applied separately.

### 3.3 Sampled domain

- \(m_V=10\) MeV;
- radii: \(8,10,12,15,18.5,20,22,23,24,25\) km;
- local vector energies: \(12,15,20,30,50,100\) MeV;
- direct neutrino angular quadrature: 512-point Gauss--Legendre;
- independent B.17 susceptibility quadrature: 256-point Gauss--Legendre.

The dimuon channel is kinematically closed at this mediator mass.

## 4. Numerical closure

| Check | Maximum relative residual |
|---|---:|
| \(\nu_\mu\): direct B.6 vs analytic reference | \(4.77\times10^{-15}\) |
| \(\nu_\tau\): direct B.6 vs analytic reference | \(6.05\times10^{-15}\) |
| \(\nu_\mu\): B.10 detailed balance | \(2.67\times10^{-15}\) |
| \(\nu_\tau\): B.10 detailed balance | \(2.67\times10^{-15}\) |
| Neutrino B.4 reduced opacity | \(2.72\times10^{-15}\) |
| Compton B.16 production vs reference implementation | \(4.91\times10^{-14}\) |
| Compton B.19 detailed balance | \(2.19\times10^{-16}\) |
| Compton B.4 reduced opacity | \(2.26\times10^{-16}\) |
| Total local production closure | \(2.23\times10^{-14}\) |
| Total local absorption closure | \(2.28\times10^{-14}\) |
| Total local reduced-absorption closure | \(2.26\times10^{-14}\) |

The total closure compares the independently reconstructed channel sum with the original local-rate implementation. It is not a fit to the global luminosity.

## 5. Numerical issue found and corrected

The first independent run showed a maximum \(10.85\%\) relative discrepancy between the B.16 Compton rate and reference.py. It occurred only in the dilute outer profile where the muon chemical potential is set to zero.

The cause was the absolute integration tolerance in negative_muon_density_and_degeneracy:
\[
\texttt{epsabs}=10^{-9},\qquad \texttt{epsrel}=2\times10^{-9}.
\]
The actual outer-shell susceptibility is much smaller than \(10^{-9}\,\mathrm{MeV}^3\). QUADPACK could therefore terminate without resolving the relative size of the dilute Fermi tail.

Representative values:

| Radius | \(T\) (MeV) | \(\mu_\mu\) (MeV) | Independent \(n_\mu F_{\rm deg}\) (MeV\(^3\)) | Old adaptive result (MeV\(^3\)) | Old relative deficit |
|---:|---:|---:|---:|---:|---:|
| 23 km | 3.3840 | 0 | \(2.50940\times10^{-11}\) | \(2.26387\times10^{-11}\) | 9.78% |
| 24 km | 3.2164 | 0 | \(4.55705\times10^{-12}\) | \(4.19043\times10^{-12}\) | 8.05% |
| 25 km | 3.0338 | 0 | \(5.77406\times10^{-13}\) | \(5.43135\times10^{-13}\) | 5.94% |

The reference integral now uses relative convergence (\(\texttt{epsabs}=0.0\), \(\texttt{epsrel}=2\times10^{-9}\)). A regression test compares the adaptive result with the independent transformed quadrature at all three dilute-tail temperatures.

After this correction, the maximum B.16 production discrepancy falls to \(4.91\times10^{-14}\).

This numerical defect is immaterial to the 10 MeV outer-shell optical depth: over the sampled \(r\geq22\) km points, the Compton contribution is at most \(6.45\times10^{-15}\) of the total local reduced opacity. It is nevertheless corrected because the local rate should be numerically reliable independently of whether a channel is dominant.

## 6. Important distinction: B.16 implementation vs the exact B.13 kernel

Passing the local B.16 audit does **not** establish that the B.14--B.16 approximation is physically accurate for \(m_V=10\) MeV.

The separate B.13 full moving-muon calculation already shows a substantial difference from B.14--B.16:

| Local point | Exact B.13 vector Compton emissivity | B.14--B.16 vector emissivity | B.13 / B.16 |
|---|---:|---:|---:|
| \(r=0\) km | 13.6975 | 28.5916 | 0.479 |
| \(r=12.5\) km | 381.1135 | 889.2185 | 0.429 |

At \(r=12.5\) km, the fixed-energy B.13/B.16 rate ratios are approximately 0.57--0.58 for \(\omega=12\)--20 MeV, 0.56 at 30 MeV, and decrease further at higher energies.

This is not a failure of the B.16 algebraic implementation. It is a difference between:

1. the full moving-muon/recoil phase-space calculation in B.13; and
2. the non-relativistic, negligible-recoil approximation used to obtain B.14--B.16.

The distinction matters for transport. In the B.16 baseline, Compton supplies up to 42.6% of the local reduced opacity at the sampled \(8\)--15 km points. It is therefore not safe to dismiss the B.13/B.16 difference solely because Compton is a modest part of the thin source.

The paper notes that this Compton approximation is conventionally most relevant for \(m_V\lesssim\) MeV. The 10 MeV benchmark is outside that stated typical regime. Before declaring the 10 MeV vector transport benchmark physically validated, we must establish whether the published numerical curve used the B.14--B.16 approximation as implemented here or the full B.13 integral. The exact B.13 result is retained as a separate diagnostic and is **not** substituted into the reference baseline at this stage.

## 7. Interpretation and next step

The following conclusions are supported:

1. The direct B.6 neutrino production and absorption integrals are correct to numerical precision.
2. The B.10 and B.4 neutrino relations close independently.
3. The B.14--B.17 Compton implementation, including the \(1/v_V\) factor, B.19, and B.4, is internally correct to numerical precision.
4. A low-density absolute-tolerance defect in the reference muon susceptibility integral is fixed. Its effect on the 10 MeV outer-shell opacity is negligible.
5. The physical validity of using the B.14--B.16 Compton approximation at \(m_V=10\) MeV remains unresolved and is potentially relevant in the inner opacity region.

Accordingly, the pure-vector transport curve remains **not yet validated**. No empirical rescaling is applied, and no axial-vector curve is regenerated.

## 8. Reproducibility files

- audit_b16_local_absorption.py: independent local B.6/B.10/B.4 and B.14--B.19 calculation.
- test_b16_local_absorption.py: direct phase-space, susceptibility convergence, B.19 and dilute-tail regression tests.
- reference.py: relative-tolerance correction in the B.17 susceptibility quadrature.
- outputs/b16_local_absorption_10mev_2026-11-09.json: pointwise machine-readable results.
- .github/workflows/b16-local-absorption.yml: automated test and audit workflow.

The original profile remains a public-figure reconstruction, not the raw Garching simulation table.
