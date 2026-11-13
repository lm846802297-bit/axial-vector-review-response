# Axial stellar-cooling calculation — two-VEV baseline

This is a clean research line based on the current `main` at branch creation.
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

- `stellar_semi_compton_axial_matrix_element.py`: exact vacuum tree-level
  \(\gamma\mu\to\mu A'\) amplitude, EM Ward checks, exact lab/CM phase space,
  and T/L projections in the frame of the supplied momenta.
- `stellar_semi_compton_thermal_rate.py`: variant-local adapter to the shared optically thin homogeneous-cell thermal-rate implementation in `../stellar-cooling-shared-20261105/`; it resolves this directory's two-VEV matrix-element module.
- `stellar_semi_compton_thermal_convergence.py`: variant-local adapter to the shared quadrature/cutoff study.
- The identical thermal-convergence CSV is stored once in the original-UV model directory and is shared by reference.
- `axial_decay_widths.py`: current-level \(A'\to\nu\bar\nu,\mu^+\mu^-\)
  partial-width comparison, independent of the VEV parameterization.
- `two_vev_axial_mapping.py`: exact gauge-mass and eaten-Goldstone map.

The matrix-element routine takes \(g_V,g_A,m_{A'}\) as independent physical
inputs. It does not need to be rewritten when the VEV parameterization changes.
The VEV-to-Goldstone map is isolated in its own module.

The neutrino partial-width helper uses the inclusive light-neutrino result
\(\mathrm{Tr}(G_\nu^\dagger G_\nu)=2\) for a unitary three-flavour PMNS
rotation. It assumes active-heavy mixing is negligible and all heavy-neutrino
channels are closed. If an \(N_R\) threshold opens, the total width must be
extended before computing branching fractions or lifetimes.

## 3. Local validation commands

Run from this directory:

```bash
python -m unittest -v test_two_vev_axial_mapping.py
python stellar_semi_compton_axial_matrix_element.py --check
python axial_decay_widths.py
python stellar_semi_compton_thermal_rate.py --check
```

The local acceptance has been run and is recorded in
`validation-results-2026-11-05.md`; the associated machine-readable data are in
`../stellar-cooling-original-uv-model-20261105/thermal-convergence-2026-11-05.csv`. The convergence script now derives its
reference cutoffs from the same defaults as `thermal_emissivity`, unless
explicit reference cutoffs are supplied.

## 4. Physics/validation boundaries

The semi-Compton matrix element is a vacuum tree-level calculation. The
thermal script is a homogeneous, optically thin, polarization-summed local
rate. It is not a medium-rest-frame T/L decomposition, opacity, trapping,
radial supernova transport, SN1987A luminosity calculation, or LESN exclusion.

No supernova profile, radial transport, diffusion, or final exclusion contour
is claimed in this branch. No result is added to the referee-facing letter.

## 5. Acceptance checklist

- [x] Exact two-VEV mass relation and Goldstone projection verified.
- [x] Semi-Compton `--check` executed locally on the fetched branch source.
- [x] Decay-width checks executed locally.
- [x] Thermal `--check` executed locally.
- [x] Reduced and higher-order quadrature/cutoff stability results archived.
- [ ] Medium-frame T/L opacity and SN transport: explicitly deferred, not part of this phase.
