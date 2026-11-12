#!/usr/bin/env python3
"""B5-2B4: Pauli-triplet derivative operator EOM/current-basis audit."""
import sympy as sp

I = sp.I
g2 = sp.symbols("g2", real=True)
C_LD = sp.symbols("C_LD", real=True)
DeltaUV, L = sp.symbols("DeltaUV L", real=True)
eps3 = sp.LeviCivita

SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(s/2 for s in SIGMA)


def triplet_derivative_eom_identity():
    """Check Q_LD^(3) = -O_HL^(1)+E_L^(1)-Q_LD mod total derivative."""
    h = sp.symbols("h0:2", commutative=True)
    hb = sp.symbols("hb0:2", commutative=True)
    dh = sp.symbols("dh0:2", commutative=True)
    dhb = sp.symbols("dhb0:2", commutative=True)

    # Abstract Lorentz bilinears:
    # J_ad = bar L_a gamma L_d
    # JD_ad = bar L_a gamma D L_d
    # JDb_ad = (D bar L)_a gamma L_d
    J = sp.Matrix(2, 2, lambda a, d: sp.Symbol(f"J{a}{d}", commutative=True))
    JD = sp.Matrix(2, 2, lambda a, d: sp.Symbol(f"JD{a}{d}", commutative=True))
    JDb = sp.Matrix(2, 2, lambda a, d: sp.Symbol(f"JDb{a}{d}", commutative=True))

    # Symmetrized triplet derivative bilinear:
    # i/2 [ (bar L sigma^I H) gamma D_adj(H^dagger sigma^I L)
    #      - D_adj(bar L sigma^I H) gamma (H^dagger sigma^I L) ].
    Q3 = sp.Integer(0)
    for sigma in SIGMA:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        Q3 += I*sp.Rational(1, 2)*sigma[a, b]*sigma[c, d]*(
                            h[b]*dhb[c]*J[a, d]
                            + h[b]*hb[c]*JD[a, d]
                            - h[b]*hb[c]*JDb[a, d]
                            - dh[b]*hb[c]*J[a, d]
                        )

    JH1 = I*sum(hb[a]*dh[a]-dhb[a]*h[a] for a in range(2))
    JL1 = sum(J[a, a] for a in range(2))
    O_HL1 = sp.expand(JH1*JL1)
    E_L1 = sp.expand(
        sum(hb[a]*h[a] for a in range(2))
        * I*sum(JD[a, a]-JDb[a, a] for a in range(2))
    )
    Q_LD = sp.expand(
        I*sum(
            h[a]*(dhb[c]*J[a, c]+hb[c]*JD[a, c])
            for a in range(2) for c in range(2)
        )
    )

    # Total derivative of (bar L H) gamma^mu (H^dagger L).
    total_derivative = sp.expand(sum(
        dh[a]*hb[c]*J[a, c]
        + h[a]*dhb[c]*J[a, c]
        + h[a]*hb[c]*JD[a, c]
        + h[a]*hb[c]*JDb[a, c]
        for a in range(2) for c in range(2)
    ))

    residual = sp.simplify(
        sp.expand(Q3 - (-O_HL1 + E_L1 - Q_LD) - I*total_derivative/2)
    )
    assert residual == 0
    return True


def current_basis_projection():
    """Substitute the already-fixed Q_LD EOM map into the triplet identity."""
    O1, O3, E1, E3 = sp.symbols("O_HL1 O_HL3 E_L1 E_L3")
    QLD_eom = -sp.Rational(1,4)*O1 - sp.Rational(1,4)*O3 \
              + sp.Rational(1,4)*E1 + sp.Rational(1,4)*E3
    Q3_eom = sp.expand(-O1 + E1 - QLD_eom)
    expected = (
        -sp.Rational(3,4)*O1 + sp.Rational(1,4)*O3
        + sp.Rational(3,4)*E1 - sp.Rational(1,4)*E3
    )
    assert sp.simplify(Q3_eom-expected) == 0
    return Q3_eom


def adjoint_covariant_derivative_check():
    """Check both adjoint composites and their common covariant-derivative sign."""
    W = sp.symbols("W0:3", commutative=True)
    h = sp.Matrix(sp.symbols("h0:2", commutative=True))
    hb = sp.Matrix([[*sp.symbols("hb0:2", commutative=True)]])
    L = sp.Matrix(sp.symbols("l0:2", commutative=True))
    barL = sp.Matrix([[*sp.symbols("barl0:2", commutative=True)]])

    for a in range(3):
        for Jidx in range(3):
            comm = T[a]*SIGMA[Jidx] - SIGMA[Jidx]*T[a]
            expected = I*sum(
                (eps3(a, Jidx, K)*SIGMA[K] for K in range(3)),
                sp.zeros(2, 2)
            )
            assert all(sp.simplify(x) == 0 for x in comm-expected)

            # C^I = H^dagger sigma^I L:
            # D_mu C^I = partial_mu C^I - g2 eps^{a I J} W_mu^a C^J.
            gauge_C = I*g2*W[a]*(hb*(T[a]*SIGMA[Jidx]-SIGMA[Jidx]*T[a])*L)[0]
            expected_C = -g2*sum(
                eps3(a, Jidx, K)*W[a]*(hb*SIGMA[K]*L)[0]
                for K in range(3)
            )
            assert sp.simplify(gauge_C-expected_C) == 0

            # Cbar^I = bar L sigma^I H transforms in the same real adjoint.
            gauge_Cbar = I*g2*W[a]*(barL*(T[a]*SIGMA[Jidx]-SIGMA[Jidx]*T[a])*h)[0]
            expected_Cbar = -g2*sum(
                eps3(a, Jidx, K)*W[a]*(barL*SIGMA[K]*h)[0]
                for K in range(3)
            )
            assert sp.simplify(gauge_Cbar-expected_Cbar) == 0
    return True


