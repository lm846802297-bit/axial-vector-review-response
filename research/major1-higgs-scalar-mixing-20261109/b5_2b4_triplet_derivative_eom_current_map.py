#!/usr/bin/env python3
"""B5-2B4: Pauli-triplet derivative operator EOM/current-basis audit."""
import sympy as sp

I = sp.I
g2 = sp.symbols("g2", real=True)
C_LD = sp.symbols("C_LD", real=True)
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
    """Check D(H^dagger sigma^I L)=partial C^I-g eps^{aIJ}W^a C^J."""
    W = sp.symbols("W0:3", commutative=True)
    h = sp.Matrix(sp.symbols("h0:2", commutative=True))
    hb = sp.Matrix([[*sp.symbols("hb0:2", commutative=True)]])
    L = sp.Matrix(sp.symbols("l0:2", commutative=True))
    dh = sp.Matrix(sp.symbols("dh0:2", commutative=True))
    dhb = sp.Matrix([[*sp.symbols("dhb0:2", commutative=True)]])
    dL = sp.Matrix(sp.symbols("dl0:2", commutative=True))

    for a in range(3):
        for Jidx in range(3):
            comm = T[a]*SIGMA[Jidx] - SIGMA[Jidx]*T[a]
            expected = I*sum(
                eps3(a, Jidx, K)*SIGMA[K] for K in range(3)
            )
            assert all(sp.simplify(x) == 0 for x in comm-expected)

    # The product rule yields the adjoint connection with the stated sign.
    for Jidx in range(3):
        ordinary = (dhb*SIGMA[Jidx]*L + hb*SIGMA[Jidx]*dL)[0]
        gauge_from_doublets = sum(
            I*g2*W[a]*(hb*(T[a]*SIGMA[Jidx]-SIGMA[Jidx]*T[a])*L)[0]
            for a in range(3)
        )
        adjoint = -g2*sum(
            eps3(a, Jidx, K)*W[a]*(hb*SIGMA[K]*L)[0]
            for a in range(3) for K in range(3)
        )
        assert sp.simplify(gauge_from_doublets-adjoint) == 0
    return True


def box_to_current_coefficients():
    """Map the raw WW T3 box coefficient through the triplet EOM identity."""
    # C3 = (3/4) * g2^2/(16 pi^2) * C_LD.
    C3 = sp.Rational(3, 4)*g2**2*C_LD/(16*sp.pi**2)
    delta_C_HL1 = -sp.Rational(3,4)*C3
    delta_C_HL3 = +sp.Rational(1,4)*C3
    delta_E1 = +sp.Rational(3,4)*C3
    delta_E3 = -sp.Rational(1,4)*C3

    assert sp.simplify(delta_C_HL1 + sp.Rational(9,4)*g2**2*C_LD/(16*sp.pi**2)) == 0
    assert sp.simplify(delta_C_HL3 - sp.Rational(3,4)*g2**2*C_LD/(16*sp.pi**2)) == 0
    assert sp.simplify(delta_E1 - sp.Rational(9,4)*g2**2*C_LD/(16*sp.pi**2)) == 0
    assert sp.simplify(delta_E3 + sp.Rational(3,4)*g2**2*C_LD/(16*sp.pi**2)) == 0
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
    coeffs = box_to_current_coefficients()

    print("B5-2B4 Pauli-triplet derivative EOM/current audit")
    print("PASS: Q_LD^(3) = -O_HL^(1) + E_L^(1) - Q_LD modulo total derivative.")
    print("PASS: substituting the Q_LD EOM map gives the common Pauli-current basis.")
    print("PASS: adjoint derivative D_mu(H^dagger sigma^I L) has -g2 eps^{aIJ}W^a contact.")
    print("Raw box coefficient C3 = 3 g2^2 C_LD/(64 pi^2)")
    print("delta C_HL^(1) = -9 g2^2 C_LD/(256 pi^2)")
    print("delta C_HL^(3) = +3 g2^2 C_LD/(256 pi^2)")
    print("EOM-source companions: delta E_L^(1)=+9/4 C3; delta E_L^(3)=-1/4 C3.")
    print("LIMIT: these are the four-cross-box subset only; LSZ, counterterms and Ward completion remain open.")


if __name__ == "__main__":
    main()
