# Major Point 1 — complex pole residues in the existing Plan-C-lite propagator

This is a reproducibility extension of the archived Plan-C-lite **approximate** \(2\times2\) propagator. It computes the derivative of the determinant and the matrix residue at each complex pole:
\[
{\cal D}^{-1}(s)=
\begin{pmatrix}s-a&-\Pi_{hs}(s)\\-\Pi_{hs}(s)&s-b\end{pmatrix},\qquad
F(s)=(s-a)(s-b)-\Pi_{hs}(s)^2,
\]
\[
\boxed{
\operatorname{Res}_{s=s_i}{\cal D}(s)
=\frac1{F'(s_i)}
\begin{pmatrix}
s_i-b&\Pi_{hs}(s_i)\\
\Pi_{hs}(s_i)&s_i-a
\end{pmatrix}.}
\]
The script uses the same selected \(\mu,\tau\) soft bubble plus contact and candidate finite derivative hard term, the same second-sheet continuation, and the same fixed diagonal-width approximation as Plan-C-lite. It does not upgrade that approximation to a complete physical prediction.

## Results

The numerical output is recorded in pole_residue_audit.txt. At the non-degenerate points \(m_s=100,150\) GeV, the Higgs-channel residue is approximately one on the Higgs-like pole and approximately zero on the singlet-like pole.

At exact degeneracy:
- Benchmark A (open \(A'A'\)): the Higgs-like pole retains \(R_{hh}\simeq1+O(10^{-7})\), while the singlet-like pole has a negligible Higgs-channel residue. This is consistent with the large \(s\) width from \(A'A'\) suppressing resonant mixing in this approximate kernel.
- Benchmark B (closed \(A'A'\)): the two poles share the Higgs-channel residue nontrivially:
\[
R_{hh}^{(1)}=-0.035432-0.024342i,\qquad
R_{hh}^{(2)}=1.035432+0.024342i.
\]
Their sum is \(1\) to numerical precision. The residues are complex and one has a negative real part. They are not probabilities, branching fractions, or independent signal strengths. Their nontrivial distribution demonstrates why the coherent two-pole amplitude must be used rather than assigning a real mixing angle to each state.

The residue matrix follows from the derivative of the inverse propagator. In a complete calculation the production/decay amplitude must use the physical vertices and the full residue matrix, including nonresonant terms and detector response.

## Acceptance boundary

This is a useful next diagnostic, but the following limitations remain inherited from Plan-C-lite: (i) fixed diagonal widths, (ii) diagonal real parts absorbed into input masses, (iii) candidate rather than fully closed hard derivative matching, (iv) incomplete same-order EFT soft/counterterm set, and (v) no gauge/Goldstone/ghost completion. No Higgs likelihood or exclusion is inferred.
