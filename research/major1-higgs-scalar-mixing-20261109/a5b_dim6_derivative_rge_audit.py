#!/usr/bin/env python3
"""A5b: restricted one-loop RGE audit for the VLL-induced h-s EFT sector.

This is deliberately a sector-level calculation:
  * C5 C5* soft bubble + contact tadpole -> derivative operator counterterm;
  * the corresponding inhomogeneous one-loop beta function;
  * exact cancellation of the hard/soft subtraction-scale logarithms;
  * the scalar-only portal beta contribution already derived in A3a;
  * absence of an additive |y|^2 |lambda|^2 UV portal pole in the one-loop
    VLL determinant, distinguished from its finite threshold.

It is NOT the complete model EFT anomalous-dimension matrix. Gauge/Yukawa
corrections to C5, Q_LD/Q_RD/current operators, full EOM/source closure,
and the complete O(hbar^2) portal beta function remain open.
"""
from math import log, pi
import sympy as sp

ME = 20_000.0
VH = 246.22
MH = 125.25
THETA_L = 1.0e-2
M_MU = 0.1056583755
M_TAU = 1.77686
BENCHMARKS = {
    "A": {"vS": 70.886458, "lambdaHS_UV": 0.210763976387},
    "B": {"vS": 315.0, "lambdaHS_UV": 0.0106733764886},
}

def symbolic_checks():
    q, C5sq, Mstar, vh, vs, eps = sp.symbols(
        "q C5sq Mstar vh vs eps", positive=True
    )
    piS = sp.pi
    q_relation = sp.Eq(q, C5sq * vh * vs / 2)
    delta_c_q = -Mstar**2 * q / (16 * piS**2 * vh * vs) / eps
    delta_c_C5 = -Mstar**2 * C5sq / (32 * piS**2) / eps
    assert sp.simplify(delta_c_q.subs(q, C5sq*vh*vs/2)-delta_c_C5) == 0

    # In d=4-2 eps, c_B = mu^(2 eps) [c + a/eps],
    # C5_B = mu^(2 eps) C5. Bare-scale independence gives beta_c=2a
    # at this one-loop order. Here a is the residue of delta c.
    a = -Mstar**2 * C5sq / (32 * piS**2)
    beta_c = sp.simplify(2*a)
    expected_beta = -Mstar**2 * C5sq / (16 * piS**2)
    assert sp.simplify(beta_c-expected_beta) == 0

    mu, ME_sym, x = sp.symbols("mu ME x", positive=True)
    c_hard = Mstar**2*C5sq/(32*piS**2) * (
        sp.log(ME_sym**2/mu**2) - sp.Rational(2,3)
    )
    d_hard = sp.simplify(mu*sp.diff(c_hard, mu))
    assert sp.simplify(d_hard-beta_c) == 0

    qsym = sp.symbols("q", positive=True)
    hard_prime = qsym/(16*piS**2) * (
        sp.log(ME_sym**2/mu**2)-sp.Rational(2,3)
    )
    soft_prime = qsym/(16*piS**2) * sp.log(mu**2/x)
    assert sp.simplify(mu*sp.diff(hard_prime+soft_prime,mu)) == 0

    # The UV VLL determinant has no mixed h^2 s^2 pole.
    h, s, y, lam, M = sp.symbols("h s y lam M", real=True)
    mass = sp.Matrix([[0, y*h/sp.sqrt(2)], [lam*s/sp.sqrt(2), M]])
    mm = mass.T*mass
    tr = sp.expand(sp.trace(mm*mm))
    mixed = sp.expand(tr).coeff(h,2).coeff(s,2)
    assert mixed == 0

    # Scalar-only portal pole from A3a; beta is twice the MS pole residue.
    lHS, lH, lS = sp.symbols("lHS lH lS")
    scalar_pole_residue = lHS*(6*lH+4*lS)/(16*piS**2)
    beta_lHS_scalar = sp.simplify(2*scalar_pole_residue)
    assert sp.simplify(
        beta_lHS_scalar-lHS*(12*lH+8*lS)/(16*piS**2)
    ) == 0

    return {
        "q_relation": sp.sstr(q_relation),
        "delta_c": sp.sstr(delta_c_C5),
        "beta_c": sp.sstr(beta_c),
        "hard_running": sp.sstr(d_hard),
        "hard_soft_scale_derivative": "0",
        "mixed_h2s2_trace_coefficient": str(mixed),
        "beta_lambdaHS_scalar_linear": sp.sstr(beta_lHS_scalar),
    }

