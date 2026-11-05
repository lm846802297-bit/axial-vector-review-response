# Portal-induced scalar-loop power counting: P2-lite

- Date: 2026-11-05
- PR: #49, Major Point 1.3
- Scope: original one-singlet \(S+\mathrm{VLL}\) model only; no neutrino-sector extension.
- Status: **CP-even radial-scalar subset derived and numerically evaluated; complete two-loop UV--EFT matching is not claimed.**
- Reproduction: [portal_scalar_loop_power_counting_2026-11-05.py](portal_scalar_loop_power_counting_2026-11-05.py)

## 1. Decision for the referee response

The calculation supports a more precise statement of the perturbative order, but it does **not** justify describing all scalar-loop effects as numerically negligible. The UV portal is itself fixed to a one-loop-sized VLL threshold. A CP-even scalar-potential bubble with one portal cubic and one ordinary Higgs/singlet cubic is therefore next order in the combined counting. Its finite momentum-dependent subset can be larger than the already-subtracted leading fermionic \(\Pi_{hs}^{\mathrm{ret}}\), because the latter is numerically small after local matching/subtraction.

Accordingly:

1. Put the cubic vertices, the CP-even bubble formula, and the combined loop-order statement in the referee response.
2. Do **not** put the raw CP-even subset numbers into the referee response as if they were a physical two-loop correction. They are not a complete matched/gauge-complete result.
3. Keep the non-degenerate Higgs comparison as a leading-order, isolated-pole diagnostic, not as a full pole prediction.
4. Keep the near-degenerate region explicitly unassessed. The subset diagnostic reinforces that no physical near-degenerate conclusion should be inferred from the present leading fermionic result.

This follows the repository writing rule: include the necessary physical qualification, but do not expose internal task status or present an incomplete calculation as a completed physical prediction.

## 2. Scalar potential and cubic vertices

Use
\[
V(H,S)\supset
\lambda_H(H^\dagger H)^2+
\lambda_S(S^\dagger S)^2+
\lambda_{HS}^{\mathrm{UV}}(H^\dagger H)(S^\dagger S),
\]
with
\[
H^0=\frac{v_h+h}{\sqrt2},\qquad
S=\frac{v_s+s+ia}{\sqrt2}.
\]
The matched reference is
\[
\lambda_{HS}^{\mathrm{EFT}}(M_E)=0,\qquad
\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}>0.
\]
The benchmark values reproduced from the Plan-C-lite inputs are
\[
\lambda_{HS}^{\mathrm{UV}}=
\begin{cases}
0.2107639762,& A,\\
0.01067337649,& B.
\end{cases}
\]
The Higgs quartic is
\[
\lambda_H=\frac{m_h^2}{2v_h^2}=0.1293834774,
\]
and \(\lambda_S=m_s^2/(2v_s^2)\).

The CP-even cubic potential derivatives are
\[
g_{hhh}=6\lambda_Hv_h,\qquad
g_{sss}=6\lambda_Sv_s,\qquad
g_{hhs}=\lambda_{HS}^{\mathrm{UV}}v_s,\qquad
g_{hss}=\lambda_{HS}^{\mathrm{UV}}v_h.
\]

## 3. CP-even radial-scalar bubble subset

For real cubic couplings and diagonal reference propagators with masses \(m_h,m_s\), the three one-loop CP-even bubble topologies are:

- \(hh\) internal: \(g_{hhh}\,g_{hhs}\);
- \(ss\) internal: \(g_{hss}\,g_{sss}\);
- mixed \(hs\) internal: \(g_{hhs}\,g_{hss}\), with the two orderings included.

