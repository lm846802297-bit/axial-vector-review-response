#!/usr/bin/env python3
"""Charge-compatible attachment-class census for RC-001 dimension-six gauge matching.

This is a structural generator, not a Feynman-diagram generator or loop integrator. The dedicated GitHub Actions workflow runs it and compares its stdout with the checked-in validation artifact.
It enumerates all unordered pairs among the four external line types and the
internal heavy E line, with exact hypercharge, normalized X-charge, SU(2)
representation, and mixed B-A' charge factor.
"""
from fractions import Fraction
from itertools import combinations

def F(n, d=1):
    return Fraction(n, d)

def fmt(v):
    if isinstance(v, Fraction):
        if v.denominator == 1:
            return str(v.numerator)
        return f"{v.numerator}/{v.denominator}"
    return str(v)

def build_ld(eta):
    return {
        "E": {"Y": F(-1), "X": F(eta), "W": False},
        "Lbar": {"Y": F(1,2), "X": F(-eta), "W": True},
        "L": {"Y": F(-1,2), "X": F(eta), "W": True},
        "Hbar": {"Y": F(-1,2), "X": F(0), "W": True},
        "H": {"Y": F(1,2), "X": F(0), "W": True},
    }

def build_rd(eta):
    return {
        "E": {"Y": F(-1), "X": F(eta), "W": False},
        "lbar": {"Y": F(1), "X": F(eta), "W": False},
        "l": {"Y": F(-1), "X": F(-eta), "W": False},
        "Sbar": {"Y": F(0), "X": F(-2*eta), "W": False},
        "S": {"Y": F(0), "X": F(2*eta), "W": False},
    }

def mixed_factor(lines, a, b):
    ca, cb = lines[a], lines[b]
    return ca["Y"] * cb["X"] + ca["X"] * cb["Y"]

def census(lines):
    result = {g: [] for g in ("B", "W", "X", "BX")}
    for a, b in combinations(lines, 2):
        ca, cb = lines[a], lines[b]
        if ca["Y"] * cb["Y"] != 0:
            result["B"].append((a, b, ca["Y"] * cb["Y"]))
        if ca["W"] and cb["W"]:
            result["W"].append((a, b, "T_i.T_j"))
        if ca["X"] * cb["X"] != 0:
            result["X"].append((a, b, ca["X"] * cb["X"]))
        mixed = mixed_factor(lines, a, b)
        if mixed != 0:
            result["BX"].append((a, b, mixed))
    return result

def print_family(label, result):
    print(label)
    for gauge in ("B", "W", "X", "BX"):
        pairs = result[gauge]
        print(f"  {gauge}: {len(pairs)} classes")
        for a, b, coeff in pairs:
            print(f"    {a}-{b}: {fmt(coeff)}")
    print()

def main():
    expected = {
        "Q_LD": {"B": 10, "W": 6, "X": 3, "BX": 9},
        "Q_RD": {"B": 3, "W": 0, "X": 10, "BX": 7},
    }
    for eta, flavor in ((1, "mu"), (-1, "tau")):
        ld = census(build_ld(eta))
        rd = census(build_rd(eta))
        assert {g: len(ld[g]) for g in ld} == expected["Q_LD"]
        assert {g: len(rd[g]) for g in rd} == expected["Q_RD"]
        ldl = build_ld(eta)
        rdl = build_rd(eta)
        assert mixed_factor(ldl, "Hbar", "H") == 0
        assert mixed_factor(rdl, "E", "lbar") == 0
        assert mixed_factor(rdl, "E", "l") == 0
        assert mixed_factor(rdl, "Sbar", "S") == 0
        assert ldl["E"]["Y"] == -1 and ldl["E"]["X"] == eta
        assert rdl["S"]["X"] == 2 * eta and rdl["Sbar"]["X"] == -2 * eta
        print(f"FLAVOR eta={eta} ({flavor})")
        print_family("Q_LD: E,Lbar,L,Hbar,H", ld)
        print_family("Q_RD: E,lbar,l,Sbar,S", rd)
    print("CONTACTS")
    print("  Q_LD: D(Hdagger L) has Y=-1, X=eta, SU(2)=singlet; B and A' contacts, no W contact.")
    print("  Q_RD: D(S_l l_R) has Y=-1, X=eta, SU(2)=singlet; B and A' contacts, no W contact.")
    print("RESULT: attachment-class counts verified for both flavors.")
    print("SCOPE: structural charge/representation census only; no loop integrals or exact Feynman-graph multiplicities.")

if __name__ == "__main__":
    main()
