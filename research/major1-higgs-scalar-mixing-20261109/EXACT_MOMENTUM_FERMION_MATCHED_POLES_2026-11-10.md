# Major Point 1 — exact-momentum fermion hard matching in the complex-pole diagnostic

> Numerical review (2026-11-15): a current rerun of the exact-momentum pole driver emitted a SciPy integration roundoff warning. The quoted pole-based quantities need integral convergence/error verification before their displayed precision is relied on; see [the audit](../../docs/repository-management/TWENTY_NINTH_REVIEW_POLE_AND_RGE_OUTPUTS_2026-11-15.md).

**Purpose:** replace the leading-derivative hard approximation in Plan-C-lite by the exact momentum-dependent one-loop fermion-sector hard remainder, while retaining the same explicit limitations on diagonal widths and missing sectors.

For each charged-lepton family, the exact \(2\times2\) mass matrix is diagonalized by an SVD. The full \(hh,hs,ss\) fermion-loop kernels use all four internal mass-eigenstate pairings. For the off-diagonal entry define the finite momentum-dependent hard remainder
\[
\Delta\Pi_{hs}^{\rm hard}(s)=
[\Pi_{hs}^{\rm full}(s)-\Pi_{hs}^{\rm full}(0)]
-
[\Pi_{hs}^{\rm light}(s)-\Pi_{hs}^{\rm light}(0)].
\]
The EFT light-light bubble and the dimension-five \(hs\bar\ell\ell\) contact tadpole are then retained explicitly:
\[
\Pi_{hs}^{\rm matched}(s)=
\Pi_{hs}^{\rm light}(s)+\Pi_{hs}^{\rm contact}
+\Delta\Pi_{hs}^{\rm hard}(s).
\]
The portal constant is a separate matching input and is not added again. The B0 functions are evaluated from their Feynman-parameter representation with the resonance-sheet continuation for open light-lepton cuts.

## Numerical cross-check

At \(s=m_h^2\), the exact hard remainders reproduce the independently archived mass-eigenstate values:
\[
\Delta\Pi_{hs}^{\rm hard}(m_h^2)=
\begin{cases}
0.0240304439859~{\rm GeV}^2 &(A),\\
0.00540772399471~{\rm GeV}^2 &(B).
\end{cases}
\]
This agrees with the previous leading-derivative hard approximation at the quoted point, but the present implementation retains the full \(s\)-dependence rather than extrapolating a linear term.

The exact-light EFT bubble plus contact gives
\[
\Pi_{hs}^{\rm matched}(m_h^2)=
\begin{cases}
-0.4131216491-0.1131333101i~{\rm GeV}^2 &(A),\\
-0.0929673982-0.02545910995i~{\rm GeV}^2 &(B).
\end{cases}
\]
The small difference from the earlier Plan-C-lite soft values comes from replacing leading mass-proportional light couplings by the exact SVD light-state couplings.

## Complex poles and residues

Using the same diagonal inputs as Plan-C-lite (SM Higgs width fixed to 4.07 MeV; singlet width restricted to \(A'A'\), \(\mu\mu\), \(\tau\tau\); diagonal real self-energies absorbed into the mass inputs), the exact-momentum matched off-diagonal kernel gives the pole/residue results recorded in exact_momentum_pole_audit.txt.

At exact degeneracy:
- Benchmark A: the Higgs-like pole remains narrow, while the singlet-like pole is broad due to \(s\to A'A'\).
- Benchmark B: the two poles remain overlapping and share the Higgs-channel residue as complex quantities:
\[
R_{hh}^{\rm narrow}\simeq-0.035407-0.024321i,\qquad
R_{hh}^{\rm broad}\simeq1.035407+0.024321i.
\]
The sum is unity within numerical precision in this approximate kernel. These residues are not probabilities or individual signal strengths.

## Limitations

This improves the momentum dependence of the fermion-sector hard matching, but it does not close the physical prediction. The diagonal widths remain fixed inputs; the \(s\) width omits mixing-induced SM and other open channels; diagonal self-energies and their field counterterms are not fully included; the EFT contact/counterterm and all same-order matching sectors are not closed; and no gauge/Goldstone/ghost completion or detector-level coherent likelihood is included. No allowed/excluded interval is inferred.
