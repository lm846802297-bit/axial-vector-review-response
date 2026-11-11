# P1-IIId: Esseili–Kribs Fig. 12 native-vector extraction and Caputo cross-check

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Result and scope

The checksum-pinned SCOAP3 copy of the published APS PDF is used as the reproducible source for native PDF-vector extraction. Its exact SHA-256 is checked by CI. The
SFHo-18.8 temperature path and the right-panel neutron/proton paths are
identified by stroke color and exact path index, flattened from cubic Bézier
segments, clipped to the plotted frame, and calibrated against the PDF tick
marks. The extraction is reproducible from the checksum-pinned PDF and script.

This is a cross-publication figure-level consistency audit. Caputo et al. and
Esseili–Kribs use the same Garching SFHo-18.8 model lineage at 1 s after bounce;
this does not constitute an independent hydrodynamic simulation comparison and
does not replace access to the raw Garching profile.

## 2. Source and native vector provenance

- Paper: Esseili & Kribs, *Phys. Rev. D* 114, 016023 (2026), DOI
  `10.1103/718s-7k7v`.
- Source used for the archived extraction: the SCOAP3 open-access copy of the
  published APS PDF, [SCOAP3 record 109482](https://repo.scoap3.org/records/109482).
- Exact PDF SHA-256:
  `c3b92fe6cf2a8bd3fec84925e2baababfe0c707327a68135013f953ed3d87d43`;
  size: 2,749,668 bytes. GitHub Actions verifies this checksum before
  extraction.
- Native PDF page index 14 (printed page 15); native paths: temperature
  `25` (orange), neutron `181` (blue), proton `182` (cyan). The script
  verifies the expected stroke RGB values before extraction.
- Flattened/clipped point counts: 386 temperature, 337 neutron, 473 proton.
- Visible radial supports: temperature 0.300–22.000 km, neutron
  0.300–21.916 km, proton 0.300–19.298 km.
- The arXiv v3 PDF is useful as a textual/version cross-check (the arXiv
  record says v3 matches the published version), but it is not substituted
  for this vector extraction: its PDF-internal path ordering/stroke grouping
  differs, and the published-PDF path indices 25/181/182 do not identify the
  same curves there.

The reproducible products are:

- `extract_esseili_kribs_fig12_vector.py`;
- `audit_esseili_kribs_fig12_crosscheck.py`;
- `outputs/esseili_kribs_fig12_vector_vertices_2026-11-11.csv`;
- `outputs/esseili_kribs_fig12_vector_provenance_2026-11-11.json`;
- `outputs/esseili_kribs_fig12_caputo_temperature_crosscheck_2026-11-11.csv`;
- `outputs/esseili_kribs_fig12_bollig_temperature_crosscheck_2026-11-11.csv`;
- `outputs/esseili_kribs_fig12_caputo_density_crosscheck_2026-11-11.csv`;
- `outputs/esseili_kribs_fig12_crosscheck_summary_2026-11-11.json`.

## 3. Axis calibration and the right-panel density-axis ambiguity

The left-panel radius is calibrated from its native 5, 10, 15, and 20 km tick
paths. Temperature is calibrated from the 10–60 MeV horizontal ticks. The
right-panel radius is independently calibrated from its own tick paths.

The right-panel density ticks are equally spaced by 25.56, 25.60, 25.61, and
25.61 PDF points. The lower three labels identify (10^{-2}), (10^{-3}), and
(10^{-4}). Equal spacing on a logarithmic axis therefore implies the upper
two values (10^{-1}) and (10^0=1). The upper two glyphs are visually
ambiguous at the available raster resolution; importantly, the native PDF
does not expose them as text spans. The extraction records zero text spans in
the right-axis margin and retains the vector-glyph provenance. We therefore
do not claim that the paper definitely contains a typesetting error.

Both candidate calibrations are retained in the raw CSV:

[
log_{10}(n/n_0)=-4+rac{166.643982-y_{m PDF}}{25.6},
qquad n_0=0.181;mathrm{fm}^{-3},
]

and the literal upper-glyph reading, exactly ten times larger. The physically
cross-validated calibration is selected because it agrees with Caputo's
independently reconstructed free-neutron and free-proton curves; the literal
alternative misses them by nearly a factor of ten. This is a calibration
decision supported by the same-model comparison, not a claim about the
authors' intended typography.

## 4. Temperature comparison

The E–K orange curve is compared with the existing Caputo SFHo-18.8 temperature
profile at 55 common radii from 5.126 to 14.930 km:

- RMS relative residual: **0.0707%**;
- mean absolute relative residual: 0.0480%;
- maximum absolute relative residual: **0.218%**.

A second comparison uses the native Bollig et al. Fig. 1 SFHo-18.8 temperature
path on a 0.05-km grid from 0.5 to 20 km:

- 391 comparison points;
- RMS relative residual: **0.0953%**;
- maximum absolute relative residual: **0.277%**.

The E–K curve peaks at 39.222 MeV near 8.381 km. The Bollig vector curve peaks
at 39.250 MeV near 8.482 km. The peak positions and amplitudes agree within the
published line-width uncertainty. These numerical results supersede the earlier
qualitative-only temperature comparison in
\`B16_P1IIID_FIG12_PDF_PAGE_RENDER_AUDIT_2026-11-11.md\`.

## 5. Density and species-definition comparison

The right-panel curves are compared with Caputo's reconstructed free-nucleon
profiles at the ten common radii 1, 5, 8, 9, 10, 11, 12, 13, 14, and 15 km.
Caputo's free densities are reconstructed as

\[
n_n^{\rm free}=Y_n n_B,\qquad n_p^{\rm free}=Y_p n_B,
\]

using the Fig. 4 abundances; \`n_B - n_p\` is not used as a neutron density.

With the corrected candidate density-axis transform:

| Comparison | RMS relative residual | Maximum absolute relative residual |
|---|---:|---:|
| E–K \`n\` vs Caputo free neutron | **0.580%** | 0.976% |
| E–K \`p\` vs Caputo free proton | **0.586%** | 0.853% |
| E–K \`n+p\` vs Caputo free baryons \`n_B(1-X_cluster)\` | **0.574%** | 0.939% |

By contrast, the literal top-two labels shift both E–K density curves by a
factor of ten. Their RMS relative residuals against the Caputo free-nucleon
curves are approximately 895% for both species. The corrected interpretation
is therefore strongly preferred by the same-model cross-publication check.

The sum of the E–K \`n\` and \`p\` curves does **not** follow total Caputo \`n_B\` in
the outer region. The residual relative to total baryons grows from about
0.44% at 8 km to 9.29% at 15 km. This is not a defect: it follows the Caputo
cluster baryon fraction, which grows from zero in the inner region to 8.85% at
15 km. Thus the E–K \`n,p\` curves are consistent with **free neutron and free
proton densities**, not with a partition of all baryons into only two free
species.

The density comparison is limited to 1–15 km, where the Caputo Fig. 4
abundance curves have common support. The E–K proton path itself terminates at
19.298 km; no extrapolation beyond a path's support is used.

## 6. Digitization uncertainty

The E–K density path stroke width is 1.071 PDF points. Half a stroke corresponds
to approximately:

- radius: 0.0542 km;
- temperature: 0.277 MeV;
- density: 0.0209 decades, or about 4.9% multiplicative uncertainty.

The sub-percent temperature and density residuals are therefore below the
figure-level line-width uncertainty. They should not be interpreted as
sub-percent agreement of the underlying raw hydrodynamic profiles.

## 7. Consequences for the EOS/transport work

1. The upper two Fig. 12 density-axis glyphs are visually ambiguous and are
   not extractable as PDF text spans. Keep both transforms in the archived raw
   data; use the equal-spacing calibration supported by Caputo for numerical
   comparisons, without claiming a definitive typesetting error.
2. The E–K neutron/proton curves are consistent with Caputo free-nucleon
   densities and with the cluster-corrected baryon sum. They should not be
   substituted for total \`n_B\`.
3. The free-nucleon composition must remain explicit in the local weak
   collision kernel. The omitted cluster response remains a separate physical
   contribution; this comparison does not calculate it.
4. No raw Garching profile, B.2 opacity, pure-vector Fig. 7 result, or
   axial-vector cooling curve is changed by this figure extraction.

## 8. Reproduction

Download the APS PDF from
\`https://journals.aps.org/prd/pdf/10.1103/718s-7k7v\` and verify its SHA-256
against the value in the provenance JSON. Then run:

\`\`\`bash
python extract_esseili_kribs_fig12_vector.py aps_fig12_source.pdf \\
  --outdir outputs
python audit_esseili_kribs_fig12_crosscheck.py --root . --outdir outputs
\`\`\`

The extraction script checks the exact PDF SHA-256, expected path colors,
plot-frame bounds, and writes the vertex CSV and provenance JSON. The
cross-check script reads only the archived Caputo/Bollig profile records and
the extracted E–K vector paths.
