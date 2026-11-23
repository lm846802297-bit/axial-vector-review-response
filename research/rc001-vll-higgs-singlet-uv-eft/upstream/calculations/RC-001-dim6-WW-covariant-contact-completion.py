#!/usr/bin/env python3
"""Gauge-covariant completion of the nonexceptional WW hard polynomial.

The three off-shell momentum directions are represented by:
  Q_D^(3): derivative on the adjoint composite Hdag sigma^I L;
  O_-^(3): i times the antisymmetric Higgs derivative bilinear;
  O_+^(3): i times the symmetric Higgs derivative bilinear.

This is a redundant off-shell gauge-covariant basis. O_+ is retained as a
form-factor/source direction; its Hermitian completion and EOM/IBP reduction
are not performed here. The script computes the local EFT one-W contacts
implied by these representatives. It does not calculate the UV five-point
amplitude.
"""
import sympy as sp

I = sp.I
g2,L = sp.symbols("g2 L", real=True)
p1,p2,p3 = sp.symbols("p1 p2 p3")
a = -sp.Rational(1,2)+L/2
b = -sp.Rational(1,32)+sp.Rational(7,16)*L
c = sp.Rational(7,32)-sp.Rational(5,16)*L

sigma = (
    sp.Matrix([[0,1],[1,0]]),
    sp.Matrix([[0,-I],[I,0]]),
    sp.Matrix([[1,0],[0,-1]]),
)
T = [s/2 for s in sigma]
delta = sp.eye(2)


def verify_momentum_decomposition():
    vD = -(p1+p2)
    vminus = p2-p3
    vplus = p2+p3
    target = (
        (sp.Rational(1,2)-L/2)*p1
        +(sp.Rational(11,16)-sp.Rational(3,8)*L)*p2
        +(sp.Rational(1,4)-sp.Rational(3,4)*L)*p3
    )
    return sp.simplify(a*vD+b*vminus+c*vplus-target)


def verify_pauli_contact_tensor():
    # T3_(ij,kl) = sum_A sigma^A_(ij) sigma^A_(kl).
    # Contract the H_j index with the fundamental generator T^I=sigma^I/2.
    for Iidx in range(3):
        for i in range(2):
            for l in range(2):
                for k in range(2):
                    for m in range(2):
                        lhs = sum(
                            sigma[A][i,j]*sigma[A][k,l]*T[Iidx][j,m]
                            for A in range(3) for j in range(2)
                        )
                        rhs = (
                            delta[i,l]*sigma[Iidx][k,m]
                            -sp.Rational(1,2)*sigma[Iidx][i,m]*delta[k,l]
                        )
                        assert sp.simplify(lhs-rhs)==0


def contact_coefficients():
    # Q_D^(3): D_adj Y^I = partial Y^I + g2 eps^{IJK} W^J Y^K.
    qd_contact = I*g2*a
    # O_-^(3): i[Hdag D H - (D Hdag)H] -> +2 g2 Hdag T^I H W^I.
    minus_contact = 2*g2*b
    # O_+^(3): i[Hdag D H + (D Hdag)H] has cancelling gauge connections.
    plus_contact = sp.Integer(0)
    return qd_contact, minus_contact, plus_contact


def main():
    assert verify_momentum_decomposition()==0
    verify_pauli_contact_tensor()
    qd,minus,plus = contact_coefficients()
    assert sp.simplify(plus)==0
    at_match = {
        "Q_D": sp.simplify(qd.subs(L,0)),
        "O_minus": sp.simplify(minus.subs(L,0)),
        "O_plus": sp.simplify(plus),
    }
    assert at_match["Q_D"] == -I*g2/2
    assert at_match["O_minus"] == -g2/16
    print("RC-001 gauge-covariant local one-W contact completion")
    print("PASS: hard polynomial = a v_D + b v_minus + c v_plus.")
    print("PASS: Pauli tensor contraction T3_(ij,kl) (sigma^I/2)_(jm)")
    print("      = delta_il sigma^I_(km) - 1/2 sigma^I_(im) delta_kl.")
    print(f"Q_D^(3) adjoint contact coefficient: {qd}")
    print(f"O_minus^(3) Higgs-current contact coefficient: {minus}")
    print(f"O_plus^(3) direct W contact coefficient: {plus}")
    print("At mu_R=M_E:")
    print(f"  Q_D^(3): {at_match['Q_D']}")
    print(f"  O_minus^(3): {at_match['O_minus']}")
    print("The common overall factor g2^2 |y_l|^2/(16 pi^2 M_E^2) is understood.")
    print("BOUNDARY: EFT local contact only; UV five-point form factor, Hermitian completion, EOM/IBP reduction and full Ward sum remain open.")

if __name__ == "__main__":
    main()
