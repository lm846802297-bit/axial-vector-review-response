# P1-IIId: Caputo density curves extracted from the arXiv source package

Date: 2026-11-11  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`

## 1. Source package and integrity

The uploaded `arXiv-2109.03244v3.tar.gz` contains `figures/SNProfile.pdf`. Its SHA-256 is

`19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e`

which exactly matches the checksum pinned by the existing repository extraction script. The source archive SHA-256 is

`2e4a1280460bce9a5f7596d3dfd1d3e0f4752f2e1706e85d3a2c20b5f9dbbd8e`.

## 2. Exact lower-panel vector paths

| Quantity | PDF path | Stroke | Unique vertices | Encoded radial extent |
|---|---:|---|---:|---:|
| (n_B/n_0) | 158 | blue | 245 | 0.1167–22.1252 km |
| (n_p/n_0) | 159 | red | 186 | 0.1167–19.3111 km |
| (n_e/n_0) | 160 | magenta | 198 | 0.1167–19.9864 km |
| (n_\mu/n_0) | 161 | green | 102 | 0.1167–15.2729 km |

The three missing paths are therefore (n_B:158), (n_p:159), and (n_e:160). The known (n_\mu) path 161 is recovered independently.

## 3. Axis calibration and data products

[
r\,[\mathrm{km}]=\frac{x_{\rm PDF}-47.52}{324.0-47.52}\,20,
\qquad
\frac{n_i}{n_0}=10^{-4+(442.918-y_{\rm PDF})/41.4718},
\quad n_0=0.181\,\mathrm{fm}^{-3}.
]

All unique PDF polyline vertices are archived in
`outputs/caputo_density_pdf_vertices_2026-11-11.csv.gz`. The reproducible script
`extract_caputo_density_curves.py` regenerates the expanded vertex table with transformed
(r,n_i/n_0) and plot-boundary flags at
`outputs/caputo_density_curves_vertices_2026-11-11.csv`.

## 4. Clipping and interpretation limits

The blue (n_B) vector path contains 47 encoded vertices beyond the visible (r=20) km frame.
They are retained for provenance but flagged; they must not be treated as plotted data or used
for physical extrapolation. All four curves begin at (r=0.1167) km, so no value at (r=0)
is invented here.

These are public-figure digitizations, not raw Garching tables. In particular, (n_B-n_p)
must not automatically be labelled (n_n^{\rm free}), and (n_p) must not automatically
be labelled (n_p^{\rm free}). The free-nucleon composition and cluster-content questions
remain open.

## 5. Scope

This closes the Caputo PDF path-identification and density-curve extraction subtask. It does
not close the independent Esseili–Kribs comparison or the SFHoY composition sensitivity.
No B.2 opacity, energy/transport sphere, escape probability, pure-vector Fig. 7 result, or
axial cooling curve is changed.
