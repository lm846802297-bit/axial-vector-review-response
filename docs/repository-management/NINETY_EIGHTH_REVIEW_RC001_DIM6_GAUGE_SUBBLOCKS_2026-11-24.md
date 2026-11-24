# Ninety-eighth supplemental document review — RC-001 dimension-six gauge sub-blocks

**Review date:** 2026-11-24  
**Review branch:** `maintenance/92nd-document-review-20261124`  
**PR:** #142, base `main` at `6986463487ddade80ad72e67087b376e34969835`  
**Frozen upstream source:** `high-energy-theory-research` commit `b2dd8f7e4427d0292bc299d273c780c05021fdab`  
**Scope:** diagonal and mixed input-parameter counterterms, heavy-line Yukawa-vertex kernels, light-only UV/EFT cancellation, Yukawa charge factors, mixed kinetic threshold, and the associated independent soft-kernel/kinematic validation records.

The selected dimension-six records below are handled in the existing register order. This is a sub-block review, not a claim that the earlier RC-001 QLD8/WW records or the full document queue have been cleared.

## 1. Scientific findings

### 1.1 Diagonal gauge parameter counterterms

The exact-rational source was executed. For the parameter-renormalization sub-block,
[
\frac{\delta C_{LD}}{C_{LD}}
=\frac{1}{16\pi^2\epsilon}
\left(\frac94g_Y^2-\frac94g_2^2+0\,g_X^2Q_\ell^2\right),
\qquad
\frac{\delta C_{RD}}{C_{RD}}=0.
]
The (g_X^2) cancellation in (C_{LD}) is only the cancellation between the (y_\ell) and (M_E) parameter counterterms. It is not a cancellation of the complete (X)-gauge correction to the dimension-six operator. The source checks the arithmetic of the supplied one-loop MS pole formulas; it does not evaluate the loop integrals or the operator counterterm matrix.

**Disposition:** `PASS_WITH_NOTES`.

### 1.2 Heavy-line Yukawa-vertex hard pieces

The exact source and its stdout were reproduced. Retaining the (O(\epsilon)) part of the numerator is essential:
[
dB_0=(4-2\epsilon)
\left(\Delta_\epsilon+1-L_\ell\right)
=4\Delta_\epsilon+2-4L_\ell+O(\epsilon).
]
The six one-orientation hard factors (v=-F_{FF}dB_0-F_{FS}B_0) are
[
\begin{array}{c|l}
LD,B & \frac52\Delta_\epsilon+\frac32-\frac52L_\ell\\
LD,X & 4\Delta_\epsilon+2-4L_\ell\\
LD,BX & \eta_\ell\left(-\frac{13}{2}\Delta_\epsilon-\frac72+\frac{13}{2}L_\ell\right)\\
RD,B & 4\Delta_\epsilon+2-4L_\ell\\
RD,X & -2\Delta_\epsilon+2L_\ell\\
RD,BX & \eta_\ell(-2\Delta_\epsilon-2+2L_\ell).
\end{array}
]
The two conjugate vertices give (2v/(16\pi^2)) with the corresponding coupling and charge prefactors. The charge factors and oriented (-F) convention are those derived in the paired research note. This is a heavy-containing vertex sub-block only; it is not the complete four-point amplitude or a final Wilson coefficient.

**Disposition:** `PASS_WITH_NOTES`.

### 1.3 Light-only Yukawa-vertex cancellation

The tree propagator expansion is
[
P_R\frac{i(\slashed P+M_E)}{P^2-M_E^2}P_L
=-\frac{i\slashed P P_L}{M_E^2}+O(M_E^{-4}).
]
The paired script checks this expansion. Its second equality check assigns the same symbolic expression to the UV and EFT placeholders, so that line is not an independent calculation of the loop/contact equality. The physical cancellation is instead established by the analytic derivation in the subtraction ledger §2.5: the (Q_{LD/RD}) insertion, including the gauge-covariant derivative contact vertices, reproduces the leading heavy-propagator term when the same external momenta, gauge fixing, regulator and light-field convention are used. Thus the complete light-only subfamily cancels in the UV-minus-EFT difference at (O(M_E^{-2})). Individual scaleless integrals must still retain their UV/IR labels until that subfamily is assembled.

**Disposition:** `PASS_WITH_NOTES`; the executable assertion is limited to the propagator expansion, while the cancellation proof is analytic and sourced to ledger §2.5.

