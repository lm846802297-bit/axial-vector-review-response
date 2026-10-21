"""Audit Wick-rotation signs for loop integrals with K^(2r) numerators.
Convention: metric (+---), denominators (K_M^2-Delta+i0)^n, and positive Euclidean
integrals I_E(r,n)=int d^4K_E/(2pi)^4 (K_E^2)^r/(K_E^2+Delta)^n.
This audits relative signs only; external-vertex and graph multiplicity conventions must
still be stated in the amplitude definition.
"""
from fractions import Fraction

# I_M(r,n) = i*(-1)^(n+r) I_E(r,n)
items = [
    ("C_ij f_ij", 0, 4, "numerator t_i.t_j; no shifted-loop K"),
    ("H g", 1, 4, "four-slash term with one K^2 after angular averaging"),
    ("H d", 2, 5, "-4 deltaDelta times zero-order H K^4"),
    ("S d", 1, 5, "-4 deltaDelta times zero-order S K^2"),
    ("M d", 0, 5, "-4 deltaDelta times zero-order mass term M"),
]
print("Term | r | n | Wick factor J_M/(i J_E) | coefficient before common closed-loop factor")
for name,r,n,desc in items:
    sign = (-1)**(r+n)
    if name == "C_ij f_ij": coeff = "+2 C f I_0^(4)"
    elif name == "H g": coeff = "-2 H g I_1^(4)"
    elif name == "H d": coeff = "+8 H d I_2^(5)"
    elif name == "S d": coeff = "-8 S d I_1^(5)"
    else: coeff = "+8 M d I_0^(5)"
    print(f"{name} | {r} | {n} | {sign:+d} | {coeff}")

# Using I_E values from the cumulative derivation, derive B coefficients before
# the common closed-fermion-loop prefactor. The common i is factored out.
# I0^4=1/(6 D^2), I1^4=1/(3 D), I2^5=1/(4 D), I1^5=1/(12 D^2), I0^5=1/(12 D^3).
# Coefficients are in units 1/(16 pi^2).
print("\nDerived kernel before common closed-loop factor:")
print("B1 = H*(-2/3*g + 2*d)")
print("B2 = (1/3)*sum(C_ij*f_ij) - (2/3)*S*d")
print("B3 = +(2/3)*M*d")
print("Compare with prior B definitions: B1_prior=H*(+2/3*g - 2*d), B2_prior same, B3_prior=-(2/3)*M*d")
print("CONCLUSION: under the explicitly stated Minkowski convention, the prior B1 and B3 are opposite in sign to the Wick-rotated kernel; B2 is unchanged. Recheck external momentum continuation and numerator convention before adopting as a physical correction.")
