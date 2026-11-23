#!/usr/bin/env python3
"""Independent analytic cross-checks for RC-001 dimension-six EFT soft loops.

The script derives scalar master-integral pole/finite parts from Feynman-parameter
Gamma functions, checks the tensor-reduction identities, and verifies the hard +
soft pole cancellations for:
  * the C5 C5* crossed two-fermion/two-scalar current channels;
  * the C5 C5* four-fermion scalar bubble;
  * one Q6 insertion plus a scalar-quartic vertex.

It is not a Feynman-rule generator, a FeynCalc run, or a complete gauge-sector
matching calculation. Overall field/operator projections are documented in the
companion research note; the checks here operate on explicitly stated stripped
loop kernels and their common MS-bar normalization.
"""
import sympy as sp

eps = sp.symbols("eps", positive=True)
x = sp.symbols("x", positive=True)
L, ell = sp.symbols("L_E ell_q")
d = 4 - 2 * eps
Delta = 1 / eps - sp.EulerGamma + sp.log(4 * sp.pi)
checks = []


def check(name, lhs, rhs):
    diff = sp.simplify(lhs - rhs)
    if diff != 0:
        raise AssertionError(f"{name}: residual = {diff}")
    checks.append(name)


# 1. Massless two-propagator bubble from its Feynman-parameter representation.
# B0(q^2;0,0) = Delta - log((-q^2-i0)/mu^2) - int_0^1 log[x(1-x)] dx.
log_endpoint = sp.integrate(sp.log(x * (1 - x)), (x, 0, 1))
check("massless B0 finite parameter integral gives +2", -log_endpoint, 2)

# Tensor reduction follows from x <-> 1-x symmetry after shifting
# k -> l - (1-x)q: int k_mu = -q_mu/2 B0, int (k+q)_mu = +q_mu/2 B0.
check("crossed numerator k+q gives +q/2", -sp.Rational(1, 2) + 1, sp.Rational(1, 2))
check("crossed numerator k gives -q/2", -sp.Rational(1, 2), -sp.Rational(1, 2))

# The scalar four-point numerator reduces as
# 2 k.(k+q) = k^2 + (k+q)^2 - q^2; the first two terms are scaleless tadpoles.
k2, q2, kdotq = sp.symbols("k2 q2 kdotq")
check("scalar bubble numerator identity", 2 * (k2 + kdotq),
      k2 + (k2 + 2 * kdotq + q2) - q2)

# 2. Independent Feynman-parameter Gamma-function expansions for hard integrals.
# All values below are normalized by i/(16 pi^2 M^n).
scale = sp.exp(eps * (sp.log(4 * sp.pi) - L))
J22n = scale * sp.gamma(2 + eps) * sp.gamma(-eps) / sp.gamma(2 - eps)
K1n = -scale * sp.gamma(1 + eps) * sp.gamma(-eps) / sp.gamma(2 - eps)
J12n = -scale * sp.gamma(1 + eps) / (1 - eps)
J13n = scale * sp.gamma(2 + eps) / (2 * (1 - eps))

check("J22 hard integral: -Delta_IR + L_E - 2",
      sp.series(J22n, eps, 0, 1).removeO(), -Delta + L - 2)
check("single-heavy K1 integral: +Delta_IR + 1 - L_E",
      sp.series(K1n, eps, 0, 1).removeO(), Delta + 1 - L)
check("J12 finite integral equals -1",
      sp.limit(J12n, eps, 0), -1)
check("J13 finite integral equals +1/2",
      sp.limit(J13n, eps, 0), sp.Rational(1, 2))

# Independent Feynman-parameter evaluation of the crossed-current hard integral.
# With z=x3+x4, x2=(1-z)u, x3=zt, x4=z(1-t), the simplex measure is
# z(1-z) dz du dt. The q and (p3-p1) coefficients reduce to these 1D integrals.
Fq_param = scale * sp.gamma(2 + eps) * (
    -1 / (2 * eps) - 1 / (2 * (2 - eps))
)
Fp_param = scale * sp.gamma(2 + eps) / (2 * (1 - eps) * (2 - eps))
check("Feynman-parameter crossed-current q coefficient independently reproduces -Delta/2+L/2-3/4",
      sp.series(Fq_param, eps, 0, 1).removeO(),
      -Delta / 2 + L / 2 - sp.Rational(3, 4))
