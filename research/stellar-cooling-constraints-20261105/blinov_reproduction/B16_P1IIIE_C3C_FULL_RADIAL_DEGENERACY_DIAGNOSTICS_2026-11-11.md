# P1-IIIe-C3C: full-radial degeneracy-factor physical diagnostics

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose and scope

C3-C characterizes the radial dependence of the local static neutron and proton degeneracy factors on the 301-point \(t_{\rm pb}=1\) s Caputo SFHo-18.8 published-figure snapshot. It tests the dimensionless variables \(\eta_N=\nu_N/T\) and \(\theta_N=T/m_N^*\), quantifies their correlations with the EOS free-nucleon/cluster composition, and compares relativistic and nonrelativistic kinetic dispersions.

This is a local quasiparticle-occupation diagnostic. It is not a time-space weighted core average, dynamic structure factor, B.2 opacity, transport calculation, or luminosity result.

## 2. Exact dimensionless reduction

The local occupation is
\[
f_N(p)=\left[\exp\left(\frac{\sqrt{p^2+m_N^{*2}}-m_N^*-\nu_N}{T}\right)+1\right]^{-1}.
\]
With
\[
\eta_N=\frac{\nu_N}{T},\qquad
\theta_N=\frac{T}{m_N^*},\qquad
p=\sqrt{2m_N^*T}\,y,
\]
the kinetic energy becomes
\[
\frac{K_N}{T}
=\frac{\sqrt{1+2\theta_N y^2}-1}{\theta_N}.
\]
The common momentum-measure normalization cancels in the ratio, giving
\[
F_{NN}^{\rm deg}=\mathcal F(\eta_N,\theta_N).
\]
Thus, in this local ideal quasiparticle prescription, \(X_N\) and \(\xi_{\rm SPP}\) are not explicit arguments of \(F_{NN}^{\rm deg}\). Composition affects it indirectly through the EOS state variables, especially \(\nu_N\), \(m_N^*\), and \(T\).

The nonrelativistic limit \(\theta_N\to0\) gives \(K/T\to y^2\) and \(F_{NN,\rm NR}^{\rm deg}=\mathcal F_{\rm NR}(\eta_N)\).

## 3. Full-radial ranges and correlations

| Quantity | Neutrons | Protons |
|---|---:|---:|
| \(\eta_N=\nu_N/T\) | 0.4437--6.5960 | -3.1341--2.6983 |
| \(T/m_N^*\) | 0.01380--0.05537 | 0.01382--0.05547 |
| \(m_N^*\) [MeV] | 541.15--898.95 | 539.86--897.66 |
| \(T\) [MeV] | 12.40--39.24 | 12.40--39.24 |
| free fraction \(X_N\) | 0.7818--0.8754 | 0.03492--0.2182 |
| EOS cluster fraction | 0--0.08972 | 0--0.08972 |
| relativistic \(F_{NN}^{\rm deg}\) | 0.23989--0.73419 | 0.45851--0.98527 |

The free-fraction closure
\[
X_n+X_p+X_{\rm cluster}^{\rm EOS}=1
\]
holds over the full profile with maximum absolute residual \(9.0\times10^{-13}\). Tiny negative cluster fractions at the innermost points are roundoff-level values and are clipped to zero only for the reported range/correlation diagnostics.

### 3.1 Correlation with degeneracy parameter

| Correlation | Neutrons | Protons |
|---|---:|---:|
| Pearson \(r(F^{\rm deg},\eta_N)\) | -0.98807 | -0.98613 |
| Spearman \(\rho(F^{\rm deg},\eta_N)\) | -0.9999956 | -1.00000 |
| Pearson \(r(F^{\rm deg},T/m_N^*)\) | -0.14721 | -0.16145 |
| Spearman \(\rho(F^{\rm deg},T/m_N^*)\) | -0.30867 | -0.30949 |

The radial ordering is almost perfectly monotonic in \(\eta_N\) for both species. A simple linear regression gives:

| Linear predictor set | Neutron \(R^2\) | Proton \(R^2\) |
|---|---:|---:|
| \(\eta_N\) only | 0.97628 | 0.97246 |
| \(\eta_N\) and \(T/m_N^*\) | 0.98229 | 0.99689 |
| \(\eta_N\) and \(X_N\) | 0.98726 | 0.99586 |

These are descriptive fits along one radial trajectory, not universal EOS fits or causal decompositions. The exact two-variable dependence follows from the dimensionless reduction above; the regression numbers only quantify how the variables co-vary in this particular snapshot.

### 3.2 Composition correlations

The radial Pearson correlations are
\[
r(F_{nn}^{\rm deg},X_n)=+0.8365,\qquad
r(F_{pp}^{\rm deg},X_p)=-0.7809,
\]
and
\[
r(F_{NN}^{\rm deg},X_{\rm cluster})\simeq+0.696
\quad(n),\qquad +0.708\quad(p).
\]
These correlations must not be interpreted as direct composition factors multiplying the degeneracy correction. \(X_N\) and \(X_{\rm cluster}\) are correlated with the EOS chemical potentials and therefore co-vary with \(\eta_N\); neither appears explicitly in the local \(F^{\rm deg}\) ratio.

## 4. Relativistic versus nonrelativistic dispersion

Two distinct comparisons are required because keeping \(\nu_N\) fixed does not keep the density fixed when the dispersion relation is changed.

