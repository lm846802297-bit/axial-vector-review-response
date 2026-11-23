# RC-001 — Dimension-six gauge matching: UV–EFT subtraction and common-basis ledger

**Status:** matching protocol and per-amplitude evidence ledger established. Selected \(Q_{LD}\) pure-\(WW\) sub-blocks now have nonexceptional hard/soft results: cross-vertex classes 01/02/05/06 have a finite local hard polynomial and pole closure, while same-vertex classes 03/04 are pure-soft and give zero hard-minus-EFT contribution at \(O(M_E^{-2})\). The EFT local one-\(W\) contacts implied by this fixed hard polynomial now have an exact SU(2) covariance audit (research/RC-001-dim6-WW-fivepoint-EFT-ward.md). The UV external-\(W\) five-point form factor, complete counterterm sum, and common-basis Wilson vector remain open; no complete finite gauge-correction Wilson coefficient is claimed. Existing bosonic coefficients from master §254 and previously checked scalar/soft kernels are not duplicated.

## 1. Common conventions

Use \(d=4-2\epsilon\), one common \(\overline{\mathrm{MS}}\) convention, and
\[
\Delta_{\rm UV,IR}=\frac1{\epsilon_{\rm UV,IR}}-\gamma_E+\ln4\pi,\quad
L_\ell=\ln\frac{M_{E_\ell}^2}{\mu_R^2},\quad
\ell_q=\ln\frac{-q^2-i0}{\mu_R^2}.
\]
Use the same nonexceptional off-shell external momenta (or one explicitly shared infrared regulator) in the UV and EFT calculations. Do not set all external momenta and light masses to zero before separating UV and IR poles. Keep the same gauge-fixing parameter, external-leg amputation/LSZ convention, and input scheme for \(y_\ell,\lambda_\ell,M_{E_\ell},g_Y,g_2,g_X\), and kinetic mixing.

For each amplitude,
\[
\Gamma_{\rm UV}^{(1)}=
\Gamma_{\rm hard}^{(1)}+\Gamma_{\rm soft}^{(1)},\qquad
\Gamma_{\rm EFT}^{(1)}=\Gamma_{\rm soft}^{(1)}
\]
only after all EFT insertions, external-field terms, parameter counterterms, and contact vertices required by that amplitude are included. The local matching difference is the hard part,
\[
\Delta\Gamma_{\rm hard}^{(1)}
=\Big[\Gamma_{\rm UV}^{(1)}-\Gamma_{\rm EFT}^{(1)}\Big]_
{\text{same IR prescription, same external state}}.
\]
Expand the difference to the required external-momentum order and \(M_E^{-2}\), then project onto the declared operator basis. A pole cancellation at the level of a stripped subgraph is necessary but not sufficient for a Wilson coefficient.

## 2. Required amplitude ledger

Each row is to be populated with explicit UV graphs, EFT graphs, UV and IR poles, finite local terms, counterterms, and basis projection. The status column is deliberately explicit: **NOT EVALUATED** means no loop coefficient has been invented.

