#!/usr/bin/env python3
"""Exact Gram-matrix checks for the symmetric nonexceptional four-point point."""
import sympy as sp

mu2 = sp.symbols("mu_IR2", positive=True)
G3 = mu2*sp.Matrix([
    [1, -sp.Rational(1,3), -sp.Rational(1,3)],
    [-sp.Rational(1,3), 1, -sp.Rational(1,3)],
    [-sp.Rational(1,3), -sp.Rational(1,3), 1],
])


def checks():
    # p4 = -(p1+p2+p3)
    p4_sq = sum(G3[i,j] for i in range(3) for j in range(3))
    p4_dots = [-sum(G3[i,j] for j in range(3)) for i in range(3)]
    eigenvalues = sorted(
        [sp.simplify(v/mu2) for v in G3.eigenvals().keys()],
        key=sp.default_sort_key,
    )
    return {
        "p4_on_shell_offshell_norm": sp.simplify(p4_sq-mu2),
        "p4_pairwise_dot": [sp.simplify(v+mu2/3) for v in p4_dots],
        "determinant": sp.simplify(G3.det()-sp.Rational(16,27)*mu2**3),
        "eigenvalues": eigenvalues,
        "two_particle_channel": sp.simplify(2*mu2+2*(-mu2/3)),
    }


def main():
    r = checks()
    assert r["p4_on_shell_offshell_norm"] == 0
    assert all(v == 0 for v in r["p4_pairwise_dot"])
    assert r["determinant"] == 0
    assert r["two_particle_channel"] == sp.Rational(4,3)*mu2
    print("PASS: p1+p2+p3+p4=0 is consistent with all four p_i^2=mu_IR^2.")
    print("PASS: all six pairwise dot products equal -mu_IR^2/3.")
    print("PASS: det G_(p1,p2,p3)=16 mu_IR^6/27.")
    print("PASS: all two-particle channels have invariant 4 mu_IR^2/3.")
    print("Gram eigenvalues of G3/mu_IR^2: 1/3, 4/3, 4/3.")
    print("BOUNDARY: kinematics only; no loop tensor projector or matching integral is evaluated.")


if __name__ == "__main__":
    main()
