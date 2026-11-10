# B5-2B3 — \(Q_{LD}\) pure-\(WW\) cross-box numerator and hard-master audit

**Date:** 2026-11-11  
**Gauge:** Feynman gauge, \(d=4-2\epsilon\).  
**Status:** the four cross-vertex box numerator families have been reduced in a declared canonical routing, and the required hard scalar masters have been evaluated. The weak-tensor-weighted result below is explicitly **conditional** on the still-unverified relative Feynman-rule orientations and multiplicities. It is not yet a Wilson coefficient.

## 1. Reduce the six attachment classes before integrating

The tree-level \(Q_{LD}\) exchange has external lines \(\bar L,L,H^\dagger,H\). The six \(WW\) pair contractions are fixed in the upstream exact SU(2) audit:

| Pair | Line pair | Weak tensor |
|---|---|---:|
| LD-W-01 | \(\bar L-L\) | \(-T_3/4\) |
| LD-W-02 | \(\bar L-H^\dagger\) | \(+T_3/4\) |
| LD-W-03 | \(\bar L-H\) | \(-3T_0/4\) |
| LD-W-04 | \(L-H^\dagger\) | \(-3T_0/4\) |
| LD-W-05 | \(L-H\) | \(+T_3/4\) |
| LD-W-06 | \(H^\dagger-H\) | \(-T_3/4\) |

Here
\[
T_0=\delta_{ij}\delta_{kl},\qquad
T_3=\sigma^I_{ij}\sigma^I_{kl}=2T_x-T_0.
\]

The same-vertex pairs LD-W-03 and LD-W-04 are pure light-field Yukawa-vertex corrections. The upstream UV–EFT subtraction ledger proves that their complete gauge-covariant subfamilies, including the corresponding EFT insertion/contact set, reproduce the same \(O(M_E^{-2})\) tree kernel and cancel in the hard difference. They must remain in the Ward/contact bookkeeping, but they do not supply a new hard coefficient at this order.

Thus the hard \(WW\) box problem is restricted to four cross-vertex pairs:
\[
\boxed{\mathrm{LD-W-01,\ LD-W-02,\ LD-W-05,\ LD-W-06}.}
\]
There is no \(WEE\) vertex and no heavy-\(E\) \(WW\) self-energy or heavy-containing Yukawa-vertex correction, because \(E\) is an \(SU(2)_L\) singlet.

## 2. Scalar hard masters

Use the upstream normalization
\[
\int_k\equiv \mu_R^{2\epsilon}
\int\frac{d^dk}{i\pi^{d/2}},
\qquad
L=\ln\frac{M_E^2}{\mu_R^2}.
\]

The representative box master is
\[
J(M_E)=\int_k\frac{1}{(k^2)^2(k^2-M_E^2)}.
\]
Its full and soft parts retain separate UV and IR poles:
\[
J_{\rm full}=\frac{\Delta_{\rm IR}+1-L}{M_E^2},
\qquad
J_{\rm soft}=\frac{-\Delta_{\rm UV}+\Delta_{\rm IR}}{M_E^2}.
\]
Therefore
\[
\boxed{J_{\rm hard}=\frac{\Delta_{\rm UV}+1-L}{M_E^2}.}
\]

The denominator expansion also produces
\[
K(M_E)=\int_k\frac{1}{k^2(k^2-M_E^2)^2}.
\]
Feynman parametrization gives
\[
K(M_E)=
\frac{\Gamma(1+\epsilon)}{\epsilon-1}
\frac{1}{M_E^2}
\left(\frac{\mu_R^2}{M_E^2}\right)^\epsilon
=-\frac{1}{M_E^2}+O(\epsilon).
\]
Its soft expansion is proportional to the scaleless integral \(\int_k1/k^2\), so it has no logarithmic UV/IR pole at \(\epsilon=0\). For the hard numerator coefficients needed here,
\[
\boxed{K_{\rm hard}=-\frac{1}{M_E^2}.}
\]

The tensor reductions are
\[
\int_k\frac{k_\mu k_\nu}{(k^2)^3(k^2-M_E^2)}
=\frac{g_{\mu\nu}}{d}J(M_E),
\]
\[
\int_k\frac{k_\mu k_\nu}{(k^2)^2(k^2-M_E^2)^2}
=\frac{g_{\mu\nu}}{d}K(M_E).
\]
The second relation is the source of the \(K\) master when the heavy propagator denominator is expanded to first order in the external momentum.

## 3. Canonical numerator routing

