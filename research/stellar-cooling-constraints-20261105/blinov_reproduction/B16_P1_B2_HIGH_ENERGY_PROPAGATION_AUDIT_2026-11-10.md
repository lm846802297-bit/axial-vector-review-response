# P1 B.2 high-energy propagation audit (2026-11-10)

**PR:** #57  
**Branch:** `research/moving-muon-thermal-rates-20261107`  
**Benchmark:** \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
**Profile:** vertex-preserving SFHo-18.8 reconstruction, SHA-256  
`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`  
**Machine-readable result:** `outputs/b16_p1_b2_high_energy_propagation_audit_2026-11-10.json`

## 1. Scope and acceptance question

This P1 audit targets the strong-coupling B.2 propagation kernel in the energy interval that dominates the escaping luminosity. The 210--510 MeV band contains 9.670% of the optically-thin source but contributes 69.756% of the escaped luminosity. The question is whether a hidden path quadrature, angular quadrature, or radial-opacity interpolation effect could account for the \(+92.2406\%\) fixed-\(\omega\) strong-endpoint discrepancy.

The calculations below are direct V8 binary64 computations executed in the current calculation environment, not GitHub Actions jobs. They retain the literal fixed-\(\omega\), scalar-opacity, Euclidean-chord B.2 baseline unless a separately labelled path-redshift diagnostic is being evaluated. No source, opacity normalization, coupling, or axial-vector curve is changed.

## 2. Direct path-coordinate integration versus the analytic radial primitive

The first check evaluates the optical-depth integral directly in the path coordinate \(s\), rather than using the analytic radial primitive. The path is split at every crossing of the 642-node opacity interpolation grid, each radial shell boundary, and the turning point for inward-going rays. Both neutrino inverse decay and semi-Compton opacity are integrated separately.

The 108-ray set covers:
- emission radii \(r_0=8,10,12.5,15\) km;
- energies \(\omega=210,300,510\) MeV;
- \(\cos\theta=-1,-0.9999,-0.75,-0.25,0,0.25,0.75,0.95,1\).

| Direct path quadrature | Maximum absolute relative difference from analytic radial primitive |
|---:|---:|
| 2-point Gauss per split segment | \(1.035\times10^{-7}\) |
| 4-point Gauss per split segment | \(8.293\times10^{-14}\) |
| 8-point Gauss per split segment | \(6.595\times10^{-14}\) |

The check explicitly includes exact central crossing (\(\cos\theta=-1\)), near-central crossing, tangential emission (\(\cos\theta=0\)), and exactly outward radial emission (\(\cos\theta=1\)). Thus the agreement is not restricted to generic outward rays.

An independent angular integration using composite Simpson orders 128, 256, and 512 and Gauss--Legendre orders 32 and 64 gives a maximum \(256\)-to-\(512\) Simpson change of \(1.17\times10^{-8}\), and a maximum Gauss-64 versus Simpson-512 difference of \(5.77\times10^{-7}\) over the four representative high-energy \((r_0,\omega)\) pairs.

**Result:** the path-coordinate implementation and the analytic radial primitive agree to floating-point precision once four Gauss points are used per profile segment. No high-energy path or angle quadrature error of phenomenological significance is found.

## 3. Does the 642-node opacity grid smooth over the original profile vertices?

The current B.2 opacity grid contains 642 nodes (640 composite Gauss--Legendre nodes plus the two radial endpoints). The thermodynamic profile itself contains 1687 retained vertices. To test whether the opacity grid smooths over a narrow feature or a profile-vertex kink, the local B.16 reduced opacities are recomputed on both:
1. the 642-node opacity interpolation grid; and
2. all 1687 retained profile vertices.

The same exact piecewise-linear radial chord primitive is then applied to 60 rays with \(r_0=8,10,12.5,15\) km, \(\omega=210,300,510\) MeV, and \(\cos\theta=-0.75,-0.25,0.25,0.75,0.95\).

| Quantity | Maximum absolute relative change, 1687 vertices versus 642 opacity nodes |
|---|---:|
| Neutrino optical depth | \(1.15\times10^{-6}\) |
| Semi-Compton optical depth | \(6.74\times10^{-4}\) |
| Total optical depth | \(1.87\times10^{-5}\) |
| Single-ray escape probability | \(1.57\times10^{-4}\) |

The largest channel-specific change occurs in the Compton optical depth, but its effect on the total optical depth remains much smaller because the neutrino contribution dominates the outer path. For four representative angle-averaged escape probabilities at \(r_0=8,12.5\) km and \(\omega=210,510\) MeV, the 1687-vertex versus 642-node change ranges from \(-2.18\times10^{-5}\) to \(+1.21\times10^{-5}\).

A representative \(r_0=10\) km, \(\omega=300\) MeV, \(\cos\theta=0.75\) ray also shows that shell-by-shell changes nearly cancel: the largest individual shell shift in \(\tau_\nu+\tau_C\) is below \(1.0\times10^{-5}\).

