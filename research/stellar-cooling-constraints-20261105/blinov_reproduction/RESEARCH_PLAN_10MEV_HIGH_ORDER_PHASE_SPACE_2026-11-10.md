# Research plan: 10 MeV high-order energy-resolved escape diagnosis

Date: 2026-11-10  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Scope: pure-vector reproduction of Blinov et al. Fig. 7, 10 MeV strong-absorption endpoint only.

## 0. Research question and stopping rule

The high-order fixed-\(\omega\) B.16 result at the strongest digitized 10 MeV point is
\[
L_{\rm B.16}=2.43963596\times10^{52}\ {\rm erg\,s^{-1}},
\]
compared with
\[
L_{\rm Fig.7}\simeq1.2678\times10^{52}\ {\rm erg\,s^{-1}},
\]
a residual of approximately \(+92.43\%\). The purpose of the next stage is to determine *which part of the source-weighted phase space survives* and which energy/radius/direction sectors carry the excess. The next stage is not another broad convergence scan.

The scope is deliberately restricted to:
- \(m_V=10\) MeV and the same strongest Fig. 7 digitized coupling;
- the archived vertex-preserving reconstructed SFHo-18.8 profile;
- the literal fixed-\(\omega\) Eq. (B.2) transport convention;
- the already accepted B.1 source and B.2 opacity definitions;
- the exact archived high-order grids \(N_r=200\), \(N_{\rm opacity}=640\), \(N_E=200\) (842 nodes after lapse-threshold insertion), \(N_\theta=32\), \(N_s=64\).

No 0.1 or 1 MeV runs, no global mass scan, no new stellar profile, no empirical opacity rescaling, and no modification of the axial-vector production outputs or constraint curves are part of this stage.

**Stopping rule:** first produce and validate the high-order phase-space JSON. Only if that output reveals a specific unresolved sector may a narrowly targeted second-stage diagnostic be added. Do not expand the grid or physical model by default.

## 1. Stage A — freeze and verify the calculation contract

Before running the physical diagnostic:

1. Check out the exact research branch and record the HEAD commit.
2. Verify SHA-256 identities of:
   - reconstructed SFHo-18.8 profile;
   - Fig. 7 digitization;
   - high-order baseline JSON;
   - source-radius grid, opacity-radius grid, and energy grid reconstructed by the script.
3. Confirm that the baseline is the fixed-\(\omega\) B.2 result and that its coupling is the strongest digitized 10 MeV vertex.
4. Run the dedicated phase-space binning unit tests and Python compilation.
5. Record Python, NumPy, SciPy, OS, CPU, memory, and elapsed-time information.

**Gate A:** do not run the long calculation if any hash, branch, mass, coupling, baseline convention, or regression test differs from the archived contract. Resolve the mismatch rather than silently updating the reference.

## 2. Stage B — execute one high-order phase-space decomposition

