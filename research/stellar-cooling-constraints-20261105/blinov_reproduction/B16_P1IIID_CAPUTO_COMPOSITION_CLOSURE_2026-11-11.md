# P1-IIId: Caputo composition closure and free-nucleon reconstruction

Date: 2026-11-11  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Main correction

The earlier diagnostic
\[
(n_p-n_e-n_\mu)/n_p
\]
must **not** be interpreted as a violation of charge neutrality. Caputo, Raffelt, and Vitagliano explicitly explain in Fig. 4 that the difference between \(Y_e+Y_\mu\) and \(Y_p\) signals light nuclei or nuclear clusters in the neutrino-decoupling region.

Thus:
\[
Y_e+Y_\mu-Y_p = Y_Q^{\rm cl},
\]
the positive charge per baryon carried by nuclei/clusters, assuming the listed charged species exhaust the relevant lepton charge. This is a physical composition contribution, not a numerical defect to be repaired by rescaling.

The same figure defines \(Y_n\), \(Y_p\), and the remaining baryon fraction. In the notation used here:
\[
X_{\rm cl}=1-Y_n-Y_p,\qquad
Y_Q^{\rm cl}=Y_e+Y_\mu-Y_p.
\]
The first is the total baryon mass fraction in clusters; the second is their positive charge per baryon.

## 2. Source identity: this is a cross-publication check, not an independent simulation

Esseili–Kribs Fig. 12 uses the SFHo-18.8 model at 1 s after core collapse, normalized to \(n_0=0.181\,\mathrm{fm}^{-3}\). Its reference [174] is Bollig et al., *Muons in Supernovae: Implications for the Axion-Muon Coupling*, PRL 125, 051104 (2020), with erratum PRL 126, 189901 (2021).

Caputo Fig. 1 uses the Garching muonic SFHo-18.8 model at \(t_{\rm pb}=1\) s and cites the same Bollig et al. simulation as Ref. [3]. Caputo et al. also acknowledge Bollig and Janka for providing the supernova profiles.

Therefore the two publications trace back to the **same Garching model lineage and reference snapshot**. This comparison is valuable as an independent published-figure / extraction / species-definition consistency check, but it is not an independent hydrodynamic simulation cross-validation.

Esseili–Kribs Fig. 12 shows \(T(r)\) in the left panel and \(n,p,e,\mu\), and neutrino number densities in the right panel. The caption gives the common normalization \(n_0=0.181\,\mathrm{fm}^{-3}\). The full profile data are directed to the Garching archive; the relevant archive endpoint returned HTTP 401 in the present access path, so no raw profile is claimed.

## 3. Reproducible vector extraction

The exact arXiv:2109.03244v3 source archive is pinned by SHA-256:
\[
\texttt{2e4a1280460bce9a5f7596d3dfd1d3e0f4752f2e1706e85d3a2c20b5f9dbbd8e}.
\]

