# Forty-ninth review: B.16 outer-shell and thermodynamic-input records

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Branch: maintenance/repository-organization-audit-20261114  
Reviewed source snapshot: 38acc0837d9457d3c96b25a1ae00c3ded5635931

## 1. Executive result

Six baseline documents were individually reviewed against their cited scripts, tests, machine-readable outputs, profile fingerprints, workflow definitions, and later current-profile records. Three are classified HISTORICAL and three PASS_WITH_NOTES. This batch corrects one physical description, makes one earlier pointwise note explicitly historical, and adds an artifact-provenance map to the P1-B.2 report.

No production rate, opacity, coupling, luminosity curve, transport output, or axial-vector constraint was recalculated or modified.

The baseline document register now contains 294 individually reviewed documents and 168 PENDING documents: 190 PASS_WITH_NOTES, 2 PASS, 9 REVISION_REQUIRED, and 93 HISTORICAL.

## 2. Individual document outcomes

| Document | Outcome | Findings and disposition |
|---|---|---|
| B16_OUTER_ESCAPE_ANGULAR_DISTRIBUTION_2026-11-08.md | HISTORICAL | Paired JSON identifies the 501-node uniform profile, SHA-256 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9. The report already labels this profile version historical. Preserve the angular/emission-radius decomposition as provenance; do not merge its numbers with the vertex-preserving output. |
| B16_OUTER_INPUT_AND_INVERSE_DECAY_AUDIT_2026-11-08.md | PASS_WITH_NOTES | Section 1 uses the 1687-row profile-A input (6c47d071...); Section 2 and its direct B.6 JSON use the 501-node profile (08d7afce...). The document explicitly records this section-level split. Profile A and the later profile B differ only at floating-point serialization level in active thermodynamic columns, but the older Section-2 sample remains historical. |
| B16_OUTER_PROFILE_NEUTRINO_OPACITY_DIRECTION_AUDIT_2026-11-08.md | HISTORICAL | The paired outer escape and direct inverse-decay outputs use the 501-node uniform profile. Its equation mapping and historical diagnostics remain useful, but the file itself warns against combining those values with current-profile results. |
| B16_OUTER_SHELL_POLARIZATION_RESOLVED_AUDIT_2026-11-09.md | PASS_WITH_NOTES | Uses current profile B, SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c, with 222 outer-shell nodes. The 48-point mode rates agree with 512-point direct checks at approximately 1.7e-15 (production) and 1.66e-15 (absorption); B.10 detailed balance closes at 3.55e-14. The mode-summed/scalar rate residual is 8.91e-8 and the outer path-column closure is 2.69e-8. Corrected the Compton-column wording as detailed below. |
| B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md | PASS_WITH_NOTES | The 36-ray V8 interpolation artifact reports a maximum total-optical-depth difference of 9.07e-6 between direct primitive-field/kernel evaluation and 642-node opacity interpolation. The Compton-only difference is 1.43e-3 but remains subdominant in total opacity. The broad ±10% input stresses are conditional tests, not profile uncertainties. Added a precise distinction between the archived V8 output and the separate Python driver. |
| B16_P1B_THERMODYNAMIC_INPUT_SENSITIVITY_2026-11-10.md | HISTORICAL | Retain the earlier pointwise B.7--B.10 local-derivative table. Its next action has been superseded by P1-B.2, P1-E2/P1-E3 and the consolidated Fig. 7 acceptance. No dedicated script, test module or machine-readable output is linked by this note; it is not a current global-luminosity sensitivity result. |

## 3. Profile-version and section-level provenance

The relevant fingerprints are distinct and must remain explicit:

- Uniform profile: 501 rows, SHA-256 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9.
- Vertex-preserving profile A: 1687 rows, SHA-256 6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc.
- Vertex-preserving profile B: 1687 rows, SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c.

The profile-version reconciliation documents that A and B have identical radial coordinates/node counts and differ only at floating-point serialization level in the active thermodynamic columns. This does not make the 501-node uniform profile identical to either vertex-preserving profile: support-boundary knots and local interpolation differ.

The outer-input/inverse-decay report is a mixed snapshot by design. Its Section 1 outer-profile input result uses profile A, while Section 2's direct B.6 angular-integral result uses the 501-node profile. The document's section-level provenance statement is sufficient to retain it as PASS_WITH_NOTES, provided downstream users do not pool the two sections as one profile realization.

## 4. Outer-shell polarization result and Compton wording correction

The current-profile mode-resolved calculation is restricted to the 22--25 km path segment. It is a diagnostic comparison among the literal scalar B.2 exponent, a one-third-opacity comparison, and production-weighted mode propagation. It is not a full-path luminosity result and does not authorize a factor-of-three correction to the published Fig. 7 baseline.

