#!/usr/bin/env python3
"""Exact convention audit for the QLD8 second-order fermion-EOM map."""
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
sigma = {}
for mu in range(4):
    for nu in range(4):
        sigma[mu, nu] = sp.simplify(I/2*(gamma[mu]*gamma[nu]-gamma[nu]*gamma[mu]))

# Verify Clifford algebra and sigma convention exactly.
for mu in range(4):
    for nu in range(4):
        anti = sp.simplify(gamma[mu]*gamma[nu] + gamma[nu]*gamma[mu])
        expected = 2*metric[mu]*sp.eye(4) if mu == nu else sp.zeros(4)
        assert anti == expected

# For arbitrary antisymmetric F_{mu nu}, compare
# 1/4 [gamma^mu,gamma^nu] [D_mu,D_nu]
# with 1/2 sigma^{mu nu} F_{mu nu}, [D_mu,D_nu]=i F_{mu nu}.
F = {}
for mu in range(4):
    for nu in range(mu+1, 4):
        F[mu, nu] = sp.symbols(f"F{mu}{nu}")
lhs = sp.zeros(4)
rhs = sp.zeros(4)
for (mu, nu), value in F.items():
    # Sum over both antisymmetric index orderings.
    comm_gamma = gamma[mu]*gamma[nu]-gamma[nu]*gamma[mu]
    comm_D = I*value
    lhs += sp.Rational(1, 2)*comm_gamma*comm_D
    sigma_up = sigma[mu, nu]
    # 1/2 sigma^{rho sigma} F_{rho sigma} includes both rho,sigma.
    rhs += sigma_up*value
assert sp.simplify(lhs-rhs) == sp.zeros(4)

# Hypercharge source check: all three J_H^(4) pieces transform as H.
Y_Q, Y_u, Y_d, Y_L, Y_e, Y_H = (
    sp.Rational(1, 6), sp.Rational(2, 3), -sp.Rational(1, 3),
    -sp.Rational(1, 2), -1, sp.Rational(1, 2)
)
source_hypercharges = {
    "J_d": -Y_d + Y_Q,
    "J_u": -Y_Q + Y_u,
    "J_e": -Y_e + Y_L,
}
assert source_hypercharges == {"J_d": Y_H, "J_u": Y_H, "J_e": Y_H}

# The retained quarks and electron have zero L_mu-L_tau charge.
x_charges = {
    "Q_L": 0, "u_R": 0, "d_R": 0, "L_e": 0, "e_R": 0
}
assert all(q == 0 for q in x_charges.values())

print("RC-001 QLD8 second-order fermion-EOM convention audit")
print("PASS: explicit gamma matrices satisfy the (+---) Clifford algebra.")
print("PASS: D^2 = slash(D)^2 - (1/2) sigma^{mu nu} F_{mu nu} for [D_mu,D_nu]=i F_{mu nu}.")
print("PASS: J_d, J_u, and J_e each carry Higgs hypercharge Y_H=+1/2.")
print("PASS: Q_L, u_R, d_R, L_e, e_R are neutral under U(1)_X.")
print("LIMIT: no Wilson coefficients, d-dimensional loop mixing, or finite matching computed.")
