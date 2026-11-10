# P1-B thermodynamic-input sensitivity of high-energy B.2 neutrino opacity

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV; \(210\leq\omega\leq510\) MeV  
Profile file: \`data/sfho188_digitized.csv\`  
Profile Git blob: \`e41df78c8035540760fbcb7ef592cd830171822e\`

## 1. Question

After the P1 path and radial-opacity numerical checks, determine whether the thermodynamic inputs \(T(r)\) and \(\mu_{\nu_\mu}(r)\) used by the B.7--B.10 neutrino inverse-decay kernel have enough local leverage to plausibly explain the fixed-\(\omega\) strong-endpoint discrepancy.

This is a local-kernel sensitivity audit, not a new global B.1+B.2 luminosity scan. No profile is shifted, refitted, or substituted.

## 2. Method

At selected radii, evaluate the reduced inverse-decay opacity directly:
\[
\Gamma_{\nu,\mathrm{red}}^*(\omega,r)
=(e^{\omega/T}-1)\frac{m_V^2}{8\pi\omega}
\left[I(\mu_{\nu_\mu},\omega,T,v_V)+I(0,\omega,T,v_V)\right],
\qquad
v_V=\sqrt{1-m_V^2/\omega^2}.
\]
The Fermi-pair integral is evaluated independently with a 512-point Gauss--Legendre angular quadrature. The local logarithmic sensitivities are estimated by symmetric finite differences:
\[
S_T=\frac{\partial\ln\Gamma^*}{\partial\ln T},\qquad
S_\mu=\frac{\partial\ln\Gamma^*}{\partial\ln|\mu_{\nu_\mu}|}.
\]
At \(\mu_{\nu_\mu}=0\), the second expression is not used; instead, a finite \(0.1\) MeV perturbation is tested. The exact identity \(I(\mu)=I(-\mu)\) is also checked numerically.

## 3. Results

Representative local logarithmic derivatives:

| Radius | \(T\) (MeV) | \(\mu_{\nu_\mu}\) (MeV) | \(S_T\), \(\omega=210\) MeV | \(S_T\), \(\omega=510\) MeV |
|---:|---:|---:|---:|---:|
| 8 km | 38.85 | -20.43 | -0.324 | -0.116 |
| 10 km | 33.93 | -10.22 | -0.281 | -0.101 |
| 12.5 km | 23.88 | -2.59 | -0.187 | -0.069 |
| 17 km | 7.41 | +1.58 | -0.0405 | -0.0163 |
| 18 km | 5.92 | +1.52 | -0.0405 | -0.0163 |
| 22 km | 3.55 | 0 | -0.0240 | -0.00975 |
| 24 km | 3.22 | 0 | -0.0217 | -0.00882 |

Thus, a 1% local temperature change produces approximately a 0.9--0.32% change in the local reduced neutrino opacity across the sampled 210--510 MeV, 8--24 km domain. The largest response occurs at the inner end and lowest sampled energy. This is a local derivative; it is not a direct percentage change in the integrated luminosity.

The chemical-potential sensitivity is much smaller. At 8 km, the largest sampled \(|S_\mu|\) is \(1.66\times10^{-2}\); at 10 km it is \(4.66\times10^{-3}\); at 12.5 km it is below \(4.0\times10^{-4}\). In the outer positive-\(\mu_{\nu_\mu}\) support region, a \(0.1\) MeV change at 17--18 km changes the local opacity by at most \(3.5\times10^{-5}\) (0.0035%) over the sampled energies. The sign flip \(\mu_{\nu_\mu}\to-\mu_{\nu_\mu}\) changes the local pair kernel by less than \(2\times10^{-15}\) relative, consistent with its exact evenness.

The two active neutrino contributions are nearly equal in the sampled high-energy band: the nonzero-\(\mu_{\nu_\mu}\) contribution supplies approximately 49.6--50.0% of the local pair sum. This does not mean the chemical potential is irrelevant; rather, its actual magnitude has weak leverage at these high energies.

## 4. Important profile-support detail

The digitized \(\mu_{\nu_\mu}(r)\) profile is not a single negative branch that smoothly tends to zero. It has:
- a negative branch ending near \(13.10993\) km;
- a zero interval;
- a positive branch beginning near \(16.58818\) km and ending near \(18.42300\) km.

The positive outer branch was explicitly sampled at 16.588, 17, 17.5, 18, and 18.423 km. It is small in absolute magnitude and its effect on the high-energy pair kernel is correspondingly small. The exact zero interval and support endpoints are preserved from the public-figure reconstruction; they are not silently filled or smoothed.

The kernel is even in \(\mu_{\nu_\mu}\), so a sign-convention change alone cannot explain the opacity discrepancy. A change in the *magnitude* or radial support would have to be assessed as a different profile input, not as a sign correction.

## 5. Interpretation and decision

1. The B.7--B.10 local kernel has been independently evaluated in the sampled high-energy domain.
2. The high-energy neutrino opacity is more sensitive to \(T(r)\) than to the plotted \(\mu_{\nu_\mu}(r)\) magnitude.
3. The sign of \(\mu_{\nu_\mu}\) is immaterial to this pair kernel; its magnitude and support are the relevant profile data.
4. The local derivatives are too small to motivate an arbitrary chemical-potential rescaling. They do not establish a global luminosity uncertainty and must not be promoted to one.
5. This calculation does not explain the \(+92.24\%\) fixed-\(\omega\) strong-endpoint residual. It does not replace the need for the original same-snapshot Garching profile.

## 6. Next P1-B action

The next meaningful step is a source/provenance cross-check of the exact \(T(r)\), \(\mu_{\nu_\mu}(r)\), and lapse curves used to reconstruct the SFHo-18.8 background, especially the digitized support boundaries and the outer continuation. The existing Caputo-versus-Ferreira \(\mu_\mu\) comparison concerns the *charged-muon* chemical potential entering the Compton target distribution; it must not be conflated with \(\mu_{\nu_\mu}\) in the inverse-decay kernel.

The original archive access remains a separate provenance issue. No credentials or restricted files are requested, accessed, or committed here.

No source normalization, opacity, coupling, profile, Fig. 7 curve, or axial-vector result is modified.
