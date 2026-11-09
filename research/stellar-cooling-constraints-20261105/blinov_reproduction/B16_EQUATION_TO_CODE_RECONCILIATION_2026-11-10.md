# B.1--B.19 equation-to-code reconciliation: pure-vector 10 MeV benchmark

Date: 2026-11-10  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`  
Benchmark: (m_V=10\,\mathrm{MeV}), pure vector, (s18.8\)-SFHo-MUONS, (t_{\rm pb}=1\,\mathrm{s})  
Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`

## Executive result

The current literal B.1--B.19 pure-vector implementation has been reconciled against the published Appendix B equations and the repository call chain. **No algebraic or normalization mismatch has been identified in the inspected baseline implementation.** The B.1 source measure, B.2 chord/angle average, B.4 reduced absorption, B.5 velocity, B.7--B.10 neutrino inverse decay, and B.14--B.19 reference Compton rate map consistently to the implementation.

This is not a claim that the full Fig. 7 calculation is reproduced: the reconstructed stellar profile is not the original simulation table, and the article states that no associated data or code will be deposited. The independent full B.1+B.2 integration agrees with the archived implementation to a maximum 0.4451%, but both retain the +92.05% strong-endpoint difference from the digitized Fig. 7 point.

## 1. Equation-to-code map

| Published equation | Required operation | Current implementation | Audit status |
|---|---|---|---|
| B.1 | (4\pi r^2N^2dr\int_{m_V/N}d\omega\,[k\omega^2/(2\pi^2)]\Gamma_{\rm prod}\mathcal O) | `audit_b16_global_redshift.py::eq_b1_source_measure`; `audit_b16_b1b2_full_independent.py` | Formula and source quadrature cross-checked |
| B.2 | (\mathcal O=\frac12\int_{-1}^{1}dc_\theta\,e^{-\tau}) with the full chord | `reference.py::scalar_optical_depths`; independent `audit_b16_path_independent.py::analytic_chord_columns` | Geometry, normalization and convergence checked |
| B.3 | (s_{\max}=-r c_\theta+\sqrt{R_{\max}^2-r^2+r^2c_\theta^2}) | `reference.py::scalar_optical_depths`; independent chord routine | Direct match |
| B.4 | (\Gamma^*_{\rm abs}=(1-e^{-\omega/T})\Gamma_{\rm abs}) | `reference.py::local_rates` | Algebraically equivalent to ( (e^{\omega/T}-1)\Gamma_{\rm prod}) |
| B.5 | (v_V=\sqrt{1-m_V^2/\omega^2}), with (1/v_V) in (\tau) | `reference.py::scalar_optical_depths` | Direct match |
| B.6--B.9 | Neutrino inverse-decay phase space, polarization sum, vacuum width and Fermi integral | `reference.py::decay_production` and `fermi_pair_average` | Independent closed-form and direct angular checks |
| B.10 | (\Gamma_{\rm prod}=e^{-\omega/T}\Gamma_{\rm abs}) | `reference.py::local_rates` and the local-kernel audit | Detailed-balance closure |
| B.11--B.12 | Inverse dimuon decay | `reference.py::decay_production` | Correctly closed at (m_V=10\) MeV |
| B.13 | Full thermal Compton phase-space integral | Separate `moving_muon_compton.py` implementation | Alternative exact-kernel diagnostic; not the B.14--B.16 Fig. 7 baseline |
| B.14--B.16 | Non-relativistic/no-recoil reference cross section and thermal rate | `reference.py::compton_production` | Literal reference approximation |
| B.17 | (n_\mu F_{\rm deg}=\int 2d^3p/(2\pi)^3 f_\mu(1-f_\mu)) | `reference.py::negative_muon_density_and_degeneracy` | Spin degeneracy 2 and single negative-muon distribution implemented |
| B.18 | Forward/reverse cross-section ratio | Separate Compton matrix-element checks | Retained in the Compton validation chain |
| B.19 | Compton detailed balance | B.13 local-kernel audit | Checked separately from neutrino B.10 |

## 2. B.1 source normalization

