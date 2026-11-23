#!/usr/bin/env python3
"""Exact chiral-flavor basis-invariance audit for RC-001 loop traces.

Uses exact rational parametrizations of the orthogonal U_L/U_R rotations and
four generic 2x2 flavor blocks. For each of the 16 left/right chirality-flow
patterns, it verifies that the cyclic trace of transformed blocks
U_{a_i}^T X_i U_{a_{i+1}} equals Tr[X_1 X_2 X_3 X_4]. This is the algebraic
basis-invariance identity underlying the complete internal mass-eigenstate sum.
It is not a loop integral, does not identify physical diagram multiplicities,
and does not replace the dimensionally regulated UV-EFT subtraction.
Requires Python 3 + SymPy.
"""
from itertools import product
import sympy as sp

checks=[]
def check(name,expr,expected=0):
    residual=sp.cancel(sp.together(sp.simplify(expr-expected)))
    if isinstance(residual, sp.MatrixBase):
        is_zero = residual == sp.zeros(*residual.shape)
    else:
        is_zero = residual == 0
    if not is_zero: raise AssertionError(f"{name}: residual={residual}")
    checks.append(name); print(f"PASS: {name}")

tL,tR=sp.symbols("t_L t_R", real=True)
def rotation(t):
    den=1+t**2
    c=(1-t**2)/den
    s=2*t/den
    return sp.Matrix([[c,s],[-s,c]])
UL=rotation(tL); UR=rotation(tR)
U={"L":UL,"R":UR}
check("U_L is exactly orthogonal under rational angle parametrization",UL.T*UL,sp.eye(2))
check("U_R is exactly orthogonal under rational angle parametrization",UR.T*UR,sp.eye(2))

X=[]
for n in range(1,5):
    entries=sp.symbols(f"x{n}11 x{n}12 x{n}21 x{n}22")
    X.append(sp.Matrix([[entries[0],entries[1]],[entries[2],entries[3]]]))
base_trace=sp.trace(X[0]*X[1]*X[2]*X[3])
flows=list(product(("L","R"),repeat=4))
for idx,flow in enumerate(flows,1):
    transformed=[]
    for i in range(4):
        left=U[flow[i]]
        right=U[flow[(i+1)%4]]
        transformed.append(left.T*X[i]*right)
    transformed_trace=sp.trace(transformed[0]*transformed[1]*transformed[2]*transformed[3])
    check(f"cyclic trace basis invariance for chirality flow {''.join(flow)}",transformed_trace,base_trace)

# Check the actual model vertices in signed and positive-light-mass conventions.
a,b=sp.symbols("a b", real=True)
Yh0=a*sp.Matrix([[0,1],[0,0]])
Ys0=b*sp.Matrix([[0,0],[1,0]])
D=sp.diag(-1,1)
cL,sL=UL[0,0],UL[0,1]
cR,sR=UR[0,0],UR[0,1]
Yh_eq13=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys_eq13=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
Gh=UL.T*Yh0*UR
Gs=UL.T*Ys0*UR
Gh276=sp.Matrix([[-a*cL*sR,a*cL*cR],[-a*sL*sR,a*sL*cR]])
Gs276=sp.Matrix([[-b*sL*cR,-b*sL*sR],[b*cL*cR,b*cL*sR]])
check("signed-light h vertex matches source §276",Gh,Gh276)
check("signed-light s vertex matches source §276",Gs,Gs276)
check("positive-light h vertex after D rephasing matches Eq.(13)",Gh*D,Yh_eq13)
check("positive-light s vertex after D rephasing matches Eq.(13)",Gs*D,Ys_eq13)

print(f"RESULT: {len(checks)} exact symbolic chiral-flavor basis-invariance checks passed.")
print("INTERPRETATION: with complete chiral blocks and all internal mass indices summed, each fixed ordered-loop trace is basis invariant; omitted chiral blocks or incomplete path sums would break this identity.")
print("LIMIT: this is an algebraic trace-covariance identity, not an explicit evaluation of the six-cycle momentum integrals, common i/symmetry factors, or UV-EFT finite matching.")