def numeric_benchmarks():
    L = log(ME**2/MH**2)
    out = []
    for name, p in BENCHMARKS.items():
        vs = p["vS"]
        q_mu = 2*M_MU**2/(VH*vs)
        q_tau = 2*M_TAU**2/(VH*vs)
        qsum = q_mu+q_tau
        c5_mu = 2*M_MU/(VH*vs)
        c5_tau = 2*M_TAU/(VH*vs)
        beta_mu = -ME**2*c5_mu**2/(16*pi**2)
        beta_tau = -ME**2*c5_tau**2/(16*pi**2)
        beta = beta_mu+beta_tau

        delta_lambda = -sum(
            ( (2**0.5*ME*THETA_L/VH)
              * (2**0.5*m/(THETA_L*vs)) )**2
            for m in (M_MU, M_TAU)
        )/(8*pi**2)

        delta_c_running = beta*log(MH/ME)
        hard_log_shift = MH**2*qsum*L/(16*pi**2)
        assert abs(beta-delta_lambda/2) < 2e-12
        assert abs(
            delta_c_running*VH*vs/ME**2*MH**2-hard_log_shift
        ) < 2e-12

        out.append({
            "benchmark": name,
            "vS_GeV": vs,
            "q_mu": q_mu,
            "q_tau": q_tau,
            "beta_c_mu": beta_mu,
            "beta_c_tau": beta_tau,
            "beta_c_total": beta,
            "Delta_lambda_HS_VLL": delta_lambda,
            "beta_c_minus_DeltaLambda_over_2": beta-delta_lambda/2,
            "ln_ME2_over_mh2": L,
            "delta_c_ME_to_mh": delta_c_running,
            "leading_log_Pi_shift_GeV2": hard_log_shift,
            "lambdaHS_UV_boundary": p["lambdaHS_UV"],
        })
    return out

def scale_variation_diagnostic():
    """Vary the common subtraction/matching scale at fixed physical M_E."""
    rows = []
    for name, p in BENCHMARKS.items():
        vs = p["vS"]
        flavors = ((M_MU, 2*M_MU**2/(VH*vs)),
                   (M_TAU, 2*M_TAU**2/(VH*vs)))
        target = sum(
            q/(16*pi**2)*(log(ME**2/m**2)-2.0/3.0)
            for m, q in flavors
        )
        for muM in (ME/2.0, ME, 2.0*ME):
            hard = sum(
                q/(16*pi**2)*(log(ME**2/muM**2)-2.0/3.0)
                for _, q in flavors
            )
            soft = sum(
                q/(16*pi**2)*log(muM**2/m**2)
                for m, q in flavors
            )
            total = hard+soft
            assert abs(total-target) < 2e-16
            rows.append({
                "benchmark": name,
                "muM_GeV": muM,
                "hard_derivative": hard,
                "soft_derivative": soft,
                "sum_derivative": total,
                "reference_sum": target,
                "Pi_at_mh_GeV2": total*MH**2,
            })
    return rows

def scalar_portal_diagnostic():
    lamH = MH**2/(2*VH**2)
    rows = []
    for name, p in BENCHMARKS.items():
        vs = p["vS"]
        lamS = MH**2/(2*vs**2)  # explicitly m_s=m_h diagnostic only
        lamHS = p["lambdaHS_UV"]
        beta_linear = lamHS*(12*lamH+8*lamS)/(16*pi**2)
        beta_with_portal_squared = lamHS*(
            12*lamH+8*lamS+4*lamHS
        )/(16*pi**2)
        rows.append({
            "benchmark": name,
            "lambdaH": lamH,
            "lambdaS_ms_eq_mh": lamS,
            "beta_lambdaHS_scalar_linear": beta_linear,
            "beta_lambdaHS_scalar_including_portal_squared": beta_with_portal_squared,
        })
    return rows

