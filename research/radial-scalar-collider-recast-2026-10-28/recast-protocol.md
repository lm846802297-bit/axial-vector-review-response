# Recast protocol — radial scalar \(s\)

**Model scope:** original paper's one-VEV UV model only. The benchmark identities are \(m_{A'}=2g_Xv_s\), \(m_s^2=2\lambda_Sv_s^2\), and \(y_{s\ell\ell}=m_\ell/v_s\), subject to the stated VLL mass-eigenstate assumptions. Do not import a different UV completion or scalar sector into this protocol.

## 1. Fixed model definition

Before generating a scan, record a versioned benchmark card containing:

- \(m_s,m_{A'},g_X,v_s\) and the identity \(m_{A'}=2g_Xv_s\);
- \(\lambda_S=m_s^2/(2v_s^2)\) and the declared perturbativity threshold;
- the portal potential convention, renormalization/matching scale and boundary condition for \(\lambda_{HS}\);
- the \(h\)-\(s\) mixing prescription, including whether it is a tree-level input or a loop/pole-scheme result;
- \(M_{E_\mu},M_{E_\tau}\), left/right mixing angles and the exact mass-eigenstate scalar couplings;
- all open scalar and \(A'\) decay channels;
- the \(A'\) branching fractions used in cascade signatures;
- the scan's confidence-level convention and the exact experimental observables to compare.

Do not infer a unique \(m_s\) interval from the \(m_{A'}\)-\(g_X\) plane alone. The portal and decay inputs also matter.

## 2. Decay and lifetime calculation

At every point compute the partial widths, total width and branching fractions. For each channel \(i\),

\[
\Gamma_s^{\mathrm{tot}}=\sum_i\Gamma(s\to i),\qquad
\mathrm{BR}(s\to i)=\frac{\Gamma(s\to i)}{\Gamma_s^{\mathrm{tot}}}.
\]

The minimum channel list is:

- \(s\to\mu^+\mu^-\) above threshold;
- \(s\to\tau^+\tau^-\) above threshold;
- \(s\to A'A'\) for \(m_s>2m_{A'}\);
- mixing-mediated Standard Model final states with the correct mass-dependent SM-Higgs reference widths;
- loop-induced channels where relevant;
- decays to vector-like leptons if their thresholds are open;
- cascade decays of \(A'\), including visible and invisible final states.

The proper decay length is

\[
c\tau_s=\frac{\hbar c}{\Gamma_s^{\mathrm{tot}}}.
\]

Prompt-search efficiencies must not be used unchanged if the model point predicts a displaced or detector-stable scalar. The same warning applies to \(A'\) daughters.

## 3. Belle II four-muon analysis

For the published process \(e^+e^-\to\mu^+\mu^-s\), \(s\to\mu^+\mu^-\), the predicted visible signal is

\[
N_{4\mu}^{\mathrm{pred}}
=\mathcal L_{\mathrm{int}}\,
\sigma(e^+e^-\to\mu^+\mu^-s)\,
\mathrm{BR}(s\to\mu^+\mu^-)\,
A\epsilon.
\]

At leading order in a muon-radiation topology, the production rate scales with \(|y_{s\mu\mu}|^2\), but the numerical coefficient and acceptance must be taken from the actual analysis or a validated event simulation. The branching fraction must use the total width of this UV scalar, including \(s\to A'A'\) where open and portal-mediated channels where relevant.

Required procedure:

1. Extract the mass-dependent 90% CL upper limit on the source observable and its mass grid from the publication/supplement.
2. Reproduce the published muonphilic-scalar benchmark with the paper's exact normalization and branching assumptions.
3. Determine whether the UV model has the same production kinematics and prompt-decay topology. If not, use published efficiency information or validate a dedicated simulation.
4. For each UV point, compare predicted signal with the source's mass-dependent limit. Keep the source CL and statistical convention.
5. If only \(\sigma\times\mathrm{BR}\) limits and not the needed efficiency maps are available, label the result as a published-limit reinterpretation and document the approximation; do not call it a full detector-level recast.

## 4. Belle II tau-pair resonance analysis

For a scalar resonance in \(e^+e^-\to\mu^+\mu^-\tau^+\tau^-\), map the actual production mechanism and the observable used by the publication. The signal prediction must include the correct production coupling and \(\mathrm{BR}(s\to\tau^+\tau^-)\), not merely a generic scalar coupling.

Repeat the same five-step source extraction, benchmark reproduction, topology/acceptance check, per-point comparison, and limitations log used for the four-muon analysis. Treat the tau-pair analysis as an independent search; do not combine its upper limits with the four-muon search without a statistically justified combination.

## 5. Higgs-portal and heavier-mass searches

For searches whose production is inherited from Higgs mixing, begin with the model's validated mixing prescription. Away from near degeneracy and for sufficiently small mixing, rates may scale approximately as \(\sin^2\theta_{hs}\) times a reference SM-Higgs rate at mass \(m_s\). This scaling is not a substitute for the full calculation when the portal boundary, widths, or pole overlap matter.

Check separately:

- direct searches for a singlet-like scalar produced through mixing;
- Higgs signal-strength constraints;
- exotic \(h\to ss\) decays if \(m_s<m_h/2\), using the actual trilinear and branching fraction;
- multi-lepton/cascade searches for \(s\to A'A'\);
- higher-mass searches only when the production and decay topology can be matched to the published observable.

The current two-benchmark one-loop \(h\)-\(s\) self-energy is an input to be audited, not a global experimental exclusion. The near-degenerate region around \(m_s\simeq m_h\) remains unclassified until a width/pole-consistent treatment and applicable search constraints are available.

## 6. Translating a coupling limit

If a source provides a valid bound on \(|y_{s\mu\mu}|\), the stated mass-proportional benchmark gives

\[
|g_X|\leq \frac{|y_{s\mu\mu}|_{\mathrm{lim}}m_{A'}}{2m_\mu}.
\]

This translation is valid only if:

1. the UV matching relation for \(y_{s\mu\mu}\) is the one used at that point;
2. the source's scalar production and decay assumptions are reproduced or corrected;
3. the source mass and lifetime acceptance apply;
4. the fixed \(m_s\) is inside the source's applicability range;
5. any effect of the additional \(A'\) and Higgs-portal channels is included.

If any condition is not met, report the source limit as contextual evidence only, not a UV-model exclusion.

## 7. Mass scan and classification

The first pass should use a transparent mass grid that resolves:

- the published Belle II ranges \(0.212\text{--}9.0\,\mathrm{GeV}\) and \(3.6\text{--}10\,\mathrm{GeV}\);
- thresholds \(m_s=2m_\mu\), \(2m_\tau\), and \(2m_{A'}\);
- \(m_s=m_h/2\), where exotic Higgs decays can open;
- \(m_s\simeq m_h\), where portal mixing can become sensitive to widths and pole treatment;
- the heavier-mass regions for which a direct search has been identified.

At each fixed \((m_{A'},g_X,\text{portal/VLL benchmark})\), classify each point as **excluded**, **passes the evaluated constraints**, **unclassified**, or **theoretically inconsistent**. The output must state which searches were evaluated; “passes evaluated constraints” is not equivalent to globally allowed.

## 8. Reproducibility requirements

- Keep raw source data separate from transformed tables.
- Record URLs, version/retrieval dates, units, CL and SHA-256 for local inputs.
- Version the benchmark card and scripts.
- Include tests for threshold behavior, positive widths, branching-ratio normalization, and dimensional consistency.
- Reproduce each source's benchmark before applying it to the UV model.
- Store plots with visible source domains; never extend a limit line beyond its stated validity.
- Every final excluded region must be traceable to source data, a model prediction, and a stated statistical comparison.