The two source PDF members are:
- \`figures/SNProfile.pdf\`: SHA-256 \`19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e\`;
- \`figures/ScreeningPlot.pdf\`: SHA-256 \`39d66c37dd67d73fbe1b3afe2f5e2a532e0e040e9d220e66ec389abb5daf17ab\`.

The Fig. 1 lower-panel vector paths are \(n_B,n_p,n_e,n_\mu\), path indices 158, 159, 160, and 161. The Fig. 4 upper-panel vector paths are \(Y_p\) (orange, path 0), \(1-Y_n\) (blue, path 1), and \(Y_e+Y_\mu\) (green, path 2). All curves are extracted from the original PDF vector paths, not screen captures.

The extraction and reconstruction are implemented in \`extract_caputo_composition_abundances.py\`. Running it on the pinned arXiv source archive regenerates the 0.05-km composition profile CSV and the JSON provenance/validation summary.

## 4. Cross-figure validation

We independently compare the Fig. 4 abundance curves with ratios formed from the Fig. 1 density curves:
\[
Y_p^{(1)}(r)=\frac{n_p^{(1)}(r)}{n_B^{(1)}(r)},\qquad
Y_\ell^{(1)}(r)=\frac{n_e^{(1)}(r)+n_\mu^{(1)}(r)}{n_B^{(1)}(r)}.
\]

Over the common radial interval \(0.2\le r\le15.2\) km, using the 0.05-km output grid:

| Cross-check | RMS relative difference | Maximum absolute relative difference |
|---|---:|---:|
| \(Y_p^{(4)}\) vs. \(n_p^{(1)}/n_B^{(1)}\) | 0.0320% | 0.0850% |
| \((Y_e+Y_\mu)^{(4)}\) vs. \((n_e^{(1)}+n_\mu^{(1)})/n_B^{(1)}\) | 0.1074% | 0.2643% |

The cluster-charge abundance from Fig. 4 and the same quantity reconstructed from Fig. 1 differ by an RMS absolute amount \(1.62\times10^{-4}\) per baryon, with a maximum \(4.13\times10^{-4}\). The small residual is consistent with independent vector-path digitization and interpolation.

This cross-figure closure strongly supports the species interpretation:
- \(Y_p\) is the free-proton abundance per baryon;
- \(Y_n\) is the free-neutron abundance per baryon;
- \(1-Y_n-Y_p\) is the baryon fraction in nuclei/clusters;
- \(Y_e+Y_\mu-Y_p\) is the positive charge per baryon carried by those clusters.

## 5. Reconstructed free-nucleon profiles and cluster fractions

The correct reconstruction is
\[
n_n^{\rm free}(r)=Y_n(r)n_B(r),\qquad
n_p^{\rm free}(r)=Y_p(r)n_B(r),
\]
and
\[
n_{\rm cl}^{\rm baryon}(r)=X_{\rm cl}(r)n_B(r).
\]

Selected values from the vector-path reconstruction:

| \(r\) (km) | \(n_B/n_0\) | \(n_n^{\rm free}/n_0\) | \(n_p^{\rm free}/n_0\) | \(X_{\rm cl}\) | \(Y_Q^{\rm cl}\) | \((Z/A)_{\rm eff}\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1.9402 | 1.5170 | 0.4232 | 0.00% | 0.00% | — |
| 5 | 1.6100 | 1.2630 | 0.3470 | 0.00% | 0.00% | — |
| 8 | 0.9957 | 0.7957 | 0.2000 | 0.00% | 0.00% | — |
| 9 | 0.8365 | 0.6861 | 0.1466 | 0.45% | 0.19% | 0.420 |
| 10 | 0.7012 | 0.5764 | 0.1094 | 2.20% | 0.91% | 0.414 |
| 12 | 0.4511 | 0.3750 | 0.05045 | 5.68% | 2.29% | 0.403 |
| 14 | 0.2373 | 0.2034 | 0.01485 | 8.04% | 3.16% | 0.393 |
| 15 | 0.1497 | 0.1306 | 0.00589 | 8.85% | 3.43% | 0.387 |
| 18 | 0.01048 | 0.00917 | 0.000217 | 10.43% | 4.33% | 0.415 |

Here \((Z/A)_{\rm eff}=Y_Q^{\rm cl}/X_{\rm cl}\) is only the aggregate charge-to-baryon ratio of all clusters; it does not identify the individual D, T, alpha, or heavy-nucleus abundances.

The cluster baryon fraction reaches approximately 2.2% at 10 km, 5.7% at 12 km, and 8.9% at 15 km. This is large enough that a free-nucleon-only collision kernel must quantify the omitted nuclear component in the relevant radial layers. The outer profile changes rapidly; no extrapolation beyond the source support is made.

## 6. Consequence for P1-IIIb

Do **not** use
\[
n_n^{\rm free}=n_B-n_p^{\rm free}.
\]
That expression incorrectly assigns all baryons not in free protons to free neutrons, thereby absorbing cluster baryons into the neutron target density.

Use the separately reconstructed \(Y_n\) and \(Y_p\):
\[
n_n^{\rm free}=Y_n n_B,\quad n_p^{\rm free}=Y_p n_B,\quad
n_{\rm cl}^{\rm baryon}=(1-Y_n-Y_p)n_B.
\]

The present free \(nn,np,pp\) kernel does not include cluster response. Before integrating it through the full 8–15 km region, either:
1. include the relevant nuclear targets/responses, or
2. define a validated free-nucleon-dominated radial mask and quantify the omitted cluster layer separately.

No B.2 opacity, Fig. 7 vector benchmark, escape probability, or axial cooling curve is changed by this composition audit.

## 7. Fig. 12 comparison status and next action

The SFHo-18.8 temperature curve in Esseili–Kribs Fig. 12 is visually consistent with Caputo Fig. 1: the Caputo maximum is \(39.25\) MeV at \(r=8.48\) km, while the published orange curve peaks near 40 MeV around 8–9 km. The \(n,p\) curves are also consistent in overall shape with the Caputo reconstructed free-neutron/free-proton profiles at figure-reading precision.

A point-by-point E–K residual is **not** reported yet: the official APS PDF page is available for visual inspection, but its vector paths have not yet been extracted into a local reproducible data file. The next task is to digitize E–K Fig. 12 \(T,n,p\) with an explicit axis calibration and uncertainty, then compare against the Caputo reconstructed profiles. Since both publications use the same Garching SFHo-18.8 reference model, this is a cross-publication consistency test rather than an independent simulation test.
