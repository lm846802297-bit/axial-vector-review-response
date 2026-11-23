# RC-001 — Exact longitudinal inverse-kernel completion of \(R_{\rm FG}\)

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-d  
**Status:** the residual \(R_{\rm FG}\) from the transverse Yang–Mills inverse kernel has been identified exactly as minus the propagator-sandwiched longitudinal \(p_\mu p_\nu\) difference. Adding the longitudinal part converts the transverse inverse kernel into the full Feynman-gauge inverse kernel and removes \(R_{\rm FG}\) algebraically. This identifies the precise Lorentz tensor the complete gauge-fixed/BRST analysis must account for. It is not a ghost-diagram calculation and does not yet prove cancellation in the full matter amplitude.

## 1. Transverse Yang–Mills kernel

With \(\kappa=k+q\), define
\[
K_{\mu\nu}(p)=p^2g_{\mu\nu}-p_\mu p_\nu,
\qquad
D_{\mu\nu}^{\rm FG}(p)=\frac{g_{\mu\nu}}{p^2}.
\]
The already checked three-W contraction gives the transverse inverse-kernel difference \(K(\kappa)-K(k)\). Its Feynman-gauge propagator sandwich is
\[
\boxed{
D^{\rm FG}(\kappa)\,[K(\kappa)-K(k)]\,D^{\rm FG}(k)
=D^{\rm FG}(k)-D^{\rm FG}(\kappa)+R_{\rm FG},
}
\tag{1.1}
\]
where
\[
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-\kappa^\mu\kappa^\nu}{k^2\kappa^2}.
\]
This is the exact remainder previously retained in IVh/IVl.

## 2. Longitudinal inverse-kernel difference

Define the longitudinal tensor
\[
L_{\mu\nu}(p)=p_\mu p_\nu.
\]
Its propagator sandwich is
\[
\begin{aligned}
D^{\rm FG}(\kappa)\,[L(\kappa)-L(k)]\,D^{\rm FG}(k)
&=\frac{\kappa^\mu\kappa^\nu-k^\mu k^\nu}
{\kappa^2k^2}\\
&=\boxed{-R_{\rm FG}^{\mu\nu}}.
\end{aligned}
\tag{2.1}
\]
Thus the transverse remainder is canceled exactly by the longitudinal inverse-kernel difference:
\[
D^{\rm FG}(\kappa)\left[
K(\kappa)-K(k)+L(\kappa)-L(k)
\right]D^{\rm FG}(k)
=D^{\rm FG}(k)-D^{\rm FG}(\kappa).
\tag{2.2}
\]

Since
\[
K_{\mu\nu}(p)+L_{\mu\nu}(p)=p^2g_{\mu\nu},
\]
the sum is precisely the full Feynman-gauge quadratic inverse operator (up to the overall \(i\) and sign convention of the propagator).

## 3. What this means for the STI calculation

Equation (2.1) gives an unambiguous target for the missing completion: the full gauge-fixed/BRST identity must account for the longitudinal tensor \(p_\mu p_\nu\) at the two internal-W endpoints. In the complete nonabelian theory this is organized through gauge fixing, BRST variations, ghost Green functions, and inverse-propagator terms.

It would be incorrect to identify (2.1) with a ghost Feynman diagram by itself. The calculation here is only the exact Lorentz algebra of the inverse kernels. The actual ghost/BRST terms must still be derived with the same momentum routing, weak tensors, and open matter-current ordering.

A useful consequence is that the \(R_{\rm FG}\) term is not an arbitrary leftover: its exact tensor structure is fixed. Any proposed STI completion must reproduce \(-R_{\rm FG}\) after the same two Feynman-gauge propagators are attached.

## 4. Exact reproduction

- Source: \`calculations/RC-001-dim6-WW-fivepoint-longitudinal-inverse-kernel-completion.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_longitudinal_inverse_kernel_completion.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-longitudinal-inverse-kernel-completion.txt\`

The local exact SymPy audit checks:
- transverse kernel sandwich (1.1): 16/16 Lorentz components;
- longitudinal sandwich (2.1): 16/16 components;
- \(K+L=p^2g\) and the full Feynman-gauge chain (2.2): 32/32 components.

No external momenta, matter currents, or loop integrals are approximated in these identities. This is an exact symbolic identity, not a numerical benchmark and not a GitHub Actions result.

## 5. Remaining boundary

The next calculation is not to delete \(R_{\rm FG}\). It is to derive the BRST/ghost Slavnov–Taylor terms and demonstrate that their insertion into the actual six-pair matter chains supplies the longitudinal completion (2.1), together with the appropriate inverse-propagator and external-field terms. Until that is done, \(R_{\rm FG}\) remains explicit in the ordinary-matter integrand.

No complete STI closure, loop integration, UV–EFT subtraction, transverse form factor, or Wilson coefficient is claimed.