For the numerator audit, take a common routing with gauge momentum \(k\), heavy momentum \(P-k\), and common denominator
\[
(k^2)^3\big[(P-k)^2-M_E^2\big].
\]
\(P\) is the soft momentum whose \(\slashed P\) coefficient matches the derivative structure in \(Q_{LD}\). The following are explicitly defined numerator representatives; their overall diagram signs are not included.

### 3.1 Fermion–fermion pair: LD-W-01

Define
\[
N_{FF}=
\gamma^\mu\slashed k(\slashed P-\slashed k)
\slashed k\gamma_\mu.
\]
Expand
\[
\frac{1}{(P-k)^2-M_E^2}
=
\frac{1}{k^2-M_E^2}
+\frac{2k\cdot P}{(k^2-M_E^2)^2}
+O(P^2).
\]
Using
\[
\langle k_\mu k_\nu\rangle
=\frac{g_{\mu\nu}}{d}k^2
\]
and
\[
\gamma^\mu\gamma^\alpha\gamma_\mu=(2-d)\gamma^\alpha,
\]
the coefficient of \(\slashed P\) is
\[
\boxed{
A_{FF}(d)=
\frac{(d-2)^2}{d}J
+\frac{2(d-2)}{d}K.
}
\]

### 3.2 Fermion–scalar pair: LD-W-02 and LD-W-05

For the canonical scalar momentum numerator \(k_\mu\), define
\[
N_{FS}=\gamma^\mu\slashed k
(\slashed P-\slashed k)k_\mu.
\]
Contracting \(k_\mu\gamma^\mu=\slashed k\) gives
\[
N_{FS}=k^2(\slashed P-\slashed k).
\]
The same first-order expansion yields
\[
\boxed{
A_{FS}(d)=J-\frac{2}{d}K.
}
\]
The two mixed pairs have this same canonical Lorentz kernel before their individual scalar-flow and fermion-arrow signs are assigned.

### 3.3 Scalar–scalar pair: LD-W-06

For the canonical product of scalar momentum numerators \(+k^2\), define
\[
N_{SS}=k^2(\slashed P-\slashed k).
\]
It is algebraically identical to the reduced \(N_{FS}\), hence
\[
\boxed{A_{SS}(d)=A_{FS}(d)}
\]
for this canonical routing. The sign of the actual scalar-vertex product must still be obtained from the oriented \(H/H^\dagger\) Feynman rules; it is not contained in this equality.

## 4. Retain \(O(\epsilon)\) before multiplying the UV pole

At \(d=4-2\epsilon\),
\[
\frac{(d-2)^2}{d}
=1-\frac32\epsilon+O(\epsilon^2),
\qquad
\frac{2(d-2)}{d}
=1-\frac12\epsilon+O(\epsilon^2),
\]
\[
\frac{2}{d}
=\frac12+\frac14\epsilon+O(\epsilon^2).
\]

Substituting \(J_{\rm hard}\) and \(K_{\rm hard}\), and retaining the \(O(\epsilon)\) coefficient multiplying the UV pole in \(J\), gives
\[
\boxed{
A_{FF}^{\rm hard}
=\frac{1}{M_E^2}
\left(\Delta_{\rm UV}-L-\frac32\right),
}
\]
\[
\boxed{
A_{FS}^{\rm hard}=A_{SS}^{\rm hard}
=\frac{1}{M_E^2}
\left(\Delta_{\rm UV}-L+\frac32\right).
}
\]
The difference between the fermion–fermion and fermion–scalar/scalar–scalar canonical kernels is finite:
\[
\boxed{
A_{FS}^{\rm hard}-A_{FF}^{\rm hard}
=\frac{3}{M_E^2}.
}
\]
In particular, replacing \(d\) by four before the UV-pole multiplication would miss the \(-3/2\) finite shift in \(A_{FF}\).

## 5. Oriented numerator signs and the cross-box subset

Fix the external field ordering to
\[
\bar L_i(p_1),\ H_j(p_2),\ H_k^\dagger(p_3),\ L_l(p_4),
\]
with \(p_1=p_3=0\), \(p_2=P\), \(p_4=-P\) for the projector, and let the gauge momentum \(k\) flow from the left Yukawa vertex to the right one. The heavy momentum along the \(E_R\to\bar E_R\) arrow is \(P-k\).

