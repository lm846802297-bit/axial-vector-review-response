# P1-IIId/e: Garching EOS nucleon distributions and degeneracy benchmarks

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. New source

D. F. G. Fiorillo, A. Gil Muyor, H.-T. Janka, G. G. Raffelt, E. Vitagliano, *Axion-photon conversion in transient compact stars: Systematics, constraints, and opportunities*, JCAP 03 (2026) 053, DOI: 10.1088/1475-7516/2026/03/053, arXiv:2509.13322.

This paper uses the Garching muonic SN models including SFHo-18.8. Section 4.2 states that the models were evolved to 10 s post-bounce and are publicly available upon request. Appendix C.1 explicitly gives the nucleon phase-space distributions consistent with the Garching EOS. This is a more direct microphysical reference for P1-III than a generic free Fermi gas.

## 2. EOS-consistent nucleon occupation

Appendix C.1 gives
\[
f_N(p)=\left\{\exp\left[\frac{U_N+K_N(p)-\mu_N^*}{T}\right]+1\right\}^{-1},
\]
with
\[
K_N(p)=\sqrt{p^2+m_N^{*2}}-m_N^*.
\]
The Garching profiles tabulate \(m_N^*\) and \(U_N\) for \(N=n,p\), as well as \(\mu_N^*\). For SFHo, the effective masses are density dependent and substantially below vacuum masses; the neutron-proton effective-mass difference remains the vacuum splitting, \(m_n^*-m_p^*=1.2933\) MeV.

For same-species elastic neutral-current scattering at fixed radius, the common \(U_N\) cancels from the initial/final energy-conservation difference, but it still enters the occupation through \(U_N-\mu_N^*\). The effective mass changes both the quasiparticle dispersion and the response kinematics. Therefore the present vacuum-mass P1-IIIb kernel remains an ideal-gas benchmark and must not be described as EOS-consistent.

## 3. Published degeneracy-factor validation targets

Section 4.3 defines the recoil-free degeneracy suppression factor
\[
F_{NN}^{\rm deg}=
\frac{\int 2\,d^3p/(2\pi)^3\,f_N(p)[1-f_N(p)]}
{\int 2\,d^3p/(2\pi)^3\,f_N(p)}.
\]
This is a static occupation/Pauli-blocking diagnostic, not the full dynamic scattering response \(W^{\mu\nu}(q_0,q)\).

For SFHo-18.8, Table 1 reports:
- \(T^3\)-weighted averages: \(\langle F_{pp}^{\rm deg}\rangle=0.80\), \(\langle F_{nn}^{\rm deg}\rangle=0.48\);
- \(\rho T^{5/2}\)-weighted averages (in parentheses): \(\langle F_{pp}^{\rm deg}\rangle=0.77\), \(\langle F_{nn}^{\rm deg}\rangle=0.42\).

The same table reports the weighted abundances per baryon:
\[
\begin{array}{c|cc}
& T^3 & \rho T^{5/2}\\
\langle Y_p\rangle&0.138&0.132\\
\langle Y_n\rangle&0.853&0.865\\
\langle Y_e\rangle&0.119&0.111\\
\langle Y_\mu\rangle&0.022&0.022
\end{array}
\]
The averages are over the SN core and the simulation time, without gravitational redshift. They are not \(t_{\rm pb}=1\) s local values and must not be compared directly to the Caputo Fig. 1 snapshot.

A useful composition diagnostic is:
- \(1-\langle Y_p+Y_n\rangle=0.009\) for the \(T^3\) weighting and \(0.003\) for the \(\rho T^{5/2}\) weighting;
- \(\langle Y_e+Y_\mu-Y_p\rangle=0.003\) and \(0.001\), respectively.

If \(Y_n,Y_p\) denote free-nucleon fractions, these differences are consistent with a small emission-weighted bound-nucleus baryon fraction and its positive charge. The ratios of the rounded central values are about \(1/3\), but the table is rounded to three decimals, so this is only a consistency hint, not a precision measurement of cluster \(Z/A\).

## 4. Why these targets matter

The published \(F_{pp}^{\rm deg}\) and \(F_{nn}^{\rm deg}\) values provide a direct independent check of the Fermi occupation, spin degeneracy, and EOS input used in our implementation. They do **not** validate the dynamic angular/energy redistribution kernel by themselves.

The validation ladder should therefore be:
1. Reproduce the local EOS-consistent densities from \(f_N(p)\) using \(m_N^*,U_N,\mu_N^*,T\).
2. Reproduce the published weighted \(F_{pp}^{\rm deg},F_{nn}^{\rm deg}\) with the same time/mass weighting and model.
3. Verify the static \(q_0=0\) response limit against the corresponding occupation integral.
4. Then validate the dynamic \(W_N^{\mu\nu}(q_0,q)\) and the Horowitz dilute/stationary limit.
5. Only then use the EOS-consistent kernel in radial transport.

## 5. Consequences for the current project

- Keep the existing vacuum-mass moving-Fermi-gas code as a controlled ideal-gas comparison.
- Add a separate EOS-quasiparticle branch using \(m_N^*,U_N,\mu_N^*\); do not silently replace the old benchmark.
- The SFHo-18.8 profiles required for a local calculation are not fully present in the cited paper; it says the Garching simulations are available upon request. The published weighted factors are usable as aggregate validation targets.
- The \(T^3\) and \(\rho T^{5/2}\) averages integrate over the model's evolution, so they are not substitutes for the 1 s snapshot needed to compare Fig. 12 with Caputo Fig. 1.
- No B.2 opacity, vector Fig. 7 result, or axial cooling curve is updated.

## 6. Source locations

- Section 4.2 and Table 1: Garching model provenance, weighted abundances, and degeneracy factors.
- Section 4.3, Eq. (4.1): definition of \(F_{NN}^{\rm deg}\).
- Appendix C.1, Eqs. (C.1)–(C.2): EOS-consistent \(f_N(p)\), effective mass, scalar potential, and chemical-potential convention.
- Appendix C.2: Garching lapse convention and its effect on local versus distant-observer energies/rates.