### 1.4 Yukawa-vertex charge factors

The exact charge source was executed for (eta_\mu=+1) and (eta_\tau=-1). All four (y,y^*,\lambda,\lambda^*) vertices conserve (Y) and (X); all 12 unordered pair assignments reproduce the signed (B), (X), and mixed (BX) factors, including equality of conjugate orientations. The heavy-containing FF/FS factors used above are
[
\begin{array}{c|rr|rr|rr}
 & F_{FF}^{B}&F_{FS}^{B}&F_{FF}^{X}&F_{FS}^{X}
 &F_{FF}^{BX}&F_{FS}^{BX}\\ \hline
LD&-\frac12&-\frac12&-1&0&\frac32\eta_\ell&\frac12\eta_\ell\\
RD&-1&0&+1&-2&0&2\eta_\ell
\end{array}
]
The paired script checks the Abelian charge products. The (SU(2)_L) representation contraction is a separate analytic group-theory statement in the research note; no (W)-loop amplitude is evaluated by this script.

**Disposition:** `PASS_WITH_NOTES).

### 1.5 Mixed (B-A') kinetic threshold

The light Weyl trace cancels separately for each flavor. The two heavy Dirac traces cancel additively between (mu) and (	au), while the finite threshold remains
[
\Pi_{YX}^{E}(0)
=\frac{g_Yg_XQ_\ell}{12\pi^2}
\ln\frac{M_{E_\mu}^2}{M_{E_\tau}^2}.
]
The paired script checks the charge traces and logarithm identity. The (1/(12\pi^2)) normalization and sign follow from the one-Dirac transverse vacuum-polarization integral derived in the companion note. This threshold is a separate two-point gauge-sector matching result; it does not set the independent renormalized boundary value of (\chi), and inserting a one-loop-generated threshold into another one-loop four-point graph would be a two-loop effect.

**Disposition:** `PASS_WITH_NOTES).

### 1.6 Mixed input-parameter counterterms

With the signed off-diagonal propagator convention (\rho_{BX}=-\chi+O(\chi^2)), the exact charge algebra gives
[
\frac{\delta C_{LD}}{C_{LD}}\bigg|_{BX,\mathrm{parameter}}
=-3\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}
{16\pi^2\epsilon},
\qquad
\frac{\delta C_{RD}}{C_{RD}}\bigg|_{BX,\mathrm{parameter}}
=-12\frac{\rho_{BX}\eta_\ell g_Yg_XQ_\ell}
{16\pi^2\epsilon}.
]
The difference arises because the mixed term in the (\lambda_\ell) Yukawa counterterm vanishes, while the heavy-mass counterterm does not. These are parameter-only poles; mixed vertex/box graphs, EFT contacts, the operator counterterm matrix and the summed Ward identity remain separate.

**Disposition:** `PASS_WITH_NOTES).

### 1.7 Independent soft-kernel checks

The compact independent-kernel source passed 23 exact symbolic checks, including the massless Feynman-parameter logarithm, first moment, scalar numerator identity, stripped hard/soft sums for the crossed-current, four-fermion and (Q_6)-plus-quartic kernels, and all 16 (SU(2)) singlet/triplet completeness components.

The larger soft-loop cross-check passed 41 exact symbolic checks. It reconstructs the stated (J_{22}), (K_{21}), (J_{12}), and (J_{13}) Gamma-function limits; the crossed-current hard/soft kernel with the (O(\epsilon)\times1/\epsilon) term retained; the four-fermion scalar bubble; the (Q_6)-plus-quartic EOM kernel; the (SU(2)) tensor completeness; and the explicit four-dimensional chiral Fierz matrix identity. The script uses a common pole placeholder in its algebraic hard-plus-soft sums; the research note keeps (\Delta_{UV}) and (\Delta_{IR}) distinct. Neither script generates the full UV diagrams or gauge-correction amplitudes.

**Disposition:** both validation outputs `PASS_WITH_NOTES); the companion soft-loop research note is `PASS_WITH_NOTES) within its stated stripped-kernel scope.

### 1.8 Nonexceptional kinematics record

The symmetric point has
[
p_i^2=\mu_{IR}^2,\qquad p_i\cdot p_j=-\frac{\mu_{IR}^2}{3}
\quad(i\ne j),
]
so each two-particle channel is (4\mu_{IR}^2/3) and
[
\det G_{(p_1,p_2,p_3)}=\frac{16}{27}\mu_{IR}^6.
]
The paired script checks the momentum-conservation completion, (p_4^2), (p_4\cdot p_i), the Gram determinant and channel invariants. Its archived validation text is a curated summary, not byte-identical stdout; the eigenvalue line is printed by the script but not asserted there. An additional exact local check gives (G_3/\mu_{IR}^2) eigenvalues ((1/3,4/3,4/3)), and the full (4\times4) Gram matrix has one zero eigenvalue from momentum conservation and three positive eigenvalues. Direct high-precision integration also reproduces the note's two scalar-triangle numbers:
[
T(4/3)=2.12403394800381915507545158988847321747826679,
]
[
I_\epsilon(4/3)=0.746770041339790484348277151967488877997198981.
]
This batch does not rederive the complete fixed-routing WW hard-region tensor expansion, its nonlocal rank-three soft form factor, or the full Ward/EOM projection. Therefore the **kinematics validation output** is `PASS_WITH_NOTES), while the broader `RC-001-dim6-nonexceptional-matching-kinematics.md` remains `PENDING).

## 2. Local execution and exact provenance

**Environment**
- Python `3.13.5`; SymPy `1.14.0).
- Linux `6.18.57-x86_64-with-glibc2.41`; architecture `x86_64`.
- CPU: Intel Xeon Platinum 8573C, 5 available vCPUs; reported memory 6,090,668 kB.
- All nine existing dimension-six source scripts passed `py_compile` and executed with exit status zero.
- The independent dimension-six charge/kernel regression and the earlier degree-five target regression were also compiled and executed successfully.

