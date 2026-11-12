# P1-IIIa: Relativistic finite-temperature free-Fermi-gas response

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Scope

This stage implements the **nucleon phase-space response** for a relativistic, non-interacting, finite-temperature neutron/proton gas. It adds Fermi motion and final-state nucleon Pauli blocking to the free-target kinematics.

It is deliberately **not yet the complete weak collision kernel**. The vector/axial single-nucleon tensor, weak magnetism, finite-size form factors, and the leptonic contraction are the next stage. No B.2 opacity, luminosity, pure-vector Fig. 7 curve, or axial-vector constraint is changed.

## 2. Dynamic structure factor

For neutral-current scattering on a fixed nucleon species \(N=n,p\), define
\[
q_0=E_\nu-E_\nu',\qquad q=|\mathbf k-\mathbf k'|,
\]
and
\[
E_p=\sqrt{p^2+M_N^2},\qquad
f_N(p)=\frac{1}{e^{(E_p-\mu_N)/T}+1}.
\]

The spin-summed ideal-gas response is
\[
S_N(q_0,q)=
2\int\frac{d^3p}{(2\pi)^3}\,
2\pi\delta(q_0+E_p-E_{|\mathbf p+\mathbf q|})
f_N(p)\,[1-f_N(|\mathbf p+\mathbf q|)].
\]

The factor 2 is the nucleon spin degeneracy. With the convention above, \(S_N\) has units of MeV\(^2\), and
\[
\int\frac{dq_0}{2\pi}S_N(q_0,q)
=
2\int\frac{d^3p}{(2\pi)^3}
f_N(p)[1-f_N(|\mathbf p+\mathbf q|)]
\]
is the static structure factor.

Choosing \(\mathbf q\) along the \(z\)-axis, the energy delta function fixes
\[
\cos\theta_{pq}=
\frac{2q_0E_p+q_0^2-q^2}{2pq},
\]
with Jacobian \(E_{p+q}/(pq)\). Therefore the 3D integral reduces to
\[
\boxed{
S_N(q_0,q)=
\frac{1}{\pi q}
\int_{p_{\min}}^\infty dp\,
p(E_p+q_0)f_N(E_p)
[1-f_N(E_p+q_0)]
}
\]
for \(|q_0|<q\). The lower limit is the exact relativistic boundary at which \(|\cos\theta_{pq}|=1\).

