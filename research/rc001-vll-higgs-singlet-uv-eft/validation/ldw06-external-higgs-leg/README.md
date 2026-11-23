# LD-W-06 reducible external Higgs emission

One external $W^a(q)$ attaches to $H(p_2)$ **outside** the fixed ordered LD-W-06 $H$–$H^\dagger$ four-point box. Cutting the $H$ propagator between this vertex and the box separates the graph. The prior [ordered internal subset](../ldw06-ordered-kernel/README.md) and the frozen archive are unchanged. This is one explicit contribution to gate 7 of the [assembly ledger](../../upstream/research/RC-001-dim6-WW-fivepoint-common-k-ordinary-matter-assembly-ledger.md), not another internal Ward insertion or a new local EFT contact.

## Four-point amplitude and sewing

Use the [frozen all-incoming order](../../upstream/research/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.md) $(\bar L_i(p_1),H_j(p_2),H^\dagger_k(p_3),L_l(p_4),W^a(q))$, with $p_4=-p_1-p_2-p_3-q$. The bare $WHH^\dagger$ vertex, with scalar momenta $p_2$ and $-P$, has $P=p_2+q$ by conservation and current $w^\alpha=(2p_2+q)^\alpha$. Thus the shifted lower-point arguments are $(p_1,P,p_3,p_4)$ and they sum to zero. Write $\ell$ for the single internal W loop momentum in this four-point seed and use the archived metric $+---$, phases, and final chiral projector $P_L$.

The reduced lower-point box integrand, including the actual light and heavy numerators and denominators but omitting its weak tensor and overall phase, is
$$
F_{06}(\ell;p_1,P,p_3)=
\frac{(2P-\ell)\cdot(-2p_3-\ell)\ \slashed H_E P_L}
{\ell^2\,(\ell-P)^2\,(\ell+p_3)^2\,(H_E^2-M_E^2)},\qquad
H_E=\ell-p_1-P.
$$
It follows directly from the [oriented numerator and phase record](../../upstream/research/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.md) §§1–2,6. The chirality projection removes the heavy mass numerator, not the shifted mass denominator. No loop-momentum or $1/M_E$ expansion is made.

The phase is $P_4=-g_2^2|y_\ell|^2$; the seed weak tensor is $T_{AB}=-T_3/4$, with $T_{3,ijkl}=2\delta_{il}\delta_{kj}-\delta_{ij}\delta_{kl}$ in the [frozen physical external-slot basis](../../upstream/research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md). Sewing the radiation vertex on the *external side* inserts $Z_A^a=(R_H^a T_{AB})_{ijkl}$: literally $\sum_{m,b}t^a_{jm}t^b_{mi}(-t^{bT})_{kl}$ in that basis. This is the order of the tilded weak tensor when written in the notation of the frozen internal bridge; it is not the ordered A-line tensor $R_H^bR_H^aR_{H^\dagger}^b T_0$, nor does it add a second internal diagram.

The extra scalar propagator $i/P^2$ times the vertex $+ig_2$ gives the relative minus. With the original $H(p_2)$ leg amputated,
$$
\begin{aligned}
{\cal E}_{H,\mathrm{amp}}^{a,\alpha}
  &=-g_2 P_4\, Z_A^a\,\frac{(2p_2+q)^\alpha}{P^2}\,F_{06}(\ell;p_1,P,p_3),\\
q_\alpha{\cal E}_{H,\mathrm{amp}}^{a,\alpha}
  &=-g_2 P_4\,Z_A^a\left(1-\frac{p_2^2}{P^2}\right)F_{06}(\ell;p_1,P,p_3).
\end{aligned}
$$
Restoring **only** the original external Higgs propagator $i/p_2^2$, with other external propagators still stripped, gives a contracted factor $-ig_2(1/p_2^2-1/P^2)$ multiplying $P_4 Z_A^a F_{06}$. This implements the [1PI/1PR boundary](../../upstream/research/RC-001-dim6-WW-fivepoint-1PI-vs-1PR-LSZ-boundary.md) with the actual lower-point amplitude. The term $p_2^2/P^2$ must remain off shell. At $p_2^2=0$ with $P^2\neq0$ it drops out *after* amputation; this is a scalar mass-shell check only, not a field-strength or complete LSZ calculation.

## Comparison to the internal common-$k$ bookkeeping

To express this same integrand with $\ell=k+q=\kappa$, its denominators become $\kappa^2 (k-p_2)^2(\kappa+p_3)^2(h^2-M_E^2)$, with $h=k-p_1-p_2$. Its numerator uses $V_A=2p_2-k+q$ and $V_B=-2p_3-\kappa$. The ordered [internal scalar-line A graph](../../upstream/research/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.md) instead uses $V_A^{\rm line}=2p_2-k-q$. Hence matching selected propagator arguments does **not** license copying the internal current or the weak order into this external graph. The two representations of the external graph evaluate at relabelled arguments; no equal-integral claim between different graphs is made.

## Local checks

[check.py](check.py) constructs vertex momenta from conservation, sews the explicit indices and factors of $i$, and compares against the factorized amplitude. On three exact rational points it passes **9,216/9,216** uncontracted and **2,304/2,304** contracted amputated Lorentz/weak/Dirac matrix entries. The two off-shell points additionally pass **1,536/1,536** with the external scalar propagator present; the third point has precisely the scalar mass-shell projection (**768** entries, included among the contracted checks). The controls reject the wrong weak order, using the unshifted heavy propagator at fixed $\ell$, using the internal A current instead of this one, and dropping the relative minus. Dropping the external inverse-propagator term fails off shell, and correctly has no effect after the scalar mass-shell projection.

Replay from this folder: `sha256sum -c SHA256SUMS`, then `python -B check.py | cmp - native.json`. The immutable input blob and SHA-256 pins are in [provenance.json](provenance.json); no GitHub CI was run.

This validates one reducible Higgs emission on the actual LD-W-06 box only. The companion emissions, complete wavefunction normalization and counterterms, full Ward/LSZ/STI assembly, regulator-governed integration, UV–EFT subtraction, and Wilson coefficients remain open.
