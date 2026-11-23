# RC-001 — VLL–Higgs–Singlet UV–EFT One-Loop Matching

> **Record type:** baseline consolidation and verification-gap tracking. This record does not assert that the complete matching calculation is finished.
>
> **Work status:** Verification in progress  
> **Overall model-level claim status:** Unresolved  
> **Created:** 2026-10-23  
> **Repository baseline at record creation:** `main` at `c992daac633ac9df3d0aad008e104125206cb890` (historical anchor; not a live pointer to the current `main` HEAD).

## 1. Scientific question

What can be established, under the explicitly recorded VLL–Higgs–Singlet model assumptions, by matching the UV theory onto an EFT at one loop, and what additional evidence is required before the results can be used as a complete nonredundant Wilson-coefficient set or a physical prediction for scalar mixing?

The record links the existing model definition, analytical derivations, symbolic checks, Mathematica runs, the unexecuted FeynArts/FeynCalc scaffold, and the current scope of the physical conclusions. It is a consolidation of existing work, not a new derivation and not a declaration that any unresolved result has passed verification.

## 2. Immutable baseline and provenance

### Primary research source

- **Document:** higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261021)(153)_matchete_mapping_version_history.md
- **Source location:** ChatGPT Library, file ID [private-library-id-withheld], version ID 1
- **Size:** 1,989,214 bytes
- **SHA-256:** f30af8ccc62feafa3923e8356437e4b80b40e518fc9b1188646b4d763e2791f1
- **Relevant sections:** §§248–251 (fixed-sector hard matching and effective-potential threshold); §§261–262 (broken-phase algebra and light-field soft functions); §273.9 (historical FeynArts/FeynCalc scaffold and effective-potential algebra check); §274 (parameterized momentum-dependent h–s self-energy, tracked as a downstream dependency only). Earlier candidate-kernel audits in §§238–240 are relevant to the open B1/B3 sign reconciliation. Section presence does not imply that every derivation in this cumulative working document has been independently revalidated.
- **Model reference used by the source note:** original paper, version v1, model section: https://arxiv.org/html/2608.27258v1#S2

The primary source is a Library artifact, not a file currently committed to this repository. The filename, Library ID/version, size, and SHA-256 identify the exact source used to seed this record. If a later source revision is adopted, add a new baseline entry rather than silently replacing this one.

### Supporting computational artifacts

| Artifact | SHA-256 | Status and scope |
|---|---|---|
| section273_feyncalc_threshold_workflow.wl | 8e2c7a36c5cacecf35194a92cde50e52ec457cb884684c719e5aafc6b67053ab | 2,577-byte annotated FeynArts/FeynCalc scaffold for the four-point portal threshold. It is not an execution log and has not been run. The custom FeynArts model file and schematic particle-label mapping are still required. |
| section273_feyncalc_audit_log.json | dea8c3ff0a18163d4e1b697a4a44ea44f33a416ab7c85adc3dc71c8bd11e0bfa | Historical audit log: its metadata identifies v76 as base_document and v77 as new_document. It records the effective-potential algebra check and FeynCalc as NOT RUN; it is not a v153 execution log. |
| uv_eft_audit_suite_output.txt | d8471c9b990671777d957ea1afa5b2c3d5e67ffd6e2e1f6925f7713f68d66a86 | Python bookkeeping/algebra audit output. It includes an unresolved historical candidate-kernel sign warning: B1 and B3 flip relative to prior definitions while B2 is unchanged. It lacks the complete external-leg permutation sum, counterterms, and UV–EFT subtraction; it does not validate CL-001. |

The supporting files above were located in the Library and their SHA-256 hashes were recomputed for provenance. The JSON audit log explicitly names v76 and v77, so it is a historical artifact included in the v153 source bundle, not a run performed against v153. Its PASS status applies only to the listed Coleman–Weinberg algebra and artifact-integrity checks; it explicitly says FeynCalc was NOT RUN. The Python audit output likewise records checks of its declared algebraic kernels, not a complete amplitude. In particular, its B1/B3 sign warning remains an open cross-reconciliation item described below. File integrity is verified; physical equivalence across source versions is not implied.

### Committed artifact bundle

The working tree behind an earlier generation of the primary source is committed at [artifacts/higgs-portal-v66-20261019](../artifacts/higgs-portal-v66-20261019/), with its inventory and provenance notes in [artifacts/README.md](../artifacts/README.md).

**This bundle does not supersede the v153 baseline.** It records the v66 main document (2026-10-19) together with the historical `work/` and `计算脚本/` trees. The bundle contains 138 files (12,445,122 bytes; 12.45 MB). Its purpose is to provide a committed, hashable location for this earlier generation's sources and outputs.

| Consequence | Detail |
|---|---|
| Hash match | `计算脚本/section273_feyncalc_threshold_workflow.wl` is byte-identical to the hash listed above (`8e2c7a36…053ab`). This establishes file provenance only; the FeynArts/FeynCalc scaffold remains unrun. |
| Not covered | `section273_feyncalc_audit_log.json` and `uv_eft_audit_suite_output.txt` are not in the v66 bundle; their hashes still refer to the Library copies. |
| Version gap | Results present only in the v153 source have no committed backing in this v66 bundle. Presence in the bundle does not establish a v153 claim. |
| Unchanged claims | All claim statuses in §6 and the open B1/B3 item are unaffected. Archiving scripts and outputs does not advance diagram-level verification. |

### Version lineage and future baseline adoption

This record distinguishes **historical artifact preservation** from **selection of the active research baseline**.

| Version | Role | Status and handling |
|---|---|---|
| **v66** (main document dated 2026-10-19) | Earlier research generation archived at [`artifacts/higgs-portal-v66-20261019`](../artifacts/higgs-portal-v66-20261019/) | Historical provenance only. It is not the latest research version and does not supersede v153. Its scripts, logs, and hash matches do not promote a scientific Claim. |
| **v153** (main source dated 2026-10-21) | Primary source selected in §2 for this record | **Current baseline for RC-001.** The overall model-level claim remains unresolved and the verification gaps in this record remain open. The primary source is currently identified by its Library filename, version metadata, byte count, and SHA-256; it is not yet committed as a complete source bundle here. |
| **Any later candidate version** | Possible successor to v153 | Not adopted merely because a newer filename or file exists. Review the substantive diff and evidence first. If adopted, update this primary-source entry deliberately; if its files are committed, add a new immutable artifact directory rather than editing v66. Record exact version/date, full filename, source location, byte count, SHA-256, explicit parent baseline, changes from that baseline, and which verification/Claim statuses do or do not change. |

The v66 and v153 labels identify different source states in the same research line; this archive is not, by itself, proof of byte-for-byte ancestry or scientific equivalence between them. Likewise, a future source hash proves the identity of that file, not the validity of its derivations. Preserve earlier bundles unchanged and use a separate versioned snapshot for each subsequently archived source state. The repository-level rules are summarized in [`artifacts/README.md`](../artifacts/README.md).


## 3. Model, scheme, and scope frozen for this record

The working UV interaction is the flavor-resolved VLL model

\[
\mathcal L_{\mathrm{int}}\supset
-\sum_{\ell=\mu,\tau}
\left[
y_\ell \bar L_\ell H E_{\ell R}
+\lambda_\ell S_\ell \bar E_{\ell L}\ell_R
+M_{E\ell}\bar E_{\ell L}E_{\ell R}
\right]+\mathrm{h.c.},
\qquad S_\mu=S,\quad S_\tau=S^* .
\]

The tree-level dimension-five coefficient convention used in the source record is

\[
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E\ell}}.
\]

The scalar invariants and portal term are

\[
X=H^\dagger H,\qquad Y=S^\dagger S,\qquad
V\supset \lambda_{HS}XY .
\]

