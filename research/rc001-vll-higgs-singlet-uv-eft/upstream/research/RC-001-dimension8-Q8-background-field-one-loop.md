# RC-001 — Q8 one-loop background-gauge-field soft matching

**Status (2026-11-10):** loop-counting correction and exact formal background-field expansion recorded. This is a one-loop EFT functional with zero, one, or two external background gauge fields. The corresponding momentum-space loop integrals, UV poles, Ward identities, and UV hard partners have not yet been evaluated.

## 1. Scope and loop-counting distinction

For
\[
Q_{a,\ell}^{(8)}=\bar\Psi_{a,\ell}(i\slashed D_a)^3\Psi_{a,\ell},
\quad
\Psi_{L,\ell}=H^\dagger L_\ell,\quad
\Psi_{R,\ell}=S_\ell\ell_R,
\]
consider the one-loop functional linear in the dimension-eight coefficient \(c_{a,\ell}^{(8)}\), in a prescribed external background gauge field \(A_\mu\).

External background gauge legs do not add independent loop momenta. The following are all one-loop objects:
- zero external gauge legs: the pure Q8 fermion contraction;
- one external gauge leg: the background-field three-point response;
- two external gauge legs: the background-field four-point response, including the Q8 contact vertices.

By contrast, contracting two gauge fields with an internal quantum-gauge propagator adds a gauge momentum and produces a two-loop EFT contribution. That is a separate correction to a chosen Green function, for example the scalar two-point function. Do not conflate the one-loop background-field functional with this two-loop internal-gauge correction.

## 2. Exact formal expansion

Write the background-covariant fermion operator as
\[
\mathscr D_A=\mathscr D_0+V_A,\qquad S_0=\mathscr D_0^{-1},
\]
and expand the Q8 insertion itself as
\[
\mathcal V_8[A]=
\mathcal V_8^{(0)}+\mathcal V_8^{(1)}[A]
+\mathcal V_8^{(2)}[A,A]+\cdots.
\]
The notation \(\mathcal V_8^{(n)}\) includes the full ordered expansion of \((i\slashed D_A)^3\), with the scalar backgrounds and their momenta retained. It includes all derivative and field-strength terms; it is not a commuting replacement \(D\to\partial-igA\) applied to each factor independently.

The term linear in \(c_8\) in the one-loop fermion functional is, up to the global sign/\(i\) fixed by the chosen Minkowski effective-action convention,
\[
\Gamma_8^{(1)}[A]\propto
\operatorname{Tr}\left[(\mathscr D_0+V_A)^{-1}\mathcal V_8[A]\right].
\]
Using
\[
(\mathscr D_0+V_A)^{-1}
=S_0-S_0V_AS_0+S_0V_AS_0V_AS_0+\cdots,
\]
the background-field sectors are
\[
\Gamma_8^{(1,0)}\propto
\operatorname{Tr}(S_0\mathcal V_8^{(0)}),
\]
\[
\Gamma_8^{(1,1)}\propto
\operatorname{Tr}\left[
S_0\mathcal V_8^{(1)}
-S_0V_AS_0\mathcal V_8^{(0)}
\right],
\]
\[
\Gamma_8^{(1,2)}\propto
\operatorname{Tr}\left[
S_0\mathcal V_8^{(2)}
-S_0V_AS_0\mathcal V_8^{(1)}
+S_0V_AS_0V_AS_0\mathcal V_8^{(0)}
\right].
\]
Each trace has one independent loop momentum. The three terms in the two-background sector are respectively: the quadratic Q8 contact vertex, one ordinary gauge vertex plus one linear Q8 contact vertex, and two ordinary gauge vertices on the fermion loop. They must be summed with common momentum routing and a common regulator.

This expansion is the useful bookkeeping identity for the one-loop calculation. It does not yet provide the momentum-space vertex polynomials or the evaluated loop integrals.

## 2A. Explicit one-background contact vertex

