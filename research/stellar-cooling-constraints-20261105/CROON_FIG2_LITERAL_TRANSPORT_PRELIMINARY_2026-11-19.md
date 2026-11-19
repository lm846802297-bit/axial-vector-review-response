# Croon Fig. 2: literal transport reconstruction (preliminary)

Date: 2026-11-19

## Status

This is the first independent numerical implementation of the Croon et al. (2021) vector luminosity prescription. It is a **preliminary public-profile reconstruction**, not yet a quantitative reproduction of the digitized Fig. 2 points. It does not alter the validated Blinov B.2/B.13 baseline and it is not an axial-vector result.

The implementation is deliberately isolated as lane C0. It uses Croon's own local-rate approximations and Sec. 3 transport prescription without importing Blinov's velocity factor, reduced opacity, lapse/redshift, or the Lai trapping prescription.

## Literal equations implemented

Croon Eq. (4.6), per \(g_{Z'}^2\), is the generic **single-neutrino-flavour** expression,

\[
\Gamma_{\nu\bar\nu,\,\rm generic}^{\rm prod}/g_{Z'}^2
=\frac{m_{Z'}^2}{12\pi\omega}\,
\frac{1}{e^{\omega/T}-1}.
\]

For the actual \(U(1)_{L_\mu-L_\tau}\) model, Croon Sec. 4.4 explicitly states that both \(\nu_\mu\) and \(\nu_\tau\) contribute. We therefore apply the factor of two to **both** the differential production power and the absorptive optical depth:

\[
\Gamma_{\nu\bar\nu,\,L_\mu-L_\tau}^{\rm prod}/g_{Z'}^2
=2\,\Gamma_{\nu\bar\nu,\,\rm generic}^{\rm prod}/g_{Z'}^2,
\qquad
\Gamma_{\nu\bar\nu,\,L_\mu-L_\tau}^{\rm abs}/g_{Z'}^2
=2\,\Gamma_{\nu\bar\nu,\,\rm generic}^{\rm abs}/g_{Z'}^2.
\]

The factor of two is a model-flavour multiplicity, not a vector-polarization factor. The B.7 rate is not substituted.

Croon Eq. (4.7), per \(g_{Z'}^2\), is implemented as

\[
\Gamma_{\gamma\mu}^{\rm prod}/g_{Z'}^2
=\frac{2\alpha_{\rm EM}}{3m_\mu^2}
(n_\mu F_{\rm deg})
\sqrt{1-\frac{m_{Z'}^2}{\omega^2}}\,
\frac{1}{e^{\omega/T}-1}.
\]

The susceptibility \(n_\mu F_{\rm deg}\) is evaluated from the single \(\mu^-\) Fermi-Dirac distribution used in Bollig et al. Eq. (2), including the two muon spin states. Antimuons are not added to this Croon-literal lane. A separate charge-summed sensitivity check finds the \(\mu^+\) susceptibility is at most about 1.5% of the \(\mu^-\) susceptibility in the muon-rich region; it remains a separate convention, not part of C0.

Detailed balance is imposed as

\[
\Gamma_{\rm abs}=e^{\omega/T}\Gamma_{\rm prod},
\]

so the local absorption expressions contain \(1+f_B\). The generic one-flavour outer \(R_\nu\to R_{\rm far}\) opacity retains the vacuum \(Z'\to\nu\bar\nu\) decay tail,

\[
\tau_{\nu,\rm out}^{\rm generic}/g_{Z'}^2
=(R_{\rm far}-R_\nu)\frac{m_{Z'}^2}{12\pi\omega},
\]

with \(R_{\rm far}=100\) km. No extra \(1/v_{Z'}\) is inserted in the radial optical-depth integral because Croon Eq. (3.3) does not contain it. For the \(L_\mu-L_\tau\) transfer, the same neutrino vacuum tail and the interior neutrino absorption are both multiplied by two, as stated in Sec. 4.4.

The luminosity integral is

\[
L_{Z'}=\int_0^{R_\nu}4\pi r^2dr
\int_{m_{Z'}}^\infty d\omega\,
\frac{\sqrt{\omega^2-m_{Z'}^2}\,\omega^2}{2\pi^2}
\Gamma_{\rm prod}(\omega,r)e^{-\tau_{\rm abs}(\omega,r)}.
\]

The factor of \(\omega\) from the emitted energy is already included in the \(k\omega^2\) phase-space measure after changing variables from \(k\) to \(\omega\). It must not be multiplied a second time.

The Croon Raffelt line is \(3\times10^{52}\) erg/s. The largest plotted mass, 200 MeV, is below \(2m_\mu=211.3168\) MeV, so the dimuon channel is closed throughout this Fig. 2 mass set.

## Profile and numerical setup

Croon Fig. 2 uses SFHo-18.8. The public profile available to this project is a Caputo-based reconstruction cross-checked against Bollig figures; it is not the raw Garching simulation file used by Croon. The code records the profile SHA-256 and source-row count in its output.

The \(T=3\) MeV boundary is obtained by linearly extrapolating the final two profile points:

\[
R_\nu=25.1511683\ {\rm km}.
\]

The main Fig. 2 C0 run uses the generic single-neutrino-flavour Eq. (4.6) normalization. The separate \(U(1)_{L_\mu-L_\tau}\) extension applies the Sec. 4.4 factor of two to both neutrino production and absorption; it is not folded into the generic Fig. 2 curve. Both lanes use the single \(\mu^-\) susceptibility convention. The Fig. 2 run uses:

- \(R_{\rm far}=100\) km;
- \(r\)-grid spacing 0.05 km, with the last nonzero and first zero muon-profile points retained;
- 160-point transformed energy Gauss quadrature, \(\omega=m+T_{\max}y^2\), \(0\le y\le6\);
- 256-point Gauss-Legendre momentum quadrature for \(n_\mu F_{\rm deg}\);
- cumulative Simpson integration for \(\tau_{\rm abs}\) and Simpson integration for the volume integral;
- 81 logarithmic couplings from \(10^{-11}\) to \(10^{-1}\).

The 0.1 eV curve is also computed with \(R_{\rm far}=R_\nu\), corresponding to the dashed-boundary comparison described in the Fig. 2 caption.

## Preliminary numerical results

The table below is the current **generic single-neutrino-flavour Fig. 2 benchmark**. It uses Croon Eq. (4.6) as written for the muon-number-coupled reference. The separate Sec. 4.4 \(L_\mu-L_\tau\) extension, which doubles both the neutrino source and opacity, is not included in these six curves. These values remain preliminary until compared with digitized points from the original figure:

| \(m_{Z'}\) | Peak \(g_{Z'}\) | Peak \(L_{Z'}\) [erg/s] | Low-\(g\) crossing of \(3\times10^{52}\) | High-\(g\) crossing |
|---:|---:|---:|---:|---:|
| 0.1 eV | \(7.50\times10^{-8}\) | \(2.244\times10^{55}\) | \(1.672\times10^{-9}\) | \(4.03\times10^{-2}\) |
| 1 eV | \(7.50\times10^{-8}\) | \(2.244\times10^{55}\) | \(1.672\times10^{-9}\) | \(1.75\times10^{-2}\) |
| 10 eV | \(7.50\times10^{-8}\) | \(2.244\times10^{55}\) | \(1.672\times10^{-9}\) | \(3.38\times10^{-3}\) |
| 0.1 MeV | \(7.50\times10^{-8}\) | \(2.229\times10^{55}\) | \(1.672\times10^{-9}\) | \(1.57\times10^{-6}\) |
| 10 MeV | \(1.00\times10^{-8}\) | \(1.049\times10^{54}\) | \(8.61\times10^{-10}\) | \(3.19\times10^{-8}\) |
| 200 MeV | \(7.50\times10^{-10}\) | \(6.325\times10^{52}\) | \(3.41\times10^{-10}\) | \(1.21\times10^{-9}\) |

These are **not yet the final Croon Fig. 2 benchmark numbers**. They are the output of the literal equations on the public-profile reconstruction, before digitized-curve comparison and before profile-systematic bracketing.

The optically-thin source fractions show the expected channel hierarchy:

| \(m_{Z'}\) | Neutrino coalescence fraction | Semi-Compton fraction |
|---:|---:|---:|
| 0.1 eV | \(3.0\times10^{-16}\) | \(1-3.0\times10^{-16}\) |
| 1 eV | \(3.0\times10^{-14}\) | \(1-3.0\times10^{-14}\) |
| 10 eV | \(3.0\times10^{-12}\) | \(1-3.0\times10^{-12}\) |
| 0.1 MeV | \(3.04\times10^{-4}\) | 0.999696 |
| 10 MeV | 0.7439 | 0.2561 |
| 200 MeV | 0.9981 | 0.0019 |

Thus the semi-Compton channel controls the sub-MeV curves, while neutrino coalescence controls the 10 and 200 MeV curves. At 200 MeV, the Thomson semi-Compton approximation contributes below 0.2% of the optically-thin source.

## Numerical checks completed locally

- The thin-limit luminosity scales as \(g_{Z'}^2\); a dedicated \(g=(1,2)\times10^{-12}\) test pair agrees with the exact quadratic scaling to better than \(2\times10^{-5}\). The plotted \(10^{-11}\) lower edge is not forced to be perfectly thin for the 10 MeV case: its small residual outer-decay attenuation is retained.
- The energy quadrature change from order 160 to 240 is below \(10^{-11}\) over the luminosity range used for the crossing extraction.
- The momentum susceptibility at order 256 agrees with order 512 to numerical precision in the muon-rich region.
- Refining the radial integration from 0.1 km to 0.05 km changes the peak luminosities by less than \(0.03\%\); the radial-integrated curve differs by less than about \(0.13\%\) near the high-coupling tail for the low-mass cases when Simpson integration is used.
- The detailed-balance identity \(\Gamma_{\rm abs}/\Gamma_{\rm prod}=e^{\omega/T}\) is satisfied algebraically.
- The outer vacuum decay tail has a visible effect for heavier masses. For \(m=0.1\) eV, \(R_{\rm far}=100\) km and \(R_{\rm far}=R_\nu\) differ by less than \(0.1\%\) at \(g=10^{-2}\), increasing to about 8% at \(g=0.1\).

## What remains before calling this a Fig. 2 reproduction

1. Run the committed full-profile implementation on all 1687 source rows and archive the JSON/CSV output.
2. Digitize Croon Fig. 2 from the original PDF and compare curve positions and luminosities without fitting or tuning any normalization.
3. Quantify the public-profile reconstruction uncertainty, especially \(T(r)\) and \(n_\mu F_{\rm deg}(r)\), against the Bollig SFHo-18.8 profile.
4. Bracket the unknown \(R_\nu\to100\) km finite-temperature opacity between the literal vacuum tail and a \(T=3\) MeV upper envelope.
5. Keep the C0 result separate from the corrected B.13 local-rate lane and from all axial-vector predictions.

No axial-vector curve or SN1987A exclusion is updated by this preliminary calculation.