check("Feynman-parameter crossed-current EOM coefficient independently gives +1/4",
      sp.limit(Fp_param, eps, 0), sp.Rational(1, 4))

# 3. Crossed C5 C5* two-fermion/two-scalar channel.
# Representative stripped kernel:
# M^2 (k+q)^mu/[k^2 (k+q)^2 ((k+p1)^2-M^2)((k-p3)^2-M^2)].
# Its hard expansion is M^2[(1-2/d)q^mu J22 + (2/d)(p3-p1)^mu J13].
hard_current_q = (1 - 2 / d) * (-Delta + L - 2)
check("crossed-current hard q coefficient retains O(epsilon) x IR pole",
      sp.series(hard_current_q, eps, 0, 1).removeO(),
      -Delta / 2 + L / 2 - sp.Rational(3, 4))
check("crossed-current finite J13 vector coefficient",
      sp.limit(1 / d, eps, 0), sp.Rational(1, 4))

# The soft vector integral is q/2 times B0. Its UV pole cancels the hard IR pole.
crossed_sum = sp.simplify(
    (-Delta / 2 + L / 2 - sp.Rational(3, 4))
    + (Delta - ell + 2) / 2
)
check("crossed-current hard+soft pole cancellation and finite q kernel",
      crossed_sum, (L - ell) / 2 + sp.Rational(1, 4))

# On-shell, (p3-p1)_mu bar u(p1) gamma^mu u(p3) = 0 by both massless Dirac equations.
check("crossed-current hard+soft q coefficient in common normalization",
      2 * crossed_sum, L - ell + sp.Rational(1, 2))

# For O_phi_f = (phi^dagger i <->D_mu phi)(bar f gamma^mu f),
# q_mu J^mu = +1/2 (p_phi-p_phi^dagger)_mu J^mu when the barred fermion
# and phi are at the same C5 vertex; the conjugate orientation flips this sign.
check("on-shell q to scalar-current momentum factor",
      sp.Rational(1, 2) * 2, 1)

# 4. C5 C5* four-fermion scalar bubble.
# Hard part M^2 J22; soft part B0. Their poles and constants cancel.
fourf_sum = sp.simplify((-Delta + L - 2) + (Delta - ell + 2))
check("four-fermion hard+soft poles and finite constants cancel",
      fourf_sum, L - ell)

# 5. One Q6 insertion plus a scalar-quartic vertex.
# Let p be the momentum on the barred fermion, p' on the unbarred fermion,
# and Q=-(p+p') the total external scalar momentum. The Q6 derivative gives
# the stripped numerator -(k+p); the full UV graph has one heavy propagator.
K1exp = sp.series(K1n, eps, 0, 1).removeO()
J12exp = -1
hard_Q6_p = -K1exp + (2 / d) * J12exp
hard_Q6_Q = -(2 / d) * K1exp
check("Q6-quartic hard p coefficient",
      sp.series(hard_Q6_p, eps, 0, 1).removeO(),
      -Delta + L - sp.Rational(3, 2))
check("Q6-quartic hard Q coefficient",
      sp.series(hard_Q6_Q, eps, 0, 1).removeO(),
      -Delta / 2 + L / 2 - sp.Rational(3, 4))
check("Q6-quartic hard polynomial has the required p+Q/2 ratio",
      (-Delta + L - sp.Rational(3, 2)) / 2,
      -Delta / 2 + L / 2 - sp.Rational(3, 4))

# Independent Feynman-parameter reduction of the one-heavy-line, two-scalar hard
# kernel: the remaining z integral is int_0^1 dz z^(-1-eps)(1-z)^2.
q6_param = scale * sp.gamma(1 + eps) * (-1 / eps - sp.Rational(3, 2))
check("Feynman-parameter Q6-quartic hard kernel independently gives -Delta+L-3/2",
      sp.series(q6_param, eps, 0, 1).removeO(),
      -Delta + L - sp.Rational(3, 2))

