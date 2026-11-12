# 10 MeV Fig. 7 Follow-up Diagnostic — 2026-11-08

## Executive summary

The requested follow-up is now split into four evidence-based conclusions:

1. **Energy convention:** the printed Appendix-B Eq. (B.2) carries the same symbol \(\omega\) along the chord, but the paper's main-text Eq. (4.2) describes \(\omega\) as the energy at spatial infinity, whereas the lower limit \(m_V/N(r)\) and the local thermal factors in Appendix B indicate a local production-frame energy. This is a genuine notation/convention ambiguity between the main-text description and the detailed Appendix-B formulae. The fixed-\(\omega\) code remains the literal Eq. (B.2) lane; the conserved-\(E_\infty\) path remains a separate physical diagnostic. The authors' unpublished numerical implementation cannot be inferred from the printed formula alone.
2. **Fig. 7 digitization:** the 10 MeV violet curve is reconstructed from native vector-path vertices in the pinned arXiv v2 PDF, not from screenshot pixels. The digitization audit passes at floating-point reconstruction precision. Ordinary raster digitization error is therefore not a credible explanation for the high-coupling residual, although the authors' original unplotted simulation samples remain unavailable.
3. **Spatial weights:** a new joint production-radius/absorber-radius matrix is computed with frozen local rates and the independently validated analytic path integral. It shows that most optically thin emission is produced at 5–15 km, while the neutrino optical depth accumulated at 15–25 km is important for every production shell and becomes dominant for outer production shells. At high coupling, the escaping luminosity is still dominated by production at 5–15 km.
4. **Fixed-background limitation:** the paper explicitly warns that above the \(\lambda_{\rm mfp}(T_{\max})=R_\nu\) line, the new vector can modify supernova energy transport and fixed-SM-profile constraints become uncertain. The 10 MeV high-coupling endpoint lies above this line. This is a physical-applicability caveat, **not** an explanation for the numerical mismatch between two calculations that both purport to use the same fixed profile.

No local collision rate, chemical potential, opacity normalization, coupling, or source term is fitted.

## 1. Energy convention: what the paper actually says

### 1.1 Appendix B, Eq. (B.2)

