# Pointwise B.13 + neutrino mode-resolved B.2 adapter audit

**Date:** 2026-11-18  
**Benchmark:** \(m_{A'}=10\) MeV, pure vector, \(g_V/g_X=1\), \(g_A/g_X=0\).  
**Profile:** SFHo-18.8, \(t_{\rm pb}=1\) s, 1687-row public-figure reconstruction.  
**Status:** local channel adapter passes at one high-order radial anchor and three local energies. This is not a radial transport or B.2 luminosity result.

## 1. Reproducible inputs

| Input | SHA-256 |
|---|---|
| Downloaded source-bundle ZIP | `b27c101a063d6f5784d72ef12ad699abc2ceae000b5824cfc4aaa0d191c3474d` |
| SFHo profile | `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c` |
| B.13 local audit kernel | `ff6479a8d6d4ba417dc4b31e745b4028a28d9e42df5598144334453ea9627683` |
| Moving-muon Compton kernel | `38436b94f070069c8696b37b9bce1955e2d5d7e39dad9b302ab754582ff6a5a5` |
| Neutrino rate module | `2fc7bc2d3b0d7b98c191755cd2bb87944e4ebe259adc3d3bbc8e0f60dcc57f56` |

The exact source bundle was recovered from Actions run 43534587169, artifact 14089450366. Its ZIP hash matches the committed provenance record. The local run used the archived source snapshot and did not use GitHub Actions as the compute backend.

The anchor is

\[
r=8.24821831451522\ {\rm km},\quad
T=39.1873531264166\ {\rm MeV},\quad
\mu_\mu=95.5870186126576\ {\rm MeV},\quad
\mu_{\nu_\mu}=-18.9549075346137\ {\rm MeV}.
\]

The B.13 moving-muon kernel uses quadrature order \((26,14,14,14)\); the neutrino inverse-decay kernel uses angular order 64. The local rates are normalized per \(g_X^2\).

## 2. Correct channel combination

For each physical mode \(h\in\{L,+,-\}\), the two independently evaluated channels are

\[
\Gamma_{\rm prod,h}^{\rm tot,Q}
=\Gamma_{\rm prod,h}^{\nu\bar\nu}
+\Gamma_{\rm prod,h}^{\mu\gamma,Q},
\]

\[
\widetilde\Gamma_{\rm abs,h}^{\rm tot,Q}
=(1-e^{-\omega/T})
\left(\Gamma_{\rm abs,h}^{\nu\bar\nu}
+\Gamma_{\rm abs,h}^{\mu\gamma,Q}\right),
\]

where \(Q=\mu^-\) is the primary like-for-like B.17 convention and \(Q=\mu^-+\mu^+\) is a separately retained thermal-gas extension. The exact B.13 kernel supplies charge-resolved rates; the neutrino module supplies the three mode-resolved \(\nu_\mu+\nu_\tau\) rates. No Compton polarization rate is divided by three.

## 3. Numerical results

All values below are local absorption rates per \(g_X^2\), in the source kernel's native units.

| \(x=(\omega-m)/T\) | \(\omega\) (MeV) | B.13 \(R_{LT}\), \(\mu^-\) | B.13 \(R_{LT}\), charge sum | Neutrino \(R_{LT}\) | Total \(R_{LT}\), \(\mu^-\) lane | Total \(R_{LT}\), charge-sum lane |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10.0000 | 1.000160 | 1.000159 | 1.000000 | 1.000042 | 1.000043 |
| 0.015 | 10.5878 | 0.921579 | 0.921539 | 1.000090 | 0.979028 | 0.978836 |
| 0.05 | 11.9594 | 0.771227 | 0.771126 | 1.000320 | 0.937753 | 0.937191 |

The transverse \(+\) and \(-\) rates are equal to numerical precision for each charge. The charge-summed B.13 ratios reproduce the previously reported high-order anchor values.

### Compton fraction of total local absorption

| \(x\) | \(\mu^-\)-only lane | \(\mu^-+\mu^+\) lane |
|---:|---:|---:|
| 0 | 26.572% | 26.802% |
| 0.015 | 26.309% | 26.537% |
| 0.05 | 25.763% | 25.987% |

Thus, at this anchor, neutrino inverse decay supplies roughly 73--74% of the total local absorption. It is nearly polarization independent, so it dilutes the larger B.13 Compton longitudinal suppression.

At \(x=0.05\), for example, the Compton-only charge-summed ratio is \(R_{LT}=0.771126\), but after adding neutrino inverse decay the total ratio is \(R_{LT}=0.937191\). It would be incorrect to apply the Compton-only 22.9% longitudinal suppression to the complete B.2 opacity.

## 4. Algebraic checks

| Check | Maximum residual |
|---|---:|
| Charge-sum closure, B.13 production and absorption | 0 |
| Neutrino mode-sum closure against scalar decay production | \(6.82\times10^{-15}\) |
| B.13 mode/charge detailed balance | \(5.24\times10^{-16}\) |
| Neutrino mode detailed balance | \(4.92\times10^{-16}\) |
| B.13 transverse \(+/-\) equality | below \(3.0\times10^{-16}\) |

The reduced absorption was formed channel by channel using the same local \((1-e^{-\omega/T})\) factor. The total reduced opacity therefore closes to the sum of the neutrino and B.13 channel contributions.

## 5. Physical interpretation and limits

1. The B.13 Compton channel has a real longitudinal/transverse difference at finite momentum.
2. The neutrino inverse-decay channel is nearly isotropic at these points and substantially dilutes the Compton-only anisotropy.
3. The \(\mu^+\) correction is small but nonzero; the one-species and charge-summed lanes remain distinct.
4. The result is local at one radius and three energies. It does not determine the radial optical depth, the source-weighted escape probability, or the integrated B.2 luminosity.
5. The low-x range \(0\le x\le0.05\) is not the complete energy domain required for B.1/B.2. Do not update Fig. 7, the SN1987A bound, or axial-vector limits from this adapter test.

## 6. Reproduction

Run from the project root:

```bash
python finite_mixing/thermal_integrals/test_b13_b2_mode_adapter_local.py
```

Machine-readable output: [B13_B2_LOCAL_MODE_ADAPTER_2026-11-18.json](results/B13_B2_LOCAL_MODE_ADAPTER_2026-11-18.json).  
Test driver: [test_b13_b2_mode_adapter_local.py](test_b13_b2_mode_adapter_local.py).