Define the finite zero-momentum-subtracted function
\[
\Delta B_{ij}\equiv
B_0(m_h^2;m_i^2,m_j^2)-B_0(0;m_i^2,m_j^2)
=-\int_0^1dx\,
\ln\left[
1-\frac{x(1-x)m_h^2}
{x m_i^2+(1-x)m_j^2}
\right],
\]
for the selected points below all corresponding two-scalar thresholds. The CP-even subset is
\[
\boxed{
\Delta\Pi_{hs}^{(h,s)\,\mathrm{subset}}
=\frac{1}{32\pi^2}\left[
g_{hhh}g_{hhs}\Delta B_{hh}
+g_{hss}g_{sss}\Delta B_{ss}
+2g_{hhs}g_{hss}\Delta B_{hs}
\right].
}
\]
Equivalently,
\[
\Delta\Pi_{hs}^{(h,s)\,\mathrm{subset}}
=\frac{\lambda_{HS}^{\mathrm{UV}}v_hv_s}{32\pi^2}
\left[
6\lambda_H\Delta B_{hh}
+6\lambda_S\Delta B_{ss}
+2\lambda_{HS}^{\mathrm{UV}}\Delta B_{hs}
\right].
\]
The overall sign changes if the opposite self-energy convention is adopted; the numerical comparisons below use magnitudes and are not added coherently to \(\Pi_{hs}^{\mathrm{ret}}\).

The first two terms contain one portal insertion and one ordinary scalar cubic. Since \(\lambda_{HS}^{\mathrm{UV}}\) is itself chosen at the one-loop VLL-threshold order, these terms are next order in the combined counting. The mixed term has two portal insertions and is one order further in that counting.

## 3.1 Closed forms and independent numerical cross-check

The Feynman-parameter representation above is exact. For the sub-threshold benchmark points, all three bubble functions also admit real closed forms.

Write \(s=p^2\), \(a=m_i^2\), \(b=m_j^2\), and
\[
\Delta B_0(s;a,b)
=-\int_0^1 dx\,
\ln\!\left[1-\frac{x(1-x)s}{xa+(1-x)b}\right].
\]

For equal internal masses \(a=b=m^2\),
\[
\boxed{
\Delta B_0(s;a,a)
=2-2\sqrt{\frac{4a}{s}-1}\,
\arctan\!\left(\frac{1}{\sqrt{4a/s-1}}\right),
\quad 0<s<4a.
}
\]

For unequal internal masses, define
\[
\Lambda=(s-a-b)^2-4ab,\quad
q=\frac{\sqrt{-\Lambda}}{2s},\quad
t_0=\frac{a-b-s}{2s},\quad t_1=t_0+1,
\]
\[
G(t)=t\ln\!\left[\frac{s(t^2+q^2)}{\mu_0^2}\right]
-2t+2q\arctan(t/q),
\]
\[
I_0(a,b;\mu_0)=
\frac{a\ln(a/\mu_0^2)-b\ln(b/\mu_0^2)}{a-b}-1.
\]
Then
\[
\boxed{
\Delta B_0(s;a,b)=I_0(a,b;\mu_0)-[G(t_1)-G(t_0)],
\quad a\ne b,\quad \Lambda<0.
}
\]
The arbitrary reference scale \(\mu_0\) cancels. The benchmark evaluations all lie on this real branch. The \(hh\) and \(ss\) functions use the equal-mass expression; the \(hs\) function uses the unequal-mass expression.

### Closed form versus Simpson integration

The standard-library script now evaluates the bubble functions from the closed forms and independently compares them with 8,000-interval composite Simpson integration. The unique function values are:

| Bubble | Internal masses | Closed form | Simpson, \(n=8000\) | Relative difference |
|---|---|---:|---:|---:|
| \(hh\) | \(125.25,125.25\) GeV | 0.186200635765782 | 0.186200635765782 | \(1.2\times10^{-15}\) |
| \(ss\) | \(100,100\) GeV | 0.315060125853570 | 0.315060125853571 | \(5.3\times10^{-16}\) |
| \(hs\) | \(125.25,100\) GeV | 0.236692107871086 | 0.236692107871088 | \(1.0\times10^{-14}\) |
| \(ss\) or \(hs\) at \(m_s=m_h\) | \(125.25,125.25\) GeV | 0.186200635765782 | 0.186200635765782 | \(1.2\times10^{-15}\) |

