#!/usr/bin/env python3
"""B5-1: full one-loop UV beta function for the Higgs-singlet portal.

Scope:
- Original one-doublet/one-complex-singlet U(1)_X model with the two VLLs.
- Diagonal Abelian gauge kinetic terms at the common matching scale.
- Full one-loop MS beta expression, plus the lambda_HS=O(hbar) truncation.
- Exact checks of the mixed VLL fermion-box UV pole and Tr(Y X).

This is the UV beta above the common VLL threshold M_E. It is not the EFT
beta below M_E, nor the full UV-EFT matching-scale cancellation.
"""
from math import pi, sqrt
import sympy as sp

ME = 20_000.0
VH = 246.22
MH = 125.25
THETA_L = 1.0e-2
M_MU = 0.1056583755
M_TAU = 1.77686

BENCHMARKS = {
    "A": {"vS": 70.886458, "mX": 10.0, "lambdaHS_UV": 0.210763976387},
    "B": {"vS": 315.0, "mX": 63.0, "lambdaHS_UV": 0.0106733764886},
}


def symbolic_checks():
    h, s, y, lam, M = sp.symbols("h s y lam M", real=True)
    mass = sp.Matrix([[0, y*h/sp.sqrt(2)], [lam*s/sp.sqrt(2), M]])
    tr_m4 = sp.expand(sp.trace((mass.T*mass)*(mass.T*mass)))
    mixed_h2s2 = sp.expand(tr_m4).coeff(h, 2).coeff(s, 2)
    assert mixed_h2s2 == 0

    lHS, lH, lS = sp.symbols("lHS lH lS", real=True)
    scalar_residue = lHS*(6*lH + 2*lHS + 4*lS)
    beta_scalar = sp.simplify(2*scalar_residue)
    expected_scalar = lHS*(12*lH + 4*lHS + 8*lS)
    assert sp.simplify(beta_scalar-expected_scalar) == 0

    g2, gY, gX = sp.symbols("g2 gY gX", real=True)
    casimir_H_SU2 = sp.Rational(3, 4)
    hypercharge_H_sq = sp.Rational(1, 4)
    xcharge_S_sq = sp.Integer(4)  # Q_S = 2 in the g_X convention
    beta_gauge = sp.simplify(
        -6*(casimir_H_SU2*g2**2 + hypercharge_H_sq*gY**2
            + xcharge_S_sq*gX**2)
    )
    expected_gauge = (
        -sp.Rational(9, 2)*g2**2
        -sp.Rational(3, 2)*gY**2
        -24*gX**2
    )
    assert sp.simplify(beta_gauge-expected_gauge) == 0

    # Left-handed Weyl fields, including SU(2) multiplicities.
    reps = [
        ("L_mu", 2, sp.Rational(-1, 2), 1),
        ("mu_Rc", 1, 1, 1),
        ("L_tau", 2, sp.Rational(-1, 2), -1),
        ("tau_Rc", 1, 1, -1),
        ("E_muL", 1, -1, 1),
        ("E_muRc", 1, 1, -1),
        ("E_tauL", 1, -1, -1),
        ("E_tauRc", 1, 1, 1),
    ]
    trace_YX = sp.simplify(
        sum(mult*Y*X for _, mult, Y, X in reps)
    )
    assert trace_YX == 0

    return {
        "mixed_h2s2_fermion_trace": str(mixed_h2s2),
        "scalar_beta": sp.sstr(beta_scalar),
        "gauge_beta_coefficient": sp.sstr(beta_gauge),
        "Tr_YX": str(trace_YX),
        "checks": 4,
    }


