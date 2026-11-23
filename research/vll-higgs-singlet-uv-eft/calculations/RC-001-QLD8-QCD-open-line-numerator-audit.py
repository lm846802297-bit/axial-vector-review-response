#!/usr/bin/env python3
"""Exact 4D checks of the QLD8 d†d Feynman-gauge open-line gamma chains."""
import sympy as sp

I = sp.I
zero2 = sp.zeros(2)
pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for p in pauli:
    gamma.append(sp.BlockMatrix([[zero2, p], [-p, zero2]]).as_explicit())
metric = [1, -1, -1, -1]
gamma_lower = [metric[mu] * gamma[mu] for mu in range(4)]
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
eye = sp.eye(4)
PR = sp.simplify((eye + gamma5) / 2)
PL = sp.simplify((eye - gamma5) / 2)
Gamma2 = {
    (mu, nu): sp.simplify(
        (gamma[mu] * gamma[nu] - gamma[nu] * gamma[mu]) / 2
    )
    for mu in range(4) for nu in range(4)
}


def g(mu, nu):
    return sp.Integer(metric[mu] if mu == nu else 0)


def Gamma_up_down(mu, nu):
    return metric[nu] * Gamma2[mu, nu]


def Gamma_down_up(mu, nu):
    return metric[mu] * Gamma2[mu, nu]


def kron(a, b):
    return sp.kronecker_product(a, b)


zero16 = sp.zeros(16)
checks = 0

for alpha in range(4):
    for beta in range(4):
        gab = g(alpha, beta)

        # barQ--Q: (gamma^rho gamma^alpha PR) x (PL gamma^beta gamma_rho)
        lhs = sum(
            (
                kron(
                    gamma[rho] * gamma[alpha] * PR,
                    PL * gamma[beta] * gamma_lower[rho],
                )
                for rho in range(4)
            ),
            zero16,
        )
        rhs = gab * kron(PR, PL)
        rhs += kron(PR, Gamma2[beta, alpha] * PL)
        rhs += kron(Gamma2[beta, alpha] * PR, PL)
        for rho in range(4):
            rhs += kron(
                Gamma2[rho, alpha] * PR,
                Gamma_up_down(beta, rho) * PL,
            )
        assert sp.simplify(lhs - rhs) == zero16
        checks += 1

        # barQ--bard: (gamma^rho gamma^alpha PR) x (gamma_rho gamma^beta PL)
        lhs = sum(
            (
                kron(
                    gamma[rho] * gamma[alpha] * PR,
                    gamma_lower[rho] * gamma[beta] * PL,
                )
                for rho in range(4)
            ),
            zero16,
        )
        rhs = gab * kron(PR, PL)
        rhs += kron(PR, Gamma2[alpha, beta] * PL)
        rhs += kron(Gamma2[beta, alpha] * PR, PL)
        for rho in range(4):
            rhs += kron(
                Gamma2[rho, alpha] * PR,
                Gamma_down_up(rho, beta) * PL,
            )
        assert sp.simplify(lhs - rhs) == zero16
        checks += 1

        # Q--d: (PR gamma^alpha gamma^rho) x (PL gamma^beta gamma_rho)
        lhs = sum(
            (
                kron(
                    PR * gamma[alpha] * gamma[rho],
                    PL * gamma[beta] * gamma_lower[rho],
                )
                for rho in range(4)
            ),
            zero16,
        )
        rhs = gab * kron(PR, PL)
        rhs += kron(PR, Gamma2[beta, alpha] * PL)
        rhs += kron(Gamma2[alpha, beta] * PR, PL)
        for rho in range(4):
            rhs += kron(
                Gamma2[alpha, rho] * PR,
                Gamma_up_down(beta, rho) * PL,
            )
        assert sp.simplify(lhs - rhs) == zero16
        checks += 1

        # bard--d: (PR gamma^alpha gamma^rho) x (gamma_rho gamma^beta PL)
        lhs = sum(
            (
                kron(
                    PR * gamma[alpha] * gamma[rho],
                    gamma_lower[rho] * gamma[beta] * PL,
                )
                for rho in range(4)
            ),
            zero16,
        )
        rhs = gab * kron(PR, PL)
        rhs += kron(PR, Gamma2[alpha, beta] * PL)
        rhs += kron(Gamma2[alpha, beta] * PR, PL)
        for rho in range(4):
            rhs += kron(
                Gamma2[alpha, rho] * PR,
                Gamma_down_up(rho, beta) * PL,
            )
        assert sp.simplify(lhs - rhs) == zero16
        checks += 1

# Same-bilinear contracted chain in 4D:
# gamma^rho gamma^alpha gamma^beta gamma_rho = 4 g^{alpha beta}.
same_bilinear_checks = 0
for alpha in range(4):
    for beta in range(4):
        lhs = sum(
            (
                gamma[rho] * gamma[alpha] * gamma[beta] * gamma_lower[rho]
                for rho in range(4)
            ),
            sp.zeros(4),
        )
        rhs = 4 * g(alpha, beta) * eye
        assert sp.simplify(lhs - rhs) == sp.zeros(4)
        same_bilinear_checks += 1

print("RC-001 QLD8 d†d QCD open-line numerator gamma audit")
print(f"PASS: four cross-exchange decompositions: {checks}/64 Lorentz-index assignments.")
print(f"PASS: same-bilinear contracted chain in 4D: {same_bilinear_checks}/16 assignments.")
print("PASS: all displayed direct-pairing chains contain gamma rank at most two on each bilinear.")
print("D-dimensional identity used: gamma^rho Gamma^(2) gamma_rho = (D-4) Gamma^(2).")
print("LIMIT: no Feynman-rule overall signs, loop integrals, UV poles, or Z matrix.")