A later full-path vertex-preserving decomposition resolves the outer-shell Compton column as nonzero but negligible. For the dominant 8--15 km emission region at the strong endpoint:

\[
\overline{\tau}_{\rm Compton}^{22-25}/g_X^2=0.7934816881,
\]

\[
\left(\overline{\tau}_{\nu_\mu}^{22-25}
+\overline{\tau}_{\nu_\tau}^{22-25}\right)/g_X^2
=1.5633323742\times10^{15},
\]

\[
\frac{\overline{\tau}_{\rm Compton}}
{\overline{\tau}_{\nu_\mu}+\overline{\tau}_{\nu_\tau}}
=5.07558\times10^{-16}.
\]

The earlier phrase “zero at numerical precision” was therefore too strong. The audit document now says “nonzero but numerically negligible” and links the paired full-path JSON. No source, rate or transport output was changed.

## 5. P1-B.2 interpolation and thermodynamic sensitivity

The archived interpolation result is a direct V8 binary64 output. It records the 36-ray sample (four emission radii, three energies and three directions), the 1687-vertex profile fingerprint, the 4-point-per-segment path quadrature and the independent 8-point check. The maximum relative differences are:

- neutrino optical depth: 1.13e-6;
- semi-Compton optical depth: 1.432e-3;
- total optical depth: 9.07e-6.

The source-frozen 210--510 MeV stress tests show strong response to deliberately broad ±10% variations in T and charged-muon chemical potential, while the ±10% muon-neutrino chemical-potential changes alter the escaped band by less than 0.03%. These are sensitivity experiments under fixed source and fixed propagation conventions, not statistical errors or self-consistent perturbed supernova models.

The repository also contains a Python driver named audit_b16_p1b2_thermodynamic_input_sensitivity.py. Its default output filename and schema differ from the archived V8 JSON; it is a separate Python stress-test implementation and does not reproduce the 36-ray V8 primitive-field/kernel comparison. No dedicated test module for that driver is present. The report now records this distinction and the missing V8 source/invocation. The V8 JSON remains inspectable evidence but is not source-rerunnable from this repository.

## 6. Associated workflow review

Six workflow YAML files were individually inspected and their register rows updated to REVIEWED_WITH_NOTES. All six are branch-scoped to research/moving-muon-thermal-rates-20261107; workflow_dispatch is available, but a job-level condition also requires that branch. Thus these workflows are not PR checks for the maintenance branch.

Four historical Actions runs were independently fetched and confirmed completed/successful:

- #42486733302, outer-shell angular distribution, research-branch SHA 5bda11f13e11fa8a4ece16306eb728dddf4c611b.
- #42450499283, outer-profile input audit, research-branch SHA 5feab1135998df4765496f45b8cd8a2627843458.
- #42479382380, outer-profile path interpolation, research-branch SHA aa78b55fac8d6b26575c2fb9821ef8949f340d29.
- #42450822390, neutrino inverse-decay audit, research-branch SHA 71e00efeb72b664f98b23d8dd7623e0828356383.

These are historical research-branch runs, not checks on this maintenance PR. No new workflow was dispatched in this review.

All six workflows use Python 3.12 and install NumPy/SciPy without exact dependency pins. Five workflows have a test or direct quadrature check; the outer-profile path-interpolation workflow has no dedicated test step, and the direct inverse-decay workflow also has no test step. All six use contents:write because they commit generated JSON back to the research branch. The branch guards constrain that write-back, but a future hardening pass could consider artifact upload with contents:read where durable commits are not required.

## 7. Scientific boundaries

1. The reconstructed public-figure SFHo-18.8 profile is not the original raw Garching snapshot.
2. The B.2 fixed-\(\omega\) versus conserved-\(E_\infty\) convention ambiguity is not resolved by this batch.
3. Literal scalar B.2 attenuation and mode-resolved attenuation remain separate prescriptions; no empirical opacity rescaling or factor-of-three substitution is authorized.
4. Local detailed balance and quadrature closure do not establish the full physical Fig. 7 baseline or a final axial-vector exclusion.
5. No production axial outputs, coupling values, rates or luminosity curves were modified.

## 8. Disposition

The six document rows and six workflow rows are updated in their respective registers. The next document batch should continue from the next PENDING baseline row; do not revisit the three historical records unless a new provenance question arises.



## 9. Independent review of this report (2026-11-16)