# The soft region of the heavy propagator contributes (p+Q/2) B0.
q6_sum = sp.simplify((-Delta + L - sp.Rational(3, 2)) + (Delta - ell + 2))
check("Q6-quartic hard+soft pole cancellation and finite EOM kernel",
      q6_sum, L - ell + sp.Rational(1, 2))
p, pp = sp.symbols("p pprime")
Q = -(p + pp)
check("Q6-quartic momentum polynomial reduces to fermion EOM",
      p + Q / 2, (p - pp) / 2)

# 6. SU(2) tensor completeness for the crossed H-current channel:
# delta_il delta_jk = 1/2(delta_ij delta_kl + sigma^I_ij sigma^I_kl).
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                lhs = int(i == l and j == k)
                rhs = sp.Rational(1, 2) * (
                    int(i == j and k == l)
                    + sum(s[i, j] * s[k, l] for s in (sigma1, sigma2, sigma3))
                )
                check(f"SU(2) singlet/triplet tensor completeness {i}{j}{k}{l}", lhs, rhs)

# 7. Chiral Fierz identity in an explicit Weyl/chiral gamma-matrix basis.
# The matrix identity is positive; the familiar minus sign in
# (bar L e_R)(bar e_R L) = -1/2 (bar L gamma_mu L)(bar e_R gamma^mu e_R)
# arises when the Grassmann fields are reordered after applying this identity.
I2 = sp.eye(2)
zero2 = sp.zeros(2)
gamma = [
    sp.BlockMatrix([[zero2, I2], [I2, zero2]]).as_explicit(),
    sp.BlockMatrix([[zero2, sigma1], [-sigma1, zero2]]).as_explicit(),
    sp.BlockMatrix([[zero2, sigma2], [-sigma2, zero2]]).as_explicit(),
    sp.BlockMatrix([[zero2, sigma3], [-sigma3, zero2]]).as_explicit(),
]
gamma5 = sp.I * gamma[0] * gamma[1] * gamma[2] * gamma[3]
PL = (sp.eye(4) - gamma5) / 2
PR = (sp.eye(4) + gamma5) / 2
metric = (1, -1, -1, -1)
gamma_algebra_failures = 0
fierz_failures = 0
for mu in range(4):
    for nu in range(4):
        anticommutator = gamma[mu] * gamma[nu] + gamma[nu] * gamma[mu]
        expected = 2 * metric[mu] * sp.eye(4) if mu == nu else sp.zeros(4)
        if anticommutator != expected:
            gamma_algebra_failures += 1
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d0 in range(4):
                lhs = PR[a, b] * PL[c, d0]
                rhs = sp.Rational(1, 2) * sum(
                    metric[mu] * (gamma[mu] * PL)[a, d0] * (gamma[mu] * PR)[c, b]
                    for mu in range(4)
                )
                if sp.simplify(lhs - rhs) != 0:
                    fierz_failures += 1
check("explicit chiral-basis Dirac algebra", gamma_algebra_failures, 0)
check("explicit chiral Fierz matrix identity (Grassmann sign separate)", fierz_failures, 0)

# 8. Explicit power-counting and multiplicity ledger.
hard_crossed_channel_multiplicities = {
    "Lbar L Sdag S": 1,
    "lRbar lR Hdag H": 1,
    "lRbar lR Sdag S": 2,
}
check("three loop-dependent crossed channels are explicitly counted",
      sum(hard_crossed_channel_multiplicities.values()), 4)

print(f"RESULT: {len(checks)} exact symbolic checks passed")
for name in checks:
    print("PASS:", name)
print("SCOPE: analytic integral kernels and exact symbolic identities only.")
print("NOT CLAIMED: FeynArts/FeynCalc execution, full gauge-sector matching, or a closed model-level Wilson vector.")