For the nine existing source/output pairs, eight archived outputs are byte-identical to captured stdout. The nonexceptional-kinematics output is a curated summary rather than raw stdout. The two independent regression artifacts are separately fingerprinted below.

| Source script | Source Git blob SHA-1 | Output Git blob SHA-1 | Source SHA-256 | Archived output SHA-256 | Comparison |
|---|---|---|---|---|---|
| `RC-001-dim6-gauge-parameter-counterterms.py` | `219c35748fde05671c349e2237facfd0ab539a59` | `8ee2b5a9e02a60960138539a2c0569c3845706bd` | `c8b20ff126e106001b57786c8045d6dc40486917b6a50e33e1d2b074ff86e985` | `a15f166096d631926f473f21db4eb9d616acaa18ac2800eb515d4144bcbb1a9b` | byte-identical |
| `RC-001-dim6-heavy-vertex-hard-pieces.py` | `9af35a00b1777135286c7c04c02e801b23d19c6b` | `b03afe6273508db3b6af87116388e8a520d70a2c` | `9a41759873983c8e300103a71281284222291bec67e245c1fc758ddae568e4e7` | `55742069583a450cf858159bd805b3baffec3397af24732ee3dc781482493fca` | byte-identical |
| `RC-001-dim6-independent-kernel-check.py` | `052a14d36b2a7efc102fb39f51a50fcae4822c1d` | `6fc04e3bcaa23e851517374eb8a064280eb001dd` | `7dffc4418050a8ec082f9edf4a4580e58b19fe4e13c805ad7736dbcb46ac6bd9` | `b943b2feed10e2590bbe17c1f79bc39387cbecf57ef8563571a4595e1aca7813` | byte-identical |
| `RC-001-dim6-light-only-vertex-cancellation.py` | `1b1a4d3d676c8f39f1c49b9eaf3ea6ef12ae3d1e` | `6c5a65dc80b84a7c8df05c470c333d87588f9c03` | `233217120fc422d2d5550ea469092afbba8f0ef0063c38953f5a39ccaa4eb831` | `c5101b864dd3322a1a7f193874900a14f16fd57bf576c689fa945af4b1902bf6` | byte-identical |
| `RC-001-dim6-mixed-kinetic-threshold.py` | `4b9776f45935785361c77197acfcf8942cf5f7d3` | `8d484bd50f960f698890e2921366e634c5e794c1` | `f92e3292f93be567c95cbd197123283b3bc8cf6056b59701e9fe051f94ae911e` | `e4f61c9099c2717e1d19a8cf933b8cdcf954be07c3908a7616c06a0bbab136b0` | byte-identical |
| `RC-001-dim6-mixed-parameter-counterterms.py` | `151f54829a529224ef1330a1d2bd4c91bf3ec3d0` | `d1ad92faed0e1d8e3701fb9f87ce7a4b735ab4cc` | `e98710730590197e7824631d381602cd85c2bad5eed5b18a3d8393e11cfb30f5` | `c533e142e44a7cba5a39833d026cf027087b0e473e292a1a1e50d40d2341b268` | byte-identical |
| `RC-001-dim6-nonexceptional-kinematics.py` | `9e2433d90b54c02f97fad8dd57c48061b2e5e64b` | `201e9a7ff93307da556826d2fd4ad54b70e68354` | `bc05dfae54002289599643a44198ef2e9ee8979e3cabb549fd06179b8eaf323a` | `fbca51f9e67316f13c57903965c9fdbac59f29f616718144ac24193b4ade840d` | curated summary |
| `RC-001-dim6-soft-loop-crosscheck.py` | `13ad1d453f2dcb27bae2cbc98546bad5b7e4b8ca` | `a63b99622cedfb3074ac10a9f9c5708f9d9e1b74` | `167d698fe58894b6b0a4689becd6a8e075d1c107fb1b174c94ce8b31c94b32c6` | `8dae0c92bbac16ed89362a4da1e0f9bad3d2805e24f1af862f0800d0e9c1c7f1` | byte-identical |
| `RC-001-dim6-yukawa-vertex-charge-factors.py` | `4f74a0ea416833859c668a6392ffce070e273ca1` | `587e1999a4c4c905cf20ab9b215514b58db7ae1e` | `8f33169e3fac7819d450ad9dff6c0828be39283cd2dc33089cc2a61c0f3b75dc` | `1666eced13195d05cdc43b801ac8eb9dcf95eaeeda4de71e36653071a84ea3b1` | byte-identical |

