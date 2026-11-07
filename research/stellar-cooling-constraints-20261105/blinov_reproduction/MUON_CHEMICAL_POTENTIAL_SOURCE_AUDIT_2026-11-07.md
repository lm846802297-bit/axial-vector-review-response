# SFHo-18.8 muon chemical-potential source and convention audit

Date: 2026-11-07  
Status: **Caputo baseline quantitatively cross-checked against Bollig Figs. 3 and 4; Ferreira discrepancy unresolved**  
Scope: Blinov Fig. 7 10 MeV vector reproduction only. This note does not change the baseline profile, rates, transport prescription, or axial-vector results.

## Executive result

The present discrepancy between the Caputo and Ferreira reconstructions is **not explained by a simple rest-mass convention shift**.

Both papers use the same Fermi-Dirac convention for negatively charged leptons,
\[
f_{\mu^-}(E)=\frac{1}{\exp[(E-\mu_\mu)/T]+1},
\]
with the corresponding antiparticle distribution using the opposite sign. Ferreira et al. explicitly use the muon vacuum mass in the on-shell energy, integrate the incoming lepton energy from \(m_\mu\), and state that thermal corrections to the muon dispersion relation are neglected. Caputo et al. use the same sign convention in their Eq. (5). A consistent shift of the energy zero would require shifting both \(E\) and \(\mu_\mu\) by the same constant; it leaves \(E-\mu_\mu\) and the occupation unchanged. The observed profile difference is strongly radius-dependent, so it cannot be repaired by subtracting or adding a constant rest mass to one curve.

More importantly, both Caputo et al. and Ferreira et al. identify the SFHo-18.8, 1 s post-bounce model with the Garching Prometheus-Vertex simulations of Bollig et al. Yet the digitized \(\mu_\mu(r)\) curves differ strongly in the inner core. The temperature curves agree to better than 0.27% over their common radial interval, so the discrepancy is specifically in the muon chemical-potential profile, not a general radial-axis or temperature mismatch.

An independent check against Bollig et al.'s Fig. 4 is especially useful: that figure plots the SFHo-18.8 degeneracy parameter \(\mu_\mu/T\). The Caputo reconstruction has the same qualitative radial behavior and O(1) values in the high-muon-density region. The Ferreira reconstruction gives much larger inner-core values, notably \(\mu_\mu/T\simeq9.2\) at 5 km, whereas the SFHo-18.8 curve in Bollig Fig. 4 is visually around O(1) there. This is a source-level inconsistency that needs explanation; it is not a basis for silently replacing either published curve.

**Working decision:** retain Caputo as the current baseline for the Blinov reproduction because its \(\mu_\mu(r)\) is internally checked against Caputo's independently plotted muon-density profile and is qualitatively consistent with Bollig Fig. 4. Keep Ferreira as an unresolved cross-check, not as an adopted alternative profile. This decision is provisional until the public-figure digitizations and the original profile provenance are fully reconciled.

## 1. Source chain

### Caputo et al.

Caputo, Raffelt and Vitagliano, *Muonic Boson Limits: Supernova Redux*, arXiv:2109.03244 (current v3, including post-publication corrections dated 2026-03-13), use the Garching SFHo-18.8 model at \(t_{\rm pb}=1\,\mathrm{s}\) as their cold reference model. Their Fig. 1 displays \(T\), chemical potentials, plasma frequency and screening scale, and their lower panel independently displays the particle number densities, including \(n_\mu\).

Their Eq. (5) defines
\[
f_F^{\pm}(E)=\left[\exp\left(\frac{E\pm\mu}{T}\right)+1\right]^{-1},
\]
where \(\mu>0\) and the signs distinguish negatively charged leptons and antileptons. Thus for \(\mu^-\), the exponent is \((E-\mu_\mu)/T\).

### Ferreira, Marsh and Ravensburg

Ferreira et al., *ALP couplings to muons and electrons: a comprehensive analysis of supernova bounds*, arXiv:2510.14469v1 (published in *Physics of the Dark Universe* 53 (2026) 102435), also use the SFHo-18.8 model at 1 s post bounce. Section III identifies it as the coldest model of their Ref. [18], i.e. Bollig et al., and says it was obtained with Prometheus-Vertex and is accessible through the Garching Core-Collapse Supernova Archive.