This is the relativistic-dispersion extension of the finite-temperature phase-space response defined by Reddy, Prakash and Lattimer. Their Sec. III uses nonrelativistic baryon energies; their Eqs. (14), (16), and (17) explicitly retain the Fermi factors, energy-conserving delta function, and angular Jacobian. The present calculation replaces the nonrelativistic dispersion by \(\sqrt{p^2+M_N^2}\). [Reference](https://arxiv.org/abs/astro-ph/9710115).

## 3. Thermodynamic benchmark

To avoid importing an unverified proton fraction from another stellar model, this first numerical test uses an explicitly illustrative composition:
\[
T=3.03\ {\rm MeV},\qquad Y_p=0.10,
\]
with
\[
n_B/n_0=10^{-3},\ 10^{-2},\ 10^{-1},\qquad n_0=0.16\ {\rm fm}^{-3}.
\]

The neutron and proton chemical potentials are solved independently from
\[
n_N=\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f_N(p).
\]
The quoted \(\mu_N\) includes the nucleon rest mass; the table gives \(\mu_N-M_N\).

| \(n_B/n_0\) | Species | \(p_F\) (MeV) | \(\mu_N-M_N\) (MeV) | \(e^{(\mu_N-M_N)/T}\) |
|---:|:---:|---:|---:|---:|
| \(10^{-3}\) | n | 32.00 | -8.618 | 0.0582 |
| \(10^{-3}\) | p | 15.38 | -15.324 | 0.00636 |
| \(10^{-2}\) | n | 68.94 | -1.099 | 0.6959 |
| \(10^{-2}\) | p | 33.14 | -8.286 | 0.0649 |
| \(10^{-1}\) | n | 148.52 | +10.920 | 36.74 |
| \(10^{-1}\) | p | 71.40 | -0.705 | 0.7923 |

These are controlled ideal-gas test points, not a claim that the real SFHo-18.8 profile has \(Y_p=0.10\) or these density values at a particular radius.

## 4. Pauli-blocking result

To isolate final-state nucleon blocking, I evaluated
\[
\mathcal P_N(q)=
\frac{S_N(q_0^{\rm recoil},q)\big|_{1-f_f}}
     {S_N(q_0^{\rm recoil},q)\big|_{1}},
\qquad
q_0^{\rm recoil}=\sqrt{M_N^2+q^2}-M_N.
\]

This is the suppression of the **response phase space** on the stationary-target recoil line, not a complete cross-section correction.

| \(n_B/n_0\) | Species | \(q=30\) MeV | \(q=100\) MeV | \(q=200\) MeV | \(q=500\) MeV |
|---:|:---:|---:|---:|---:|---:|
| \(10^{-3}\) | n | 0.9763 | 0.9950 | 0.99997 | 1.0000 |
| \(10^{-3}\) | p | 0.9973 | 0.99945 | 1.0000 | 1.0000 |
| \(10^{-2}\) | n | 0.8018 | 0.9490 | 0.99970 | 1.0000 |
| \(10^{-2}\) | p | 0.9736 | 0.9945 | 1.0000 | 1.0000 |
| \(10^{-1}\) | n | 0.2919 | 0.5467 | 0.99147 | 1.0000 |
| \(10^{-1}\) | p | 0.7839 | 0.9432 | 0.99966 | 1.0000 |

The trend is clear:

- At the dilute \(10^{-3}n_0\) benchmark, final-state blocking is only a few percent at \(q=30\) MeV and negligible by \(q\ge100\) MeV.
- At \(10^{-1}n_0\), neutron blocking is substantial at \(q=30\) and \(100\) MeV.
- At \(q\ge200\) MeV, blocking is already small in these test points, and at \(500\) MeV it is numerically negligible.

This supports the P1-Ic conclusion that low-\(q\) response corrections should not be promoted to a universal high-energy opacity multiplier.

## 5. Thermal energy-transfer spectrum

The response itself contains both \(q_0>0\) (the nucleon gas gains energy) and \(q_0<0\) (the nucleon gas gives energy to the neutrino). At fixed \(q\), I computed the response-weighted mean and standard deviation of \(q_0\), and the fraction of the uncontracted response integral at \(q_0<0\).

For neutrons:

| \(n_B/n_0\) | \(q\) (MeV) | \(\langle q_0\rangle\) (MeV) | \(\sigma_{q_0}\) (MeV) | \(q_0<0\) response fraction |
|---:|---:|---:|---:|---:|
| \(10^{-3}\) | 30 | 0.484 | 1.711 | 0.3882 |
| \(10^{-3}\) | 100 | 5.308 | 5.644 | 0.1735 |
| \(10^{-3}\) | 200 | 20.900 | 11.116 | 0.03096 |
| \(10^{-3}\) | 500 | 123.925 | 25.166 | \(1.75\times10^{-6}\) |
| \(10^{-1}\) | 30 | 1.212 | 2.633 | 0.3167 |
| \(10^{-1}\) | 100 | 9.156 | 6.749 | 0.09846 |
| \(10^{-1}\) | 200 | 24.113 | 13.405 | 0.03006 |
| \(10^{-1}\) | 500 | 123.189 | 34.572 | \(1.11\times10^{-5}\) |

At low momentum transfer, thermal motion creates a broad response with a substantial negative-\(q_0\) tail. At large \(q\), the recoil energy dominates and the negative-\(q_0\) fraction becomes extremely small.

These are **response-only** fractions. They are not the final probability that an outgoing neutrino gains energy: that requires contraction with the weak tensor, neutrino phase space, and the actual daughter spectrum.

## 6. Independent checks

The implementation passes the following checks:

| Check | Maximum relative residual |
|---|---:|
| Number-density equation | \(6.42\times10^{-12}\) |
| Detailed balance \(S(-q_0,q)=e^{-q_0/T}S(q_0,q)\) | \(7.83\times10^{-11}\) |
| Dynamic/static structure-factor sum rule | \(4.80\times10^{-13}\) |
| 300- vs 900-node response integration | \(4.29\times10^{-14}\) |

The nonrelativistic analytic response was also compared with the relativistic result. At \(q\le30\) MeV the maximum difference is 0.715% in the dilute neutron benchmark, while at \(q=500\) MeV it reaches 18.8%. Thus the nonrelativistic recoil dispersion should not be extrapolated to the highest daughter momenta.

## 7. What this does and does not establish

Established:

1. The finite-temperature nucleon phase-space response can be evaluated without Garching raw data.
2. Fermi motion naturally broadens the energy-transfer distribution.
3. Pauli blocking is strongly dependent on density, species, and momentum transfer; it is not a universal scale factor.
4. Relativistic nucleon dispersion matters at the high-\(q\) end.

Not yet established:

- the full vector/axial weak collision kernel;
- weak-magnetism and finite-size form-factor effects inside the moving-nucleon medium integral;
- EOS-consistent \(m_N^*(r)\), \(U_N(r)\), and \(Y_p(r)\);
- RPA, NN correlations, or other in-medium response effects;
- a B.2 escape probability or a revised cooling limit.

## 8. Next step: P1-IIIb

The next implementation is the full weak-current tensor:
\[
W^{\mu\nu}_N(q_0,q)=
\int \frac{d^3p}{(2\pi)^3}
\frac{f_N(p)[1-f_N(p')]}{4E_pE_{p'}}
\,2\pi\delta(q_0+E_p-E_{p'})
\,\frac12\mathrm{Tr}
[(\slashed p'+M_N)\Gamma^\mu
(\slashed p+M_N)\bar\Gamma^\nu].
\]

The lepton tensor will then be contracted with \(W_N^{\mu\nu}\), keeping the neutrino/antineutrino antisymmetric contribution. The mandatory validation is the dilute, zero-temperature stationary-target limit against the existing Horowitz kernel before any finite-density result is used in B.2.

Only after that will we insert same-snapshot \(n_B(r)\), \(Y_p(r)\), and \(T(r)\) inputs. RPA and NN correlations remain a separate subsequent layer.

## Reproducibility

- Script: \`audit_b16_p1iii_a_relativistic_fermi_gas_response.py\`
- Output: \`outputs/p1iii_a_relativistic_fermi_gas_response_2026-11-10.json\`
- Horowitz baseline: \`audit_b16_p1i_horowitz_transport_moments.py\`

## References

1. S. Reddy, M. Prakash, and J. M. Lattimer, “Neutrino interactions in hot and dense matter,” Phys. Rev. D 58, 013009 (1998), arXiv:astro-ph/9710115.
2. S. Reddy, M. Prakash, J. M. Lattimer, and J. A. Pons, “Effects of Strong and Electromagnetic Correlations on Neutrino Interactions in Dense Matter,” Phys. Rev. C 59, 2888 (1999), arXiv:astro-ph/9811294.
3. C. J. Horowitz, “Weak magnetism for antineutrinos in supernovae,” Phys. Rev. D 65, 043001 (2002), arXiv:astro-ph/0109209.
