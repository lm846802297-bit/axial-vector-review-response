> **Profile-source clarification (2026-11-09):** The Caputo--Bollig agreement in Fig. 1 temperature and Fig. 4 degeneracy parameter does not imply agreement of the absolute muon-density curves. Bollig Fig. 3 is 8.8% lower on average than Caputo over 12--15 km, while Caputo's own plotted density agrees with its relativistic Fermi integral to below 0.54%. The Caputo (T,\mu_\mu) inputs and derived B.1 (n_\mu F_{\rm deg}) remain the current internally consistent baseline; the Fig. 3 density residual is a separate unresolved source-level discrepancy. It does not validate the Ferreira substitutions B/B2. See BOLLIG_MUON_DENSITY_AND_B1_SOURCE_AUDIT_2026-11-09.md.

> **Follow-up resolution (2026-11-09):** The Ferreira \\(\\mu_\\mu\\) substitutions B/B2 below are now explicitly off-baseline sensitivity diagnostics. Direct digitization of Bollig et al. Fig. 4 shows that Caputo's \\(\\mu_\\mu/T\\) agrees with the original SFHo-18.8 curve to a maximum relative difference of \\(1.43\\times10^{-4}\\) over 12--15 km; Ferreira differs by up to 17.18%. The Caputo profile is therefore retained as the source-validated baseline for this benchmark. See [the original Fig. 4 cross-check](BOLLIG_ORIGINAL_FIG4_MUON_DEGENERACY_CROSSCHECK_2026-11-09.md).

# Full B.1+B.2 transport response to 12--15 km profile-input diagnostics

Date: 2026-11-09  
Benchmark: \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\), \(R_{\max}=25\) km, fixed \(\omega\) along B.2 paths.  
Status: **the \(\mu_{\nu_\mu}\) plotting-floor ambiguity is numerically negligible in the tested interval. The alternative \(\mu_\mu\) curve has a potentially significant transport effect, but it is not a validated replacement profile.**

## 1. Reproducibility and run status

The full profile-input workflow completed successfully in GitHub Actions:

