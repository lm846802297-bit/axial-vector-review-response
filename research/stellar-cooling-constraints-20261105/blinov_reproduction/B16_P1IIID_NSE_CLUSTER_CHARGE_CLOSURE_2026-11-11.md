# P1-IIId: Interpreting Caputo charge closure using the SFHo/NSE composition

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Physical interpretation

The SFHo equation of state is based on a non-uniform-matter description below saturation that includes unbound nucleons and nuclei in nuclear statistical equilibrium (NSE). The SFHo EOS paper states that, below saturation density, it applies the Hempel–Schaffner-Bielich statistical model for light and heavy nuclei within a gas of unbound nucleons. See Steiner et al., ApJ 774, 17 (2013), DOI: 10.1088/0004-637X/774/1/17.

For an NSE mixture with free neutrons/protons and nuclei \((A,Z)\), the bookkeeping identities are
\[
n_B=n_n^{\rm free}+n_p^{\rm free}+\sum_{A,Z}A n_{A,Z},
\]
\[
n_e+n_\mu=n_p^{\rm free}+\sum_{A,Z}Z n_{A,Z},
\]
assuming charge neutrality and no additional charged species relevant to the background.

Thus, if the plotted Caputo \(n_p\) is the free-proton density, the figure-level residual
\[
n_Q^{\rm cl}(r)\equiv n_e+n_\mu-n_p
\]
is the positive charge density carried by nuclei/clusters, not a failure of charge neutrality. The corresponding cluster baryon density is
\[
n_B^{\rm cl}(r)=n_B-n_n^{\rm free}-n_p^{\rm free}.
\]
If the Esseili–Kribs Fig. 12 curves \(n,p\) are the same free-nucleon variables, then their neutron curve supplies the missing information needed to infer the cluster baryon density and an effective cluster charge fraction:
\[
\left\langle\frac ZA\right\rangle_{\rm cl}
=\frac{n_e+n_\mu-n_p}{n_B-n_n^{\rm free}-n_p^{\rm free}}.
\]

This interpretation is physically well motivated by the SFHo/NSE EOS construction, but the precise mapping of the plotted symbols \(n,p\) to archive variables must still be checked against the Garching variable definitions. The figure captions alone do not prove that mapping.

## 2. Caputo digitized positive-charge residual

Using the checksum-verified Caputo Fig. 1 vector paths, define
\[
n_Q^{\rm cl}/n_0=(n_e+n_\mu-n_p)/n_0.
\]
The following values are linearly interpolated between digitized vector vertices. They are figure-level estimates, not raw Garching outputs.

| \(r\) (km) | \(n_B/n_0\) | \(n_p/n_0\) | \((n_e+n_\mu)/n_0\) | \(n_Q^{\rm cl}/n_0\) | \(n_Q^{\rm cl}/n_B\) |
|---:|---:|---:|---:|---:|---:|
| 8 | 0.99570 | 0.20009 | 0.20046 | 0.000368 | 0.037% |
| 9 | 0.83652 | 0.14667 | 0.14851 | 0.001846 | 0.221% |
| 10 | 0.70118 | 0.10937 | 0.11596 | 0.006582 | 0.939% |
| 11 | 0.57302 | 0.07714 | 0.08659 | 0.009450 | 1.649% |
| 12 | 0.45112 | 0.05048 | 0.06086 | 0.010380 | 2.301% |
| 13 | 0.33857 | 0.02952 | 0.03900 | 0.009476 | 2.799% |
| 14 | 0.23729 | 0.01486 | 0.02236 | 0.007501 | 3.161% |
| 15 | 0.14974 | 0.005897 | 0.01103 | 0.005132 | 3.427% |

The required extra positive charge peaks around 11–12 km at roughly \(10^{-2}n_0\), then declines. This radial pattern is compatible with the emergence of nuclear clusters as the matter becomes sub-saturation and the free-proton fraction falls.

The old relative residual \((n_p-n_e-n_\mu)/n_p\) becomes large outside 10 km partly because the free-proton density becomes small. For composition interpretation, the absolute missing charge \(n_Q^{\rm cl}\) and its fraction of total baryon density are more informative than the relative residual normalized to \(n_p\).

## 3. Important caution

The above interpretation is conditional:
- If \(n_p\) is free-proton density, \(n_Q^{\rm cl}\) is the nuclear-cluster charge density (up to any other charged components).
- If \(n_p\) is total proton-equivalent density including protons bound in nuclei, charge neutrality should instead close directly, and the residual would point to a figure-path, normalization, or definition mismatch.

Do not rescale \(n_p,n_e,n_\mu\) to force closure. Do not infer the cluster baryon density from charge alone without the cluster \(Z/A\) distribution.

## 4. Why Fig. 12 neutron/proton curves are now essential

The Fig. 12 \(n,p\) curves can test whether they are the free-nucleon densities corresponding to Caputo \(n_B,n_p\). If that mapping is verified, digitizing \(n_n^{\rm free}(r)\) gives
\[
n_B^{\rm cl}=n_B-n_n^{\rm free}-n_p^{\rm free}
\]
and therefore the effective cluster charge-to-baryon ratio above.

This also defines the correct applicability of the existing free-nucleon collision kernel. The kernel uses only free \(n,p\); it must not be normalized to total \(n_B\) when a significant fraction of baryons resides in nuclei. Neutrino scattering on nuclei and nuclear response contributions may need to be included separately in the outer layers.

## 5. Next validation steps

1. Digitize Fig. 12 \(p(r)\) and compare with Caputo \(n_p(r)\).
2. Digitize Fig. 12 \(n(r)\); check its normalization and whether \(n_n+n_p\le n_B\).
3. Obtain the Garching archive variable documentation to establish whether \(n,p\) are free nucleons.
4. If the mapping is confirmed, compute \(n_B^{\rm cl}\), \(n_Q^{\rm cl}\), and \(\langle Z/A\rangle_{\rm cl}\) with propagated figure-digitization errors.
5. Only then decide whether the outer-layer neutrino opacity needs explicit nuclear coherent/inelastic scattering in addition to the free-nucleon kernel.

No B.2, vector Fig. 7, or axial cooling result is changed by this composition diagnostic.
