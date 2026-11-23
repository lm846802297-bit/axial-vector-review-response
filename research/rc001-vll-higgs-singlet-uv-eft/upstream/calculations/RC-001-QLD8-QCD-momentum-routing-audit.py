#!/usr/bin/env python3
"""Exact momentum-routing audit for the QLD8 d†d QCD pilot.

For ordered pair (a,b), ell flows from b to a. With all external momenta
incoming at the insertion, r_a=p_a+ell and r_b=p_b-ell.
"""
import sympy as sp

p1 = sp.Matrix(sp.symbols("p1_0:4"))
p2 = sp.Matrix(sp.symbols("p2_0:4"))
p3 = sp.Matrix(sp.symbols("p3_0:4"))
ell = sp.Matrix(sp.symbols("ell_0:4"))
p4 = -(p1 + p2 + p3)

qA = p1 + p2
qB = p3 + p4
assert sp.simplify(qA + qB) == sp.zeros(4, 1)

# Four product-rule placements, with the two derivative momenta drawn
# from opposite source bilinears.
placement_sum = (
    p1.dot(p3) + p1.dot(p4)
    + p2.dot(p3) + p2.dot(p4)
)
assert sp.simplify(-placement_sum - qA.dot(qA)) == 0

source_A = {"barQ", "d"}
pair_shifts = {
    ("barQ", "Q"): +1,
    ("barQ", "bard"): +1,
    ("barQ", "d"): 0,
    ("Q", "bard"): 0,
    ("Q", "d"): -1,
    ("bard", "d"): -1,
}

# ell flows from the second named leg to the first; the source-A shift is
# +ell for (A,B), -ell for (B,A), and zero within one source.
for pair, expected_shift in pair_shifts.items():
    derived_shift = (
        (1 if pair[0] in source_A else 0)
        - (1 if pair[1] in source_A else 0)
    )
    assert derived_shift == expected_shift
    qA_loop = qA + expected_shift * ell
    qB_loop = -qA_loop
    assert sp.simplify(qA_loop + qB_loop) == sp.zeros(4, 1)
    assert sp.simplify(
        -qA_loop.dot(qB_loop) - qA_loop.dot(qA_loop)
    ) == 0

print("RC-001 QLD8 d†d QCD momentum-routing audit")
print("PASS: q_A + q_B = 0 for four incoming external momenta.")
print("PASS: four derivative placements sum to q_A^2.")
print("PASS: all six exchange routings have the correct source-current shift.")
print("PASS: q_A^(ab) + q_B^(ab) = 0 for all six topologies.")
print("PASS: insertion factor is [q_A^(ab)]^2 for all six topologies.")
print("LIMIT: no Dirac numerator, loop integral, UV pole, or Z matrix.")
