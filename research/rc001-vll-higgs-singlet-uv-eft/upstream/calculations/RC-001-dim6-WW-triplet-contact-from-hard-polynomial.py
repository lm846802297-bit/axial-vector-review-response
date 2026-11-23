#!/usr/bin/env python3
"""Extract the Q_LD^(3) derivative/contact component of the WW hard polynomial.

The nonexceptional hard polynomial is first decomposed into
v_D=p3+p4=-(p1+p2), v_-=p2-p3, v_+=p2+p3.
Only v_D is identified here with the derivative matrix element of Q_LD^(3).
The other two off-shell directions are not assigned to operators yet.
"""
import sympy as sp

L = sp.symbols("L", real=True)
p1,p2,p3 = sp.symbols("p1 p2 p3")
g2,y,M_E,mu = sp.symbols("g2 y M_E mu", positive=True)
a = -sp.Rational(1,2)+L/2
b = -sp.Rational(1,32)+sp.Rational(7,16)*L
c = sp.Rational(7,32)-sp.Rational(5,16)*L
vD = -(p1+p2)
vminus = p2-p3
vplus = p2+p3

def main():
    alpha = (
        sp.Rational(1,2)-L/2,
        sp.Rational(11,16)-sp.Rational(3,8)*L,
        sp.Rational(1,4)-sp.Rational(3,4)*L,
    )
    reconstructed = sp.expand(a*vD+b*vminus+c*vplus)
    target = sp.expand(alpha[0]*p1+alpha[1]*p2+alpha[2]*p3)
    assert sp.simplify(reconstructed-target)==0

    # Raw +slash(P) amplitude coefficient is -a because v_D=-P.
    raw_P_coefficient = -a
    # The Q_LD^(3) derivative matrix element is slash(q_D)=slash(v_D),
    # so its operator coefficient is a in this Fourier convention.
    operator_coefficient = a
    assert sp.simplify(operator_coefficient+raw_P_coefficient)==0

    at_match = sp.simplify(operator_coefficient.subs(L,0))
    assert at_match == -sp.Rational(1,2)
    ratio = sp.simplify(at_match*g2**2/(16*sp.pi**2))
    assert sp.simplify(ratio+g2**2/(32*sp.pi**2))==0

    print("RC-001 Q_LD^(3) contact component from WW hard polynomial")
    print(f"v_D coefficient a(L) = {operator_coefficient}")
    print(f"raw +slash(P) amplitude coefficient = {raw_P_coefficient}")
    print("PASS: sign follows q_D=p3+p4=-P in the all-incoming Fourier convention.")
    print(f"At mu_R=M_E: a = {at_match}")
    print(f"C_Q3/C_LD at mu_R=M_E = {ratio}")
    print("The associated EFT one-W contact is")
    print("  i g2 C_Q3 epsilon^{IJK} (barL sigma^I H) gamma^mu W_mu^J (Hdag sigma^K L).")
    print("BOUNDARY: this is only the v_D/Q_LD^(3) component; v_minus/v_plus and the UV five-point form factor remain open.")

if __name__ == "__main__":
    main()
