# Axial stellar-cooling calculation — two-VEV baseline

This is a clean research line based on the current \`main\` at branch creation.
It carries forward only the useful generic-current calculations from the
former PR #30; it does not inherit that PR's commit history.

## 1. Model conventions

\[
S=\frac{v_s+s+i a_s}{\sqrt2},\quad Q_X(S)=2,\qquad
\sigma=\frac{v_\sigma+\sigma_r+i a_\sigma}{\sqrt2},\quad Q_X(\sigma)=1.
\]

With \(D_\mu=\partial_\mu-i g_X Q_X A'_\mu\),

\[
v_X=\sqrt{4v_s^2+v_\sigma^2},\qquad
m_{A'}=|g_X|v_X.
\]

The eaten and physical CP-odd directions are

\[
G=\frac{2v_s a_s+v_\sigma a_\sigma}{v_X},\qquad
a_\perp=\frac{v_\sigma a_s-2v_s a_\sigma}{v_X}.
\]

In the charged-lepton seesaw limit, the S-phase Yukawa is \(m_\ell/v_s\).
Its projection onto the eaten Goldstone is therefore

\[
|g_{G\ell\ell}|=\frac{m_\ell}{v_s}\frac{2v_s}{v_X}
=\frac{2m_\ell}{v_X}
=\frac{2|g_A^\ell|m_\ell}{m_{A'}}
\quad (|g_A^\ell|=|g_X|).
\]

Thus the old \(m_\ell/v_s\) Goldstone result is recovered only in the
\(v_\sigma=0\) limit. The exact map at fixed \((m_{A'},g_X)\) is
\(v_s=m_{A'}/[2|g_X|\sqrt{1+r_\sigma}]\), where
\(r_\sigma=v_\sigma^2/(4v_s^2)\).

## 2. Carried-forward calculation components

- \`stellar_semi_compton_axial_matrix_element.py\`: exact vacuum tree-level
  \(\gamma\mu\to\mu A'\) amplitude, EM Ward checks, exact lab/CM phase space,
  and T/L projections in the frame of the supplied momenta.
- \`stellar_semi_compton_thermal_rate.py\`: optically thin homogeneous-cell
  polarization-summed production prototype, with Fermi/Bose distributions
  and final-state Pauli blocking.
- \`stellar_semi_compton_thermal_convergence.py\`: quadrature/cutoff study.
- \`axial_decay_widths.py\`: current-level \(A'\to\nu\bar\nu,\mu^+\mu^-\)
  partial-width comparison, independent of the VEV parameterization.
- \`two_vev_axial_mapping.py\`: exact gauge-mass and eaten-Goldstone map.

The matrix-element routine takes \(g_V,g_A,m_{A'}\) as independent physical
inputs. It does not need to be rewritten when the VEV parameterization changes.
The VEV-to-Goldstone map is isolated in its own module.

## 3. Local validation commands

Run from this directory:

\`\`\`bash
python -m unittest -v test_two_vev_axial_mapping.py
python stellar_semi_compton_axial_matrix_element.py --check
python axial_decay_widths.py
python stellar_semi_compton_thermal_rate.py --check
\`\`\`

The full convergence sweep is deliberately not part of the first acceptance
gate. First establish that the amplitude and homogeneous-cell integration
checks pass; then run a reduced order/cutoff sweep and record the CSV output.

## 4. Physics/validation boundaries

The semi-Compton matrix element is a vacuum tree-level calculation. The
thermal script is a homogeneous, optically thin, polarization-summed local
rate. It is not a medium-rest-frame T/L decomposition, opacity, trapping,
radial supernova transport, SN1987A luminosity calculation, or LESN exclusion.

No supernova profile, radial transport, diffusion, or final exclusion contour
is claimed in this branch. No result is added to the referee-facing letter.

## 5. Acceptance checklist

- [ ] Exact two-VEV mass relation and Goldstone projection verified.
- [ ] Semi-Compton \`--check\` executed locally on this branch.
- [ ] Decay-width checks executed locally.
- [ ] Thermal \`--check\` executed locally.
- [ ] Reduced quadrature/cutoff stability CSV archived.
- [ ] Medium-frame T/L opacity and SN transport remain explicitly out of scope.
