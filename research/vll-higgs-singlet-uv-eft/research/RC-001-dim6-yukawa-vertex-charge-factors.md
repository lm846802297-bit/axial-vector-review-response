# RC-001 — Signed charge factors for both conjugate Yukawa vertices

**Status:** charge-conservation and gauge-factor algebra completed for the three line pairs at each of the four Yukawa vertices. This is the vertex-graph input layer, not the loop amplitude: momentum routing, Lorentz numerators, overall Feynman-rule signs, integration, EFT subtraction, and full Ward-identity sum remain open.

## 1. Conventions

Use all fields entering a Yukawa vertex as incoming. Let \(x=Q_X/Q_\ell\), \(\eta_\mu=+1\), and \(\eta_\tau=-1\). For a pair \(i,j\), define the diagonal and mixed charge factors
\[
F_B(i,j)=Y_iY_j,\qquad
F_X(i,j)=x_ix_j,\qquad
F_{BX}(i,j)=Y_ix_j+x_iY_j.
\]
The corresponding coupling prefactors are \(g_Y^2F_B\), \(g_X^2Q_\ell^2F_X\), and \(g_Yg_XQ_\ell F_{BX}\), respectively. The mixed factor applies only when the off-diagonal \(B-A'\) propagator is included; its overall propagator normalization is not absorbed into \(F_{BX}\).

Every listed vertex is separately hypercharge- and \(X\)-charge-neutral. The table retains the signed \(F_{BX}\) factor, rather than merely marking a mixed attachment as allowed.

## 2. \(y_\ell\bar L_\ell H E_{\ell R}\) and its conjugate

### Original vertex: \(\bar L_\ell H E_{\ell R}\)

| Pair | \(F_B=Y_iY_j\) | \(F_X=x_ix_j\) | \(F_{BX}=Y_ix_j+x_iY_j\) |
|---|---:|---:|---:|
| \(\bar L-H\) | \(+1/4\) | \(0\) | \(-\eta_\ell/2\) |
| \(\bar L-E_R\) | \(-1/2\) | \(-1\) | \(+3\eta_\ell/2\) |
| \(H-E_R\) | \(-1/2\) | \(0\) | \(+\eta_\ell/2\) |

### Conjugate vertex: \(\bar E_{\ell R}H^\dagger L_\ell\)

| Pair | \(F_B=Y_iY_j\) | \(F_X=x_ix_j\) | \(F_{BX}=Y_ix_j+x_iY_j\) |
|---|---:|---:|---:|
| \(\bar E_R-H^\dagger\) | \(-1/2\) | \(0\) | \(+\eta_\ell/2\) |
| \(\bar E_R-L\) | \(-1/2\) | \(-1\) | \(+3\eta_\ell/2\) |
| \(H^\dagger-L\) | \(+1/4\) | \(0\) | \(-\eta_\ell/2\) |

The \(W^I\) exchange exists only between the doublet and Higgs legs. With \(T^I=\sigma^I/2\), the singlet contraction at either same-vertex pair is
\[
\sum_I \bar T^I T^I=-C_F\,\mathbf 1=-\frac34\mathbf 1.
\]
No \(W E E\) vertex exists because \(E\) is an \(SU(2)_L\) singlet.

## 3. \(\lambda_\ell S_\ell\bar E_{\ell L}\ell_R\) and its conjugate

### Original vertex: \(S_\ell\bar E_{\ell L}\ell_R\)

| Pair | \(F_B=Y_iY_j\) | \(F_X=x_ix_j\) | \(F_{BX}=Y_ix_j+x_iY_j\) |
|---|---:|---:|---:|
| \(S-\bar E_L\) | \(0\) | \(-2\) | \(+2\eta_\ell\) |
| \(S-\ell_R\) | \(0\) | \(-2\) | \(-2\eta_\ell\) |
| \(\bar E_L-\ell_R\) | \(-1\) | \(+1\) | \(0\) |

### Conjugate vertex: \(S_\ell^\ast\bar\ell_R E_{\ell L}\)

| Pair | \(F_B=Y_iY_j\) | \(F_X=x_ix_j\) | \(F_{BX}=Y_ix_j+x_iY_j\) |
|---|---:|---:|---:|
| \(S^\ast-\bar\ell_R\) | \(0\) | \(-2\) | \(-2\eta_\ell\) |
| \(S^\ast-E_L\) | \(0\) | \(-2\) | \(+2\eta_\ell\) |
| \(\bar\ell_R-E_L\) | \(-1\) | \(+1\) | \(0\) |

The \(B\) boson attaches to the fermion–fermion pair only. The \(A'\) boson can attach to all three pairs. For mixed propagation, the fermion–fermion factor vanishes exactly at both conjugate vertices, while the two scalar–fermion pair factors have opposite signs.

## 4. Vertex-pair to scalar-kernel map

The pair factors above determine which gauge exchange is allowed. The denominator/numerator class is separate:

| Operator / vertex | Pair | Allowed exchange | Scalar-kernel class before overall signs |
|---|---|---|---|
| \(Q_{LD}\), \(\bar LHE_R\) | \(\bar L-H\) | \(B,W\), and conditional \(BA'\) | Purely light fermion–scalar loop; zero-momentum limit is scaleless \(\int_k 1/(k^2)^2\), with UV and IR poles kept separate |
| \(Q_{LD}\), \(\bar LHE_R\) | \(\bar L-E_R\) | \(B,A'\), conditional \(BA'\) | Heavy–light fermion numerator reduces to \(d B_0(0;0,M_E^2)\) |
| \(Q_{LD}\), \(\bar LHE_R\) | \(H-E_R\) | \(B\), conditional \(BA'\) | Heavy–scalar numerator reduces to \(B_0(0;0,M_E^2)\) |
| \(Q_{LD}\), \(\bar E_RH^\dagger L\) | \(\bar E_R-H^\dagger\) | \(B\), conditional \(BA'\) | Heavy–scalar kernel \(B_0(0;0,M_E^2)\) |
| \(Q_{LD}\), \(\bar E_RH^\dagger L\) | \(\bar E_R-L\) | \(B,A'\), conditional \(BA'\) | Heavy–light fermion kernel \(d B_0(0;0,M_E^2)\) |
| \(Q_{LD}\), \(\bar E_RH^\dagger L\) | \(H^\dagger-L\) | \(B,W\), and conditional \(BA'\) | Purely light, scaleless at zero external momenta; common UV/EFT soft bookkeeping required |
| \(Q_{RD}\), \(S\bar E_L\ell_R\) | \(S-\bar E_L\) | \(A'\), conditional \(BA'\) | Heavy–scalar kernel \(B_0(0;0,M_E^2)\) |
| \(Q_{RD}\), \(S\bar E_L\ell_R\) | \(S-\ell_R\) | \(A'\), conditional \(BA'\) | Purely light, scaleless at zero external momenta |
| \(Q_{RD}\), \(S\bar E_L\ell_R\) | \(\bar E_L-\ell_R\) | \(B,A'\); mixed factor exactly zero | Heavy–light fermion kernel \(d B_0(0;0,M_E^2)\) |
| \(Q_{RD}\), \(S^\ast\bar\ell_RE_L\) | \(S^\ast-\bar\ell_R\) | \(A'\), conditional \(BA'\) | Purely light, scaleless at zero external momenta |
| \(Q_{RD}\), \(S^\ast\bar\ell_RE_L\) | \(S^\ast-E_L\) | \(A'\), conditional \(BA'\) | Heavy–scalar kernel \(B_0(0;0,M_E^2)\) |
| \(Q_{RD}\), \(S^\ast\bar\ell_RE_L\) | \(\bar\ell_R-E_L\) | \(B,A'\); mixed factor exactly zero | Heavy–light fermion kernel \(d B_0(0;0,M_E^2)\) |

Here
\[
B_0(0;0,M_E^2)=\Delta_\epsilon+1-\ln\frac{M_E^2}{\mu_R^2}.
\]
The \(d B_0\) and \(B_0\) labels denote only the reduced numerator kernels. They do not include the oriented Feynman-rule signs, the full graph symmetry factors, the \(BA'\) propagator normalization, or the corresponding EFT graph. A scaleless light-only vertex graph must not be dropped before its UV/IR poles are matched against the EFT.

## 5. What this fixes—and what it does not

The tables fix the signed representation/charge products to be inserted into the vertex integrals and prevent accidental sign loss when the conjugate vertices are combined. They do not fix the overall sign from the oriented fermion/scalar propagators or the gauge propagator, nor do they determine the Dirac numerator, finite integral, or local operator coefficient.

The oriented Feynman-rule signs, numerator kernels, UV poles, and finite hard parts for the heavy-containing FF/FS rows are now derived separately in research/RC-001-dim6-heavy-vertex-hard-pieces.md. The remaining work is to combine those sub-blocks with the complete crossed-box set, EFT soft/contact graphs, heavy-line self-energy and counterterms, external-field terms, and the common operator-basis projection; only that summed result can support a full Wilson coefficient.