**Result:** retaining every original profile vertex does not reveal a hidden radial interpolation error. The existing 642-node opacity interpolation is adequate for the sampled high-energy propagation problem; its residual effect is orders of magnitude below the Fig. 7 discrepancy.

## 4. Channel attribution of the path-redshift sensitivity

The path-redshift branch is not the published fixed-\(\omega\) B.2 baseline. It is evaluated only to determine which absorption channel produces the already observed redshift sensitivity:
\[
\omega_{\rm local}(s)=\omega_{\rm source}
\frac{N(r_{\rm source})}{N(r(s))}.
\]

A new direct-\(s\) calculation uses all 1687 profile vertices as path breakpoints, four-point Gauss--Legendre integration per segment, a 64-point Gauss--Legendre Fermi-pair angular average, and an independently integrated muon susceptibility. It compares fixed-\(\omega\) and path-redshift optical depths on 36 representative rays:
- \(r_0=8,10,12.5,15\) km;
- \(\omega_{\rm source}=210,300,510\) MeV;
- \(\cos\theta=-0.75,0.25,0.75\).

The following are **unweighted descriptive statistics across these 36 selected rays**, not source-weighted global averages:

| Channel | Mean relative change in \(\tau\) | Minimum | Maximum |
|---|---:|---:|---:|
| Neutrino inverse decay | +4.976% | -0.926% | +9.634% |
| Semi-Compton | +0.000256% | -0.0221% | +0.0131% |
| Total | +4.107% | -0.567% | +7.906% |

The path integral is also checked by increasing the direct-\(s\) quadrature from 4 to 8 Gauss points per profile segment. Across six representative inward and outward rays, the maximum relative change is \(1.71\times10^{-14}\) for the Compton column and \(1.05\times10^{-14}\) for the neutrino column. The Fermi-pair angular average changes by at most \(4.77\times10^{-7}\) from 32 to 64 Gauss points and \(1.80\times10^{-12}\) from 64 to 128 points.

For a representative \(r_0=10\) km, \(\omega_{\rm source}=300\) MeV, \(\cos\theta=0.75\) ray:

| Channel | Fixed-\(\omega\) \(\tau\) | Path-redshift \(\tau\) | Relative change |
|---|---:|---:|---:|
| Neutrino inverse decay | 3.67037 | 3.95539 | +7.765% |
| Semi-Compton | 0.540303 | 0.540325 | +0.00414% |
| Total | 4.21067 | 4.49571 | +6.769% |

The shell decomposition shows where this occurs. The neutrino optical-depth contribution grows progressively toward the outer path:
- 10--12 km: \(0.50590\to0.51171\);
- 12--15 km: \(0.73432\to0.76499\);
- 15--18 km: \(0.73625\to0.79228\);
- 18--20 km: \(0.48820\to0.53625\);
- 20--22 km: \(0.48473\to0.53899\);
- 22--24 km: \(0.48132\to0.54042\);
- 24--25 km: \(0.23966\to0.27075\).

The Compton contribution is concentrated inside 15 km and changes negligibly under the path-redshift prescription. The redshift sensitivity is therefore carried almost entirely by neutrino inverse-decay opacity, not by semi-Compton absorption.

The previously archived global 210--510 MeV result is consistent with this channel attribution: the path-redshift prescription lowers the band escape probability from \(2.345801\times10^{-3}\) to \(1.686751\times10^{-3}\) and the escaped luminosity from \(1.70178\times10^{52}\) to \(1.22367\times10^{52}\) erg/s, a \(-28.09\%\) change. The B.1 source is identical in the two branches. This global result is source weighted; the 36-ray channel statistics above are not.

**Interpretation:** the energy convention is a material physical transport sensitivity, and its effect is neutrino-opacity dominated. It is not a numerical path-integration error and it does not justify replacing the printed fixed-\(\omega\) prescription.


## 4.1 Source-weighted global Shapley attribution of the path-redshift effect

The preceding 36-ray channel comparison is a local diagnostic. To determine the channel responsible for the *global* high-energy luminosity shift, a second calculation was performed with the same high-order Eq. (B.1) source measure and the archived B.2 quadrature configuration:
- 200 independent source-radius nodes;
- 640 opacity radial nodes;
- 842 energy nodes in the full integration grid, with 10 nodes in the 210--510 MeV band;
- 32 angular nodes and 64 path nodes.

Four counterfactual transport calculations were evaluated with identical B.1 source weights:
\(L_{00}\): fixed-\(\omega\) neutrino and Compton opacity;
\(L_{10}\): redshifted neutrino opacity, fixed-\(\omega\) Compton opacity;
\(L_{01}\): fixed-\(\omega\) neutrino opacity, redshifted Compton opacity;
\(L_{11}\): both channels redshifted.
The channel contributions are assigned with the two-player Shapley decomposition, so the nonlinear cross term is shared symmetrically.

| Counterfactual | 210--510 MeV escaped luminosity (erg/s) |
|---|---:|
| \(L_{00}\): both fixed | \(1.70178483\times10^{52}\) |
| \(L_{10}\): neutrino redshift only | \(1.22372442\times10^{52}\) |
| \(L_{01}\): Compton redshift only | \(1.70170496\times10^{52}\) |
| \(L_{11}\): both redshifted | \(1.22367050\times10^{52}\) |