def benchmark_rows():
    lamH = MH**2/(2*VH**2)
    y = sqrt(2)*ME*THETA_L/VH
    rows = []
    for name, p in BENCHMARKS.items():
        vs = p["vS"]
        gx = p["mX"]/(2*vs)
        lamHS = p["lambdaHS_UV"]
        lam_mu = sqrt(2)*M_MU/(THETA_L*vs)
        lam_tau = sqrt(2)*M_TAU/(THETA_L*vs)

        T_H_VLL = 2*y**2
        T_S_VLL = lam_mu**2 + lam_tau**2
        C_Y_VLL = 2*(T_H_VLL + T_S_VLL)
        C_X = 24*gx**2

        for ms in (10.0, 50.0, 100.0, 125.25, 150.0):
            # Leading unmixed radial-mass relation; not a near-degenerate
            # mass-eigenstate inversion.
            lamS = ms**2/(2*vs**2)
            C_scalar = 12*lamH + 8*lamS
            beta_scalar = lamHS*C_scalar/(16*pi**2)
            beta_vll_yuk = lamHS*C_Y_VLL/(16*pi**2)
            beta_x_gauge = -lamHS*C_X/(16*pi**2)
            beta_portal2 = lamHS*(4*lamHS)/(16*pi**2)
            beta_known_full = (
                beta_scalar + beta_vll_yuk + beta_x_gauge + beta_portal2
            )
            beta_known_combined = beta_known_full - beta_portal2

            rows.append({
                "benchmark": name,
                "ms": ms,
                "lambdaS": lamS,
                "lambdaH": lamH,
                "lambdaHS_UV": lamHS,
                "y": y,
                "lambda_mu": lam_mu,
                "lambda_tau": lam_tau,
                "gX": gx,
                "T_H_VLL": T_H_VLL,
                "T_S_VLL": T_S_VLL,
                "C_scalar": C_scalar,
                "C_Y_VLL": C_Y_VLL,
                "C_X": C_X,
                "beta_scalar": beta_scalar,
                "beta_vll_yuk": beta_vll_yuk,
                "beta_x_gauge": beta_x_gauge,
                "beta_portal2": beta_portal2,
                "beta_known_full": beta_known_full,
                "beta_known_combined": beta_known_combined,
                "D_SM_coefficient": lamHS/(16*pi**2),
            })
    return rows


def main():
    print("B5-1 one-loop UV Higgs-singlet portal beta audit")
    print("Inputs: M_E=20 TeV, v_h=246.22 GeV, m_h=125.25 GeV, theta_L=1e-2")

    print("\nSYMBOLIC CHECKS")
    for key, value in symbolic_checks().items():
        print(f"PASS {key}: {value}")

    print("\nFULL ONE-LOOP UV PORTAL BETA")
    print("16 pi^2 beta_lambdaHS = lambdaHS * [12 lambdaH + 8 lambdaS + 4 lambdaHS")
    print("  - (9/2) g2^2 - (3/2) gY^2 - 24 gX^2")
    print("  + 2*(T_SM + sum_l |y_l|^2 + sum_l |lambda_l|^2)]")
    print("The additive VLL mixed-box UV-pole coefficient is zero.")

    rows = benchmark_rows()
    print("\nBENCHMARK INPUTS AND DECOMPOSITION")
    for name in ("A", "B"):
        r = next(x for x in rows
                 if x["benchmark"] == name and x["ms"] == 125.25)
        print(f"\nBenchmark {name}:")
        for key in (
            "lambdaHS_UV", "y", "lambda_mu", "lambda_tau", "gX",
            "T_H_VLL", "T_S_VLL", "C_scalar", "C_Y_VLL", "C_X"
        ):
            print(f"  {key}={r[key]:.12g}")
        print("  beta pieces at m_s=125.25 GeV:")
        for key in (
            "beta_scalar", "beta_vll_yuk", "beta_x_gauge",
            "beta_portal2", "beta_known_full", "beta_known_combined",
            "D_SM_coefficient"
        ):
            print(f"    {key}={r[key]:+.12e}")

    print("\nMASS-RANGE TABLE")
    print("Columns: benchmark, ms, beta_scalar, beta_VLL_Yukawa, "
          "beta_U1X_gauge, beta_portal2, beta_known_full")
    for r in rows:
        print(
            f"{r['benchmark']} {r['ms']:6.2f} "
            f"{r['beta_scalar']:+.9e} {r['beta_vll_yuk']:+.9e} "
            f"{r['beta_x_gauge']:+.9e} {r['beta_portal2']:+.9e} "
            f"{r['beta_known_full']:+.9e}"
        )

    print("\nREMAINDER")
    print("beta_SM remainder = lambdaHS/(16 pi^2) * D_SM")
    print("D_SM = 2*[3 Tr(Yu^dag Yu)+3 Tr(Yd^dag Yd)+Tr(Ye^dag Ye)]")
    print("       -(9/2)g2^2-(3/2)gY^2")
    print("No numerical D_SM is inserted: running SM inputs at 20 TeV "
          "have not been fixed in this calculation.")

    print("\nCOMBINED-ORDER NOTE")
    print("Since lambdaHS^UV=O(hbar), the 4 lambdaHS^2 term in beta is "
          "O(hbar^3); drop beta_portal2 at retained O(hbar^2), but retain "
          "it in the full one-loop MS formula.")
    print("Benchmark A has lambda_tau=sqrt(4 pi), the perturbativity "
          "boundary; monitor higher-loop running.")
    print("LIMIT: UV beta above M_E only. EFT beta below M_E and full "
          "matching-scale cancellation remain separate tasks.")


if __name__ == "__main__":
    main()
