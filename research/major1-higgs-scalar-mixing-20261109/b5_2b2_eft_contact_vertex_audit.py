#!/usr/bin/env python3
"""B5-2B2: exact charge and covariant-derivative contact-vertex audit."""
import sympy as sp

gY, g2, gX, Q = sp.symbols("gY g2 gX Q", real=True)
eta = sp.symbols("eta", real=True)
I = sp.I


def composite_charges(eta_value):
    """Return (Y, X, SU2 representation) for the differentiated composites."""
    if eta_value not in (+1, -1):
        raise ValueError("eta must be +1 (mu) or -1 (tau)")
    # H^dagger L and S_l l_R, using Y_H=+1/2, X(S_l)=2 eta Q.
    psiL = (sp.Rational(-1, 2) + sp.Rational(-1, 2), eta_value*Q, "singlet")
    psiR = (0 - 1, 2*eta_value*Q - eta_value*Q, "singlet")
    assert sp.simplify(psiL[0] + 1) == 0
    assert sp.simplify(psiL[1] - eta_value*Q) == 0
    assert sp.simplify(psiR[0] + 1) == 0
    assert sp.simplify(psiR[1] - eta_value*Q) == 0
    return psiL, psiR


def eft_contact_coefficients(eta_value):
    """Coefficients in i D_mu = i partial_mu + g q A_mu."""
    psiL, psiR = composite_charges(eta_value)
    def coeffs(q):
        return {
            "B": sp.simplify(gY*q[0]),
            "A_prime": sp.simplify(gX*q[1]),
            "W": sp.Integer(0) if q[2] == "singlet" else None,
        }
    cL, cR = coeffs(psiL), coeffs(psiR)
    assert cL == cR
    assert sp.simplify(cL["B"] + gY) == 0
    assert sp.simplify(cL["A_prime"] - eta_value*Q*gX) == 0
    assert cL["W"] == 0
    return cL


def weak_singlet_covariant_derivative_check():
    """Verify cancellation of W^I in D_mu(H^dagger L)."""
    h1, h2, l1, l2 = sp.symbols("h1 h2 l1 l2", commutative=True)
    tau1 = sp.Matrix([[0, 1], [1, 0]])/2
    tau2 = sp.Matrix([[0, -I], [I, 0]])/2
    tau3 = sp.Matrix([[1, 0], [0, -1]])/2
    Hbar = sp.Matrix([[h1, h2]])
    L = sp.Matrix([l1, l2])
    # D H^dagger has + i g H^dagger tau^I W^I; D L has - i g tau^I W^I L.
    W1, W2, W3 = sp.symbols("W1 W2 W3", commutative=True)
    W = (W1, W2, W3)
    left = sum((I*g2*Hbar*tau[a]*W[a] for a in range(3)), sp.zeros(1, 2))*L
    right = Hbar*sum((-I*g2*tau[a]*L*W[a] for a in range(3)), sp.zeros(2, 1))
    assert sp.simplify((left+right)[0]) == 0
    return True


def main():
    print("B5-2B2 EFT covariant-derivative contact audit")
    for name, eta_value in (("mu", +1), ("tau", -1)):
        psiL, psiR = composite_charges(eta_value)
        coeff = eft_contact_coefficients(eta_value)
        print(f"{name}: Psi_L charges (Y,X,SU2)={psiL}; Psi_R={psiR}")
        print(f"{name}: contact coefficients B={coeff['B']}, A'={coeff['A_prime']}, W={coeff['W']}")
    weak_singlet_covariant_derivative_check()
    print("PASS: H^dagger L and S_l l_R have identical (Y,X)=(-1,eta_l Q_l) composite charges.")
    print("PASS: EFT derivative contact terms are -gY B_mu J_comp^mu + eta_l Q_l gX A'_mu J_comp^mu.")
    print("PASS: direct W contact cancels in D_mu(H^dagger L); Q_RD is an SU(2) singlet.")
    print("LIMIT: this is the EFT contact-vertex sub-block only, not a loop integral or Ward-identity closure.")


if __name__ == "__main__":
    main()
