# RC-001 — EFT soft-topology census and heavy-mass power counting

**Status:** expanded structural census across scalar, two-fermion/two-scalar, four-fermion, current/source, and dimension-eight candidate families. Analytic hard/soft kernels are now checked for the crossed-current, four-fermion, and Q6-plus-quartic sectors; the full fermionic gauge-correction set, EOM/source closure, external diagram-package validation, and model-level Wilson-vector closure remain open. Master v153 §§254–255 already contain separate bosonic field-strength/current-to-gauge and external-field/source calculations.

**Baseline:** PR #4 head before this addition, 1fa84601b95b79d325877a11651393dc2d58269f; frozen primary source v153, especially §§243.2–243.5, 244, 252.3–252.10, 283–285, and 301.1–301.4.

## 1. Scope and conventions

The matching problem integrates out the heavy vector-like lepton \(E_\ell\) while retaining \(H\), \(S\), the light leptons, and \(A'\) in the EFT. The unbroken-phase matching convention is used for the Wilson expansion; light masses are set to zero unless a broken-phase projection is explicitly identified. Dimensional regularization and one common \(\overline{\mathrm{MS}}\) prescription are assumed on the UV and EFT sides.

The tree-level heavy-fermion expansion contains
\[
C_{5,\ell}\sim \frac{y_\ell\lambda_\ell}{M_{E_\ell}},\qquad
C_{LD,\ell}\sim\frac{|y_\ell|^2}{M_{E_\ell}^2},\qquad
C_{RD,\ell}\sim\frac{|\lambda_\ell|^2}{M_{E_\ell}^2},
\]
where \(Q_{LD}\) and \(Q_{RD}\) are the unreduced dimension-six derivative operators defined in master §243.2. The full scalar potential retains \(\lambda_H,\lambda_S,\lambda_{HS}\). The \(A'\) field remains in the EFT; the \(U(1)_X\)-hypercharge kinetic-mixing boundary is not fixed by the current baseline.

For a connected graph, the topological loop count is \(L=I-V+1\). A self-contracted fermion tadpole counts as an internal line. A graph's loop count, 1PI status, explicit \(1/M_E\) power, and contribution to the chosen coefficient are separate questions.

## 2. Topology ledger

The companion script calculations/RC-001-eft-soft-topology-census.py checks 26 candidate topology families, their Euler loop counts, and explicit heavy-mass powers. It is a structural audit, not an integral evaluator or an automatic Feynman-diagram generator.

| ID | Candidate EFT topology | Loops | Explicit heavy-mass order | 1PI w.r.t. stated external amplitude? | Power-counting decision / scope |
|---|---|---:|---:|---|---|
| SFT-01 | \(C_5 C_5^\ast\) light-fermion bubble with \(H,S,H^\dagger,S^\dagger\) external legs | 1 | \(M_E^{-2}\) | Yes | **Keep.** This is the direct mixed-scalar soft graph in the fixed \(|y_\ell|^2|\lambda_\ell|^2\) sector. Its PV expression is already recorded; independent diagram-level validation remains open. |
| SFT-02 | One \(Q_{LD}\) insertion plus a scalar quartic, with one fermion tadpole and one scalar line | 1 | \(M_E^{-2}\) | No | **Do not add to the local 1PI four-scalar coefficient.** In the unbroken massless theory the fermion tadpole is scaleless and vanishes in dimensional regularization. |
| SFT-03 | One \(Q_{RD}\) insertion plus a scalar quartic, with one fermion tadpole and one scalar line | 1 | \(M_E^{-2}\) | No | Same conclusion as SFT-02. Broken-phase mass-dependent pieces must be re-counted and are not automatically \(O(M_E^{-2})\). |
| SFT-04 | \(Q_{LD}Q_{LD}\) fermion loop in the pure-Higgs four-scalar channel | 1 | \(M_E^{-4}\) | Yes | Exclude from dimension six; retain for the dimension-eight audit. |
| SFT-05 | \(Q_{RD}Q_{RD}\) fermion loop in the pure-singlet four-scalar channel | 1 | \(M_E^{-4}\) | Yes | Exclude from dimension six; retain for the dimension-eight audit. |
| SFT-06 | \(Q_{LD}Q_{RD}\) candidate in the mixed four-scalar channel | — | — | No | **Remove from the direct one-loop soft list.** \(Q_{LD}\) contains only an \(L_\ell\) bilinear and \(Q_{RD}\) only an \(\ell_R\) bilinear; the unbroken massless EFT has no \(L_\ell\)-\(\ell_R\) propagator. Two insertions cannot form one connected fermion loop. Any mixed contribution requires extra chirality-changing insertions and a fresh loop/order count. |
| SFT-07 | \(Q_{LD}\) current form factor connected to an external \(S^\dagger S A'\) vertex | 1 | \(g_X^2|y_\ell|^2/M_E^2\) | No, due to the exchanged \(A'\) line | Track in the current/source sector. Do not count it as a direct local 1PI coefficient of \(\partial(H^\dagger H)\partial(S^\dagger S)\). |
| SFT-08 | \(Q_{RD}\) current form factor connected to an external \(H^\dagger H B_\mu\) vertex | 1 | \(g_Y^2|\lambda_\ell|^2/M_E^2\) | No, due to the exchanged \(B\) line | Track in the current/source sector and in connected-amplitude matching; do not misidentify the reducible exchange as a local 1PI scalar vertex. |
| SFT-09 | \(Q_{LD}\) current form factor connected to an external \(H^\dagger H B_\mu/W_\mu\) vertex | 1 | \(g_{\rm SM}^2|y_\ell|^2/M_E^2\) | No, due to the exchanged gauge line | Track for the pure-Higgs current/source amplitudes if the corresponding Wilson vector is claimed complete. |
| SFT-10 | \(Q_{RD}\) current form factor connected to an external \(S^\dagger S A'\) vertex | 1 | \(g_X^2|\lambda_\ell|^2/M_E^2\) | No, due to the exchanged \(A'\) line | Track for the pure-singlet current/source amplitudes if the corresponding Wilson vector is claimed complete. |
| SFT-11 | Four \(C_5\) insertions in an eight-scalar light-fermion loop | 1 | \(M_E^{-4}\) | Yes | Retain for the dimension-eight \(X^2Y^2\) potential sector. The broken-phase \(C_5^2\) constant self-energy projection is a VEV projection of this operator structure, not an extra graph to add a second time. |
| SFT-12 | \(C_5 C_7^\ast\) light-fermion loop, if a dimension-seven representative survives EOM reduction | 1 | \(M_E^{-4}\) | Yes | Conditional dimension-eight contribution. First derive and reduce the \(1/M_E^3\) tree-level operator; if it is redundant, preserve its EOM-induced source/potential companions. |
| SFT-13 | \(C_5 C_5^\ast\) bubble with a \(Q_{LD}\) or \(Q_{RD}\) VEV wavefunction insertion | 1 | \(M_E^{-4}\) at fixed \(v_h,v_s\) | Yes | Exclude from strict dimension six; retain in a complete broken-phase \(O(M_E^{-4})\) calculation. This agrees with the explicit \(\delta Z_{L,R}\) counting in §243.4. |
| SFT-14 | \(C_5 C_5^\ast\) crossed loop in \(\bar L L H^\dagger H\), with internal \(\ell_R\) and \(S\) | 1 | \(M_E^{-2}\) | Yes | Keep for the complete dimension-six fermion-operator vector; one internal fermion and one scalar propagator form a 1PI loop. |
| SFT-15 | \(C_5 C_5^\ast\) crossed loop in \(\bar L L S^\dagger S\), with internal \(\ell_R\) and \(H\) | 1 | \(M_E^{-2}\) | Yes | Keep for the complete dimension-six fermion-operator vector; one internal fermion and one scalar propagator form a 1PI loop. |
| SFT-16 | \(C_5 C_5^\ast\) crossed loop in \(\bar\ell_R\ell_R H^\dagger H\), with internal \(L\) and \(S\) | 1 | \(M_E^{-2}\) | Yes | Keep for the complete dimension-six fermion-operator vector; one internal fermion and one scalar propagator form a 1PI loop. |
| SFT-17 | \(C_5 C_5^\ast\) crossed loop in \(\bar\ell_R\ell_R S^\dagger S\), with internal \(L\) and \(H\) | 1 | \(M_E^{-2}\) | Yes | Keep for the complete dimension-six fermion-operator vector; one internal fermion and one scalar propagator form a 1PI loop. |
| SFT-18 | \(C_5 C_5^\ast\) scalar loop in the \(\bar L L\,\bar\ell_R\ell_R\) four-fermion channel, with internal \(H,S\) | 1 | \(M_E^{-2}\) | Yes | Keep for the complete dimension-six four-fermion vector; the two scalar propagators form a 1PI bubble. |
| SFT-19 | \(Q_{LD}\) plus \(\lambda_H\) scalar bubble in \(\bar L L H^\dagger H\) | 1 | \(M_E^{-2}\) | Yes | Keep for the full dimension-six fermion-operator vector; two scalar propagators give a non-scaleless bubble. |
| SFT-20 | \(Q_{LD}\) plus \(\lambda_{HS}\) scalar bubble in \(\bar L L S^\dagger S\) | 1 | \(M_E^{-2}\) | Yes | Keep for the full dimension-six fermion-operator vector; order \(\lambda_{HS}|y|^2/M_E^2\). |
| SFT-21 | \(Q_{RD}\) plus \(\lambda_S\) scalar bubble in \(\bar\ell_R\ell_R S^\dagger S\) | 1 | \(M_E^{-2}\) | Yes | Keep for the full dimension-six fermion-operator vector; two scalar propagators give a non-scaleless bubble. |
| SFT-22 | \(Q_{RD}\) plus \(\lambda_{HS}\) scalar bubble in \(\bar\ell_R\ell_R H^\dagger H\) | 1 | \(M_E^{-2}\) | Yes | Keep for the full dimension-six fermion-operator vector; order \(\lambda_{HS}|\lambda|^2/M_E^2\). |
| SFT-23 | \(C_5\) plus \(\lambda_{HS}\) scalar bubble in the \(\bar L\ell_R H S\) amplitude | 1 | \(M_E^{-1}\) | Yes | Required only if claiming one-loop closure of \(C_5\); not needed for the one-loop dimension-six scalar coefficient. |
| SFT-24 | \(C_5\) insertion with one-loop gauge corrections in the \(\bar L\ell_R H S\) amplitude | 1 | \(M_E^{-1}\) | Yes | Required for one-loop \(C_5\) closure; include gauge vertex, leg, and covariant-derivative contact graphs as a gauge-invariant set. |
| SFT-25 | \(Q_{LD}\) insertion with gauge-loop corrections in \(\bar L L H^\dagger H\) | 1 | \(M_E^{-2}\) | Yes | Required for the complete one-loop \(Q_{LD}\) coefficient; include gauge vertex, leg, contact, and counterterm contributions. |
| SFT-26 | \(Q_{RD}\) insertion with gauge-loop corrections in \(\bar\ell_R\ell_R S^\dagger S\) | 1 | \(M_E^{-2}\) | Yes | Required for the complete one-loop \(Q_{RD}\) coefficient; include gauge vertex, leg, contact, and counterterm contributions. |

The table separates direct scalar 1PI graphs, fermionic external-state graphs, reducible current-exchange graphs, and dimension-eight candidates. Reducible current-exchange graphs must not be silently dropped from a full connected amplitude or current-operator analysis, but they are not extra local 1PI contributions to the scalar derivative coefficient. Whether their form factors are needed explicitly depends on the chosen matching object and whether gauge-current operators are retained or eliminated with gauge-field EOM.

## 3. What is actually required at \(O(M_E^{-2})\)?

### 3.1 Fixed mixed Yukawa sector \(|y_\ell|^2|\lambda_\ell|^2\)

For the marked unbroken-phase external legs \(H,S,H^\dagger,S^\dagger\), the two conjugate \(C_5\) insertions provide all four scalar legs and close through two light-fermion propagators. This is one 1PI loop channel per flavor. The \(\mu\) and \(\tau\) assignments differ in the complex-singlet orientation, so the bubble momentum is \(s\) for \(\mu\) and \(u\) for \(\tau\); they must not be merged before the flavor-resolved projection.

In this coupling sector, the existing master calculation and the later off-shell/EOM completion in §§252 and 301 cover the stated \(C_5C_5^\ast\) soft subtraction. The \(\frac43\) historical difference is resolved for that specified Yukawa-box sector by the off-shell/EOM completion; this does not close the other model sectors or substitute for an independent diagram-package calculation.

### 3.2 Scalar-quartic candidates in four-scalar amplitudes

For a four-scalar external state, one \(Q_{LD}\) or \(Q_{RD}\) insertion plus a scalar-quartic vertex can leave one fermion tadpole and one scalar propagator. The graph is one-loop by \(L=I-V+1\), but is reducible through the scalar line. In the unbroken massless theory the fermion tadpole is scaleless and vanishes in dimensional regularization.

This excludes that candidate from the local scalar 1PI coefficient at strict \(O(M_E^{-2})\). It does **not** delete \(Q_{LD}\), \(Q_{RD}\), the scalar portal, or their EOM consequences from the EFT. If light masses, VEV insertions, a different IR regulator, or a different matching object are retained, the integral and its power counting must be reconsidered under that stated scheme.

### 3.3 Other one-loop soft graphs in fermionic external-state amplitudes

The full dimension-six Wilson vector also requires external-state families beyond the scalar four-point function:

- **Two fermions plus two scalars from \(C_5C_5^\ast\):** four crossed channels are possible: \(\bar L L H^\dagger H\), \(\bar L L S^\dagger S\), \(\bar\ell_R\ell_R H^\dagger H\), and \(\bar\ell_R\ell_R S^\dagger S\). Each has one internal fermion and one internal scalar propagator, so \(L=1\), the product is \(O(M_E^{-2})\), and the topology is 1PI. Their hard/soft vector kernels are now analytically reduced; the three loop-dependent hard regions and the soft-only \(\bar L L H^\dagger H\) channel are distinguished in §3.5.
- **Four fermions from \(C_5C_5^\ast\):** the external \(\bar L,L,\bar\ell_R,\ell_R\) legs are supplied by the two insertions and the internal \(H,S\) scalar propagators form a one-loop 1PI bubble. Its hard/soft scalar-bilinear kernel is now analytically reduced; the final basis conversion and external diagram-level sign check remain open.
- **One \(Q_6\) insertion plus a scalar-quartic bubble:** \(Q_{LD}+\lambda_H\) contributes to \(\bar L L H^\dagger H\), \(Q_{LD}+\lambda_{HS}\) to \(\bar L L S^\dagger S\), \(Q_{RD}+\lambda_S\) to \(\bar\ell_R\ell_R S^\dagger S\), and \(Q_{RD}+\lambda_{HS}\) to \(\bar\ell_R\ell_R H^\dagger H\). Their universal hard/soft kernel is analytically reduced and is proportional to a fermion-EOM momentum polynomial. For the model's \(\mu,\tau\) fields, the renormalizable EOM sources vanish (master §255.8), so these insertions do not induce nonzero dimension-six Yukawa-source rows at this order; the \(\lambda_H\) weak-index projection still must be recorded consistently.
- **Remaining fermionic gauge corrections:** one-loop vertex, heavy/light external-leg, and covariant-derivative contact contributions to \(Q_{LD}/Q_{RD}\) and the fermion-current operators at \(O(g^2/M_E^2)\) remain open, including counterterms and the declared external-field scheme. This is distinct from the bosonic field-strength/current-to-gauge matching already recorded in master §254.
- **One-loop corrections to \(C_5\):** \(C_5+\lambda_{HS}\) scalar bubbles and gauge corrections enter the \(\bar L\ell_R H S\) amplitude at \(O(M_E^{-1})\). They are not needed to obtain the one-loop dimension-six scalar coefficient from a tree-level \(C_5C_5^\ast\) insertion, because inserting a one-loop-corrected \(C_5\) there would be a two-loop effect. They are required if the claim is expanded to the full one-loop dimension-five Wilson coefficient.

These fermionic external-state graphs are not optional if the claim is a complete dimension-six Wilson vector. The analytic kernels for the listed crossed and quartic channels are recorded in §3.5, but the structural script does not generate diagrams, and the full gauge, counterterm, and common-basis operator projection is not yet closed.

### 3.4 Current exchange is a separate matching problem

A \(Q_{LD}\) or \(Q_{RD}\) insertion can enter a one-loop current form factor, with a gauge propagator connecting that form factor to an external scalar current. Gauge-covariant contact vertices from the covariant derivatives must be included in the same gauge-invariant set; a scaleless contact tadpole may vanish, but that is not grounds to omit the remaining vertex graphs. Examples are \(Q_{LD}\)-\(A'\)-\(S^\dagger S\), \(Q_{RD}\)-\(B\)-\(H^\dagger H\), \(Q_{LD}\)-\(B/W\)-\(H^\dagger H\), and \(Q_{RD}\)-\(A'\)-\(S^\dagger S\). These graphs carry one \(1/M_E^2\) Wilson coefficient and one loop, but are reducible through the exchanged gauge propagator in the four-scalar amplitude.

Therefore:
- Do not add these graphs as direct local 1PI contributions to \(C_{\partial HS}\).
- Do not claim the full connected amplitude or full current/source Wilson vector is closed while the corresponding current form factors and their UV counterparts remain untracked.
- If a basis change uses gauge-field EOM, record the induced operator shifts once, with the same gauge-current conventions on both sides.
- The kinetic-mixing boundary is not fixed in the baseline. Crossed \(B\)-\(A'\) current contributions are conditional on that input and must not be silently set to zero in a full-model claim.

### 3.5 Analytic integral results and matching boundary

The independent note research/RC-001-dim6-soft-loop-integrals-and-checks.md records the stripped integrals, momentum routings, hard/soft decompositions, and operator projections. The script calculations/RC-001-dim6-soft-loop-crosscheck.py passes 41 exact symbolic checks, with output saved in validation/RC-001-dim6-soft-loop-crosscheck.txt.

The results sharpen the ledger as follows:

- The \(C_5C_5^\ast\) crossed channels \(\bar L L S^\dagger S\), \(\bar\ell_R\ell_R H^\dagger H\), and \(\bar\ell_R\ell_R S^\dagger S\) have loop-dependent heavy propagators and a nonzero hard region. Their routed hard vector kernel has the local coefficient \(\tfrac12L_E-\tfrac34\); the \(O(\epsilon)\) term in \(1-2/d\) is required to recover the finite \(-3/4\). The \(\bar\ell_R\ell_R S^\dagger S\) channel has an internal doublet multiplicity of two.
- In the \(\bar L L H^\dagger H\) channel, both heavy propagators carry only external-channel momenta in the stated bare topology. Its \(O(M_E^{-2})\) loop is reproduced by the EFT soft integral; the associated current counterterms and operator renormalization must still be matched.
- The \(C_5C_5^\ast\) four-fermion scalar bubble has hard coefficient \(|C_5|^2(L_E-2)/(16\pi^2)\) in the scalar-bilinear basis. Its hard IR pole cancels the EFT bubble UV pole, and the finite constants \(-2,+2\) cancel in the summed amplitude.
- A single \(Q_{LD}\) or \(Q_{RD}\) insertion plus a scalar quartic gives a hard/soft kernel proportional to \(p+Q/2=(p-p')/2\). This is an EOM/source structure for massless on-shell external fermions, not an independent on-shell current coefficient. The \(\lambda_H\) weak-index contractions must remain separate until the singlet/triplet and source projection.
- These checks are analytic integral and tensor-reduction checks, not FeynArts/FeynCalc diagram generation. The full gauge-corrected current/operator matching and the complete EOM/source coefficient vector remain open.

## 4. Pure-light graphs and cancellation rule

Pure scalar or gauge loops with no heavy-dependent EFT insertion carry \(M_E^0\). When the same light fields, parameters, IR regulator, gauge convention, and external-state normalization are used on both sides, they are reproduced by the EFT and cancel in the UV-minus-EFT Wilson matching difference. They can still enter a physical amplitude or RG calculation. If \(A'\) is also integrated out, or the kinetic-mixing or portal boundary differs between the two theories, the cancellation list must be rebuilt.

## 5. EOM and source-term closure is not another loop topology

The derivative coefficients in the chosen redundant basis induce companion terms when \(R_H,R_S,T_H,T_S\) are reduced with IBP/EOM. At \(O(M_E^{-2})\), these include shifts to the derivative basis, scalar-potential rows such as \(X^2,Y^2,XY,X^3,Y^3,X^2Y,XY^2\), and the corresponding fermion-source rows. These terms are part of the Wilson-vector bookkeeping even though they are not new loop integrals.

The v153 §252.8–§252.10 ledger already provides the source/potential mapping for the specified Yukawa-derived derivative coefficients. Apply the updated mapping exactly once; do not retain both the old on-shell representative and the new off-shell/EOM completion. The same ledger explicitly states that its pure-scalar/source projection is not a full independent matching of all fermion-current, bilinear, or four-fermion amplitudes.

Source power counting must remain explicit:
- Multiplying a dimension-six coefficient by the renormalizable dimension-four source gives the \(O(M_E^{-2})\) companion rows.
- Terms involving the dimension-five source \(C_5\) begin at \(O(M_E^{-3})\).
- Source-square terms proportional to \(C_5C_5^\ast\) begin at \(O(M_E^{-4})\).
- Thus \(C_5\)-dependent source terms are excluded from a strict dimension-six truncation but return in the dimension-eight closure.

## 6. Required \(O(M_E^{-4})\) dimension-eight census

A complete dimension-eight claim must separately include, without double counting:

1. The unbroken-phase \(C_5^4\) eight-scalar soft loop for the \(X^2Y^2\) potential operator.
2. The broken-phase constant \(h\)-\(s\) projection of the \(C_5^2\) bubble/contact subset as a cross-check of that same potential structure, not as an independent duplicate.
3. The \(Q_{LD}Q_{LD}\) and \(Q_{RD}Q_{RD}\) soft loops in the pure-Higgs and pure-singlet channels. The putative \(Q_{LD}Q_{RD}\) one-loop mixed channel is absent in the unbroken massless EFT because the two insertions contain distinct, chirality-preserving fermion species; see research/RC-001-dimension8-tree-eom-and-soft-integrals.md.
4. \(C_5C_7^\ast\) soft insertions if the \(1/M_E^3\) operator survives the declared EOM reduction, or the corresponding induced source/potential terms if it is eliminated.
5. \(Q_{LD}/Q_{RD}\) VEV wavefunction insertions into the \(C_5C_5^\ast\) bubble and any other \(O(M_E^{-4})\) tree-level EFT insertion required by the fixed amplitude.
6. The corresponding dimension-eight UV hard expansion, counterterms, and EOM/source companions.

The existing four-check \(C_5^2\) constant-pole audit verifies only the stated soft-potential subset counterterm. It does not close the items above or the full dimension-eight hard Wilson vector.

## 7. Decision and next calculation order

**Power-counting decision:** at strict \(O(M_E^{-2})\), keep the \(C_5C_5^\ast\) mixed scalar bubble as the direct 1PI soft subtraction in the fixed \(|y|^2|\lambda|^2\) sector; do not add \(Q_{LD}/Q_{RD}\)-plus-quartic tadpoles to that local 1PI coefficient; keep gauge-current exchange graphs in the separate current/source ledger; and do not import \(Q_6Q_6\), \(C_5C_7^\ast\), or \(C_5^4\) terms into the dimension-six result.

**Explicit-integral priority:**
1. Independently generate/check the UV diagrams for the crossed-current and four-fermion kernels with FeynArts/FeynCalc or an equivalent diagram-level tool; confirm field-flow signs, weak-index factors, and the displayed finite coefficients.
2. Complete the gauge corrections to \(Q_{LD}\), \(Q_{RD}\), and the current operators, including gauge-boson attachments to the heavy line, external legs, covariant-derivative contact terms, and counterterms.
3. Complete the \(\lambda_H,\lambda_S,\lambda_{HS}\) weak-index projections and the EOM/source mapping, including external-field and parameter renormalization. State the kinetic-mixing boundary and input scheme.
4. Re-run the structural and analytic checks locally when relevant files change, comparing outputs with the checked-in records. CI is explicitly skipped as an unavailable infrastructure check and is not a closure gate for this iteration. Keep PR #4 open until the missing UV–EFT gauge amplitudes and independent diagram-level evidence are resolved.
5. Only after the dimension-six gauge/source closure, start the \(O(M_E^{-4})\) dimension-eight hard/soft calculation using the list in §6.

No loop integral is evaluated by the companion census script. No FeynCalc, Mathematica, FeynArts, Matchete, or Matchmakereft execution is claimed. PR #4 remains Draft/Open; no merge is authorized by this topology census.


## 8. Dimension-six gauge attachment atlas and subtraction ledger

The next gauge-correction phase now has two linked records:

- `research/RC-001-dim6-gauge-diagram-atlas.md`: charge-compatible one-gauge-boson attachment classes for the \(\bar L L H^\dagger H\) and \(\bar\ell_R\ell_R S^\ast S\) tree-exchange amplitudes, including external-leg self-energies, heavy-line attachments, vertex/box classes, mixed \(B-A'\) charge factors, and EFT derivative-contact vertices.
- `research/RC-001-dim6-uv-eft-subtraction-ledger.md`: UV/EFT subtraction, pole/finite-part, counterterm, Ward-identity, common-basis, current/source and kinetic-mixing ledger.

The local charge-aware census verifies, for each flavor, the attachment-class counts
\[
Q_{LD}: (BB,WW,A'A',BA')=(10,6,3,9),\qquad
Q_{RD}: (BB,WW,A'A',BA')=(3,0,10,7).
\]
These are unordered line-pair classes, not a generated count of individual Feynman diagrams. In particular, the \(Q_{LD}/Q_{RD}\) derivative contact vertices have \(B\) and \(A'\) components but no direct \(W\) component because the differentiated composites are \(SU(2)_L\) singlets.

No \(O(g^2/M_E^2)\) gauge-loop integral or finite Wilson coefficient has yet been evaluated. The runtime availability record `validation/RC-001-dim6-diagram-tool-availability.txt` confirms that the current execution environment lacks Mathematica/Wolfram, FeynCalc, FeynArts, pyfeyn and QGRAF; therefore independent diagram-level validation remains open. GitHub Actions was attempted but the runner never started; per the explicit project decision, CI is skipped and is not a closure gate. This does not count as a CI pass, and does not alter the remaining physics-validation requirements.

The existing analytic \(C_5C_5^\ast\) soft kernels and master §§252–255 bosonic/source blocks remain separate evidence modules. Do not double-count them when the gauge-corrected fermionic derivative/current sector is eventually summed. PR #4 remains Draft/Open.
