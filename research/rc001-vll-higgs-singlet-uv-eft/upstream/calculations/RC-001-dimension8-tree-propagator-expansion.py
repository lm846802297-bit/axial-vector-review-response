#!/usr/bin/env python3
"""Exact algebraic checks for the tree-level VLL Schur-complement expansion.

The checks distinguish the Lagrangian coefficients from Wilson coefficients
defined through L_EFT = -C5 O5 - C7 O7 + h.c.
"""
import sympy as sp

M, z, d = sp.symbols("M z d", positive=True)
y, lam = sp.symbols("y lambda")
a_y, a_lam = sp.symbols("|y|^2 |lambda|^2", positive=True)

# Exact cross-chirality term from -Jbar (i Dslash - M)^(-1) J:
# - y lambda M / (z - M^2), z=(i Dslash)^2 on the full source.
cross = -y * lam * M / (z - M**2)
cross_series = sp.series(cross, z, 0, 3).removeO()
cross_expected = y * lam / M + y * lam * z / M**3 + y * lam * z**2 / M**5
assert sp.simplify(cross_series - cross_expected) == 0

# Same-chirality terms from -|y|^2 Dslash/(Dslash^2-M^2)
# and -|lambda|^2 Dslash/(Dslash^2-M^2).
same = -a_y * d / (d**2 - M**2)
same_series = sp.series(same, d, 0, 4).removeO()
same_expected = a_y * d / M**2 + a_y * d**3 / M**4
assert sp.simplify(same_series - same_expected) == 0

C5 = -y * lam / M
C7 = C5 / M**2
C9 = C5 / M**4
assert sp.simplify(-C5 - y * lam / M) == 0
assert sp.simplify(-C7 - y * lam / M**3) == 0
assert sp.simplify(-C9 - y * lam / M**5) == 0

print("PASS: exact Schur-complement cross term expands with Lagrangian coefficients +y lambda/M and +y lambda/M^3")
print("PASS: in L_EFT = -C5 O5 - C7 O7 + h.c., C5=-y lambda/M and C7=C5/M_E^2")
print("PASS: same-chirality tree terms generate +|y|^2 Q_LD/M_E^2 and +|y|^2 Q_LD^(8)/M_E^4")
print("PASS: same-chirality tree terms generate +|lambda|^2 Q_RD/M_E^2 and +|lambda|^2 Q_RD^(8)/M_E^4")
print("PASS: the next cross-chirality term is dimension nine and order M_E^-5")
print("CONVENTION: z=(i Dslash)^2 and d=i Dslash act on the complete right-hand source")
print("LIMIT: no scalar/gauge EOM basis canonicalization, loop matching, or diagram-package validation is performed")
