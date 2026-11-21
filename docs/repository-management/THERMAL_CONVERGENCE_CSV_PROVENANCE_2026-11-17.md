# Original-UV / Two-VEV thermal-convergence CSV provenance disposition

Date: 2026-11-17

Scope: source attribution and interpretation of the two historical
`thermal-convergence-2026-11-05.csv` tables. This note does not change the
semi-Compton matrix element, thermal rates, model-specific width results, or
any supernova constraint.

## 1. Exact file identity

The CSVs on the Original-UV and Two-VEV research branches are byte-identical:

| Item | Value |
|---|---|
| Path on Original-UV branch | `research/stellar-cooling-original-uv-model-20261105/thermal-convergence-2026-11-05.csv` |
| Path on Two-VEV branch | `research/stellar-cooling-two-vev-20261105/thermal-convergence-2026-11-05.csv` |
| Shared Git blob SHA-1 | `075314ff389cfa2eade061d8a6d359473e8225c2` |
| Rows | 8 data rows |
| Columns | `study, order, p_max_MeV, photon_max_MeV, phi_order, event_rate_MeV4, emissivity_MeV5, relative_rate_percent, relative_emissivity_percent` |

The convergence driver is also byte-identical on both branches:
`stellar_semi_compton_thermal_convergence.py`, blob
`e36ab13ae32216ae4d3c9a2323099485f880a1b0`. This is a shared generic
thermal-kernel benchmark, not two independently generated model-specific
convergence tables. The model-specific width implementations remain separate.

## 2. The CSV reference formula is not the current driver's order-sweep formula

The archived CSV's four order-sweep rows use the order-10 row as their
reference:
[
\delta Q_N^{\rm CSV}=100\left(\frac{Q_N}{Q_{10}}-1\right),
\qquad
Q\in\{\Gamma,\mathcal E\}.
]

This is confirmed by the archived values:

| Gauss order | `phi_order` | Rate relative to order 10 | Emissivity relative to order 10 |
|---:|---:|---:|---:|
| 6 | 12 | +0.835443% | +3.253905% |
| 8 | 16 | +0.210722% | -0.067038% |
| 10 | 20 | 0 | 0 |
| 12 | 24 | -0.010803% | +0.020199% |

The current driver instead sets
`reference_rate = order_values[-1]` and
`reference_emissivity = order_values[-1]`; for the recorded order list
`[6, 8, 10, 12]`, this means order 12 is the order-sweep reference.
Re-expressing the same four archived numerical rows relative to order 12
would give:

| Gauss order | Rate relative to order 12 | Emissivity relative to order 12 |
|---:|---:|---:|
| 6 | +0.846338% | +3.233053% |
| 8 | +0.221549% | -0.087219% |
| 10 | +0.010804% | -0.020195% |
| 12 | 0 | 0 |

The four cutoff rows are different: they are relative to the order-10 default
cutoff benchmark, which is consistent with the current driver's cutoff
branch. The CSV cutoff reference is
`p_max=195.03080572053227 MeV`,
`photon_max=200 MeV`, `order=10`, `phi_order=20`:

| Variation | Rate change | Emissivity change |
|---|---:|---:|
| (p_{\max}=160) MeV | -0.188694% | -0.438520% |
| (p_{\max}=240) MeV | +0.013690% | +0.042405% |
| (\omega_{\max}=160) MeV | -0.012605% | +0.008413% |
| (\omega_{\max}=240) MeV | +0.019111% | -0.046954% |

Consequently, the CSV is **not** the output of the current driver blob as a
whole. The exact historical producer/run that wrote this CSV has not been
recovered. We explicitly withdraw direct-producer attribution; the values
are retained as a separately identified legacy table, not silently
regenerated or relabeled as output from the current driver.

## 3. Two-VEV scan is joint quadrature refinement

For the Two-VEV branch the archived rows pair
[
n_\phi=2n_{\rm GL},
\]
namely ((6,12),(8,16),(10,20),(12,24)). The order sweep therefore changes
the Gauss-Legendre and azimuthal orders together. It is a **joint quadrature
refinement**, not an independent azimuthal convergence test. The table
cannot support a claim that (n_\phi) has independently converged.

The identical CSV blob on both branches is another reason not to present it
as two independent model-specific convergence studies. The model-specific
width scripts are different:
- Original-UV current `axial_decay_widths.py` blob:
  `32cc52210464d7e7618ca5b6e84be84ba616434e`.
- Two-VEV current `axial_decay_widths.py` blob:
  `be2aefbd9078f43b8aa586f5516ce4caf953a107`.

The earlier Original-UV width-script blob
`8f2d320858bd16173f16bed72af3d1cf1d8a8625` is recorded in the prior
historical audit, but that object is not retrievable from the current
reachable Git object history. We therefore record the old/current hash
relation without claiming a fresh byte-level or formula-body diff. No
model-specific width result is inferred from the shared convergence CSV.

## 4. Ward and energy-conservation residual scope

The validation notes state that the vacuum-amplitude test suite covers the
electromagnetic Ward identity for vector, axial, and mixed currents. The
thermal-convergence CSV contains no Ward residual column and is not evidence
for a new Ward-identity bound. The separately recorded medium-frame
energy-conservation residual is (3.553\times10^{-15}) at the stated
homogeneous-cell benchmark. It is an absolute, benchmark-specific numerical
residual, not a relative convergence percentage or a universal bound over
the parameter space.

## 5. Disposition

- Keep the eight-row CSV unchanged and label it as a **legacy archived
  convergence table** with unknown exact producer.
- Keep the order-10 reference formula for interpreting its archived
  `relative_*_percent` columns.
- Do not attribute the table to the current driver blob.
- Describe the Two-VEV order sweep as joint (n_{\rm GL})-(n_\phi)
  refinement; do not call it independent azimuthal convergence.
- Preserve the separate Original-UV and Two-VEV width-code fingerprints.
- Do not infer a converged SN luminosity, opacity, trapping result, or
  supernova exclusion from this homogeneous optically thin benchmark.

This closes the **documentation/provenance disposition** for the two
historical convergence tables. It does not expand the physical scope of the
underlying validation and does not replace the need for a newly generated,
fully source-pinned model-specific convergence study if such a study is
later required.
