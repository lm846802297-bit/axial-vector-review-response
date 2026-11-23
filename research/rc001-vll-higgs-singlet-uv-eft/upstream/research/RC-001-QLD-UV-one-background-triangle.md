# RC-001 — QLD UV one-background triangle: exact integrands and Ward ledger

**Status (2026-11-10):** the two full-theory attachment classes, their routing, parity-even numerators, and relative sign are fixed at the integrand/Ward level. The complete degree-five Euclidean hard-region subgraph reduction through \(M_E^{-4}\) is evaluated with the corrected Wick sign. The ordinary light-line soft form factors are now evaluated through \(O(\epsilon^0)\); their poles cancel both hard IR poles, and the pure-\(U(1)_X\) hard-plus-soft amplitude is transverse and matching-scale independent. The Abelian transverse-pair IBP/Higgs-EOM reduction and its first potential/source/gauge-current companions are now recorded in §5K. Overall 1PI normalization, the non-Abelian \(SU(2)_L\) completion, the fermion-EOM/Fierz reduction of the generated scalar-source companions, the full source/current basis projection, and the final nonredundant Wilson coefficients remain open.

## 1. Frozen interaction and charges

Use
\[
\mathcal L_Y=-y_\ell\bar L_\ell H E_{\ell R}
-y_\ell^*\bar E_{\ell R}H^\dagger L_\ell
-M_E\bar E_\ell E_\ell.
\]
The gauge charges obey
\[
-q_L+q_H+q_E=0,\qquad q_E=q_L-q_H.
\]
The external composite source is \(\Psi_L=H^\dagger L_\ell\), so \(q_{\Psi_L}=q_E\).

For the three gauge sectors:
\[
\begin{array}{c|ccc}
 &q_L&q_H&q_E\\\hline
U(1)_Y&-\frac12&+\frac12&-1\\
U(1)_X&\eta_\ell Q_\ell&0&\eta_\ell Q_\ell\\
SU(2)_L&T^a& T^a&0
\end{array}
\]
The weak generators act on the doublet indices; \(E\) is a weak singlet.

## 2. Momentum routing

