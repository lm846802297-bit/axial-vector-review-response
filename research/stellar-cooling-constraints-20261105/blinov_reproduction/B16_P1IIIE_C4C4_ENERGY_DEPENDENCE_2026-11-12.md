# P1-IIIe-C4-C4: incident-energy dependence of moving-nucleon weak scattering

Date: 2026-11-12  
Branch: `research/c4c4-energy-dependence-20261112`  
Status: C4-C4-A implementation prepared; numerical run pending.

## 1. Research question

C4-C3 establishes the fixed-local-energy (E_\nu=100\,\mathrm{MeV}) radial baseline. C4-C4 studies how the local total neutral-current scattering rate changes with incident neutrino energy while preserving the C4-B2/C1/C2 EOS moving-nucleon kernel.

The observable is
\[
\Gamma_N^{\rm avail}(E_\nu,r)
=2\pi\int_{-1}^{1}d\cos\theta
\int_{E'_{\min}}^{E'_{\max}}dE'\,
\frac{d\Gamma_N}{dE'\,d\Omega'} ,
\qquad N=n,p.
\]
The allowed (E'\) interval is recomputed from the exact moving-nucleon support condition
\[
p_{\min}(E_\nu',\cos\theta;m_N^*)\le p_{\max}(m_N^*,\nu_N,T),
\]
with the existing (45T) momentum-tail cutoff. No fixed (\pm60\,\mathrm{MeV}) window is used.

The calculation retains the EOS effective mass in quasiparticle spinors and energies, EOS chemical potentials in both Fermi factors, final-state Pauli blocking, the existing weak form factors, and separate neutron/proton and neutrino/antineutrino channels.

## 2. C4-C4-A: four-radius anchor scan

The first stage uses the four already validated C4-C2/C4-C3 anchor radii:
\[
r=0.20,\ 5.00,\ 10.00,\ 15.20\ \mathrm{km}.
\]
The exploratory first-pass energy grid is
\[
E_\nu=10,\ 20,\ 40,\ 60,\ 100,\ 150\ \mathrm{MeV}.
\]
This six-point grid is a working exploration grid, not a final physical boundary or an approved exclusion range. The (100\,\mathrm{MeV}) entries are reused from the byte-pinned C4-C2 full-angle baseline; the other five energies are recomputed. The resulting matrix contains 96 local cases, of which 80 are new calculations.

For each case,
\[
\kappa_N(E_\nu,r)=\xi_{\rm SPP}(r)\Gamma_N^{\rm avail}(E_\nu,r),
\qquad
\lambda_N(E_\nu,r)=\kappa_N^{-1}.
\]
The (\xi_{\rm SPP}) factor is applied exactly once. Rates are normalized per available volume; the (\xi_{\rm SPP}\) factor is restored only for total-volume opacity.

## 3. Numerical setup and acceptance

The initial scan reuses the accepted C4-C2 quadrature:
- outgoing-angle cosine: 8 Gauss-Legendre nodes;
- outgoing energy: 48 Gauss-Legendre nodes over the full exact support;
- initial nucleon momentum: 36 nodes;
- azimuth: 12 midpoint nodes;
- support-root scan: 10,001 points, followed by Brent refinement.

The C4-C2 100-MeV baseline is pinned by Git blob SHA
`881b6459e8d9a1ac867b0f4dc47ac168d454e488`. Input profile and occupation files retain their existing SHA/Git-blob checks.

C4-C4-A numerical-integrity checks:
1. exactly 96 unique energy/radius/target/sign cases;
2. 16 cases at each energy;
3. positive, finite total rates, per-target cross sections, opacities, and mean free paths;
4. support-root relative residual below (10^{-7});
5. (\kappa_N/(\xi_{\rm SPP}\Gamma_N^{\rm avail})=1) to floating-point precision;
6. exact provenance reuse of the 16 C4-C2 100-MeV reference rows.

These are software/numerical-integrity checks. They do not constitute a physical transport or literature-reproduction acceptance.

## 4. Outputs

The data archive is separate from the source-code commit and contains:
- `local_rates_96.csv`: all local rates and derived per-target/opacity quantities;
- `energy_scaling_ratios.csv`: each channel normalized to its own 100-MeV value;
- `channel_ratios.csv`: neutron/proton and neutrino/antineutrino opacity ratios;
- `summary.json`: numerical-integrity results, quadrature, and source provenance;
- `SHA256SUMS.txt`: archive checksum manifest.

## 5. Scope boundary and next stage

C4-C4-A is a four-radius, fixed-local-energy, flat-space local scattering study. It does not include gravitational redshift, energy redistribution, angular transport, escape probabilities, full radial integration, hydrodynamic feedback, or supernova luminosity.

Only after the anchor scan and its energy-dependent quadrature checks are understood should C4-C4-B extend the calculation to all 301 radial points and construct (\tau(E_\nu,r)). The C4-C3 100-MeV 301-radius archive remains the baseline and is not overwritten. No manuscript, referee response, PR #56 transport result, or axial cooling limit is modified.
