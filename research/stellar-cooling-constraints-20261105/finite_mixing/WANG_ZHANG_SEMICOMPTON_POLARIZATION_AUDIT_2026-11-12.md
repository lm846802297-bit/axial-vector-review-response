# Source-level audit of the semi-Compton polarization formulas

**Primary source:** Wang and Zhang, *Revisiting supernova constraints on dark gauge bosons*, arXiv:2610.35379v1, PDF pp. 30 and 45–46.  
**Date:** 2026-11-12  
**Status:** Equation numbering, integrated/differential algebra, positivity, vector Ward identities, and the soft-muon limit have been checked. The origin of the discrepancy in the printed Eqs. (5.9) and (B.6) is not yet identified. No production rate, opacity, transport result, manuscript, referee-response file, or published constraint figure is changed by this audit.

## 1. Scope and conventions

We audit
\[
\gamma(k)+\mu^-(p_1)\longrightarrow \mu^-(p_2)+Z'(q),
\qquad q\equiv k_{Z'}.
\]
The incoming muon is at rest for the analytic low-energy comparison. The mediator is on shell, \(q^2=m_{Z'}^2\), and \(k^2=0\).

Define
\[
\alpha_{\mu\tau}\equiv \frac{g_{\mu\tau}^2}{4\pi},\qquad
c\equiv\cos\theta,\qquad
x\equiv\frac{m_{Z'}}{E_\gamma},\qquad
\beta\equiv\sqrt{1-x^2}.
\]
The low-energy condition \(E_\gamma/m_\mu\ll1\) and the light-vector condition \(x\ll1\) are distinct expansions. They must not be conflated.

The physical final-state vector has two transverse polarizations and one longitudinal polarization. The labels \(T,L\) below refer to physical projectors, not to a polarization average.

## 2. Equation-number map from the original PDF

The equation labels printed in the PDF, rather than the continuous labels produced by the HTML conversion, are used throughout.

| Object | Original equation | PDF page |
|---|---:|---:|
| Integrated transverse cross section | (5.9a) | 30 |
| Integrated longitudinal cross section | (5.9b) | 30 |
| \(s\)- and \(u\)-channel amplitudes | (B.1a), (B.1b) | 45–46 |
| Transverse spin-summed trace | (B.2) | 46 |
| Longitudinal trace defined by subtraction | (B.3) | 46 |
| Total spin-summed trace | (B.4) | 46 |
| Low-energy outgoing-\(Z'\) energy | (B.5) | 46 |
| Differential transverse cross section | (B.6a) | 46 |
| Differential longitudinal cross section | (B.6b) | 46 |
| Medium polarization projectors | (A.15) | 40 |

The HTML rendering uses continuous equation numbers for some of these expressions (including (58a,b) and (106a,b)). Those are not the labels printed in the PDF.

## 3. Amplitude ordering and Ward identities

Let
\[
P_s=p_1+k=p_2+q,\qquad P_u=p_1-q,
\]
and \(D_s=P_s^2-m_\mu^2\), \(D_u=P_u^2-m_\mu^2\). With the outgoing \(Z'\) index denoted by \(\mu\) and the incoming photon index by \(\nu\), the gauge-consistent Compton amplitude is
\[
\mathcal M^{\mu\nu}
=e g_{\mu\tau}\,\bar u(p_2)
\left[
\gamma^\mu\frac{\not P_s+m_\mu}{D_s}\gamma^\nu
+
\gamma^\nu\frac{\not P_u+m_\mu}{D_u}\gamma^\mu
\right]u(p_1).
\]
The two vertices in the \(u\)-channel are reversed relative to the \(s\)-channel.

### 3.1 Printed form of (B.1b)

In the PDF, (B.1b) appears to print the \(u\)-channel chain with the same order,
\[
\gamma^\mu(\not P_u+m_\mu)\gamma^\nu,
\]
while retaining the external polarization factors \(\epsilon_\mu^*(q)\epsilon_\nu(k)\). With the stated momentum routing, this is not the standard crossed Compton chain. The required \(u\)-channel chain is
\[
\boxed{\gamma^\nu(\not P_u+m_\mu)\gamma^\mu.}
\]
This is recorded as an apparent vertex-order/notation issue in the printed (B.1b), not yet as a conclusion about how the authors generated (B.2)–(B.4).

### 3.2 Explicit outgoing-vector Ward contraction

For the correctly ordered amplitude, the on-shell Dirac equations give
\[
q_\mu\mathcal M_s^{\mu\nu}
=+e g_{\mu\tau}\bar u(p_2)\gamma^\nu u(p_1),
\]
\[
q_\mu\mathcal M_u^{\mu\nu}
=-e g_{\mu\tau}\bar u(p_2)\gamma^\nu u(p_1),
\]
so
\[
\boxed{q_\mu\mathcal M^{\mu\nu}=0.}
\]
The analogous contraction with the incoming photon momentum also vanishes:
\[
\boxed{k_\nu\mathcal M^{\mu\nu}=0.}
\]

If the printed \(u\)-channel chain is used literally, the \(q_\mu\) contraction leaves
\[
\bar u(p_2)\not q\,
\frac{\not P_u+m_\mu}{D_u}\gamma^\nu u(p_1),
\]
which does not reduce to the required negative of the \(s\)-channel term. The photon Ward contraction likewise does not telescope. Thus the literal printed chain cannot be used as the gauge-invariant starting amplitude without clarification or correction.

## 4. Physical \(T/L\) projectors and the conserved-current limit

The medium projector (A.15) is
\[
P_T^{\mu\nu}
=\sum_{\lambda=1,2}
\epsilon_\lambda^\mu(q)\epsilon_\lambda^{*\nu}(q),
\qquad
P_L^{\mu\nu}
=-g^{\mu\nu}+\frac{q^\mu q^\nu}{m_{Z'}^2}-P_T^{\mu\nu}.
\]
These projectors resolve the three positive-norm on-shell polarizations.

For a conserved vector current, write
\[
q^\mu=(E',0,0,k'),\qquad k'=\sqrt{E'^2-m_{Z'}^2},
\]
and choose
\[
\epsilon_L^\mu=\frac{1}{m_{Z'}}(k',0,0,E').
\]
Current conservation gives
\[
E'\mathcal M^0-k'\mathcal M^z=0.
\]
Consequently,
\[
\begin{aligned}
\epsilon_L\cdot\mathcal M
&=\frac{k'\mathcal M^0-E'\mathcal M^z}{m_{Z'}}\\
&=-\frac{m_{Z'}}{k'}\mathcal M^0.
\end{aligned}
\]
At fixed nonzero \(E'\), the longitudinal amplitude is therefore suppressed by \(m_{Z'}/E'\), and its squared amplitude by \(m_{Z'}^2/E'^2\). The transverse amplitudes remain finite as \(m_{Z'}\to0\).

This follows from conservation of the muon vector current and does not depend on the supernova profile or on a thermal integration.

## 5. What the printed (B.6) implies

Define
\[
C_0\equiv\frac{\pi\alpha\alpha_{\mu\tau}}{m_\mu^2}.
\]
The printed angular expressions (B.6a,b) become
\[
\frac{d\sigma_T^{\rm paper}}{dc}
=C_0(x^2+2c),
\]
\[
\frac{d\sigma_L^{\rm paper}}{dc}
=C_0[(1-c)^2-x^2c].
\]
The common two-body final-state velocity factor \(\beta\) is not displayed in (B.6). To compare with (5.9), it must either be supplied as a common phase-space factor or understood to have been factored out of the angular kernel. This convention does not affect the sign or polarization-hierarchy tests.

### 5.1 The angular integrals do reproduce (5.9)

Direct integration gives
\[
\int_{-1}^{1}dc\,(x^2+2c)=2x^2,
\]
\[
\int_{-1}^{1}dc\,[(1-c)^2-x^2c]=\frac83.
\]
Restoring the common \(\beta\),
\[
\sigma_T^{\rm paper}=2C_0x^2\beta,
\qquad
\sigma_L^{\rm paper}=\frac83C_0\beta,
\]
which are exactly (5.9a,b).

Thus (5.9) and (B.6) are algebraically consistent with one another. This does not establish that either expression is a valid physical polarization decomposition.

### 5.2 Pointwise positivity fails

A differential cross section into a specified physical polarization is proportional to a nonnegative squared amplitude and must be nonnegative throughout the allowed angular interval.

For \(0<x<1\), the printed transverse expression is negative whenever
\[
-1\le c<-\frac{x^2}{2}.
\]
The printed longitudinal expression is negative whenever
\[
c>0,\qquad (1-c)^2<x^2c.
\]
The boundary of the latter interval is
\[
c_L=1+\frac{x^2}{2}
-x\sqrt{1+\frac{x^2}{4}}.
\]

| \(x=m_{Z'}/E_\gamma\) | Printed \(T\) is negative for | Printed \(L\) is negative for |
|---:|---:|---:|
| 0.01 | \(c<-5.0\times10^{-5}\) | \(c>0.990050\) |
| 0.10 | \(c<-0.005\) | \(c>0.904875\) |
| 0.30 | \(c<-0.045\) | \(c>0.741644\) |
| 0.50 | \(c<-0.125\) | \(c>0.609612\) |

The sum is nonnegative:
\[
\frac{d\sigma_T^{\rm paper}}{dc}
+\frac{d\sigma_L^{\rm paper}}{dc}
=C_0[1+c^2+x^2(1-c)]>0.
\]
A positive polarization sum does not repair negative components. These components cannot be used as separate physical production or absorption rates.

## 6. Independent soft-muon-limit derivation

The decisive comparison is the low-energy limit of the conserved vector-current amplitude with the physical projectors. Retain the finite mediator-mass ratio \(x=m_{Z'}/E_\gamma\) while expanding in \(r=E_\gamma/m_\mu\ll1\).

Let \(\mathcal B_T\) and \(\mathcal B_{\rm tot}\) denote the dimensionless brackets multiplying \(e^2g_{\mu\tau}^2\) in (B.2) and (B.4), and let
\[
\mathcal B_L=\mathcal B_{\rm tot}-\mathcal B_T.
\]
The physical-projector trace, independently evaluated with the correctly ordered \(s/u\) amplitudes, has the leading light-vector behavior
\[
\mathcal B_T=8(1+c^2)+O(r),
\]
\[
\mathcal B_L=8x^2(1-c^2)+O(x^4,r).
\]
The \(O(x^2)\) longitudinal term is the first nonzero term. At angular endpoints where this leading term vanishes, retain the unexpanded exact trace.

The two-body differential cross section is
\[
\frac{d\sigma_h}{dc}
=\frac{1}{32\pi s}\frac{|\mathbf q|}{|\mathbf k|}
\overline{|\mathcal M_h|^2},
\qquad
s=m_\mu^2+2m_\mu E_\gamma.
\]
The bar averages over the two initial muon spin states and the two initial photon polarizations. Since
\[
e^2=4\pi\alpha,\qquad
g_{\mu\tau}^2=4\pi\alpha_{\mu\tau},\qquad
\frac{|\mathbf q|}{|\mathbf k|}
=\beta+O(r),
\]
the leading physical differential cross sections are
\[
\boxed{
\frac{d\sigma_T^{\rm vec}}{dc}
=C_0\beta(1+c^2)+O(r)
}
\]
and
\[
\boxed{
\frac{d\sigma_L^{\rm vec}}{dc}
=C_0\beta x^2(1-c^2)+O(x^4,r).
}
\]
Both are nonnegative, and the longitudinal contribution vanishes in the massless-vector limit.

Integrating the leading terms gives
\[
\boxed{
\sigma_T^{\rm vec}
=\frac83 C_0\beta
=\frac{8\pi\alpha\alpha_{\mu\tau}}{3m_\mu^2}\beta,
}
\]
\[
\boxed{
\sigma_L^{\rm vec}
=\frac43 C_0x^2\beta
=\frac{4\pi\alpha\alpha_{\mu\tau}}{3m_\mu^2}
\frac{m_{Z'}^2}{E_\gamma^2}\beta.
}
\]
In particular,
\[
\frac{\sigma_L^{\rm vec}}{\sigma_T^{\rm vec}}
=\frac12\frac{m_{Z'}^2}{E_\gamma^2}
+O(x^4,r).
\]
This is the conserved-vector-current hierarchy: transverse production dominates for a light vector.

### 6.1 Comparison with (5.9): not a simple label swap

The paper gives
\[
\sigma_T^{\rm paper}=2C_0x^2\beta,\qquad
\sigma_L^{\rm paper}=\frac83C_0\beta.
\]
The independent physical-projector result gives
\[
\sigma_T^{\rm vec}=\frac83C_0\beta,\qquad
\sigma_L^{\rm vec}=\frac43C_0x^2\beta.
\]
Hence
\[
\sigma_L^{\rm paper}=\sigma_T^{\rm vec},
\qquad
\sigma_T^{\rm paper}=\frac32\sigma_L^{\rm vec}.
\]

The unsuppressed integrated term agrees with the physical transverse result but is assigned to \(L\) in the paper. The suppressed term is assigned to \(T\), and its coefficient is \(3/2\) times the physical longitudinal result. A pure \(T\leftrightarrow L\) relabeling is insufficient.

The angular functions also fail to match: the physical soft-limit shapes are \(1+c^2\) for \(T\) and \(x^2(1-c^2)\) for \(L\), whereas (B.6) gives \(x^2+2c\) and \((1-c)^2-x^2c\). They are not related by a common normalization or a global angular reversal.

## 7. Numerical trace cross-check and precision boundary

The existing vector-current Dirac-trace implementation in ../rates.py uses both Compton diagrams, the physical \(T/L\) basis, and the Ward-equivalent shifted longitudinal polarization. A direct production-amplitude trace was evaluated at
\[
E_\gamma=0.1\ {\rm MeV},\qquad
m_{Z'}=0.01\ {\rm MeV},\qquad x=0.1.
\]
The paper's (B.2) and (B.4) spin sums were compared with the explicit trace. The paper's displayed spin sums are unaveraged over the initial muon spin and photon polarization, whereas the explicit cross section uses the conventional initial-state averages. The expected common ratio is therefore 4.

| \(c\) | (B.2) / explicit \(T\) spin sum | (B.4) / explicit total spin sum |
|---:|---:|---:|
| -0.5 | 4.000061 | 3.999920 |
| 0.0 | 4.000076 | 3.999900 |
| +0.5 | 4.000061 | 3.999920 |

This is a generic-angle consistency check of the transverse and total traces with the expected spin-average convention. It is not proof that the printed (B.1b) ordering is correct. The longitudinal trace obtained by subtracting two larger quantities, (B.3), is numerically more sensitive; it must be checked by direct \(P_L\) contraction or higher-precision arithmetic rather than inferred from the relative agreement of the two large terms.

An independent finite-angle check of the soft limit was made at \(E_\gamma=0.1\) MeV and \(x=0.1,0.3,0.5\). The exact Dirac-trace differential cross sections divided by the leading expressions in Sec. 6 lie between 0.996 and 0.999 over \(c=-0.9,-0.5,0,0.5,0.9\). The residual is consistent with the finite \(E_\gamma/m_\mu\) correction. This supports the analytic leading forms; it is not a full thermal integral.

## 8. Consequences for the supernova-rate construction

1. **The integrated total and the mode decomposition are different questions.** The leading unsuppressed contribution to the total low-energy rate is present in both calculations, but the paper assigns it to \(L\) whereas the conserved-current result assigns it to \(T\). The subleading \(O(x^2)\) term also differs by a factor \(3/2\).
2. **Equation (5.10) inherits the polarization assignment.** Inserting the printed \(\sigma_T,\sigma_L\) separately into production rates does not give the physical vector-current source by mode.
3. **Equation (5.12) does not cure the issue.** Detailed balance relates consistently defined forward and inverse rates. It cannot turn a negative or incorrectly projected differential cross section into a physical one. The \(2/3\) polarization-degeneracy factor must be tracked separately from the mode-resolved kernels.
4. **A polarization-summed leading rate is not enough for transport.** The optical depth and escape probability are evaluated along the mediator trajectory. Incorrectly assigning the dominant rate to the longitudinal mode changes the mode-resolved opacity even when a leading unpolarized total is close.
5. **No empirical correction is authorized.** Do not swap labels, multiply one channel by \(3/2\), rescale the opacity, or replace the published vector benchmark in production transport code on the basis of this note alone.

## 9. Current assessment and remaining work

| Check | Result | Interpretation |
|---|---|---|
| PDF equation numbering | Verified | Use (5.9), (B.1)–(B.6), and (A.15) |
| (B.6) integrated to (5.9) | Pass | Algebraic closure only |
| Pointwise positivity of printed (B.6a,b) | Fail | Both physical components have negative angular regions |
| Conserved-vector Ward identity | Pass for correctly ordered \(u\) channel | Printed (B.1b) appears to reverse the vertex order |
| (B.2)/(B.4) generic-angle trace comparison | Consistent up to initial-state factor 4 | Longitudinal subtraction needs a more stable direct check |
| Soft-muon/light-vector hierarchy | Pass for independent physical projection | \(T=O(1)\), \(L=O(m_{Z'}^2/E_\gamma^2)\) |
| Source of the paper's (5.9)/(B.6) discrepancy | Open | Do not label it a simple typesetting swap |

Next analytic tasks:

1. Re-derive (B.2) and (B.4) from the correctly ordered amplitude and explicit projectors, retaining exact \(m_{Z'}\) and exact two-body kinematics.
2. Compute the longitudinal contribution directly from \(P_L^{\mu\nu}\), not solely as the subtraction (B.3), and compare at high precision.
3. Re-derive the phase-space Jacobian from \(d\sigma/d\cos\theta\) to the integrated cross section, explicitly tracking the common \(\beta\) factor and initial-state averages.
4. Determine whether the discrepancy first enters the trace, polarization projection, angular variable/Jacobian, or final integration.
5. Only after these checks, decide how to describe the source inconsistency in the literature comparison. Keep the published Blinov Fig. 7 reproduction and the physical mode-resolved calculation as separate validation lanes.

**Claim boundary:** this note establishes a source-level inconsistency between the printed polarization-resolved formulas and the conserved-vector-current soft limit. It does not establish a corrected full finite-mass cross section, a global supernova luminosity, or a replacement exclusion curve. The pure-vector Fig. 7 literature gate remains **NOT PASSED**.

## 10. Reproduction references

- Primary source PDF: [arXiv:2610.35379v1](https://arxiv.org/pdf/2610.35379v1), Sec. 5.2 and Appendices A–B.
- Existing physical vector/axial kernels: [../rates.py](../rates.py).
- Existing mode-resolved balance and code audit: [../POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md](../POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md).
- Existing vector/axial response scan: [response_scan.py](response_scan.py).
- Existing response-map rationale: [VECTOR_TO_AXIAL_RESPONSE_MAPPING_2026-11-07.md](VECTOR_TO_AXIAL_RESPONSE_MAPPING_2026-11-07.md).

No production code, CI workflow, manuscript, referee response, or published constraint figure is modified by this document.


## 11. Direct longitudinal-projector follow-up

The direct rank-one longitudinal projection is now evaluated independently. For
\[
q^\mu=(\omega,|\mathbf q|\hat{\mathbf q}),\qquad
\epsilon_L^\mu=\frac{1}{m_{Z'}}(|\mathbf q|,\omega\hat{\mathbf q}),
\]
the conserved vector current obeys \(q_\mu\mathcal M^\mu=0\). Therefore, at amplitude level,
\[
\epsilon_L^\mu\longrightarrow
\widetilde\epsilon_L^\mu
=\epsilon_L^\mu-\frac{q^\mu}{m_{Z'}}
=\frac{m_{Z'}}{\omega+|\mathbf q|}
(-1,\hat{\mathbf q})
\]
is an exact Ward-equivalent representative. The small representative is evaluated before squaring, avoiding the catastrophic cancellation that occurs if the large physical \(\epsilon_L\) components are contracted only after forming a tensor of spin sums. This identity is specific to the conserved pure-vector current and must not be applied to the axial component.

### 11.1 Independent projection checks

A new standalone calculation uses exact two-body kinematics, explicit Dirac spinors, and an independent trace with the Ward-equivalent longitudinal polarization. It scans 36 points:
\[
E_\gamma=(0.05,0.1,0.5,1)\ {\rm MeV},\quad
m_{Z'}/E_\gamma=(10^{-3},10^{-2},10^{-1}),\quad
\cos\theta=(-0.7,0.2,0.8).
\]

| Check | Maximum result |
|---|---:|
| Physical \(\epsilon_L\) vs Ward-equivalent \(\widetilde\epsilon_L\) | \(3.27\times10^{-7}\) |
| Independent trace vs explicit spinor sum | \(8.37\times10^{-11}\) |
| Correct crossed-amplitude Ward residual, relative amplitude | \(1.34\times10^{-14}\) |
| Direct longitudinal positivity | all 36 points positive |

The literal \(u\)-channel ordering printed in (B.1b), with the same gamma-matrix order as the \(s\)-channel, gives a nonzero normalized \(q_\mu\mathcal M^\mu\) amplitude residual between \(1.74\times10^{-2}\) and \(1.06\) on this grid. The crossed ordering \(\gamma^\nu S_u\gamma^\mu\) satisfies the Ward identity. This establishes a source-level ordering inconsistency in the printed (B.1b); it does not establish which ordering the authors used internally to generate their later trace expressions.

### 11.2 The B.3 discrepancy is a recoil-order effect amplified by subtraction

The direct \(P_L\) result is compared with the printed B.2/B.4 spin sums using the same unaveraged initial-muon-spin convention. The B.2 and B.4 individual traces remain close to the exact spinor results, but B.3 is systematically below the direct longitudinal projection. An 80-digit evaluation of the scalar B.2/B.4 subtraction leaves the residual unchanged, so it is not solely floating-point roundoff.

For \(x=m_{Z'}/E_\gamma\ll1\) and \(r=E_\gamma/m_\mu\ll1\), the numerical scan resolves the leading patterns
\[
\frac{B_2^{\rm paper}}{T_{\rm exact}}-1
\simeq \frac{2x^2r}{1+\cos^2\theta},
\qquad
\frac{B_3^{\rm paper}}{L_{\rm direct}}-1
\simeq -\frac{2r}{1-\cos^2\theta}.
\]
These are numerically extracted asymptotic laws; the complete symbolic finite-recoil expansion remains to be derived. At \(x=10^{-3}\) and \(E_\gamma\le0.1\) MeV, their maximum relative fit errors are 0.154% and 0.0921%, respectively.

The reason for the amplification is transparent from
\[
\frac{L_{\rm direct}}{T_{\rm exact}}
\simeq x^2\frac{1-\cos^2\theta}{1+\cos^2\theta}.
\]
The \(O(x^2r)\) transverse residual in B.2 is of the same \(x\)-order as the physical longitudinal signal. When B.2 is subtracted from B.4, it becomes an \(O(r)\) relative bias in B.3. Thus B.3 should not be treated as a precision longitudinal kernel merely because B.2 and B.4 each agree closely with the leading soft-muon result.

### 11.3 Reproducibility and claim boundary

- Calculation: [audit_vector_longitudinal_projector.py](thermal_integrals/audit_vector_longitudinal_projector.py).
- Regression tests: [test_vector_longitudinal_projector.py](thermal_integrals/test_vector_longitudinal_projector.py).
- Machine-readable summary: [vector_longitudinal_direct_projector_summary_2026-11-12.json](thermal_integrals/outputs/vector_longitudinal_direct_projector_summary_2026-11-12.json).

The local acceptance checks pass. These files do not change the production kernel, opacity, thermal integration, transport calculation, manuscript, referee response, or published constraint figure. The pure-vector Blinov Fig. 7 gate remains **NOT PASSED**. The next task is the symbolic derivation of the leading recoil terms and the exact phase-space/Jacobian mapping, not another broad parameter scan.