def main():
    print("A5b restricted one-loop EFT RGE audit")
    print("\nSYMBOLIC CHECKS")
    for key, value in symbolic_checks().items():
        print(f"PASS {key}: {value}")

    print("\nDIMENSION-SIX DERIVATIVE OPERATOR")
    print("delta c_(dHS) = -M_*^2 sum_l |C5_l|^2 /(32 pi^2) * Delta_UV")
    print("beta c_(dHS)  = -M_*^2 sum_l |C5_l|^2 /(16 pi^2)")
    print("For M_*=M_E and C5_l=-y_l lambda_l/M_E:")
    print("beta c_(dHS)  = -sum_l |y_l|^2 |lambda_l|^2 /(16 pi^2)")
    print("              = Delta lambda_HS^VLL / 2 in this benchmark convention.")

    print("\nBENCHMARK NUMERICS")
    for row in numeric_benchmarks():
        print(
            f"{row['benchmark']}: q_mu={row['q_mu']:.12e}, "
            f"q_tau={row['q_tau']:.12e}"
        )
        print(
            f"  beta_c: mu={row['beta_c_mu']:+.12e}, "
            f"tau={row['beta_c_tau']:+.12e}, "
            f"sum={row['beta_c_total']:+.12e}"
        )
        print(
            f"  Delta lambda_HS^VLL={row['Delta_lambda_HS_VLL']:+.12e}; "
            f"beta_c-Delta_lambda/2={row['beta_c_minus_DeltaLambda_over_2']:+.3e}"
        )
        print(
            f"  ln(M_E^2/m_h^2)={row['ln_ME2_over_mh2']:.12f}; "
            f"delta c(20 TeV -> m_h)={row['delta_c_ME_to_mh']:+.12e}"
        )
        print(
            f"  leading-log self-energy shift at p^2=m_h^2="
            f"{row['leading_log_Pi_shift_GeV2']:+.12e} GeV^2"
        )

    print("\nFIXED-MASS FACTOR-TWO MATCHING/SUBTRACTION-SCALE DIAGNOSTIC")
    print("M_E is held fixed; hard and soft terms are evaluated at the same mu.")
    for row in scale_variation_diagnostic():
        print(
            f"{row['benchmark']} mu={row['muM_GeV']/1000.0:.1f} TeV: "
            f"hard={row['hard_derivative']:+.12e}, "
            f"soft={row['soft_derivative']:+.12e}, "
            f"sum={row['sum_derivative']:+.12e}, "
            f"Pi(m_h)={row['Pi_at_mh_GeV2']:+.12e} GeV^2"
        )

    print("\nSCALAR-ONLY PORTAL RUNNING DIAGNOSTIC")
    print("Illustrative m_s=m_h only; not the full portal beta function.")
    for row in scalar_portal_diagnostic():
        print(
            f"{row['benchmark']}: lambdaH={row['lambdaH']:.9f}, "
            f"lambdaS={row['lambdaS_ms_eq_mh']:.9f}, "
            f"beta_scalar_linear={row['beta_lambdaHS_scalar_linear']:+.12e}, "
            f"including portal^2={row['beta_lambdaHS_scalar_including_portal_squared']:+.12e}"
        )

    print("\nSCOPE LIMITS")
    print("OPEN: gauge/Yukawa pieces of beta_lambdaHS and beta_C5.")
    print("OPEN: Q_LD/Q_RD/current-operator anomalous dimensions and EOM/source closure.")
    print("OPEN: complete O(hbar^2) UV-EFT portal matching and all diagonal counterterms.")
    print("OPEN: dimension-eight hard matching; q_l*m_l^2 pole is O(M_E^-4), not beta_lambdaHS.")
    print("PASS: fixed-sector hard/soft subtraction-scale logarithms cancel analytically.")
    print("PASS: restricted C5*C5* contribution to beta_c_(dHS) is derived and benchmarked.")
    print("LIMIT: this is a restricted sector-level RGE result, not a complete model RGE.")

if __name__ == "__main__":
    main()
