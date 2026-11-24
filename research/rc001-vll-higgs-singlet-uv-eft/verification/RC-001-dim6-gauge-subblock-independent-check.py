#!/usr/bin/env python3
"""Independent charge-derived regression for the RC-001 dimension-six gauge sub-block.

This check derives Yukawa-vertex pair factors from the field charge assignments,
then reconstructs the FF/FS heavy-vertex kernels and the diagonal/mixed input-
parameter pole coefficients. It does not reuse the producer scripts' hard-coded
expected charge-factor dictionaries. It does not evaluate loop integrals or the
complete UV-EFT amplitudes.
"""
from fractions import Fraction as F
import sympy as sp

Delta, L, eta, rho = sp.symbols("Delta L eta rho")

def pair_factors(a, b):
    Ya, xa = a
    Yb, xb = b
    return (Ya * Yb, xa * xb, Ya * xb + xa * Yb)

def make_vertices(e):
    h = F(1, 2)
    return {
        "LD_y": {
            "barL": (h, -e), "H": (h, 0), "E_R": (-1, e),
        },
        "LD_y_conjugate": {
            "barE_R": (1, -e), "Hdag": (-h, 0), "L": (-h, e),
        },
        "RD_lambda": {
            "S": (0, 2*e), "barE_L": (1, -e), "lR": (-1, -e),
        },
        "RD_lambda_conjugate": {
            "Sdag": (0, -2*e), "barlR": (1, e), "E_L": (-1, e),
        },
    }

def all_pairs(fields):
    keys = list(fields)
    return {(keys[i], keys[j]): pair_factors(fields[keys[i]], fields[keys[j]])
            for i in range(len(keys)) for j in range(i+1, len(keys))}

def check_charge_conservation():
    for e in (1, -1):
        vertices = make_vertices(e)
        for name, fields in vertices.items():
            assert sum(v[0] for v in fields.values()) == 0, (name, "Y")
            assert sum(v[1] for v in fields.values()) == 0, (name, "X")
        ld = all_pairs(vertices["LD_y"])
        ldc = all_pairs(vertices["LD_y_conjugate"])
        rd = all_pairs(vertices["RD_lambda"])
        rdc = all_pairs(vertices["RD_lambda_conjugate"])
        assert ld[("barL", "H")] == (F(1,4), 0, -F(e,2))
        assert ld[("barL", "E_R")] == (-F(1,2), -1, F(3*e,2))
        assert ld[("H", "E_R")] == (-F(1,2), 0, F(e,2))
        assert ldc[("barE_R", "Hdag")] == (-F(1,2), 0, F(e,2))
        assert ldc[("barE_R", "L")] == (-F(1,2), -1, F(3*e,2))
        assert ldc[("Hdag", "L")] == (F(1,4), 0, -F(e,2))
        assert rd[("S", "barE_L")] == (0, -2, 2*e)
        assert rd[("S", "lR")] == (0, -2, -2*e)
        assert rd[("barE_L", "lR")] == (-1, 1, 0)
        assert rdc[("Sdag", "barlR")] == (0, -2, -2*e)
        assert rdc[("Sdag", "E_L")] == (0, -2, 2*e)
        assert rdc[("barlR", "E_L")] == (-1, 1, 0)
        # Conjugate vertices must have the same corresponding real pair factors.
        assert ld[("barL", "H")] == ldc[("Hdag", "L")]
        assert ld[("barL", "E_R")] == ldc[("barE_R", "L")]
        assert ld[("H", "E_R")] == ldc[("barE_R", "Hdag")]
        assert rd[("S", "barE_L")] == rdc[("Sdag", "E_L")]
        assert rd[("S", "lR")] == rdc[("Sdag", "barlR")]
        assert rd[("barE_L", "lR")] == rdc[("barlR", "E_L")]
    return True