Run the existing \`audit_b16_escape_phase_space.py\` exactly once with:
\[
(N_r,N_{\rm opacity},N_E,N_\theta,N_s)=(200,640,200,32,64),
\]
\[
\Delta E_{\rm offset}=1000\ {\rm MeV}.
\]

The energy bins are reporting partitions of the already fixed energy quadrature; they must not modify the quadrature nodes or weights. The output must contain:

1. **Global and 8--15 km regional partitions**
   - B.1 thin-source fraction;
   - escaped-luminosity fraction;
   - source-weighted mean escape probability;
   - source- and escape-weighted optical-depth quantiles.
2. **Energy partition**
   - thin-source contribution in each energy bin;
   - escaped luminosity in each energy bin;
   - escape probability in each bin;
   - source- and escape-weighted \(\tau\) summaries.
3. **Emission-radius and direction partitions**
   - same source/escape quantities;
   - both four-bin and eight-bin \(\cos\theta\) partitions.
4. **Joint radius-energy-direction partition**
   - rank cells by escaped luminosity;
   - retain source fraction and escape fraction for each cell;
   - identify whether the dominant escaping cells are a small subset of the B.1 source.
5. **Source-channel accounting**
   - retain the B.1 neutrino inverse-decay and Compton source fractions;
   - do not infer channel-resolved opacity from source-channel fractions.

The central comparison is between
\[
W_{\rm source}(r,E,\cos\theta)
\quad\text{and}\quad
W_{\rm esc}=W_{\rm source}\,e^{-g^2\tau(r,E,\cos\theta)}.
\]
The diagnostic must distinguish a sector that is weakly populated at production from a sector that is populated but strongly absorbed.

## 3. Stage C — numerical and physical acceptance

The JSON is accepted only if all checks pass:

### C1. Exact baseline identity
- source, opacity, and energy grid hashes match the archived high-order B.16 baseline;
- profile and Fig. 7 digitization hashes match;
- mass and coupling match the strongest 10 MeV reference vertex.

### C2. Integral closure
\[
\left|\frac{L_{\rm phase}-L_{\rm B.16}}{L_{\rm B.16}}\right|<2\times10^{-10},
\qquad
\left|\frac{L_{\rm thin,phase}-L_{\rm thin,B.16}}{L_{\rm thin,B.16}}\right|<2\times10^{-10}.
\]
The integrated escape probability must agree with the archived B.16 value to the separately recorded floating-point tolerance.

### C3. Partition closure
For every region and every axis partition, source fractions and escaped-luminosity fractions must separately sum to unity within \(2\times10^{-10}\). The global fractions of a subregion must sum back to that subregion's fraction of the global source and escaped luminosity. Direction quadrature weights must sum to one within \(10^{-14}\).

### C4. Non-negativity and coverage
- all bin weights and luminosities are non-negative;
- bin edges cover the entire quadrature energy support;
- no finite quadrature weight is silently dropped by digitization or bin-edge conventions;
- joint-bin sums reproduce the corresponding one-dimensional marginals.

### C5. Independent checks
- run the dedicated unit tests;
- independently reconstruct energy and direction marginals from the joint-bin table;
- compare the high-order integrated escape probability with the previously archived lower-order directional/path result, while keeping the two grid configurations clearly labeled.

A failed closure or coverage check invalidates the output. It is not a physical result.

## 4. Stage D — interpret before adding more calculations

The first output is used to answer these questions, in order:

1. **Energy selection:** which bins dominate \(L_{\rm esc}\), and how do their fractions compare with the B.1 source spectrum?
2. **Radius selection:** within those energy bins, which emission shells dominate the escaping luminosity?
3. **Direction selection:** within those same radius-energy cells, is escape concentrated in outward directions?
4. **Opacity selection:** do the dominant escaping cells have a distinct \(\tau\) distribution, or do they simply carry a different source spectrum?
5. **Source versus transport:** is the discrepancy visible already in \(L_{\rm thin}\), or does it arise almost entirely after multiplying by the B.2 survival probability?

Use the exact identities
\[
L_{\rm thin}=g^2\int d\Gamma\,W_{\rm source},\qquad
L_{\rm esc}=g^2\int d\Gamma\,W_{\rm source}e^{-g^2\tau},
\]
where \(d\Gamma\) denotes the existing discrete source-radius, energy, and direction quadrature measure. Do not replace the distribution by a single mean optical depth.

## 5. Stage E — conditional second-stage diagnostics (only if Stage D identifies a target)

No second-stage calculation is launched until the Stage B JSON has passed Stage C and has been inspected.

### E1. If one or two energy bins dominate the residual
Perform a narrow energy-window audit using the *same nodes and weights*:
- compare source and escaped contributions within the selected energy window;
- inspect the local absorption kernel at the corresponding \(\omega\) in the \(12\)--\(25\) km opacity region;
- check interpolation and lapse-threshold-node treatment only within that window.

Do not change the energy grid globally unless this targeted comparison demonstrates unresolved quadrature error.

### E2. If the dominant cells are tied to outer path shells
Compute additive optical-depth contributions along the *same rays*:
\[
\tau=\sum_{r\text{-segments}}\tau_j,
\]
separately for the \(8\)--\(12\), \(12\)--\(15\), \(15\)--\(20\), \(20\)--\(22\), and \(22\)--\(25\) km path intervals. Report source-weighted and escape-weighted distributions for the dominant cells. Do not use leave-one-shell-out luminosity ratios as additive opacity fractions.

### E3. If opacity channels dominate
Decompose the opacity into inverse-neutrino-decay and Compton pieces at the integrand level, then recompute the same optical depths with each channel separately accumulated. Keep the full total-opacity result as the reference. Do not infer opacity-channel shares from the relative B.1 production fractions.

### E4. If the energy/radius/direction bins do not explain the residual
Only then revisit profile reconstruction systematics in \(15\)--\(25\) km, with the temperature, lapse, and \(\mu_{\nu_\mu}\) inputs checked against their source figures and digitization uncertainties. Do not alter the profile to force agreement with Fig. 7.

## 6. Execution environment decision

Recent GitHub Actions attempts fail before runner allocation, with no steps and no logs. This is an infrastructure failure; it is not a failed numerical run. Do not create repeated empty workflow runs.

The preferred execution order is:
1. use the existing GitHub workflow after hosted-runner provisioning is restored; or
2. execute the exact runbook on a local checkout of this exact branch using Python 3.12, NumPy, and SciPy.

The local execution is accepted only with the same code, inputs, hashes, grids, closure tests, and archived JSON schema. Record the local machine/OS and numerical library versions. The calculation is CPU-based and does not require CUDA or a GPU.

## 7. Deliverables

Only these artifacts are required for this stage:

1. \`outputs/b16_escape_phase_space_10mev_2026-11-10.json\` — accepted numerical result.
2. This plan — research logic, conditional branches, and stopping criteria.
3. A concise results note — physical interpretation of the energy/radius/direction distribution and any justified Stage E target.

No new mass-scan tables, no revised Fig. 7 curve, no axial-vector output, and no PR merge are part of this stage.

## 8. Final decision rule

After Stage D/E, classify the discrepancy into one of four evidence-based categories:

- **Numerical integration issue:** only if a controlled isolated refinement changes the relevant accepted observable beyond its tolerance.
- **Opacity-kernel/transport prescription issue:** only if the dominant escaping phase-space cells show a reproducible, formula-traceable difference in the relevant absorption or propagation prescription.
- **Stellar-profile reconstruction limitation:** only if a specific profile input and its source/digitization uncertainty are demonstrated to control the residual.
- **Unresolved:** if none of the above is established.

The current \(+92.43\%\) difference remains an unresolved reproduction discrepancy until one of these categories is supported. It is not evidence by itself that the published calculation is wrong.

Throughout, preserve the pure-vector benchmark as the validation gate. Do not update the axial-vector limit curve before the vector benchmark is independently accepted.


## 9. Status update after P1-D/P1-F (2026-11-10)

Stage D and the targeted follow-ups are complete at the scope supported by the public reconstruction:

- high-energy source/escape phase-space partition and closure;
- channel-resolved opacity and source/escape decomposition;
- path quadrature, angular quadrature, and opacity-grid interpolation;
- fixed-\(\omega\) versus path-redshift diagnostic;
- scalar polarization normalization and separate mode-resolved diagnostic;
- \(R_{\max}\) inward/outward conditional sensitivity;
- source-side \(\mu_{\nu_\mu}\), \(\mu_{\nu_\tau}=0\), and lapse sensitivity;
- energy-dependent daughter-neutrino kinematics and the physical meaning of the \(R_\nu\simeq25\) km boundary.

The new P1-F result is that the 210--510 MeV vector band produces daughter pairs with mean daughter energies of 105--255 MeV. The neutrino decoupling region is energy- and flavor-dependent, and heavy-flavor transport and energy spheres differ. The 25-to-30 km P1-D conditional extension suppresses the dominant high-energy band by 70.94%; a band-only total-luminosity proxy would lie 2.79% below Fig. 7 if all other bins were held fixed. This is not a self-consistent full luminosity result and does not authorize changing \(R_{\max}\).

The exact energy-dependent daughter-pair escape/reprocessing probability cannot be computed from the current CSV because same-snapshot baryon density, composition, neutrino angular moments, and energy-dependent heavy-flavor opacities are unavailable. The corresponding Garching archive endpoints require authorized access.

**Stopping decision:** do not repeat numerical quadrature, expand the mass scan, fit \(R_{\max}\), or alter the B.2 opacity. Retain \(R_{\max}=25\) km as the literal paper baseline. Classify the remaining strong-endpoint discrepancy as unresolved by the available public data, with energy-dependent heavy-flavor neutrino energy decoupling identified as the leading unclosed physical boundary issue. Keep PR #57 Draft/Open and do not update the axial-vector constraint curve.


### P1-G public-density transport envelope (2026-11-10)

Caputo et al. Fig. 1 provides the same SFHo-18.8, \(t_{\rm pb}=1\) s baryon-density profile through 20 km. A figure-level exponential-tail model combined with the published \(\nu N\) mean-free-path scaling gives central radial transport radii of about 22.4 km at 100 MeV, 24.6 km at 255 MeV, and 26.2 km at 500 MeV. Across the broad read-off envelope, the high-energy tail reaches roughly 22.6--27.8 km.

This narrows the boundary uncertainty: 25 km is plausible for much of the daughter-pair energy, while a smooth transition for the highest-energy tail may extend beyond 25 km. The transport estimate is not the heavy-flavor energy sphere and cannot select a new \(R_{\max}\). The full 30 km P1-D extension remains an extreme sharp-boundary diagnostic, not a physical prediction.

The remaining actionable calculation would require energy-changing heavy-flavor neutrino collision kernels and moments for the same snapshot. Without those inputs, no further parameter scan is justified. Keep the literal 25 km baseline and classify the remaining Fig. 7 discrepancy as unresolved by the available data.


### P1-H official archive access verification and stopping gate (2026-11-10)

The official Garching archive index has now been checked directly. It lists a Bollig/Hüdepohl collection with neutrino signals, radial neutrino moments/spectral data, and hydro profiles. The relevant radial-neutrino and hydro endpoints return HTTP 401 Unauthorized; the public index explicitly says that some collections are password protected and that access should be requested from the archive contact. See \`B16_P1H_GARCHING_ARCHIVE_ACCESS_AND_DATA_REQUIREMENTS_2026-11-10.md\`.

This establishes a legitimate route to request the relevant data, but does not prove that every archive file is the exact \(s18.8\)-SFHo-MUONS snapshot used in the Blinov benchmark. The model identifier, \(t_{\rm pb}=1\) s timestamp, frame convention, and field definitions must be confirmed by the data provider.

**P1-H stop/go gate:** do not attempt a full energy-dependent daughter-pair reprocessing integral until the provider confirms the same snapshot and supplies the required heavy-flavor energy-/angle-dependent neutrino distributions and energy-changing collision kernels. The public-density P1-G transport envelope is not an energy-sphere calculation. Keep \(R_{\max}=25\) km as the literal fixed-\(\omega\) B.2 baseline, keep PR #57 Draft/Open, and do not update the axial-vector curve.


### P1-H smooth B.2 daughter reprocessing (2026-11-10)

P1-H has completed a full B.2 source-radius/energy/angle/path integration for the 210--510 MeV band with the P1-G transport-only daughter reprocessing factor. The central equal-mode tail changes the band by \(-4.14\%\); the high-density tail by \(-10.60\%\); the low-density tail by \(-0.33\%\). The band-only total proxies remain \(+86.87\%\), \(+78.21\%\), and \(+91.98\%\) above Fig. 7. The sharp full-opacity \(R_{\max}=30\) km extension, by comparison, suppresses the band by \(70.94\%\) and gives a near-match that is not reproduced by the smooth model.

The direct V8 calculation closes to the archived P1-C/P1-D band results at \(10^{-11}\)--\(10^{-12}\). A Python reproduction script is archived but has not yet been independently rerun. The smooth model remains a transport-only diagnostic, not a full heavy-flavor energy-sphere calculation.

**Final stopping point:** no further numerical quadrature or boundary fitting is justified with the public inputs. Retain \(R_{\max}=25\) km and the literal scalar B.2 baseline. The strong-endpoint discrepancy remains unresolved by the available public data. Keep PR #57 Draft/Open and keep the axial-vector curve frozen.
