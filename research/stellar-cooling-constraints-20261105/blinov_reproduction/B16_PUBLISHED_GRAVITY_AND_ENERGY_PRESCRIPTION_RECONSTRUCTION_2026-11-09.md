# Reconstruction of the published gravity and energy prescription in Blinov et al. (2026)

Date: 2026-11-09  
Purpose: distinguish the literal published Fig. 7 prescription from a full-GR extension. This audit uses the version-of-record paper and the gravitational-redshift supplement that it cites; it does not require raw Garching tables.

## Executive conclusion

**The missing spatial metric A(r) is not a prerequisite for reproducing Blinov et al.'s published Appendix-B calculation.** The paper uses a lapse correction in the source luminosity and escape threshold, but uses Euclidean straight chords in the opacity integral. It does not contain A(r), a proper spatial-volume factor, or GR-bent particle trajectories.

The cited gravitational-redshift treatment, Caputo et al., arXiv:2201.09890, explicitly states that the Garching pseudo-Newtonian model is treated with flat spatial coordinates and distant-observer time; the lapse redshifts the emitted particle energy and multiplies the source luminosity by lapse squared. This explains the structure of Blinov's B.1.

The remaining ambiguity is narrower: Sec. 4.1 describes omega as energy at spatial infinity, whereas the Appendix-B.1 lower limit and source measure identify omega as the local energy at emission. B.2 then keeps the same omega along the Euclidean chord. The literal Appendix-B formula is the reproduction target; the path-redshift-only calculation is a separate sensitivity extension.

## 1. Direct reconstruction of B.1

Blinov et al. write the source luminosity in the form

```
L_V = ∫_0^Rmax 4π r² dr N(r)²
      ∫_[mV/N(r)]^∞ dω [k ω²/(2π²)] Γ_prod(r,ω) O(r,ω).
```

The structure has a direct interpretation:

- omega is the local energy in the emitting-medium frame;
- the escape condition is N(r) omega > mV, hence omega_min = mV/N(r);
- N(r)^2 accounts for the redshift of particle energy and the conversion between local proper time and distant-observer time;
- k = sqrt(omega² - mV²) and the phase-space measure are evaluated with the local energy.

This is not merely inferred from notation. Caputo et al., arXiv:2201.09890, Supplemental Material C, states that E_infinity = E_local × lapse, that the local emission threshold is E_local > m_a/lapse, and that the luminosity at infinity carries a total lapse² factor. The same supplement explicitly says that the Garching pseudo-Newtonian model is treated with flat spatial coordinates and distant-observer time.

Sources:
- Blinov et al., JHEP 06 (2026) 155, Sec. 4.1 and Appendix B, Eqs. (B.1)--(B.5): https://doi.org/10.1007/JHEP06(2026)155
- Caputo et al., *Low-Energy Supernovae Severely Constrain Radiative Particle Decays*, arXiv:2201.09890, Supplemental Material C, especially Eq. (S16): https://arxiv.org/abs/2201.09890

## 2. What B.2 actually propagates

The published B.2 opacity is

```
tau(r,omega,cos(theta)) =
  ∫_0^smax ds Gamma_abs*(r'(s),omega) / vV(omega),

r'(s) = sqrt(r² + s² + 2 r s cos(theta)),
vV(omega) = sqrt(1 - mV²/omega²).
```

This is a Euclidean straight-chord path. The formula has:

- no A(r) or g_rr;
- no proper-distance factor A(r) dr;
- no GR geodesic bending;
- no explicit replacement omega -> E_infinity/N(r') along the chord.

The reduced absorption rate in B.4 contains the thermal factor 1 - exp[-omega/T(r')]. Thus, in a literal reading of Appendix B, the same omega is passed to the local opacity kernel at every point along the chord. This is the fixed-omega prescription used by the current B.16 reproduction baseline.

## 3. The notation issue that remains

The main text, Sec. 4.1, describes omega as the energy at spatial infinity. The B.1 source integral instead has the local-energy threshold mV/N(r) and the local phase-space measure multiplied by N(r)^2. Those statements cannot all refer to the same untransformed integration variable.

The safe reproduction rule is:

1. implement B.1 exactly as printed, interpreting its integration variable as the local source energy, as required by the mV/N(r) threshold and the cited lapse-squared prescription;
2. implement B.2 exactly as printed, keeping the same omega in the path opacity and in vV;
3. retain the path-redshift-only alternative separately, with omega_loc(r') = omega_source N(r_source)/N(r'), and do not substitute it for the published baseline without evidence that the authors used it.

The article does not provide the numerical code, so the exact unpublished implementation cannot be inferred beyond the printed prescription. The mismatch between the Sec. 4.1 description and Appendix-B notation should be reported as a paper-level convention ambiguity, not resolved by silently changing the equations.

## 4. Consequence for the role of A(r)

A full static-GR extension would require A(r), or an enclosed-mass profile M(r), to calculate proper path lengths and curved geodesics. That is a legitimate additional study, but **it is not needed to reproduce the approximation that Blinov actually writes in Appendix B**.

Accordingly:
- A(r) is reclassified as an optional full-GR extension input;
- the lapse N(r) and the thermodynamic profiles entering B.1--B.5 remain the relevant figure-reproduction inputs;
- the 20--25 km thermodynamic continuation remains important because the published B.2 integral extends to Rmax = 25 km and the current neutrino inverse-decay path audit finds a non-negligible outer-shell contribution;
- no synthetic A(r), TOV replacement, or cross-snapshot splice is introduced.

## 5. Reconciliation with existing diagnostics

The current-profile fixed-omega baseline remains the paper-faithful calculation. The path-redshift-only variant is retained as a separate physical sensitivity test. At 10 MeV it reduces the strong-endpoint residual from +92.2406% to +36.7448%, but this does not make it the published B.2 prescription.

The strong-absorption radial-path audit remains relevant and independent of this convention question:
- the 8--22 km path group accounts for about 75.54% of the source-weighted neutrino inverse-decay optical depth;
- 22--25 km contributes about 19.07%;
- the outer shell is important but is not the only important attenuation region.

These results are recorded in:
- `B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md`
- `B16_NEUTRINO_INVERSE_DECAY_RADIAL_PATH_SYNTHESIS_2026-11-09.md`

## 6. Revised project decision

Do not wait for A(r) to continue reproducing Fig. 7. The next checks should reconstruct and stress-test the published algorithms using the current profile:

1. extend the exact B.13 versus B.14--B.16 Compton comparison across the Fig. 7 masses, especially 0.1 and 1 MeV where the paper says the Compton channel is relevant;
2. keep the fixed-omega B.2 implementation as the reproduction baseline and quantify the path-redshift alternative separately;
3. continue checking the nonlinear strong-absorption response and the 20--25 km neutrino opacity using the already reconstructed profile;
4. keep raw-profile uncertainty explicit, but do not make it a prerequisite for these method-level checks.

No production axial-vector output, manuscript, or referee response is modified by this audit.
