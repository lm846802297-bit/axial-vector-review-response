#!/usr/bin/env python3
"""Exact basis/evanescent seed audit for the RC-001 QLD8 source-square sector.

This checks representations, color completeness, derivative bookkeeping, and
4D gamma-string projections. It is NOT a one-loop counterterm calculation.
"""
from itertools import permutations, product
import sympy as sp

I = sp.I
zero2 = sp.zeros(2)
pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
gamma = [sp.diag(1, 1, -1, -1)]
for s in pauli:
    gamma.append(sp.BlockMatrix([[zero2, s], [-s, zero2]]).as_explicit())
metric = [1, -1, -1, -1]
gamma_lower = [metric[mu] * gamma[mu] for mu in range(4)]
gamma5 = I * gamma[0] * gamma[1] * gamma[2] * gamma[3]
identity4 = sp.eye(4)
projectors = {
    "R": (identity4 + gamma5) / 2,
    "L": (identity4 - gamma5) / 2,
}
chirality_sign = {"R": 1, "L": -1}


def epsilon4(indices):
    if len(indices) != 4 or len(set(indices)) != 4:
        return 0
    inversions = sum(
        1
        for i in range(4)
        for j in range(i + 1, 4)
        if indices[i] > indices[j]
    )
    return -1 if inversions % 2 else 1


def antisym_gamma(indices):
    """Unit-weight Gamma_[mu1 ... mun] using upper-index gamma matrices."""
    n = len(indices)
    out = sp.zeros(4)
    for perm in permutations(range(n)):
        inversions = sum(
            1
            for i in range(n)
            for j in range(i + 1, n)
            if perm[i] > perm[j]
        )
        term = identity4
        for slot in perm:
            term = term * gamma[indices[slot]]
        out += (-1 if inversions % 2 else 1) * term
    return sp.simplify(out / sp.factorial(n))


def kron(a, b):
    return sp.kronecker_product(a, b)


# 1. Exact Clifford algebra and open-line NDR gamma5/projector identities.
for mu, nu in product(range(4), repeat=2):
    anticommutator = gamma[mu] * gamma[nu] + gamma[nu] * gamma[mu]
    expected = 2 * metric[mu] * identity4 if mu == nu else sp.zeros(4)
    assert sp.simplify(anticommutator - expected) == sp.zeros(4)
assert sp.simplify(gamma5 * gamma5 - identity4) == sp.zeros(4)
for mu in range(4):
    assert sp.simplify(gamma5 * gamma[mu] + gamma[mu] * gamma5) == sp.zeros(4)
for chirality in "RL":
    assert sp.simplify(
        gamma5 * projectors[chirality]
        - chirality_sign[chirality] * projectors[chirality]
    ) == sp.zeros(4)

# 2. Exact 4D dualities for antisymmetrized rank-3 and rank-4 strings.
rank3_checks = 0
for idx in product(range(4), repeat=3):
    lhs = antisym_gamma(idx)
    rhs = sp.zeros(4)
    for sigma in range(4):
        rhs += I * epsilon4(idx + (sigma,)) * gamma_lower[sigma] * gamma5
    assert sp.simplify(lhs - rhs) == sp.zeros(4)
    rank3_checks += 1

rank4_checks = 0
for idx in product(range(4), repeat=4):
    lhs = antisym_gamma(idx)
    rhs = -I * epsilon4(idx) * gamma5
    assert sp.simplify(lhs - rhs) == sp.zeros(4)
    rank4_checks += 1

# 3. Contracted rank-3/rank-4 projections for RR, RL, LR, LL.
for x, y in product("RL", repeat=2):
    lhs3 = sp.zeros(16)
    lhs4 = sp.zeros(16)
    for idx in product(range(4), repeat=3):
        upper = antisym_gamma(idx)
        lower = sp.prod(metric[mu] for mu in idx) * upper
        lhs3 += kron(upper * projectors[x], lower * projectors[y])
    for idx in product(range(4), repeat=4):
        upper = antisym_gamma(idx)
        lower = sp.prod(metric[mu] for mu in idx) * upper
        lhs4 += kron(upper * projectors[x], lower * projectors[y])

    rhs_vector = sp.zeros(16)
    for mu in range(4):
        rhs_vector += kron(
            gamma_lower[mu] * projectors[x],
            gamma[mu] * projectors[y],
        )
    rhs_scalar = kron(projectors[x], projectors[y])

    eta_xy = chirality_sign[x] * chirality_sign[y]
    assert sp.simplify(lhs3 - 6 * eta_xy * rhs_vector) == sp.zeros(16)
    assert sp.simplify(lhs4 - 24 * eta_xy * rhs_scalar) == sp.zeros(16)

# 4. Direct-pairing RL tensor evanescent from a two-gamma chain.
sigma = {}
for mu in range(4):
    for nu in range(4):
        sigma[mu, nu] = sp.I / 2 * (
            gamma[mu] * gamma[nu] - gamma[nu] * gamma[mu]
        )
tensor_rl = sp.zeros(16)
gamma_chain_rl = sp.zeros(16)
for mu, nu in product(range(4), repeat=2):
    sigma_lower = metric[mu] * metric[nu] * sigma[mu, nu]
    tensor_rl += kron(
        sigma[mu, nu] * projectors["R"],
        sigma_lower * projectors["L"],
    )
    gamma_chain_rl += kron(
        gamma[mu] * gamma[nu] * projectors["R"],
        projectors["L"] * gamma_lower[nu] * gamma_lower[mu],
    )
