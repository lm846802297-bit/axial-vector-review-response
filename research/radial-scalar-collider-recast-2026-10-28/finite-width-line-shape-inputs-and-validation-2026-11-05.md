# Finite-width line-shape convolution: implementation and missing Belle II inputs

**Date:** 2026-11-05  
**Scope:** original one-VEV \(S+\mathrm{VLL}\) radial scalar only. No change to the formal referee response or manuscript.

## 1. What is implemented

The module finite_width_line_shape.py implements a data-driven convolution of the original-UV scalar spectral shape with the two-component Crystal-Ball response form described by the Belle II analyses.

For a true scalar invariant mass \(q\), the unnormalized signal spectrum is taken as
\[
\frac{dN_f}{dq}
\propto
\frac{2q^2\,\Gamma_f(q)\,[\sigma_{\rm prod}(q)\epsilon(q)]}
{\pi\left[(q^2-m_s^2)^2+q^2\Gamma_{\rm tot}^2(q)\right]}.
\]
The running partial width \(\Gamma_f(q)\), running total width \(\Gamma_{\rm tot}(q)\), and production-times-efficiency product are explicit inputs. No flat efficiency is silently assumed.

The reconstructed distribution is
\[
\frac{dN_f}{dx_{\rm rec}}
=
\int dq\,
\frac{dN_f}{dq}\,
R(x_{\rm rec}\mid x_{\rm true}(q)),
\]
where \(R\) is a normalized two-component Crystal-Ball mixture with a shared mean. The response parameters may vary with the true fitted observable.

The analysis-specific observable maps are separate:

- Four-muon: \(x_{\rm true}=M_R(q)=\sqrt{q^2-4m_\mu^2}\).
- Tau-pair: \(x_{\rm true}=M_{\rm recoil}(q)=q\).

The fit-window conventions are also separate: the four-muon paper uses a total interval of 60 mass resolutions, and the tau-pair paper uses a total interval of 40 mass resolutions. The module returns the convolved signal shape and the fraction of signal in that nominal fit window. It does **not** recompute a likelihood or a CLs upper limit.

## 2. Required inputs not currently public in the archived supplements

The papers state that their signal response is modeled as a sum of two Crystal-Ball functions sharing a common mean. The archived numerical coupling-limit supplements do not provide the complete mass-dependent parameter tables needed to reconstruct those functions. In particular, the following are missing:

- component fractions;
- component widths;
- tail directions, \(\alpha\) and \(n\) parameters;
- mass-dependent mean biases;
- the full mass-dependent parameter grid.

The published resolution curves/anchors are not enough to uniquely determine the double-Crystal-Ball response. They provide only a resolution scale, not the tail parameters or component mixture.

The finite-width kernel also requires a mass-dependent \(\sigma_{\rm prod}(q)\epsilon(q)\) input. The four-muon analysis has a dedicated scalar efficiency curve, while the tau analysis reports scalar-specific efficiencies and relative differences from the vector benchmark; neither archived numerical limit table contains the full response and production-times-efficiency arrays required for an exact broad-line convolution.

## 3. Input-table schema

The response table is keyed by the fitted observable mass, not necessarily the scalar invariant mass. For four-muon it is \(M_R\); for tau-pair it is \(M_{\rm recoil}\).

Required columns:
- mass_GeV
- fraction_1
- mean_bias_GeV
- sigma_fit_GeV (published nominal resolution used to define the fit window)
- sigma_1_GeV, alpha_1, n_1, tail_side_1
- sigma_2_GeV, alpha_2, n_2, tail_side_2

The two component PDFs are individually normalized and share one mean. Each tail side is specified as left or right. At least two mass points are required; interpolation is linear in the response parameters. The code rejects missing, nonnumeric, nonfinite, or unphysical parameters rather than filling them with guesses.

The production-times-efficiency table must cover the true-mass integration range and include the scalar spin-0 production normalization, ISR convention, and the corresponding analysis selection efficiency. The running-width arrays must include all relevant open UV decay channels at each true mass.

## 4. Validation

Seven local unit tests pass for:
- normalization of each Crystal-Ball component;
- normalization of the two-component mixture;
- the four-muon reduced-mass transformation and tau recoil-mass identity;
- a synthetic four-muon convolution;
- the tau fit-window width (40 resolutions total);
- rejection of incomplete response parameter tables.

The synthetic tests validate the numerical kernel only. They do not validate any Belle II response parameters or experimental efficiency.

## 5. Current status and next step

The finite-width convolution machinery is implemented and unit-tested, but **no real Belle II finite-width convolution has been run**. It is not possible to claim a finite-width recast until the response parameters and production-times-efficiency inputs are obtained from Belle II auxiliary material or reconstructed from sufficiently detailed published figures with a quantified digitization uncertainty.

If those inputs remain unavailable, a Gaussian or approximate Crystal-Ball response may be used only as a labeled sensitivity study. It must not be presented as the experiment's exact response or as a new 90% CL exclusion.
