# Flavor-resolved neutrino opacity: fixed omega versus path redshift

**Status:** numerical audit completed; four unit tests pass and both path-column closures are verified.  
**Scope:** \(m_V=10\) MeV, pure-vector B.14--B.16 benchmark, digitized SFHo-18.8 \(t_{\rm pb}=1\) s background. The source term and all background profiles are held fixed.

## 1. Two prescriptions

The published Appendix-B baseline is
\[
\tau(r,\omega)=\int_0^{s_{\max}}ds\,
\frac{\Gamma_{\rm abs}^{*}(r'(s),\omega)}{v_V(\omega)},
\]
with the same \(\omega\) argument along the chord [Blinov et al., Eq. (B.2)]. Gravitational source redshift is already included in the B.1 luminosity integral through \(N(r)^2\) and the lower bound \(m_V/N(r)\).

The independent sensitivity diagnostic instead imposes conserved energy at infinity,
\[
E_\infty=N(r_{\rm src})\omega_{\rm src},\qquad
\omega_{\rm loc}(s)=\frac{E_\infty}{N(r'(s))}
=\omega_{\rm src}\frac{N(r_{\rm src})}{N(r'(s))},
\]
and updates the local rates and \(v_V(s)\). It deliberately retains the Euclidean chord length \(ds\); it is not a full GR ray-tracing calculation and is not substituted for Eq. (B.2).

## 2. Flavor decomposition

For the \(L_\mu-L_\tau\) vector, the neutrino production kernel is the sum
\[
\Gamma_{\nu,\rm prod}
=\frac{m_V^2}{8\pi\omega}
\left[
I\!\left(\frac{\mu_{\nu_\mu}}{T},\frac{\omega}{T},v_V\right)
+I\!\left(0,\frac{\omega}{T},v_V\right)
\right].
\]
The two terms are \(\nu_\mu\bar\nu_\mu\) and \(\nu_\tau\bar\nu_\tau\), respectively. The latter uses \(\mu_{\nu_\tau}=0\), as in the published calculation. Each flavor is separately converted to reduced absorption using
\[
\Gamma_{\rm abs}^{*}
=(e^{\omega/T}-1)\Gamma_{\rm prod}.
\]

The audit computes the optical-depth contribution of each flavor in each radial shell for both energy prescriptions. It also includes the semi-Compton and dimuon channels in the total optical depth so that flavor-removal tests are performed against the same full escape exponent as the baseline.

## 3. Numerical closure and interpretation

The audit requires:

1. fixed-\(\omega\) shell columns summed over \(\nu_\mu,\nu_\tau\), Compton, and dimuon to reproduce the direct Eq. (B.2) total optical depth;
2. path-redshift shell columns to reproduce the independent path-redshift total optical depth on escaping source-energy bins;
3. \(\nu_\mu\) and \(\nu_\tau\) columns to agree when \(\mu_{\nu_\mu}=0\);
4. flavor-removal diagnostics to leave non-escaping modes non-escaping (their infinite optical-depth barrier is not subtracted).

The luminosity-removal factor is
\[
\frac{L_{\rm without\ selected\ opacity}}{L_{\rm baseline}},
\]
with the Eq. (B.1) source held fixed. It is a diagnostic attribution, not a new physical supernova model or an exclusion curve.

**Interpretation rule:** only the fixed-\(\omega\) result is compared to the published Fig. 7 curve. The path-redshift result quantifies sensitivity to an alternative energy prescription, with the limitation that the metric path-length factor is not included.

## 4. Numerical result: 10 MeV benchmark

The dedicated GitHub Actions run completed all four unit tests. The shell-column closure residuals are:

- fixed-\(\omega\) all-channel shell sum: \(6.72\times10^{-16}\);
- fixed-\(\omega\) \(\nu_\mu+\nu_\tau\) production-rate sum: \(2.81\times10^{-16}\);
- path-redshift all-channel shell sum on escaping bins: \(8.60\times10^{-16}\).

The fraction of source weight in gravitationally non-escaping bins is only \(3.24\times10^{-5}\).

### 4.1 Source-weighted mean optical depths

All entries below are per unit \(g_{\mu\tau}^2\).

| Channel | Fixed \(\omega\) | Path redshift | Change |
|---|---:|---:|---:|
| \(\nu_\mu\bar\nu_\mu\) | \(4.1264\times10^{15}\) | \(4.3866\times10^{15}\) | +6.31% |
| \(\nu_\tau\bar\nu_\tau\) | \(4.1982\times10^{15}\) | \(4.4543\times10^{15}\) | +6.10% |
| Semi-Compton | \(9.4779\times10^{14}\) | \(9.4743\times10^{14}\) | -0.038% |
| Dimuon | 0 | 0 | -- |
| **All channels** | \(9.2723\times10^{15}\) | \(9.7883\times10^{15}\) | **+5.57%** |

The path-redshift prescription changes the neutrino opacity appreciably more than the semi-Compton opacity.

### 4.2 Radial dependence

The outer-shell fraction of the source-weighted mean optical depth is

\[
f_{\tau}(r\geq15\,\mathrm{km})=
\begin{cases}
56.76\%,&\text{fixed }\omega,\\
58.75\%,&\text{path-redshift diagnostic}.
\end{cases}
\]

The ratio of path-redshift to fixed-\(\omega\) neutrino optical depth in the outer shells is:

| Shell | \(\nu_\mu\) ratio | \(\nu_\tau\) ratio |
|---|---:|---:|
| 15--16.5 km | 1.049 | 1.049 |
| 16.5--18.5 km | 1.071 | 1.071 |
| 18.5--20 km | 1.090 | 1.090 |
| 20--22 km | 1.105 | 1.105 |
| 22--25 km | 1.121 | 1.121 |

The two flavors respond almost identically outside 15 km because the reconstructed \(\mu_{\nu_\mu}\) is small there and vanishes in the outer profile. The effect is not driven by a large outer muon-neutrino chemical potential.

### 4.3 Luminosity-removal diagnostic

At the common luminosity-peak coupling \(g=1.1341\times10^{-8}\), removing selected outer opacity gives:

| Removed opacity | Fixed \(\omega\) | Path redshift |
|---|---:|---:|
| Outer \(\nu_\mu\) | 1.301 | 1.331 |
| Outer \(\nu_\tau\) | 1.301 | 1.331 |
| Both outer neutrino flavors | 1.756 | 1.845 |

At the strong-absorption endpoint \(g=4.1717\times10^{-8}\), the corresponding factors are 5.329, 5.331, and 113.90 for fixed \(\omega\), compared with 6.009, 6.011, and 157.15 for the path-redshift diagnostic. These large endpoint factors arise because the baseline luminosity is already exponentially suppressed; they are not standalone physical limits.

At the luminosity peak, the path-redshift-only luminosity is 5.2% below the fixed-\(\omega\) value. At the strong-absorption endpoint it is about 28.9% lower. The peak remains at the same sampled coupling in this scan.

## 5. Conclusion

The main physical conclusion is stable under the energy-prescription comparison:

- the outer optical depth is carried predominantly by inverse decay into neutrino pairs;
- \(\nu_\mu\) and \(\nu_\tau\) contribute almost equally in the outer layers;
- the outer contribution does not require a large outer \(\mu_{\nu_\mu}\);
- allowing the local energy to redshift along the path strengthens the outer neutrino opacity by roughly 5--12% shell by shell, while leaving the semi-Compton contribution almost unchanged.

The path-redshift result remains a sensitivity diagnostic, not a replacement for the published fixed-\(\omega\) Eq. (B.2) benchmark. A full GR ray calculation would also require the proper spatial line element and a consistent treatment of the ray geometry. No such correction is inferred from this comparison.

Machine-readable output: \`outputs/b16_flavour_fixed_vs_redshift_10mev_2026-11-08.json\`.

## References

N. Blinov, P. J. Fox, K. J. Kelly, R. Plestid, and T. Zhou, “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B, Eqs. (B.1)--(B.19).