The frozen model convention is \(D_\mu=\partial_\mu-i g_YYB_\mu-i g_XQ_XA'_\mu+\cdots\). For a composite source with charges \(q_{\Psi,A}\), let \(P'=P+q\) be the source momentum after an incoming background gauge field of momentum \(q\). The exact linear contact vertex from the ordered cubic operator is
\[
V_{8,A}^{\mu}(P',P)
=g_Aq_{\Psi,A}
\left[\slashed P'^{\,2}\gamma^\mu+
\slashed P'\gamma^\mu\slashed P+
\gamma^\mu\slashed P^{\,2}\right].
\]
Contracting in the actual noncommuting matrix order gives
\[
q_\mu V_{8,A}^{\mu}
=g_Aq_{\Psi,A}
\left[
\slashed P'^{\,2}\slashed q+
\slashed P'\slashed q\slashed P+
\slashed q\slashed P^{\,2}
\right]
=g_Aq_{\Psi,A}(\slashed P'^{\,3}-\slashed P^{\,3}).
\]
This is the contact-vertex Ward identity. It is not yet the full one-loop Green-function Ward identity: the ordinary background insertion on the light-fermion propagator and the scalar-source charge flow must also be included.

For QLD and QRD, the direct contacts are \(B_\mu:-g_Y\), \(A'_\mu:+\eta_\ell g_XQ_\ell\), and \(W_\mu^a:0\). The ordinary W insertion on the L constituent line remains in QLD.

The symbolic noncommuting-slash check is in calculations/RC-001-dimension8-Q8-one-background-vertex-audit.py; its recorded output is validation/RC-001-dimension8-Q8-one-background-vertex-audit.txt.

## 3. Required one-loop amplitudes

For each flavor and gauge factor, calculate:

1. \(\Gamma_8^{(1,0)}\): zero-background-gauge sector. The already checked gauge-free massless scalar tadpole is scaleless and vanishes for its restricted two-scalar projection.
2. \(\Gamma_8^{(1,1)}\): one external background gauge field. Retain all momenta on the scalar legs and gauge leg; extract the independent transverse/local form factors after imposing the background Ward identity.
3. \(\Gamma_8^{(1,2)}\): two external background gauge fields. Include both ordinary fermion-line insertions and the linear/quadratic covariant Q8 contacts, as well as the explicit field-strength pieces from the exact ordered operator identity.

These are one-loop soft Green functions. They are not obtained by closing the two gauge legs into a propagator. That contraction is a distinct two-loop calculation.

## 4. Representation bookkeeping

The frozen source representations are
\[
\Psi_{L,\ell}=H^\dagger L_\ell:
(\mathbf1,Y=-1,x=\eta_\ell),\qquad
\Psi_{R,\ell}=S_\ell\ell_R:
(\mathbf1,Y=-1,x=\eta_\ell),
\]
where \(\eta_\mu=+1,\eta_\tau=-1\) and \(x=Q_X/Q_\ell\). Thus the connection at the composite Q8 insertion contains hypercharge \(B_\mu\) and \(A'_\mu\), but no direct \(W_\mu^I\) generator.

This does not remove \(W\) attachments to the separate \(L_\ell\) and \(H\) constituent lines in the full \(Q_{LD}\) amplitude. \(Q_{RD}\) has no \(W\) attachments because both constituents are SU(2) singlets.

## 5. Ward identities and UV subtraction

The one-background and two-background amplitudes must be derived from the same background-gauge-covariant functional. Check the one-gauge Ward identity and the two-gauge Ward identity (or Slavnov–Taylor identities when non-Abelian quantum fields are introduced) only after summing all ordinary and contact contributions.

Keep nonzero external momenta until UV and IR poles are separated. Reduce the local UV pole to a gauge-invariant Green basis, retaining EOM/source operators. Match this one-loop soft UV pole only against the one-loop hard region of the same external Green function and same perturbative order.

The background-field Ward identities do not by themselves evaluate or eliminate the two-loop diagrams obtained by contracting external background legs with internal gauge propagators.

## 6. Explicit acceptance boundary

Completed:
- corrected loop-counting distinction between external background gauge fields (one loop) and internal gauge exchange (two loops);
- formal expansion of the one-loop fermion functional through two external background gauge fields;
- identification of the three required terms in each sector and their relative resolvent-expansion signs.

Open:
- explicit momentum-space Q8 one- and two-background vertices;
- evaluated one-loop integrals for \(Q_{LD}^{(8)}\) and \(Q_{RD}^{(8)}\);
- summed Ward identities and local UV poles;
- one-loop UV hard partners and finite matching;
- EOM/IBP reduction to the common nonredundant basis;
- numerical Benchmark A/B cross-check.

No one-loop Q8 background-field coefficient, counterterm, or matched Wilson coefficient is claimed by this setup note.
