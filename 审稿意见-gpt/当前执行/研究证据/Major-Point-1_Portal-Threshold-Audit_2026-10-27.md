# Major Point 1 — Higgs–Singlet Portal Threshold Evidence Audit

> **Document type:** Internal research-evidence record; not part of the formal referee response.
>
> **Status:** Partial analytical support. The portal-threshold algebra is recorded and the benchmark arithmetic is independently reproducible; the full diagram-level UV–EFT calculation and physical scalar-mixing prediction remain open.
>
> **Audit date:** 2026-10-27

## 1. Purpose and scope

This note carries into `axial-vector-review-response` a concise, traceable evidence summary for the Higgs–singlet portal threshold relevant to Major Point 1. It does **not** copy the complete calculation repository or promote a provisional result to a final model prediction.

The calculation authority remains `high-energy-theory-research`. The evidence snapshot in this repository records the source version, assumptions, formulas, benchmark arithmetic, validation limits, and the reviewer-task mapping.

In scope:

- the zero-momentum effective-potential threshold for \(\lambda_{HS}\);
- the distinction between a UV portal boundary and a low-energy matched portal boundary;
- a reproducible numerical scale check;
- the evidence needed before using the threshold as a physical scalar-mixing prediction.

Out of scope:

- changing the manuscript or the formal response letter;
- changing the v5.6 task checkboxes or declaring any reviewer point closed;
- copying the historical v66 archive or candidate B1/B3 scripts;
- asserting a final Wilson coefficient, mixing angle, or exclusion region.

## 2. Immutable source provenance

### 2.1 Research repository