**A. Fixed-\(\nu_N\) comparison.** Keep \(T,m_N^*,\nu_N\) unchanged and replace
\[
K_{\rm rel}(p)=\sqrt{p^2+m_N^{*2}}-m_N^*
\quad\longrightarrow\quad
K_{\rm NR}(p)=\frac{p^2}{2m_N^*}.
\]
This isolates the change in the dispersion at the same chemical potential, but the resulting NR density is not constrained to equal the relativistic density.

**B. Fixed-density comparison.** Keep \(T,m_N^*\) and the relativistic available-volume density \(n_N'\) fixed, solve for \(\nu_N^{\rm NR}\) satisfying
\[
n_{\rm NR}'(T,m_N^*,\nu_N^{\rm NR})
=n_{\rm rel}'(T,m_N^*,\nu_N),
\]
and then compare the two \(F^{\rm deg}\) values. This is the controlled comparison for two local descriptions of the same density state.

### 4.1 Maximum and RMS relative shifts over all radii

The shift is defined as
\[
\Delta_{\rm NR}=
\frac{F_{\rm NR}^{\rm deg}-F_{\rm rel}^{\rm deg}}
{F_{\rm rel}^{\rm deg}}.
\]

| Comparison | Species | Maximum \(|\Delta_{\rm NR}|\) | RMS \(|\Delta_{\rm NR}|\) | Radius of maximum |
|---|---|---:|---:|---:|
| Fixed \(\nu_N\) | n | 8.876% | 5.105% | 0.20 km |
| Fixed \(\nu_N\) | p | 3.674% | 1.958% | 0.20 km |
| Fixed density | n | 18.991% | 11.436% | 0.20 km |
| Fixed density | p | 8.867% | 4.921% | 0.20 km |

In every radial point and for both species, the nonrelativistic calculation gives a smaller \(F^{\rm deg}\) than the relativistic one. The density-matched comparison requires a larger \(\nu_N^{\rm NR}\): the maximum absolute shift is 17.18 MeV for neutrons and 4.92 MeV for protons. The final density-matching residual is below \(5.9\times10^{-15}\).

The larger fixed-density correction is physically expected. At a given momentum, \(K_{\rm rel}<K_{\rm NR}\); to recover the same density with the NR dispersion, \(\nu_N^{\rm NR}\) must be raised. This increases degeneracy and lowers \(F^{\rm deg}\) further.

### 4.2 Selected radial points

| Species | \(r\) [km] | \(F_{\rm rel}^{\rm deg}\) | \(F_{\rm NR}^{\rm deg}\), fixed \(\nu\) | \(F_{\rm NR}^{\rm deg}\), fixed density |
|---|---:|---:|---:|---:|
| n | 0.20 | 0.23990 | 0.21860 | 0.19434 |
| n | 5.00 | 0.36081 | 0.33798 | 0.30859 |
| n | 10.00 | 0.68923 | 0.67672 | 0.65510 |
| n | 15.20 | 0.73419 | 0.73081 | 0.72496 |
| p | 0.20 | 0.45851 | 0.44166 | 0.41785 |
| p | 5.00 | 0.62849 | 0.61423 | 0.59081 |
| p | 10.00 | 0.91679 | 0.91336 | 0.90638 |
| p | 15.20 | 0.98527 | 0.98508 | 0.98470 |

The NR approximation becomes progressively better toward the outer profile, where \(\eta_N\) is smaller and the gas is closer to the classical limit. It is not uniformly accurate in the inner core, particularly for neutrons.

## 5. Physical conclusions

1. The local static degeneracy factor has an exact dimensionless representation \(F^{\rm deg}=\mathcal F(\nu/T,T/m^*)\). The degeneracy parameter \(\nu/T\) is the dominant radial correlator in this snapshot.
2. The apparent correlation with free-nucleon/cluster fractions is indirect. Composition determines the EOS state but does not multiply \(F^{\rm deg}\) as a separate factor.
3. A nonrelativistic dispersion is not uniformly interchangeable with the relativistic SFHo quasiparticle dispersion for percent-level local degeneracy corrections. The inner-core discrepancy is appreciable, especially for neutrons.
4. For a controlled same-density comparison, the chemical potential must be refitted after changing the dispersion. Merely retaining the relativistic \(\nu_N\) compares different densities.

## 6. Acceptance and scope boundary

C3-C acceptance:
- all 301 radii and both species are included (602 rows);
- the relativistic calculation reproduces C2 \(F^{\rm deg}\) within \(5\times10^{-12}\);
- EOS composition closure is below \(10^{-8}\);
- the NR fixed-density root reproduces the relativistic density within \(10^{-8}\);
- all three \(F^{\rm deg}\) values lie in \((0,1)\);
- the NR shifts are finite and negative at every radial point;
- the Spearman correlation with \(\eta_N\) is below \(-0.999\) for both species.

**C3-C direct numerical status: PASS.** The independent Python CI reconstruction is tracked separately.

This result does not establish the accuracy of a nonrelativistic approximation for dynamic \(W_N^{\mu\nu}(q_0,q;r)\), B.1 production, B.2 absorption, or transport. Those involve momentum/energy transfer, recoil, and response kinematics beyond the static occupation ratio.

Next: C4, construct the local dynamic nucleon response with the relativistic EOS baseline retained, and validate the limiting/static relations before using it in any luminosity calculation.