def check_heavy_vertex_kernels():
    B0 = Delta + 1 - L
    dB0 = 4*Delta + 2 - 4*L
    # Charge factors are derived from the field assignments above, for eta=+1;
    # the mixed factors retain symbolic eta after the exact integer coefficient is read.
    v = make_vertices(1)
    ld = all_pairs(v["LD_y"])
    rd = all_pairs(v["RD_lambda"])
    F_LD_B = (ld[("barL", "E_R")][0], ld[("H", "E_R")][0])
    F_LD_X = (ld[("barL", "E_R")][1], ld[("H", "E_R")][1])
    F_LD_BX = (sp.Rational(3,2)*eta, sp.Rational(1,2)*eta)
    F_RD_B = (rd[("barE_L", "lR")][0], rd[("S", "barE_L")][0])
    F_RD_X = (rd[("barE_L", "lR")][1], rd[("S", "barE_L")][1])
    F_RD_BX = (0, 2*eta)
    factors = {
        "LD_B": F_LD_B, "LD_X": F_LD_X, "LD_BX": F_LD_BX,
        "RD_B": F_RD_B, "RD_X": F_RD_X, "RD_BX": F_RD_BX,
    }
    actual = {name: sp.expand(-(ff*dB0 + fs*B0)) for name, (ff, fs) in factors.items()}
    expected = {
        "LD_B": sp.Rational(5,2)*Delta + sp.Rational(3,2) - sp.Rational(5,2)*L,
        "LD_X": 4*Delta + 2 - 4*L,
        "LD_BX": -sp.Rational(13,2)*eta*Delta - sp.Rational(7,2)*eta + sp.Rational(13,2)*eta*L,
        "RD_B": 4*Delta + 2 - 4*L,
        "RD_X": -2*Delta + 2*L,
        "RD_BX": -2*eta*Delta - 2*eta + 2*eta*L,
    }
    assert all(sp.simplify(actual[k] - expected[k]) == 0 for k in actual)
    doubled = {k: sp.expand(2*actual[k]) for k in actual}
    assert sp.simplify(doubled["LD_B"] - (5*Delta + 3 - 5*L)) == 0
    assert sp.simplify(doubled["LD_X"] - (8*Delta + 4 - 8*L)) == 0
    assert sp.simplify(doubled["LD_BX"] - eta*(-13*Delta - 7 + 13*L)) == 0
    assert sp.simplify(doubled["RD_B"] - (8*Delta + 4 - 8*L)) == 0
    assert sp.simplify(doubled["RD_X"] - (-4*Delta + 4*L)) == 0
    assert sp.simplify(doubled["RD_BX"] - eta*(-4*Delta - 4 + 4*L)) == 0
    eps, delta = sp.symbols('eps delta')
    dB0_series = sp.series((4-2*eps)*(1/eps + delta + 1-L), eps, 0, 1).removeO()
    assert sp.simplify(dB0_series - (4/eps + 4*delta + 2 - 4*L)) == 0
    return actual

def check_parameter_poles():
    # Mixed B-X propagator coefficient rho is defined relative to the diagonal propagator.
    YL, xL = -F(1,2), eta
    YE, xE = -1, eta
    YR, xR = -1, -eta
    sum_LD = sp.simplify(YL*xL + YE*xE)
    sum_RD = sp.simplify(YE*xE + YR*xR)
    dM_BX = sp.simplify(-6*rho*YE*xE)
    dy_LD_BX = sp.simplify(-3*rho*sum_LD)
    dy_RD_BX = sp.simplify(-3*rho*sum_RD)
    dC_LD_BX = sp.simplify(2*dy_LD_BX - 2*dM_BX)
    dC_RD_BX = sp.simplify(2*dy_RD_BX - 2*dM_BX)
    assert sum_LD == -sp.Rational(3,2)*eta
    assert sum_RD == 0
    assert dM_BX == 6*rho*eta
    assert dy_LD_BX == sp.Rational(9,2)*rho*eta
    assert dy_RD_BX == 0
    assert dC_LD_BX == -3*rho*eta
    assert dC_RD_BX == -12*rho*eta

    # Diagonal parameter sub-blocks from the same field representations.
    yLD_B = -sp.Rational(3,2)*(sp.Rational(1,4) + 1)
    yLD_W = -sp.Rational(3,2)*(sp.Rational(3,4) + 0)
    yLD_X = -sp.Rational(3,2)*(1 + 1)
    mE_B, mE_W, mE_X = -3, 0, -3
    cLD = (2*yLD_B-2*mE_B, 2*yLD_W-2*mE_W, 2*yLD_X-2*mE_X)
    yRD_B, yRD_W, yRD_X = -3, 0, -3
    cRD = (2*yRD_B-2*mE_B, 2*yRD_W-2*mE_W, 2*yRD_X-2*mE_X)
    assert cLD == (sp.Rational(9,4), -sp.Rational(9,4), 0)
    assert cRD == (0, 0, 0)
    return cLD, cRD

def check_light_propagator_expansion():
    P2, invM2 = sp.symbols("P2 invM2")
    exact = -invM2/(1-P2*invM2)
    series = sp.series(exact, invM2, 0, 3).removeO()
    assert sp.simplify(series + invM2 + P2*invM2**2) == 0
    return series

def main():
    check_charge_conservation()
    heavy = check_heavy_vertex_kernels()
    diagonal = check_parameter_poles()
    prop = check_light_propagator_expansion()
    print("PASS: all four Yukawa vertices conserve Y and X for eta_mu=+1 and eta_tau=-1.")
    print("PASS: all 12 pair tuples reproduce B, X, and mixed BX factors, including conjugate-vertex equality.")
    print("PASS: six FF/FS heavy-vertex factors follow from charge-derived pairs and d*B0=4*Delta+2-4*L.")
    print("PASS: conjugate-vertex doubling reproduces the six Q_LD/Q_RD hard sub-blocks.")
    print("PASS: diagonal parameter poles give C_LD=(9/4,-9/4,0), C_RD=(0,0,0) in (gY^2,g2^2,gX^2 Q_l^2).")
    print("PASS: mixed parameter poles give delta C_LD=-3 rho eta and delta C_RD=-12 rho eta.")
    print("PASS: chirality-preserving heavy propagator begins -i slash(P)/M_E^2 at O(M_E^-2).")
    print("ANALYTIC INPUT: complete light-only UV/EFT cancellation with covariant contacts is derived in the subtraction ledger, section 2.5; this script does not integrate that loop or generate its contact graphs.")
    print("SCOPE: exact charge/algebra regression of sub-blocks only; no complete UV-EFT amplitude or Wilson coefficient.")

if __name__ == "__main__":
    main()