The code implements the published source measure as
[
dL_{\rm thin}=
4\pi(r\,\mathrm{MeV})^2dr\,N(r)^2
\frac{k\omega^2}{2\pi^2}
\Gamma_{\rm prod}(r,\omega)d\omega,
\qquad k=\sqrt{\omega^2-m_V^2}.
]

The conversion from km to natural units is applied to both (r) and (dr). The factor (N^2) is applied at the emission radius. The radius-dependent threshold (m_V/N(r)) is inserted in the energy integration. The coupling is factored outside the local rates: local kernels are per (g^2), and the luminosity is multiplied by (g^2) once.

The archived implementation uses a piecewise-linear energy integral on a common grid. The independent B.1 calculation instead inserts the exact threshold at every radial quadrature node and uses a logarithmic-energy quadrature. The latter agrees with the archived B.1 source at the sub-percent level; the combined independent B.1+B.2 calculation agrees with archived B.16 at a maximum 0.4451% over the 25 Fig. 7 coupling vertices.

## 3. B.2 propagation and the fixed-energy convention

The literal optical-depth implementation is
[
\tau(r,\omega,c_\theta)=
\frac{1}{v_V(\omega)}
\int_0^{s_{\max}}ds\,
\Gamma^*_{\rm abs}(r'(s),\omega),
\quad
r'(s)=\sqrt{r^2+s^2+2rsc_\theta}.
]

The reference implementation uses:
- the B.3 chord endpoint;
- the same fixed (omega) and (v_V(omega)) for every path point;
- local (T,mu_{\nu_\mu},mu_\mu) evaluated at (r'(s));
- the B.4 reduced absorption;
- a normalized (dc_\theta/2) angular average.

The independent analytic chord integrator integrates the piecewise-linear radial opacity exactly on each interpolation segment. It agrees with the original path-quadrature implementation within the already documented sub-percent full-luminosity closure.

### Important distinction: path-redshift diagnostic

The paper's printed B.2 uses (Gamma^*_{\rm abs}(r'(s),\omega)) and (v_V(\omega)), with no (N(r)/N(r'(s))) factor. The fixed-(omega) code is therefore the equation-level reproduction baseline.

The alternative
[
\omega_{\rm loc}(s)=\omega_{\rm source}
\frac{N(r_{\rm source})}{N(r'(s))}
]
is a separate propagation prescription. It changes both the local thermal kernel and vector speed. The existing path-redshift calculation keeps the Euclidean chord and does not include proper spatial metric factors or ray bending; it is not a full GR transport solution. Its numerical effect is important, but it must not be used to tune the published-equation baseline.

The article's discussion of gravitational effects in B.1 (the (N^2) luminosity factor and the threshold (m_V/N(r))) does not insert a path-dependent lapse factor into the displayed B.2 integrand.

## 4. Local neutrino inverse-decay normalization

For one active flavour, the paper writes
[
\Gamma_{\nu\bar\nu\to V}^{\rm prod}
=\frac{m_V}{\omega}\,3\Gamma_{V\to\nu\bar\nu}
I(\mu_\nu/T,\omega/T,v_V),
\qquad
\Gamma_{V\to\nu\bar\nu}=\frac{\alpha_Vm_V}{6}.
]
With (\alpha_V=g^2/(4\pi)), the rate per (g^2) is
[
\frac{m_V^2}{8\pi\omega}I.
]
The implementation sums the two active channels using (\mu_{\nu_\mu}(r)) and (\mu_{\nu_\tau}=0), as specified in the paper for the simulation data used. The local B.7--B.10 audit independently compares the closed form, direct angular phase-space integration, and detailed balance. No missing factor of three or two-flavour normalization error is indicated.

At (m_V=10\) MeV, the inverse dimuon-decay channel is kinematically closed.

## 5. Reference Compton rate and the separate B.13 calculation

The Fig. 7 reference implementation uses B.14--B.16:
[
\Gamma_{\mu\gamma\to\mu V}^{\rm prod}
=n_\mu F_{\rm deg}\,
\frac{2}{v_V}\,
\frac{\sigma_{\mu\gamma\to\mu V}}{e^{\omega/T}-1}.
]
The code's cross section contains the B.14 factor (v_V), which cancels the explicit (1/v_V) in the rate as required. The cross section is evaluated per (g^2) using (\alpha_V/g^2=1/(4\pi)); the global luminosity applies (g^2) once. The B.17 density integral includes the spin factor 2 and uses the single (\mu^-) distribution in the like-for-like reference case.

The full B.13 moving-muon calculation is a different, more complete local-kernel prescription. It replaces both Compton production and absorption together and must remain separate from the B.14--B.16 reproduction baseline. Its current 10 MeV global result is (+131.53\%) at the strong endpoint, compared with (+92.24\%) for B.16. It does not repair the Fig. 7 discrepancy.

The separate polarization-resolved transport diagnostic also must not be confused with the baseline: the paper uses polarization-summed scalar rates, whereas the diagnostic divides the scalar Compton opacity equally among three vector modes as an explicitly artificial bookkeeping assumption.

## 6. Coupling and Fig. 7 reference

The digitized Fig. 7 vertices store (g). The corresponding horizontal-axis variable is
[
\alpha_V=\frac{g^2}{4\pi}.
]
The 25-point 10 MeV vertex sequence is monotonic in (\alpha_V). The source-PDF vector-path audit reconstructs the visible vertices with zero relative residual in the stored (g) and luminosity values. The final visible reference point is (1.2678147591\times10^{52}\,\mathrm{erg\,s^{-1}}) at (g=4.1716896502\times10^{-8}); the next source-PDF vertex lies below the plotted luminosity range and is correctly excluded.

Thus the existing strong-endpoint mismatch is not explained by a curve-label swap, path-order error, or visible-tail digitization error.

## 7. Numerical comparison and remaining physical-input limitation

At the strong endpoint:
- digitized Fig. 7: (1.2678147591\times10^{52}\,\mathrm{erg\,s^{-1}});
- archived fixed-(\omega) B.16 implementation: (2.4396359574\times10^{52}\,\mathrm{erg\,s^{-1}});
- relative difference: (+92.43\%).

The independent full B.1+B.2 integration agrees with the archived B.16 implementation to a maximum 0.4451% over the 25 points, while its strong-endpoint difference from Fig. 7 remains (+92.05\%). This isolates the residual away from the old integration implementation, conditional on the shared local kernels, fixed-(\omega) prescription, and adopted profile.

The public-figure reconstruction has 1687 rows and is not the raw Garching (s18.8\)-SFHo-MUONS simulation table. The original article's data-availability statement says no associated data will be deposited, and its code-availability statement says no code will be deposited. The relevant raw archive endpoints previously tested require authorization. The profile is therefore the main unresolved physical input for an exact independent reproduction; it must not be tuned to fit Fig. 7.

## 8. Final decision

1. Keep the literal B.14--B.16, fixed-(\omega), polarization-summed implementation as the Fig. 7 reproduction baseline.
2. Keep B.13 exact Compton, mode-resolved propagation, and path-redshift calculations as separately labelled diagnostics.
3. Do not rescale the source, opacity, coupling, or luminosity.
4. Do not update the production axial-vector constraint curve until the pure-vector benchmark's profile provenance and residual discrepancy are resolved.
5. Do not treat the path-redshift variant as a correction to the printed B.2 equation.

## 9. Reproducibility references

Repository files:
- `reference.py`
- `audit_b16_global_redshift.py`
- `audit_b16_path_independent.py`
- `audit_b16_b1b2_full_independent.py`
- `audit_b16_neutrino_b7_b9_kernel.py`
- `audit_b16_channel_resolved_energy.py`
- `audit_b13_global_transport.py`

Related reports:
- `B16_ORIGINAL_PAPER_CROSSCHECK_2026-11-08.md`
- `B16_NEUTRINO_B7_B10_LOCAL_KERNEL_AUDIT_2026-11-10.md`
- `B16_FULL_INDEPENDENT_B1B2_LUMINOSITY_AUDIT_2026-11-09.md`
- `B16_HIGH_ENERGY_CHANNEL_KERNEL_AUDIT_2026-11-10.md`
- `B16_HIGH_ENERGY_PATH_REDSHIFT_AUDIT_2026-11-10.md`
- `FIG7_DIGITIZATION_AUDIT_2026-11-08.md`
