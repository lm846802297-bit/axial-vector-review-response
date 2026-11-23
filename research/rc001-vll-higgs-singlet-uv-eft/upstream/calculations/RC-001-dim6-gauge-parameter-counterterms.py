#!/usr/bin/env python3
"""Exact-rational audit of the diagonal-gauge parameter-counterterm sub-block.

This checks only the arithmetic of the standard one-loop MS pole formulas
recorded in research/RC-001-dim6-gauge-parameter-counterterms.md. It does not
compute loop integrals, finite hard matching, mixed kinetic-mixing terms, or
the EFT operator counterterm matrix.
"""
from fractions import Fraction as F

def yukawa_pole(*charge_squares):
    """Coefficient of g^2/(16*pi^2*epsilon): -3/2 sum of fermion charge squares."""
    return -F(3, 2) * sum(charge_squares, F(0))

def mass_pole(charge_square):
    """Coefficient of g^2/(16*pi^2*epsilon): -3 times heavy-fermion charge square."""
    return -3 * charge_square

def fmt(value):
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"

def main():
    # Q_LD: Y_L^2=1/4, Y_E^2=1; C2(L)=3/4, C2(E)=0;
    # X_L^2=X_E^2=Q_l^2.
    y_ld = {
        "gY^2": yukawa_pole(F(1, 4), F(1)),
        "g2^2": yukawa_pole(F(3, 4), F(0)),
        "gX^2 Q_l^2": yukawa_pole(F(1), F(1)),
    }
    m_e = {
        "gY^2": mass_pole(F(1)),
        "g2^2": mass_pole(F(0)),
        "gX^2 Q_l^2": mass_pole(F(1)),
    }
    c_ld = {g: 2 * y_ld[g] - 2 * m_e[g] for g in y_ld}

    # Q_RD: E and l_R have Y^2=1; X^2=Q_l^2 for both; both are SU(2) singlets.
    lam_rd = {
        "gY^2": yukawa_pole(F(1), F(1)),
        "g2^2": yukawa_pole(F(0), F(0)),
        "gX^2 Q_l^2": yukawa_pole(F(1), F(1)),
    }
    c_rd = {g: 2 * lam_rd[g] - 2 * m_e[g] for g in lam_rd}

    expected_y_ld = {"gY^2": F(-15, 8), "g2^2": F(-9, 8), "gX^2 Q_l^2": F(-3)}
    expected_m_e = {"gY^2": F(-3), "g2^2": F(0), "gX^2 Q_l^2": F(-3)}
    expected_c_ld = {"gY^2": F(9, 4), "g2^2": F(-9, 4), "gX^2 Q_l^2": F(0)}
    expected_lam_rd = {"gY^2": F(-3), "g2^2": F(0), "gX^2 Q_l^2": F(-3)}
    expected_c_rd = {"gY^2": F(0), "g2^2": F(0), "gX^2 Q_l^2": F(0)}
    assert y_ld == expected_y_ld
    assert m_e == expected_m_e
    assert c_ld == expected_c_ld
    assert lam_rd == expected_lam_rd
    assert c_rd == expected_c_rd

    for name, values in (
        ("delta y_LD/y_LD", y_ld),
        ("delta M_E/M_E", m_e),
        ("2 delta y/y - 2 delta M/M for C_LD", c_ld),
        ("delta lambda_RD/lambda_RD", lam_rd),
        ("2 delta lambda/lambda - 2 delta M/M for C_RD", c_rd),
    ):
        print(name + ": " + ", ".join(f"{g}={fmt(v)}" for g, v in values.items()))
    print("RESULT: exact-rational parameter-counterterm algebra PASS.")
    print("SCOPE: no loop integrals, mixed B-A' terms, EFT operator counterterms, or finite Wilson coefficients.")

if __name__ == "__main__":
    main()
