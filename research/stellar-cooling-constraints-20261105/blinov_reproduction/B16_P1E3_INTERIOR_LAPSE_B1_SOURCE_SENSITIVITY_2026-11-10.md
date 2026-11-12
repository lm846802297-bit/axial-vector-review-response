# P1-E3: Interior lapse sensitivity of the B.1 source

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, pure vector, \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1\) s  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Question

The weak-coupling endpoint is nearly optically thin, and the current high-resolution B.1 source is \(9.0303\%\) below the digitized Fig. 7 weak point. The outer 24--25 km lapse continuation changes the full B.1+B.2 strong-point luminosity by at most \(0.0262\%\), while broad \(\mu_{\nu_\mu}\) source stresses change B.1 by at most \(1.17\%\).

The remaining lapse question is whether a normalization error in the *interior*, where most B.1 emission occurs, could account for the weak-end deficit.

## 2. Method

The B.1 expression is evaluated with the local-energy convention:
\[
L_{\rm thin}=4\pi\int dr\,r^2N(r)^2
\int_{m_V/N(r)}^\infty d\omega\,
\frac{\sqrt{\omega^2-m_V^2}\,\omega^2}{2\pi^2}
\Gamma_{\rm prod}(r,\omega).
\]

Only the lapse is changed. For each selected shell, the diagnostic is
\[
N(r)\longrightarrow s_N N(r),
\]
with \(s_N=0.95,0.97,0.99,1.01,1.03,1.05\). The exact lower limit \(m_V/[s_NN(r)]\) is recomputed at every source-radius node, as is the \(N^2\) source measure. \(T,\mu_\mu,\mu_{\nu_\mu}\), all local kernels, the coupling, and the radial/energy integration prescription are held fixed.

Two shells are tested:
- the dominant \(8\)--\(15\) km source region;
- the broader \(5\)--\(15\) km source region.

The higher-resolution run uses 200 source-radius nodes and 520 energy nodes (320 logarithmic base nodes plus the baseline threshold knots). The 100-radius/260-energy run is retained as a joint refinement check. This is a B.1 source-only sensitivity test; no B.2 opacity is altered.

## 3. Source distribution

In the higher-resolution baseline, the B.1 source fractions are:
- \(5\)--\(8\) km: \(17.4724\%\);
- \(8\)--\(10\) km: \(39.9126\%\);
- \(10\)--\(12\) km: \(26.0426\%\);
- \(12\)--\(15\) km: \(13.6971\%\).

Thus \(8\)--\(15\) km supplies \(79.6522\%\) of the source and \(5\)--\(15\) km supplies \(97.1247\%\).

The baseline weak-point source is
\[
L_{\rm thin}^{\rm base}=9.90960\times10^{51}\ {\rm erg\,s^{-1}},
\]
compared with
\[
L_{\rm Fig.7}=1.08933\times10^{52}\ {\rm erg\,s^{-1}}.
\]
The source-only residual is \(-9.0303\%\).

## 4. Lapse stress tests

The higher-resolution changes in the total B.1 source are:

| Lapse rescaling | \(8\)--\(15\) km only | \(5\)--\(15\) km only |
|---|---:|---:|
| \(-5\%\) | \(-7.7960\%\) | \(-9.5045\%\) |
| \(-3\%\) | \(-4.7251\%\) | \(-5.7606\%\) |
| \(-1\%\) | \(-1.5908\%\) | \(-1.9395\%\) |
| \(+1\%\) | \(+1.6067\%\) | \(+1.9588\%\) |
| \(+3\%\) | \(+4.8675\%\) | \(+5.9344\%\) |
| \(+5\%\) | \(+8.1916\%\) | \(+9.9872\%\) |

The source response is stable under joint radial-and-energy refinement. The required multiplicative lapse shifts to make the *optically-thin weak point* equal the digitized Fig. 7 value are:

| Rescaled region | Required \(s_N\) | Required relative increase |
|---|---:|---:|
| \(8\)--\(15\) km | 1.06029 | \(+6.029\%\) |
| \(5\)--\(15\) km | 1.04970 | \(+4.970\%\) |

The lower-resolution roots are \(+5.930\%\) and \(+4.887\%\), respectively. The required shifts are therefore stable to about \(0.1\) percentage point under the joint refinement.

## 5. Comparison with the independent lapse visualization

The current lapse profile is independently corroborated by Zuowei Liu's 2026-10-31 presentation, slide 65. The visual read-offs and current profile values at \(r=(0,5,10,15,20)\) km differ by absolute amounts
\[
(0.00133,-0.00132,0.00136,-0.00150,-0.00111).
\]
The presentation is rasterized and supports only a qualitative comparison at the level of a few \(10^{-3}\); it is not a precision numerical profile.

The lapse increase required by the B.1 source match corresponds to an absolute \(\Delta N\) of roughly \(0.04\)--\(0.05\) across the dominant source region. This is approximately 27--38 times the independent visual read-off differences. The required shift is therefore not supported by the available independent lapse visualization.

This comparison is not a formal uncertainty bound: the original Garching lapse table remains unavailable. It does show that a lapse correction large enough to repair the weak-end source deficit would be conspicuous in the independent public plot.

## 6. Interpretation and decision

1. The outer 24--25 km lapse continuation is negligible for the global luminosity.
2. The interior lapse would need to be raised by about \(5\%\)--\(6\%\) over the dominant emission region to match the weak Fig. 7 source.
3. The independent lapse visualization differs from the current profile only at the few-\(10^{-3}\) absolute read-off level, not at the \(0.04\)--\(0.05\) level required.
4. An interior lapse mismatch is therefore not a plausible explanation of the weak-end source deficit within the available public evidence.
5. No lapse value is changed, and no fit to Fig. 7 is made.

Machine-readable results are in \`outputs/b16_inner_lapse_b1_source_sensitivity_10mev_2026-11-10.json\`. The standalone V8 implementation is \`audit_b16_inner_lapse_b1_source_sensitivity.js\`.

## 7. P1-E status

The three current-profile source/provenance tests are now complete:
- P1-E1: outer 24--25 km lapse continuation in full B.1+B.2;
- P1-E2: \(\mu_{\nu_\mu}\) and \(\mu_{\nu_\tau}=0\) sensitivity in the B.1 source;
- P1-E3: interior lapse normalization sensitivity in the B.1 source.

Together with the existing temperature, \(\mu_\mu/T\), and absolute-muon-density audits, these tests do not identify a supported profile adjustment that explains the weak-end source residual. The current public-figure reconstruction remains the working baseline; the original Garching profile remains unavailable.

The strong-endpoint \(+92.26\%\) fixed-\(\omega\) B.1+B.2 mismatch remains a separate propagation/reproduction problem. Do not apply an opacity rescaling, change \(R_{\max}\), or update the axial-vector curve.

## References

1. N. Blinov et al., *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, Sec. 4.1 and Appendix B, Eq. (B.1), https://doi.org/10.1007/JHEP06(2026)155.
2. Z. Liu, *Supernova constraints on millicharged particles and lepton-flavor-violating axions*, 7th Joint Workshop on the Standard Model and Beyond, 2026-10-31, slide 65.
3. R. Bollig et al., *Muons in Supernovae: Implications for the Axion-Muon Coupling*, arXiv:2005.07141v7.