**Reviewed against:** maintenance-branch HEAD \`50e7c42a868336a02273539990c04249b87f6dfb\`, the six source documents, their paired JSON outputs and Python drivers, the six workflow definitions, the workflow register, and the four cited historical Actions runs.

**Disposition of this report: PASS_WITH_NOTES.** The profile-version boundaries, the nonzero-but-negligible outer Compton column, the V8/Python separation, and the limitation of historical CI evidence are correctly stated. The independent review found two source-record inconsistencies that the original batch did not identify, plus one workflow-coverage wording issue. They are recorded below rather than silently changing historical numerical outputs.

### 9.1 Historical source-fraction value in the 501-node escape record

\`B16_OUTER_ESCAPE_ANGULAR_DISTRIBUTION_2026-11-08.md\` labels its paired output as the historical 501-node profile, SHA-256 \`08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9\`. The paired JSON independently confirms \`radial_nodes = 501\` and reports

\[
f_{8-15\,\mathrm{km}}^{\mathrm{historical}}
=0.7923233149765334
=79.2323315\%.
\]

The Markdown body instead says that the selected source contributes 79.61% of the global B.1 source. That value matches the later current-profile-B full-path JSON,

\[
f_{8-15\,\mathrm{km}}^{\mathrm{profile\,B}}
=0.7961143383648793
=79.6114338\%,
\]

with profile SHA-256 \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`. The 79.61% statement is therefore a current-profile value embedded in a historical-profile report. The historical JSON and the current-profile result must remain separate; the historical report's global source-fraction sentence requires correction or an explicit cross-version note. The three within-selected-source shell fractions are consistent with the historical JSON.

### 9.2 Outer-profile interpolation table versus paired JSON

The paired \`b16_outer_profile_inputs_10mev_2026-11-08.json\` is pinned to profile A SHA-256 \`6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc\`, as stated in the source document. Its stored interpolation summary does not reproduce several values in Section 1.2 of \`B16_OUTER_INPUT_AND_INVERSE_DECAY_AUDIT_2026-11-08.md\`:

| Quantity | Markdown | Paired JSON |
|---|---:|---:|
| \(T\) maximum absolute interpolation error | 0.00426 MeV | 0.0045676034 MeV |
| \(\mu_\mu\) maximum absolute interpolation error | 2.63 MeV | 2.7480281 MeV |
| Neutrino reduced-absorption maximum relative error | \(8.37\times10^{-4}\) | \(8.97123\times10^{-4}\) |
| Neutrino reduced-absorption RMS relative error | \(2.52\times10^{-4}\) | \(2.57820\times10^{-4}\) |

The JSON's \(\mu_\mu\) maximum relative-error field is \(1.7480\), evaluated wherever \(|\mu_\mu^{\rm truth}|>10^{-12}\); the Markdown's phrase “where meaningful” does not state its denominator floor. Those relative-error figures are not demonstrably the same statistic. The paired JSON does confirm the Compton-to-neutrino peak-rate ratio \(1.35262\times10^{-15}\), so the conclusion that Compton is negligible in this 10 MeV outer-shell local-rate comparison is unaffected. The interpolation table should be reconciled to the paired artifact or its distinct sampling/threshold convention should be documented.

### 9.3 Workflow coverage wording

The six workflow YAML files and their job-level branch guards were checked directly. Four workflows contain an explicit test step: outer escape, outer-profile inputs, outer-shell polarization-resolved, and the neutrino inverse-decay audit. Two do not contain a dedicated test step: outer-profile path interpolation and direct inverse-decay. Both still execute their named numerical audit scripts. The original phrase “five workflows have a test or direct quadrature check” is ambiguous; the auditable count is **4/6 with explicit test steps and 2/6 without dedicated test steps**. A numerical audit command is not automatically a regression-test suite.

All four cited historical runs were independently confirmed completed/successful on their stated research-branch commits. They are not checks on PR #115. The two workflows whose records say “no run claimed” remain static-only in this review. All six workflows use Python 3.12, unpinned NumPy/SciPy dependencies, \`contents: write\`, and a branch guard restricting the job to \`research/moving-muon-thermal-rates-20261107\`.

### 9.4 Claims confirmed and scientific boundary

The full-path vertex-preserving JSON confirms the outer-reference-shell source-weighted Compton column \(0.7934816880606981/g_X^2\), compared with the two-flavor neutrino column \(1.5633323742\times10^{15}/g_X^2\); their ratio is \(5.07558\times10^{-16}\). The report's correction from “zero” to “nonzero but negligible” is correct.

The 36-ray V8 artifact records its 1687-vertex profile, 642-node opacity grid, ray set and quadrature checks, and its maximum total-\(\tau\) difference \(9.06891\times10^{-6}\). Its V8 producer source is not archived; the separate Python driver does not reproduce that V8 comparison. The result remains a targeted diagnostic, not a full global transport rerun. The old P1-B pointwise note is correctly treated as historical.

**No production rate, B.2 opacity, luminosity, Fig. 7 curve, SN1987A limit, or axial-vector exclusion was changed or accepted by this review.** PASS_WITH_NOTES applies to the audit report's scope and traceability, not to full physical validation. The two source-record mismatches above remain explicit follow-up items.
