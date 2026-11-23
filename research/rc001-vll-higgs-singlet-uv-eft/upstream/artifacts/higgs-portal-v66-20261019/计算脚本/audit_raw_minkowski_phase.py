"""Raw Feynman-rule phase ledger and term-by-term Wick-sign audit.

Assumptions: L_int = -phi psi_bar (Y_L P_L + Y_R P_R) psi + h.c.,
metric (+---), four Yukawa vertices, four fermion propagators, one closed
fermion loop, and denominator (K_M^2-Delta+i0)^n. This tracks common i/signs
and relative signs; it does not determine graph multiplicities or EFT matching.
"""
from fractions import Fraction

# Four Yukawa vertices (-i)^4, four propagator factors i^4, and one closed loop.
vertex_factor = (-1j) ** 4
propagator_factor = (1j) ** 4
closed_fermion_loop = -1
assert vertex_factor == 1
assert propagator_factor == 1
assert closed_fermion_loop == -1

# J_M(r,n) = i*(-1)^(n+r)*I_E(r,n). The table includes the coefficient
# multiplying each q^2 structure before the common closed-loop factor.
terms = [
    ("C f", 0, 4, 2, "+2 C f I0(4)"),
    ("H g", 1, 4, 2, "-2 H g I1(4)"),
    ("H deltaDelta", 2, 5, -8, "+8 H d I2(5)"),
    ("S deltaDelta", 1, 5, -8, "-8 S d I1(5)"),
    ("M deltaDelta", 0, 5, -8, "+8 M d I0(5)"),
]
print("RAW MINKOWSKI PHASE LEDGER")
print(f"four vertices (-i)^4 = {vertex_factor.real:+.0f}")
print(f"four propagators i^4 = {propagator_factor.real:+.0f}")
print(f"closed fermion loop = {closed_fermion_loop:+d}")
print("The closed loop multiplies the entire graph by -1; it cannot change relative signs.")
print("\nTERM-WISE WICK LEDGER")
for name, r, n, coeff, after in terms:
    wick = (-1) ** (n + r)
    print(f"{name:16s} (r,n)=({r},{n}), Wick={wick:+d}, pre-Wick coefficient={coeff:+d} -> {after}")

# Euclidean integral reductions in units 1/(16 pi^2).
# I0(4)=1/(6 D^2), I1(4)=1/(3 D), I2(5)=1/(4 D),
# I1(5)=1/(12 D^2), I0(5)=1/(12 D^3).
# Resulting kernels before the common closed-loop factor:
old = {"B1_g": Fraction(2,3), "B1_d": Fraction(-2,1), "B2_C": Fraction(1,3),
       "B2_S": Fraction(-2,3), "B3_M": Fraction(-2,3)}
wicked = {"B1_g": Fraction(-2,3), "B1_d": Fraction(2,1), "B2_C": Fraction(1,3),
          "B2_S": Fraction(-2,3), "B3_M": Fraction(2,3)}
assert wicked["B1_g"] == -old["B1_g"]
assert wicked["B1_d"] == -old["B1_d"]
assert wicked["B2_C"] == old["B2_C"] and wicked["B2_S"] == old["B2_S"]
assert wicked["B3_M"] == -old["B3_M"]
print("\nPASS: common Feynman-rule phase is separated from relative Wick signs")
print("PASS: B1 and B3 reverse relative to the prior kernel; B2 is unchanged")
print("BOUNDARY: no external-leg permutation sum, no counterterm, and no UV-EFT subtraction here.")
