#!/usr/bin/env python3
"""RC-001 fixed-sector hard/soft pole ledger.

Separately tracks the hard-region IR pole, EFT soft-loop UV pole, the local EFT
counterterm, and the finite remainder for the source-recorded §248 four-scalar
Yukawa sector. It also checks the existing §39 two-point bubble/contact pole
cancellation at the algebraic level.

This is a fixed-sector bookkeeping audit, not the complete four-scalar EFT
diagram census or final Wilson-coefficient matching.
Requires Python 3 and SymPy.
"""
import sympy as sp

checks=[]
def check(name,expr,expected=0):
    residual=sp.simplify(expr-expected)
    if residual != 0:
        raise AssertionError(f"{name}: residual={residual}")
    checks.append(name)
    print(f"PASS: {name}")

s,t,L,ell=sp.symbols("s t L ell", real=True)
DeltaIR,DeltaUV=sp.symbols("Delta_IR Delta_UV")
# Source §248 hard region and bare EFT soft bubble, with common |C5|^2/(16 pi^2) factored out.
hard=(-DeltaIR+L-2)*s+t/sp.Integer(6)
soft=(DeltaUV-ell+2)*s
soft_ct=-DeltaUV*s

check("hard-region IR pole residue is -s",sp.diff(hard,DeltaIR),-s)
check("bare EFT soft-loop UV pole residue is +s",sp.diff(soft,DeltaUV),s)
check("local EFT counterterm cancels the soft UV pole",sp.diff(soft+soft_ct,DeltaUV),0)
check("renormalized soft term retains the nonlocal logarithm and finite constant",
      soft+soft_ct,(-ell+2)*s)
regions=hard+soft
check("hard-plus-soft region sum retains separately labeled pole difference",
      regions,(DeltaUV-DeltaIR+L-ell)*s+t/sp.Integer(6))
check("identifying region IR/UV poles cancels the pole in the full region sum",
      regions.subs(DeltaIR,DeltaUV),(L-ell)*s+t/sp.Integer(6))
check("finite local hard polynomial has the source-recorded coefficients",
      hard.subs(DeltaIR,0),(L-2)*s+t/sp.Integer(6))
check("finite local t coefficient is 1/6",sp.diff(hard.subs(DeltaIR,0),t),sp.Rational(1,6))
check("finite local s coefficient is L-2",sp.diff(hard.subs(DeltaIR,0),s),L-2)

# Independent two-point EFT bubble/contact counterterm identities already present in RC-001 §39.
q,x=sp.symbols("q x", real=True)
p2=sp.symbols("p2", real=True)
epsUV=sp.symbols("Delta_UV_2pt")
eft_bubble_contact=-q*(8*x-p2)*epsUV
local_inverse_ct=+q*(8*x-p2)*epsUV
check("two-point EFT bubble/contact UV pole cancels its local inverse-kernel counterterm",
      eft_bubble_contact+local_inverse_ct,0)
contact_tadpole=2*q*sp.symbols("A0")
check("contact tadpole has zero external-momentum derivative",
      sp.diff(contact_tadpole,p2),0)
Mstar2,vh,vs=sp.symbols("Mstar2 v_h v_s", nonzero=True)
delta_c=-Mstar2*q*epsUV/(16*sp.pi**2*vh*vs)
check("two-point dimension-six derivative counterterm cancels the p2 pole",
      delta_c*vh*vs/Mstar2*p2+q*p2*epsUV/(16*sp.pi**2),0)

print(f"RESULT: {len(checks)} exact symbolic pole/counterterm checks passed.")
print("SCOPE: fixed §248 four-scalar hard/soft sector plus existing §39 two-point pole identities.")
print("OPEN: this does not enumerate/evaluate every same-order EFT soft graph, integrate the six-cycle UV kernels, or establish the final finite Wilson vector.")
