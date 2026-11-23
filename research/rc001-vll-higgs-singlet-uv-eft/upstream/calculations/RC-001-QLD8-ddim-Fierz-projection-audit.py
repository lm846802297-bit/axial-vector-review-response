#!/usr/bin/env python3
"""Formal d-dimensional Fierz-projection coefficients for the direct RL tensor.

The symbolic D-dimensional part uses Clifford trace identities. The explicit
4D matrix part independently checks the sigma--Gamma^(n)--sigma sandwich
eigenvalues for n=0,...,4. This is an algebraic basis audit, not a loop
calculation and not a claim that a finite rank-1/rank-3 Fierz basis closes.
"""
from itertools import combinations, permutations
import sympy as sp

I = sp.I
D, eps = sp.symbols("D eps")


def falling_factorial(x, n):
    return sp.prod(x - k for k in range(n))


def sigma_sandwich_eigenvalue(n):
    # sigma^{mu nu} Gamma^(n) sigma_{mu nu}
    return sp.factor(D * (D - 1) - 4 * n * (D - n))


def chiral_trace_norm(n):
    # tr[Gamma^(n) P_R Gamma_(n) P_L], with tr(1)=4.
    # This formula is used only for odd n, for which the chiral projectors
    # select the non-vanishing crossed channel.
    return sp.factor(
        2 * (-1) ** (n * (n - 1) // 2) * falling_factorial(D, n)
    )


def crossed_projection_coefficient(n):
    assert n % 2 == 1
    return sp.factor(
        sigma_sandwich_eigenvalue(n) / chiral_trace_norm(n)
    )


f1 = crossed_projection_coefficient(1)
f3 = crossed_projection_coefficient(3)
f5 = crossed_projection_coefficient(5)

assert sp.simplify(
    f1 - (D - 1) * (D - 4) / (2 * D)
) == 0
assert sp.simplify(
    f3 + (D - 4) * (D - 9) /
    (2 * D * (D - 1) * (D - 2))
) == 0
assert sp.simplify(
    f5 - (D**2 - 21 * D + 100) /
    (2 * D * (D - 1) * (D - 2) * (D - 3) * (D - 4))
) == 0

assert sp.limit(f1.subs(D, 4 - 2 * eps) / eps, eps, 0) == -sp.Rational(3, 4)
assert sp.limit(f3.subs(D, 4 - 2 * eps) / eps, eps, 0) == -sp.Rational(5, 24)
assert sp.limit(eps * f5.subs(D, 4 - 2 * eps), eps, 0) == -sp.Rational(1, 3)

# Explicit (+---) 4D gamma matrices for the sigma-sandwich check.
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
sigma = {
    (mu, nu): sp.simplify(
        I / 2 * (gamma[mu] * gamma[nu] - gamma[nu] * gamma[mu])
    )
    for mu in range(4) for nu in range(4)
}
sigma_lower = {
    (mu, nu): metric[mu] * metric[nu] * sigma[(mu, nu)]
    for mu in range(4) for nu in range(4)
}


def antisym_gamma(indices):
    n = len(indices)
    if n == 0:
        return sp.eye(4)
    total = sp.zeros(4)
    for perm in permutations(indices):
        inversions = sum(
            1
            for i in range(n)
            for j in range(i + 1, n)
            if perm[i] > perm[j]
        )
        product = sp.eye(4)
        for mu in perm:
            product = product * gamma[mu]
        total += (-1) ** inversions * product
    return sp.simplify(total / sp.factorial(n))


expected_4d = {0: 12, 1: 0, 2: -4, 3: 0, 4: 12}
for n in range(5):
    for indices in combinations(range(4), n):
        G = antisym_gamma(indices)
        sandwich = sp.zeros(4)
        for mu in range(4):
            for nu in range(4):
                sandwich += sigma[(mu, nu)] * G * sigma_lower[(mu, nu)]
        sandwich = sp.simplify(sandwich)
        assert sp.simplify(sandwich - expected_4d[n] * G) == sp.zeros(4)

norm5 = chiral_trace_norm(5)
assert sp.simplify(norm5.subs(D, 4)) == 0
assert sp.simplify(sp.limit(norm5 / (D - 4), D, 4)) != 0

print("RC-001 QLD8 d-dimensional direct RL tensor Fierz-projection audit")
print("PASS: sigma-Gamma^(n)-sigma eigenvalue checked explicitly for n=0,...,4 in 4D.")
print("PASS: formal Clifford eigenvalue lambda_n = D(D-1)-4 n(D-n).")
print("PASS: chiral trace norm t_n = 2 (-1)^[n(n-1)/2] D(D-1)...(D-n+1), odd n.")
print(f"PASS: f_1(D) = {f1}")
print(f"PASS: f_3(D) = {f3}")
print(f"PASS: f_5(D) = {f5}")
print("PASS: D=4-2epsilon: f_1 = -3 epsilon/4 + O(epsilon^2).")
print("PASS: D=4-2epsilon: f_3 = -5 epsilon/24 + O(epsilon^2).")
print("PASS: D=4-2epsilon: f_5 = -1/(3 epsilon) + O(1).")
print("PASS: rank-five chiral Gram norm vanishes at D=4; f_5 pole is a basis-projection singularity.")
print("LIMIT: projection coefficients only; no finite-rank Fierz closure, loop UV pole, or Z matrix.")