Their Eq. (5) uses the same Fermi-Dirac sign convention. In Sec. IV.1, the incoming lepton energy is integrated from \(m_\ell\), with \(E_\ell^{\rm in}=\sqrt{p_{\rm in}^2+m_\ell^2}\); the authors state that muons have vacuum mass \(m_\mu^0\simeq106\,\mathrm{MeV}\), are non-relativistic in the plasma, and that thermal corrections to their dispersion relation are neglected. This is consistent with using total single-particle energy including the rest mass in the Fermi factor.

### Bollig et al.

Bollig et al., *Muons in supernovae: implications for the axion-muon coupling*, arXiv:2005.07141v7, describe the same Garching Prometheus-Vertex simulation family. Their Fig. 4 directly plots \(\mu_\mu/T\) for SFHo-18.8, SFHo-18.6, SFHo-20.0 and LS220-20.0. The text states that the degeneracy parameter remains O(1) in the region of high muon density, approximately 5--15 km. Their Fig. 3 independently shows the radial muon number density.

The source chain is therefore:
- underlying simulation: Bollig et al., Garching Prometheus-Vertex, SFHo-18.8, 1 s post bounce;
- public Caputo reconstruction: \(T(r)\), \(\mu_\mu(r)\), \(n_\mu(r)\) shown in Fig. 1;
- public Ferreira reconstruction: \(T(r)\), \(\mu_\mu(r)\) shown in Fig. 1;
- our data: digitizations of those published PDF vector paths, not original simulation tables.

## 2. Matched radial comparison

The current public-figure digitizations give the following values. Both chemical-potential profiles are divided by the Caputo temperature at the same radius for this comparison; the temperature curves themselves agree at the sub-percent level over the overlap.

