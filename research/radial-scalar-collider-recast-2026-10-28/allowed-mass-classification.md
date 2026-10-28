# Scalar-mass classification: definition and acceptance criteria

## 1. Why there is not yet one universal allowed interval

The scalar self-coupling condition constrains a fixed UV benchmark through

\[
\lambda_S=\frac{2g_X^2m_s^2}{m_{A'}^2}
\leq\lambda_S^{\max}
\quad\Longrightarrow\quad
m_s\leq \sqrt{\frac{\lambda_S^{\max}}{2}}\frac{m_{A'}}{g_X}.
\]

This is a theoretical upper bound conditional on \((m_{A'},g_X,\lambda_S^{\max})\), not a collider exclusion. Experimental viability additionally depends on the scalar's production rate, total width, branching fractions, lifetime, portal mixing, and the actual search acceptance.

Consequently, the result should initially be reported as a set of allowed/excluded/unclassified points at fixed benchmark inputs, not as a single number or universal mass interval.

## 2. Parameter basis

Use \((m_s,m_{A'},g_X)\) as the visible scan coordinates, but retain the following derived or fixed inputs in each record:

| Quantity | Definition / requirement |
|---|---|
| \(v_s\) | \(m_{A'}/(2g_X)\) under the model's one-VEV convention |
| \(y_{s\mu\mu}\) | Exact matched coupling; compare with \(m_\mu/v_s\) only after checking mass-eigenstate mixing assumptions |
| \(y_{s\tau\tau}\) | Exact matched coupling, with the corresponding tau-sector assumptions |
| \(\lambda_S\) | \(m_s^2/(2v_s^2)\); store the selected \(\lambda_S^{\max}\) |
| Portal input | \(\lambda_{HS}\), a boundary condition, or a validated pole/mixing prescription; these are not interchangeable without matching |
| VLL inputs | \(M_{E_\mu},M_{E_\tau}\), left/right mixings and the exact scalar vertices |
| Widths | Every kinematically open scalar and \(A'\) decay, including \(s\to A'A'\) |
| Search metadata | Observable, mass grid, CL, production/decay benchmark, acceptance and lifetime assumptions |

## 3. Point classification

Each scan point must receive one and only one status:

1. **Theoretically inconsistent:** violates the declared perturbativity or other theoretical requirements.
2. **Excluded by an evaluated search:** a validated model prediction exceeds a source's applicable observed upper limit at the stated CL.
3. **Passes evaluated constraints:** passes all constraints that were actually implemented and declared applicable.
4. **Unclassified:** a relevant constraint is known to exist but its normalization, acceptance, branching fraction, lifetime dependence, or numerical data have not been established.

The statuses are not interchangeable. In particular, missing efficiency information means “unclassified” or “published-limit reinterpretation with an explicit caveat,” not “allowed.”

## 4. Minimum acceptance gates for a reported mass interval

A mass interval may be described as an experimentally validated allowed interval only if all of the following hold:

- the UV Lagrangian and benchmark assumptions are frozen;
- the perturbativity criterion is stated and applied point by point;
- all source curves used in the claim have been transcribed from the publication/supplement with their mass domains and confidence levels;
- the experiment's own scalar benchmark is reproduced within documented numerical/interpolation accuracy;
- production, total width, branching fractions and lifetime are computed consistently;
- \(s\to A'A'\) and its visible/invisible cascades are included wherever open;
- the Higgs-portal/mixing input is consistent with the selected boundary and with the near-degenerate pole treatment;
- all applicable searches in the declared scope are applied;
- points with unresolved detector acceptance or incomplete search coverage remain explicitly unclassified;
- the connectedness of the allowed set is checked before presenting it as one interval.

Until all gates pass, use the phrase **“conditional benchmark classification”** or **“allowed by the constraints evaluated so far”**, not “the allowed scalar-mass range.”

## 5. Immediate deliverables

1. Extract the public numerical curves for the Belle II four-muon and tau-pair searches.
2. Build a minimal, unit-tested width/branching-ratio calculator for the radial scalar and \(A'\).
3. Reproduce each paper's scalar benchmark before using its upper limits.
4. Map the model-specific coupling and decay pattern onto the measured observables.
5. Audit Higgs-portal direct searches and near-degenerate mixing separately.
6. Produce a table with benchmark inputs, theory status, each search status, and final point classification.
