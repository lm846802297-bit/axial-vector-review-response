"""Labelled h h s s cyclic-order audit for the current fixed-routing coefficients.

This helper does two things:
  1. Enumerates the 6 cyclic classes of four DISTINCT labelled external legs.
  2. Applies momentum-conservation transformations to the six Q invariants and
     sums the already-computed fixed-routing coefficient vectors at r=1 and r=2.

Important: the input coefficient vectors are copied from document sections 71.3
and 72.3. The aggregate is a bookkeeping/projection check only; it does NOT
supply the still-unverified overall Minkowski loop sign or replace the EFT match.
Requires: sympy.
"""
from itertools import permutations
import sympy as sp

Q1, Q2, Q3, Q12, Q13, Q23 = sp.symbols("Q1 Q2 Q3 Q12 Q13 Q23")
Q = [Q1, Q2, Q3, Q12, Q13, Q23]
# Baseline labelled momenta: p1=h1, p2=h2, p3=s1, p4=s2=-(p1+p2+p3).
P = {
    1: sp.Matrix([1, 0, 0]),
    2: sp.Matrix([0, 1, 0]),
    3: sp.Matrix([0, 0, 1]),
    4: sp.Matrix([-1, -1, -1]),
}

def dot(v, w):
    return sp.expand(
        v[0]*w[0]*Q1 + v[1]*w[1]*Q2 + v[2]*w[2]*Q3
        + (v[0]*w[1] + v[1]*w[0])*Q12
        + (v[0]*w[2] + v[2]*w[0])*Q13
        + (v[1]*w[2] + v[2]*w[1])*Q23
    )

def square(v):
    return dot(v, v)

def invariant_map(momentum_order):
    """Return rows M so Q'_alpha = sum_beta M[alpha,beta] Q_beta."""
    q = [P[label] for label in momentum_order[:3]]
    exprs = [square(q[0]), square(q[1]), square(q[2]),
             dot(q[0], q[1]), dot(q[0], q[2]), dot(q[1], q[2])]
    return sp.Matrix([[sp.expand(e).coeff(v) for v in Q] for e in exprs])

# Fix h1 as the first leg in each cycle, then permute the remaining labels.
# For the two hssh cycles, rotate the trace cyclically to canonical hhss order;
# this changes the momentum ordering but not the cyclic trace.
cyclic_classes = [
    ("hhss", (1, 2, 3, 4)),
    ("hhss", (1, 2, 4, 3)),
    ("hshs", (1, 3, 2, 4)),
    ("hhss", (2, 1, 3, 4)),  # cyclic rotation of (1,3,4,2)
    ("hshs", (1, 4, 2, 3)),
    ("hhss", (2, 1, 4, 3)),  # cyclic rotation of (1,4,3,2)
]

# Fixed-route coefficient vectors copied from the current document; order is
# (Q1,Q2,Q3,Q12,Q13,Q23), with m2=1 and the document's fixed mixing point.
C = {
    ("hshs", "r=1"): [-4.12295581519481e-5, -5.49727442025973e-5,
                         -4.12295581519481e-5, -5.49727442025973e-5,
                         -2.74863721012987e-5, -5.49727442025973e-5],
    ("hhss", "r=1"): [1.20899653227935e-5, -1.61611791152080e-4,
                         -1.21208843364060e-4, -2.83129824652266e-5,
                          5.24929131108135e-5, -2.94910599838934e-4],
    ("hshs", "r=2"): [3.19838438215421e-5, 4.19545426906868e-5,
                         3.19838438215421e-5, 4.19545426906868e-5,
                         2.20131449523975e-5, 4.19545426906868e-5],
    ("hhss", "r=2"): [-9.03227109231993e-5, -1.51461546715154e-4,
                        -9.07910076075895e-5, -1.44061399053701e-4,
                        -2.96521718156351e-5, -1.51929843399544e-4],
}

def main():
    print("Six cyclic classes for labelled (h1,h2,s1,s2):")
    for i, (order, perm) in enumerate(cyclic_classes, 1):
        print(f"{i}. type={order:4s}, momentum order={perm}")
        print("   Q' map rows:")
        M = invariant_map(perm)
        for row in M.tolist():
            print("    ", row)
    for ratio in ("r=1", "r=2"):
        total = sp.zeros(6, 1)
        for order, perm in cyclic_classes:
            vec = sp.Matrix(C[(order, ratio)])
            total += invariant_map(perm).T * vec
        print(f"\nProvisional aggregate in baseline Q basis at {ratio}:")
        for q, val in zip(Q, total):
            print(f"  {q}: {float(val):.14e}")
        print("NOTE: bookkeeping projection only; no final Minkowski sign / EFT subtraction.")

if __name__ == "__main__":
    main()