These values are independent of whether benchmark A or B is selected; the benchmarks enter through \(v_s\), \(\lambda_{HS}^{UV}\), and \(\lambda_S\), not through the loop functions at fixed masses. The script checks all 12 benchmark/mass/topology combinations. The maximum closed-form versus Simpson relative difference is below \(10^{-14}\), while the separate 2k/4k/8k/16k convergence test remains satisfied.

## 4. Goldstone, tadpole, and VEV bookkeeping

The Goldstone interactions are also fixed by the same potential. For each of the three real Goldstones in the Higgs doublet,
\[
g_{hG_HG_H}=2\lambda_Hv_h,\qquad
g_{sG_HG_H}=\lambda_{HS}^{\mathrm{UV}}v_s.
\]
For the \(U(1)_X\) Goldstone \(a\),
\[
g_{haa}=\lambda_{HS}^{\mathrm{UV}}v_h,\qquad
g_{saa}=2\lambda_Sv_s.
\]
In an \(R_\xi\) gauge their bubble terms have the same \(\Delta B_0\) structure, with \(m_{G^\pm}^2=\xi_Wm_W^2\), \(m_{G^0}^2=\xi_Zm_Z^2\), and \(m_a^2=\xi_Xm_{A'}^2\).

These Goldstone terms are **not** numerically added to the CP-even table. A Goldstone-only sum is gauge-parameter dependent; a physical pole calculation requires the associated gauge-boson/ghost contributions and a consistent tadpole/VEV prescription. The \(W,Z,A'\) and top-loop effects induced by portal mixing also enter the same higher-order completion and cannot be inferred from the scalar-only subset.

The portal quartic contains \(h^2s^2\). Its two-point tadpole contraction requires an off-diagonal internal \(h\)-\(s\) propagator; it vanishes for the diagonal matched-reference propagators used in this subset. If an off-diagonal mass insertion is retained, this tadpole is of higher order and is momentum independent. Tadpole and VEV counterterms are likewise local. They cancel in the displayed \(\Pi(m_h^2)-\Pi(0)\) difference, but they must be included in a complete un-subtracted mass/pole renormalization.

Thus the subtraction above removes the local constant of this **diagram subset**; it is not a complete two-loop hard/soft UV--EFT matching calculation.

## 5. Numerical inputs and results

Inputs follow the current Plan-C-lite benchmarks:
\[
M_E=20~\mathrm{TeV},\quad
\theta_{\ell L}=10^{-2},\quad
v_h=246.22~\mathrm{GeV},\quad
m_h=125.25~\mathrm{GeV}.
\]
The two \(v_s,m_{A'}\) points are:
\[
(A):\ (v_s,m_{A'})=(70.8864580,10)~\mathrm{GeV},
\qquad
(B):\ (v_s,m_{A'})=(315,63)~\mathrm{GeV}.
\]

### 5.1 Momentum-subtracted CP-even bubble results

All entries below are in \(\mathrm{GeV}^2\). The hh, ss, and hs columns are the three terms in the boxed expression.

| \(m_s\) | Benchmark | \(hh\) | \(ss\) | mixed \(hs\) | \(|\Delta\Pi_{hs}^{(h,s)\,\mathrm{subset}}|\) |
|---:|:---:|---:|---:|---:|---:|
| 100 GeV | A | 1.68362 | 21.90894 | 1.16210 | 24.75466 |
| 100 GeV | B | 0.378876 | 0.249678 | 0.013244 | 0.641797 |
| 125.25 GeV | A | 1.68362 | 20.31256 | 0.914199 | 22.91038 |
| 125.25 GeV | B | 0.378876 | 0.231485 | 0.010418 | 0.620779 |

For \(m_s=100\) GeV,
\[
\frac{|\Delta\Pi_{hs}^{(h,s)\,\mathrm{subset}}|}
{|\Pi_{hs}^{\mathrm{ret}}|}
=
57.77\quad(A),\qquad 6.656\quad(B),
\]
where the retained leading fermionic values are
\[
\Pi_{hs}^{\mathrm{ret}}=
\begin{cases}
-0.413277859-0.113173709i~\mathrm{GeV}^2,&A,\\
-0.093002551-0.025468201i~\mathrm{GeV}^2,&B.
\end{cases}
\]
This ratio is a diagnostic of the relative size of two separately defined pieces. It is **not** a statement that the scalar subset is a physical correction larger than the leading result: the required same-order matching terms have not been combined, and the relative sign is convention-dependent.

### 5.2 Isolated-pole scale diagnostic at \(m_s=100\) GeV

Using the Plan-C-lite diagonal widths, \(\Gamma_s=1.8668349\) GeV (A) and \(0.1268113\) MeV (B), define only for comparison
\[
\eta_{\mathrm{subset}}\equiv
\frac{|\Delta\Pi_{hs}^{(h,s)\,\mathrm{subset}}|}
{|(m_h^2-im_h\Gamma_h)-(m_s^2-im_s\Gamma_s)|}.
\]
The values are
\[
\eta_{\mathrm{subset}}=4.3501\times10^{-3}\quad(A),
\qquad
1.1284\times10^{-4}\quad(B).
\]
If each subset were inserted alone into the isolated-pole weak-mixing estimate, the corresponding \(\eta_{\mathrm{subset}}^2\) scales would be \(1.89\times10^{-5}\) and \(1.27\times10^{-8}\), respectively. Both are below the approximately \(5.3\%\) inclusive Higgs signal-strength precision, but these are **subset-only scale comparisons**, not physical rate predictions or exclusion limits. They must not be added to the existing fermionic rate shifts.

### 5.3 Exact diagonal-mass degeneracy

At \(m_s=m_h=125.25\) GeV, using the same fixed-width denominator solely as a diagnostic gives
\[
\eta_{\mathrm{subset}}=0.04887\quad(A),
\qquad
1.2673\quad(B).
\]
For B the first-order isolated-pole expansion is plainly invalid. These numbers are not a pole solution and do not define an allowed or excluded interval. They reinforce the decision to leave the near-degenerate narrow-width region unclassified until the complete matched self-energy and pole residues/lineshape are available.

## 6. What this calculation does and does not establish

**Established**
- The cubic vertices and all three CP-even radial bubble topologies follow directly from the scalar potential.
- The finite \(B_0(m_h^2)-B_0(0)\) differences are numerically converged.
- The CP-even radial subset is formally higher order in the joint counting because \(\lambda_{HS}^{\mathrm{UV}}\) is fixed at the one-loop VLL-threshold order.
- At the non-degenerate \(m_s=100\) GeV point, the subset-only mixing scale is still below current inclusive Higgs signal-strength precision.

**Not established**
- A complete gauge-independent scalar-plus-gauge two-loop correction.
- The full two-loop UV--EFT threshold, including mixed VLL-scalar diagrams and all matching counterterms.
- A complete physical pole/residue/lineshape prediction in the near-degenerate region.
- A model-specific LHC likelihood or a global allowed/excluded scalar-mass interval.

The correct referee-facing conclusion is therefore: the leading fermionic calculation is a leading-order benchmark diagnostic; the portal-induced scalar-potential terms are higher order, but the isolated subset is not sufficient to claim they are uniformly negligible. The near-degenerate region remains unassessed.

## 7. Validation

The accompanying standard-library Python script:
- derives \(\lambda_{HS}^{\mathrm{UV}}\) from the same VLL-threshold formula used in Plan C-lite;
- evaluates all three \(\Delta B_0\) functions using composite Simpson integration;
- checks convergence at 2,000, 4,000, 8,000 and 16,000 intervals;
- reproduces the table and the width-regulated diagnostic values.

The script is intentionally limited to the CP-even radial subset. It does not silently label this subset as the full scalar-loop correction.