**Independent dimension-six charge/kernel regression**
- Source Git blob: `19cc4cffac58b054f3587b03d3e5f0302bd25656`; SHA-256: `e5b7bffe8a79a2f20384e220701b526ed39100b730599cffcdf406a93824097b`.
- Native output Git blob: `444ec2b058c87b312f9b584cb76be3b0d4b3c0fe`; SHA-256: `f3d76c4d68ac744c18094c8e7683ffba1937550966494d9403d730304df371c3`.

**Earlier degree-five regression re-execution**
- Source Git blob: `18b87e3e1221e9aff3354cee698f8f0506d27624`; SHA-256: `acc5cde604dd39511ca82629f141bb06b315f7e66bdc4ac36fdbc12216db9eef`.
- Captured stdout Git blob: `01908141c033a6ca4e3f9718471f62ba22754ec8`; SHA-256: `beabe7779a96299792cfc75a8bf2b06b99d3c64bb9128fee541cde9abca7af60`.
- The local run reproduces the corrected angular-reduction structures: light (31/12/12), heavy (14/3/3). It does not repeat the 25 radial-master integrations or hard-soft matching.

## 3. Register disposition and remaining work

The following records are promoted to `PASS_WITH_NOTES` with the scopes above: diagonal parameter-counterterm note; heavy-vertex hard-piece note; mixed kinetic-threshold note; mixed parameter-counterterm note; soft-loop-integral note; Yukawa charge-factor note; and the seven pending dimension-six validation outputs (heavy vertex, independent kernel, light-only, mixed parameter, nonexceptional kinematics, soft-loop cross-check, Yukawa charge factors). The already-passing diagonal parameter and mixed kinetic validation rows are updated with the fresh local execution provenance.

Two broader research documents remain `PENDING`:
- `RC-001-dim6-nonexceptional-matching-kinematics.md`: only the Gram-geometry and the two quoted scalar-triangle numbers were checked in this batch; the full WW hard/soft tensor and common EOM/Ward projection were not re-reviewed.
- `RC-001-dim6-uv-eft-subtraction-ledger.md`: §2.5 was used as the analytic source for the light-only cancellation, but the full ledger remains pending.

No full gauge-corrected Wilson coefficient, complete UV-EFT amplitude, diagram-package reproduction, or model-level Wilson vector is claimed. No GitHub Actions pass is claimed; the project continues to use local execution as the primary calculation route.

## 4. Next register-order step

Continue with the next still-PENDING RC-001 dimension-six research record, `RC-001-dim6-nonexceptional-matching-kinematics.md`, then the remaining subtraction-ledger sections and the outstanding gauge/contact/WW records in their existing register order. Only after those are reviewed should the queue advance to the next dimension-eight records.
