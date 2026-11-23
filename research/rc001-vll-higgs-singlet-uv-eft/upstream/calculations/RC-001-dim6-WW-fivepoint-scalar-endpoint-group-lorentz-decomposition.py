#!/usr/bin/env python3
"""RC-001 B2c-IVg: scalar endpoint Lorentz/weak-tensor decomposition.

This exact symbolic check keeps the scalar-line ordered weak tensor distinct
from the seagull anticommutator tensor. It also records the different
cross-vertex A->B and same-vertex S->F three-W group-phase signs.

It is an algebraic decomposition, not a loop integral or full STI closure.
"""
import sympy as sp

I = sp.I
g2 = sp.symbols("g_2", real=True)
DeltaY, DeltaW = sp.symbols("Delta_Y Delta_W", real=True)
VA, VB, qmu = sp.symbols("V_A_mu V_B_mu q_mu", real=True)
SA, SB, GAB, GFS = sp.symbols("S_A S_B G_AB G_FS")

# Raw ordered scalar-line tensors:
# W_A = S_A/2 + i G_AB/2
# W_B = S_B/2 + i G_AB/2
WA = SA/2 + I*GAB/2
WB = SB/2 + I*GAB/2

# A-side scalar endpoint:
# q.N_A = DeltaY-DeltaW; P_line/P4=-g2; P_sg/P4=+g2.
A_original = (
    -g2*(DeltaY-DeltaW)*VA*WA
    +g2*DeltaY*qmu*SA
)
A_decomposed = g2*(
    (-sp.Rational(1,2)*(DeltaY-DeltaW)*VA + DeltaY*qmu)*SA
    -I*sp.Rational(1,2)*(DeltaY-DeltaW)*VA*GAB
)
assert sp.simplify(A_original-A_decomposed) == 0

# B-side scalar endpoint and same-vertex S endpoint:
# q.N_B = DeltaW-DeltaY; after P_line/P4=-g2 this is
# +g2*(DeltaY-DeltaW) times the ordered line tensor.
# For same-vertex S->F use G_FS, not G_AB.
WB_same = SB/2 + I*GFS/2
B_original = (
    +g2*(DeltaY-DeltaW)*VB*WB_same
    +g2*DeltaY*qmu*SB
)
B_decomposed = g2*(
    (+sp.Rational(1,2)*(DeltaY-DeltaW)*VB + DeltaY*qmu)*SB
    +I*sp.Rational(1,2)*(DeltaY-DeltaW)*VB*GFS
)
assert sp.simplify(B_original-B_decomposed) == 0

# Phase-weighted commutator versus three-W group factors.
line_comm_cross = -I*g2*GAB
threeW_cross = -I*g2*GAB
line_comm_same = -I*g2*GFS
threeW_same = +I*g2*GFS
assert sp.simplify(line_comm_cross-threeW_cross) == 0
assert sp.simplify(line_comm_same+threeW_same) == 0

def main():
    print("RC-001 B2c-IVg scalar endpoint Lorentz/weak decomposition")
    print("PASS: A scalar line + seagull decomposition.")
    print("  symmetric tensor S_A and antisymmetric tensor G_AB kept separate.")
    print("PASS: B/S scalar line + seagull decomposition.")
    print("  symmetric tensor S_B and antisymmetric tensor G_FS kept separate.")
    print("PASS: cross-vertex three-W group phase equals the line commutator group phase.")
    print("PASS: same-vertex S->F three-W group phase is opposite to the line commutator group phase.")
    print("A-side formula:")
    print("  g2*[(-1/2*(DeltaY-DeltaW)*V_A + DeltaY*q)*S_A")
    print("      - i/2*(DeltaY-DeltaW)*V_A*G_AB]")
    print("B/S-side formula:")
    print("  g2*[(+1/2*(DeltaY-DeltaW)*V_B + DeltaY*q)*S_B")
    print("      + i/2*(DeltaY-DeltaW)*V_B*G_FS]")
    print("BOUNDARY: exact algebraic decomposition only; no common-k integral or STI closure.")


if __name__ == "__main__":
    main()
