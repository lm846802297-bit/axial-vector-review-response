# RC-001 — LD-W-06 secondary scalar shift and heavy-channel audit

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-g/01  
**Status:** both LD-W-06 scalar-line \(-\Delta_W\) terms have been shifted explicitly. The scalar propagator, opposite scalar propagator, internal-W momentum, and actual endpoint currents align with the neighboring common-\(k\) routing, but the heavy momentum changes to \(h-q\) on the A-side and \(h+q\) on the B-side. These shifted heavy denominators are nonzero and distinct from the unshifted three-W heavy denominator at an exact rational point. This is a routing result, not evidence of a physical non-cancellation.

## 1. Why a second shift is needed

For LD-W-06,
\[
h=k-p_1-p_2,\quad \kappa=k+q,
\]
\[
r_A^Y=k-p_2,\quad r_A^W=\kappa-p_2,\quad
r_B^Y=\kappa+p_3,\quad r_B^W=k+p_3.
\]
After the first common-\(k\) routing, the A scalar-line WTI contains
\[
\delta_A=\Delta_{AY}(k)-\Delta_{AW}(k),
\]
and the B scalar-line WTI contains
\[
\delta_B=\Delta_{BY}(k)-\Delta_{BW}(k).
\]
The \(-\Delta_W\) terms can be aligned with the neighboring scalar propagator only after a second loop-variable shift. That second shift acts on every factor, including the heavy propagator and both scalar currents.

## 2. A-side \(-\Delta_{AW}\) term

Set
\[
k_A'=k+q.
\]
Then
\[
\begin{aligned}
\kappa(k)&=k_A',&
r_A^W(k)&=r_A^Y(k_A'),\\
r_B^Y(k)&=r_B^W(k_A'),&
V_A^{\rm line}(k)&=V_A^{3W}(k_A'),\\
V_B^{3W}(k)&=V_B^{\rm line}(k_A').
\end{aligned}
\]
But the heavy channel transforms as
\[
\boxed{h(k)=h(k_A')-q.}
\]
Consequently, the A-side negative-propagator term has the shifted heavy denominator
\[
\boxed{(h(k_A')-q)^2-M_E^2,}
\]
not \(h(k_A')^2-M_E^2\).

Its denominator factors map as
\[
\kappa^2(r_B^Y)^2(r_A^W)^2(h^2-M_E^2)
\longrightarrow
(k_A')^2(r_B^W(k_A'))^2(r_A^Y(k_A'))^2
((h(k_A')-q)^2-M_E^2).
\]

## 3. B-side \(-\Delta_{BW}\) term

Set
\[
k_B'=k-q,\qquad k=k_B'+q.
\]
Then
\[
\begin{aligned}
k&=\kappa(k_B'),&
r_A^Y(k)&=r_A^W(k_B'),\\
r_B^W(k)&=r_B^Y(k_B'),&
V_A^{3W}(k)&=V_A^{\rm line}(k_B'),\\
V_B^{\rm line}(k)&=V_B^{3W}(k_B').
\end{aligned}
\]
The heavy channel instead transforms as
\[
\boxed{h(k)=h(k_B')+q.}
\]
Thus the B-side negative-propagator term carries
\[
\boxed{(h(k_B')+q)^2-M_E^2.}
\]
Its denominator factors map as
\[
k^2(r_A^Y)^2(r_B^W)^2(h^2-M_E^2)
\longrightarrow
\kappa(k_B')^2(r_A^W(k_B'))^2(r_B^Y(k_B'))^2
((h(k_B')+q)^2-M_E^2).
\]

## 4. Exact heavy-denominator comparison

The three heavy denominators are related by
\[
\begin{aligned}
H_0&=h^2-M_E^2,\\
H_A&=(h-q)^2-M_E^2
=H_0+q^2-2h\cdot q,\\
H_B&=(h+q)^2-M_E^2
=H_0+q^2+2h\cdot q.
\end{aligned}
\]
They are not identical for generic off-shell momenta. At the exact rational diagnostic point
\[
\begin{aligned}
k&=(6,1,0,1),&q&=(1,1,0,0),\\
p_1&=(1,0,1,0),&p_2&=(0,2,0,1),\\
p_3&=(2,0,1,0),&M_E^2&=400,
\end{aligned}
\]
one obtains
\[
h=(5,-1,-1,0),\quad h^2=23,
\]
\[
\boxed{H_0=-377,\qquad H_A=-389,\qquad H_B=-365.}
\]
All W and scalar denominator factors in the two shifted terms are nonzero. The exact maps and these three distinct heavy denominators are checked by the standalone SymPy source.

## 5. Interpretation

The earlier common-\(k\) endpoint maps correctly align the original A/B scalar-line subgraphs with their respective three-W routing. The additional shifts needed to expand the \(-\Delta_W\) pieces are different:
- A-side: \(k\to k+q\), with \(h\to h-q\);
- B-side: \(k\to k-q\), with \(h\to h+q\).

Therefore one must not shift only the scalar denominator while leaving the heavy propagator, the opposite scalar current, or the other endpoint momentum unchanged. Nor can these terms be identified pointwise with the unshifted \(h\)-channel three-W integrand.

This does **not** establish a nonzero physical remainder. The shifted heavy-channel terms must be compared with the corresponding Yukawa-endpoint gauge variations and the reducible external-leg/LSZ contributions. The existing local Yukawa-singlet charge test was performed at the first common-\(k\) routing; the secondary \(h\pm q\) maps are now an explicit additional input for extending that test.

## 6. Reproduction and boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_06_secondary_shift_heavy_channel_audit.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-06-secondary-shift-heavy-channel-audit.txt\`

The source checks 16/16 vector components for each secondary shift, four current/propagator factor maps on each side, and both generic heavy-denominator identities. This is a local exact SymPy result, not a GitHub Actions result.

No complete ordinary-matter Ward sum, external-leg/LSZ cancellation, ghost/ST closure, loop integration, UV–EFT subtraction, or Wilson coefficient is claimed.
