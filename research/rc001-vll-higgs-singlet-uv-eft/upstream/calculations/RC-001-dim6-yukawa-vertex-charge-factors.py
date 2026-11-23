#!/usr/bin/env python3
"""Exact rational checks for signed charge factors at RC-001 Yukawa vertices."""
from fractions import Fraction

def factors(a, b):
    Ya, xa = a
    Yb, xb = b
    return (Ya * Yb, xa * xb, Ya * xb + xa * Yb)

def check_vertex(name, fields, expected, eta):
    assert sum(v[0] for v in fields.values()) == 0, f"{name}: hypercharge not conserved"
    assert sum(v[1] for v in fields.values()) == 0, f"{name}: X charge not conserved"
    keys = list(fields)
    actual = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            pair = (keys[i], keys[j])
            actual[pair] = factors(fields[pair[0]], fields[pair[1]])
    for pair, base in expected.items():
        y, x, bx_eta = base
        want = (y, x, bx_eta * eta)
        assert actual[pair] == want, f"{name} {pair}: {actual[pair]} != {want}"

def run_for_eta(eta):
    half = Fraction(1, 2)
    LD_y = {
        "barL": (half, -eta), "H": (half, 0), "E_R": (-1, eta)
    }
    check_vertex("LD_y", LD_y, {
        ("barL", "H"): (Fraction(1,4), 0, Fraction(-1,2)),
        ("barL", "E_R"): (Fraction(-1,2), -1, Fraction(3,2)),
        ("H", "E_R"): (Fraction(-1,2), 0, Fraction(1,2)),
    }, eta)

    LD_yc = {
        "barE_R": (1, -eta), "Hdag": (-half, 0), "L": (-half, eta)
    }
    check_vertex("LD_y_conjugate", LD_yc, {
        ("barE_R", "Hdag"): (Fraction(-1,2), 0, Fraction(1,2)),
        ("barE_R", "L"): (Fraction(-1,2), -1, Fraction(3,2)),
        ("Hdag", "L"): (Fraction(1,4), 0, Fraction(-1,2)),
    }, eta)

    RD_lam = {
        "S": (0, 2*eta), "barE_L": (1, -eta), "lR": (-1, -eta)
    }
    check_vertex("RD_lambda", RD_lam, {
        ("S", "barE_L"): (0, -2, 2),
        ("S", "lR"): (0, -2, -2),
        ("barE_L", "lR"): (-1, 1, 0),
    }, eta)

    RD_lamc = {
        "Sdag": (0, -2*eta), "barlR": (1, eta), "E_L": (-1, eta)
    }
    check_vertex("RD_lambda_conjugate", RD_lamc, {
        ("Sdag", "barlR"): (0, -2, -2),
        ("Sdag", "E_L"): (0, -2, 2),
        ("barlR", "E_L"): (-1, 1, 0),
    }, eta)

def main():
    run_for_eta(+1)
    run_for_eta(-1)
    print("Yukawa-vertex charge conservation: PASS for mu and tau")
    print("All 12 pair tuples (36 exact B, X, and mixed BX factor entries): PASS")
    print("Mixed BX fermion-pair zeros in RD vertices: PASS")
    print("SCOPE: charge-factor algebra only; no loop amplitudes or Wilson coefficients.")

if __name__ == "__main__":
    main()
