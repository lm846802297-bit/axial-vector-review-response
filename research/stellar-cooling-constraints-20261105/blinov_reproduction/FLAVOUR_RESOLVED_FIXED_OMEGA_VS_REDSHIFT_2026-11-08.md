# Flavor-resolved neutrino opacity: fixed omega versus path redshift

**Status:** independent comparison implemented; numerical audit is run by the dedicated GitHub Actions workflow.  
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

## References

N. Blinov, P. J. Fox, K. J. Kelly, R. Plestid, and T. Zhou, “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B, Eqs. (B.1)--(B.19).
