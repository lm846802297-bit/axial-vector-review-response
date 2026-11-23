#!/usr/bin/env python3
"""Exact SU(2) map from the WW T3 derivative tensor to its adjoint-W contact."""
import sympy as sp

I = sp.I
g = sp.symbols("g", commutative=True)
sigma = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
W = sp.symbols("W1:4", commutative=True)
Y = sp.symbols("Y1:4", commutative=True)


def delta(a, b):
    return sp.Integer(1 if a == b else 0)


def audit_pauli_completeness():
    # Sum_a sigma^a_ij sigma^a_kl = 2 delta_il delta_kj - delta_ij delta_kl.
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    lhs = sum(sigma[a][i, j]*sigma[a][k, l] for a in range(3))
                    rhs = 2*delta(i, l)*delta(k, j)-delta(i, j)*delta(k, l)
                    assert sp.simplify(lhs-rhs) == 0
    return True


def adjoint_contact_matrix():
    A = sum((W[a]*sigma[a]/2 for a in range(3)), sp.zeros(2))
    Ymat = sum((Y[a]*sigma[a] for a in range(3)), sp.zeros(2))
    return sp.simplify(-I*g*(A*Ymat-Ymat*A))


def epsilon_contact_matrix():
    rhs = sp.zeros(2)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                rhs += g*sp.LeviCivita(a, b, c)*W[b]*Y[c]*sigma[a]
    return sp.simplify(rhs)


def audit_adjoint_derivative():
    lhs = adjoint_contact_matrix()
    rhs = epsilon_contact_matrix()
    assert all(sp.simplify(lhs[i, j]-rhs[i, j]) == 0
               for i in range(2) for j in range(2))
    return True


def audit_triplet_tensor_normalization():
    # With sigma^I normalization, X^I Y^I has exactly the T3 tensor.
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    t3 = 2*delta(i, l)*delta(k, j)-delta(i, j)*delta(k, l)
                    tensor = sum(sigma[a][i, j]*sigma[a][k, l]
                                 for a in range(3))
                    assert sp.simplify(tensor-t3) == 0
    return True


def main():
    audit_pauli_completeness()
    audit_adjoint_derivative()
    audit_triplet_tensor_normalization()
    print("RC-001 Q_LD triplet derivative / external-W contact audit")
    print("PASS: sum_I sigma^I_ij sigma^I_kl = 2 delta_il delta_kj - delta_ij delta_kl = T3.")
    print("PASS: -i g_2 [W^I sigma^I/2, Y^J sigma^J] = g_2 epsilon^{IJK} W^J Y^K sigma^I.")
    print("Therefore D_mu^adj Y^I = partial_mu Y^I + g_2 epsilon^{IJK} W_mu^J Y^K.")
    print("For Q_LD^(3)=(barL sigma^I H) i gamma^mu D_mu^adj(Hdag sigma^I L),")
    print("the local one-W contact is i g_2 epsilon^{IJK}(barL sigma^I H) gamma^mu W_mu^J(Hdag sigma^K L).")
    print("BOUNDARY: this is the EFT contact required by a local T3 derivative operator;")
    print("it is not the UV one-loop five-point form factor or the full matching coefficient.")


if __name__ == "__main__":
    main()