The source normalization is \(4.1685932062\times10^{69}\) erg/s per \(g^2\), agreeing with the archived high-energy source measure at relative residual \(1.88\times10^{-11}\). The fixed-\(\omega\) band luminosity agrees with the archived result at \(2.84\times10^{-6}\) relative residual; the bilinear path-redshift result agrees at \(4.09\times10^{-7}\).

| Shapley contribution | Luminosity change (erg/s) | Fraction of total change |
|---|---:|---:|
| Neutrino inverse decay | \(-4.78047434\times10^{51}\) | **99.9860%** |
| Semi-Compton | \(-6.68950648\times10^{47}\) | **0.0140%** |
| Total | \(-4.78114329\times10^{51}\) | 100% |

This is the source-weighted global result, not an unweighted average over selected rays. It establishes that the global 28.0949% high-energy-band luminosity reduction in the bilinear path-redshift branch is almost entirely caused by neutrino inverse-decay opacity. The semi-Compton contribution is negligible.

A separate calculation evaluates the local opacity kernels directly at \(\omega_{\rm local}(s)\), rather than bilinearly interpolating in local energy. It gives \(L_{11}=1.22981457\times10^{52}\) erg/s, about 0.502% above the bilinear result, while the fixed-\(\omega\) result is unchanged. Its Shapley fractions are 99.9864% neutrino and 0.0136% Compton. Thus the interpolation choice changes the redshift-only luminosity at the half-percent level but does not change the channel attribution.

The path-redshift calculation remains a sensitivity analysis, not the published fixed-\(\omega\) Eq. (B.2) benchmark. It is not used to adjust the Fig. 7 curve.


## 5. Boundary and published-equation interpretation

The version-of-record paper, Blinov et al., JHEP 06 (2026) 155, Eq. (B.2) explicitly writes the same \(\omega\) in \(\Gamma_{\rm abs}^{*}(r'(s),\omega)\) and \(v_V(\omega)\) along the chord. The path-redshift branch is retained only as a separately labelled physical sensitivity. The paper identifies \(R_{\max}\) with the neutrinosphere \(R_\nu\simeq25\) km; the 25 km endpoint is therefore the published escape boundary, not an arbitrary numerical truncation. See [Blinov et al., JHEP 06 (2026) 155](https://doi.org/10.1007/JHEP06(2026)155), Appendix B and the paragraph following Eq. (B.2).

## 6. P1 decision

1. Direct path integration, analytic radial integration, and angular integration agree at high precision on the targeted 210--510 MeV rays.
2. Replacing the 642-node opacity grid with all 1687 profile vertices changes total optical depths and angle-averaged escape probabilities by at most the \(10^{-4}\) level.
3. The path-redshift sensitivity is attributable to neutrino inverse decay; semi-Compton opacity is essentially unchanged.
4. The printed fixed-\(\omega\), scalar-opacity B.2 expression remains the Fig. 7 reproduction baseline. The path-redshift result is not substituted.
5. The \(+92.2406\%\) fixed-\(\omega\) strong-endpoint residual remains unresolved. These P1 tests do not establish the original same-snapshot Garching profile and do not reproduce the unpublished numerical code.

**P1 numerical propagation audit: complete for the targeted high-energy B.2 path, angle, and opacity-interpolation checks.** Further generic increases of path or angle quadrature order are not justified. The remaining reproduction limitation is physical/input-level: the public-figure stellar profile is not the original Garching snapshot, and the unpublished implementation cannot be inspected.

No opacity, source normalization, profile, coupling, vector curve, or axial-vector result is modified. No empirical rescaling is applied.


## 7. P1-B thermodynamic-input follow-up (2026-11-10)

The local-field interpolation and source-frozen high-energy sensitivity tests are archived in [B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md](B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md).

The main numerical result is that evaluating the local B.16 kernel directly from linearly interpolated \(T,\mu_{\nu_\mu},\mu_\mu\) at the path nodes, rather than interpolating the precomputed 642-node opacity table, changes the sampled total optical depth by at most \(9.07\times10^{-6}\). Thus the previous vertex-preserving opacity test is not hiding a nonlinear-kernel interpolation effect.

The source-frozen 210--510 MeV global calculation also shows that the inner semi-Compton opacity is sensitive to broad \(T,\mu_\mu\) variations, while the \(\mu_{\nu_\mu}\) sensitivity is below \(0.03\%\) for \(\pm10\%\) changes. The \(T,\mu_\mu/T\) inputs are independently anchored to Bollig Figs. 1 and 4 at the \(10^{-4}\) relative scale. These results do not support a profile correction or opacity rescaling and do not explain the \(+92.2406\%\) fixed-\(\omega\) strong-endpoint residual.

The next unresolved B.2 issue is the normalization map between polarization-summed production, per-polarization inverse absorption, and the scalar absorption rate in the B.2 exponent. This must be derived from B.6--B.10 before any alternative opacity convention is considered.