- **Repository:** [`high-energy-theory-research`](https://github.com/lm846802297-bit/high-energy-theory-research)
- **Source `main` HEAD at audit:** [`d6143c2aa15191ac8521e062d90860ba86713f00`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/d6143c2aa15191ac8521e062d90860ba86713f00)
- **Authoritative RC-001 record:** [`research/RC-001-vll-higgs-singlet-uv-eft.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/research/RC-001-vll-higgs-singlet-uv-eft.md)
- **Record blob SHA:** `4a334a2ad0ca1ebed9063b9657588c82cdf2f14b`
- **Relevant source-record sections:** §§4.3–4.5 (zero-momentum threshold and scope); §§9.4–9.5 (normalization/sign discussion and algebraic-audit limits); §§10.4–10.5 (hard-minus-EFT kernel and the stated EFT subset counterterm); §§6–7 (claim status and acceptance gates).

The record explicitly distinguishes effective-potential algebra from a complete UV amplitude minus EFT amplitude, and states that the FeynArts/FeynCalc scaffold has not been run.

### 2.2 Primary working source used by RC-001

The RC-001 record freezes the following Library source as its baseline:

- **File:** `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261021)(153)_matchete_mapping_version_history.md`
- **Library file ID:** `file_00000000b7b48230a2ada1957a9ed4a0`
- **Version ID:** `1`
- **Size:** `1,989,214` bytes
- **SHA-256:** `f30af8ccc62feafa3923e8356437e4b80b40e518fc9b1188646b4d763e2791f1`
- **Relevant sections:** §§248–251, §§261–262, §273.9, §274; the historical B1/B3 candidate-kernel issue is discussed in §§238–240.

This Library file is not itself committed as a complete v153 source bundle in the research repository. The filename and hash identify the source used by RC-001; they do not imply that every derivation in the cumulative working file has been independently revalidated.

### 2.3 Supporting artifact provenance and limits

The RC-001 record lists an annotated FeynArts/FeynCalc scaffold with SHA-256 `8e2c7a36c5cacecf35194a92cde50e52ec457cb884684c719e5aafc6b67053ab`. It is a 2,577-byte scaffold, **not** an execution log; the custom model file and schematic particle mapping are still required.

The associated historical audit JSON has SHA-256 `dea8c3ff0a18163d4e1b697a4a44ea44f33a416ab7c85adc3dc71c8bd11e0bfa` and identifies v76→v77, not a run against v153. Its reported PASS applies only to the listed effective-potential algebra and artifact-integrity checks; it explicitly records FeynCalc as not run.

The v66 archive remains historical and unchanged. This evidence note does not copy or overwrite it.

## 3. Portal-threshold relation

Under the potential and matching convention recorded in RC-001, the zero-momentum effective-potential result is

\[
\Delta V\big|_{XY}
=-\sum_{\ell=\mu,\tau}
\frac{|y_\ell|^2|\lambda_\ell|^2}{8\pi^2}XY,
\]

and therefore

\[
\lambda_{HS}^{\mathrm{EFT}}(\mu_R)
=\lambda_{HS}^{\mathrm{UV}}(\mu_R)
-\sum_{\ell=\mu,\tau}
\frac{|y_\ell|^2|\lambda_\ell|^2}{8\pi^2}
+\cdots.
\]

This is a leading one-loop, zero-momentum matching relation under the source's stated potential convention. It is not, by itself, a finite-momentum self-energy or a physical mixing-angle prediction.

For the illustrative mass-relation approximation

\[
|y_\ell\lambda_\ell|
\simeq \frac{2M_E m_\ell}{v\,v_s},
\]

the threshold magnitude is

\[
|\Delta\lambda_{HS}^{E}|
\simeq \frac{1}{8\pi^2}
\sum_{\ell=\mu,\tau}
\left(\frac{2M_E m_\ell}{v\,v_s}\right)^2.
\]

The approximation must be checked against the exact mass-eigenstate couplings for any final benchmark. It is used here only to reproduce the numerical scale comparison.

### 3.1 Reproducible illustrative benchmark

Inputs:

| Input | Value |
|---|---:|
| \(M_E\) | \(1000\ \mathrm{GeV}\) |
| \(v\) | \(246\ \mathrm{GeV}\) |
| \(v_s\) | \(30\ \mathrm{GeV}\) |
| \(m_h\) | \(125\ \mathrm{GeV}\) |
| \(m_\mu\) | \(0.105658\ \mathrm{GeV}\) |
| \(m_\tau\) | \(1.77686\ \mathrm{GeV}\) |

The arithmetic can be reproduced with standard Python:

```python
from math import pi

M_E = 1000.0
v = 246.0
v_s = 30.0
m_h = 125.0
m_mu = 0.105658
m_tau = 1.77686

products_sq = sum(
    (2.0 * M_E * m / (v * v_s)) ** 2
    for m in (m_mu, m_tau)
)
delta_lambda = -products_sq / (8.0 * pi**2)

# Potential Hessian contribution and the source's 1PI convention
delta_Mhs_sq = v * v_s * delta_lambda
delta_Pi_hard_0 = -v * v_s * delta_lambda

print("Delta lambda_HS =", delta_lambda)
print("delta M_hs^2 from potential =", delta_Mhs_sq, "GeV^2")
print("Delta Pi_hs^hard(0) =", delta_Pi_hard_0, "GeV^2")
print("|delta M_hs^2| / m_h^2 =", abs(delta_Mhs_sq) / m_h**2)
```

Rounded output:

- \(\Delta\lambda_{HS}^{E}\simeq-2.9471\times10^{-3}\) if the UV portal boundary is set to zero at the matching scale in this convention;
- the corresponding potential-Hessian contribution is \(\Delta M_{hs}^2=v v_s\Delta\lambda_{HS}^{E}\simeq-21.7497\ \mathrm{GeV}^2\);
- the source's 1PI convention gives \(\Delta\Pi_{hs}^{\mathrm{hard}}(0)=-v v_s\Delta\lambda_{HS}^{E}\simeq+21.7497\ \mathrm{GeV}^2\);
- the magnitude ratio \(|\Delta M_{hs}^2|/m_h^2\simeq1.3920\times10^{-3}\).

**Sign bookkeeping:** the potential-Hessian entry and the source-convention 1PI self-energy have opposite signs in these definitions. They must not be silently identified with one another. The common magnitude is a threshold scale, not a final physical mixing angle.

### 3.2 Why the historical low-energy estimate is not interchangeable with the threshold

A historical low-energy \(\tau\)-loop estimate in the cumulative working source has the parametric form

\[
\frac{|\delta m_{sh}^2(m_h^2)|}{m_h^2}
\simeq
\frac{m_\tau^2}{16\pi^2 v\,v_s}
\ln\frac{M_E^2}{m_h^2}.
\]

Comparing magnitudes after substituting the same leading mass relation gives the indicative ratio

\[
R\simeq
\frac{8M_E^2}{m_h^2\ln(M_E^2/m_h^2)}
\simeq 1.23\times10^2
\]

for \(M_E=1\ \mathrm{TeV}\) and \(m_h=125\ \mathrm{GeV}\).

This ratio is **not** a comparison of two already-matched physical observables. It compares a hard, zero-momentum threshold scale with a historical low-energy logarithmic estimate. The complete calculation must specify the portal boundary, matching scale and scheme, finite-momentum terms, EFT soft subtraction, and the pole/input scheme before interpreting their sum. The numerical difference alone does not prove either formula wrong.

## 4. Portal boundary conditions: two distinct assumptions

At the stated matching scale and to the displayed order, the matching relation permits different choices:

| Choice | Boundary condition | Consequence at this order | What it does not establish |
|---|---|---|---|
| A | \(\lambda_{HS}^{\mathrm{UV}}(M_E)=0\) | \(\lambda_{HS}^{\mathrm{EFT}}(M_E)\simeq-2.9471\times10^{-3}\) for the illustrative benchmark | Does not establish a negligible physical mixing angle |
| B | Choose \(\lambda_{HS}^{\mathrm{UV}}(M_E)\simeq+2.9471\times10^{-3}\) so that \(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\) at this order | Cancels the displayed constant portal threshold in the matched EFT parameter | Does not automatically cancel finite-\(p^2\) terms, running, other sectors, or the physical pole mixing |

Choice B is a **chosen boundary condition**, not a cancellation predicted without input. It may be a legitimate benchmark, but it must be declared as such and consistently used in the scalar potential and subsequent phenomenology.

The two choices cannot be mixed in one argument—for example, one cannot set the UV portal to zero to calculate the threshold and then assume the low-energy portal is also zero without specifying an additional condition.

## 5. Evidence classification

### Supported within the recorded scope

- RC-001 records the effective-potential threshold and the matching relation under a stated potential convention.
- The record reports agreement between two effective-potential expansion routes for the stated background-field coefficients, with exact-polynomial and high-precision checks.
- The leading zero-momentum sign relation between the portal threshold and the source-convention hard self-energy is stated explicitly.
- The numerical benchmark arithmetic in §3.1 is independently reproducible from the displayed formula and inputs.

### Conditional or not independently validated

- The mass relation \(|y_\ell\lambda_\ell|\simeq2M_E m_\ell/(v v_s)\) is an approximation; it must be checked against exact mass-eigenstate couplings for a selected UV benchmark.
- The effective-potential algebra does not constitute a completed FeynArts/FeynCalc diagram-level UV-amplitude-minus-EFT-amplitude calculation.
- The historical effective-potential audit JSON refers to v76→v77, not v153; it must not be described as a v153 execution.
- The parameterized momentum-dependent \(h\)–\(s\) self-energy is an algebraic downstream result. The record says its audit does not numerically evaluate the PV integrals and does not run Mathematica/FeynCalc.

### Still open

- A fully specified renormalized \(\lambda_{HS}\) boundary and matching/input scheme.
- Complete UV/EFT hard-minus-soft self-energy at finite momentum, with the required same-order soft insertions, counterterms, tadpole treatment, and external-state normalization.
- The complete physical pole/mixing solution, especially near \(m_s\simeq m_h\).
- Higgs signal-strength, exotic-decay, and scalar-search constraints evaluated consistently with the chosen benchmark.
- Independent diagram-level reproduction and a closed, nonredundant model-level Wilson-coefficient vector.

The current evidence therefore supports **a conditional portal-threshold subclaim**, not a final scalar-mixing prediction or a statement that the entire parameter space is safe.

## 6. Separate open item: historical B1/B3 candidate-kernel signs

B1/B3 is recorded here only as a linked dependency, not as part of the portal-threshold result.

The current RC-001 record states that the historical candidate-kernel audit found a B1/B3 sign difference under its declared Minkowski/Wick convention, while B2 was unchanged. It also explicitly says that the audit lacks the complete external-leg permutation sum, counterterms, and UV–EFT subtraction. It does not settle a physical Wilson coefficient.

- [RC-001 record: evidence boundary and open B1/B3 item](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/research/RC-001-vll-higgs-singlet-uv-eft.md#L130-L140)
- [RC-001 record: claim–evidence decision and required reconciliation](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/research/RC-001-vll-higgs-singlet-uv-eft.md#L216-L238)
- Historical scripts remain in the [v66 calculation archive](https://github.com/lm846802297-bit/high-energy-theory-research/tree/main/artifacts/higgs-portal-v66-20261019/%E8%AE%A1%E7%AE%97%E8%84%9A%E6%9C%AC); they are not copied into this evidence snapshot.

**Decision:** keep B1/B3 open until the numerator convention, Wick factors, external-leg permutations, counterterms, EFT soft subtraction, and common-basis projection are reconciled term by term. Do not change a physical coefficient on the basis of the historical sign warning alone.

## 7. Mapping to referee-response work

| Referee task | What this evidence contributes | Status after this audit |
|---|---|---|
| Major Point 1 — scalar potential, perturbativity, portal/mixing | Records the portal-threshold formula, a reproducible scale check, and the boundary-condition ambiguity | Partial evidence only; the physical scalar-mixing conclusion remains open |
| Major Point 2 — parameter domain and UV–EFT consistency | Makes the portal matching convention and assumptions explicit | Does not close the complete UV–EFT matching or parameter scan |
| Major Point 4.2 — kinetic mixing | No new kinetic-mixing observable or full mixed-propagator calculation is added here | Unchanged; remains a separate task |
| Major Point 3 — neutrino masses and PMNS | No neutrino mass matrix or PMNS fit is performed here | Unchanged; remains open |
| Major Points 4.3–4.4 — finite vector coupling and stellar/SN constraints | No corresponding experimental recast is performed here | Unchanged; remains open |

This document is an evidence supplement, **not** a replacement for the v5.6 execution manual or manuscript Diff. No task state is changed by adding it.

## 8. Next acceptance gates

1. Choose and record the UV portal boundary, renormalization scheme, and matching scale; do not leave them implicit.
2. Reconcile the zero-momentum threshold with the finite-\(p^2\) self-energy and the EFT soft contribution in one sign-consistent ledger.
3. Execute the relevant FeynArts/FeynCalc workflow with the actual model file, recording versions, graph counts, warnings, intermediate expressions, and output hashes.
4. Solve the complete scalar pole/mixing problem in a declared benchmark and separately inspect the near-degenerate region.
5. Apply the corresponding Higgs/scalar constraints before making any exclusion or viability claim.
6. Only after these gates pass should the internal status and the manuscript Diff be updated. The formal response letter must not claim the calculation is complete beforehand.

## 9. Change control

- No formal response letter or manuscript PDF was changed.
- No v5.6 task checkbox was changed.
- No physical Wilson coefficient or exclusion claim was changed.
- No candidate B1/B3 script was copied.
- The source research repository and its v66 historical archive remain unchanged.
- This file is an internal evidence snapshot. Any later change to the baseline or conclusion must be recorded as a new, reviewable diff with source provenance.
