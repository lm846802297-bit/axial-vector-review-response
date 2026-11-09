# Caputo off-frame thermodynamic vector-vertex audit: 20--22 km

Date: 2026-11-09

## Source identity and visible frame

- Source PDF: https://arxiv.org/src/2109.03244v3
- SHA-256: 19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e
- The existing extraction map defines the visible top-panel radial frame as 0.1--20 km.
- The T and mu_mu PDF drawing paths continue beyond the visible right edge; the 20--22 km segment is encoded off-frame vector data.

## Off-frame path audit

| Curve | Total vertices | 20--22 km vertices | Value range in 20--22 km | CSV-vs-PDF max relative residual | Continuity gaps |
|---|---:|---:|---:|---:|---:|
| T | 404 | 45 | [3.5593029764985356, 4.198857323941706] | 1.354e-12% | 0 |
| mu_mu | 251 | 48 | [6.106781624100045, 14.745120038474239] | 9.013e-11% | 0 |

## Selected off-frame values

| r (km) | T (MeV) | mu_mu (MeV) |
|---:|---:|---:|
| 20 | 4.204423025594307 | 14.77142401797812 |
| 20.5 | 3.9732831966903057 | 13.519248033404269 |
| 21 | 3.793739369398038 | 12.140970585475124 |
| 21.5 | 3.6594855725690887 | 10.122891954952108 |
| 22 | 3.55138904910432 | 5.519979123189131 |
| 22.19 | 3.5155788776791392 | 1.1183211607064063 |

## Interpretation and limits

The 20--22 km T and mu_mu inputs are not extrapolations invented by the current calculation: the coordinates are present in the Caputo PDF vector drawing paths and are reproduced by the committed vertex CSVs. However, they lie outside the visible 0.1--20 km plotting frame. This makes them encoded off-frame figure data, not visible plot data and not a substitute for the original Garching simulation tables.

The independent Bollig Fig. 1 and Fig. 4 comparison remains valid only through 20 km. Thus the off-frame Caputo continuation is anchored by excellent agreement at the 20 km boundary but has no independent Bollig cross-check over 20--22 km.

The B.16 +/-10% temperature and +/-1 MeV mu_numu floor tests quantify sensitivity to these inputs; they do not establish their true uncertainty.

No production profile or physical output is modified.

## Reproducibility

- Script: audit_caputo_offframe_thermodynamic_vertices.py
- Machine-readable result: outputs/caputo_offframe_thermodynamic_vertices_20_22km_2026-11-09.json
- Profile provenance: ../data/profile_provenance.json
