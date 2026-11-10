# B5-1d PyR@TE 3 model-input preparation

**Status:** model file prepared; PyR@TE execution has not yet been completed in the current runtime.

## Purpose

This input is an independent external-generator representation of the original
\(U(1)_{L_\mu-L_\tau}\) model with one complex singlet and two charged VLL
Dirac fermions. It is intended to validate the one-loop dimensionless
couplings above the common VLL threshold. It does not change the production
RGE implementation or the EFT matching prescription.

## Fixed conventions

- Gauge ordering: \(U(1)_Y\), \(U(1)_X\), \(SU(2)_L\), \(SU(3)_c\).
- \(X(L_\mu,\mu_R,E_\mu)=+1,-1,+1\), with opposite tau charges.
- Both chiral components of \(E_\mu\) have \((Y,X)=(-1,+1)\); both tau VLL
  components have \((Y,X)=(-1,-1)\).
- \(H\sim(\mathbf2,1/2,0)\), \(S\sim(\mathbf1,0,+2)\), so
  \(m_X=2g_Xv_S\).
- \(S_\mu=S\) and \(S_\tau=S^\ast\).
- The scalar potential uses exactly
  \[
  V_4=\lambda_H(H^\dagger H)^2+
      \lambda_S(S^\dagger S)^2+
      \lambda_{HS}(H^\dagger H)(S^\dagger S).
  \]
- The SM quark fields retain three generations. The Yukawa substitutions
  select only \(y_t\), matching the top-dominance approximation used in the
  current numerical run. The direct electron Yukawa is set to zero for that
  approximation; it can be restored for a full SM trace comparison.
- The VLL Dirac mass terms are omitted from this model input because the
  target comparison is the mass-independent \(\overline{\rm MS}\) beta
  functions of dimensionless couplings. Their presence does not change those
  one-loop beta functions above the common threshold.

## Kinetic mixing

PyR@TE 3 handles multiple Abelian factors through its generalized gauge
coupling matrix. The model keeps the off-diagonal coupling \(g_{YX}\) explicit
rather than deleting it. The comparison to B5-1b is made at
\(g_{YX}(M_E)=0\). The exact Weyl-spectrum sum gives
\(\operatorname{Tr}(YX)=0\), so the one-loop additive mixing source must
vanish at this boundary.

The independent model output should be checked before imposing
\(g_{YX}=0\) in any substitution. In particular, do not erase the
off-diagonal beta function before verifying its source.

## Pinned external implementation

- PyR@TE 3 upstream repository: https://github.com/LSartore/pyrate
- Pinned upstream commit: 04b219c2016f3fc4f2371d72607edc26a7e06364
- Reference: L. Sartore and I. Schienbein, *PyR@TE 3*, arXiv:2007.12700.

## Execution and acceptance checklist

1. Run PyR@TE 3 with all one-loop contributions and gauge-invariance checking.
2. Confirm the model file passes PyR@TE's gauge-invariance validation.
3. Extract the beta functions for \(g_Y,g_X,g_2,g_3,y_t,y_\mu,y_\tau,
   \lambda_\mu,\lambda_\tau,\lambda_H,\lambda_S,\lambda_{HS}\).
4. Set \(g_{YX}=0\) only after recording its beta function and verify that its
   one-loop source vanishes.
5. Normalize the output to the potential and hypercharge conventions above.
6. Compare every coefficient against the independent analytic audit and the
   production RHS.
7. Archive the verbatim PyR@TE output, the normalized comparison table, the
   model-file hash, and the pinned upstream commit.

Until those steps actually run, this is a prepared validation input, not a
completed PyR@TE cross-check.
