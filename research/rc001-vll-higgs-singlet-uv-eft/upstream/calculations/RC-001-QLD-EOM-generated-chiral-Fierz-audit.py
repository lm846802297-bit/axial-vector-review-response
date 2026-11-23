#!/usr/bin/env python3
"""Exact 4D Fierz audit for scalar-vector and scalar-tensor EOM structures."""
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
gamma5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
eye = sp.eye(4)
PR = sp.simplify((eye + gamma5) / 2)
PL = sp.simplify((eye - gamma5) / 2)
metric = [1, -1, -1, -1]
gamma_lower = [metric[mu] * gamma[mu] for mu in range(4)]
sigma = {
    (mu, nu): sp.simplify(I / 2 * (gamma[mu] * gamma[nu] - gamma[nu] * gamma[mu]))
    for mu in range(4) for nu in range(4)
}


def eps4(indices):
    if len(set(indices)) < 4:
        return 0
    inversions = sum(
        1 for i in range(4) for j in range(i + 1, 4)
        if indices[i] > indices[j]
    )
    return -1 if inversions % 2 else 1


def crossed_tensor(A, B):
    """Matrix with entries A_(alpha delta) B_(gamma beta)."""
    out = sp.zeros(16)
    for a in range(4):
        for d in range(4):
            for c in range(4):
                for b in range(4):
                    out[4 * a + d, 4 * c + b] = sp.simplify(A[a, d] * B[c, b])
    return out


def original_tensor(A, B):
    """Matrix with entries A_(alpha beta) B_(gamma delta)."""
    out = sp.zeros(16)
    for a in range(4):
        for d in range(4):
            for c in range(4):
                for b in range(4):
                    out[4 * a + d, 4 * c + b] = sp.simplify(A[a, b] * B[c, d])
    return out


def exact_zero(matrix):
    return sp.simplify(matrix) == sp.zeros(16)


def audit():
    # Scalar-vector: 2 x 2 chiralities x 4 Lorentz components = 16 identities.
    vector_count = 0
    for x, p in (("R", PR), ("L", PL)):
        for y, q in (("R", PR), ("L", PL)):
            for mu in range(4):
                if (x, y) == ("R", "R"):
                    rhs = sp.Rational(1, 2) * crossed_tensor(PR, gamma[mu] * PR)
                    for nu in range(4):
                        rhs += I * sp.Rational(1, 2) * crossed_tensor(
                            sigma[mu, nu] * PR, gamma_lower[nu] * PR
                        )
                elif (x, y) == ("R", "L"):
                    rhs = sp.Rational(1, 2) * crossed_tensor(gamma[mu] * PL, PR)
                    for nu in range(4):
                        rhs -= I * sp.Rational(1, 2) * crossed_tensor(
                            gamma_lower[nu] * PL, sigma[mu, nu] * PR
                        )
                elif (x, y) == ("L", "R"):
                    rhs = sp.Rational(1, 2) * crossed_tensor(gamma[mu] * PR, PL)
                    for nu in range(4):
                        rhs -= I * sp.Rational(1, 2) * crossed_tensor(
                            gamma_lower[nu] * PR, sigma[mu, nu] * PL
                        )
                else:
                    rhs = sp.Rational(1, 2) * crossed_tensor(PL, gamma[mu] * PL)
                    for nu in range(4):
                        rhs += I * sp.Rational(1, 2) * crossed_tensor(
                            sigma[mu, nu] * PL, gamma_lower[nu] * PL
                        )
                assert exact_zero(original_tensor(p, gamma[mu] * q) - rhs), (x, y, mu)
                vector_count += 1

    # Opposite-chirality scalar-tensor: 2 chiralities x 6 independent mu<nu.
    opposite_tensor_count = 0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            rhs_rl = -I * sp.Rational(1, 2) * (
                crossed_tensor(gamma[mu] * PL, gamma[nu] * PR)
                - crossed_tensor(gamma[nu] * PL, gamma[mu] * PR)
            )
            rhs_lr = -I * sp.Rational(1, 2) * (
                crossed_tensor(gamma[mu] * PR, gamma[nu] * PL)
                - crossed_tensor(gamma[nu] * PR, gamma[mu] * PL)
            )
            for rho in range(4):
                for sig in range(4):
                    eps = eps4((mu, nu, rho, sig))
                    if eps:
                        rhs_rl -= sp.Rational(1, 2) * eps * crossed_tensor(
                            gamma_lower[rho] * PL, gamma_lower[sig] * PR
                        )
                        rhs_lr += sp.Rational(1, 2) * eps * crossed_tensor(
                            gamma_lower[rho] * PR, gamma_lower[sig] * PL
                        )
            assert exact_zero(original_tensor(PR, sigma[mu, nu] * PL) - rhs_rl), ("RL", mu, nu)
            assert exact_zero(original_tensor(PL, sigma[mu, nu] * PR) - rhs_lr), ("LR", mu, nu)
            opposite_tensor_count += 2

    # Same-chirality scalar-tensor: 2 chiralities x 3 independent sigma^(0i).
    same_tensor_count = 0
    for chirality, p, eps_coefficient in (
        ("R", PR, sp.Rational(1, 2)),
        ("L", PL, -sp.Rational(1, 2)),
    ):
        for i in (1, 2, 3):
            rhs = (
                sp.Rational(1, 2) * crossed_tensor(p, sigma[0, i] * p)
                + sp.Rational(1, 2) * crossed_tensor(sigma[0, i] * p, p)
            )
            for j in (1, 2, 3):
                for k in (1, 2, 3):
                    eps = eps4((0, i, j, k))
                    if eps:
                        rhs += eps_coefficient * eps * crossed_tensor(
                            sigma[0, j] * p, sigma[0, k] * p
                        )
            assert exact_zero(original_tensor(p, sigma[0, i] * p) - rhs), (chirality, i)
            same_tensor_count += 1

    # Self-duality/anti-self-duality of the chiral tensor components.
    duality_count = 0
    for chirality, p, coefficient in (("R", PR, -I), ("L", PL, I)):
        for i, j, k in ((1, 2, 3), (2, 3, 1), (3, 1, 2)):
            assert sp.simplify(sigma[i, j] * p - coefficient * sigma[0, k] * p) == sp.zeros(4)
            duality_count += 1

    total_identities = vector_count + opposite_tensor_count + same_tensor_count
    total_components = total_identities * 256
    assert (vector_count, opposite_tensor_count, same_tensor_count) == (16, 12, 6)
    assert total_identities == 34
    assert total_components == 8704
    assert duality_count == 6
    return vector_count, opposite_tensor_count, same_tensor_count, total_components, duality_count


if __name__ == "__main__":
    v, ot, st, components, duality = audit()
    print("RC-001 EOM-generated chiral Fierz exact-matrix audit")
    print(f"PASS: scalar-vector identities: {v}/16")
    print(f"PASS: opposite-chirality scalar-tensor identities: {ot}/12")
    print(f"PASS: same-chirality scalar-tensor identities: {st}/6")
    print(f"PASS: total exact components: {components}/8704")
    print(f"PASS: chiral tensor self-duality relations: {duality}/6")
    print("LIMIT: four-dimensional Fierz projections only; no d-dimensional loop mixing or finite matching")
