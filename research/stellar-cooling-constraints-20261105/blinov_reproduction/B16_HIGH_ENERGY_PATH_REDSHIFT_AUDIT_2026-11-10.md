# 10 MeV high-energy B.2 fixed-energy versus path-redshift audit

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Input PR head: \`8406eb809d2485f2489645bc1d05a7e42aaabb67\`  
Machine-readable result: [b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-10.json](outputs/b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-10.json)

## 1. Purpose and scope

This calculation quantifies the effect of a **counterfactual path-redshift sensitivity** relative to the literal fixed-\(\omega\) Eq. (B.2) prescription, and does so only for the \(210\text{--}510\) MeV emission-energy band. The displayed Eq. (B.2) itself explicitly uses fixed \(\omega\); this is not an ambiguity in the printed equation.

The B.1 source distribution is identical in both cases.

## 2. Definitions

Printed-equation baseline:
\[
\omega_{\rm local}(s)=\omega_{\rm source},\qquad
v(s)=\sqrt{1-\frac{m_V^2}{\omega_{\rm source}^2}}.
\]

Path-redshift sensitivity:
\[
\omega_{\rm local}(s)=\omega_{\rm source}
\frac{N(r_{\rm source})}{N(r(s))},\qquad
v(s)=\sqrt{1-\frac{m_V^2}{\omega_{\rm local}(s)^2}}.
\]

The second prescription updates the local thermal kernel, reduced absorption, and velocity along the ray while retaining the same Euclidean straight chord. It is not a full-GR ray trace and is not substituted for the printed B.2 baseline.

## 3. Numerical closure

At \(m_V=10\,\mathrm{MeV}\), \(g=4.171689650228597\times10^{-8}\), the fixed-\(\omega\) branch reproduces the previously archived high-energy phase-space integral:
- B.1 source relative residual: \(-3.331\times10^{-16}\);
- fixed-\(\omega\) escaped-integral relative residual: \(0.000\);
- fixed-\(\omega\) escape probability: \(2.345801\times10^{-3}\).

The same B.1 source is used for the redshifted path variant.

## 4. Main result

| Quantity | Fixed \(\omega\) | Path-redshift |
|---|---:|---:|
| B.1 source, per \(g^2\) | \(4.16859\times10^{69}\) | identical |
| Escape probability | \(2.345801\times10^{-3}\) | \(1.686751\times10^{-3}\) |
| Source-weighted mean \(\tau\) | \(7.7193\) | \(8.1169\) |
| Escaped luminosity | \(1.70178\times10^{52}\) | \(1.22367\times10^{52}\,\mathrm{erg\,s^{-1}}\) |

The path-redshift prescription lowers the \(210\text{--}510\) MeV escaped luminosity by **\(-28.09\%\)** relative to the fixed-\(\omega\) baseline. The source-weighted mean optical depth increases by \(5.15\%\).

### Sub-band response

| Emission-energy bin | Fixed-\(\omega\) escape probability | Path-redshift escape probability | Escaped-luminosity change |
|---|---:|---:|---:|
| \(210\text{--}300\) MeV | \(1.6308\times10^{-3}\) | \(1.1308\times10^{-3}\) | \(-30.66\%\) |
| \(300\text{--}510\) MeV | \(5.4424\times10^{-3}\) | \(4.0942\times10^{-3}\) | \(-24.77\%\) |

The lower \(210\text{--}300\) MeV part of the dominant tail is more sensitive than the \(300\text{--}510\) MeV part.

## 5. Equation-level decision and interpretation

The published B.2 equation explicitly writes \(\Gamma_{\rm abs}^{*}(r'(s),\omega)\) and \(v_V(\omega)\) along the full chord. It does not insert a path-dependent lapse ratio into the energy argument. Therefore fixed-\(\omega\) is the literal equation-level reproduction baseline.

The path-redshift branch is retained only as a counterfactual transport sensitivity. It changes the local energy argument and velocity while retaining a Euclidean chord; it is not a full-GR ray trace and must not be used to tune or replace the Fig. 7 reproduction baseline.

The separate global 10 MeV path-redshift diagnostic reduced the strong-endpoint Fig. 7 residual from \(+92.24\%\) to \(+36.74\%\), but did not close it. That global all-energy result is distinct from the \(-28.09\%\) change in the present \(210\text{--}510\) MeV band.

## 6. Reproducibility qualification

The referenced global-band JSON declares a direct V8 JavaScript binary64 execution and has no Python script hash. The repository's \`audit_b16_high_energy_nu_energy_convention.py\` is a **targeted local-ray** diagnostic; it evaluates selected rays and writes a separate \`b16_high_energy_nu_energy_convention...\` output. It does not calculate the global \(210\text{--}510\) MeV luminosity comparison archived here.

Thus the targeted-ray Python script is not a strict Python reproduction of this global-band JSON. A separate NumPy implementation and output archive for the energy-integrated band remain required. The V8 output is retained as cross-runtime evidence only.

## 7. Physical disposition

The path-redshift prescription materially changes the dominant high-energy escaping component, but it does not establish which prescription the authors' unpublished numerical code used. The displayed equation-level baseline remains fixed-\(\omega\). The redshifted branch retains Euclidean chords and is not full GR.

The same-snapshot metric and thermodynamic profile remain unavailable. No opacity, source normalization, energy cutoff, coupling, or axial-vector constraint curve is adjusted to force agreement with Fig. 7.

## 8. Strict NumPy global-band reproduction and interpolation audit (2026-11-15)

A strict NumPy reproduction of the archived \(210\text{--}510\) MeV comparison is now available at [b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-15_numpy.json](outputs/b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-15_numpy.json).

- Output SHA-1 (Git blob): \`77c40bc10ca8dca8af7be261ae2344b176389647\`.
- Script SHA-256: \`d18de99fd57e7d894d0861d68b362d3d40b4c6afd17b1329f6be486f36fc918e\`.
- Run commit: \`9d7665560d61479b2cda653b2dd842a4340b14d6\`.
- Execution and five V8-comparison tests: [GitHub Actions #43648694518](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43648694518).

The important numerical detail is that the archived V8 result specifies **bilinear interpolation in radius and local energy** for the path-redshift opacity. The strict NumPy implementation now reproduces that exact interpolation prescription. Its fixed-\(\omega\) and path-redshift luminosities, escape probabilities, mean optical depths, channel fractions, and two sub-band changes agree with V8 at relative differences below \(3\times10^{-14}\).

The reproduced bilinear result is:
- fixed-\(\omega\) escape probability: \(2.3458008936\times10^{-3}\);
- path-redshift escape probability: \(1.6867510535\times10^{-3}\);
- \(210\text{--}510\) MeV escaped-luminosity change: \(-28.09487548\%\);
- source-weighted mean-\(\tau\) change: \(+5.15093986\%\);
- \(210\text{--}300\) MeV escaped-luminosity change: \(-30.65510027\%\);
- \(300\text{--}510\) MeV escaped-luminosity change: \(-24.77264570\%\).

### Direct local-rate recomputation is a separate numerical method

The same script also retains an independent alternative that recomputes the local rates directly from the interpolated thermodynamic fields at each path node, rather than bilinearly interpolating the precomputed opacity grid. That alternative gives an escaped luminosity \(0.5021\%\) above the bilinear result and a source-weighted mean optical depth \(0.0810\%\) below it.

This is not a failure of the V8 reproduction: it is a method-dependent interpolation difference. The archived V8 result is specifically the bilinear-grid calculation, so only the bilinear branch is used for the strict V8 comparison. Both methods are retained and labeled separately; neither is promoted to the printed Eq. (B.2) baseline.

This supersedes the earlier Section 6 qualification that the global-band NumPy output was missing. The physical disposition is unchanged: fixed-\(\omega\) remains the literal Eq. (B.2) baseline; path-redshift is a counterfactual Euclidean-chord sensitivity, not a full-GR ray trace and not a fitted correction to Fig. 7.