def triplet_adjoint_contact_check():
    """Verify the symmetrized triplet derivative contact and its EOM-current form."""
    W = sp.symbols("W0:3", commutative=True)
    B = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"B{i}{j}", commutative=True))
    C = sp.symbols("C0:3", commutative=True)
    Cbar = sp.symbols("Cbar0:3", commutative=True)

    # The two conjugate composites transform in the same real adjoint:
    # D C^I = partial C^I - g eps W C^J,
    # D Cbar^I = partial Cbar^I - g eps W Cbar^J.
    # Therefore the symmetrized derivative has a nonzero contact term.
    sym_contact = sp.Integer(0)
    for a in range(3):
        for Iidx in range(3):
            for Jidx in range(3):
                sym_contact += I*sp.Rational(1,2)*W[a]*eps3(a,Iidx,Jidx)*(
                    -g2*B[Iidx,Jidx] + g2*B[Jidx,Iidx]
                )
    expected_contact = -I*g2*sum(
        W[a]*eps3(a,Iidx,Jidx)*B[Iidx,Jidx]
        for a in range(3) for Iidx in range(3) for Jidx in range(3)
    )
    assert sp.simplify(sym_contact-expected_contact) == 0

    # Exact Pauli identity for the contact in
    # Q_LD^(3) = -O_HL^(1) + E_L^(1) - Q_LD:
    # -i eps^{aIJ} sigma^I_{ij} sigma^J_{kl}
    # = delta_{jk} sigma^a_{il} - sigma^a_{kj} delta_{il}.
    for a in range(3):
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        lhs = -I*sum(
                            eps3(a,Iidx,Jidx)
                            *SIGMA[Iidx][i,j]*SIGMA[Jidx][k,l]
                            for Iidx in range(3) for Jidx in range(3)
                        )
                        rhs = (
                            (1 if j == k else 0)*SIGMA[a][i,l]
                            - SIGMA[a][k,j]*(1 if i == l else 0)
                        )
                        assert sp.simplify(lhs-rhs) == 0
    return True

def box_to_current_coefficients():
    """Map the raw WW T3 box coefficient through the triplet EOM identity."""
    # Exact-routing B5-2B3R coefficient, before the full EFT counterterm sum.
    base = g2**2*C_LD/(16*sp.pi**2)
    C3 = (
        sp.Rational(3,8)*DeltaUV
        -sp.Rational(3,8)*L
        +sp.Rational(11,16)
    )*base
    delta_C_HL1 = -sp.Rational(3,4)*C3
    delta_C_HL3 = +sp.Rational(1,4)*C3
    delta_E1 = +sp.Rational(3,4)*C3
    delta_E3 = -sp.Rational(1,4)*C3

    expected_HL1 = -(
        sp.Rational(9,32)*DeltaUV-sp.Rational(9,32)*L+sp.Rational(33,64)
    )*base
    expected_HL3 = (
        sp.Rational(3,32)*DeltaUV-sp.Rational(3,32)*L+sp.Rational(11,64)
    )*base
    assert sp.simplify(delta_C_HL1-expected_HL1) == 0
    assert sp.simplify(delta_C_HL3-expected_HL3) == 0
    assert sp.simplify(delta_E1+expected_HL1) == 0
    assert sp.simplify(delta_E3+expected_HL3) == 0
    return {
        "C3": C3,
        "delta_C_HL1": delta_C_HL1,
        "delta_C_HL3": delta_C_HL3,
        "delta_E1": delta_E1,
        "delta_E3": delta_E3,
    }


def main():
    triplet_derivative_eom_identity()
    current_basis_projection()
    adjoint_covariant_derivative_check()
    triplet_adjoint_contact_check()
    coeffs = box_to_current_coefficients()

    print("B5-2B4 Pauli-triplet derivative EOM/current audit")
    print("PASS: Q_LD^(3) = -O_HL^(1) + E_L^(1) - Q_LD modulo total derivative.")
    print("PASS: substituting the Q_LD EOM map gives the common Pauli-current basis.")
    print("PASS: both H^dagger sigma^I L and bar L sigma^I H transform in the same real adjoint.")
    print("PASS: symmetrized Q_LD^(3) has the nonzero -i g2 eps^{aIJ} W^a bar C^I gamma C^J contact.")
    print("PASS: the triplet contact equals the gauge-field part of -O_HL^(1)+E_L^(1)-Q_LD.")
    print("Exact-routing box coefficient C3 = (3 Delta_UV/8 - 3 L/8 + 11/16) g2^2 C_LD/(16 pi^2)")
    print("delta C_HL^(1) = (-9 Delta_UV/32 + 9 L/32 - 33/64) g2^2 C_LD/(16 pi^2)")
    print("delta C_HL^(3) = (+3 Delta_UV/32 - 3 L/32 + 11/64) g2^2 C_LD/(16 pi^2) [Pauli normalization]")
    print("EOM-source companions: delta E_L^(1)=+3/4 C3; delta E_L^(3)=-1/4 C3.")
    print("LIMIT: these are the four-cross-box subset only; LSZ, counterterms and Ward completion remain open.")


if __name__ == "__main__":
    main()
