# Lai et al. (2024): independent plateau benchmark and equation-level comparison

Date: 2026-11-19

Primary reference: K.-C. Lai, C. S. J. Leung and G.-L. Lin, *SN1987A constraints to BSM models with extra neutral bosons near the trapping regime: \(U(1)_{L_\mu-L_\tau}\) model as an illustrative example*, arXiv:2401.16023v2.

This is an **independent vector-transport benchmark**. It is not an axial-vector calculation and its numerical curves must not be transplanted into the axial model without rederiving the production and absorption kernels.

## 1. Why this is the next independent benchmark

Lai et al. use the same \(U(1)_{L_\mu-L_\tau}\) vector boson and the same SFHo-18.8, \(t_{\rm pb}=1\) s simulation family cited by Croon. They explicitly revisit the trapping calculation and identify a high-coupling plateau when production and attenuation are evaluated in the same region.

This provides a useful cross-check that is logically independent of reproducing Croon Fig. 2:

- Croon: source integral inside \(R_\nu\), attenuation integrated to \(R_{\rm far}\simeq100\) km, and the earlier two-radial-direction approximation.
- Lai: source and attenuation both restricted to \(R_\nu\), full propagation-direction average, and an analytic thin-shell plateau.
- Our current Croon lane: public-profile interior rates are tested against the \(R_{\rm far}=R_\nu\) digitized dashed curve; the \(R_{\rm far}=100\) km low-mass curve remains incomplete without the raw outer profile.

Lai et al. argue that if attenuation is extended from \(R_\nu\) to \(R_{\rm far}\), production in that same region should also be included for consistency. Their numerical study instead uses \(R_{\rm far}=R_\nu\), because the relevant particle densities fall rapidly outside the neutrinosphere. This is a genuine physical prescription difference, not a parameter that should be tuned away.

## 2. Geometry: full angular average versus two radial rays

Lai Eq. (4) uses
\[
A(\omega,\mathbf r)=\frac12\int_{-1}^{1}d(\cos\theta)\,
\exp\!\left[-\int_0^{r_{\max}(\theta)}
\Gamma_{\rm abs}(\omega,\mathbf r_\theta)\,dr_\theta\right].
\]
The direction average is over the full sphere of propagation directions.

In the large-coupling thin-shell limit, only bosons produced in a shell of thickness \(\lambda_{\rm att}\) near the neutrinosphere can escape. The outward projected flux gives
\[
\frac{\int_0^1 \mu\,d\mu}{\int_{-1}^{1}d\mu}=\frac14.
\]
The two-ray \((+z,-z)\) prescription instead gives the factor \(1/2\). Thus, all else equal, the two-ray thin-shell estimate is twice the full-angle result. Lai explicitly notes that the two-ray approximation is not justified in the large-coupling regime.

This is a geometry comparison. It does not by itself determine the complete luminosity ratio because the local source, opacity and radial gradients must also agree.

## 3. Analytic plateau formula

