# P1-IIIb: Full weak-current tensor — implementation and validation specification

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## Scope and status

This note specifies the next implementation layer after P1-IIIa. It is a derivation/validation specification, **not a claim that the full tensor code or B.2 calculation has already been completed**. P1-IIIa remains a scalar ideal-gas phase-space response. No opacity, luminosity, Fig. 7 curve, or axial constraint is updated here.

## 1. Conventions

Use metric \(g^{\mu\nu}=(+,-,-,-)\), \(q^\mu=k^\mu-k'^\mu=p'^\mu-p^\mu\), and \(Q^2=-q_\mu q^\mu\geq0\). The on-shell nucleon momenta obey
\[
p^\mu=(E_p,\mathbf p),\quad p'^\mu=(E_p+q_0,\mathbf p+\mathbf q),\quad
E_p=\sqrt{p^2+M_N^2}.
\]

For each species \(N=n,p\), use
\[
\Gamma_N^\mu(q)=F_1^N(Q^2)\gamma^\mu
+i\frac{F_2^N(Q^2)}{2M_N}\sigma^{\mu\alpha}q_\alpha
-G_A^N(Q^2)\gamma^\mu\gamma^5.
\]
The sign and index placement of the Pauli term must be matched to the exact Horowitz convention before numerical comparison. Define
\[
\overline\Gamma^\nu=\gamma^0(\Gamma^\nu)^\dagger\gamma^0,\qquad
H_N^{\mu\nu}=\frac12\mathrm{Tr}[
(\slashed p'+M_N)\Gamma_N^\mu
(\slashed p+M_N)\overline\Gamma_N^\nu].
\]
The trace includes the initial-spin average \(1/2\); the medium response separately includes the spin degeneracy 2. Do not add a second spin factor.

## 2. Medium response tensor

The convention to implement is
\[
W_N^{\mu\nu}(q_0,q)=
2\pi\int\frac{d^3p}{(2\pi)^3}
\frac{f_N(E_p)[1-f_N(E_p+q_0)]}{4E_p(E_p+q_0)}
\delta(q_0+E_p-E_{p'})
\,2H_N^{\mu\nu}.
\]
Equivalently, absorb the final factor 2 into the spin-summed hadronic tensor. This convention must be fixed once in code and checked against the stationary-target limit; never mix the two versions.

The energy delta function fixes
\[
\cos\theta_{pq}=
\frac{2E_pq_0+q_0^2-q^2}{2pq},
\]
with
\[
\left|\frac{\partial(E_p-E_{p'})}{\partial\cos\theta_{pq}}\right|
=\frac{pq}{E_{p'}}.
\]
After azimuthal averaging, the tensor reduces to a one-dimensional integral over \(p\ge p_{\min}\). Unlike the scalar response, the tensor integrand retains the angular dependence of \(p^\mu\), so each tensor component must be evaluated with the kinematically fixed \(\cos\theta_{pq}\). It is not permissible to set \(\mathbf p=0\) inside this integral.

## 3. Leptonic contraction

For neutrinos, use
\[
L_{\mu\nu}=8[k'_\mu k_\nu+k'_\nu k_\mu
-g_{\mu\nu}(k\cdot k')+i\epsilon_{\mu\nu\alpha\beta}k'^\alpha k^\beta],
\]
with the sign of the antisymmetric term reversed for antineutrinos, subject to the chosen \(\epsilon^{0123}\) convention. The collision kernel is proportional to \(G_F^2 L_{\mu\nu}W_N^{\mu\nu}\), together with the explicitly documented external-state and phase-space normalization.

Keep VV, AA, VA, weak-magnetism, and finite-\(Q^2\) contributions. Do not discard \(W^{0i}\), spatial longitudinal/transverse pieces, or antisymmetric components before contraction.

## 4. Required validation ladder

1. **Gamma algebra:** verify Hermiticity/conjugation of the vertex and tensor symmetry properties numerically for generic on-shell momenta.
2. **Stationary target:** take a dilute, cold, zero-momentum target limit and reproduce Horowitz's \(d\sigma/d\cos\theta\) for \(\nu n,\bar\nu n,\nu p,\bar\nu p\), including recoil, weak magnetism, and the same form factors.
3. **Integrated moments:** reproduce total, angular-transport, momentum-transfer, and energy-transfer moments from the existing Horowitz implementation. A total-cross-section-only match is insufficient.
4. **Dilute thermal gas:** verify the Maxwell-Boltzmann limit and detailed balance.
5. **Finite density:** verify Pauli blocking species by species and demonstrate that the result is not represented by a universal multiplicative suppression.
6. **Quadrature:** independently increase radial and angular orders and test near the kinematic boundaries \(q_0=\pm q\).

Acceptance target for the stationary-target differential kernel is a relative residual below \(10^{-3}\) over the supported angular/energy grid, followed by a tighter convergence study for integrated moments. Any failure must be resolved before the kernel is used in B.2.

## 5. Benchmark separation

The P1-IIIa choice \(T=3.03\) MeV, \(Y_p=0.10\), and \(n_B/n_0=10^{-3},10^{-2},10^{-1}\) is an illustrative ideal-gas benchmark only. It is not an extracted SFHo-18.8 radial snapshot. EOS-consistent application requires co-located \(n_B(r),Y_p(r),T(r)\), and, if used, \(m_N^*(r)\), \(U_N(r)\), and chemical potentials from one and the same stellar model.

## 6. Explicit exclusions

This stage does not yet include RPA, NN correlations, in-medium vertex corrections, additional baryons, neutrino final-state blocking, general-relativistic path transport, or a solution of the Boltzmann equation. In particular, \(e^{-\tau_{\rm therm}}\) is not to be used as an escape probability.

## 7. Next executable task

Implement the tensor trace and its azimuthal average in a standalone local-kernel module. First compare the \(p\to0\) limit pointwise against the existing Horowitz differential kernel. Only after that test passes should the finite-\(T\), finite-density integrations be enabled. Keep this code and its validation outputs separate from the production B.2 path until acceptance.