Use a consistent mixed incoming/outgoing convention: scalar momentum \(p\) enters the first Yukawa vertex, scalar momentum \(p'\) leaves the second, and background momentum \(q\) leaves the fermion loop. Momentum conservation gives \(q=p-p'\). Choose the light-fermion loop momentum \(k\). Define
\[
K=k+p,\qquad K'=k+p',\qquad k'=k+q.
\]
The two attachment classes have denominators
\[
D_L=k^2(k+q)^2(K^2+M_E^2),
\]
\[
D_E=k^2(K^2+M_E^2)(K'^2+M_E^2).
\]
These are Euclidean denominators. Overall factors of \(i\), the closed-loop minus sign, and the common coupling factor are to be restored consistently when converting the Euclidean integrals to 1PI vertices.

## 2A. Metric convention: keep Minkowski Ward algebra separate from Euclidean hard integrals

The routing/numerator identities in §§2–4 are first defined in Minkowski signature \((+---)\), where the heavy inverse propagator is \(K^2-M_E^2\). Since \(q=K-K'\), the Ward contraction in the heavy attachment is
\[
q_\mu N_E^\mu=
2\left[(K'\cdot k)(K^2-M_E^2)
-(K\cdot k)(K'^2-M_E^2)\right].
\]
The Euclidean hard-region integrals are obtained only after Wick rotation, with
\[
K_M^2-M_E^2\longrightarrow -(K_E^2+M_E^2),
\qquad k_M^2\longrightarrow-k_E^2,
\]
and corresponding factors of \(i\) in slash numerators and loop measures. The denominator symbols \(D_L,D_E\) in §2 are therefore Euclidean denominators; they must not be inserted directly into the Minkowski Ward identities of §4.

For clarity, the Euclidean hard expansion is
\[
\frac1{(k_E+p_E)^2+M_E^2}
=\frac1{k_E^2+M_E^2}
\sum_{n=0}^\infty
\left[-\frac{2k_E\cdot p_E+p_E^2}
{k_E^2+M_E^2}\right]^n.
\]
The previous shorthand mixed the Minkowski Ward denominators \(K^2-M_E^2\) with Euclidean denominators \(K_E^2+M_E^2\) without displaying the Wick rotation. This subsection fixes that convention. All subsequent tensor integration must be done wholly in Euclidean signature, and the Ward identity checked before Wick rotation in Minkowski signature (or after a fully consistent Euclidean continuation), never by mixing the two.

## 3. Exact parity-even chiral numerators

At each Yukawa endpoint the heavy propagator is projected onto its right-handed component, so a single heavy propagator between the two Yukawa endpoints has no mass numerator:
\[
P_R(\slashed K+M_E)P_L=\slashed K P_L,
\]
with the conjugate identity for the opposite orientation. For the parity-even part, the remaining chiral trace is one half of the corresponding four-component trace.

With the ordered routing above, \(k'=k+q\) and \(K=k+p=k'+p'\). For the heavy attachment \(K'=k+p'=K-q\), so \(q=K-K'\). Define
\[
N_L^\mu=\frac12\operatorname{tr}
[\slashed K\,\slashed{k'}\,\gamma^\mu\slashed k],
\qquad
N_E^\mu=\frac12\operatorname{tr}
[(\slashed K'+M_E)\gamma^\mu(\slashed K+M_E)\slashed k]_{\rm even}.
\]
Using \(\frac12\operatorname{tr}(\slashed a\slashed b\slashed c\slashed d)
=2[(a\cdot b)(c\cdot d)-(a\cdot c)(b\cdot d)+(a\cdot d)(b\cdot c)]\), these become
\[
N_L^\mu=2\left[
(K\cdot k')k^\mu-(k'\cdot k)K^\mu
+(K\cdot k)k'^\mu
\right],
\]
\[
N_E^\mu=2\left[
(K\cdot k)K'^\mu-(K'\cdot K)k^\mu
+(K'\cdot k)K^\mu+M_E^2 k^\mu
\right].
\]
**Caution:** for the heavy-attachment graph the two heavy propagators are separated by a vector vertex. The \(M_E^2 k^\mu\) term in the trace is therefore retained; dropping it would invalidate the heavy-line Ward contraction. With the momentum routing and common fermion flow fixed in §2, the Ward contractions below select the same relative sign for the two attachment classes. The trace definitions above are the numerator starting point, not yet an accepted integrated result.

The UV amplitude has the structural form
\[
\Gamma^\mu_{\rm UV}
\propto g_A|y_\ell|^2
\left[
q_L\int_k\frac{N_L^\mu}{D_L}
+q_E\int_k\frac{N_E^\mu}{D_E}
\right],
\]
where \(q_L,q_E\) are replaced by the appropriate representation generators for \(B_\mu,A'_\mu,W_\mu^a\). The same relative sign is fixed by the common fermion-flow convention and checked by the charge-resolved Ward contraction in §4.

## 4. Ward contraction and charge relation

For a fermion line,
\[
q_\mu\gamma^\mu=S_0^{-1}(k+q)-S_0^{-1}(k),\qquad q=k'-k=K-K'.
\]
Contracting the light-line attachment therefore collapses one of its two light propagators and produces the difference of the two heavy-light scalar two-point integrands with the external scalar momentum routed at \(p'\) and \(p\). Contracting the heavy-line attachment similarly collapses one heavy propagator and produces the corresponding difference with the heavy charge \(q_E\).

With \(\Sigma(p)\equiv\int_k (K\cdot k)/[k^2(K^2-M_E^2)]\), the adjacent-propagator reductions give
\[
q_\mu I_L^\mu=2[\Sigma(p)-\Sigma(p')],\qquad
q_\mu I_E^\mu=2[\Sigma(p')-\Sigma(p)].
\]
Thus the plus sign between the two attachment classes in the trace convention of §3 is fixed: the charge-weighted sum is proportional to
\[
(q_L-q_E)[\Sigma(p)-\Sigma(p')]
=q_H[\Sigma(p)-\Sigma(p')].
\]
This matches the scalar-source Ward identity for the stated outgoing-\(q\) convention.

With the common fermion-flow convention, the two attachment classes enter with the same relative sign in the trace convention of §3: their longitudinal contractions are opposite for equal constituent charges. The sum must obey the scalar-source Ward identity
\[
q_\mu\Gamma^\mu_{A H^\dagger H}(p,p')
=g_Aq_H\left[
\Gamma_{H^\dagger H}(p)-\Gamma_{H^\dagger H}(p')
\right],
\]
with the outgoing-\(q\) convention above. Equivalently, the constituent charge coefficients combine using \(q_L-q_E=q_H\), which follows from \(-q_L+q_H+q_E=0\). This is a stringent sign/routing test. For \(U(1)_X\), \(q_H=0\) and \(q_L=q_E\), so the light- and heavy-line longitudinal pieces cancel. For hypercharge and \(SU(2)_L\), the remainder is precisely the scalar-leg transformation term.

## 5. Hard-region expansion target

For \(k\sim M_E\), expand
\[
\frac1{(k+p)^2+M_E^2}
=\frac1{k^2+M_E^2}
\sum_{n\ge0}
\left[-\frac{2k\cdot p+p^2}{k^2+M_E^2}\right]^n,
\]
and analogously for \(p'\). Retain total external-momentum degree five in the sum of the two attachment classes; this is the \(M_E^{-4}\) contribution to the dimension-eight one-background form factor. Keep the \(d\)-dimensional tensor averages until after the radial integrals, since \(O(\epsilon)\) angular terms can multiply UV poles.

The light-attachment graph also has a soft region \(k\sim p,q\), in which the heavy propagator is expanded in \(1/M_E\). Its soft terms must be compared with the ordinary light-line insertion and all ordered covariant-derivative contact vertices generated by \(Q_{LD}^{(8)}\). The heavy-attachment graph has no massless two-propagator bubble. At this order its soft expansion contains only one massless denominator; in the unbroken massless dimensional-regularization setup it is scaleless. This is established by the explicit expansion, not by topology alone. If light masses, VEVs, or another IR scale are retained, this conclusion must be revisited.

## 5A. Mandatory correction to the hard-region expansion

The expansion written in §5 is incomplete if read as expanding only the heavy propagators. In the hard region \(k\sim M_E\), **every propagator carrying a shifted momentum must be expanded**, including the massless light propagator \((k+q)^{-2}\) in the light-attachment graph. The correct Euclidean expansions are
\[
\frac1{(k+q)^2}
=\frac1{k^2}\sum_{n=0}^\infty
\left[-\frac{2k\cdot q+q^2}{k^2}\right]^n,
\]
\[
\frac1{(k+p)^2+M_E^2}
=\frac1{k^2+M_E^2}\sum_{n=0}^\infty
\left[-\frac{2k\cdot p+p^2}{k^2+M_E^2}\right]^n,
\]
and similarly for \(p'\). The numerator must also be expanded by its explicit polynomial dependence on \(p,p',q\), with \(q=p-p'\) imposed only after the expansion.

Both trace numerators are polynomials of external-momentum degree at most two (the heavy numerator also contains the mass term \(M_E^2 k^\mu\), of external degree zero). Explicitly, with \(k^2\equiv k_E^2\),
\[
N_L^\mu=2\left[
(k^2+2k\cdot p+p\cdot q)k^\mu
-(k^2+k\cdot q)p^\mu
+(k^2+k\cdot p)q^\mu
\right],
\]
\[
N_{E,\mathrm{Euclidean}}^\mu=2\left[
(k^2-M_E^2-p\cdot p')k^\mu
+(k^2+k\cdot p')p^\mu
+(k^2+k\cdot p)p'^\mu
\right].
\]
The Minkowski trace in §3 has \(+M_E^2 k^\mu\); after Wick rotation this term has the opposite relative sign because the momentum-product trace terms contain one Minkowski scalar product, whereas the mass term does not.
The Lorentz vector itself carries one external momentum after tensor reduction. Therefore the degree-five vector amplitude requires degree-four scalar form factors. For explicit external-vector components, the contributions come from degree-four denominator-series terms times degree-zero numerator coefficients, degree-three denominator terms times degree-one numerator coefficients, and degree-two denominator terms times degree-two numerator coefficients. For a free \(k^\mu\) component, the loop vector itself is converted into an external vector by the angular average; its scalar coefficient must therefore be extracted at degree five, and its odd-rank tensor average can be nonzero. Expanding only the heavy denominators misses terms and cannot yield the complete hard coefficient.

A reproducible expansion generator should represent the external momenta as formal commuting vectors, generate the series to total degree five, reduce tensor integrals using \(d\)-dimensional rotational invariance, and only then perform the radial integrals. In particular, do not impose \(q=p'-p\) before generating the series, because it obscures the independent Taylor coefficients needed to identify the local operator basis.

## 5B. Euclidean hard-region master integrals

After expanding all shifted propagators, every tensor integral is reduced to rotationally invariant scalar masters. For an even-rank tensor,
\[
\int_k k^{\mu_1}\cdots k^{\mu_{2n}} f(k^2)
=\frac{\mathcal S^{\mu_1\cdots\mu_{2n}}}
{d(d+2)\cdots(d+2n-2)}
\int_k (k^2)^n f(k^2),
\]
where \(\mathcal S\) is the sum over all \((2n-1)!!\) metric pairings. Odd-rank tensors vanish.

A convenient radial master, with \(\int_k\equiv\mu^{2\epsilon}\int d^dk_E/(2\pi)^d\), is
\[
J_{a b}^{(t)}
=\int_k\frac{(k_E^2)^t}
{(k_E^2)^a(k_E^2+M_E^2)^b}
=\frac{\mu^{2\epsilon}}{(4\pi)^{d/2}}
(M_E^2)^{d/2+t-a-b}
\frac{\Gamma(d/2+t-a)\Gamma(a+b-d/2-t)}
{\Gamma(d/2)\Gamma(b)}.
\]
The formula is understood by analytic continuation in dimensional regularization. It keeps UV and IR singularities visible as separate Gamma-function singularities when a given expanded term has both. It must not be replaced by a four-dimensional cutoff integral.

For the two attachment classes, the denominator-series terms reduce to this master with:
- light attachment: \(a=2+n_L\), \(b=1+n_E\);
- heavy attachment: \(a=1\), \(b=2+n_{E1}+n_{E2}\);
where the nonnegative expansion indices are constrained by scalar form-factor degree four. The \(M_E^2 k^\mu\) and other free-\(k^\mu\) terms must be retained: at scalar degree five their odd number of loop-momentum contractions combines with the free vector index to give an even-rank rotational tensor and can contribute to the external-vector form factors.

The complete Taylor-partition sums and radial master integrations are evaluated in §5D. A Gamma-function pole in an individual hard Taylor term is not by itself a matched UV pole: it must be combined with the EFT soft region in the same subtraction convention. The corrected ordinary-line soft pole comparison is given in §5E.

## 5C. Superseded first Taylor-count attempt

The earlier 28/20/20 count treated the scalar coefficient degree as the full vector-amplitude degree and therefore selected degree five before accounting for the explicit external Lorentz vector. It also did not provide the claimed dedicated generator on the PR head. **Those counts are superseded and must not be used for matching.**

For a decomposition \(\Gamma^\mu=p^\mu F_p+q^\mu F_q\), a total degree-five vector amplitude requires degree-four scalar form factors. The corrected generator and radial reduction are in calculations/RC-001-QLD-hard-expansion-numerator-audit.py.

## 5D. Corrected degree-five vector amplitude: complete d-dimensional radial reduction

The corrected tensor reduction treats the two vector structures separately:
- explicit \(p^\mu,q^\mu,p'^\mu\) numerator components require scalar form-factor degree four;
- a free \(k^\mu\) component requires scalar coefficient degree five, because its angular average pairs the free index with one external momentum.

After angular averaging, the structures combine into 17 radial terms each for the light-attachment \(p^\mu\) and \(q^\mu\) form factors, and 7 terms each for the heavy-attachment \(p^\mu\) and \(p'^\mu\) form factors. The free-\(k^\mu\) contributions are included in these counts. There are 25 distinct radial masters:
\[
\begin{split}
&(1,4,1),(1,5,1),(1,5,2),(1,6,2),(1,6,3),(1,7,3),(1,7,4),\\
&(2,3,1),(2,4,2),(2,5,3),(2,6,4),\\
&(3,2,1),(3,3,2),(3,4,3),(3,5,4),\\
&(4,1,1),(4,2,2),(4,3,3),(4,4,4),\\
&(5,1,2),(5,2,3),(5,3,4),(6,1,3),(6,2,4),(7,1,4).
\end{split}
\]
Each tuple denotes \((a,b,t)\) in \(J_{ab}^{(t)}\). The denominator indices are
\[
L:\quad a=2+n_q,\quad b=1+n_p,\qquad
E:\quad a=1,\quad b=2+n_p+n_{p'}.
\]
The \(p\)-shift in the light graph raises the massive denominator power \(b\), not the massless power \(a\).

For all 25 masters, the UV Gamma-function argument \(a+b-2-t\) is positive, so the hard-region integrals are UV convergent. Eight masters have IR poles:
\[
\begin{array}{c|c}
(a,b,t)&J_{ab}^{(t)}\\\hline
(3,2,1)&-\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+2\right)\\
(4,1,1)&+\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+1\right)\\
(4,2,2)&-\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+2\right)\\
(5,1,2)&+\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+1\right)\\
(5,2,3)&-\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+2\right)\\
(6,1,3)&+\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+1\right)\\
(6,2,4)&-\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+2\right)\\
(7,1,4)&+\dfrac{1}{16\pi^2M_E^4}\left(\dfrac1{\epsilon_{\rm IR}}+L_M+1\right).
\end{array}
\]
The remaining 17 masters are finite. Here
\[
L_M=\ln\frac{\mu^2}{M_E^2}+\ln(4\pi)-\gamma_E.
\]

Summing the radial masters gives the following Euclidean hard-region form factors in the trace/routing convention of §3, before restoring the common Wick/Feynman-rule phase, \(g_A|y_\ell|^2\), and representation charges. Let \(P=p^2\), \(Q=q^2\), \(R=p\cdot q\), \(P'=p'^2\), and \(T=p\cdot p'\). For the light attachment:
\[
F_p^L\big|_{\rm hard}=
\frac{Q(P-R)}{24\pi^2M_E^4\epsilon_{\rm IR}}
+\frac{12L_MQ(P-R)-9P^2+18PR+16PQ-12R^2-13RQ+3Q^2}
{288\pi^2M_E^4},
\]
\[
F_q^L\big|_{\rm hard}=
-\frac{R(P-R)}{24\pi^2M_E^4\epsilon_{\rm IR}}
+\frac{-24L_MPR+24L_MR^2+9P^2-68PR+9PQ+62R^2-24RQ+3Q^2}
{576\pi^2M_E^4}.
\]
For the heavy attachment:
\[
F_p^E\big|_{\rm hard}=
\frac{5P^2+13PP'+13P'^2-8PT-14P'T+6T^2}
{960\pi^2M_E^4},
\]
\[
F_{p'}^E\big|_{\rm hard}=
\frac{13P^2+13PP'+5P'^2-14PT-8P'T+6T^2}
{960\pi^2M_E^4}.
\]

For the pure \(U(1)_X\) sector, \(q_L=q_E\) and \(q_H=0\). After imposing \(p'=p-q\), the heavy-attachment contribution in the \((p^\mu,q^\mu)\) basis is
\[
F_{p}^{E,pq}=
\frac{15P^2+20PQ-30PR+9Q^2-25QR+20R^2}
{480\pi^2M_E^4},
\]
\[
F_{q}^{E,pq}=
-\frac{15P^2+15PQ-20PR+5Q^2-12QR+10R^2}
{960\pi^2M_E^4}.
\]
Adding the light and heavy attachments gives the compact result
\[
F_{p,\mathrm{hard}}^{X}=
\frac{Q}{720\pi^2M_E^4}
\left[
\frac{30(P-R)}{\epsilon_{\rm IR}}
+30L_M(P-R)+70P+21Q-70R
\right],
\]
\[
F_{q,\mathrm{hard}}^{X}=
-\frac{R}{720\pi^2M_E^4}
\left[
\frac{30(P-R)}{\epsilon_{\rm IR}}
+30L_M(P-R)+70P+21Q-70R
\right].
\]
Consequently,
\[
R F_{p,\mathrm{hard}}^{X}+QF_{q,\mathrm{hard}}^{X}=0
\]
for both the pole and finite terms. This is the charge-resolved hard-region Ward check for \(q_L=q_E\). The common factor \(g_X q_\ell |y_\ell|^2\) and the overall 1PI phase are still omitted.

A useful internal check is that the light-attachment hard IR pole is transverse:
\[
R\,F_p^{L,\rm pole}+Q\,F_q^{L,\rm pole}=0.
\]
The poles are IR poles of the hard region, not UV counterterms. In the pure-\(U(1)_X\) sector they cancel the ordinary-line EFT soft UV poles in both form factors, as shown in §5E. The common coupling/1PI phase and the hypercharge/\(SU(2)_L\) charge-weighted source projections are not yet included.

The reproducible symbolic reduction, including the free-\(k^\mu\) tensor contributions, is in calculations/RC-001-QLD-hard-expansion-numerator-audit.py, with checks in validation/RC-001-QLD-hard-expansion-numerator-audit.txt.

## 5E. Corrected EFT-soft pole comparison: ordinary light-line insertion

The \(M_E^{-4}\) soft expansion of the light-attachment graph is
\[
I_{L,\mathrm{soft}}^{(M^{-4}),\mu}
=-\frac1{M_E^4}\int_k
\frac{N_L^\mu(k,p,q)(k+p)^2}{k^2(k+q)^2}.
\]
Combine the two massless denominators with one Feynman parameter \(x\) and shift \(k=\ell-xq\). Then
\[
k=\ell-xq,\quad k'=\ell+(1-x)q,\quad K=\ell+p-xq.
\]
Writing \(A=K\cdot k'\), \(B=k'\cdot k\), and \(C=K\cdot k\), the numerator becomes
\[
N_L^\mu K^2
=2K^2\left[
(A-B+C)\ell^\mu
-Bp^\mu
+\big(-xA+xB+(1-x)C\big)q^\mu
\right].
\]
The \(p^\mu\) coefficient is \(-B\), not \(-B+C\): \(k'^\mu\) has no \(p^\mu\) component after this shift. The previous soft audit used \(-B+C\), which was an algebraic projection error and generated a spurious \(p^\mu\) residual. The corrected coefficient is used in the current script.

After the exact \(d\)-dimensional angular average and extraction of the UV pole,
\[
F_{p,\mathrm{soft,line}}^{\rm UV}
=-\frac{Q(P-R)}
{24\pi^2M_E^4\epsilon_{\rm UV}},
\qquad
F_{q,\mathrm{soft,line}}^{\rm UV}
=+\frac{R(P-R)}
{24\pi^2M_E^4\epsilon_{\rm UV}},
\]
where \(P=p^2,\ Q=q^2,\ R=p\cdot q\). Hence the soft UV pole is transverse:
\[
R F_{p,\mathrm{soft,line}}^{\rm UV}
+Q F_{q,\mathrm{soft,line}}^{\rm UV}=0.
\]
Comparing with §5D gives exact cancellation in both components:
\[
F_{p,\mathrm{hard}}^{\rm IR}
+F_{p,\mathrm{soft,line}}^{\rm UV}=0,\qquad
F_{q,\mathrm{hard}}^{\rm IR}
+F_{q,\mathrm{soft,line}}^{\rm UV}=0.
\]
Thus **the ordinary light-line soft graph already cancels both hard IR poles** in this parity-even projection. The previously reported \(p^\mu\) remainder is superseded and must not be used to motivate an additional pole counterterm or to assign a pole to a particular Q8/source graph.

The complete soft form factors through \(O(\epsilon^0)\) are
\[
F_{p,\mathrm{soft}}=
-\frac{Q(P-R)}{24\pi^2M_E^4}
\left[
\frac1{\epsilon_{\rm UV}}+
\ln\frac{\mu^2}{Q}+\ln(4\pi)-\gamma_E+\frac53
\right],
\]
\[
F_{q,\mathrm{soft}}=
+\frac{R(P-R)}{24\pi^2M_E^4}
\left[
\frac1{\epsilon_{\rm UV}}+
\ln\frac{\mu^2}{Q}+\ln(4\pi)-\gamma_E+\frac53
\right].
\]
They are transverse beyond the pole:
\[
R F_{p,\mathrm{soft}}+QF_{q,\mathrm{soft}}=0.
\]

For \(q_L=q_E\), adding the corrected hard \(L+E\) result in §5D gives the complete method-of-regions amplitude
\[
F_{p,\mathrm{UV+soft}}^X=
\frac{Q}{720\pi^2M_E^4}
\left[
30(P-R)\ln\frac{Q}{M_E^2}
+20(P-R)+21Q
\right],
\]
\[
F_{q,\mathrm{UV+soft}}^X=
-\frac{R}{720\pi^2M_E^4}
\left[
30(P-R)\ln\frac{Q}{M_E^2}
+20(P-R)+21Q
\right].
\]
Both the \(1/\epsilon\) poles and the arbitrary \(\mu\)-dependence cancel, and the full result obeys the \(U(1)_X\) Ward identity. These are still stripped form factors: the common \(g_Xq_\ell|y_\ell|^2\) and 1PI phase are omitted. The hard part alone is the local matching contribution; the soft part is reproduced by the EFT loop and must not be folded into the Wilson coefficient.

The reproducible calculation is in calculations/RC-001-QLD-hard-expansion-numerator-audit.py, with the exact checks and expressions in validation/RC-001-QLD-hard-expansion-numerator-audit.txt. This closes the ordinary-line finite hard/soft comparison for the pure-\(U(1)_X\), parity-even projection. It does not yet establish the hypercharge/\(SU(2)_L\) projections or the full nonredundant Wilson vector.

## 5F. Covariant \(Q_{LD}^{(8)}\) contact vertex

The chiral heavy propagator gives the tree-level derivative expansion of the \(H^\dagger L_\ell\) composite. With \(\Psi_L=H^\dagger L_\ell\), the operator at the next order is the full covariant product
\[
Q_{LD}^{(8)}=(\bar L_\ell H)(i\slashed D)^3(H^\dagger L_\ell),
\qquad
\Delta\mathcal L_{\rm EFT}^{(8)}
=\frac{|y_\ell|^2}{M_{E_\ell}^4}Q_{LD}^{(8)}
\]
in the sign convention where \(Q_{LD}^{(6)}=(\bar L_\ell H)i\slashed D(H^\dagger L_\ell)\) has coefficient \(+|y_\ell|^2/M_E^2\). The operator is \((i\slashed D)^3\), not merely \(i\slashed D D^2\): the noncommuting covariant derivatives also contain the field-strength commutator terms.

For \(D_\mu=\partial_\mu+i g_A q_E A_\mu\), define \(\Pi_\mu=iD_\mu\). The stripped one-background vertex between composite momenta \(K\) and \(K'\), with \(q=K-K'\), is
\[
V_{Q8}^\mu(K',K)
=-g_Aq_E\left[
K'^2\gamma^\mu+\slashed K'\gamma^\mu\slashed K+K^2\gamma^\mu
\right].
\]
Its Ward contraction is
\[
q_\mu V_{Q8}^\mu
=-g_Aq_E\left[K^2\slashed K-K'^2\slashed K'\right],
\]
using
\[
\slashed K'\slashed q\slashed K
=K^2\slashed K'-K'^2\slashed K.
\]
This is exactly the difference of the zero-background \(Q_{LD}^{(8)}\) inverse kernels and fixes the ordered contact vertex. The formula includes the gauge coupling to the full composite charge \(q_E=q_L-q_H\), not just the \(L\) constituent charge.

Closing the light-lepton pair at this local contact gives a one-propagator tadpole. In the unbroken massless EFT it has no external scale; after expanding the numerator, all terms reduce to scaleless integrals of polynomials divided by \(k^2\). It therefore produces no logarithmic \(1/\epsilon_{\rm UV}\) pole in dimensional regularization at this order. It must still be retained in the Ward/source ledger if an IR mass, VEV, or a different off-shell regulator is introduced.

The heavy-attachment soft expansion likewise has only one massless propagator after both heavy denominators are expanded. In the unbroken massless dimensional-regularization setup it is scaleless at this order and gives no logarithmic soft UV pole. This is a result of the explicit expansion, not a reason to omit the attachment from the full-theory hard calculation.

## 5G. Charge-resolved \(U(1)_X\), hypercharge, and \(SU(2)_L\) projections

For a compact charge decomposition, define
\[
\ell_Q=\ln\frac{Q}{M_E^2},\qquad Q=q^2.
\]
The complete light-attachment form factors (hard plus its ordinary-line soft EFT loop) are
\[
F_p^{L,\mathrm{full}}=
\frac{Q(P-R)\ell_Q}{24\pi^2M_E^4}
+\frac{-9P^2-4PQ+18PR+3Q^2+7QR-12R^2}
{288\pi^2M_E^4},
\]
\[
F_q^{L,\mathrm{full}}=
-\frac{R(P-R)\ell_Q}{24\pi^2M_E^4}
+\frac{9P^2+9PQ-28PR+3Q^2-24QR+22R^2}
{576\pi^2M_E^4}.
\]
The pure-\(U(1)_X\) complete amplitude is
\[
F_p^X=
\frac{Q}{720\pi^2M_E^4}
\left[30(P-R)\ell_Q+20(P-R)+21Q\right],
\]
\[
F_q^X=
-\frac{R}{720\pi^2M_E^4}
\left[30(P-R)\ell_Q+20(P-R)+21Q\right].
\]
For a general gauge generator, use \(q_L=q_E+q_H\). Since the soft loop is weighted by \(q_L\), while the heavy-line hard graph is weighted by \(q_E\), the complete stripped amplitude decomposes as
\[
\Gamma_A^\mu\ \propto\
g_A|y_\ell|^2\left[
q_E\,\Gamma_X^\mu+q_H\,\Gamma_L^\mu
\right],
\]
where \(\Gamma_X^\mu\) is represented by \(F_{p,q}^X\), and \(\Gamma_L^\mu\) by \(F_{p,q}^{L,\mathrm{full}}\). The hard matching contribution is obtained by replacing both complete amplitudes by their hard parts; the soft loop is not included in the Wilson coefficient.

For hypercharge, \(q_E=-1\) and \(q_H=+1/2\), so
\[
F_{p,q}^{Y}=-F_{p,q}^{X}+\frac12F_{p,q}^{L,\mathrm{full}}.
\]
Explicitly,
\[
F_p^Y=
-\frac{
45P^2+60Q(P-R)\ell_Q+100PQ-90PR+69Q^2-115QR+60R^2
}{2880\pi^2M_E^4},
\]
\[
F_q^Y=
\frac{
45P^2+45PQ+120R(P-R)\ell_Q+20PR+15Q^2+48QR-50R^2
}{5760\pi^2M_E^4}.
\]
For \(SU(2)_L\), the composite \(H^\dagger L\) is a weak singlet, so \(q_E=0\); the background generator acts on the scalar/doublet source. In a fixed component channel,
\[
F_{p,q}^{W^a}=T^a F_{p,q}^{L,\mathrm{full}},
\]
with the appropriate fundamental/anti-fundamental index ordering understood.

The charge-resolved Ward check is
\[
R F_p^{L,\mathrm{full}}+QF_q^{L,\mathrm{full}}
=\frac{P'^3-P^3}{192\pi^2M_E^4},
\qquad P'=P+Q-2R,
\]
whereas
\[
R F_p^X+QF_q^X=0.
\]
Consequently,
\[
q_\mu\Gamma_A^\mu
\ \propto\
g_A|y_\ell|^2q_H
\frac{P'^3-P^3}{192\pi^2M_E^4}.
\]
This vanishes for \(U(1)_X\), gives one half of the light-source difference for hypercharge, and carries the \(SU(2)_L\) generator for the weak current. The nonzero hypercharge/weak longitudinal part is the scalar-source Ward term, not a failure of transversality. These relations hold for the stripped parity-even form factors; overall 1PI normalization and the full operator-basis projection remain to be restored.

## 6. Acceptance conditions

The QLD one-background matching is accepted only after:
1. the common Wick/Feynman-rule phase and charge-normalization conventions are restored and checked against the fixed fermion-flow/Ward convention;
2. the complete \(d\)-dimensional hard expansion through degree five is integrated;
3. the soft expansion is calculated with the same routing and subtraction scheme;
4. the complete EFT ordinary-line, Q8 contact, and scalar-source terms are summed;
5. the charge-resolved Ward identity is satisfied before and after pole extraction;
6. hard IR poles cancel soft UV poles and the remaining local coefficient is independent of the arbitrary matching scale.

The hard subgraph form factors and ordinary-line hard/soft pole cancellation are established in the stated trace/routing convention. No complete charge-weighted QLD dimension-eight Wilson coefficient is claimed in this record.


## 5H. Operator-level reduction of \(Q_{LD}^{(8)}\): ordered derivative identity

The hard/soft form factors are now available in a fixed off-shell momentum basis. The next step is an operator-basis projection, not another pole-cancellation graph. Before applying IBP or equations of motion, the derivative ordering in
\[
Q_{LD}^{(8)}=(\bar\Psi_L)(i\slashed D)^3\Psi_L,
\qquad \Psi_L=H^\dagger L_\ell,
\]
must be preserved.

For the convention \(D_\mu=\partial_\mu+i g_A q_E A_\mu\), define \(\Pi_\mu=iD_\mu\). Then
\[
[\Pi_\mu,\Pi_\nu]=-i g_Aq_E F_{\mu\nu},
\qquad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].
\]
The exact ordered identity is
\[
(i\slashed D)^2
=\Pi^2-\frac{g_Aq_E}{2}\sigma^{\mu\nu}F_{\mu\nu},
\]
and hence
\[
(i\slashed D)^3
=\gamma^\mu\Pi_\mu\Pi^2
-\frac{g_Aq_E}{2}\gamma^\mu\Pi_\mu
\big(\sigma^{\rho\sigma}F_{\rho\sigma}\big).
\]
This is an identity of differential operators: in the second term \(\Pi_\mu\) acts on the product \(F_{\rho\sigma}\Psi_L\), not only on \(\Psi_L\). It therefore contains both \(F_{\rho\sigma}\Pi_\mu\Psi_L\) and \((D_\mu F_{\rho\sigma})\Psi_L\) contributions. Reordering \(\Pi_\mu\Pi^2\) also generates field-strength terms through
\[
[\Pi_\mu,\Pi^2]
=-i g_Aq_E\left(F_{\mu\nu}\Pi^\nu+\Pi^\nu F_{\mu\nu}\right).
\]
These commutators are the operator-level counterpart of the ordered one-background contact vertex in §5F.

A crucial restriction for the EOM step is that \(\Psi_L=H^\dagger L_\ell\) is a composite, not an elementary field with a free Dirac equation. In particular,
\[
i\slashed D(H^\dagger L_\ell)
=(iD_\mu H^\dagger)\gamma^\mu L_\ell
+H^\dagger i\slashed D L_\ell .
\]
The second term is constrained by the SM lepton Yukawa EOM, while the first is a Higgs-derivative operator. Replacing the whole left-hand side by zero would incorrectly discard independent Higgs-derivative and field-strength operators. The correct reduction must use the separate SM EOM for \(L_\ell\) and \(H\), then IBP, and finally project onto a declared dimension-eight basis.

For the present one-background two-Higgs/two-lepton channel, the minimum basis ledger must keep separate until the projection is complete:
1. derivative-current structures with three covariant derivatives distributed among \(H^\dagger\), \(L_\ell\), and \(\bar L_\ell H\);
2. field-strength structures generated by \([\Pi_\mu,\Pi_\nu]\), including the derivative-on-\(F_{\mu\nu}\) terms;
3. EOM-reducible terms proportional to the Higgs and lepton EOM, together with the induced Yukawa/source operators;
4. total derivatives and IBP relations.

No coefficient in this basis is assigned by inspection of the transverse \(U(1)_X\) form factor alone. The \(U(1)_X\) result constrains the transverse combination; hypercharge and \(SU(2)_L\) additionally test the scalar-source Ward term. The hard coefficient must be projected from the hard part only; the soft form factors in §5E are reproduced by EFT loops and are not Wilson coefficients.

**Acceptance gate for the next calculation:** construct the ordered derivative/field-strength operator list, derive its one-background Feynman rules, evaluate each operator on the same independent off-shell \(p,p',q\) kinematics, and solve the resulting linear system for the hard form factors. Only after this map is full-rank (modulo explicitly listed IBP/EOM relations) should the nonredundant Wilson coefficients be quoted.

## 5I. Explicit Leibniz expansion before EOM/IBP

To make the basis projection reproducible, expand the composite derivative without commuting any derivatives. Let \(\Pi_\mu=iD_\mu\) act in the appropriate representation on each factor. The covariant product rule gives
\[
\begin{split}
\Pi^2(H^\dagger L_\ell)={}&
(\Pi^2H^\dagger)L_\ell
+2(\Pi_\nu H^\dagger)(\Pi^\nu L_\ell)
+H^\dagger\Pi^2L_\ell,\\
\gamma^\mu\Pi_\mu\Pi^2(H^\dagger L_\ell)={}&
\gamma^\mu\Big[
(\Pi_\mu\Pi^2H^\dagger)L_\ell
+(\Pi^2H^\dagger)(\Pi_\mu L_\ell)\\
&+2(\Pi_\mu\Pi_\nu H^\dagger)(\Pi^\nu L_\ell)
+2(\Pi_\nu H^\dagger)(\Pi_\mu\Pi^\nu L_\ell)\\
&+(\Pi_\mu H^\dagger)(\Pi^2L_\ell)
+H^\dagger\Pi_\mu\Pi^2L_\ell
\Big].
\end{split}
\]
The field-strength part must likewise be expanded as
\[
-\frac{g_Aq_E}{2}\,
\bar L_\ell H\,\gamma^\mu
\left[
(\Pi_\mu\sigma^{\rho\sigma}F_{\rho\sigma})(H^\dagger L_\ell)
+\sigma^{\rho\sigma}F_{\rho\sigma}\,
\Pi_\mu(H^\dagger L_\ell)
\right].
\]
Here the first \(\Pi_\mu\) in the square bracket differentiates the field-strength tensor (with its adjoint gauge-covariant derivative), while the second term distributes onto \(H^\dagger\) and \(L_\ell\) by the product rule.

These expressions define an ordered overcomplete generating set, not yet a nonredundant basis. The next reduction must:
- retain the ordering \(\Pi_\mu\Pi_\nu\) until its antisymmetric part has been converted with \([\Pi_\mu,\Pi_\nu]=-ig_Aq F_{\mu\nu}\);
- apply the lepton EOM only to \(\Pi^2L_\ell\) or \(\slashed\Pi L_\ell\) combinations after gamma identities, and apply the Higgs EOM to \(\Pi^2H\) terms;
- integrate by parts with the conjugate representation on \(\bar L_\ell H\), recording each total derivative;
- keep the generated Yukawa, Higgs-potential, and source operators in the coefficient vector rather than dropping them as “EOM zero” before the off-shell matching projection.

The six derivative-distribution terms and the two field-strength derivative placements above are ordered pieces in the expansion of one covariant operator; they are **not eight independent operators or eight independent Wilson-coefficient columns**. Their coefficients are fixed together by the single tree-level \(Q_{LD}^{(8)}\) coefficient. The independent amplitude columns used for the restricted one-background projection are defined separately in §5J. A full operator-basis reduction still requires IBP/EOM identities and the induced source/current companions.


## 5K. Abelian covariant IBP/EOM reduction of the transverse pair

This subsection reduces the two transverse representatives of §5J before calling them independent operators. It is restricted to a single Abelian background, consistently with the operator representatives in §5J; other gauge backgrounds are set to zero in this commutator subcalculation. Restoring the full SM covariant derivative adds the corresponding other field strengths and mixed two-background contacts, which are not projected here. Let
\[
D_\mu=\partial_\mu+i g_A q_H A_\mu,\qquad
[D_\mu,D_\nu]H=i g_Aq_HF_{\mu\nu}H,
\]
and abbreviate \(\mathfrak g_A=g_Aq_H\). Define
\[
X=H^\dagger H,\quad Y=S^\dagger S,\quad
j_H^\mu=iH^\dagger\overleftrightarrow D^\mu H.
\]

Using antisymmetry of \(F^{\mu\nu}\),
\[
\mathcal O_P=iF^{\mu\nu}(D_\rho D_\mu H)^\dagger
D^\rho D_\nu H,\qquad
\mathcal O_Q=-i(D_\mu H)^\dagger D_\nu H\,\Box F^{\mu\nu}.
\]
For an Abelian field strength, two covariant integrations by parts give
\[
\mathcal O_Q\doteq
-iF^{\mu\nu}\Box[(D_\mu H)^\dagger D_\nu H].
\]
The product rule is
\[
\begin{aligned}
\Box[(D_\mu H)^\dagger D_\nu H]
={}&(D^2D_\mu H)^\dagger D_\nu H
+2(D_\rho D_\mu H)^\dagger D^\rho D_\nu H\\
&+(D_\mu H)^\dagger D^2D_\nu H.
\end{aligned}
\]
Consequently,
\[
\boxed{\mathcal O_P+\frac12\mathcal O_Q
\doteq\mathcal O_{E,H}^{(8)}}
\]
with
\[
\boxed{
\mathcal O_{E,H}^{(8)}
=-\frac i2F^{\mu\nu}\left[
(D^2D_\mu H)^\dagger D_\nu H
+(D_\mu H)^\dagger D^2D_\nu H
\right].
}
\]
This is an action-level IBP identity, not merely an on-shell relation. Its one-background vertex is
\[
\mathcal B_E^\mu=\mathcal B_P^\mu+\frac12\mathcal B_Q^\mu
=\frac{P+P'}2\,T^\mu,
\]
so it is transverse and vanishes when \(P=P'=0\). This explains the rank-one massless on-shell collapse found in §5J.

### 5K.1 Commutator completion: gauge-EOM and two-background terms

Do not commute \(D^2\) through \(D_\mu\) without recording the field-strength terms:
\[
[D^2,D_\mu]H
=i\mathfrak g_A\left[
(\partial_\rho F^\rho{}_\mu)H
+2F^\rho{}_\mu D_\rho H
\right].
\]
Writing \(\mathcal O_{E,H}^{(8)}
=\mathcal O_{E,H,\mathrm{ord}}^{(8)}
+\mathcal O_{\mathrm{comm}}^{(8)}\), where
\[
\mathcal O_{E,H,\mathrm{ord}}^{(8)}
=-\frac i2F^{\mu\nu}\left[
(D_\mu D^2H)^\dagger D_\nu H
+(D_\mu H)^\dagger D_\nu D^2H
\right],
\]
the commutator contribution is
\[
\boxed{\begin{aligned}
\mathcal O_{\mathrm{comm}}^{(8)}
={}&-\frac{\mathfrak g_A}{2}
F^{\mu\nu}(\partial_\rho F^\rho{}_\mu)\partial_\nu X\\
&-\mathfrak g_A F^{\mu\nu}F^\rho{}_\mu
\left[(D_\rho H)^\dagger D_\nu H
+(D_\nu H)^\dagger D_\rho H\right].
\end{aligned}}
\]
The first row is a gauge-field-EOM direction; the second is a genuine two-background \(F^2H^2D^2\) contact term. Neither is visible in the one-background form-factor projection alone.

For the convention above and gauge kinetic term \(-F_{\mu\nu}F^{\mu\nu}/4\), the Abelian gauge EOM is
\[
\partial_\rho F^\rho{}_\mu=g_AJ_\mu^{\mathrm{tot}},
\]
where \(J_\mu^{\mathrm{tot}}\) is the full matter current with charges included but without the overall \(g_A\). Thus one may replace the first commutator term by
\[
-\frac{g_A^2q_H}{2}
F^{\mu\nu}J_\mu^{\mathrm{tot}}\partial_\nu X.
\]
This replacement is optional and mutually exclusive with retaining the \(\partial_\rho F^\rho{}_\mu\) operator. The total current must include every charged matter field; it is not just the Higgs current.

### 5K.2 Higgs EOM and its potential/source companions

Use the same source convention as the project baseline:
\[
D^2H=-f_HH-\mathcal J_H,\qquad
f_H=-\mu_H^2+2\lambda_HX+\lambda_{HS}Y.
\]
Define the EOM residual
\[
\mathcal E_H=D^2H+f_HH+\mathcal J_H.
\]
Then
\[
\begin{aligned}
\mathcal O_{E,H,\mathrm{ord}}^{(8)}
\doteq{}&
f_H\,\mathcal O_{FH}^{(6)}
-\frac12F^{\mu\nu}j_{H\mu}\partial_\nu f_H
+\mathcal O_{FJ_H}^{(8)}
+\mathcal O_{\mathrm{EOM}},\\
\mathcal O_{FH}^{(6)}
\equiv{}&iF^{\mu\nu}(D_\mu H)^\dagger D_\nu H,\\
\mathcal O_{FJ_H}^{(8)}
\equiv{}&\frac i2F^{\mu\nu}\left[
(D_\mu\mathcal J_H)^\dagger D_\nu H
+(D_\mu H)^\dagger D_\nu\mathcal J_H
\right],\\
\mathcal O_{\mathrm{EOM}}
\equiv{}&-\frac i2F^{\mu\nu}\left[
(D_\mu\mathcal E_H)^\dagger D_\nu H
+(D_\mu H)^\dagger D_\nu\mathcal E_H
\right].
\end{aligned}
\]
The derivative-current term follows from
\[
(D_\mu H)^\dagger H=\frac12(\partial_\mu X+i j_{H\mu}),
\qquad
H^\dagger D_\mu H=\frac12(\partial_\mu X-i j_{H\mu}),
\]
and antisymmetry of \(F^{\mu\nu}\). Expanding \(f_H\) gives
\[
\boxed{\begin{aligned}
f_H\mathcal O_{FH}^{(6)}
={}&-\mu_H^2\mathcal O_{FH}^{(6)}
+2\lambda_HX\mathcal O_{FH}^{(6)}
+\lambda_{HS}Y\mathcal O_{FH}^{(6)},\\
-\frac12F^{\mu\nu}j_{H\mu}\partial_\nu f_H
={}&-\lambda_HF^{\mu\nu}j_{H\mu}\partial_\nu X
-\frac{\lambda_{HS}}2F^{\mu\nu}j_{H\mu}\partial_\nu Y.
\end{aligned}}
\]
The source operator \(\mathcal O_{FJ_H}^{(8)}\) must also be retained. In the original flavor-diagonal model, the leading-renormalizable source is
\[
(\mathcal J_{H}^{(4)})^k
=\bar d_RY_d^\dagger Q_L^k
+\epsilon_{ik}\bar Q_L^iY_u u_R
+y_e^*\bar e_RL_e^k.
\]
The charged-lepton \(U(1)_X\) charge matrix for \(\bar L_iHe_{Rj}\), with rows \(L_e,L_\mu,L_\tau\) and columns \(e_R,\mu_R,\tau_R\), is
\[
\begin{pmatrix}0&-1&+1\\-1&-2&0\\+1&0&+2\end{pmatrix}.
\]
Thus the electron diagonal entry is allowed, the diagonal \(\mu,\tau\) entries are forbidden, and the off-diagonal \(\bar L_\mu H\tau_R\), \(\bar L_\tau H\mu_R\) entries are gauge-allowed. The original model sets the latter two to zero by its flavor-diagonal/block-diagonal mass-matrix assumption; they must not be described as gauge-forbidden. If that flavor assumption is relaxed, the Higgs source and charged-lepton mass matrix must be enlarged. The explicit source/charge map is recorded in [RC-001-QLD-Higgs-source-EOM-model-map.md](RC-001-QLD-Higgs-source-EOM-model-map.md).

The dimension-five axial source is
\[
(\mathcal J_H^{(5)})^k
=C_{5,\mu}^*S^*\bar\mu_RL_\mu^k
+C_{5,\tau}^*S\bar\tau_RL_\tau^k,
\]
which is separately \(U(1)_X\)-neutral. Since \(C_5=O(M_E^{-1})\), its insertion with this \(O(M_E^{-4})\) coefficient starts at \(O(M_E^{-5})\), outside the strict order retained here; it is marked as higher order rather than set to zero.

### 5K.3 Charge boundary and retained transverse coefficient

The operator coefficient map is
\[
a\mathcal O_P+b\mathcal O_Q
\doteq a\mathcal O_{E,H}^{(8)}
+\left(b-\frac a2\right)\mathcal O_Q.
\]
After eliminating the Higgs-EOM direction, the retained transverse coefficient is therefore \(b-a/2\), while all companions in §§5K.1–5K.2 are generated with coefficient \(a\).

For the hard-region coefficients of §5J:
\[
\begin{array}{c|c|c|c}
\text{sector}&a&b&b-a/2\\ \hline
U(1)_X&q_Ea_X&q_Eb_X&
-q_E\dfrac{30/\epsilon_{\rm IR}+30L_M+28}{1440}\\[2mm]
U(1)_Y&a_Y&b_Y&
\dfrac{60/\epsilon_{\rm IR}+60L_M+47}{5760}\\[2mm]
SU(2)_L&T^aa_L&T^ab_L&
-T^a\dfrac{12/\epsilon_{\rm IR}+12L_M+13}{576}
\end{array}
\]
The \(SU(2)_L\) last column is only the algebraic amplitude-level combination; its non-Abelian adjoint derivative, generator ordering, and two-background completion are not reduced in this subsection.

The charge dependence in the commutator terms is important. Within the single-Abelian-background truncation used in this subsection, the external \(U(1)_X\) field has \(q_X(H)=0\), so the same-sector \(F_X\,\partial F_X\,\partial X\) and \(F_X^2H^2D^2\) commutator terms vanish. This does not remove mixed \(F_XF_Y\) or \(F_XW\) two-background terms generated by the full SM covariant derivative; see §5M. For hypercharge \(Y_H=+1/2\), the same-sector terms remain. This is distinct from the \(U(1)_X\) gauge-current dependence of the fermionic fields.

The hard coefficients in this table still contain hard-region IR poles; they are not finite renormalized Wilson coefficients. The scalar-source coefficient \(c_S=1/192\) is not changed by this transverse IBP step. Its higher-derivative EOM reduction is a separate task.

The exact polynomial and coefficient checks are in calculations/RC-001-QLD-dim8-IBP-EOM-reduction.py, with captured output in validation/RC-001-QLD-dim8-IBP-EOM-reduction.txt.

**Scope boundary.** This closes the Abelian covariant IBP identity and the first Higgs-EOM/source/current decomposition of the transverse pair. It does not close the full non-Abelian \(SU(2)_L\) completion, the higher-derivative EOM reduction of \(\mathcal O_S\), all two-background operators, the complete gauge-current basis, or the final UV–EFT-renormalized Wilson vector.


## 5L. Higher-derivative EOM reduction of the scalar-source representative

The bosonic scalar-source representative of §5J is
\[
\mathcal O_S=H^\dagger(-D^2)^3H.
\]
It is distinct from the singlet-scalar kinetic operators and from the fermionic \(Q_{LD}^{(8)}\) contact. This subsection reduces only this \(H\)-sector operator.

Define the self-adjoint differential operator \(K=-D^2\) and
\[
K_H=f_HH+\mathcal J_H,\qquad
f_H=-\mu_H^2+2\lambda_HX+\lambda_{HS}Y,
\qquad D^2H=-f_HH-\mathcal J_H.
\]
Using self-adjointness in the action,
\[
\begin{aligned}
\int d^4x\,H^\dagger K^3H
&=\int d^4x\,(KH)^\dagger K(KH)\\
&\doteq\int d^4x\,K_H^\dagger(-D^2)K_H\\
&\doteq\int d^4x\,(D_\mu K_H)^\dagger D^\mu K_H.
\end{aligned}
\]
Therefore the exact leading-EOM replacement is
\[
\boxed{\mathcal O_S\doteq
\left|D_\mu(f_HH+\mathcal J_H)\right|^2.}
\]
No commutation of \(D^2\) through a single \(D_\mu\) is used here; the covariant derivative remains on the complete gauge-covariant source \(K_H\).

The product rule gives
\[
D_\mu K_H=(\partial_\mu f_H)H+f_HD_\mu H+D_\mu\mathcal J_H.
\]
Keeping every term,
\[
\boxed{\begin{aligned}
\mathcal O_S\doteq{}&
X(\partial_\mu f_H)(\partial^\mu f_H)
+f_H^2(D_\mu H)^\dagger D^\mu H
+f_H(\partial_\mu f_H)\partial^\mu X\\
&+(\partial_\mu f_H)
\left[H^\dagger D^\mu\mathcal J_H
+(D^\mu\mathcal J_H)^\dagger H\right]\\
&+f_H\left[(D_\mu H)^\dagger D^\mu\mathcal J_H
+(D^\mu\mathcal J_H)^\dagger D_\mu H\right]\\
&+(D_\mu\mathcal J_H)^\dagger D^\mu\mathcal J_H.
\end{aligned}}
\]
The first three lines' first three terms are purely bosonic; the remaining three structures are the Higgs–Yukawa source and source-square companions. They are not discarded by the EOM transformation.

### 5L.1 Explicit pure-bosonic companions

Since
\[
\partial_\mu f_H
=2\lambda_H\partial_\mu X+\lambda_{HS}\partial_\mu Y,
\]
the coefficient multiplying the Higgs kinetic structure is
\[
\begin{aligned}
f_H^2={}&
\mu_H^4-4\mu_H^2\lambda_HX
-2\mu_H^2\lambda_{HS}Y\\
&+4\lambda_H^2X^2
+4\lambda_H\lambda_{HS}XY
+\lambda_{HS}^2Y^2.
\end{aligned}
\]
The remaining pure derivative terms combine to
\[
\boxed{\begin{aligned}
X(\partial f_H)^2+f_H\partial_\mu f_H\partial^\mu X
={}&
\left[-2\mu_H^2\lambda_H
+8\lambda_H^2X
+2\lambda_H\lambda_{HS}Y\right](\partial X)^2\\
&+\left[-\mu_H^2\lambda_{HS}
+6\lambda_H\lambda_{HS}X
+\lambda_{HS}^2Y\right]
\partial_\mu X\partial^\mu Y\\
&+\lambda_{HS}^2X(\partial Y)^2.
\end{aligned}}
\]
These are the explicit potential/derivative companions of the \(p^6\) scalar two-point source coefficient. They must be multiplied by the same \(c_S=1/192\) and the common UV matching normalization. Further IBP reduction of \((\partial X)^2\), \(\partial X\partial Y\), and the \(f_H^2|DH|^2\) term is a separate basis choice and must carry its own EOM/source ledger.

### 5L.2 Yukawa-source companions and truncation

The complete source contribution is
\[
\boxed{\begin{aligned}
\mathcal O_{S,\mathrm{src}}\doteq{}&
(\partial_\mu f_H)
\left[H^\dagger D^\mu\mathcal J_H+\mathrm{h.c.}\right]\\
&+f_H\left[(D_\mu H)^\dagger D^\mu\mathcal J_H+\mathrm{h.c.}\right]\\
&+(D_\mu\mathcal J_H)^\dagger D^\mu\mathcal J_H.
\end{aligned}}
\]
At the retained \(M_E^{-4}\) coefficient order, \(\mathcal J_H^{(4)}\), the allowed renormalizable SM Yukawa source, is included. The dimension-five source \(\mathcal J_H^{(5)}\propto C_5\sim M_E^{-1}\) contributes one further inverse heavy mass and hence starts at \(M_E^{-5}\) when multiplied by this coefficient. It is beyond the present strict order, not identically zero. The model's forbidden diagonal \(\mu,\tau\) renormalizable Yukawa entries remain excluded.

The exact algebraic expansion is checked in calculations/RC-001-QLD-dim8-scalar-source-EOM.py, with the captured output in validation/RC-001-QLD-dim8-scalar-source-EOM.txt.

**Scope boundary.** This completes the leading-Higgs-EOM replacement of the bosonic \(p^6\) source representative and lists its pure-bosonic and Yukawa-source companions. It does not yet reduce the generated fermionic source operators with fermion EOM/Fierz identities, select a final dimension-eight bosonic basis, or combine these coefficients with all UV/EFT soft terms and counterterms.

## 5J. Exact three-column off-shell amplitude projection

The hard form factors can be decomposed before any IBP/EOM reduction. Define
\[
P=p^2,\quad Q=q^2,\quad R=p\cdot q,\quad
P'=p'^2=P+Q-2R,\quad q=p-p',
\]
and
\[
\Sigma_3=P^2+PP'+P'^2,\qquad
T^\mu=Qp^\mu-Rq^\mu,\qquad
S^\mu=-(p+p')^\mu\Sigma_3.
\]
The three normalized amplitude columns are
\[
\mathcal B_P^\mu=(P-R)T^\mu,\qquad
\mathcal B_Q^\mu=Q T^\mu,\qquad
\mathcal B_S^\mu=S^\mu.
\]
Their form factors in \(\Gamma^\mu=p^\mu F_p+q^\mu F_q\) are
\[
\begin{array}{c|cc}
 &F_p&F_q\\ \hline
\mathcal B_P&Q(P-R)&-R(P-R)\\
\mathcal B_Q&Q^2&-RQ\\
\mathcal B_S&-2\Sigma_3&+\Sigma_3
\end{array}
\]
with
\[
q_\mu\mathcal B_P^\mu=q_\mu\mathcal B_Q^\mu=0,\qquad
q_\mu\mathcal B_S^\mu=P'^3-P^3.
\]

For an Abelian background, convenient local representatives with these stripped one-background vertices are
\[
\mathcal O_P=
\frac{i}{2}\left[
(D_\rho D_\mu H)^\dagger D^\rho D_\nu H
-(D_\rho D_\nu H)^\dagger D^\rho D_\mu H
\right]F^{\mu\nu},
\]
\[
\mathcal O_Q=
-\frac{i}{2}\left[
(D_\mu H)^\dagger D_\nu H
-(D_\nu H)^\dagger D_\mu H
\right]\Box F^{\mu\nu},
\qquad
\mathcal O_S=H^\dagger(-D^2)^3H.
\]
Use the Fourier convention in which \(H\) carries incoming momentum \(p\), \(H^\dagger\) carries outgoing momentum \(p'\), and the background momentum \(q=p-p'\) leaves the vertex. The common gauge coupling/charge and overall 1PI phase are stripped. With that convention, the one-background vertices are respectively \(\mathcal B_P^\mu,\mathcal B_Q^\mu,\mathcal B_S^\mu\). The first two representatives are useful Abelian lifts of the transverse columns; \(\mathcal O_S\) is the covariant scalar-source representative whose two-point kernel is \(P^3\). A non-Abelian completion requires the appropriate adjoint-generator insertion and covariant derivative on the field strength and is not claimed here.

Do not identify \(\mathcal O_S\) with \(Q_{LD}^{(8)}\). The latter is the fermionic Green-basis operator \((\bar L H)(i\slashed D)^3(H^\dagger L)\); \(\mathcal O_S\) is the bosonic scalar two-point source representative whose \(p^6\) inverse-kernel term is gauged to produce \(\mathcal B_S^\mu\). The \(Q_{LD}^{(8)}\) one-background contact/tadpole discussed in §5F is a separate EFT topology.

The source coefficient has now passed an independent analytic two-point cross-check. The exact \(B_0\) expansion recorded in the v153 source §250.3 is
\[
B_0=\Delta_{\rm UV}-L_\ell+1+\frac z2+\frac{z^2}{6}+\frac{z^3}{12}+\cdots,\qquad z=p^2/M_E^2.
\]
In \(A_0+(M_E^2-p^2)B_0\), the \(z^3\) coefficient is \(1/12-1/6=-1/12\). Including the overall minus sign in the stated \(i\Pi\) convention gives
\[
\Pi_{H\ell}^{\rm bare}(p^2)\supset
\frac{|y_\ell|^2}{16\pi^2}\frac{p^6}{12M_E^4}
=\frac{|y_\ell|^2p^6}{192\pi^2M_E^4}.
\]
Gauging this \(p^6\) inverse-kernel term gives precisely the scalar-source Ward coefficient \(c_S=1/192\) in the stripped normalization of §5J. This is an analytic extension of the recorded \(A_0/B_0\) two-point kernel, not a new FeynArts/FeynCalc or independent diagram-package run. The extended two-point formula is also recorded in research/RC-001-vll-higgs-singlet-uv-eft.md §4.2 and checked in the projection script.

Flatten the two form factors into the six independent quadratic monomials \((P^2,PQ,PR,Q^2,QR,R^2)\), first for \(F_p\) and then for \(F_q\). The exact polynomial projection matrix is
\[
M_{\rm amp}=
\begin{pmatrix}
0&0&-6\\
1&0&-6\\
0&0&12\\
0&1&-2\\
-1&0&8\\
0&0&-8\\
0&0&3\\
0&0&3\\
-1&0&-6\\
0&0&1\\
0&-1&-4\\
1&0&4
\end{pmatrix},
\]
where the columns are \((\mathcal B_P,\mathcal B_Q,\mathcal B_S)\). Exact SymPy reduction gives
\[
\operatorname{rank}M_{\rm amp}=3.
\]
For example, the minor formed from rows \((F_p:P^2,F_p:PQ,F_p:Q^2)\) is \(-6\), so all three columns are independent as polynomial functions of generic off-shell kinematics. This is a polynomial-function rank statement; at one fixed kinematic point the two-component vector \((F_p,F_q)\) cannot by itself resolve three coefficients. This is also why the projection must remain off shell: on the massless on-shell scalar surface \(P=P'=0\), one has \(R=Q/2\), \(\mathcal B_P=-\mathcal B_Q/2\), and \(\mathcal B_S=0\), so the map collapses to rank one.

In this basis the hard-region form factors of §§5D–5G become
\[
\Gamma_{X,\rm hard}^\mu
=a_X\mathcal B_P^\mu+b_X\mathcal B_Q^\mu,
\qquad
\Gamma_{L,\rm hard}^\mu
=a_L\mathcal B_P^\mu+b_L\mathcal B_Q^\mu+c_S\mathcal B_S^\mu,
\]
where the common factor \(g_A|y_\ell|^2/(\pi^2M_E^4)\) and the charge weights are omitted, and
\[
a_X=\frac{30/\epsilon_{\rm IR}+30L_M+70}{720},
\qquad b_X=\frac{21}{720},
\]
\[
a_L=\frac{12/\epsilon_{\rm IR}+12L_M+25}{288},
\qquad b_L=\frac1{48},
\qquad c_S=\frac1{192}.
\]
The source coefficient is fixed independently by the Ward identity:
\[
R F_{p,L,\rm hard}+QF_{q,L,\rm hard}
=\frac{P'^3-P^3}{192\pi^2M_E^4}.
\]
The transverse coefficients follow by subtracting \(c_S\mathcal B_S\) and dividing the remaining \(F_p\) by \(Q\); the \(F_q\) equation gives the same result exactly.

The charge projections are therefore
\[
\begin{array}{c|ccc}
 &\mathcal B_P&\mathcal B_Q&\mathcal B_S\\ \hline
U(1)_X & q_Ea_X&q_Eb_X&0\\
U(1)_Y & -a_X+\frac12a_L&-b_X+\frac12b_L&\frac12c_S\\
SU(2)_L & T^a a_L&T^a b_L&T^a c_S
\end{array}
\]
in the same common normalization. In particular, the hypercharge coefficients are
\[
a_Y=-\frac{60/\epsilon_{\rm IR}+60L_M+155}{2880},
\qquad b_Y=-\frac3{160},
\qquad c_Y=\frac1{384}.
\]

As a finite full-amplitude cross-check, after adding the ordinary-line EFT soft contribution the same decomposition gives
\[
a_X^{\rm full}=\frac{30\ell_Q+20}{720},\quad
b_X^{\rm full}=\frac{21}{720},\quad
c_X^{\rm full}=0,
\]
\[
a_L^{\rm full}=\frac{12\ell_Q+5}{288},\quad
b_L^{\rm full}=\frac1{48},\quad
c_L^{\rm full}=\frac1{192},
\qquad \ell_Q=\ln\frac{Q}{M_E^2},
\]
which reconstructs the finite form factors in §5G and preserves the scalar-source Ward difference. The \(\ell_Q\) terms are nonlocal EFT/full-amplitude information and are not local Wilson coefficients.

The reproducible exact projection is in calculations/RC-001-QLD-dim8-form-factor-projection.py; its output is validation/RC-001-QLD-dim8-form-factor-projection.txt.

**Interpretation and limitation.** This closes the polynomial projection of the already-computed one-background hard amplitude onto three independent off-shell amplitude representatives. It does **not** establish a complete nonredundant dimension-eight SMEFT basis. The displayed \(\mathcal O_P,\mathcal O_Q,\mathcal O_S\) are representatives for this restricted amplitude, not proof that no other operator maps onto the same columns or that these representatives survive unchanged after IBP/EOM/gauge-EOM reduction. The hard coefficients retain hard-region IR poles and are not finite renormalized Wilson coefficients. The full two-Higgs/two-lepton Green-basis projection, non-Abelian completion, source/current companions, counterterms, and other \(O(M_E^{-4})\) channels remain open.


## 5M. Full electroweak covariant completion

The Abelian relation in §5K extends to the adjoint-covariant \(SU(2)_L\) field-strength insertion. The matrix-ordered commutator, the \(SU(2)\) \(\delta^{ab}/\epsilon^{abc}\) decomposition, the mixed \(B\)-\(W\) two-background contacts, and the corresponding gauge-EOM current representatives are derived in [the non-Abelian IBP/EOM completion note](RC-001-QLD-nonabelian-IBP-EOM-completion.md). The exact SymPy checks are archived in calculations/RC-001-QLD-nonabelian-IBP-EOM-audit.py and validation/RC-001-QLD-nonabelian-IBP-EOM-audit.txt.

This closes the algebraic non-Abelian IBP/commutator map for the restricted Higgs-current representatives. It does not close the complete current basis, all off-shell mixed-background matching, counterterms, or the final renormalized dimension-eight Wilson vector.


## 5N. Derivative-aware source-square Fierz and covariant IBP ledger

The source-square contribution is organized in [RC-001-QLD8-derivative-Fierz-IBP-ledger.md](RC-001-QLD8-derivative-Fierz-IBP-ledger.md). For any two Higgs-doublet sources,
\[
(D_\mu J_A^\dagger)(D^\mu J_B)\doteq-J_A^\dagger D^2J_B,
\]
because \(J_A^\dagger D^\mu J_B\) is a gauge singlet. Expanding the Laplacian of a bilinear gives the two endpoint-Laplacian terms and the mixed derivative term. This identity applies to the complete product-rule sum; it does not equate the individual four placements.

The ledger tracks the derivative on each original fermion through the crossed spinor Fierz rearrangement. In particular, the \((0,1)\) and \((1,0)\) placements put both derivatives into one of the Fierz-rearranged bilinears. The \(RL,LR,RR,LL\) Fierz-difference evanescents are assigned channel by channel in the fixed open-line NDR convention.

This is a tree-level operator identity and derivative bookkeeping result. It does not evaluate the remaining fermion-EOM reductions, one-loop evanescent mixing, same-order EFT soft insertions, or finite UV-minus-EFT Wilson coefficients.


## 5O. Second-order fermion EOM for the source-square Laplacians

The endpoint Laplacians in §5N are now mapped using the leading renormalizable fermion EOMs in [RC-001-QLD8-second-order-fermion-EOM-map.md](RC-001-QLD8-second-order-fermion-EOM-map.md). With \(D_\mu=\partial_\mu+i\mathcal A_\mu\), \([D_\mu,D_\nu]=i\mathscr F_{\mu\nu}\), and \(\sigma^{\mu\nu}=i[\gamma^\mu,\gamma^\nu]/2\),
\[
D^2\psi=\slashed D^2\psi-\frac12\sigma^{\mu\nu}\mathscr F_{\mu\nu}\psi.
\]
For \(Q_L,u_R,d_R,L_e,e_R\), the resulting second-order EOMs produce Higgs-derivative and gauge-field-strength four-fermion structures. The mixed term \(2(D_\mu\bar f)Y D^\mu\chi\) remains because the first-order Dirac EOM fixes only the gamma trace.

The retained source fermions are all neutral under the model \(U(1)_X\); their curvatures contain QCD, \(SU(2)_L\), and/or hypercharge fields, but no \(F_X\). The exact convention audit checks the Minkowski Clifford algebra, the Dirac-square curvature sign, the Higgs hypercharge of each source, and this \(U(1)_X\) neutrality.

Important scheme boundary: the four scalar-pair Fierz-difference evanescents do not close the basis after second-order EOM substitution. New \(\gamma^\mu D_\mu H\) and \(\sigma^{\mu\nu}F_{\mu\nu}\) structures require their own d-dimensional Fierz-difference evanescents before loop renormalization. No complete evanescent mixing matrix or finite Wilson coefficient is claimed.


## 5P. Chiral Fierz projections after second-order EOM substitution

The second-order EOMs in §5O generate scalar–vector products from \(\gamma^\mu D_\mu H\) and scalar–tensor products from \(\sigma^{\mu\nu}\mathscr F_{\mu\nu}\). Their exact four-dimensional Fierz projections are recorded in [RC-001-QLD-EOM-generated-chiral-Fierz-identities.md](RC-001-QLD-EOM-generated-chiral-Fierz-identities.md). The exact matrix audit verifies 16 scalar–vector identities, 12 opposite-chirality scalar–tensor identities, and 6 same-chirality scalar–tensor identities, for 8704/8704 exact components, plus six chiral tensor self-duality relations.

The operator-level projections include the Grassmann reordering minus sign. The corresponding d-dimensional Fierz-difference evanescents are defined by subtracting these four-dimensional operator projections, with all derivative, Higgs, field-strength, color, weak, and flavor labels preserved.

This completes the displayed four-dimensional spinor algebra needed for the second-order EOM-generated Dirac structures. It does not close the full d-dimensional one-loop evanescent counterterm basis, calculate its mixing matrix, or produce finite UV-minus-EFT Wilson coefficients.


## 5Q. Explicit d-dimensional Fierz-difference definitions for EOM-generated channels

The EOM-generated scalar–vector and scalar–tensor channels now have explicit minimal Fierz-difference definitions in [RC-001-QLD-EOM-generated-chiral-Fierz-identities.md](RC-001-QLD-EOM-generated-chiral-Fierz-identities.md). The \(E_{XY;V}^{\mu,rs}\) definitions cover all four scalar–vector chiral combinations; \(E_{RL;T}^{\mu\nu,rs}\) and \(E_{LR;T}^{\mu\nu,rs}\) cover the opposite-chirality tensor channels including their Levi-Civita terms; and \(E_{RR;T}^{i,rs}\), \(E_{LL;T}^{i,rs}\) cover the same-chirality tensor channels in the independent three-component chiral basis.

Each evanescent is the original operator minus its four-dimensional operator-level Fierz projection, so the Grassmann reordering sign is included. The definitions use no \(O(\epsilon)\) physical-operator admixture at the definition stage and retain the original derivative/Higgs/curvature labels.

This defines the tree-level Fierz-difference set for the displayed EOM-generated structures. It is not asserted to close the one-loop counterterm basis; UV-generated higher gamma strings and the evanescent mixing matrix remain to be computed.