Use the Feynman rules following from
\[
\mathcal L_W=
g_2\bar L\gamma^\mu T^I L\,W_\mu^I
+i g_2 H^\dagger T^I\overleftrightarrow{\partial^\mu}H\,W_\mu^I.
\]
For this routing, the internal fermion propagator momentum is \(-k\) on each fermion-attached line, and each scalar gauge vertex contributes \(-k_\mu\). The four numerator chains are then:

| Pair | Internal numerator factors | Reduced numerator | Relative numerator sign |
|---|---|---|---:|
| LD-W-01 | \(\gamma^\mu(-\slashed k)\slashed{(P-k)}(-\slashed k)\gamma_\mu\) | \(N_{FF}\) | \(+\) |
| LD-W-02 | \(\gamma^\mu(-\slashed k)\slashed{(P-k)}(-k_\mu)\) | \(N_{FS}\) | \(+\) |
| LD-W-05 | \((-k_\mu)\slashed{(P-k)}(-\slashed k)\gamma^\mu\) | \(N_{FS}\) | \(+\) |
| LD-W-06 | \((-k_\mu)(-k_\nu)g^{\mu\nu}\slashed{(P-k)}\) | \(N_{SS}\) | \(+\) |

The two Yukawa vertices, two gauge vertices, internal matter propagators, heavy propagator and Feynman-gauge \(W\) propagator have the same net \(i\)-factor in all four topologies. Reversing the gauge momentum is the same graph under \(k\mapsto-k\); for the fixed ordered external amplitude there is one exchange contraction per unordered line pair. The hermitian-conjugate external amplitude is the complex conjugate and is not an additional factor of two in this Green function.

Combining the four oriented numerator chains with the exact weak tensors gives
\[
\begin{aligned}
\mathcal A_{\rm box}^{WW,\rm hard}
&\propto
-\frac14 A_{FF}^{\rm hard}T_3
+\frac14 A_{FS}^{\rm hard}T_3
+\frac14 A_{FS}^{\rm hard}T_3
-\frac14 A_{SS}^{\rm hard}T_3\\
&=\frac14(A_{FS}^{\rm hard}-A_{FF}^{\rm hard})T_3\\
&=\boxed{\frac{3}{4M_E^2}T_3.}
\end{aligned}
\]
The UV pole and matching logarithm cancel in this four-box tensor sum. Restoring the common coupling and loop factor, the raw amputated amplitude subset in this convention is
\[
\boxed{
\Gamma_{\rm box}^{WW,\rm hard}
=-i\,\frac{|y_\ell|^2g_2^2}{16\pi^2}
\frac{3}{4M_E^2}\,
T_3\,\slashed P
}
\]
with the tree amplitude convention
\[
\Gamma_{\rm tree}
=-i\,\frac{|y_\ell|^2}{M_E^2}\,
T_0\,\slashed P.
\]
Equivalently, the coefficient of this **raw \(T_3\) amplitude tensor only** is \(+3|y_\ell|^2g_2^2/(64\pi^2M_E^2)\).

This is a completed canonical cross-box numerator/hard-integral sub-block under the stated momentum and Feynman-rule conventions. It is **not** yet the final \(C_{HL}^{(3)}\), \(C_{LD}\), or any other nonredundant Wilson coefficient: the tensor still has to be embedded in the complete gauge-covariant operator basis, combined with external-field/parameter/operator counterterms, and checked against the summed Ward/Slavnov–Taylor identity. No FeynArts/FeynCalc diagram-package reproduction has been performed.

## 6. Required completion before coefficient promotion

Still required:
1. Fix the all-incoming/outgoing momentum and fermion-arrow convention separately for LD-W-01, 02, 05 and 06.
2. Derive the scalar \(H/H^\dagger\) gauge-vertex momentum factors and the fermion propagator numerators in the same convention.
3. Establish whether the four pair classes have equal or different overall signs and whether additional crossed routings occur.
4. Add the external \(L,H\) LSZ/self-energy pieces and the \(g_2,y_\ell,C_{LD}\) parameter/operator counterterms exactly once.
5. Verify the summed weak Ward/Slavnov–Taylor identity. There is no direct \(W\) contact at the \(Q_{LD}\) derivative insertion, but the external-doublet attachments are mandatory.
6. Perform the UV–EFT subtraction with the same nonexceptional external momenta or shared IR regulator, then project \(T_0,T_3\) and the EOM/current structures.

The companion script b5_2b3_qld_ww_crossbox_tensor_kernels.py reproduces the scalar-master and canonical numerator algebra. Its six regression tests validate this kernel layer only. No complete \(WW\) Wilson coefficient, anomalous dimension, or Ward-identity closure is claimed.