Lai Appendix E derives
\[
\boxed{
L_\infty(m_{Z'})=
\pi R_\nu^2\int_{m_{Z'}}^\infty d\omega\,
\lambda_{\rm att}(m_{Z'},R_\nu,\omega)
\frac{d\dot\epsilon}{d\omega}(m_{Z'},R_\nu,\omega)
}.
\]
If
\[
\frac{d\dot\epsilon}{d\omega}\propto g_{Z'}^2,
\qquad
\lambda_{\rm att}\propto g_{Z'}^{-2},
\]
then their product is independent of \(g_{Z'}\), giving a constant high-coupling plateau.

The implementation in lai2024_plateau_equation_audit.py evaluates the normalized expression
\[
L_\infty=\pi R_\nu^2\int d\omega\,
\frac{(d\dot\epsilon/d\omega)/g_{Z'}^2}
{(1/\lambda_{\rm att})/g_{Z'}^2}.
\]
The unit tests explicitly rescale \(g_{Z'}\) over \(10^{-9}\) to \(0.1\) and verify that the thin-shell result is invariant. This is an algebraic and numerical structural check; it is not yet a reproduction of Lai Fig. 4.

## 4. Rate-level comparison

### 4.1 Neutrino-pair coalescence

Croon Eq. (4.6) is the generic one-neutrino-flavour expression
\[
\Gamma_{\nu\bar\nu}^{\rm Croon,generic}/g_{Z'}^2
=\frac{m_{Z'}^2}{12\pi\omega}f_B(\omega,T).
\]
Croon Sec. 4.4 transfers an additional factor of two to the \(L_\mu-L_\tau\) model:
\[
\Gamma_{\nu\bar\nu}^{\rm Croon,L_\mu-L_\tau}
=2\Gamma_{\nu\bar\nu}^{\rm Croon,generic}.
\]

Lai Eq. (10), already including both \(\nu_\mu\) and \(\nu_\tau\), is printed as
\[
\Gamma_{\nu\bar\nu}^{\rm Lai}/g_{Z'}^2
=\frac{m_{Z'}^2}{4\pi\omega}e^{-\omega/T}.
\]
Therefore, at the level of the printed equations,
\[
\frac{\Gamma_{\nu\bar\nu}^{\rm Lai}}
{\Gamma_{\nu\bar\nu}^{\rm Croon,L_\mu-L_\tau}}
=\frac32\left(1-e^{-\omega/T}\right).
\]
The ratio tends to \(3/2\) in the Maxwell-Boltzmann limit, but it is energy-dependent when the Croon Bose factor is retained. These are not interchangeable rate tables. The difference must be resolved by tracking polarization sums, flavour counting and statistical conventions, rather than applying a constant rescaling.

### 4.2 Semi-Compton production

Croon Eq. (4.7) and Lai Eq. (11) use the same Thomson/no-recoil production structure:
\[
\Gamma_{\rm sC}^{\rm prod}/g_{Z'}^2
=\frac{2\alpha_{\rm EM}}{3m_\mu^2}
\,n_\mu F_{\rm deg}\,v_{Z'}\,f_B(\omega,T).
\]
The public-profile implementation uses
\[
\chi_\mu\equiv n_\mu F_{\rm deg}
\]
as the muon susceptibility input.

### 4.3 Semi-Compton absorption: printed factor and mean-free-path conversion

Lai Eq. (21) states
\[
\Gamma_{\rm abs}^{\rm sC}=\frac23 e^{\omega/T}
\Gamma_{\rm prod}^{\rm sC}.
\]
Lai then converts the lab absorption rate to inverse mean free path using Eq. (15), \(1/\lambda=\Gamma_{\rm abs}^{\rm lab}/v_{Z'}\). The velocity in the production expression cancels, giving Eq. (23):
\[
\frac{1}{g_{Z'}^2\lambda_{\rm sC}^{\rm Lai}}
=\frac{4\alpha_{\rm EM}}{9m_\mu^2}
\chi_\mu(1+f_B).
\]

The current Croon/C0 continuation uses detailed balance without the explicit \(2/3\) factor and does not divide the absorption rate by \(v_{Z'}\):
\[
\frac{\kappa_{\rm sC}^{\rm C0}}{g_{Z'}^2}
=\frac{2\alpha_{\rm EM}}{3m_\mu^2}
\chi_\mu v_{Z'}(1+f_B).
\]
Thus the ratio of the two printed inverse-length coefficients is
\[
\boxed{
\frac{\lambda_{\rm sC}^{-1,\rm Lai}}
{\kappa_{\rm sC}^{\rm C0}}
=\frac{2}{3v_{Z'}}
}.
\]
For \(m_{Z'}\ll\omega\), this tends to \(2/3\); near threshold it increases. The equation-level tests verify this ratio point-by-point.

This is a **convention and normalization audit**, not a conclusion that either implementation is wrong. Before merging the two lanes, we must reconcile the polarization averaging, whether \(\Gamma\) is a lab-frame rate or an inverse length, and the precise definition of the initial/final polarization sums. We must not hide this difference in a fitted opacity factor.

### 4.4 Loop bremsstrahlung and inverse loop bremsstrahlung

Lai includes
\[
n+p\rightarrow n+p+Z'
\]
through the muon/tau-loop-induced photon mixing, together with its inverse absorption. The production spectrum is given in their Eq. (12), and the inverse mean-free-path contribution in Eq. (24). It depends on \(n_n n_p\), the in-medium mixing \(\epsilon(k^2)\), and the transport-weighted nucleon cross section \(\sigma_{np}^{(2)}(T_{\rm cm})\).

Croon discusses additional bremsstrahlung channels but treats them as subdominant in its principal vector benchmark. Lai retains the loop-bremsstrahlung channel explicitly in its trapping calculation. It is therefore not valid to compare the two plateau curves while silently treating their opacity channel sets as identical.

## 5. Transport conventions that must remain separate

| Ingredient | Croon 2021 lane | Lai 2024 lane |
|---|---|---|
| Production region | \(r<R_\nu\) | \(r<R_\nu\) |
| Absorption boundary | \(R_{\rm far}\sim100\) km; also shows \(R_{\rm far}=R_\nu\) sensitivity | \(R_{\rm far}=R_\nu\) |
| Propagation angles | Earlier two-radial-direction approximation | Full \(\cos\theta\) average |
| Semi-Compton absorption | Croon/C0 convention; needs polarization/mean-free-path reconciliation | Explicit \(2/3\) factor and \(1/v\) conversion |
| Loop bremsstrahlung | Estimated as subdominant for the principal benchmark | Included explicitly in production and inverse absorption |
| Reduced absorption | Ordinary absorption in the comparison calculation | Explicitly neglected to compare with earlier work |
| Gravitational redshift | Not included in the C0 comparison | Explicitly neglected in the comparison calculation |
| High-\(g\) behaviour | Depends on the \(R_{\rm far}\) continuation | Analytic constant plateau in the thin-shell limit |

Lai explicitly states that reduced absorption and gravitational redshift are omitted in order to compare directly with earlier calculations. Our corrected B.2 transport lane includes separate conventions for reduced opacity, energy redshift and angular propagation. Those should not be silently mixed into the literal Lai benchmark.

## 6. What can and cannot be used in our model

**Can be used now**
1. The plateau cancellation \(g^2\times g^{-2}\to g^0\) as a transport-code structural test.
2. The full-angle versus two-ray geometric factor as an independent angular-transport check.
3. The explicit Croon/Lai semi-Compton inverse-length comparison as a rate-normalization audit.
4. The printed neutrino-flavour/statistical comparison as a polarization and detailed-balance audit.
5. The distinction between production and attenuation domains as a consistency test.

**Cannot be copied directly**
1. Lai's vector \(Z'\) rates are not axial-vector rates.
2. Its plateau value cannot be used as our axial-vector SN1987A limit.
3. Its inverse loop-bremsstrahlung opacity cannot be inserted without the matching nucleon cross-section input and the same in-medium kinetic-mixing prescription.
4. Its no-reduced-opacity/no-GR comparison curve is not the corrected transport result used in our B.2 lane.
5. Its Stueckelberg benchmark is not automatically the same UV completion as our singlet-Higgs model, even when the low-energy vector coupling is matched.

## 7. Data and reproduction gate

Lai uses the SFHo-18.8 simulation by Bollig et al. [arXiv:2005.07141]. The raw simulation data are not included in the public SNforMuTau repository; its README says to request the data from the authors of Bollig et al. The Garching archive also marks the radial-profile data as access-controlled. Thus the present work is an equation-level and plateau-structure audit, not a full numerical reproduction of Lai Fig. 4.

A full numerical reproduction still requires:
- \(T(r)\), \(n_n(r)\), \(n_p(r)\), \(\mu_\mu(r)\) or \(n_\mu F_{\rm deg}(r)\), and the lapse profile at \(t_{\rm pb}=1\) s;
- the same in-medium \(\epsilon(k^2)\) convention;
- the empirical \(\sigma_{np}^{(2)}(T_{\rm cm})\) input used for Eqs. (12) and (24);
- the exact source/absorption polarization conventions;
- the full angular escape-probability integral.

No outer profile, nucleon cross section, or opacity is fitted to Fig. 4.

## 8. Reproduction code and tests

- lai2024_plateau_equation_audit.py
- test_lai2024_plateau_equation_audit.py

The tests cover:
- the \(2/(3v_{Z'})\) semi-Compton inverse-length ratio;
- the two-flavour/Bose-versus-Maxwell-Boltzmann neutrino coalescence ratio;
- coupling independence of the thin-shell plateau;
- the full-angle \(1/4\) versus two-ray \(1/2\) surface geometry factor;
- input-domain and positivity checks.

The tests establish the algebra encoded in the printed equations. They do not validate the unavailable hydrodynamic profile or the full luminosity curve.