For the hard matching sections, the baseline is the unbroken phase, massless light fermions, and integration of the heavy Dirac leptons \(E_\mu,E_\tau\), while \(H,S,A'\) and the light fields are retained in the EFT. Light-flavor off-diagonal Yukawa couplings are set to zero. Flavor-resolved expressions keep \(M_{E\ell}\) general; the equal-heavy-mass choice is a benchmark, not a necessary identity for every formula.

The two-point derivation fixes the Minkowski metric \((+---)\), \(D=4-2\epsilon\), the definition of the 1PI insertion \(i\Pi(p^2)\), the Passarino–Veltman \(A_0/B_0\) normalization, and the stated \(\overline{\mathrm{MS}}\) subtraction convention. The potential coefficient is defined in \(V\), while the Lagrangian contains \(-V\). These conventions must not be mixed when comparing signs.

### Working chiral scheme for the QLD8 open-line source/Fierz sector

For the QLD8 fermionic source/Fierz reduction only, use the following working prescription:
- \(D=4-2\epsilon\) and \(\overline{\mathrm{MS}}\), as fixed above;
- naive dimensional regularization with anticommuting \(\gamma_5\) on the open external-fermion lines;
- the minimal Fierz-difference evanescent operators \(E_{RR}^{(0)},E_{LL}^{(0)},E_{RL}^{(0)},E_{LR}^{(0)}\) defined in [RC-001-QLD-chiral-Fierz-identities.md](RC-001-QLD-chiral-Fierz-identities.md), with no \(O(\epsilon)\) physical-operator admixture at the definition stage.

This is a subsector-specific prescription, not a blanket \(\gamma_5\) rule for all RC-001 diagrams. The QLD8 one-background Green functions have open fermion lines. If a closed \(\gamma_5\) trace or anomaly-sensitive subgraph enters a later completion, treat it separately with an anomaly-preserving prescription (e.g. BMHV plus required finite symmetry-restoring counterterms), rather than extending anticommuting \(\gamma_5\) blindly. Additional antisymmetrized gamma strings generated by one-loop renormalization must be added to the evanescent basis as required; the four Fierz-difference operators alone are not asserted to close the full counterterm basis. UV and EFT amplitudes must use the same prescription.


### Included in RC-001

- The fixed four-Yukawa one-loop four-point hard-matching sector and its EFT soft subtraction.
- The heavy–light two-point hard functions, their \(p^0\), \(p^2\), and \(p^4/M_{E\ell}^2\) terms, and the related field/EOM matching recorded in the source.
- The zero-momentum effective-potential portal threshold, tracked separately from the \(p^2\) derivative coefficients.
- The existing broken-phase algebra and light-field soft-loop calculations, with their limited scope stated explicitly.
- The verification gap between analytical/symbolic checks and external diagram-level execution.
- Section 274's parameterized momentum-dependent h–s self-energy is tracked as a downstream dependency for the portal threshold and scalar-mixing analysis. Its recorded algebra checks do not constitute FeynArts/FeynCalc validation.

### Explicitly not claimed by this record

- A complete nonredundant Wilson vector for every operator and every UV-model sector.
- A unique numerical value for \(\lambda_{HS}\) or a unique physical scalar-mixing prediction; the required renormalized portal boundary is not fully specified in the baseline.
- A completed nonzero kinetic-mixing \(\epsilon_{BX}\) analysis or simultaneous integration of \(A'\).
- A completed full on-shell amplitude, external-leg/LSZ normalization, physical pole equation, or phenomenological exclusion.
- A completed FeynArts/FeynCalc diagram census or an independently reproduced full loop amplitude.
- Any conclusion about the separate Matchete/Warsaw-coefficient discrepancy (for example \(c_{ud1}\) or \(c_{lq1}\)); that is a distinct research question and must not be conflated with the scalar/two-point matching record.

## 4. Existing derivations and what they establish

### 4.1 Four-point derivative hard matching — source §248

For the fixed complex external legs \(H,S,H^\dagger,S^\dagger\), the source derives one connected 1PI UV box for each flavor and the corresponding EFT bubble with two \(C_{5,\ell}\) insertions. The local hard differences are recorded as

\[
i\Delta\Gamma_\mu^{(2)}
=i\,\frac{|C_{5,\mu}|^2}{16\pi^2}
\left[(L_\mu-2)s+\frac{t}{6}\right],
\]

\[
i\Delta\Gamma_\tau^{(2)}
=i\,\frac{|C_{5,\tau}|^2}{16\pi^2}
\left[(L_\tau-2)u+\frac{t}{6}\right],
\qquad
L_\ell=\ln\frac{M_{E\ell}^2}{\mu_R^2}.
\]

The source separates UV and IR poles, the EFT nonlocal logarithms, and the local polynomial. It also records the portal \(p^0\) projection of the same heavy/light fermion box separately from the \(p^2\) derivative projection. This prevents counting the same box as two different diagrams or placing the quartic threshold inside a dimension-six derivative coefficient.

**Evidence boundary:** this is an analytical fixed-sector matching ledger with symbolic consistency checks. The source explicitly states that FeynArts/FeynCalc was not run, that the full set of model sectors and nonzero kinetic mixing are outside this calculation, and that the full nonredundant Wilson vector and on-shell observables remain incomplete.

**Open cross-reconciliation — historical B1/B3 warning:** the cited Python audit output reports that, under its stated Minkowski/Wick convention, the prior candidate definitions of \(B_1\) and \(B_3\) have opposite signs to the Wick-rotated candidate kernel, while \(B_2\) is unchanged. The same output explicitly requires rechecking external-momentum continuation and numerator conventions before treating this as a physical correction; it does not include the full external-leg permutation sum, counterterms, or UV–EFT subtraction. Section 248 separately derives the fixed-external-leg hard-minus-soft local difference, but this record does not yet contain a term-by-term map proving that the earlier \(B_i\) candidate kernel is superseded by that result. Accordingly, EV-007 is not evidence validating CL-001, and no physical coefficient is changed on the basis of this warning alone.

### 4.2 Two-point hard matching — source §250

With the source's \(i\Pi\) convention, the flavor-resolved heavy–light scalar two-point function is recorded as

\[
\Pi_{\phi\ell}^{\mathrm{bare}}(p^2)
=\frac{|g_{\phi\ell}|^2}{16\pi^2}
\left[
-2M_{E\ell}^2(\Delta_{\mathrm{UV}}-L_\ell+1)
+p^2(\Delta_{\mathrm{UV}}-L_\ell+\tfrac12)
+\frac{p^4}{3M_{E\ell}^2}
+\frac{p^6}{12M_{E\ell}^4}
\right]
+O(p^8/M_{E\ell}^6),
\]

where \(g_{H\ell}=y_\ell\), \(g_{S\ell}=\lambda_\ell\), and \(L_\ell=\ln(M_{E\ell}^2/\mu_R^2)\). The source derives the common integral through \(A_0(M_{E\ell}^2)\) and \(B_0(p^2;0,M_{E\ell}^2)\), fixes the closed-fermion-loop sign, separates UV poles from finite pieces, and records the mass and wave-function counterterms. The \(p^4/M^2\) and \(p^6/M^4\) terms are finite hard coefficients; the \(p^6\) coefficient follows by extending the exact \(B_0\) series one term further, \(B_0=\Delta_{\rm UV}-L_\ell+1+z/2+z^2/6+z^3/12+\cdots\), so that the \(z^3\) coefficient in \(A_0+(M^2-p^2)B_0\) is \(1/12-1/6=-1/12\), with the overall self-energy sign giving \(+1/12\). This term has no new UV pole.

**Evidence boundary:** the derivation and exact-arithmetic checks are present in the baseline document. They validate the recorded algebra and conventions under the stated assumptions; they do not replace an external diagram-level implementation or establish the full model's physical pole spectrum.

### 4.3 Zero-momentum portal threshold — sources §§248.6, 251, 273.9

The source records the effective-potential threshold

\[
\Delta V\big|_{XY}
=-\sum_{\ell=\mu,\tau}
\frac{|y_\ell|^2|\lambda_\ell|^2}{8\pi^2}XY,
\]

and therefore, under the stated potential convention,

\[
\lambda_{HS}^{\mathrm{EFT}}(\mu_R)
=\lambda_{HS}^{\mathrm{UV}}(\mu_R)
-\sum_\ell\frac{|y_\ell|^2|\lambda_\ell|^2}{8\pi^2}
+\cdots .
\]

The source reports agreement between two effective-potential expansion routes for the stated background-field coefficients, along with exact-polynomial and high-precision checks. The small standalone Mathematica file in §273.9 is a **scaffold** for the separate FeynArts/FeynCalc four-point calculation; the companion audit log says FeynCalc was not executed. Thus the effective-potential algebra is checked, but the diagram-level UV amplitude minus EFT amplitude has not yet been independently run end to end.

### 4.4 Broken-phase transformations and soft functions — sources §§261–262

The source records a local Mathematica 14.2.0 execution for the section-261 symbolic matrix/EOM checks: 25 Mathematica symbolic checks passed. The associated Python audit reports 59 exact broken-phase checks, three independent diagonalization cases, and three truncation-scaling cases. These are algebraic and matrix-consistency checks, not a loop-diagram calculation.

For section 262, the source reports 62 exact light-fermion checks, eight \(B_0\) integrals, three derivative integrals, and three massless-limit checks in Python; the local Mathematica check reports 25 symbolic checks and six high-precision \(B_0\) integrals. The source explicitly says FeynArts/FeynCalc, Matchete, and matchmakereft were not run for these sections, and that the complete physical spectrum still requires additional light-field contributions and a consistent input/tadpole scheme.

These results can support the corresponding algebraic subclaims within their recorded scope. They must not be described as full external loop-package validation or as a final physical mixing angle.

### 4.5 Downstream dependency: momentum-dependent h–s self-energy — source §274

Section 274 derives a parameterized mass-eigenstate expression for the momentum-dependent h–s self-energy and states the zero-momentum relation

\[
\Pi_{hs}^{F,\mathrm{hard}}(0)=-v_hv_s\,\Delta\lambda_{HS}^{E}
\]

under its stated inverse-propagator and potential conventions. It also defines how the hard contribution is to be combined with the EFT soft self-energy in a later pole equation. The section intentionally does not quote a unique numerical pole or mixing angle because the model parameters do not specify a unique benchmark.

The associated standalone algebra audit is reported in the source as four checks of the numerator identity, PV reduction structure, UV-overlap cancellation, and the zero-momentum sign relation. It does **not** numerically evaluate the PV integrals and does not call Mathematica/FeynCalc. Therefore, for RC-001 this is a downstream analytical/algebraic dependency, not an independently diagram-validated self-energy result. The full UV/EFT hard-minus-soft self-energy, consistent portal boundary, tadpole/input scheme, and physical pole solution remain open.

The dependency must be revisited after the portal threshold and two-point matching are reconciled. Do not infer that validation of the effective-potential coefficient alone validates the finite-\(p^2\) self-energy or a physical scalar-mixing prediction.

## 5. Evidence ledger

| Evidence ID | Artifact / location | What it checks | What it does not establish |
|---|---|---|---|
| EV-001 | Baseline document §§248.1–248.9 | Fixed four-Yukawa Wick pairing, UV/EFT local subtraction, scale/log and pole bookkeeping | Full-model diagram census, all operators, external package reproduction, on-shell observables |
| EV-002 | Baseline document §§250.1–250.13 | \(i\Pi\) convention, loop phase, PV combination, hard \(p^0,p^2,p^4/M^2\) terms, counterterms and field/EOM bookkeeping | Full model counterterm matrix or physical pole/LSZ result |
| EV-003 | Baseline document §251 | Effective-potential threshold and higher scalar-potential coefficients from two analytical routes | General off-shell derivative operators, gauge/fermion external-leg matching, physical mixing angle |
| EV-004 | Baseline document §261 and embedded Mathematica log | 25 Mathematica symbolic checks of matrix/EOM/VEV transformations; related Python matrix checks | FeynArts/FeynCalc execution or direct verification of every hard loop coefficient |
| EV-005 | Baseline document §262 and embedded logs | Soft-loop functions, \(B_0\) integrals, massless limits and associated symbolic identities | Complete physical spectrum or full-model pole matching |
| EV-006 | section273_feyncalc_threshold_workflow.wl and section273_feyncalc_audit_log.json | Annotated scaffold plus a historical effective-potential algebra/artifact-integrity check. The JSON metadata identifies v76→v77, not v153. | Actual FeynArts diagram generation or FeynCalc reduction; no v153 execution log exists, and the scaffold remains unrun |
| EV-007 | uv_eft_audit_suite_output.txt | Selected numerator/trace/kernel algebra checks; includes the unresolved B1/B3 sign warning against the prior candidate kernel, with B2 unchanged | Does not validate CL-001 or settle the physical sign: no complete external-leg permutation sum, counterterms, or UV–EFT subtraction |
| EV-008 | Baseline document §274 and its linked algebra audit | Parameterized momentum-dependent h–s self-energy, the stated \(p^2=0\) relation to the portal threshold, and four reported algebraic checks | No numerical PV integration, no Mathematica/FeynCalc run, no full UV/EFT hard-minus-soft self-energy, and no physical pole solution |

## 6. Claim–evidence decisions at baseline

The RC-001-specific rows are recorded in the [RC-001 claim–evidence matrix](RC-001-claim-evidence-matrix.md); [templates/claim-evidence-matrix.md](../templates/claim-evidence-matrix.md) remains a generic reusable template.

- **CL-001 — Four-point derivative hard difference:** Conditionally supported for the fixed external legs, Yukawa order, massless-light-field setup, and scheme specified in §248. Full-model matching remains unresolved. The historical B1/B3 candidate-kernel warning is open; EV-007 does not validate this claim, and no term-by-term reconciliation has yet established whether §248 supersedes that earlier kernel.
- **CL-002 — Two-point hard kernel:** Conditionally supported for the stated heavy–light Yukawa sector and \(i\Pi\)/PV conventions in §250. External diagram-package reproduction remains open.
- **CL-003 — Portal threshold:** Conditionally supported as the effective-potential coefficient under the stated potential convention. The algebra audit JSON is historical (v76→v77), not a v153 run; the FeynArts/FeynCalc cross-check remains open.
- **CL-004 — Broken-phase symbolic/soft-function subclaims:** Supported only within the explicit algebraic and integral checks recorded in §§261–262. These checks are not a complete physical pole calculation.
- **CL-005 — Complete Wilson vector and physical scalar mixing:** Unresolved. The current evidence does not establish a unique complete vector or a final physical mixing prediction; §274 is a downstream analytical dependency and has not passed diagram-level validation.
- **CL-006 — Momentum-dependent h–s self-energy:** Conditionally supported at the algebraic level only, within the conventions and scope of §274. The reported checks do not include numerical PV integration, diagram-level UV/EFT hard-minus-soft validation, or a physical pole solution.

## 7. Verification plan and acceptance gates

The next actions are ordered by dependency.

1. **Freeze inputs and conventions.** Record the exact UV Lagrangian, field charges, \(C_5\) sign, mass basis, \(i\Pi\) definition, \(A_0/B_0\) normalization, regularization/subtraction scheme, retained EFT fields, and any benchmark choices. Do not silently promote \(M_{E\mu}=M_{E\tau}\) or \(\epsilon_{BX}=0\) from a benchmark to a general theorem.
2. **Resolve the historical B1/B3 cross-reconciliation.** Reconstruct the candidate kernel under one explicit Minkowski and external-momentum convention; trace the numerator reduction, Wick factors, closed-loop phase, vertex orientations, and all external-leg permutations. Compare its local projection with the separately derived §248 UV–EFT difference, including counterterms and EFT soft subtraction. Until the comparison is term-by-term complete, keep the discrepancy open and do not change a physical coefficient merely to reconcile the documents.
3. **Make the loop-package input executable.** Create and version the custom FeynArts model file for the actual VLL model; replace all schematic particle labels and confirm the generated graph list against the hand-derived graph ledger.
4. **Run and archive the diagram-level calculations.** Execute the relevant FeynArts/FeynCalc workflow with recorded Mathematica/FeynArts/FeynCalc versions, exact commands, warnings, diagram counts, intermediate expressions, and output hashes. Keep the portal \(p^0\) projection distinct from the derivative \(p^2\) projection.
5. **Compare by layer.** Compare the direct UV loop, the EFT soft graphs, UV/IR poles, counterterms, finite terms, and local operator projections separately. A match of the final simplified expression alone is not sufficient if conventions or IR subtraction differ.
6. **Perform a genuinely independent check.** Use a separately constructed derivation or implementation for the high-impact coefficients. Do not count the same code path run twice as independent verification. Check known limits, dimensions, scale dependence, and the expected cancellation of nonlocal EFT logarithms and IR poles.
7. **Close the EFT basis and parameter boundary.** Include the required field redefinitions/EOM terms and any additional sectors retained by the model. Specify the renormalized \(\lambda_{HS}\) boundary and decide whether \(A'\) remains in the EFT or is also integrated out.
8. **Only then evaluate physical observables.** Combine the matched coefficients with the broken-phase mass matrix, light-field/tadpole contributions, external-leg normalization, and a stated on-shell process. Revisit §274's momentum-dependent h–s self-energy in the same hard/soft and input-scheme ledger before quoting a physical pole or mixing angle. Record uncertainties before making a phenomenological claim.

### Acceptance criteria

- [ ] Exact baseline and model assumptions are identifiable.
- [ ] Every reported result is linked to its derivation and actual computational artifact.
- [ ] Mathematica symbolic algebra, Python exact checks, historical audit logs, and FeynArts/FeynCalc diagram execution are reported as distinct evidence types.
- [ ] Historical artifacts naming earlier document versions are not represented as executions against v153.
- [ ] The B1/B3 sign discrepancy is reconciled against the complete labeled amplitude and UV–EFT subtraction, or remains explicitly open.
- [ ] UV and IR poles, finite terms, counterterms, and matching conventions are consistently separated.
- [ ] Required independent checks have actual outputs and are not merely planned.
- [ ] The claim–evidence matrix reflects the valid parameter domain and remaining gaps.
- [ ] No complete Wilson vector or physical mixing prediction is declared before all required sectors and observable-level matching are closed.

## 8. Current physical conclusion

At this baseline, the defensible conclusion is **partial and conditional**:

- The source contains an analytical fixed-external-leg UV–EFT local difference and related bookkeeping for the specified four-point sector, as well as heavy–light two-point hard functions.
- The zero-momentum portal threshold has an effective-potential algebra cross-check, but the associated JSON is a historical v76→v77 audit log, not an execution against v153; FeynArts/FeynCalc remains unrun.
- The Python audit output contains a historical B1/B3 sign warning for an earlier candidate kernel. Its scope is insufficient to settle the physical sign or to validate CL-001. The relationship between that candidate kernel and the independent §248 derivation remains to be reconciled term by term.
- Section 274 supplies a parameterized momentum-dependent h–s self-energy and an algebraically checked \(p^2=0\) relation to the portal threshold, but no numerical PV integration, diagram-level validation, complete hard-minus-soft self-energy, or physical pole solution.
- The complete nonredundant model-level Wilson vector, the required portal boundary, and the physical on-shell scalar-mixing prediction remain unresolved.

This record does not change or certify the physics result. It makes the baseline and evidence chain explicit and defines what must be completed before the final physical claim can be upgraded.



## 9. Follow-up calculation: explicit UV–EFT difference for the broken-phase \(h\)–\(s\) two-point function

> **Status: preliminary supplement; the source-aligned kernel and pole analysis are superseded/clarified in §10 below.** The finite dimension-six derivative matching remains provisional; this addition does not replace the frozen v153 baseline or certify a physical scalar-mixing result.

### 9.1 Definitions and UV kernel

Set
\[
x=m_{\ell,\mathrm{light}}^2,\qquad
y=m_{\ell,\mathrm{heavy}}^2,\qquad s=p^2,
\]
and use the mass-eigenstate scalar-kernel normalization
\[
\kappa=2ab\,c_Ls_Lc_Rs_R
\]
from the associated derivation. The UV four-path sum is recorded as
\[
\mathcal F_{\rm UV}(s)=\kappa\left[
(4x-s)B_0(s;x,x)+(4y-s)B_0(s;y,y)
-2(2x+2y-s)B_0(s;x,y)\right].
\]
Its overall UV pole cancels:
\[
(4x-s)+(4y-s)-2(2x+2y-s)=0.
\]
This cancellation must be checked using the complete set of mass-eigenstate paths and the exact vertex conventions of §274.

### 9.2 EFT bubble plus contact tadpole

For the EFT calculation, the follow-up derivation separates
\[
\mathcal F_{\rm EFT,bub}(s)
=\kappa\left[2A_0(x)+(4x-s)B_0(s;x,x)\right]
\]
from the contact-vertex tadpole
\[
\mathcal F_{\rm EFT,ct}(s)=2\kappa A_0(x).
\]
Thus
\[
\mathcal F_{\rm EFT}(s)=\kappa\left[
4A_0(x)+(4x-s)B_0(s;x,x)\right].
\]
With \(A_0|_{\rm pole}=x\Delta_{\rm UV}\) and \(B_0|_{\rm pole}=\Delta_{\rm UV}\), this EFT kernel has pole \(\kappa(8x-s)\Delta_{\rm UV}\). The UV-minus-EFT bare loop difference consequently has pole \(\kappa(s-8x)\Delta_{\rm UV}\). This is a bare difference, not yet a finite Wilson coefficient: the EFT local counterterms and their renormalization conditions must be included before interpreting it as a matched result.

### 9.3 Explicit subtraction

The common light-lepton bubble cancels exactly:
\[
\boxed{
\Delta\mathcal F_{\rm bare}(s)=
\kappa\left[(4y-s)B_0(s;y,y)
-2(2x+2y-s)B_0(s;x,y)-4A_0(x)\right].
}
\]
This isolates the heavy-heavy and mixed heavy-light loop functions together with the EFT contact tadpole. It is not valid to omit the mixed \(B_0(s;x,y)\) term.

Using
\[
A_0^{\rm fin}(x)=x\left(1-\ln\frac{x}{\mu_R^2}\right),\quad
B_0^{\rm fin}(0;x,x)=-\ln\frac{x}{\mu_R^2},
\]
and the previously derived full-theory zero-momentum kernel, the recorded finite difference is
\[
\boxed{
\Delta\mathcal F_{\rm fin}(0)=
\kappa\left[
\frac{8xy}{x-y}\ln\frac{x}{y}
-4y-8x+8x\ln\frac{x}{\mu_R^2}
\right].
}
\]
This zero-momentum expression is an algebraic subtraction using the existing full-theory kernel; it is not an independent numerical loop integration.

### 9.4 Heavy-mass expansion and the factor-of-two question

For \(y\gg x,|s|\), the follow-up expansion gives
\[
\Delta\mathcal F_{\rm fin}(s)=
\kappa\left[
-4y+8x\left(\ln\frac{y}{\mu_R^2}-1\right)
+s\left(\frac23-\ln\frac{y}{\mu_R^2}\right)
\right]+\cdots .
\]
The leading local mass term agrees algebraically with the effective-potential threshold after substituting
\[
\kappa\simeq
\frac{|y_{H\ell}|^2|\lambda_\ell|^2vv_s}{2M_{E\ell}^2},
\qquad y\simeq M_{E\ell}^2,
\]
and dividing the scalar-kernel difference by \(16\pi^2\):
\[
\Delta\mathcal F_{\rm fin}(0)\simeq-4\kappa Y
\quad\Longrightarrow\quad
\Delta\Pi_{hs}^{\rm hard}(0)=-\frac{\Delta\mathcal F_{\rm fin}(0)}{16\pi^2}
\simeq+\frac{|y_{H\ell}|^2|\lambda_\ell|^2vv_s}{8\pi^2}.
\]
The self-energy sign is positive because the source convention is \(\Pi=-\mathcal F/(16\pi^2)\); the scalar-kernel coefficient itself is negative.

The numerical change \(12\to6\) can be a pure normalization conversion if, and only if, the common prefactor changes at the same time:
\[
(y_hy_s)(12x-2s)=
\kappa(6x-s),\qquad \kappa=2y_hy_s.
\]
If the two expressions use the same prefactor, this identity does not explain their difference. The original derivation's full prefactors must therefore be checked, not only the bracket coefficients.

### 9.5 Reproducibility and limitations

The source-aligned v14 SymPy audit is now synchronized between `calculations/RC-001-uv-eft-two-point-difference.py` and `validation/RC-001-uv-eft-two-point-difference.txt`. The script was executed and passed 15 exact symbolic/algebraic checks. The log is the captured output of that run, not a manually reconstructed review log.

The checks cover the exact mass-basis C,D matrices and signed-mass identity, UV-pole cancellation, mixed-channel reduction, A0 cancellation, local pole cancellation for the EFT bubble-plus-contact subset, the finite zero-momentum subtraction, the large-mass expansion, the leading portal-threshold sign, and the detected finite 4/3 discrepancy.

The audit remains algebraic. It does not run Mathematica/FeynCalc, evaluate loop integrals numerically, complete all EFT soft insertions, or determine a final physical scalar-mixing observable.

## 10. Source-aligned mass-basis kernel and local counterterm reconciliation

This section supersedes the preliminary conventions in §9 wherever they are less explicit. The comparison is against the frozen v153 source record, especially §§274.1–274.5 and 276–285, plus the EFT bubble/contact derivation in §§185.1–185.4 and 186.2.

### 10.1 Exact mass-basis vertices and UV-pole identity

For one flavor,
\[
\mathcal M_\ell=\begin{pmatrix}0&a_\ell\\b_\ell&M_{0\ell}\end{pmatrix},
\quad a_\ell=\frac{y_\ell v_h}{\sqrt2},\quad
b_\ell=\frac{\lambda_\ell v_s}{\sqrt2},
\]
and \(U_L^T\mathcal M_\ell U_R=\operatorname{diag}(m_1,m_2)\), with signed physical eigenmasses \(m_1,m_2\). Set \(x=m_1^2\), \(Y=m_2^2\), \(s=p^2\). The heavy eigenmass \(m_2\) is not exactly the input parameter \(M_{0\ell}\) except in the leading heavy-mass expansion.

Using the source rotations and Yukawa matrices,
\[
G_h=\frac{y_\ell}{\sqrt2}
\begin{pmatrix}-c_Ls_R&c_Lc_R\\-s_Ls_R&s_Lc_R\end{pmatrix},\qquad
G_s=\frac{\lambda_\ell}{\sqrt2}
\begin{pmatrix}-s_Lc_R&-s_Ls_R\\c_Lc_R&c_Ls_R\end{pmatrix},
\]
the \(C,D\) matrices of §274 are
\[
C_{hs}=\begin{pmatrix}q_\ell&-q_\ell\\-q_\ell&q_\ell\end{pmatrix},\qquad
D_{hs}=\begin{pmatrix}q_\ell&r_\ell\\r_\ell&q_\ell\end{pmatrix},
\]
with
\[
q_\ell=y_\ell\lambda_\ell c_Lc_Rs_Ls_R,\qquad
r_\ell=\frac{y_\ell\lambda_\ell}{2}(c_L^2c_R^2+s_L^2s_R^2).
\]
The exact \((1,1)\) diagonalization condition is
\[
c_Lc_Rm_1+s_Ls_Rm_2=0,
\]
which implies
\[
q_\ell(x+Y)+2r_\ell m_1m_2
=y_\ell\lambda_\ell(c_Lc_Rm_1+s_Ls_Rm_2)
(s_Ls_Rm_1+c_Lc_Rm_2)=0.
\]
This exact identity is the required reason the complete UV mass-basis sum has no UV pole. It also justifies reducing the mixed-channel coefficient; the reduced expression is not an independent assumption.

### 10.2 Compact UV kernel and 1PI sign

Using the source PV convention,
\[
K_{ij}=A_0(m_i^2)+A_0(m_j^2)
+(m_i^2+m_j^2-s)B_0(s;m_i^2,m_j^2),
\]
the \(A_0\) terms cancel in \(K_{11}+K_{22}-2K_{12}\). Before using the exact mass identity, the complete one-flavor kernel is
\[
\begin{aligned}
\mathcal F_{\rm UV}^{\ell}(s)={}&q_\ell(4x-s)B_{11}
+q_\ell(4Y-s)B_{22}\\
&+\left[4r_\ell m_1m_2-2q_\ell(x+Y-s)\right]B_{12},
\end{aligned}
\]
where \(B_{11}=B_0(s;x,x)\), \(B_{22}=B_0(s;Y,Y)\), and \(B_{12}=B_0(s;x,Y)\). The exact identity gives
\[
4r_\ell m_1m_2-2q_\ell(x+Y-s)
=-2q_\ell(2x+2Y-s),
\]
hence the compact kernel already used in §9 follows. The source inverse-propagator convention is
\[
\Gamma_{\rm inv}(s)=s\mathbf1-\mathcal M_{\rm loc}^2+\Pi(s),\qquad
\Pi_{\rm UV}^{F,\ell}(s)=-\frac{\mathcal F_{\rm UV}^{\ell}(s)}{16\pi^2}.
\]
The signed light eigenmass must be retained in \(m_1m_2\); the propagator denominators use only \(m_i^2\).

### 10.3 EFT bubble and contact tadpole

The EFT subset consists of the light-state bubble and the \(hs\bar\ell\ell\) contact tadpole induced by the tree-level dimension-five interaction. With \(q_\ell^{\rm soft}=2g_{h\ell}g_{s\ell}=q_\ell\) in the real rotation convention,
\[
\Pi_{\rm bub}^{\ell}(s)=-\frac{q_\ell}{16\pi^2}
\left[2A_0(x)+(4x-s)B_{11}\right],\qquad
\Pi_{\rm ct}^{\ell}=-\frac{q_\ell}{16\pi^2}2A_0(x).
\]
Thus
\[
\Pi_{\rm EFT,bub+ct}^{\ell}(s)
=-\frac{q_\ell}{16\pi^2}
\left[4A_0(x)+(4x-s)B_{11}\right].
\]
The contact tadpole contributes to the constant term but has zero derivative with respect to \(s\). As stated in §284.3, this bubble-plus-contact subset is not yet the complete set of same-order EFT soft insertions required for a final dimension-six matching.

### 10.4 Subtraction, finite threshold, and sign

Define \(\Delta\mathcal F=\mathcal F_{\rm UV}-\mathcal F_{\rm EFT}\). The common \(B_{11}\) term cancels, giving
\[
\Delta\mathcal F_{\rm bare}^{\ell}(s)=q_\ell\left[
(4Y-s)B_{22}-2(2x+2Y-s)B_{12}-4A_0(x)\right],
\]
and
\[
\Delta\Pi_{\rm bare}^{\ell}(s)=-\frac{\Delta\mathcal F_{\rm bare}^{\ell}(s)}{16\pi^2}.
\]
With \(L_x=\ln(x/\mu_R^2)\), \(L_Y=\ln(Y/\mu_R^2)\),
\[
A_0^{\rm fin}(x)=x(1-L_x),\quad
B_{11}^{\rm fin}(0)=-L_x,\quad
B_{22}^{\rm fin}(0)=-L_Y,\quad
B_{12}^{\rm fin}(0)=1-\frac{xL_x-YL_Y}{x-Y},
\]
the finite zero-momentum kernel difference is
\[
\boxed{\Delta\mathcal F_{\rm fin}^{\ell}(0)=q_\ell\left[
\frac{8xY}{x-Y}\ln\frac{x}{Y}-4Y-8x+8xL_x\right].}
\]
For \(Y\gg x,|s|\),
\[
\Delta\mathcal F_{\rm fin}^{\ell}(s)=q_\ell\left[
-4Y+8x(L_Y-1)+s\left(\frac23-L_Y\right)\right]+\cdots .
\]
Because the 1PI self-energy is minus the kernel divided by \(16\pi^2\), the leading hard self-energy is positive:
\[
\Delta\Pi_{\rm hard}^{\ell}(0)\simeq+\frac{4q_\ell Y}{16\pi^2}
\simeq+\frac{|y_\ell|^2|\lambda_\ell|^2v_hv_s}{8\pi^2}
=-v_hv_s\Delta\lambda_{HS}^{E,\ell}.
\]
This matches the sign condition in §274.4. The leading dimension-four portal threshold is finite.

### 10.5 Local UV-pole counterterms for the stated EFT subset

The bubble-plus-contact kernel has pole \(q_\ell(8x-s)\Delta_{\rm UV}\), so
\[
\Pi_{\rm EFT,bub+ct}^{\ell}(s)\big|_{\rm pole}
=-\frac{q_\ell}{16\pi^2}(8x-s)\Delta_{\rm UV}.
\]
The local contribution to \(\Gamma_{\rm inv}\) required to cancel this pole is
\[
\boxed{\Pi_{\rm local\,CT}^{\ell}(s)\big|_{\rm pole}
=+\frac{q_\ell}{16\pi^2}(8x-s)\Delta_{\rm UV}.}
\]
For the derivative operator and normalization in §283.2,
\[
\mathcal L_{\rm EFT}\supset\frac{c_{\partial HS}}{M_*^2}
\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S),\qquad
\Delta\Pi^{(6)}(s)=\frac{c_{\partial HS}v_hv_s}{M_*^2}s,
\]
the pole counterterm is therefore
\[
\boxed{\delta c_{\partial HS}
=-\frac{M_*^2q_\ell}{16\pi^2v_hv_s}\Delta_{\rm UV}.}
\]
This cancels the derivative pole for the explicitly stated bubble-plus-contact subset. The constant pole is \(+8q_\ell x\Delta_{\rm UV}/(16\pi^2)\) in the local inverse kernel. Since \(q_\ell=O(M_E^{-2})\) and \(x=O(M_E^{-2})\) in the seesaw expansion, it is \(O(M_E^{-4})\), not the leading dimension-four portal divergence. The (C_5^2) soft-determinant pole is assigned to the (X^2Y^2) potential counterterm in the master source §§262.5 and 264.4; the complete dimension-eight hard matching remains open.

A separate ledger is available at validation/RC-001-uv-eft-counterterm-ledger.md. These pole results do not complete the finite matching.

### 10.6 Finite derivative coefficient: reconcile the legacy on-shell representative with the EOM-completed basis

The two-point hard difference after subtracting the stated renormalized-Yukawa bubble/contact subset gives
\[
\Delta\Pi_{\rm hard}^{(2{\rm pt})\,\prime}(0)
=\frac{q_\ell}{16\pi^2}\left(L_Y-\frac23\right)+O(M_E^{-4}\ln M_E).
\]
The older four-point route in §285.3 gives the on-shell representative
\[
\Delta\Pi_{\rm hard}^{(4{\rm pt}),\,\rm old\,rep\,\prime}(0)
=\frac{q_\ell}{16\pi^2}(L_Y-2)+O(M_E^{-4}\ln M_E),
\]
so the difference between these two representatives is
\[
\Delta\Pi_{\rm hard}^{(2{\rm pt})\,\prime}(0)
-\Delta\Pi_{\rm hard}^{(4{\rm pt}),\,\rm old\,rep\,\prime}(0)
=\frac{4q_\ell}{3(16\pi^2)}+O(M_E^{-4}\ln M_E).
\]
This is not the current same-basis matching discrepancy. The cumulative master source v153, §301.1–§301.4, records the off-shell external-leg momentum terms and the redundant operators \(T_H,T_S\), with \(\eta_H=\eta_S=-a_\ell/3\). Their EOM completion shifts the derivative coefficients by \(\Delta c_H=\Delta c_S=\Delta c_D=2a_\ell/3\), making the EOM-reduced four-point coefficients agree with the two-point coefficients in the same operator basis.

Therefore, retain the \(4/3\) result as a documented difference between the older on-shell representative and the two-point representation, but do not label it as an unresolved same-basis difference. Remaining open gates are the complete model-level Wilson vector, any still-unclosed higher-dimensional EFT soft/source sectors outside this restricted comparison, the complete dimension-eight hard matching, and independent diagram-level validation.

### 10.7 Audit artifact status

The synchronized v14 SymPy script at `calculations/RC-001-uv-eft-two-point-difference.py` was executed and passed 15 exact symbolic/algebraic checks. The paired output at `validation/RC-001-uv-eft-two-point-difference.txt` is the captured execution log. The checks cover the mass-basis C,D matrices, signed-mass identity, UV-pole cancellation, mixed-channel reduction, A0 cancellation, EFT subset pole and local counterterm, finite p²=0 subtraction, large-mass expansion, leading portal-threshold sign, and the historical 4/3 difference between the two-point result and the legacy on-shell four-point representative.

The cumulative master source v153 §301.1–§301.4 shows that the off-shell external-momentum terms and EOM completion by \(T_H,T_S\) align the specified Yukawa-box derivative coefficients in the same operator basis. The audit therefore reproduces the old representative difference; it does not classify that difference as unresolved after EOM completion.

This validation is algebraic only. It does not include numerical loop integration, FeynArts/FeynCalc/Mathematica/Matchete/Matchmakereft execution, complete model-level Wilson-vector closure, all remaining EFT soft/source sectors, or a final physical observable.

**Acceptance decision:** the exact mass-basis kernel, leading hard-self-energy sign, local pole cancellation for the stated EFT subset, and script/log reproducibility are supported. The complete dimension-eight hard matching, full model-level Wilson-vector closure, and independent diagram-level validation remain open. PR #4 stays open and in Draft state.
 
### 10.8 Source-aligned off-shell/EOM reproduction

To make the §301 reconciliation directly reproducible from the repository, two calculation artifacts and their captured outputs have been added:

- `calculations/RC-001-section252-offshell-eom-reproduction.py` — extracted from the cumulative master record §252.1–§252.10. It uses exact rational sparse-polynomial arithmetic and explicit tensor/radial integration rules to reproduce the recorded mixed and pure off-shell kernels, operator projections, EOM mapping, and potential/source companion bookkeeping.
- `validation/RC-001-section252-offshell-eom-reproduction.txt` — captured run output: 46 exact symbolic checks passed.
- `calculations/RC-001-offshell-eom-completion-audit.py` — an explicit coefficient-level audit of the §301 off-shell completion, including the \(a_\ell\Sigma/3\) difference, \(\eta_H=\eta_S=-a_\ell/3\), equal \(2a_\ell/3\) shifts of \(c_H,c_S,c_D\), and agreement with the two-point coefficients.
- `validation/RC-001-offshell-eom-completion-audit.txt` — captured run output: 5 exact symbolic checks passed.

These checks support the stated reconciliation between the old on-shell four-point representative and the EOM-completed same-basis coefficients. They are not independent diagram generation or a numerical loop integration. They do not close the complete model-level Wilson vector, every remaining higher-dimensional EFT soft/source sector, the dimension-eight hard matching, or the physical pole/mixing observable.

### 10.9 \(C_5^2\) soft constant pole: dimension-eight potential counterterm and truncation boundary

The EFT bubble-plus-contact subset gives
\[
\Pi_{\rm local\,CT}^{\ell}(s)\big|_{\rm pole}
=+\frac{q_\ell}{16\pi^2}(8x_\ell-s)\Delta_{\rm UV},
\qquad x_\ell=m_\ell^2.
\]
At leading seesaw order,
\[
q_\ell\simeq\frac{|y_\ell|^2|\lambda_\ell|^2v_hv_s}{2M_{E_\ell}^2},
\qquad
x_\ell\simeq\frac{|y_\ell|^2|\lambda_\ell|^2v_h^2v_s^2}{4M_{E_\ell}^2},
\]
so the constant projection is
\[
\Pi_{\rm local\,CT}^{\ell}(0)\big|_{\rm pole}
\simeq+\frac{|y_\ell|^4|\lambda_\ell|^4}{16\pi^2M_{E_\ell}^4}
v_h^3v_s^3\,\Delta_{\rm UV}.
\]
This is \(O(M_E^{-4})\), not the leading \(O(M_E^{-2})\) derivative counterterm or the dimension-four portal threshold.

The cumulative master source already identifies the gauge-invariant pure-potential representative in §§262.5 and 264.4. With \(X=H^\dagger H\), \(Y=S^\dagger S\) and \(m_\ell^2=c_\ell^2XY\), the \(C_5^2\) light-fermion determinant has
\[
V_{1,\rm UV}= \frac{c_\ell^4}{16\pi^2}\Delta_{\rm UV}X^2Y^2,
\qquad
\delta\mathcal L_{\rm pot,8}
=+\frac{c_\ell^4}{16\pi^2}\Delta_{\rm UV}X^2Y^2,
\quad c_\ell\simeq\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
Since
\[
\left.\partial_h\partial_s(X^2Y^2)\right|_{h=s=0}=v_h^3v_s^3,
\]
this counterterm reproduces the constant mixed-kernel pole above, including its sign in the convention \(\Gamma_{\rm inv}=p^2-\mathcal M_{\rm loc}^2+\Pi\). Equivalently, if writing a potential counterterm \(V_{\rm CT}\supset\delta c_{8,\ell}X^2Y^2/M_{E_\ell}^4\), then \(\delta c_{8,\ell}=-|y_\ell|^4|\lambda_\ell|^4\Delta_{\rm UV}/(16\pi^2)\); the Lagrangian counterterm has the opposite sign.

The relation is checked by `calculations/RC-001-dimension8-constant-pole-candidate.py`; four exact symbolic checks pass, with output in `validation/RC-001-dimension8-constant-pole-candidate.txt`. This is a verification of the \(C_5^2\) soft-potential subset counterterm, not a complete dimension-eight matching result.

**Remaining boundary:** the master source explicitly leaves the dimension-eight UV hard matching and the full \(O(M_E^{-4})\) prediction incomplete. Higher-dimensional tree-level EFT vertices and their soft insertions must be included at the same retained order. At strict \(O(M_E^{-2})\), the entire \(O(M_E^{-4})\) constant-pole set must be dropped consistently; it cannot be retained selectively and absorbed into the dimension-four portal counterterm.

### 10.10 EFT soft-insertion order-counting boundary

The cumulative master source §243.2 gives the tree-level un-reduced dimension-six operators
\[
\Delta\mathcal L_{\rm EFT}^{(6)}
=\frac{|y_\ell|^2}{M_{E_\ell}^2}Q_{LD}
+\frac{|\lambda_\ell|^2}{M_{E_\ell}^2}Q_{RD},
\]
with \(Q_{LD}=(\bar L_\ell H)i\slashed D(H^\dagger L_\ell)\) and
\(Q_{RD}=S_\ell^*\bar\ell_R i\slashed D(S_\ell\ell_R)\). Their VEV wavefunction pieces scale as
\[
\delta Z_L=\frac{|y_\ell|^2v_h^2}{2M_{E_\ell}^2},\qquad
\delta Z_R=\frac{|\lambda_\ell|^2v_s^2}{2M_{E_\ell}^2}.
\]
Consequently, within the specific \(C_{5,\ell}C_{5,\ell}^*\) Yukawa bubble,
\[
|C_{5,\ell}|^2\delta Z_L
\sim\frac{|y_\ell|^4|\lambda_\ell|^2v_h^2}{2M_{E_\ell}^4},
\qquad
|C_{5,\ell}|^2\delta Z_R
\sim\frac{|y_\ell|^2|\lambda_\ell|^4v_s^2}{2M_{E_\ell}^4}.
\]
These VEV wavefunction insertions are \(O(M_E^{-4})\) at fixed VEV and do not modify the restricted Yukawa-sector coefficient at \(O(M_E^{-2})\). The same order-counting argument does **not** prove that all EFT soft topologies are closed: the source §243.4 explicitly requires separate treatment of portal/scalar/gauge coupling structures and a method-of-regions check wherever inverse light-mass factors could enhance a nominally higher-order insertion. Section §284.3 therefore remains an open gate for any full-model claim.

### 10.11 EFT soft-topology census and target-order decision

An expanded topology and explicit heavy-mass power-counting ledger is now recorded in research/RC-001-eft-soft-topology-census.md. The companion structural script calculations/RC-001-eft-soft-topology-census.py and captured output validation/RC-001-eft-soft-topology-census.txt check 26 candidate topology families, one-loop Euler counts, and explicit inverse-\(M_E\) powers. The script does not evaluate integrals or claim external diagram-package validation.

The census separates four classes that must not be conflated:

1. **Direct mixed-scalar 1PI soft graph at \(O(M_E^{-2})\) in the fixed \(|y_\ell|^2|\lambda_\ell|^2\) sector:** the \(C_{5,\ell}C_{5,\ell}^\ast\) light-fermion bubble. Its PV expression and the specified off-shell/EOM completion are already recorded; independent diagram-level validation remains open.
2. **Other \(C_5C_5^\ast\) external-state channels:** four crossed two-fermion/two-scalar channels and one four-fermion scalar-loop channel are one-loop and \(O(M_E^{-2})\). Their scalar/vector integral kernels and hard/soft pole cancellations are now analytically checked; the full renormalized operator projection and external diagram-package validation remain open.
3. **Single \(Q_{LD}\) or \(Q_{RD}\) insertion plus a scalar quartic:** in a four-scalar amplitude the candidate is reducible and contains a scaleless fermion tadpole, so it is not an extra local 1PI scalar coefficient at strict \(O(M_E^{-2})\). In two-fermion/two-scalar amplitudes, however, the corresponding two-scalar-propagator bubbles are non-scaleless one-loop 1PI contributions at the same heavy-mass order.
4. **Gauge-current exchange and gauge corrections:** current-exchange graphs are reducible in the four-scalar amplitude and belong to a separate current/source ledger. Gauge corrections to \(Q_{LD}/Q_{RD}\) in their fermionic amplitudes are instead one-loop soft corrections at \(O(M_E^{-2})\) and require explicit integrals if those Wilson coefficients are in scope.
5. **Dimension-eight soft candidates:** \(Q_{LD}^2\), \(Q_{RD}^2\), \(Q_{LD}Q_{RD}\), \(C_5^4\), conditional \(C_5C_7^\ast\), and \(Q_{LD}/Q_{RD}\) VEV wavefunction insertions into the \(C_5C_5^\ast\) bubble carry \(O(M_E^{-4})\) at fixed VEV. They are excluded from a strict dimension-six truncation but must be included in the dimension-eight closure.

The v153 §252.8–§252.10 EOM/source table is a coefficient-mapping obligation rather than a new loop topology. Its dimension-six potential and renormalizable-source companions must be applied exactly once; \(C_5\)-dependent source terms begin at \(O(M_E^{-3})\), and \(C_5C_5^\ast\) source-square terms begin at \(O(M_E^{-4})\). The kinetic-mixing boundary remains unresolved, and the scalar/source projection does not close all fermionic external-state amplitudes.

**Decision:** the scalar bubble, crossed-current hard/soft kernels, four-fermion scalar bubble, and universal Q6-plus-quartic kernel have been independently reduced and checked algebraically. The next blocking tasks are external diagram-level validation, complete gauge corrections/contact terms/counterterms, and the full common-basis EOM/source projection. These remain necessary before the model-level Wilson vector can be called closed. PR #4 is intended to be integrated as an explicitly provisional research checkpoint; the model-level matching status remains unresolved.

## 10.12 Dimension-six soft integrals: independent hard/soft checks

The detailed calculation is recorded in research/RC-001-dim6-soft-loop-integrals-and-checks.md, with the reproducible script calculations/RC-001-dim6-soft-loop-crosscheck.py and captured output validation/RC-001-dim6-soft-loop-crosscheck.txt. The script passed 41 exact symbolic checks. These are analytic integral/tensor-reduction checks, not CI and not an external diagram-package run.

The massless bubble is independently reproduced as
\[
B_0(q^2;0,0)=\Delta_{\rm UV}-\ln\frac{-q^2-i0}{\mu_R^2}+2,
\]
with \(\int_0^1\ln[x(1-x)]\,dx=-2\), and the crossed vector integral gives \(\int k^\mu/[k^2(k+q)^2]=-q^\mu B_0/2\).

For the three \(C_5C_5^\ast\) crossed two-fermion/two-scalar channels with loop-dependent heavy propagators, the hard kernel contains
\[
\left(1-\frac2d\right)q^\mu J_{22}+\frac2d(p_3-p_1)^\mu J_{13}.
\]
Retaining the \(O(\epsilon)\) part of \(1-2/d\) yields the finite hard coefficient \(L_E/2-3/4\); the hard IR pole cancels the EFT soft UV pole. The on-shell \((p_3-p_1)^\mu\) term vanishes. The \(\bar L L H^\dagger H\) bare topology is different: its heavy propagators carry only external-channel momenta, so its \(O(M_E^{-2})\) loop is reproduced by the EFT soft region; counterterm/field/operator renormalization still must be matched.

The \(C_5C_5^\ast\) four-fermion channel has hard local scalar-bilinear coefficient
\[
\frac{|C_{5,\ell}|^2}{16\pi^2}(L_\ell-2),
\]
and its hard/soft sum has neither an uncancelled pole nor the constants \(\pm2\). In the \(Q_{LD}/Q_{RD}\)-plus-quartic channels, the hard/soft kernel is proportional to \(p+Q/2=(p-p')/2\), so the massless on-shell amplitude is EOM-redundant; its Wilson/source effect must be handled in the declared basis rather than counted as an independent current coefficient.

**Evidence boundary:** no FeynArts/FeynCalc/Mathematica diagram generation has been run. The bosonic field-strength and current-to-gauge matching already recorded in master §254 is separate and is not duplicated here. Remaining fermionic gauge corrections to \(Q_{LD}/Q_{RD}\) and current-current operators, covariant-derivative contact terms, counterterms, the complete weak-index/EOM source ledger, kinetic-mixing dependence, and the remaining dimension-eight hard matching are still open. Master §255.8 gives \(\Xi_{L_\ell}^{(4)}=\Xi_{R_\ell}^{(4)}=0\) for the \(\mu,\tau\) fields; therefore the new Q6-plus-quartic EOM kernels do not generate nonzero dimension-six Yukawa-source rows for those flavors at this order. A second local check was performed with calculations/RC-001-dim6-independent-kernel-check.py. Its captured output records 23 exact symbolic checks, including the direct Feynman-parameter logarithm, the crossed-current/four-fermion/Q6-quartic hard-soft sums, the Q6 EOM momentum ratio, and all 16 components of the SU(2) singlet/triplet completeness identity. This independent local check passed. Repository CI is explicitly skipped for this research iteration because the available GitHub Actions runner is not starting; the previous run returned runner_id=0 and no recorded steps. CI is therefore neither passed nor a closure gate here. The local scripts and captured outputs remain reproducibility aids, not a substitute for diagram-level amplitude validation.

PR #4 is merged as a provisional integration checkpoint; the model-level matching status remains unresolved and the physics closure gates remain open.

## 10.13 Dimension-six gauge-correction attachment atlas and subtraction ledger

A charge-aware attachment-class census is now recorded in `research/RC-001-dim6-gauge-diagram-atlas.md`, generated by `calculations/RC-001-dim6-gauge-atlas-census.py` and captured in `validation/RC-001-dim6-gauge-atlas-census.txt`. The one-external-gauge-field form-factor topology registry is recorded separately in `research/RC-001-dim6-current-form-factor-atlas.md`, so the \(\bar L L V\) and \(\bar\ell_R\ell_R V\) amplitudes are not conflated with the four-point attachment census. For each flavor \(\eta_\mu=+1,\eta_\tau=-1\), the structural census finds 10 \(BB\), 6 \(WW\), 3 \(A'A'\), and 9 mixed \(BA'\) attachment classes for the \(Q_{LD}\) tree exchange; it finds 3 \(BB\), 0 \(WW\), 10 \(A'A'\), and 7 mixed \(BA'\) classes for the \(Q_{RD}\) tree exchange. Mixed-propagator entries are based on the signed factor \(Y_i x_j+x_iY_j\), so charge-factor cancellations are retained. The differentiated composites \(H^\dagger L_\ell\) and \(S_\ell\ell_R\) are weak singlets and yield \(B,A'\) contact vertices but no direct \(W\) contact at the EFT operator insertion.

The companion `research/RC-001-dim6-uv-eft-subtraction-ledger.md` establishes one row per gauge-coupling sector and external amplitude, including the required UV/EFT pole-and-finite data, counterterms, Ward-identity checks, weak-tensor projection, EOM/source mapping, current amplitudes, and the kinetic-mixing boundary. The six SU(2)_L generator contractions for the Q_LD attachment classes are reduced to singlet/triplet tensors in `research/RC-001-dim6-SU2-attachment-projection.md` and pass a local exact SymPy tensor check (`calculations/RC-001-dim6-SU2-attachment-projection.py`, output `validation/RC-001-dim6-SU2-attachment-projection.txt`). These are group-theory factors only, not loop coefficients. The diagonal-gauge input-parameter pole sub-block for \(C_{LD}=|y|^2/M_E^2\) and \(C_{RD}=|\lambda|^2/M_E^2\) is derived in `research/RC-001-dim6-gauge-parameter-counterterms.md`; it is explicitly only the \(y,\lambda,M_E\) counterterm contribution, not the complete UV–EFT pole or finite matching result. Its rational combination is locally reproduced by `calculations/RC-001-dim6-gauge-parameter-counterterms.py`, with captured output in `validation/RC-001-dim6-gauge-parameter-counterterms.txt`; this is an arithmetic audit of the stated pole formulas, not an independent loop calculation. A first fixed-ordering Q_LD pure-WW cross-box sub-block is now evaluated as a unit-multiplicity subset; all other newly enumerated gauge-loop integrals and finite \(O(g^2/M_E^2)\) coefficients remain **NOT EVALUATED**. The atlas is complete at the charge-compatible attachment-class level, not an exact FeynArts diagram count.

The heavy-line self-energy, Yukawa-vertex scalar kernels, and a representative crossed-box UV-EFT scalar master are evaluated in research/RC-001-dim6-heavy-line-vertex-box-integrals.md. In addition, the four pure-WW cross-vertex classes for Q_LD have explicit fixed-routing numerator reductions and a hard/soft sum in research/RC-001-dim6-WW-crossbox-exact-routing.md. Their weighted result is (d-1)(J-K)/(2d), with unit-multiplicity hard finite term 11/16; an independent gamma-function integral reproduces the full master, and the longitudinal projector vanishes in the weak-triplet sum. The fixed-routing numerator and master checks are recorded in the companion script/test/validation files; full diagram-level verification remains open. A separate manual Wick-contraction audit enumerates the six unordered pairs among barL,H,Hdag,L, verifies the 2/(2!)=1 multiplicity for each, and checks the tree-level cancellation of the direct W contact in D_mu(Hdag L); five further local tests are recorded. The T3 tensor is mapped to the Pauli-triplet derivative representative Q_LD^(3)=(barL sigma^I H)i gamma^mu D_mu^adj(Hdag sigma^I L), including its EFT one-W contact. An exact off-shell Pauli/Fierz identity and its EOM/IBP reduction map Q_LD^(3)+Q_LD to -O_Hl^(1) plus the Hermitian Higgs-dressed Yukawa-source pair; three component-level SymPy checks are recorded. This contact/operator map is not the UV one-loop five-point form factor. This remains a fixed-ordering sub-block, not a complete gauge-matched Wilson coefficient: the transverse one-loop external-W form factor, complete Slavnov-Taylor sum, extension of the nonexceptional UV-EFT subtraction to all attachment classes, and full Wilson-vector assembly remain open. The self-energy result remains only a Feynman-gauge subgraph. The parameter-integral and partial-fraction algebra is recorded in calculations/RC-001-dim6-gauge-master-integrals.py and validation/RC-001-dim6-gauge-master-integrals.txt. A nonexceptional EFT-soft calculation now fixes the general heavy routing q_E=k-p1-p2 and gives the stripped T3 UV residue (1/2 slash p1+3/8 slash p2+3/4 slash p3), reducing to 3/8 slash P in the exceptional limit. All four symmetric soft triangles share (a-b)^2=4 mu_IR^2/3; the scalar triangle master and a finite nonlocal rank-three/pseudovector form factor are evaluated in research/RC-001-dim6-nonexceptional-matching-kinematics.md §§3.1–3.3 and its calculation/validation companions. The fixed-routing hard expansion is now also evaluated: R_J(d)=[(d^2-3d+4)/(4d)]p1+[(d-1)/(2d)]p2+[(d-1)/4]p3 and R_K(d)=-(d-1)(p1+p2)/(2d). Its pole residue matches the EFT-soft pole with opposite sign. The MS-bar finite local polynomial is (1/2-L/2)p1+(11/16-3L/8)p2+(1/4-3L/4)p3, reducing to the prior 11/16-3L/8 in the exceptional projection. The finite nonlocal rank-three soft term cancels against the EFT insertion for this fixed subset by the expansion-by-regions identity; the complete set of other diagrams remains open. The EFT numerator comparison is an algebraic derivative-momentum substitution, not an independent diagram-generation check: q_D=p3+p4+k=q_E by momentum conservation, so the pairwise residuals vanish identically. The two same-vertex WW classes LD-W-03/04 are now separately shown to be pure-soft: their heavy propagator carries only P=p1+p2, their light-loop factor is identical to the EFT Q_LD insertion with q_D=p3+p4=-P, and their hard-region loop integrals are scaleless. They therefore give zero hard-minus-EFT contribution at O(M_E^-2), while remaining in the EFT soft and Ward sums. See research/RC-001-dim6-WW-same-vertex-soft-matching.md and its explicit numerator/chiral-projection check and validation output.

The additive \(B-A'\) vacuum-polarization pole and heavy threshold are separately derived in \`research/RC-001-dim6-mixed-kinetic-threshold.md\`. The stated light chiral spectrum has zero \(\operatorname{Tr}(YX)\) flavor by flavor; the two heavy vector-like leptons cancel the additive UV pole across \(\mu,\tau\), but leave the finite threshold \(g_Yg_XQ_\ell(12\pi^2)^{-1}\ln(M_{E_\mu}^2/M_{E_\tau}^2)\) if their masses differ. This does not set the independent kinetic-mixing boundary or complete the mixed-propagator four-point matching.

The runtime availability check is recorded in `validation/RC-001-dim6-diagram-tool-availability.txt`. SymPy is available, but no Mathematica/Wolfram executable, FeynCalc, FeynArts, pyfeyn, or QGRAF installation is available in this execution environment. Thus no independent diagram-level amplitude calculation is claimed. The GitHub Actions was attempted and retried on HEAD 29d73dac582dfd2883cdd7dea5b36b5da98d4bc9; both attempts returned runner_id=0 and no recorded steps. This is a runner/infrastructure failure, not evidence of a script assertion failure. By explicit project decision, CI is skipped and is not a closure gate for this iteration. No repository-CI pass is claimed; the scientific closure gates remain the uncomputed UV–EFT amplitudes and independent diagram-level validation.

## 10.14 Benchmark A/B EFT5/O8 reconciliation with PR #69 (2026-11-09)

The \(O_8=(H^\dagger H)^2(S^\dagger S)^2\) operator and its leading \(C_5^4\) soft-potential UV pole are **prior RC-001 results**, already recorded in §§262.5, 264.4, and 10.9. The independent Higgs--radial-scalar calculation in [axial-vector-review-response PR #69](https://github.com/lm846802297-bit/axial-vector-review-response/pull/69) reconstructs this subset at the original paper's Benchmark A/B points and adds a benchmark-level Plan-C scale-closure check. It is not a first discovery of \(O_8\).

### 10.14.1 Convention lock

The cross-repository comparison uses the active RC-001 convention
\[
\mathcal L_{\mathrm{EFT5}}\supset-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.},
\qquad
\mathcal O_{5,\ell}=(\bar L_\ell H)S_\ell\ell_R,
\qquad
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
This sign follows from the Schur complement of the UV charged-lepton/VLL mass matrix. The corresponding signed mass parameter is \(m_\ell^{\mathrm{EFT5}}=C_{5,\ell}v_hv_s/2\); the positive physical mass entering the determinant is \(|m_\ell^{\mathrm{EFT5}}|\). A positive \(C_5\) is an equivalent alternative only if the operator term is written \(+C_5\mathcal O_5\). The \(O_8\) pole, running, and scalar-potential coefficients depend on \(|C_5|^4\), so the sign convention does not alter those numbers.

### 10.14.2 Bubble/contact bookkeeping

The exact-SVD light-light subtraction discussed in the matrix audit is a bubble-only intermediate quantity. The separate archived Plan-C-lite finite soft function is **not** bubble-only: the 2026-10-27 higgs_portal_planC_lite.py implementation (function pi_soft_planb) evaluates a bubble and a dimension-five contact tadpole and returns their sum. Its source blob SHA is df139e099853246501d2fbf9957dbba890014d14. The PR #69 scale-check implementation independently retains bubble + contact + hard.

Consequently, the contact tadpole must not be added a second time to the Plan-C finite soft self-energy. The new PR #69 result completes the local UV-pole identification and the \(O_8\) running; it does not discover an absent finite contact term in the archived Plan-C code. The two statements—bubble-only exact-SVD subtraction and contact-complete Plan-C soft function—refer to different objects.

### 10.14.3 Benchmark-level pole and scale check

PR #69 independently reconstructs
\[
\delta c_8=-\frac{1}{16\pi^2}\sum_{\ell=\mu,\tau}|C_{5,\ell}|^4
\]
as the potential counterterm coefficient multiplying \(\Delta_{\mathrm{UV}}\), and reproduces the full leading-EFT5 mixed local Hessian \(F_{hs}=16F/(v_hv_s)\), split into \(12F/(v_hv_s)\) from the bubble and \(4F/(v_hv_s)\) from the contact.

At \(s=m_h^2\), in the Plan-B sign convention \(\Pi_B=-\Pi_{\mathrm{RC}}\), the retained soft-plus-hard scale derivative obeys
\[
\frac{d\Pi_{hs,B}^{\mathrm{soft+hard}}}{d\ln\mu}
=2\Pi_{hs,\mathrm{EFT5},B}^{\mathrm{loop,UV}},
\qquad
\beta_{c_8}^{\mathrm{loop}}
=-\frac{2}{16\pi^2}\sum_\ell|C_{5,\ell}|^4.
\]
Here \(\Pi_{hs,\mathrm{EFT5},B}^{\mathrm{loop,UV}}\) denotes the Plan-B loop-pole coefficient, not its counterterm. The \(O_8\) running contributes the opposite scale derivative. The symmetric finite-difference derivative agrees with the analytic result to relative \(5.35\times10^{-8}\) (A) and \(3.37\times10^{-8}\) (B); the residual after including \(O_8\) running is \(1.73\times10^{-13}\) (A) and \(1.50\times10^{-13}\) (B).

### 10.14.4 Finite heavy-VLL scalar-potential contribution

The same PR independently expands the exact heavy singular value in the VLL Coleman--Weinberg determinant. In the specified background-field/\(\overline{\mathrm{MS}}\) scalar-potential basis at \(\mu=M_E\), it obtains
\[
c_8^{\mathrm{VLL,CW}}(M_E)
=-\frac{7}{2(16\pi^2)}
\sum_{\ell=\mu,\tau}|C_{5,\ell}|^4,
\]
with \(c_8^A=-3.80925598\times10^{-17}\,\mathrm{GeV}^{-4}\) and \(c_8^B=-9.76902113\times10^{-20}\,\mathrm{GeV}^{-4}\). The exact heavy-eigenvalue expression and the dimension-eight-truncated background expansion agree to relative \(2.96\times10^{-11}\) at both benchmarks.

This establishes the finite heavy-VLL contribution in the **restricted scalar-potential subsector**. It does not complete the full dimension-eight hard/soft Wilson vector or the remaining higher-dimensional EFT soft/source sectors.

The PR #69 validation workflow [run 42582889232](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42582889232) passes 18 tests, including the independent EFT5 contact/O8 and Plan-C scale checks. The exact calculation report and regenerated benchmark JSON are linked from the PR description.

**Status update:** the prior RC-001 statement that the finite dimension-eight hard matching was wholly outstanding is refined for this one scalar-potential subsector: the heavy-VLL Coleman--Weinberg \(O_8\) contribution is now available as an independently validated subcalculation. The complete dimension-eight hard/soft matching, derivative-operator/EOM/source completion, remaining gauge/scalar sectors, independent diagram-level validation, and model-level Wilson-vector closure remain open.

## 11. Change history

| Date | Revision | Change | Reason |
|---|---|---|---|
| 2026-10-23 | RC-001 initial record | Consolidated the v153 source baseline, analytical subresults, Mathematica/Python evidence, unrun FeynArts/FeynCalc scaffold, and claim status | Establish the first end-to-end Scientific Diff record without overstating the completed calculation |
| 2026-10-23 | Review revision 1 | Separated the RC-001 claim matrix; recorded the B1/B3 candidate-kernel discrepancy, historical v76→v77 audit provenance, and §274 downstream dependency | Resolve evidence-traceability issues without changing physical coefficients or overstating validation |
| 2026-10-23 | Follow-up calculation | Added the explicit UV–EFT h–s subtraction and its exact symbolic checks as a provisional supplement; kept counterterm and §274 convention reconciliation open | Record the new calculation without promoting it to a fully verified physical result |
| 2026-10-23 | Kernel/counterterm reconciliation | Reconstructed the exact mass-basis C,D matrices; made the signed-mass identity explicit; corrected the leading hard-self-energy sign; derived the bubble-plus-contact UV pole and the dimension-six derivative counterterm; recorded the historical 4/3 difference between representatives and reconciled it via off-shell/EOM completion | Align the new difference with §§274–285 without promoting the finite derivative coefficient or the full EFT basis to verified |
| 2026-10-23 | Off-shell/EOM reproducibility | Added the source-aligned §252 reproduction (46 exact-rational checks) and §301 coefficient audit (5 checks), with captured output logs | Make the finite representative reconciliation and its companion-term bookkeeping directly reproducible from the repository |
| 2026-10-23 | EFT soft-insertion power counting | Recorded the (Q_{LD},Q_{RD}) tree-level (1/M_E^2) operators and showed their VEV wavefunction insertions into the (C_5^2) bubble begin at (O(M_E^{-4})) | Bound the restricted Yukawa-sector conclusion without claiming that all portal/gauge/scalar soft topologies are closed |
| 2026-10-23 | Dimension-eight soft-pole reconciliation | Matched the C5-squared constant soft pole to the X^2Y^2 counterterm in master §§262.5 and 264.4; kept full dimension-eight hard matching open | Distinguish the verified subset-level potential counterterm from the complete O(M_E^-4) Wilson vector |
| 2026-10-23 | EFT soft-topology census | Expanded the structural ledger to 26 scalar, fermionic, current/source, and dimension-eight topology families; added crossed C5-squared fermionic channels and same-order Q6-plus-quartic/gauge soft corrections | Prioritize explicit integrals without overstating model-level Wilson-vector closure |
| 2026-10-23 | Dimension-six soft-loop cross-check | Added Feynman-parameter Gamma-function checks, crossed-current hard/soft pole cancellation, four-fermion hard/soft cancellation, and the Q6-plus-quartic EOM kernel; saved 41 exact symbolic checks | Advance the dimension-six soft calculation while keeping gauge-sector and model-level closure open |
| 2026-10-23 | Independent dimension-six kernel check | Added and locally ran a separate compact SymPy script with 23 exact checks, then extended the workflow to compare both outputs | Independently recheck selected stripped kernels and tensor identities without confusing local checks with CI |
| 2026-10-23 | Dimension-six gauge attachment census | Added charge-aware (Q_{LD}/Q_{RD}) attachment-class atlas, a reproducible generator/output, and an amplitude-by-amplitude UV–EFT subtraction ledger | Enumerate gauge sectors and contact classes without claiming uncomputed loop coefficients or diagram-generator validation |
| 2026-10-23 | Gauge subgraph integral and kinetic-mixing subrecord | Evaluated the Feynman-gauge heavy-line self-energy subgraph and representative scalar master-integral UV/IR split; recorded the additive (B-A') pole cancellation and finite heavy threshold; added CL-010/CL-011 and a workflow-compliant open subrecord | Preserve the evaluated sub-blocks and explicitly scope them short of complete vertex/box amplitudes, a closed Wilson vector, and independent diagram-level validation |
| 2026-10-23 | Conjugate Yukawa-vertex charge-factor reduction | Derived and locally checked signed hypercharge, X-charge, and mixed BA' factors for the three line pairs at each y, y*, lambda, and lambda* vertex; added CL-012 and linked the factors into the UV-EFT ledger | Fix charge multipliers before explicit vertex integration without claiming full amplitudes or Wilson coefficients |
| 2026-10-23 | Light-only Yukawa-vertex hard cancellation | Expanded the chirality-preserving heavy propagator through (O(M_E^{-2})) and showed the common purely light loop factor cancels against the gauge-covariant EFT insertion when contact terms and the same IR prescription are included; added CL-013 and a symbolic check | Remove duplicated soft-only terms from the hard-coefficient worklist while retaining them in Ward/contact bookkeeping |
| 2026-10-23 | Conditional mixed input-parameter poles | Derived the first-order B-A' parameter-only pole sub-block using the signed off-diagonal propagator coefficient rho_BX=-chi+O(chi^2); added CL-014 and an exact charge-algebra check | Keep mixed kinetic renormalization separate from diagonal results and from the still-open mixed vertex/box matching |
| 2026-10-23 | Heavy-line Yukawa-vertex hard sub-blocks | Evaluated the FF and FS vertex kernels with oriented signs for both conjugate (y) and (lambda) vertices; retained the (O(epsilon)	imes 1/epsilon) term in (dB_0); added CL-015 and exact symbolic checks | Preserve vertex-only poles and finite constants as a sub-block; do not claim complete Wilson coefficients before crossed boxes, EFT contacts, and counterterms are combined |
| 2026-10-23 | Artifact bundle provenance | Added the immutable v66 (2026-10-19) working-tree snapshot with a 138-file inventory and normalized relocation metadata; preserved the v153 baseline and claim statuses | Give the earlier generation's supporting sources and outputs a repository-addressable location without implying that archive integrity establishes physical validation |
| 2026-11-13 | PR #69 Benchmark A/B cross-reconciliation | Added the bounded §10.14 benchmark cross-check, Plan-C contact bookkeeping, and heavy-VLL CW scalar-potential result; updated CL-007 and the counterterm ledger | Preserve the independent cross-check while keeping the complete Wilson vector and model-level matching open |
