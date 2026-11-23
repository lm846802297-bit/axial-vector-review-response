#!/usr/bin/env python3
"""Independent explicit 4D Dirac-matrix check of the nonexceptional hard kernels.

This implementation starts from the four unshifted numerator chains, expands
them to first order in the external momenta, and performs Euclidean angular
averages directly on their polynomial components. It checks the d=4 limit of
the analytic d-dimensional hard-kernel table; it does not validate O(epsilon)
terms or generate the complete diagram set.
"""
import sympy as sp

I = sp.I
pauli = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
zero, eye = sp.zeros(2), sp.eye(2)
GAMMA = (
    sp.BlockMatrix([[zero, -I*pauli[0]], [I*pauli[0], zero]]).as_explicit(),
    sp.BlockMatrix([[zero, -I*pauli[1]], [I*pauli[1], zero]]).as_explicit(),
    sp.BlockMatrix([[zero, -I*pauli[2]], [I*pauli[2], zero]]).as_explicit(),
    sp.BlockMatrix([[zero, eye], [eye, zero]]).as_explicit(),
)
GAMMA5 = GAMMA[0]*GAMMA[1]*GAMMA[2]*GAMMA[3]
P_L = (sp.eye(4)-GAMMA5)/2
P_R = (sp.eye(4)+GAMMA5)/2
K = sp.symbols("k0:4")
T = sp.symbols("t")


def vadd(*vectors):
    return [sp.expand(sum(v[i] for v in vectors)) for i in range(4)]


def vscale(c, vector):
    return [sp.expand(c*x) for x in vector]


def vsub(a, b):
    return [sp.expand(a[i]-b[i]) for i in range(4)]


def vdot(a, b):
    return sp.expand(sum(a[i]*b[i] for i in range(4)))


def slash(vector):
    return sum((vector[i]*GAMMA[i] for i in range(4)), sp.zeros(4))


def symmetric_momenta():
    p1 = [sp.Integer(1), 0, 0, 0]
    p2 = [-sp.Rational(1,3), 2*sp.sqrt(2)/3, 0, 0]
    p3 = [-sp.Rational(1,3), -sp.sqrt(2)/3, sp.sqrt(sp.Rational(2,3)), 0]
    p4 = vscale(-1, vadd(p1, p2, p3))
    return p1, p2, p3, p4


def numerator(pair, momenta):
    p1, p2, p3, p4 = momenta
    k = list(K)
    qE = vsub(k, vadd(p1, p2))
    qbar = vsub(p1, k)
    qL = vadd(k, p4)
    if pair == "01":
        result = sp.zeros(4)
        for mu in range(4):
            result += GAMMA[mu]*slash(qbar)*slash(qE)*slash(qL)*GAMMA[mu]
    elif pair == "02":
        result = -slash(vadd(vscale(2,p3),k))*slash(qbar)*slash(qE)
    elif pair == "05":
        result = slash(vsub(vscale(2,p2),k))*slash(qE)*slash(qL)
    elif pair == "06":
        result = -vdot(vadd(vscale(2,p3),k),vsub(vscale(2,p2),k))*slash(qE)
    else:
        raise ValueError(pair)
    return result.applyfunc(sp.expand)


def angular_average(expression, rank):
    polynomial = sp.Poly(sp.expand(expression), *K)
    result = 0
    for exponents, coefficient in polynomial.terms():
        indices = []
        for index, power in enumerate(exponents):
            indices.extend([index]*power)
        if len(indices) != rank:
            if coefficient != 0:
                raise AssertionError((rank, indices))
            continue
        if rank == 2:
            factor = sp.Rational(1,4) if indices[0] == indices[1] else 0
        elif rank == 4:
            i,j,k,l = indices
            pairings = int(i==j and k==l)+int(i==k and j==l)+int(i==l and j==k)
            factor = sp.Rational(pairings,24)
        else:
            raise ValueError(rank)
        result += coefficient*factor
    return sp.simplify(result)


def average_matrix(matrix, rank):
    return matrix.applyfunc(lambda e: angular_average(e,rank))


def chiral_vector(matrix):
    return [
        sp.simplify(sp.trace(GAMMA[mu]*P_R*matrix*P_L)/2)
        for mu in range(4)
    ]


def basis_coefficients(vector, momenta):
    p1,p2,p3,_ = momenta
    c1,c2,c3 = sp.symbols("c1 c2 c3")
    solution = sp.solve(
        [c1*p1[i]+c2*p2[i]+c3*p3[i]-vector[i] for i in range(3)],
        (c1,c2,c3), dict=True
    )
    assert len(solution)==1
    return [sp.simplify(solution[0][c]) for c in (c1,c2,c3)]


def hard_kernels_4d(pair, momenta):
    p1,p2,p3,p4 = momenta
    shifts = {
        "01": (vscale(-1,p1),p4),
        "02": (vscale(-1,p1),p3),
        "05": (vscale(-1,p2),p4),
        "06": (vscale(-1,p2),p3),
    }
    a,b = shifts[pair]
    c = vscale(-1,vadd(p1,p2))
    scaled = tuple(vscale(T,p) for p in momenta)
    n = numerator(pair,scaled)
    n0 = n.applyfunc(lambda e: sp.expand(e.subs(T,0)))
    n1 = n.applyfunc(lambda e: sp.expand(sp.diff(e,T).subs(T,0)))
    dot_a = sum(K[i]*a[i] for i in range(4))
    dot_b = sum(K[i]*b[i] for i in range(4))
    dot_c = sum(K[i]*c[i] for i in range(4))
    c1 = average_matrix(n1,2)
    c4a = average_matrix(n0.applyfunc(lambda e: sp.expand(e*dot_a)),4)
    c4b = average_matrix(n0.applyfunc(lambda e: sp.expand(e*dot_b)),4)
    c4c = average_matrix(n0.applyfunc(lambda e: sp.expand(e*dot_c)),4)
    # Radial integrals are J for the first three terms and K for the heavy shift.
    j_matrix = c1-2*(c4a+c4b)
    k_matrix = -2*c4c
    return (
        basis_coefficients(chiral_vector(j_matrix),momenta),
        basis_coefficients(chiral_vector(k_matrix),momenta),
    )


def main():
    momenta = symmetric_momenta()
    expected = {
        "01": ([-1,0,-1],[1,1,0]),
        "02": ([0,-1,sp.Rational(3,2)],[sp.Rational(1,2),sp.Rational(1,2),0]),
        "05": ([0,sp.Rational(3,2),sp.Rational(1,2)],[-sp.Rational(1,2),-sp.Rational(1,2),0]),
        "06": ([-1,-1,0],[sp.Rational(1,2),sp.Rational(1,2),0]),
    }
    for pair in ("01","02","05","06"):
        got = hard_kernels_4d(pair,momenta)
        assert got == expected[pair], (pair,got,expected[pair])
        print(f"PASS LD-W-{pair}: J={got[0]}, K={got[1]}")
    print("PASS: explicit 4D Dirac matrices reproduce all d=4 nonexceptional pair kernels.")
    print("BOUNDARY: this does not validate O(epsilon) terms or complete diagram multiplicities.")


if __name__ == "__main__":
    main()
