# Independent local neutrino-kernel audit: Eqs. (B.7)--(B.10)

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Purpose

The high-energy phase-space audit showed that neutrino inverse decay is the dominant contribution to the B.16 opacity in the \(210\text{--}510\) MeV escape bin. The local neutrino kernel is therefore checked against the paper's own closed-form expression, rather than only against a second implementation of the same repository formula.

The comparison covers \(r=8,\ 10,\ 12.5,\ 15\) km; \(\omega=60,\ 110,\ 210,\ 510,\ 1010\) MeV; and both active flavours, represented by \(\mu_{\nu_\mu}(r)\) and \(\mu_{\nu_\tau}=0\).

## 2. Eq. (B.9): published closed form versus repository kernel

The published expression is evaluated as
\[
I(\alpha,\beta,v)=
\frac{
\ln\!\left[
\frac{
\left(e^\alpha+e^{\frac12\beta(v+1)}\right)
\left(e^{\alpha+\frac12\beta(v+1)}+1\right)}
{e^{\alpha+\beta}
+(e^{2\alpha}+1)e^{\frac12\beta(v+1)}
+e^{\alpha+\beta v}}
\right]}
{(e^\beta-1)\beta v},
\]
where \(\alpha=\mu_\nu/T\), \(\beta=\omega/T\), and \(v=\sqrt{1-m_V^2/\omega^2}\).

The second numerator factor is \(e^{\alpha+\beta(v+1)/2}+1\). This placement of \(\alpha\) in the exponent is important for the exact identity.

<badge color="success">40-point comparison agrees at machine precision</badge>

The maximum absolute relative residual between the Eq. (B.9) expression and the repository's analytic Fermi-pair average is
\[
\boxed{\max|\delta I|=2.89\times10^{-15}}.
\]

A separate direct angular integral of the original Fermi-Dirac product,
\[
\frac12\int_{-1}^{1}d\cos\vartheta\,
f\!\left(\frac{\omega}{2}(1+v\cos\vartheta),\mu_\nu\right)
f\!\left(\frac{\omega}{2}(1-v\cos\vartheta),-\mu_\nu\right),
\]
agrees with the repository antiderivative to the following maximum residuals:

| Direct Gauss-Legendre order | Maximum absolute relative residual |
|---:|---:|
| 128 | \(2.89\times10^{-15}\) |
| 256 | \(3.11\times10^{-15}\) |
| 512 | \(2.66\times10^{-15}\) |
| 1024 | \(3.11\times10^{-15}\) |

This checks the same local Fermi-pair phase-space integral in three independent forms: the repository antiderivative, the published Eq. (B.9), and direct angular quadrature.

## 3. Eq. (B.7): polarization and flavour normalization

For one neutrino flavour, the paper uses
\[
\Gamma_{V\to\nu\bar\nu}=\frac16\alpha_Vm_V,
\qquad \alpha_V=\frac{g^2}{4\pi},
\]
and
\[
\Gamma_{\nu\bar\nu\to V}^{\rm prod}(\omega)
=\frac{m_V}{\omega}\,3\Gamma_{V\to\nu\bar\nu}\,
I(\mu_\nu/T,\omega/T,v).
\]
Consequently,
\[
\frac{1}{g^2}\frac{m_V}{\omega}\,3\Gamma_{V\to\nu\bar\nu}
=\frac{m_V^2}{8\pi\omega}.
\]
This is exactly the prefactor used in the repository rate. The two-flavour source is the sum \(I(\mu_{\nu_\mu})+I(0)\), with the nonzero and zero chemical-potential contributions evaluated separately.

The relative residual in the B.7 prefactor and two-flavour rate normalization is zero at the algebraic level in this comparison.

## 4. Eqs. (B.10) and (B.4): detailed balance

The paper states
\[
\Gamma_{\rm prod}=e^{-\omega/T}\Gamma_{\rm abs}.
\]
Combining this with the reduced-absorption definition gives
\[
\Gamma_{\rm abs}^*
=(1-e^{-\omega/T})\Gamma_{\rm abs}
=(e^{\omega/T}-1)\Gamma_{\rm prod}.
\]
The independently evaluated factors agree exactly at the tested points in double precision. This is the factor used to construct the channel-separated reduced opacity in the B.2 audit.

## 5. What this rules out

The high-energy neutrino source and reduced-absorption **local kernels** used in the B.16 calculation agree with the published B.7--B.10 expressions and with direct angular integration. The large Fig. 7 discrepancy is therefore not explained by:

- a missing factor of three from the vector-polarization sum;
- a missing factor from summing the two neutrino flavours;
- an incorrect local Fermi-pair angular average;
- an incorrect local detailed-balance reduction.

This is a local-kernel validation. It does not validate the reconstructed \(T(r)\), \(\mu_{\nu_\mu}(r)\), or lapse profiles, nor does it by itself establish the full B.1 source integration.

## 6. Reproducibility and scope

- Machine-readable result: \`outputs/b16_neutrino_b7_b9_kernel_10mev_2026-11-10_v8.json\`
- Reproduction script: \`audit_b16_neutrino_b7_b9_kernel.py\`
- The archived numerical comparison is from direct V8 double-precision execution. The Python/NumPy script is added as the repository reproduction implementation and was not executed in this V8 session.
- No source normalization, profile, opacity prescription, coupling, or axial-vector curve is changed.
