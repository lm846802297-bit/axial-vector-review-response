# Calculation protocol and validation gates — Higgs--scalar mixing

## A. Frozen conventions

Before adding diagrams, record in a benchmark card:
- scalar-potential sign convention and field/VEV normalization;
- renormalization scheme and scale hierarchy, with separate entries for \(M_E\), the physical heavy singular values, matching scale \(\mu_M\), hard-loop subtraction scale \(\mu_R^{\rm hard}\), and low-energy EFT scale \(\mu_{\rm EFT}\);
- whether the portal boundary is imposed at one central \(\mu_M\) and then RG-evolved, rather than reset when \(\mu_M\) is varied;
- gauge-fixing parameter and gauge choice;
- tadpole and VEV-renormalization prescription;
- field-renormalization matrix and mixing counterterm convention;
- perturbative order and the exact set of retained diagrams;
- portal boundary condition and its status as a conditional input.

No result may combine pieces computed in incompatible conventions without an explicit conversion.

## B. Matching audit

For each contribution, record:
1. full-theory diagram and analytic expression;
2. EFT diagram/operator and analytic expression;
3. UV pole and counterterm;
4. finite hard remainder;
5. finite soft contribution;
6. matching-scale dependence;
7. independent symbolic or numerical check.

The sum must be complete at the declared order. A subset may be retained as a diagnostic but cannot be called the physical matched self-energy.

## C. Propagator and pole calculation

Use a renormalized \(2\times2\) inverse propagator with both diagonal and off-diagonal entries. The pole equation is
\[
\det\Gamma_{\mathrm{inv}}(s_i)=0.
\]
Compute residues from the derivative matrix at each complex pole. Record the Riemann sheet, branch choices, numerical root-finding tolerances, and pole-tracking prescription.

For nearly overlapping poles, calculate the coherent production/decay amplitude. Do not infer a detector-level rate from a real mixing angle or an eigenvector ratio.

## D. Validation

Required checks:
- zero-momentum limit reproduces the portal threshold;
- large-\(M_E\) expansion reproduces the derivative matching coefficient;
- UV poles cancel after counterterms;
- absorptive parts satisfy the optical-theorem channel accounting;
- matching-scale dependence is reduced to higher order;
- physical pole observables are gauge-parameter independent to the claimed order;
- numerical roots and residues are stable under precision, step-size, and continuation changes;
- non-degenerate limits reproduce the isolated-pole approximation where expected.

## E. Reporting

Every result is labelled as one of:
- analytic identity;
- independently reproduced numerical subcalculation;
- selected diagram subset;
- complete matched result at a stated order;
- physical pole/residue result;
- observable line-shape prediction.

Uncomputed regions remain unassessed. The report must not turn an intermediate mixing diagnostic into an allowed/excluded statement.