| \(r\) (km) | \(T_{\rm Caputo}\) (MeV) | \(\mu_\mu^{\rm Caputo}\) (MeV) | \(\mu_\mu^{\rm Ferreira}\) (MeV) | \(\mu_\mu^{\rm Caputo}/T\) | \(\mu_\mu^{\rm Ferreira}/T\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 19.27 | 46.67 | 254.89 | 2.42 | 13.23 |
| 5 | 25.36 | 56.14 | 233.32 | 2.21 | 9.20 |
| 8 | 38.85 | 91.79 | 167.40 | 2.36 | 4.31 |
| 10 | 33.93 | 102.84 | 131.14 | 3.03 | 3.87 |
| 12 | 25.98 | 93.73 | 109.83 | 3.61 | 4.23 |
| 15 | 13.23 | 62.28 | 68.65 | 4.71 | 5.19 |
| 18 | 5.92 | 23.40 | 26.49 | 3.95 | 4.47 |
| 20 | 4.20 | 14.77 | 12.41 | 3.51 | 2.95 |

The main discrepancy is concentrated in the inner core, particularly \(r\lesssim8\,\mathrm{km}\). The two reconstructions become much closer outside about 10 km. This radial pattern is not compatible with a constant energy-zero shift.

The source PDF for Ferreira has a linear \(\mu_\mu\) axis with labeled ticks at 50, 100, 150, 200, 250 and 300 MeV. The current extraction uses that linear calibration; the large inner-core values are not caused by mistakenly treating this axis as logarithmic.

### Direct density consistency check

Using the same relativistic single-particle energy \(E=\sqrt{p^2+m_\mu^2}\) and
\[
n_{\mu^-}=\frac{1}{\pi^2}\int_0^\infty dp\,p^2
\left[\exp\left(\frac{E-\mu_\mu}{T}\right)+1\right]^{-1},
\]
the digitized Caputo chemical potential reproduces Caputo's independently plotted number-density curve:

| \(r\) (km) | Caputo Fermi integral \(n_\mu\) (fm\(^{-3}\)) | Caputo Fig. 1 \(n_\mu\) (fm\(^{-3}\)) | Relative difference | Ferreira \(\mu_\mu\), same \(T\): predicted \(n_\mu\) (fm\(^{-3}\)) | Ferreira/Caputo density |
|---:|---:|---:|---:|---:|---:|
| 0 | \(9.58\times10^{-5}\) | \(9.63\times10^{-5}\) | -0.49% | \(5.90\times10^{-2}\) | 616 |
| 5 | \(4.67\times10^{-4}\) | \(4.70\times10^{-4}\) | -0.52% | \(4.61\times10^{-2}\) | 98.8 |
| 8 | \(4.66\times10^{-3}\) | \(4.68\times10^{-3}\) | -0.50% | \(2.08\times10^{-2}\) | 4.46 |
| 10 | \(4.49\times10^{-3}\) | \(4.51\times10^{-3}\) | -0.46% | \(8.73\times10^{-3}\) | 1.94 |
| 15 | \(4.01\times10^{-5}\) | \(4.06\times10^{-5}\) | -1.07% | \(6.45\times10^{-5}\) | 1.61 |

This is the strongest internal evidence in the present audit. The Caputo \(\mu_\mu\) curve and its independently plotted \(n_\mu\) curve are mutually consistent under the stated Fermi-Dirac convention. The Ferreira curve, if inserted into that same convention and the same temperature profile, does not reproduce the same model's muon density in the inner core. The mismatch is enormous at 0--5 km and remains a factor of about 2 at 10 km.

This does not prove that the Ferreira authors used the plotted curve directly in every production integral, nor does it identify the origin of the discrepancy. It does show that the plotted Ferreira \(\mu_\mu\) curve cannot be combined with the stated free-muon dispersion and Fermi distribution and simultaneously be interpreted as the same SFHo-18.8 muon density profile, unless an additional energy shift or mean-field contribution is present and documented. No such additional term is specified in the inspected sections.

## 3. Cross-check against Bollig Fig. 4

Bollig Fig. 4 is a direct independent diagnostic because it plots \(\mu_\mu/T\) for the same named simulation profiles. Visual inspection of the SFHo-18.8 curve gives an O(1) degeneracy parameter in the high-muon-density region and a radial trend qualitatively similar to the Caputo reconstruction. In particular, the SFHo-18.8 curve is nowhere near the Ferreira-only value \(\mu_\mu/T\simeq9.2\) at 5 km.

This is no longer only a visual cross-check. The SFHo-18.8 yellow vector path in Bollig Fig. 4 is extracted from the original public PDF (drawing path 193, 219 line segments, 220 deduplicated vertices), with the x and y axes calibrated from PDF tick paths. The full pointwise comparison and provenance are archived in the JSON and CSV outputs.

## 4. Quantitative upstream cross-check against Bollig et al. Figs. 3 and 4

The previous version of this audit compared the two later reconstructions and only visually inspected Bollig Fig. 4. The original arXiv v7 PDF has now been digitized directly from its vector paths, so both upstream panels can be compared quantitatively.

### Fig. 4: degeneracy parameter

The yellow SFHo-18.8 curve is extracted from PDF drawing path 193 (219 line segments, 220 deduplicated vertices). Its axes are calibrated from the PDF tick paths. On a uniform 501-point comparison grid over (1le rle20) km:

| Reconstruction | Maximum absolute relative difference from Bollig Fig. 4 | Mean absolute relative difference |
|---|---:|---:|
| Caputo (mu_mu(r)/T(r)) | 0.0161% | 0.00551% |
| Ferreira (mu_mu(r)/T(r)) | 446% | 127.6% |

The pointwise comparison is equally clear:

| (r) (km) | Bollig (mu_mu/T) | Caputo (mu_mu/T) | Ferreira (mu_mu/T) |
|---:|---:|---:|---:|
| 1 | 2.4173 | 2.4173 | 13.2017 |
| 5 | 2.2136 | 2.2138 | 9.1999 |
| 8 | 2.3627 | 2.3629 | 4.3126 |
| 10 | 3.0311 | 3.0313 | 3.8655 |
| 12 | 3.6078 | 3.6078 | 4.2292 |
| 15 | 4.7072 | 4.7071 | 5.1926 |
| 18 | 3.9532 | 3.9535 | 4.4628 |
| 20 | 3.5133 | 3.5132 | 2.9499 |

Thus the Caputo reconstruction is not merely qualitatively compatible with Bollig Fig. 4: it reproduces the plotted SFHo-18.8 degeneracy curve to better than (2	imes10^{-4}) relative accuracy. The Ferreira reconstruction does not. This is the strongest available public-source evidence for selecting Caputo as the baseline.

### Fig. 3: muon number density

The yellow SFHo-18.8 curve is extracted from PDF drawing path 33 (126 line segments, 123 visible deduplicated vertices). The x axis is calibrated over the plotted 1--20 km interval; the y axis is logarithmic in (n_mu,[mathrm{fm}^{-3}]), with the (10^{-7}) to (10^{-1}) calibration fixed by the PDF tick paths.

Over the common resolved interval (1.30le rle15.27) km, the Caputo Fig. 1 density curve (converted from (n_mu/n_0) using (n_0=0.181,mathrm{fm}^{-3})) agrees with Bollig Fig. 3 at a mean absolute relative difference of 3.73% and a maximum of 10.45%. At representative radii:

| (r) (km) | Bollig Fig. 3 (n_mu) ((mathrm{fm}^{-3})) | Caputo Fig. 1 (n_mu) ((mathrm{fm}^{-3})) |
|---:|---:|---:|
| 5 | (4.622	imes10^{-4}) | (4.695	imes10^{-4}) |
| 8 | (4.612	imes10^{-3}) | (4.684	imes10^{-3}) |
| 10 | (4.380	imes10^{-3}) | (4.515	imes10^{-3}) |
| 12 | (1.831	imes10^{-3}) | (1.954	imes10^{-3}) |
| 15 | (3.686	imes10^{-5}) | (4.057	imes10^{-5}) |

The residual grows toward the low-density outer edge, where the logarithmic curves approach the plotting floor and small ordinate differences become large relative errors. This is consistent with the earlier independent Fermi-integral check: the Caputo (mu_mu(r)) and Caputo (n_mu(r)) curves are internally consistent to about 0.5--1.1% at the sampled radii. Together, the two independent upstream comparisons support the Caputo baseline.

The source PDF hash is `8267f8b1de184163308728c44000425ce58085c1d5bd799d0cbc1e4e8d740d61`. The digitized CSVs and full drawing inventory are archived in `outputs/bollig_fig4_sfho188_muon_degeneracy.csv`, `outputs/bollig_fig3_sfho188_muon_density.csv`, and `outputs/bollig_fig4_vector_inventory.json`. These remain digitizations of published plotting paths, not the original simulation tables.

## 5. What the convention check does and does not establish

1. The two later papers use the same Fermi-Dirac sign convention for \(\mu^-\).
2. A consistent rest-energy shift must shift both the energy argument and chemical potential. It cannot account for the observed radius-dependent difference.
3. The Ferreira paper's own Fig. 1 identifies the orange dashed curve as SFHo-18.8 and labels the right-hand axis \(\mu_\mu\,[\mathrm{MeV}]\); the digitization follows its linear tick marks.
4. The Caputo reconstruction reproduces its independently plotted \(n_\mu(r)\) to within 1.1% at all checked radii (0, 5, 8, 10 and 15 km). Inserting the Ferreira \(\mu_\mu\) curve into the same distribution at the same Caputo temperature predicts a muon density larger by factors of about 616, 99, 4.46, 1.94 and 1.61 at those radii. The temperature curves agree to 0.27%, so this is not a temperature-profile effect. Exact values are archived in outputs/muon_chemical_potential_provenance_audit.json.
5. The published figures do not reveal why Ferreira's inner-core \(\mu_\mu\) curve differs from Caputo/Bollig. Possible explanations include a different simulation data version, a variable/plotting mismatch, or a post-processing convention not documented in the paper. None is established by the public material inspected here.

The papers state that the relevant profiles originate from the same named Garching model, but the Garching raw tables are not included in these public articles. The 2026 Ferreira journal record states that the authors do not have permission to share the data. We have not requested or accessed restricted raw simulation tables.

## 6. Implication for the Blinov reproduction

The current vector reproduction should continue using the Caputo \(\mu_\mu(r)\) reconstruction as its reference input, while recording the Ferreira curve as an unresolved external cross-check. The previous Ferreira-only substitution that moved the weak/peak/high-coupling residuals to approximately +43.9%/+33.9%/+65.0% is a sensitivity test, not evidence that this alternative profile is physically correct.

Do not tune the source normalization or opacity to compensate for this discrepancy. Do not combine Caputo \(T(r)\) with Ferreira \(\mu_\mu(r)\) as a nominal model. The next profile task is to quantify the Caputo \(n_\mu\) consistency test and digitize Bollig Fig. 4 at sufficient resolution for a pointwise \(\mu_\mu/T\) comparison. If those public figures still do not resolve the provenance, the remaining uncertainty must be stated rather than guessed.

## 7. Next steps before the outer-neutrino-opacity study

1. Run the automated convention/density audit and archive its JSON output.
2. Digitize the SFHo-18.8 curve in Bollig Fig. 4, with source-PDF provenance and tick calibration, and compare it pointwise with both reconstructed \(\mu_\mu/T\) profiles.
3. Check whether the original Bollig Fig. 3 muon-density curve and Caputo Fig. 1 bottom-panel \(n_\mu\) curve agree within digitization accuracy.
4. Only after this profile-source check, freeze the adopted \(\mu_\mu(r)\) baseline and proceed to the 15--25 km neutrino-absorption audit.

No formal paper, referee response, or axial-vector exclusion curve is modified by this research note.
