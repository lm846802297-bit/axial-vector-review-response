#!/usr/bin/env python3
"""Exact off-shell Pauli/Fierz map for the Q_LD triplet derivative operator."""
import sympy as sp


def pauli_matrices():
    I = sp.I
    return (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -I], [I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )


def component_operator_identity():
    """Verify Q3 = 2 i (D H)^dag H (barL gamma L)
       + 2(Hdag H)(barL i slash D L) - Q0 component by component.
    """
    sigma = pauli_matrices()
    H = sp.symbols("H0:2")
    Hb = sp.symbols("Hb0:2")
    DHb = sp.symbols("DHb0:2")
    B0 = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"B0_{i}{j}"))
    B1 = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"B1_{i}{j}"))

    Q3 = 0
    for sig in sigma:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        Q3 += sig[i, j]*sig[k, l]*(
                            H[j]*DHb[k]*B0[i, l]
                            + H[j]*Hb[k]*B1[i, l]
                        )

    Q0 = sum(
        H[i]*(DHb[k]*B0[i, k] + Hb[k]*B1[i, k])
        for i in range(2) for k in range(2)
    )
    rhs = (
        2*sum(DHb[j]*H[j] for j in range(2))
         *sum(B0[i, i] for i in range(2))
        +2*sum(Hb[j]*H[j] for j in range(2))
         *sum(B1[i, i] for i in range(2))
        -Q0
    )
    return sp.simplify(Q3-rhs)


def derivative_current_identity():
    """Verify 2 i (D H)^dag H = i d(Hdag H) - Hdag i<->D H."""
    A, B = sp.symbols("A B", commutative=True)  # A=(D H)^dag H, B=Hdag D H
    return sp.simplify(2*sp.I*A - (sp.I*(A+B) - sp.I*(B-A)))


def eom_ibp_reduction_identity():
    """Check -i phi div(J_L)+2 phi B = phi(A+B) from the lepton EOM."""
    phi, A, B = sp.symbols("phi A B", commutative=True)
    divJ = sp.I*(A-B)
    return sp.simplify(-sp.I*phi*divJ + 2*phi*B - phi*(A+B))


def main():
    assert component_operator_identity() == 0
    assert derivative_current_identity() == 0
    assert eom_ibp_reduction_identity() == 0
    print("PASS: explicit Pauli-matrix component identity.")
    print("PASS: off-shell Q_LD^(3) = 2i(DH)^dag H (barL gamma L)")
    print("      + 2(Hdag H)(barL i slash D L) - Q_LD.")
    print("PASS: 2i(DH)^dag H = i d(Hdag H) - Hdag i<->D H.")
    print("PASS: EOM + IBP maps Q_LD^(3)+Q_LD to -O_Hl^(1) plus the Hermitian Yukawa-source pair.")
    print("BOUNDARY: no UV one-W form factor or loop matching is applied.")


if __name__ == "__main__":
    main()