The printed escape factor is
\[
\mathcal O(r,\omega)=\frac12\int_{-1}^{1}d\mu\,
\exp\!\left[
-\frac{1}{v_V(\omega)}
\int_0^{s_{\max}}ds\,
\Gamma_{\rm abs}^{*}\!\left(r'(s),\omega\right)
\right],
\]
with
\[
r'(s)=\sqrt{r^2+s^2+2rs\mu}.
\]
The same numerical argument \(\omega\) appears in the local reduced absorption rate all along the chord. The literal reference implementation therefore keeps the energy-grid index fixed along the path.

### 1.2 A convention ambiguity between the main text and Appendix B

The main text's Eq. (4.2) explicitly describes \(\omega\) as the energy carried by \(V\) at spatial infinity. However, Appendix B's Eq. (B.1) contains
\[
N(r)^2\int_{m_V/N(r)}^\infty d\omega\,
k\,\omega^2\,\Gamma_{\rm prod}(r,\omega)\,\mathcal O(r,\omega).
\]
The lower limit \(m_V/N(r)\) is the escape threshold for a **local production-frame energy** \(\omega_{\rm loc}(r)\), because
\[
E_\infty=N(r)\,\omega_{\rm loc}(r),\qquad E_\infty\ge m_V.
\]
The phase-space momentum \(k=\sqrt{\omega_{\rm loc}^2-m_V^2}\), the local thermal factors \(\omega/T(r)\), and \(v_V=\sqrt{1-m_V^2/\omega^2}\) in Eqs. (B.5)–(B.19) likewise use a local energy in the medium rest frame.

Thus, when reading Eq. (B.1) literally, its integration variable is local at the production point. Along a GR trajectory, the local energy at another radius \(r'\) should be
\[
\omega_{\rm loc}(r')
=\frac{E_\infty}{N(r')}
=\frac{N(r)}{N(r')}\,\omega_{\rm loc}(r).
\]
Equation (B.2), however, does not explicitly display this remapping. The main-text statement that \(\omega\) is the energy at infinity and the Appendix-B local-energy measure are not reconciled by an explicit variable transformation in the paper.

This is not an arXiv-v2-only wording issue: the published JHEP 06 (2026) 155 version retains the same main-text energy-at-infinity statement and the same Appendix-B Eqs. (B.1)–(B.5). Its Data Availability Statement says no associated data will be deposited, and its Code Availability Statement says no associated code will be deposited. Therefore the public record does not allow us to determine whether the authors' numerical implementation follows the literal fixed-\(\omega\) Appendix-B expression or performs an energy remapping not displayed in Eq. (B.2).

### 1.3 Relation to the cited radiative-transfer derivation

The fixed-energy structure of Eq. (B.2) is not arbitrary: it follows the single-mode radiative-transfer treatment in Caputo, Raffelt, and Vitagliano, JCAP 08 (2022) 045, whose Boltzmann equation and optical-depth construction track a mode with fixed \(\omega\) along a ray in a stationary medium. Separately, Caputo et al., Phys. Rev. D 105, 035022 (2022), Sec. III A 5, explain the gravitational source correction: the energy at infinity is local energy times the lapse, the emission rate receives another lapse, and the distant-observer luminosity of a shell is multiplied by \(N(r)^2\). This directly supports the \(N(r)^2\) factor and the escape threshold in Eq. (B.1), but it does not by itself derive an \(r'\)-dependent local-energy remapping inside the attenuation integral.

The most conservative reading is therefore that Blinov et al. combine the fixed-\(\omega\) attenuation kernel inherited from the cited radiative-transfer prescription with the gravitationally corrected source luminosity and escape threshold. That is the literal baseline implemented here. The main-text phrase “energy at spatial infinity” remains insufficiently reconciled with the local-energy variable in Eq. (B.1); the conserved-\(E_\infty\) calculation is retained as a diagnostic of this ambiguity, not as a replacement for the published prescription.

**Decision:** preserve two separately labelled lanes:
- **Literal Appendix-B lane:** fixed numerical \(\omega\) in \(\Gamma_{\rm abs}^{*}(r',\omega)\), as printed in Eq. (B.2).
- **Conserved-\(E_\infty\) diagnostic:** evaluate \(\omega_{\rm loc}(r')=N(r)\omega_{\rm src}/N(r')\) and the corresponding \(v_V(r')\) along the same geometrical ray.

The second lane is a partial GR energy-remapping diagnostic on the same Euclidean chord geometry; it is not a complete GR ray-tracing calculation because the spatial metric/geodesic geometry is not changed. Neither lane is claimed to reveal the authors' unpublished internal code.

### 1.3 Existing numerical comparison

At the representative 10 MeV points already stored in the equation-chain audit:

| Point | Fixed-\(\omega\) luminosity | Conserved-\(E_\infty\) luminosity | Change |
|---|---:|---:|---:|
| Weak | \(9.8952\times10^{51}\) | \(9.8940\times10^{51}\) | \(-0.0121\%\) |
| Peak | \(1.9547\times10^{54}\) | \(1.8514\times10^{54}\) | \(-5.2818\%\) |
| High absorption | \(2.4370\times10^{52}\) | \(1.7239\times10^{52}\) | \(-29.2634\%\) |

At the high-absorption point, the digitized Fig. 7 value is \(1.2678\times10^{52}\,\mathrm{erg\,s^{-1}}\). The residual changes from \(+92.22\%\) to \(+35.97\%\), but does not vanish.

The energy-remapping effect is therefore large enough to matter, but it does not by itself reproduce Fig. 7. It must not be used as a fitted correction.

## 2. Fig. 7 digitization: exact PDF vector-path audit

The original arXiv v2 source archive member 'luminosity_snapshot_t=1.pdf' is pinned by SHA-256:
- source archive: ea5bf58438c6442f24b3b781842fdb4ccbec80383c53d605a44ddf224ade8729
- source PDF: 4d7d1d10bfe2b52992af94df98749fa3adac887c009cbf98515fa12e6c48fdb5

The 10 MeV violet curve is PDF drawing object 43:
- 27 line segments;
- 28 raw vector vertices;
- 25 vertices inside the visible plot rectangle;
- curve color matches the violet 10 MeV legend sample;
- all stored coupling and luminosity values round-trip from the native PDF coordinates with maximum relative residuals at or below \(2.22\times10^{-16}\);
- the major-tick calibration residuals are \(1.14\times10^{-5}\) and \(5.09\times10^{-6}\) PDF points.

The final visible point is
\[
g_{\mu\tau}=4.171689650228597\times10^{-8},\qquad
L_{\rm Fig.7}=1.267814759073720\times10^{52}\ {\rm erg\,s^{-1}}.
\]

This is stronger than a screenshot-pixel digitization: the stored curve follows the native vector path in the source PDF. The remaining limitation is that a plotted polyline is not the authors' original numerical table and does not recover any unplotted samples or interpolation choices.

## 3. Joint production-radius / absorber-radius decomposition

A new calculation uses:
- the frozen Caputo-digitized reconstructed SFHo-18.8 profile;
- unchanged local neutrino and semi-Compton rates;
- the same 25 km outer boundary;
- the analytic piecewise-linear path integral validated in the independent Eq. (B.2) audit;
- 128-point angular averaging;
- the exact Fig. 7 weak, peak, and high-absorption coupling points.

The local channel sum closes to the frozen total opacity at \(5.94\times10^{-16}\). Exact absorber-shell additivity is better than \(1.54\times10^{-14}\), and the total channel path agrees with the frozen total path at \(1.28\times10^{-15}\).

### 3.1 Thin-source radial distribution

| Production radius | Fraction of optically thin source |
|---|---:|
| 0–5 km | 0.91% |
| 5–10 km | 57.32% |
| 10–15 km | 39.80% |
| 15–20 km | 1.82% |
| 20–25 km | 0.147% |

Thus 97.12% of the optically thin source is produced between 5 and 15 km.

### 3.2 Neutrino optical depth: joint radial matrix

Each table entry below is \(g^2\) times the source-weighted mean neutrino optical-depth contribution from the absorber shell, conditional on production in the listed source shell. It is an optical-depth diagnostic, **not** an absorbed-luminosity fraction.

| Production radius | Absorber 0–5 km | 5–10 km | 10–15 km | 15–20 km | 20–25 km | Total \(\langle\tau_\nu\rangle\) |
|---|---:|---:|---:|---:|---:|---:|
| 0–5 km | 1.569 | 2.386 | 2.934 | 4.724 | 5.363 | 16.975 |
| 5–10 km | 0.256 | 2.164 | 2.790 | 3.505 | 3.703 | 12.417 |
| 10–15 km | 0.137 | 1.118 | 4.297 | 5.298 | 5.435 | 16.285 |
| 15–20 km | 0.088 | 0.614 | 3.734 | 15.750 | 15.384 | 35.571 |
| 20–25 km | 0.060 | 0.395 | 2.097 | 14.322 | 40.829 | 57.703 |

The fraction of neutrino optical depth accumulated in the outer 15–25 km is:

| Production radius | Outer 15–25 km fraction |
|---|---:|
| 0–5 km | 59.42% |
| 5–10 km | 58.04% |
| 10–15 km | 65.91% |
| 15–20 km | 87.53% |
| 20–25 km | 95.58% |

The outer shell is therefore important even for particles produced in the inner 5–15 km. For particles produced outside 15 km, it dominates the optical depth.

### 3.3 Semi-Compton absorption has a different radial distribution

At high coupling, the global source-weighted mean neutrino optical-depth contributions by absorber shell are
\[
(0.21705,\ 1.71884,\ 3.40734,\ 4.46879,\ 4.67504),
\]
which sum to 14.48706; the outer 15–25 km shells contribute 63.1173% of this mean. The corresponding semi-Compton contributions are
\[
(0.008925,\ 0.986431,\ 0.652782,\ 0.001244,\ 1.66\times10^{-12}),
\]
which sum to 1.64938. The two channels therefore have distinctly different radial distributions.

Thus:
- neutrino inverse decay supplies the extended outer 15–25 km opacity;
- semi-Compton absorption is concentrated mainly at 5–15 km;
- the outer neutrino opacity must not be mimicked by rescaling the semi-Compton rate.

At \(\omega=10.1\) MeV, the local reduced neutrino opacity is about 0.057–0.060 MeV over the inner 0–10 km, then reaches 0.1395 MeV near 15 km, 0.4168 MeV near 20 km, and 0.5358 MeV at 25 km. The semi-Compton reduced opacity peaks near 10 km and falls to a negligible value at the outer boundary. This is consistent with the reduced neutrino absorption approaching its vacuum-decay limit as the thermal occupation becomes small; it does not mean the outer thermal neutrino density is large.

### 3.4 Escaping luminosity is not the same as the optical-depth weighting

At the high-absorption coupling:
- total escape fraction: \(3.239\times10^{-4}\);
- 5–10 km production supplies 59.13% of the escaped luminosity;
- 10–15 km production supplies 37.43%;
- 20–25 km production supplies 3.36%;
- the 0–5 km and 15–20 km production shells together supply less than 0.1%.

The 20–25 km source shell has a larger source-weighted escape probability (\(7.38\times10^{-3}\)) because some trajectories start close to the outer boundary and travel outward. Its optically thin source fraction is only 0.147%, so it contributes only 3.36% of the escaped luminosity.

This confirms that the high-coupling luminosity is controlled mainly by the 5–15 km production region and the overlying absorption along its rays. The outer optical-depth contribution is important, but it is not equivalent to the fraction of luminosity absorbed in the outer shell.

## 4. Fixed-background limitation at high coupling

Blinov et al. explicitly state that above the dash-dotted \(\lambda_{\rm mfp}(T_{\max})=R_\nu\) line, the new vector can significantly affect supernova energy transport and fixed-profile constraints become uncertain. They also state that much of the larger-coupling region can modify the supernova dynamics, making a fixed profile containing only SM physics likely incorrect.

For a rough check using the paper's Eq. (4.3),
\[
\lambda \sim 1.5\,{\rm km}
\left(\frac{\omega}{50\,{\rm MeV}}\right)
\left(\frac{m_V}{5\,{\rm MeV}}\right)^{-2}
\left(\frac{10^{-7}}{g_{\mu\tau}}\right)^2,
\]
take \(m_V=10\) MeV and \(\omega\simeq T_{\max}=33.92\) MeV from the reconstructed profile. Setting \(\lambda=R_\nu=25\) km gives
\[
g_{\mu\tau}^{\rm line}\sim1.01\times10^{-8}.
\]
The high-absorption Fig. 7 endpoint is \(4.17\times10^{-8}\), about 4.14 times this rough threshold; Eq. (4.3) then gives \(\lambda\sim1.46\) km. This places the high-coupling endpoint in the regime where the paper itself warns about fixed-background feedback.

**Interpretation limit:** this caveat affects whether the fixed-background Fig. 7 curve is a physically self-consistent prediction at high coupling. It does not, by itself, explain why our numerical evaluation differs from the published Fig. 7 curve: both calculations are intended to evaluate the same fixed-profile prescription. A mismatch between them still requires an implementation/input explanation. Background feedback should be discussed only after the fixed-profile benchmark is fully reconciled, and must not be used as a numerical fudge factor.

## 5. Current decision and next work

| Question | Status | Decision |
|---|---|---|
| Does the printed Eq. (B.2) hold the same \(\omega\) along the path? | Yes, literally | Keep fixed-\(\omega\) as the literal equation lane |
| Is the paper's global/local energy convention fully unambiguous? | No; Eq. (4.2) and Appendix B use \(\omega\) differently or incompletely define its frame | Record the ambiguity; do not claim access to the authors' code |
| Does conserved-\(E_\infty\) remapping improve the high tail? | Yes, but leaves \(+35.97\%\) | Keep as separate diagnostic only |
| Is screenshot digitization responsible? | No; native vector-path reconstruction passes | Freeze the 25-point reference curve |
| Which regions dominate the current source and opacity? | Quantified by the joint matrix | Keep local rates and profile frozen |
| Is the high-coupling fixed-profile interpretation secure? | No; it lies above the paper's feedback-warning line | Treat as a physical applicability caveat, not a reproduction correction |

The next useful task is not another opacity or chemical-potential scan. It is to resolve the \(\omega\)-frame convention at the level of the paper's definitions and any publicly available implementation details. If the authors' internal code remains unavailable, the reproducible result must preserve the two lanes and state the convention ambiguity. Only then should the radial source/opacity profile reconstruction be compared against any additional public data for the same s18.8-SFHo-MUONS snapshot.

## 6. Reproducibility records

- Energy convention and Eq. (B.2) equation-chain audit: FIG7_10MEV_EQUATION_CHAIN_AUDIT_2026-11-07.md
- Independent path/angular audit: EQ_B2_INDEPENDENT_PATH_INTEGRAL_AUDIT_2026-11-08.md
- Native PDF digitization audit: outputs/fig7_digitization_audit_2026-11-07.json
- Native PDF drawing records: outputs/fig7_source_drawings_2026-11-07.json
- Joint spatial-weight implementation: audit_fig7_spatial_weight_matrix.py
- Spatial-weight regression tests: test_fig7_spatial_weight_matrix.py
- Machine-readable joint matrix: outputs/fig7_spatial_weight_matrix_2026-11-08.json
- CI run: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42409199703

The spatial-weight workflow passed all five bookkeeping tests and the full numerical run. Its machine-readable output is committed to the PR branch. The manuscript and referee-response files are unchanged; PR #56 remains Open / Draft.