| ID | Amplitude / coupling sector | UV contribution to compute | EFT subtraction to compute | Counterterm / projection requirement | Status |
|---|---|---|---|---|---|
| LD-B (atlas LD-B-01…10) | \(\bar L L H^\dagger H\), \(y_\ell^2 g_Y^2/M_E^2\) | All \(BB\) attachment classes in gauge atlas §3, heavy-line insertions, vertex/box graphs | \(Q_{LD}\) insertion with \(B\) exchange and its \(B\)-contact graphs; external legs | \(\delta y,\delta M_E,\delta g_Y,\delta Z_L,\delta Z_H,\delta C_{LD}\); singlet projection | NOT EVALUATED |
| LD-W (atlas LD-W-01…06) | Same amplitude, \(y_\ell^2 g_2^2/M_E^2\) | Cross pairs 01/02/05/06: nonexceptional hard/soft pole closure and finite hard polynomial recorded; same-vertex pairs 03/04: pure-soft UV/EFT identity, zero hard matching contribution | Tree \(Q_{LD}\) singlet insertion has no direct \(W\) contact; matched triplet redundant-basis representatives have explicit EFT contacts and an exact local covariance audit in research/RC-001-dim6-WW-fivepoint-EFT-ward.md | Keep singlet/triplet tensors; include the second external-field routing, \(\delta Z_L,\delta Z_H,\delta g_2,\delta C_{LD}\), UV external-\(W\) five-point form factor, and full Ward/Slavnov-Taylor sum | **PARTIAL** — internal-\(W\) sub-block and EFT local contacts checked; UV five-point and full LD-W matching remain open |
| LD-X (atlas LD-X-01…03) | Same amplitude, \(y_\ell^2 g_X^2/M_E^2\) | \(A'A'\) pairs among \(E,\bar L,L\), heavy self-energy and vertex corrections | \(Q_{LD}\) insertion with \(A'\) exchange and \(A'\)-contact graphs | \(\delta g_X,\delta Z_L,\delta M_E,\delta C_{LD}\); flavor-resolved \(\eta_\ell\) factors | NOT EVALUATED |
| LD-BX (atlas LD-BX-01…09) | Same amplitude with mixed propagator | Every nonzero signed \(BA'\) pair from atlas §3; use the full kinetic matrix | EFT mixed-propagator exchange and contact graphs | Fix \(\chi(\mu_R)\)/threshold scheme; mixed charge factor \(Y_i x_j+x_iY_j\) | CONDITIONAL / NOT EVALUATED |
| RD-B (atlas RD-B-01…03) | \(\bar\ell_R\ell_R S_\ell^\ast S_\ell\), \(|\lambda_\ell|^2 g_Y^2/M_E^2\) | Three \(BB\) pair classes and heavy-line/vertex corrections | \(Q_{RD}\) insertion with \(B\) exchange and \(B\)-contact graphs | \(\delta\lambda,\delta M_E,\delta g_Y,\delta Z_{\ell_R},\delta Z_S,\delta C_{RD}\) | NOT EVALUATED |
| RD-X (atlas RD-X-01…10) | Same amplitude, \(|\lambda_\ell|^2 g_X^2/M_E^2\) | All ten \(A'A'\) pair classes, heavy and scalar lines, vertex/box graphs | \(Q_{RD}\) insertion with \(A'\) exchange and contact graphs | \(\delta g_X,\delta Z_{\ell_R},\delta Z_S,\delta M_E,\delta C_{RD}\); retain \(\eta_\ell\) signs | NOT EVALUATED |
| RD-BX (atlas RD-BX-01…07) | Same amplitude with mixed propagator | Seven nonzero signed \(BA'\) pair classes from atlas §4 | EFT mixed exchange/contact graphs | Fix kinetic-mixing boundary; explicitly verify the three charge-factor zeros | CONDITIONAL / NOT EVALUATED |
| LD-EXT | \(Q_{LD}\) external-field sector | \(L,H\) self-energies, seagulls and LSZ/parameter pieces in the UV convention | EFT \(L,H\) self-energies and matching field convention | Avoid counting an external-field correction both as LSZ and as a local vertex | NOT EVALUATED |
| RD-EXT | \(Q_{RD}\) external-field sector | \(\ell_R,S\) self-energies, scalar seagull and LSZ/parameter pieces | EFT \(\ell_R,S\) self-energies and matching field convention | Same external-field convention as UV | NOT EVALUATED |
| LD-CUR (see `research/RC-001-dim6-current-form-factor-atlas.md`) | \(\bar L L V\) and \(H^\dagger H V\) current/form-factor amplitudes | Gauge-invariant vertex sets and contact terms, separated from reducible gauge exchange | EFT current insertions, EOM terms and counterterms | Do not count current exchange as a local 1PI scalar coefficient; preserve \(SU(2)\) tensors | NOT EVALUATED |
| RD-CUR (see `research/RC-001-dim6-current-form-factor-atlas.md`) | \(\bar\ell_R\ell_R V\) and \(S^\dagger S V\) current/form-factor amplitudes | \(B,A'\), and conditional mixed current sets | EFT current insertions, contact terms and counterterms | Use the same \(U(1)\) current and kinetic-mixing convention | NOT EVALUATED |
| BASIS | Full common-basis coefficient vector | Sum only amplitudes at the same coupling order and external-state projection | Apply EOM/IBP/Fierz once to the summed coefficients | Record redundant coefficients, nonredundant coefficients, source/potential companions and four-fermion shifts separately | OPEN |

### 2.1 Evaluated diagonal-gauge input-parameter counterterms

The pure diagonal-gauge \(\overline{\mathrm{MS}}\) parameter-renormalization sub-block is derived in `research/RC-001-dim6-gauge-parameter-counterterms.md`. With \(Y_L=-1/2\), \(Y_E=-1\), \(C_2(L)=3/4\), \(C_2(E)=0\), and \(Q_X(L)=Q_X(E)=\eta_\ell Q_\ell\),
\[
\left.\frac{\delta C_{LD}}{C_{LD}}\right|_{y,M;\,\mathrm{diag}}
=\frac{1}{16\pi^2\epsilon}\left(\frac94g_Y^2-\frac94g_2^2+0\cdot g_X^2\right).
\]
For the \(\lambda_\ell\bar E_{\ell L}S_\ell\ell_R\) coupling, \(E\) and \(\ell_R\) have equal-magnitude hypercharge and opposite \(X\)-charge, so
\[
\left.\frac{\delta C_{RD}}{C_{RD}}\right|_{\lambda,M;\,\mathrm{diag}}=0.
\]
These are **only** the \(y,\lambda,M_E\) parameter-counterterm pieces. They are not the complete UV pole of the four-point amplitude, not the EFT operator counterterm, and not a finite matching coefficient. Mixed \(B-A'\) kinetic-mixing terms are not included in these expressions and remain conditional on the declared gauge-field basis/boundary.

### 2.2 Common light-external-leg gauge factors

For the pure gauge correction at \(O(g^2/M_E^2)\), light-field self-energy/LSZ factors are common to the UV and EFT amplitudes when the same renormalized light fields, gauge-fixing convention, and input scheme are used. At the matched tree order,
\[
\left.\Gamma_{\rm UV}^{(0)}\right|_{M_E^{-2}}
=\Gamma_{\rm EFT}^{(0)}[C_{LD/RD}],
\]
so the common external-leg contribution obeys
\[
\Delta\Gamma_{\rm ext,light}^{(1)}
=\frac12\sum_{i\in\text{light external legs}}\delta Z_i
\left(\Gamma_{\rm UV}^{(0)}-\Gamma_{\rm EFT}^{(0)}\right)
=0
\quad\text{through }O(M_E^{-2}).
\]
For \(Q_{LD}\) this common factor is \(\delta Z_L+\delta Z_H\); for \(Q_{RD}\) it is \(\delta Z_{\ell_R}+\delta Z_S\). Keep these graphs in the Ward-identity/LSZ bookkeeping, but do not count the identical light-only factor twice as a new local matching coefficient. This cancellation does **not** apply to heavy-\(E\) self-energy insertions, heavy-light vertex/box graphs, parameter counterterms, or external gauge-field wavefunction/kinetic-mixing thresholds. If the UV/EFT light-field definitions differ by a finite decoupling relation, record that relation explicitly before using this cancellation.

### 2.3 Evaluated heavy-line and scalar master-integral sub-blocks

The explicit Feynman-parameter result for the heavy-\(E_\ell\) self-energy, the zero-momentum Yukawa-vertex scalar kernel, and a representative crossed-box master integral are recorded in `research/RC-001-dim6-heavy-line-vertex-box-integrals.md`. In Feynman gauge and with \(\Delta_\epsilon=1/\epsilon-\gamma_E+\ln4\pi\),
\[
\Sigma_V(0)=-\Delta_\epsilon+L_\ell-\frac12,\qquad
\Sigma_S(0)=4\Delta_\epsilon-4L_\ell+2,
\]
so the bare 1PI insertion into the chirality-preserving heavy propagator gives the subgraph factor
\[
\left.\frac{\delta S_{E,\rm chir}}{S_{E,\rm chir}^{(0)}}\right|_{\Sigma_E^{1PI}}
=\frac{g_A^2C_E^A}{16\pi^2}
\left(-7\Delta_\epsilon+7L_\ell-\frac72\right).
\]
This is gauge-dependent and is not a Wilson coefficient. Its heavy-field/mass counterterms cancel the subgraph pole only when counted once in the full amplitude; do not add those same counterterms again through the separate tree-coefficient parameter row.

The zero-momentum Yukawa-vertex kernel reduces to \(B_0(0;0,M_E^2)=\Delta_\epsilon+1-L_\ell\); representative numerator reductions are \(d\,B_0\) for the heavy-light-fermion exchange and \(B_0\) for the heavy-scalar exchange when the external scalar momentum is set to zero, before overall Feynman-rule signs and charge generators. The finite expansion \(d\,B_0=4\Delta_\epsilon+2-4L_\ell+O(\epsilon)\) is checked explicitly, retaining the \((-2\epsilon)(1/\epsilon)\) contribution. For a crossed-box master,
\[
J_{\rm full}=\frac1{M_E^2}(\Delta_{\rm IR}+1-L_\ell),\quad
J_{\rm soft}=\frac1{M_E^2}(-\Delta_{\rm UV}+\Delta_{\rm IR}),
\]
and hence
\[
J_{\rm hard}=J_{\rm full}-J_{\rm soft}
=\frac1{M_E^2}(\Delta_{\rm UV}+1-L_\ell).
\]
This is an explicit scalar-integral UV–EFT split, not a complete box amplitude: the Lorentz numerator, graph orientation, multiplicity, and common-basis projection still have to be summed for every atlas row.

The parameter integrals, propagator numerator algebra, and box partial fractions pass the local exact-algebra audit in `calculations/RC-001-dim6-gauge-master-integrals.py` (captured output `validation/RC-001-dim6-gauge-master-integrals.txt`). The additive \(B-A'\) vacuum-polarization trace and finite heavy threshold are separately evaluated in `research/RC-001-dim6-mixed-kinetic-threshold.md` and audited in `calculations/RC-001-dim6-mixed-kinetic-threshold.py`. The additive one-loop pole cancels for the stated complete spectrum, while the finite threshold is proportional to \(\ln(M_{E_\mu}^2/M_{E_\tau}^2)\). This does not fix the independent renormalized kinetic-mixing boundary.

### 2.3.1 Conditional mixed \(B-A'\) input-parameter counterterms

The off-diagonal propagator convention and parameter-induced pole terms are derived separately in `research/RC-001-dim6-mixed-parameter-counterterms.md`. With \(\rho_{BX}\) defined by the mixed line-pair factor \(+\rho_{BX}g_Yg_XQ_\ell(Y_ix_j+x_iY_j)\), the parameter-only sub-block is
\[
\left.\frac{\delta C_{LD}}{C_{LD}}\right|_{BX,\mathrm{parameter}}
=-3\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon},\qquad
\left.\frac{\delta C_{RD}}{C_{RD}}\right|_{BX,\mathrm{parameter}}
=-12\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}{16\pi^2\epsilon}.
\]
For the Lagrangian convention \(-\chi B_{\mu\nu}X^{\mu\nu}/2\), \(\rho_{BX}=-\chi+O(\chi^2)\). These are **not** the complete mixed-gauge matching poles; mixed vertex/box graphs, EFT soft/contact graphs, operator counterterms, and the summed Ward identity remain open. The charge algebra is checked in `calculations/RC-001-dim6-mixed-parameter-counterterms.py` with the captured output `validation/RC-001-dim6-mixed-parameter-counterterms.txt`.

### 2.4 Signed charge factors for both conjugate Yukawa vertices

The signed all-incoming charge factors for all three line pairs at each of the four \(y_\ell,y_\ell^\ast,\lambda_\ell,\lambda_\ell^\ast\) vertices are now tabulated in `research/RC-001-dim6-yukawa-vertex-charge-factors.md`. The exact rational checker is `calculations/RC-001-dim6-yukawa-vertex-charge-factors.py` and the captured local output is `validation/RC-001-dim6-yukawa-vertex-charge-factors.txt`.

For the \(Q_{LD}\) Yukawa vertex \(\bar LHE_R\), the \(BB\), \(A'A'\), and mixed \(BA'\) pair factors \((F_B,F_X,F_{BX})\) are
\[
\bar L-H:\left(\frac14,0,-\frac{\eta_\ell}{2}\right),\quad
\bar L-E_R:\left(-\frac12,-1,\frac{3\eta_\ell}{2}\right),\quad
H-E_R:\left(-\frac12,0,\frac{\eta_\ell}{2}\right).
\]
At the conjugate vertex \(\bar E_RH^\dagger L\), the corresponding factors are
\[
\bar E_R-H^\dagger:\left(-\frac12,0,\frac{\eta_\ell}{2}\right),\quad
\bar E_R-L:\left(-\frac12,-1,\frac{3\eta_\ell}{2}\right),\quad
H^\dagger-L:\left(\frac14,0,-\frac{\eta_\ell}{2}\right).
\]
For \(Q_{RD}\), the mixed factor on the fermion–fermion pair vanishes at each \(\lambda_\ell\) vertex; the two scalar–fermion mixed factors are \(+2\eta_\ell\) and \(-2\eta_\ell\), with their orientation exchanged at the conjugate vertex. All four vertices separately conserve hypercharge and \(X\)-charge for both \(\eta_\mu=+1\) and \(\eta_\tau=-1\).

The charge-factor checks fix the group/charge multipliers; the heavy-containing FF/FS vertex sub-block is now separately evaluated in research/RC-001-dim6-heavy-vertex-hard-pieces.md. Its full UV–EFT four-point sum remains **OPEN** until boxes, self-energy/parameter counterterms, EFT contact graphs, and the Ward/basis projection are combined.

### 2.4.1 Heavy-containing Yukawa-vertex hard sub-blocks

The heavy–light fermion (FF) and heavy–scalar (FS) vertex graphs have now been reduced with their oriented Feynman-rule signs in Feynman gauge. The complete one-vertex results, including the finite \(O(\epsilon)\times 1/\epsilon\) term from \(dB_0\), are in research/RC-001-dim6-heavy-vertex-hard-pieces.md. The exact symbolic checker and captured output are calculations/RC-001-dim6-heavy-vertex-hard-pieces.py and validation/RC-001-dim6-heavy-vertex-hard-pieces.txt.

For a single conjugate Yukawa vertex, define
\[
B_0=\Delta_{\rm UV}+1-L_\ell,\qquad dB_0=4\Delta_{\rm UV}+2-4L_\ell.
\]
The oriented hard factors are \(-F_{\rm FF}dB_0-F_{\rm FS}B_0\), with the signed factors in §2.4. The results are
\[
\begin{array}{c|ccc}
 & B & A'A' & BA'\\ \hline
Q_{LD}:v & \frac52\Delta_{\rm UV}+\frac32-\frac52L_\ell &
4\Delta_{\rm UV}+2-4L_\ell &
-\frac{13}{2}\eta_\ell\Delta_{\rm UV}-\frac72\eta_\ell+\frac{13}{2}\eta_\ell L_\ell\\[2pt]
Q_{RD}:v & 4\Delta_{\rm UV}+2-4L_\ell &
-2\Delta_{\rm UV}+2L_\ell &
-2\eta_\ell\Delta_{\rm UV}-2\eta_\ell+2\eta_\ell L_\ell
\end{array}
\]
where the coupling prefactors are respectively \(g_Y^2\), \(g_X^2Q_\ell^2\), and \(\rho_{BX}g_Yg_XQ_\ell\). Both conjugate vertices contribute, so the corresponding tree-coefficient sub-block is \(2v/(16\pi^2)\) with those prefactors.

These poles and finite constants are **vertex-sub-block results only**. Do not combine them with the heavy-line self-energy counterterm a second time, and do not interpret the sub-block pole as a physical uncanceled divergence. The amplitude ledger rows LD-B/LD-X/LD-BX and RD-B/RD-X/RD-BX remain open until crossed boxes, EFT soft/contact terms, external-field and operator counterterms, and the summed Ward identity have been incorporated.

### 2.5 Light-only Yukawa-vertex loops cancel in the hard difference at \(O(M_E^{-2})\)

There is a useful exact matching simplification for the same-vertex pairs \(\bar L-H\) in \(Q_{LD}\) and \(S-\ell_R\) in \(Q_{RD}\), including their conjugate vertices. In these graphs the gauge loop is made entirely from retained light fields; the heavy propagator carries the fixed total external momentum \(P\) and is not part of the loop integration.

The chirality-preserving heavy propagator expands as
\[
P_R\,\frac{i(\slashed P+M_E)}{P^2-M_E^2}\,P_L
=-\frac{i\slashed P P_L}{M_E^2}
+O(M_E^{-4}),
\]
with the conjugate projection giving the corresponding opposite-chirality term. The EFT tree insertion of \(Q_{LD}\) or \(Q_{RD}\), including the gauge-covariant derivative contact vertices required by the same Ward identity, reproduces exactly this \(O(M_E^{-2})\) term. The light-only loop factor is identical on the two sides when the external momenta, gauge fixing, regulator, and field conventions are held fixed. Thus the *complete gauge-covariant light-only vertex subfamily* cancels in
\[
\left[\Gamma_{\rm UV}^{(1)}-\Gamma_{\rm EFT}^{(1)}\right]_{O(M_E^{-2})}=0
\]
for this subfamily. This is not a statement that an individual scaleless integral has zero UV or IR pole; keep \(\Delta_{\rm UV}\) and \(\Delta_{\rm IR}\) separate until the matched subfamily is assembled.

Consequences for the remaining hard calculation:
- The pure-light \(\bar L-H\) and \(H^\dagger-L\) \(Q_{LD}\) vertex corrections need to remain in the Ward/contact bookkeeping but do not require a new hard Wilson coefficient at this order.
- The pure-light \(S-\ell_R\) and \(S^\ast-\bar\ell_R\) \(Q_{RD}\) vertex corrections have the same status.
- The genuinely new hard vertex kernels are the heavy–light fermion pairs and heavy–scalar pairs listed in `research/RC-001-dim6-yukawa-vertex-charge-factors.md`. These still require their full oriented amplitudes and counterterm combination.

### 2.6 Per-subgraph progress matrix

The following matrix records which mathematical sub-block is actually evaluated. **A subgraph-level kernel is not a completed amplitude row.**

| Subgraph ID | \(Q_{LD}\) contribution | \(Q_{RD}\) contribution | Status |
|---|---|---|---|
| E-SELF-B | \(C_E^B=1\) times the Feynman-gauge kernel in §2.3 | Same heavy representation and kernel | 1PI kernel evaluated; full amplitude/counterterm sum open |
| E-SELF-X | \(C_E^X=Q_\ell^2\) times the same kernel | Same heavy representation and kernel | 1PI kernel evaluated; full amplitude/counterterm sum open |
| E-SELF-W | Zero: \(E_\ell\) is an \(SU(2)_L\) singlet | Zero | Evaluated by representation theory; this does not remove \(W\)-exchange on light \(L,H\) lines in LD |
| E-SELF-BX | Conditional factor \(-2\kappa_{BX}g_Yg_X\eta_\ell Q_\ell\) times the same kernel | Same heavy-line factor | Conditional on the off-diagonal propagator convention and input \(\chi\) |
| LD-YV-E-L | FF hard factor \(-F_{\rm FF}dB_0\) included in the evaluated vertex sub-block | — | Heavy-containing vertex sub-block evaluated; full UV–EFT amplitude/counterterm sum open |
| LD-YV-E-H | FS hard factor \(-F_{\rm FS}B_0\) included in the evaluated vertex sub-block | — | Heavy-containing vertex sub-block evaluated; full UV–EFT amplitude/counterterm sum open |
| LD-YV-L-H | Purely light loop at zero external momenta | — | Soft/scaleless limit identified; retain in common UV/EFT IR bookkeeping |
| RD-YV-E-\(\ell_R\) | — | FF hard factor \(-F_{\rm FF}dB_0\) included in the evaluated vertex sub-block | Heavy-containing vertex sub-block evaluated; full UV–EFT amplitude/counterterm sum open |
| RD-YV-E-S | — | FS hard factor \(-F_{\rm FS}B_0\) included in the evaluated vertex sub-block | Heavy-containing vertex sub-block evaluated; full UV–EFT amplitude/counterterm sum open |
| RD-YV-\(\ell_R\)-S | — | Purely light loop at zero external momenta | Soft/scaleless limit identified; retain in common UV/EFT IR bookkeeping |
| LD/RD-CROSS-BOX | Representative \(J_{\rm hard}=M_E^{-2}(\Delta_{\rm UV}+1-L_\ell)\) | Same scalar master, with distinct numerator/charge routings | Scalar master evaluated; every diagram coefficient and Fierz projection open |
| MIX-2PT | \(\Pi^E_{YX}(0)=g_Yg_XQ_\ell(12\pi^2)^{-1}\ln(M_{E_\mu}^2/M_{E_\tau}^2)\) | Same two-point threshold; not a four-point Wilson coefficient | Additive pole cancels; finite threshold evaluated separately |

The symbols \(\kappa_{BX}\) and \(\chi\) must not be conflated: \(\kappa_{BX}\) denotes the off-diagonal propagator factor in the subgraph formula, while \(\chi(\mu_R)\) is the renormalized kinetic-mixing input in the Lagrangian convention of `research/RC-001-dim6-mixed-kinetic-threshold.md`. The full \(O(g^2/M_E^2)\) Wilson-coefficient rows above remain **NOT EVALUATED** until their graph numerators, orientations, multiplicities, counterterms, EFT contact graphs, and common-basis projections are summed.

## 3. Pole and finite-part table to fill per diagram family

For every graph family \(a\), store the amplitude in a fixed common normalization:
\[
\Gamma_a^{\rm UV}=\frac{1}{16\pi^2M_E^2}
\left[\frac{u_{a,\rm UV}}{\epsilon_{\rm UV}}+
\frac{u_{a,\rm IR}}{\epsilon_{\rm IR}}+
u_{a,\log}L_\ell+u_{a,\rm fin}\right]\mathcal T_a(p_i),
\]
with the coupling product, group factor, weak tensor and Dirac tensor written outside or inside \(\mathcal T_a\) consistently. The EFT graph has the same external tensor decomposition:
\[
\Gamma_a^{\rm EFT}=\frac{1}{16\pi^2M_E^2}
\left[\frac{e_{a,\rm UV}}{\epsilon_{\rm UV}}+
\frac{e_{a,\rm IR}}{\epsilon_{\rm IR}}+
e_{a,\log}\ell_q+e_{a,\rm fin}\right]\mathcal T_a(p_i).
\]
These are data-entry templates, not asserted values. The entries \(u_{a,*}\) and \(e_{a,*}\) remain blank until the corresponding integral is calculated. After summing all graphs and counterterms, verify:

1. Identical IR poles cancel in \(\Gamma_{\rm UV}-\Gamma_{\rm EFT}\).
2. Gauge-parameter dependence cancels in the matching coefficient or is accounted for by the declared off-shell/EOM basis.
3. Remaining UV poles are removed by the EFT counterterm matrix in the chosen basis.
4. The finite polynomial has the expected dimension, chirality, weak tensor, flavor charge, and decoupling power \(M_E^{-2}\).
5. The same result follows after the allowed field redefinition/EOM transformation, with companion source and potential terms included.

A nonzero uncancelled IR pole, an unexplained gauge-parameter dependence, or a missing counterterm blocks coefficient promotion.

## 4. Common operator-basis reduction ledger

Use the following order; do not apply EOM before the UV-minus-EFT difference and tensor decomposition are recorded.

1. **Raw redundant basis.** Keep \(Q_{LD},Q_{RD}\), the explicit current operators, and the tensor structures generated by each graph. Preserve the \(SU(2)\) singlet/triplet tensors separately.
2. **Lorentz/Dirac reduction.** Apply gamma identities and chiral projectors with the stated external spinor order. For four-fermion amplitudes, keep scalar-bilinear and vector-current bases distinct until the Fierz sign and Grassmann reordering are explicitly applied.
3. **Weak-index projection.** Use the declared Pauli-matrix normalization. The completeness identity is an algebraic projection check, not a substitute for deriving the coefficient of each tensor from the diagrams.
4. **Gauge Ward identities.** Include external-leg graphs, gauge contact vertices and the gauge-parameter-dependent pieces before checking longitudinal contractions. The \(Q_{LD}/Q_{RD}\) insertion has a \(B\) and \(A'\) contact from \(D(H^\dagger L)\) or \(D(S_\ell\ell_R)\), but no direct \(W\) contact because each differentiated composite is an \(SU(2)\) singlet.
5. **EOM/IBP.** Only after the summed local amplitude is known, map redundant derivative structures into the selected master basis. Include all induced scalar-potential and source rows. Master §252.8–§252.10 gives the scalar-source map; master §254.10–§254.11 gives the optional gauge-EOM/current map. Use one representative only.
6. **Current and four-fermion ledger.** Keep local current operators, reducible gauge-exchange amplitudes, EOM-generated current-current operators, and independently matched four-fermion coefficients as separate entries. Do not add an EOM image on top of the operator it replaces.
7. **External-field/input scheme.** Record whether coefficients are for amputated 1PI Green functions or LSZ-normalized amplitudes. Parameter counterterms and finite field redefinitions must follow the same scheme on both sides.

### 4.1 Exact \(SU(2)_L\) attachment projection already checked

The six \(WW\) line-pair generator contractions for \(Q_{LD}\) are recorded in `research/RC-001-dim6-SU2-attachment-projection.md`. With \(T_0=\delta_{ij}\delta_{kl}\), \(T_x=\delta_{il}\delta_{kj}\), and \(T_3=2T_x-T_0\), the two same-vertex pairs yield \(-3T_0/4\); the cross-vertex pairs LD-W-02 and LD-W-05 yield \(+T_3/4\), while LD-W-01 and LD-W-06 yield \(-T_3/4\). All six identities pass the local exact SymPy tensor check recorded in `validation/RC-001-dim6-SU2-attachment-projection.txt`. These factors are generator contractions only. The cross-vertex loop sub-block and same-vertex pure-soft identity are recorded in §§4.2–4.3; exact full diagram signs/multiplicities and the complete counterterm/Ward sum remain open.

### 4.2 Fixed-routing \(Q_{LD}\) pure-\(WW\) cross-box sub-block

The four cross-vertex classes LD-W-01/02/05/06 are now reduced with their own external-momentum routings in research/RC-001-dim6-WW-crossbox-exact-routing.md, with the exact-rational script calculations/RC-001-dim6-WW-crossbox-exact-routing.py and output validation/RC-001-dim6-WW-crossbox-exact-routing.txt. For one fixed ordered \(\bar L H H^\dagger L\) amplitude and unit multiplicity, the Lorentz kernels derived from the explicit numerator chains are
\[
A_{01}=\frac{2(d-2)}dK,\quad
A_{02}=-J+\frac2dK,\quad
A_{05}=2\left(1-\frac1d\right)J-\frac2dK,\quad
A_{06}=-J+\frac2dK.
\]
In particular \(A_{02}=A_{06}\) after the \(q^2\) cancellation at \(O(P)\). With the weak weights \((-1,+1,+1,-1)T_3/4\), the weighted sum collapses to \((d-1)(J-K)/(2d)\). Its hard/soft/full master sums are
\[
A_{\rm hard}=\frac1{M_E^2}\left(\frac38\Delta_{\rm UV}-\frac38L+\frac{11}{16}\right),
\]
\[
A_{\rm soft}=\frac1{M_E^2}\frac38(-\Delta_{\rm UV}+\Delta_{\rm IR}),\qquad
A_{\rm full}=\frac1{M_E^2}\left(\frac38\Delta_{\rm IR}-\frac38L+\frac{11}{16}\right).
\]
The hard UV pole cancels the soft/EFT UV pole at the scalar-master level, leaving the common IR pole. The dimensional prefactor is \((d-1)/(2d)=3/8-\epsilon/16+\cdots\): the \(d=4\) hard finite constant is \(3/4\), and the \(O(\epsilon)\Delta_{\rm UV}\) term shifts it by \(-1/16\), yielding \(11/16\). An independent gamma-function evaluation of the combined full master reproduces \((J-K)_{\rm full}=(\Delta_{\rm IR}+2-L)/M_E^2\).

The same four numerator chains have also been contracted with the longitudinal gauge projector \(k_\mu k_\nu/k^2\). The pair kernels are \((-2K/d,\,-J+2K/d,\,-2K/d,\,-J+2K/d)\) for pairs (01,02,05,06), respectively; their weak-triplet weighted sum vanishes exactly. This establishes gauge-parameter independence of this fixed-routing triplet cross-box sub-block, but is not the complete Slavnov–Taylor identity for the full amplitude. The exact off-shell Pauli/Fierz and EOM/IBP map of its triplet derivative tensor is recorded in research/RC-001-dim6-current-form-factor-atlas.md §3.3. A symmetric nonexceptional four-point Euclidean kinematic point and invertible local-projector Gram matrix are specified in research/RC-001-dim6-nonexceptional-matching-kinematics.md; its Gram-matrix checks are recorded in calculations/RC-001-dim6-nonexceptional-kinematics.py and validation/RC-001-dim6-nonexceptional-kinematics.txt. The fixed-routing four-cross-box triplet sub-block now has its nonexceptional hard pole, EFT-soft pole, and finite local hard polynomial explicitly compared in research/RC-001-dim6-nonexceptional-matching-kinematics.md §§3.1–3.4. The same-vertex 03/04 pure-soft identity is now separately established in §4.3; the complete nonexceptional subtraction across the remaining external-field routings, external legs, and counterterms remains open.

A first nonexceptional **EFT-soft sub-block** is now evaluated in research/RC-001-dim6-nonexceptional-matching-kinematics.md §§3.1–3.3. The general heavy momentum is \(k-p_1-p_2\); all four soft triangles have \(a^2=b^2=\mu_{\rm IR}^2\) and \((a-b)^2=4\mu_{\rm IR}^2/3\). The stripped triplet UV-pole residue before the leading \(-1/M_E^2\) heavy factor is
\[
R_{T_3}^{\rm soft}=\frac12\slashed p_1+\frac38\slashed p_2+\frac34\slashed p_3,
\]
which reduces to \(3\slashed P/8\) in the old exceptional limit. The scalar triangle and a finite rank-three/pseudovector soft form factor are also evaluated. The latter is nonlocal and must be retained in the full off-shell tensor comparison; it is not a local Wilson coefficient. Exact algebra and numerical masters are recorded in calculations/RC-001-dim6-WW-nonexceptional-soft-pole.py and validation/RC-001-dim6-WW-nonexceptional-soft-pole.txt. The d-dimensional hard-region expansion now gives the weighted local polynomials R_J(d) and R_K(d), with hard pole residue (1/2)p1+(3/8)p2+(3/4)p3 matching the EFT-soft pole with opposite sign. The MS-bar finite local hard polynomial is (1/2-L/2)p1+(11/16-3L/8)p2+(1/4-3L/4)p3. The rank-three nonlocal soft term cancels against the EFT insertion for this fixed subset by the expansion-by-regions identity. The second routing, remaining attachment classes, counterterms, and complete Ward sum remain open.

This is a fixed-ordering, unit-multiplicity sub-block only. The charge-conjugate operator orientation is \(Q_{LD}^\dagger\), which equals \(Q_{LD}\) in the integrated action modulo a total derivative; no extra factor of two is assigned. The manual Wick-contraction factor \(2/2!=1\) is documented separately, but exact graph-generator reconciliation, same-vertex 03/04 and external-field Ward bookkeeping, operator counterterms, the UV one-\(W\) form factor, nonexceptional UV-minus-EFT subtraction, and full Wilson-vector projection remain open. No complete LD-W Wilson coefficient is claimed.

### 4.3 Same-vertex \(Q_{LD}\) pure-\(WW\) soft sub-block

The same-vertex classes LD-W-03 (\(\bar L-H\)) and LD-W-04 (\(L-H^\dagger\)) are now checked in research/RC-001-dim6-WW-same-vertex-soft-matching.md. Their W-loop denominators are \(k^2(k+p_1)^2(k-p_2)^2\) and \(k^2(k+p_4)^2(k-p_3)^2\), respectively; the heavy propagator carries only the external channel momentum \(P=p_1+p_2=-(p_3+p_4)\). The chiral projection removes the heavy mass numerator and gives \(-\slashed P/M_E^2\), identical to the EFT derivative momentum \(\slashed q_D/M_E^2\) with \(q_D=p_3+p_4=-P\). The stripped UV numerator has leading term \(-k^2\mathbf1\), so the common light triangle has a logarithmic UV pole, but its complete light-loop factor is identical in UV and EFT. Since no heavy-scale denominator occurs in the W loop, the hard-region integrals are scaleless. Thus these two same-vertex subgraphs have zero hard-minus-soft matching contribution at \(O(M_E^{-2})\); they remain in the EFT soft sum, operator renormalization and full Ward identity. The explicit algebraic check is in calculations/RC-001-dim6-WW-same-vertex-soft-identity.py and validation/RC-001-dim6-WW-same-vertex-soft-identity.txt. It is not a finite triangle integration or an independent diagram-package validation.

## 5. Existing analytic results that are not to be recomputed or double-counted

The current analytic note already records the stripped hard/soft kernels for three loop-dependent \(C_5C_5^\ast\) crossed-current channels, the \(C_5C_5^\ast\) four-fermion scalar bubble, and the \(Q_{LD}/Q_{RD}\)-plus-quartic EOM kernel. The primary SymPy script reports 41 exact checks; the separate compact script reports 23 local exact checks. These validate selected integral kernels and algebraic reductions only.

Master §§252–255 also contain the previously calculated bosonic field-strength/current-to-gauge and scalar/source blocks. They remain existing modules. The missing target here is the one-loop gauge correction to the fermionic derivative/current sector, including heavy-line attachments, external legs, contact vertices, counterterms, and a common-basis sum.

## 6. Independent diagram-level validation; CI waived

The current runtime has SymPy but no Mathematica/Wolfram executable, FeynCalc, FeynArts, pyfeyn, or QGRAF installation. The local attachment-census script therefore cannot validate loop numerators, symmetry factors, diagram signs, or finite coefficients. This absence is recorded as missing evidence, not as a successful independent check.

GitHub Actions was attempted on the updated branch but repeatedly failed before any job step, with runner ID zero and no executed steps. Per explicit project decision, CI is skipped for this iteration and is not a closure gate. This is not a CI pass and does not establish a script-level failure. The ledger's physics requirements remain unchanged: local checks may verify the structural census, but only actual amplitude calculations and independent diagram-level evidence can close the gauge-matching rows.

## 7. Physics closure criteria

Do not close the gauge sector until the diagram-level generated list is reconciled against this attachment census; each amplitude row has UV and EFT pole/finite data; the common-basis projection includes current/source/potential and four-fermion companions; and the kinetic-mixing boundary is fixed or explicitly left conditional. CI is explicitly skipped as an unavailable infrastructure check and is not a physics closure criterion; no CI pass is claimed. PR #4 remains Draft/Open until the outstanding amplitude and basis-reduction work is completed.