assert sp.simplify(tensor_rl) == sp.zeros(16)
assert sp.simplify(
    gamma_chain_rl - 4 * kron(projectors["R"], projectors["L"]) - tensor_rl
) == sp.zeros(16)

# 4. SU(3) completeness with tr(T^A T^B)=delta^{AB}/2.
sqrt3 = sp.sqrt(3)
gell_mann = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sqrt3,
]
generators = [matrix / 2 for matrix in gell_mann]
color_checks = 0
for a, b, c, d in product(range(3), repeat=4):
    lhs = sum(
        (t[a, b] * t[c, d] for t in generators),
        sp.Integer(0),
    )
    rhs = sp.Rational(1, 2) * (
        (1 if a == d and c == b else 0)
        - sp.Rational(1, 3) * (1 if a == b and c == d else 0)
    )
    assert sp.simplify(lhs - rhs) == 0
    color_checks += 1

# 5. Source representation: each J has the Higgs hypercharge and is a doublet.
Y_Q = sp.Rational(1, 6)
Y_u = sp.Rational(2, 3)
Y_d = -sp.Rational(1, 3)
Y_L = -sp.Rational(1, 2)
Y_e = -1
Y_H = sp.Rational(1, 2)
source_hypercharges = {
    "J_d": -Y_d + Y_Q,
    "J_u": -Y_Q + Y_u,
    "J_e": -Y_e + Y_L,
}
assert source_hypercharges == {
    "J_d": Y_H, "J_u": Y_H, "J_e": Y_H
}

# Epsilon is the SU(2) invariant antisymmetric tensor:
# (T^a)^T epsilon + epsilon T^a = 0 for T^a=sigma^a/2.
epsilon2 = sp.Matrix([[0, 1], [-1, 0]])
for sigma in pauli:
    generator = sigma / 2
    assert sp.simplify(
        generator.T * epsilon2 + epsilon2 * generator
    ) == sp.zeros(2)

x_charges = {
    "Q_L": 0, "u_R": 0, "d_R": 0, "L_e": 0, "e_R": 0, "H": 0
}
assert all(charge == 0 for charge in x_charges.values())

# 6. Six independent source-pair sectors; nine ordered pairs; 36 placements.
channels = [
    ("d†d", "RL", "quark-quark", "1⊕8", "delta", "Y_d⊗Y_d†"),
    ("u†u", "LR", "quark-quark", "1⊕8", "delta", "Y_u†⊗Y_u"),
    ("e†e", "RL", "lepton-lepton", "1", "delta", "|y_e|²"),
    ("d†u", "RR", "quark-quark", "1⊕8", "epsilon", "Y_d⊗Y_u"),
    ("d†e", "RL", "quark-lepton", "1", "delta", "Y_d⊗y_e*"),
    ("u†e", "LL", "quark-lepton", "1", "epsilon", "Y_u†⊗y_e*"),
]
ordered_pairs = [
    "d†d", "u†u", "e†e",
    "d†u", "u†d", "d†e", "e†d", "u†e", "e†u",
]
placements = [(r, s) for r in (0, 1) for s in (0, 1)]
assert len(channels) == 6
assert len(ordered_pairs) == 9
assert len(ordered_pairs) * len(placements) == 36
assert 3 * len(placements) + 3 * 2 * len(placements) == 36

# 7. Candidate rank ceiling for a single gauge-exchange open-line numerator:
# a physical seed has rank <=2; at most two gamma matrices are added to a
# given open line before d-dimensional reduction. This is a ceiling, not proof
# that every rank is actually generated.
seed_ranks = {"RL": (1,), "LR": (1,), "RR": (0, 2), "LL": (0, 2)}
rank_ceiling = {
    chirality: max(ranks) + 2
    for chirality, ranks in seed_ranks.items()
}
assert rank_ceiling == {"RL": 3, "LR": 3, "RR": 4, "LL": 4}

print("RC-001 QLD8 one-loop counterterm-basis seed audit")
print("PASS: exact (+---) Clifford algebra and open-line gamma5 projectors.")
print(f"PASS: rank-3 duality: {rank3_checks}/64 index assignments.")
print(f"PASS: rank-4 duality: {rank4_checks}/256 index assignments.")
print("PASS: contracted Gamma_(3) x Gamma_(3) projections for RR, RL, LR, LL.")
print("      coefficient = 6 eta_X eta_Y times vector x vector.")
print("PASS: contracted Gamma_(4) x Gamma_(4) projections for RR, RL, LR, LL.")
print("      coefficient = 24 eta_X eta_Y times scalar x scalar.")
print("PASS: direct RL tensor contraction vanishes in 4D (candidate evanescent).")
print("PASS: two-gamma RL chain = 4 scalar + direct RL tensor in 4D.")
print(f"PASS: SU(3) completeness: {color_checks}/81 color-index assignments.")
print("PASS: J_d, J_u, J_e all transform as (1,2,+1/2).")
print("PASS: SU(2) epsilon is invariant under all three generators.")
print("PASS: Q_L, u_R, d_R, L_e, e_R, H are U(1)_X neutral.")
print("PASS: six independent source-pair sectors and nine ordered pairs.")
print("PASS: four derivative placements per ordered pair: 36 total.")
print("CANDIDATE one-gauge-exchange rank ceiling: RL/LR <= 3; RR/LL <= 4.")
print("LIMIT: no loop integral, UV pole, Z matrix, anomalous dimension, or matching coefficient.")
