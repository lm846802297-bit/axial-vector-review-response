#!/usr/bin/env python3
"""Exact mass-basis vertex and light-state rephasing audit for RC-001.

Checks that the Eq.(13) positive-light-mass Yukawa matrices follow from the
interaction-basis Yukawa matrices by the stated left/right rotations and the
right-handed light-state rephasing D=diag(-1,1). Also checks reconstruction of
the original triangular mass matrix in the signed-light-mass convention.
This is a basis/convention audit, not a loop-integral or UV-EFT matching result.
Requires Python 3 + SymPy.
"""
import sympy as sp

checks=[]
def check(name,expr,expected=None):
    residual=expr if expected is None else expr-expected
    residual=sp.simplify(residual)
    if isinstance(residual, sp.MatrixBase):
        is_zero = residual == sp.zeros(*residual.shape)
    else:
        is_zero = residual == 0
    if not is_zero:
        raise AssertionError(f"{name}: residual={residual}")
    checks.append(name)
    print(f"PASS: {name}")

cL,sL,cR,sR,a,b,m1,m2=sp.symbols("c_L s_L c_R s_R a b m_1 m_2", real=True)
UL=sp.Matrix([[cL,sL],[-sL,cL]])
UR=sp.Matrix([[cR,sR],[-sR,cR]])
D=sp.diag(-1,1)
Yh0=a*sp.Matrix([[0,1],[0,0]])
Ys0=b*sp.Matrix([[0,0],[1,0]])
Yh_eq13=a*sp.Matrix([[cL*sR,cL*cR],[sL*sR,sL*cR]])
Ys_eq13=b*sp.Matrix([[sL*cR,-sL*sR],[-cL*cR,cL*sR]])
Gh_section276=sp.Matrix([[-a*cL*sR,a*cL*cR],[-a*sL*sR,a*sL*cR]])
Gs_section276=sp.Matrix([[-b*sL*cR,-b*sL*sR],[b*cL*cR,b*cL*sR]])
check("left rotation obeys UL^T UL=(cL^2+sL^2) I",UL.T*UL,(cL**2+sL**2)*sp.eye(2))
check("right rotation obeys UR^T UR=(cR^2+sR^2) I",UR.T*UR,(cR**2+sR**2)*sp.eye(2))
Gh=sp.simplify(UL.T*Yh0*UR)
Gs=sp.simplify(UL.T*Ys0*UR)
check("signed-light h vertex equals the source §276 matrix",Gh,Gh_section276)
check("signed-light s vertex equals the source §276 matrix",Gs,Gs_section276)
check("positive-light h vertex is Gh times D and reproduces Eq.(13)",Gh*D,Yh_eq13)
check("positive-light s vertex is Gs times D and reproduces Eq.(13)",Gs*D,Ys_eq13)

# Reconstruct the triangular interaction-basis mass matrix from signed masses.
Msigned=UL*sp.diag(-m1,m2)*UR.T
mL=cL*m1*sR+cR*m2*sL
mR=cL*m2*sR+cR*m1*sL
ME=cL*cR*m2-m1*sL*sR
Mtri=sp.Matrix([[0,mL],[mR,ME]])
check("mass-matrix reconstruction has the expected M12=mL",Msigned[0,1],mL)
check("mass-matrix reconstruction has the expected M21=mR",Msigned[1,0],mR)
check("mass-matrix reconstruction has the expected heavy entry ME",Msigned[1,1],ME)
check("mass-matrix reconstruction's M11 is the exact zero-entry constraint",Msigned[0,0],-cL*cR*m1+m2*sL*sR)
# The last relation follows after applying the M11=0 constraint; record it without
# dividing by a mixing angle or assuming a small-angle expansion.
constraint=-cL*cR*m1+m2*sL*sR
check("determinant identity reduces to the M11=0 constraint for normalized rotations",sp.factor(mL*mR-m1*m2-constraint*(cL*cR*m2-m1*sL*sR)),m1*m2*((cL**2+sL**2)*(cR**2+sR**2)-1))

print(f"RESULT: {len(checks)} exact symbolic mass-basis/rephasing checks passed.")
print("CONVENTION: signed mass matrix diag(-m1,m2); positive-mass convention uses right-handed D=diag(-1,1).")
print("SCOPE: confirms vertex/mass-basis conventions only; does not prove loop multiplicities, Wick signs, massless-region subtraction, or Wilson coefficients.")