- Workflow: SFHo-18.8 profile and shell-resolved B.1+B.2 sensitivity (8--15 km)
- Run: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42521503180
- Triggering commit: \`004ca9819c3d9fcd015b39dd44f0c2f55f708cc6\`
- All steps passed, including source-PDF hash checks, profile regression tests, B.1+B.2 sensitivity, radial convergence, and the guard confirming that production axial outputs are unchanged.

The profile SHA-256 is \`6c47d0712d266848d0cb2315c8a9b43cf13d0b39b6986d4239dd3f22cb9ba0bc\`. The calculation changes one named profile column at a time. Matrix elements, energy/radial/angular quadrature, fixed-\(\omega\) convention, geometry, and coupling are held fixed.

## 2. Results: \(\mu_{\nu_\mu}\) floor ambiguity

Two deliberately broad local variants were tested:

- A: set \(\mu_{\nu_\mu}=0\) throughout 12--15 km.
- C: in the part of the interval beyond the plotted support endpoint, use \(\mu_{\nu_\mu}=-1\) MeV, the magnitude of the logarithmic-plot resolution floor.

Relative to the baseline:

| Diagnostic | B.1 source ratio | Own-source \(P_{\rm esc}\) ratio | Escaped B.1 integral ratio | Fixed-source \(P_{\rm esc}\) ratio |
|---|---:|---:|---:|---:|
| A: zero \(\mu_{\nu_\mu}\) in 12--15 km | 1.0000548 | 0.9998914 | 0.9999462 | 0.9999339 |
| C: unresolved branch held at \(-1\) MeV | 0.9999912 | 1.0000262 | 1.0000174 | 1.0000179 |

The changes are at most about \(1.1\times10^{-4}\) in the escape probability and \(5.5\times10^{-5}\) in the source normalization. Thus the unresolved \(\mu_{\nu_\mu}\) support convention cannot explain a 48% strong-coupling escape-probability discrepancy in this benchmark.

This result is consistent with the local rate audit: at 12 km, replacing \(-4.31\) MeV by zero changes the sampled \(\nu_\mu\) pair-production kernel by only about 0.34% at \(\omega=12\) MeV; at 13 km, the change is about 0.043%; near and beyond the plotted endpoint, the effect is smaller still. The pair rate is even in \(\mu_{\nu_\mu}\), so the sign of the branch is not itself the issue.

The broad A/C variants bracket the plotted-floor uncertainty over the sensitive interval. A smooth transition between zero and a magnitude of 1 MeV cannot generate a larger effect than the endpoint envelope tested here, within the same local kernel.

## 3. Results: alternative \(\mu_\mu\) curve restricted to 12--15 km

Variant B substitutes the Ferreira-digitized \(\mu_\mu\) only over 12--15 km:

| Quantity | Variant / baseline |
|---|---:|
| B.1 source normalization | 1.00646 |
| Own-source escape probability | 0.93299 |
| Fixed-baseline-source escape probability | 0.93297 |
| Escaped B.1 integral | 0.93901 |
| Mean 12--15 km path-shell optical depth | 1.0360 |

This local substitution changes the source by only 0.65%, but reduces the escape probability by about 6.7%. It is a real sensitivity of the B.2 transport to the muon background, but it remains much smaller than the required strong-tail change.

## 4. Results: alternative \(\mu_\mu\) curve over the dominant 8--15 km emission region

Because the B.1 source is concentrated inside 8--15 km, an additional diagnostic B2 substitutes the Ferreira curve throughout that full emission region. It is not a proposed physical profile.

At radial order 120:

| Quantity | B2 / baseline |
|---|---:|
| B.1 source normalization | 1.26893 |
| Own-source escape probability | 0.66554 |
| Fixed-baseline-source escape probability | 0.62389 |
| Escaped B.1 integral | 0.84453 |

The source and opacity effects are separated by reporting both the fixed-source escape response and the variant's own-source response. The alternative \(\mu_\mu\) increases the B.1 source by about 26.9%, while reducing the escape probability by about 33.4%. Their product leaves the escaped B.1 integral about 15.5% below baseline.

The shell-resolved response at radial order 120 is:

| Region | B.1 source ratio | Mean path optical-depth ratio |
|---|---:|---:|
| 8--10 km | 1.5328 | 1.4970 |
| 10--12 km | 1.1917 | 1.1826 |
| 12--15 km | 1.0471 | 1.0376 |

This demonstrates why a local 12--15 km-only substitution and an 8--15 km substitution are not interchangeable. Most of the B.1 source and opacity response to the alternative curve occurs in 8--12 km, especially 8--10 km.

## 5. Radial-quadrature convergence

The B2 diagnostic was repeated at radial orders 40, 80, and 120, with all other numerical settings fixed.

| Radial order | Baseline \(P_{\rm esc}\) | B2 fixed-source \(P_{\rm esc}\) ratio | B2 B.1 source ratio | B2 escaped-integral ratio |
|---:|---:|---:|---:|---:|
| 40 | \(3.23935\times10^{-4}\) | 0.61978 | 1.27092 | 0.83990 |
| 80 | \(3.25071\times10^{-4}\) | 0.62318 | 1.26808 | 0.84317 |
| 120 | \(3.24965\times10^{-4}\) | 0.62389 | 1.26893 | 0.84453 |

Between radial orders 80 and 120, the baseline escape probability changes by about \(3.3\times10^{-4}\) fractionally, the fixed-source escape ratio by about \(1.1\times10^{-3}\), and the source ratio by less than \(7\times10^{-4}\). The B2 response is therefore radially converged to the sub-percent level for the present diagnostic.

## 6. Physical interpretation and limits

The alternative Ferreira \(\mu_\mu\) curve is confirmed to be the orange dashed SFHo-18.8, \(t_{\rm pb}=1\) s curve in Ferreira Fig. 1. However, its values disagree with the Caputo curve by roughly 9.5--17.2% over 12--15 km. The Caputo \(T,\mu_\mu\) pair reproduces the independently plotted Caputo muon density, whereas the Ferreira pair does not reproduce that Caputo density profile.

Consequently, B and B2 are sensitivity diagnostics only. The current audit does not establish that Ferreira's curve is the correct replacement for the baseline, nor does it identify the origin of the difference (e.g. chemical-potential convention, equation of state, or profile extraction). The raw Garching background remains unavailable.

Even if B2 were adopted purely as a diagnostic envelope, it does not remove the full Fig. 7 strong-tail discrepancy: its escaped B.1 integral is 0.8445 of baseline, whereas the reference comparison requires an escape-probability ratio of approximately 0.520 before accounting for the source change. The alternative curve is therefore neither a validated correction nor a complete explanation.

## 7. Decision

1. Keep Caputo \(T,\mu_\mu,\mu_{\nu_\mu}\) and the existing lapse as the baseline reconstructed profile pending source-level reconciliation.
2. Do not spend further effort on the \(\mu_{\nu_\mu}\) plotting-floor ambiguity as an explanation of the high-coupling tail; its full B.1+B.2 effect is negligible in the tested interval.
3. Retain the Ferreira \(\mu_\mu\) substitution as a systematic diagnostic only. Resolve the physical origin of the cross-paper discrepancy before selecting either profile.
4. Do not alter B.6--B.10 or B.14--B.19, do not rescale the source or opacity, and do not update the pure-vector or axial-vector cooling curves.
5. The next highest-value task is to compare the definitions and background provenance of \(\mu_\mu\) in Caputo and Ferreira, and if possible recover the public source data or an independently plotted muon density for Ferreira's exact profile.

## 8. Machine-readable outputs

- \`outputs/profile_transport_sensitivity_12_15km_2026-11-09.json\`
- \`outputs/profile_radial_convergence_8_15km_2026-11-09.json\`
- \`data/profile_12_15km_audit_2026-11-09.json\`

The profile and transport scripts are \`audit_profile_12_15km.py\`, \`audit_profile_transport_sensitivity.py\`, and \`audit_profile_radial_convergence.py\`. The production axial files are unchanged.


## 2026-11-10 provenance qualification: Ferreira curve is not an uncertainty band

The new full 5--15 km comparison in `FERREIRA_CAPUTO_MUON_PROFILE_PROVENANCE_AUDIT_2026-11-10.md` changes how the Ferreira-profile transport result must be interpreted:

- The Caputo and Ferreira temperature curves agree to a radius-weighted mean relative difference of 0.0168%.
- Their \\(\eta_\mu=\mu_\mu/T\\) profiles differ by a radius-weighted mean of 77.26% over 5--15 km, with a maximum pointwise difference of 315.59% near 5 km.
- The original Bollig Fig. 4 direct comparison in the 12--15 km shell agrees with Caputo at 0.00518% mean absolute relative difference (0.01434% maximum), whereas Ferreira differs by 12.74% (17.18% maximum).
- The difference is not a constant additive (m_\mu) rest-mass shift and is not explained by a temperature mismatch.

Consequently, the previously reported Ferreira substitution remains a useful **stress diagnostic only**. It must not be presented as a statistically meaningful profile uncertainty, averaged with the Caputo curve, or used to define the baseline envelope. The Caputo \\(T,\mu_\mu\\) reconstruction remains the working SFHo-18.8, 1 s baseline because it is the one that reproduces the original Bollig degeneracy curve and is consistent with the plotted muon density. The raw Garching profile is still required to certify the complete thermodynamic input.
